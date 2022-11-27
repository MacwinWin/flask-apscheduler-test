#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author : microfat
# @time   : 11/21/22 14:06:13
# @File   : test.py

from flask import Flask
import datetime
from flask_apscheduler import APScheduler

aps = APScheduler()


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
    SCHEDULER_TIMEZONE = 'Asia/Shanghai'


def task(a, b):
    print(
        str(datetime.datetime.now()) + ' execute task ' + '{}+{}={}'.format(a, b, a + b)
    )


if __name__ == '__main__':
    app = Flask(__name__)
    app.config.from_object(Config())

    scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.start()

    app.run(port=8000)
