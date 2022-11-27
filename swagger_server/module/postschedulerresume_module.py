#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author : microfat
# @time   : 11/27/22 08:21:32
# @File   : postschedulerresume_module.py

from flask import abort

from swagger_server import config


def main(required_body):

    try:
        config.scheduler.resume()
        response = {
            'success': True,
            'code': 200,
            'message': "成功恢复调度器",
            'data': {},
        }
        return response
    except:
        abort(
            500,
            description={
                'success': False,
                'code': 5008,
                'message': "恢复调度器失败",
                'data': None,
            },
        )
