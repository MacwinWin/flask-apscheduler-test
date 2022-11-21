#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author : microfat
# @time   : 11/20/22 20:09:06
# @File   : app.py

import datetime
import sys
from flask import jsonify
import json
import os

sys.path.insert(1, os.getcwd())
sys.path.insert(1, os.getcwd() + '/swagger_server')

import connexion
from swagger_server import encoder
import werkzeug
from flask_apscheduler import APScheduler

import config

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


def task(a, b):
    print(
        str(datetime.datetime.now()) + ' execute task ' + '{}+{}={}'.format(a, b, a + b)
    )


app = connexion.App(__name__, specification_dir='./swagger/')

app.app.json_encoder = encoder.JSONEncoder
app.app.config.from_object(Config())

# internal server error不上传sentry
def before_send(event, hint):
    if isinstance(hint['exc_info'][1], werkzeug.exceptions.InternalServerError):
        return None
    else:
        return event


app.add_api(
    'swagger.yaml', arguments={'title': 'flask-apscheduler-test'}, pythonic_params=True
)

scheduler = APScheduler()
scheduler.init_app(app.app)
scheduler.start()

if __name__ == '__main__':
    ip = config.bindIp
    port = config.bindPort
    app.run(host=ip, port=port)
