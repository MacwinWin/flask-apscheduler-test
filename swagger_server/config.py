#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author : microfat
# @time   : 11/20/22 20:18:03
# @File   : config.py


class Config(object):
    JOBS = [
        {
            'id': 'job1',
            'func': 'test:task',
            'args': (1, 2),
            'trigger': 'interval',
            'seconds': 10,
        }
    ]
    SCHEDULER_API_ENABLED = True


# 接口ip、端口
# 测试用,正式的在nginx_server.conf中
bindIp = '0.0.0.0'
bindPort = 8000
