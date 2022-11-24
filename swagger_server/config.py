#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author : microfat
# @time   : 11/24/22 09:03:56
# @File   : config.py

import datetime

from flask_apscheduler import APScheduler

scheduler = APScheduler()


class Config(object):
    JOBS = [
        {
            'id': 'job1',
            'func': 'module.test:task',
            'args': (1, 2),
            'trigger': 'interval',
            'seconds': 10,
            'start_date': datetime.datetime.now(),
        }
    ]
    SCHEDULER_API_ENABLED = True


# 接口ip、端口
# 测试用,正式的在nginx_server.conf中
bindIp = '0.0.0.0'
bindPort = 8000
