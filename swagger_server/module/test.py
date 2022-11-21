#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author : microfat
# @time   : 11/21/22 14:03:38
# @File   : test.py

import datetime


def task(a, b):
    print(
        str(datetime.datetime.now()) + ' execute task ' + '{}+{}={}'.format(a, b, a + b)
    )
