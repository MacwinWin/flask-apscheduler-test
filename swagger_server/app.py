#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author : microfat
# @time   : 11/24/22 09:03:49
# @File   : app.py

import sys
import os

sys.path.insert(1, os.getcwd())
sys.path.insert(1, os.getcwd() + '/swagger_server')

import connexion
from swagger_server import encoder

import config


app = connexion.App(__name__, specification_dir='./swagger/')

app.app.json_encoder = encoder.JSONEncoder
app.app.config.from_object(config.Config())

app.add_api(
    'swagger.yaml', arguments={'title': 'flask-apscheduler-test'}, pythonic_params=True
)

config.scheduler.init_app(app.app)
config.scheduler.start()

if __name__ == '__main__':
    ip = config.bindIp
    port = config.bindPort
    app.run(host=ip, port=port)
