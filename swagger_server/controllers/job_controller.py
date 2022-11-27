import connexion

from flask import jsonify

from swagger_server.models.jobs_requestbody import JobsRequestbody  # noqa: E501
from swagger_server.models.patch_jobs_requestbody import (
    PatchJobsRequestbody,
)  # noqa: E501
from swagger_server.models.post_jobs_requestbody import (
    PostJobsRequestbody,
)  # noqa: E501
from swagger_server.module import patchjobs_module
from swagger_server.module import postjobs_module
from swagger_server.module import postjobspause_module
from swagger_server.module import postjobsremove_module
from swagger_server.module import postjobsresume_module
from swagger_server.module import postjobsrun_module


def patch_jobs(job_id, body=None):  # noqa: E501
    """更新作业

    更新作业 # noqa: E501

    :param job_id: 任务ID
    :type job_id: str
    :param body:
    :type body: dict | bytes
    """
    if connexion.request.is_json:
        required_body = PatchJobsRequestbody.from_dict(
            connexion.request.get_json()
        ).to_dict()  # noqa: E501
        res = patchjobs_module.main(job_id, required_body)
        res = jsonify(res)
        return res


def post_jobs(body=None):  # noqa: E501
    """添加作业

    添加作业 # noqa: E501

    :param body:
    :type body: dict | bytes
    """
    if connexion.request.is_json:
        required_body = PostJobsRequestbody.from_dict(
            connexion.request.get_json()
        ).to_dict()  # noqa: E501
        res = postjobs_module.main(required_body)
        res = jsonify(res)
        return res


def post_jobs_pause(job_id, body=None):  # noqa: E501
    """暂停某个作业

    暂停某个作业 # noqa: E501

    :param job_id: 任务ID
    :type job_id: str
    :param body:
    :type body: dict | bytes
    """
    if connexion.request.is_json:
        required_body = JobsRequestbody.from_dict(
            connexion.request.get_json()
        ).to_dict()  # noqa: E501
        res = postjobspause_module.main(job_id, required_body)
        res = jsonify(res)
        return res


def post_jobs_remove(job_id, body=None):  # noqa: E501
    """删除作业

    删除作业 # noqa: E501

    :param job_id: 任务ID
    :type job_id: str
    :param body:
    :type body: dict | bytes
    """
    if connexion.request.is_json:
        required_body = JobsRequestbody.from_dict(
            connexion.request.get_json()
        ).to_dict()  # noqa: E501
        res = postjobsremove_module.main(job_id, required_body)
        res = jsonify(res)
        return res


def post_jobs_resume(job_id, body=None):  # noqa: E501
    """恢复某个作业

    恢复某个作业 # noqa: E501

    :param job_id: 任务ID
    :type job_id: str
    :param body:
    :type body: dict | bytes
    """
    if connexion.request.is_json:
        required_body = JobsRequestbody.from_dict(
            connexion.request.get_json()
        ).to_dict()  # noqa: E501
        res = postjobsresume_module.main(job_id, required_body)
        res = jsonify(res)
        return res


def post_jobs_run(job_id, body=None):  # noqa: E501
    """执行某个作业

    执行某个作业 # noqa: E501

    :param job_id: 任务ID
    :type job_id: str
    :param body:
    :type body: dict | bytes
    """
    if connexion.request.is_json:
        required_body = JobsRequestbody.from_dict(
            connexion.request.get_json()
        ).to_dict()  # noqa: E501
        res = postjobsrun_module.main(job_id, required_body)
        res = jsonify(res)
        return res
