# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.any_ofpatchjobsrequestbody_job_args_items import AnyOfpatchjobsrequestbodyJobArgsItems  # noqa: F401,E501
from swagger_server import util


class PatchjobsrequestbodyJob(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, func: str=None, args: List[AnyOfpatchjobsrequestbodyJobArgsItems]=None, trigger: str=None):  # noqa: E501
        """PatchjobsrequestbodyJob - a model defined in Swagger

        :param func: The func of this PatchjobsrequestbodyJob.  # noqa: E501
        :type func: str
        :param args: The args of this PatchjobsrequestbodyJob.  # noqa: E501
        :type args: List[AnyOfpatchjobsrequestbodyJobArgsItems]
        :param trigger: The trigger of this PatchjobsrequestbodyJob.  # noqa: E501
        :type trigger: str
        """
        self.swagger_types = {
            'func': str,
            'args': List[AnyOfpatchjobsrequestbodyJobArgsItems],
            'trigger': str
        }

        self.attribute_map = {
            'func': 'func',
            'args': 'args',
            'trigger': 'trigger'
        }
        self._func = func
        self._args = args
        self._trigger = trigger

    @classmethod
    def from_dict(cls, dikt) -> 'PatchjobsrequestbodyJob':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The patchjobsrequestbody_job of this PatchjobsrequestbodyJob.  # noqa: E501
        :rtype: PatchjobsrequestbodyJob
        """
        return util.deserialize_model(dikt, cls)

    @property
    def func(self) -> str:
        """Gets the func of this PatchjobsrequestbodyJob.

        作业函数  # noqa: E501

        :return: The func of this PatchjobsrequestbodyJob.
        :rtype: str
        """
        return self._func

    @func.setter
    def func(self, func: str):
        """Sets the func of this PatchjobsrequestbodyJob.

        作业函数  # noqa: E501

        :param func: The func of this PatchjobsrequestbodyJob.
        :type func: str
        """
        if func is None:
            raise ValueError("Invalid value for `func`, must not be `None`")  # noqa: E501

        self._func = func

    @property
    def args(self) -> List[AnyOfpatchjobsrequestbodyJobArgsItems]:
        """Gets the args of this PatchjobsrequestbodyJob.

        参数列表  # noqa: E501

        :return: The args of this PatchjobsrequestbodyJob.
        :rtype: List[AnyOfpatchjobsrequestbodyJobArgsItems]
        """
        return self._args

    @args.setter
    def args(self, args: List[AnyOfpatchjobsrequestbodyJobArgsItems]):
        """Sets the args of this PatchjobsrequestbodyJob.

        参数列表  # noqa: E501

        :param args: The args of this PatchjobsrequestbodyJob.
        :type args: List[AnyOfpatchjobsrequestbodyJobArgsItems]
        """
        if args is None:
            raise ValueError("Invalid value for `args`, must not be `None`")  # noqa: E501

        self._args = args

    @property
    def trigger(self) -> str:
        """Gets the trigger of this PatchjobsrequestbodyJob.

        触发方式  # noqa: E501

        :return: The trigger of this PatchjobsrequestbodyJob.
        :rtype: str
        """
        return self._trigger

    @trigger.setter
    def trigger(self, trigger: str):
        """Sets the trigger of this PatchjobsrequestbodyJob.

        触发方式  # noqa: E501

        :param trigger: The trigger of this PatchjobsrequestbodyJob.
        :type trigger: str
        """
        if trigger is None:
            raise ValueError("Invalid value for `trigger`, must not be `None`")  # noqa: E501

        self._trigger = trigger