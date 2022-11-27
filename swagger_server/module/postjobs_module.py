#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author : microfat
# @time   : 11/26/22 22:37:26
# @File   : postjobs_module.py

import connexion
from flask import abort

from swagger_server import config


def main(required_body):

    try:
        print(connexion.request.get_json()['job'])
        config.scheduler.add_job(**connexion.request.get_json()['job'])
        response = {
            'success': True,
            'code': 200,
            'message': "成功新增作业",
            'data': {},
        }
        return response
    except:
        abort(
            500,
            description={
                'success': False,
                'code': 5001,
                'message': "新增作业失败",
                'data': None,
            },
        )
