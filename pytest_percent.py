# -*- coding: utf-8 -*-

import logging

import pytest

LOGGER = logging.getLogger(__name__)


def pytest_addoption(parser):
    parser.addoption(
        '--required-percent',
        action='store',
        type=int,
        choices=range(101),
        help='Percent of tests required to pass.',
    )


@pytest.mark.trylast
def pytest_sessionfinish(session, exitstatus):
    required_percent = session.config.getoption('--required-percent')
    if isinstance(required_percent, int):
        passed_percent = 100 - ((session.testsfailed * 100) / session.testscollected)
        if passed_percent >= required_percent:
            LOGGER.info(f'{passed_percent}% of tests passed, required {required_percent}%.')
            exitstatus = pytest.ExitCode.OK
        else:
            LOGGER.error(f'{passed_percent}% of tests passed, required {required_percent}%.')


__version__ = '0.0.1'