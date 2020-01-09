## Requirements:

* [pytest v5.2.0 or newer](https://docs.pytest.org/en/latest/index.html)

## Installation:

    pip install pytest-percent

## About:

This plugin will change the exit code of pytest test sessions when a required percent of tests pass.

## Usage:

    pytest --required-percent=80

    =============================================================================================================================================== test session starts ===============================================================================================================================================
    platform win32 -- Python 3.8.0, pytest-5.3.1, py-1.8.0, pluggy-0.13.0
    rootdir: D:\Documents\pytest.percent, inifile: pytest.ini
    plugins: metadata-1.8.0, percent-0.0.2
    collected 5 items                                                                                                                                                                                                                                                                                                  
    
    tests/test_percent.py::test_one PASSED                                                                                                                                                                                                                                                                       [ 20%]
    tests/test_percent.py::test_two PASSED                                                                                                                                                                                                                                                                       [ 40%]
    tests/test_percent.py::test_three PASSED                                                                                                                                                                                                                                                                     [ 60%]
    tests/test_percent.py::test_four PASSED                                                                                                                                                                                                                                                                      [ 80%]
    tests/test_percent.py::test_five FAILED                                                                                                                                                                                                                                                                      [100%]
    --------------------------------------------------------------------------------------------------------------------------------------------- live log sessionfinish ----------------------------------------------------------------------------------------------------------------------------------------------
    INFO     pytest_percent:pytest_percent.py:35 80% of tests passed, required 80%.
    
    
    ================================== FAILURES ===================================
    __________________________________ test_five __________________________________
    
        def test_five():
    >       assert False
    E       assert False
    
    tests\test_percent.py:18: AssertionError
    ========================= 1 failed, 4 passed in 0.10s =========================
    
    D:\Documents\pytest.percent>echo %errorLevel%
    0

## Issues

If you encounter any problems, please file an issue along with a detailed description.

## License:

[MIT License](https://github.com/dillonm197/pytest.percent/blob/master/LICENSE)