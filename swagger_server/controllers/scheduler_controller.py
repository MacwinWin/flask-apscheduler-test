import connexion

from flask import jsonify

from swagger_server.models.post_scheduler_requestbody import (
    PostSchedulerRequestbody,
)  # noqa: E501

from swagger_server.module import postschedulerpause_module
from swagger_server.module import postschedulerresume_module


def post_scheduler_pause(body=None):  # noqa: E501
    """暂停调度器

    暂停调度器 # noqa: E501

    :param body:
    :type body: dict | bytes
    """
    if connexion.request.is_json:
        required_body = PostSchedulerRequestbody.from_dict(
            connexion.request.get_json()
        ).to_dict()  # noqa: E501
        res = postschedulerpause_module.main(required_body)
        res = jsonify(res)
        return res


def post_scheduler_resume(body=None):  # noqa: E501
    """恢复调度器

    恢复调度器 # noqa: E501

    :param body:
    :type body: dict | bytes
    """
    if connexion.request.is_json:
        required_body = PostSchedulerRequestbody.from_dict(
            connexion.request.get_json()
        ).to_dict()  # noqa: E501
        res = postschedulerresume_module.main(required_body)
        res = jsonify(res)
        return res
