# -*- coding: utf-8 -*-

import logging

import pytest

LOGGER = logging.getLogger(__name__)
REQUIRED_PERCENT = 100


def pytest_addoption(parser):
    parser.addoption(
        '--required-percent',
        action='store',
        help='Percent of tests required to pass.',
    )


def pytest_configure(config):
    global REQUIRED_PERCENT
    required_percent = config.getoption('--required-percent')
    if required_percent:
        REQUIRED_PERCENT = float(required_percent)
    if REQUIRED_PERCENT <= 1.0:
        REQUIRED_PERCENT *= 100
    REQUIRED_PERCENT = int(REQUIRED_PERCENT)
    LOGGER.info(f'Required percent set to {REQUIRED_PERCENT}%')


@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session):
    if session.exitstatus > 0 and session.testsfailed > 0:
        testspassed = session.testscollected - session.testsfailed
        passed_percent = int((testspassed / session.testscollected) * 100)
        if passed_percent >= REQUIRED_PERCENT:
            LOGGER.info(f'{passed_percent}% of tests passed, required {REQUIRED_PERCENT}%.')
            session.exitstatus = pytest.ExitCode.OK
        else:
            LOGGER.error(f'{passed_percent}% of tests passed, required {REQUIRED_PERCENT}%.')


@pytest.fixture(scope='session')
def required_percent():
    return REQUIRED_PERCENT


__version__ = '0.0.4'
