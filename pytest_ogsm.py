#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/11/10 3:29 PM
# @Author  : cw
def pytest_addoption(parser):
    parser.addoption(
        "--change",
        action="store",
        default="off",
        help="'Default 'off' for change, option: on or off"
    )


def pytest_report_teststatus(report, config):
    """turn . into √，turn F into x, turn E into 0"""
    if report.when == 'call' and report.failed:
        return report.outcome, 'x', 'failed'
    if report.when == 'call' and report.passed:
        return report.outcome, 'Y', 'passed'

