# -*- coding: utf-8 -*-

import logging

import pytest

LOGGER = logging.getLogger(__name__)


def pytest_addoption(parser):
    parser.addoption(
        '--required-percent',
        action='store',
        type=int,
        choices=range(0, 101),
        dest='percent',
        help='Percent of tests required to pass.',
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
        if exitstatus == pytest.ExitCode.TESTS_FAILED and session.testsfailed > 0:
            passed_percent = 100 - int((session.testsfailed / session.testscollected) * 100)
            if passed_percent >= self.required_percent:
                LOGGER.info(f'{passed_percent}% of the {self.required_percent}% of required tests passed.')
                session.exitstatus = pytest.ExitCode.OK
            else:
                LOGGER.error(f'{passed_percent}% of the {self.required_percent}% of required tests passed.')


__version__ = '0.1.0'
