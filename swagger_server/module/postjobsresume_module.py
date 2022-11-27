#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author : microfat
# @time   : 11/27/22 08:21:07
# @File   : postjobsresume_module.py

from flask import abort

from swagger_server import config


def main(job_id, required_body):

    try:
        config.scheduler.resume_job(job_id)
        response = {
            'success': True,
            'code': 200,
            'message': "成功恢复作业",
            'data': {},
        }
        return response
    except:
        abort(
            500,
            description={
                'success': False,
                'code': 5005,
                'message': "恢复作业失败",
                'data': None,
            },
        )
