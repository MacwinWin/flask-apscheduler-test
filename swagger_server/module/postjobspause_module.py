#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author : microfat
# @time   : 11/27/22 08:20:39
# @File   : postjobspause_module.py

from flask import abort

from swagger_server import config


def main(job_id, required_body):

    try:
        config.scheduler.pause_job(job_id)
        response = {
            'success': True,
            'code': 200,
            'message': "成功暂停作业",
            'data': {},
        }
        return response
    except:
        abort(
            500,
            description={
                'success': False,
                'code': 5003,
                'message': "暂停作业失败",
                'data': None,
            },
        )
