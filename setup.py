#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/11/10 3:29 PM
# @Author  : cw
from setuptools import setup

setup(
    name='pytest_ogsm_plugin',
    url='https://github.com/cw010/pytest_ogsm_plugin',
    version='1.0',
    author="cw",
    author_email='cwalk.t@gmail.com',
    description='pytest终端输出中的. F，以✔、×代替',
    long_description='pytest终端输出中的. F，以✔、×代替',
    classifiers=[
        'Framework :: Pytest',
        'Programming Language :: Python',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python :: 3.9',
    ],
    license='proprietary',
    py_modules=['pytest_ogsm'],
    keywords=[
        'pytest', 'py.test', 'pytest_ogsm_plugin',
    ],

    install_requires=[
        'pytest'
    ],
    entry_points={
        'pytest11': [
            'ogsm_plugin = pytest_ogsm',
        ]
    }
)
