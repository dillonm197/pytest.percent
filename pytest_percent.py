# -*- coding: utf-8 -*-

import logging

import pytest

LOGGER = logging.getLogger(__name__)


def pytest_addoption(parser):
    parser.addoption(
        '--required-percent',
        action='store',
        type=int,
        dest='percent',
        help='Percent of tests required to pass. (0/100)',
    )


def pytest_configure(config):
    if config.option.percent:
        config._percent = PercentPlugin(config.option.percent)
        config.pluginmanager.register(config._percent)


def pytest_unconfigure(config):
    percent = getattr(config, '_percent', None)
    if percent:
        del config._percent
        config.pluginmanager.unregister(percent)


@pytest.fixture(scope='session')
def required_percent(pytestconfig):
    percent = getattr(pytestconfig, '_percent', None)
    if percent:
        return percent.required_percent


class PercentPlugin:
    def __init__(self, required_percent=100):
        if not isinstance(required_percent, int) or not 0 <= required_percent <= 100:
            raise ValueError('required_percent must be an integer [0, 100]')
        self.required_percent = required_percent
        LOGGER.info(f'Required percent set to {self.required_percent * 100}%')

    @pytest.hookimpl(trylast=True)
    def pytest_sessionfinish(self, session, exitstatus):
        stats = session.config.pluginmanager.get_plugin('terminalreporter').stats
        # Using terminalreporter allows us to ignore tests marked with skip, xpass or xfail.
        num_passed = len(stats.get('passed') or [])
        num_failed = len(stats.get('failed') or [])
        num_tests = num_passed + num_failed
        if exitstatus == pytest.ExitCode.TESTS_FAILED and num_failed > 0:
            passed_percent = int((num_passed / num_tests) * 100)
            if passed_percent >= self.required_percent:
                LOGGER.info(f'{passed_percent}% of the {self.required_percent}% of required tests passed.')
                session.exitstatus = pytest.ExitCode.OK
            else:
                LOGGER.error(f'{passed_percent}% of the {self.required_percent}% of required tests passed.')


__version__ = '0.1.2'
