# -*- coding: utf-8 -*-

import setuptools

import pytest_percent

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='pytest-percent',
    version=pytest_percent.__version__,
    author='Dillon Miller',
    author_email='dillon.miller@swiftpage.com',
    maintainer='Dillon Miller',
    maintainer_email='dillon.miller@swiftpage.com',
    license='MIT',
    url='https://github.com/dillonm197/pytest.percent',
    description='Mark test sessions as successful based on a percentage of passed tests.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=['pytest_percent'],
    python_requires='>=3.7',
    install_requires=['pytest>=5.2.0'],
    classifiers=[
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'pytest11': [
            'pytest_percent = pytest_percent',
        ],
    },
)