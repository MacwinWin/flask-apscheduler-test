#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author : microfat
# @time   : 11/27/22 15:58:28
# @File   : config.py

import datetime

from flask_apscheduler import APScheduler

scheduler = APScheduler()


class Config(object):
    JOBS = [
        {
            'id': 'job1',
            'func': 'swagger_server.jobs.test:task',
            'args': (1, 2),
            'trigger': 'interval',
            'seconds': 10,
            'start_date': datetime.datetime.now(),
        }
    ]
    SCHEDULER_API_ENABLED = True
    SCHEDULER_TIMEZONE = 'Asia/Shanghai'


# 接口ip、端口
# 测试用,正式的在nginx_server.conf中
bindIp = '0.0.0.0'
bindPort = 8000
