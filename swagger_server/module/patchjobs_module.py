#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author : microfat
# @time   : 11/26/22 22:37:08
# @File   : patchjobs_module.py

import connexion
from flask import abort

from swagger_server import config


def main(job_id, required_body):

    try:
        config.scheduler.modify_job(job_id, **connexion.request.get_json()['job'])
        response = {
            'success': True,
            'code': 200,
            'message': "成功更新作业",
            'data': {},
        }
        return response
    except:
        abort(
            500,
            description={
                'success': False,
                'code': 5002,
                'message': "更新作业失败",
                'data': None,
            },
        )
