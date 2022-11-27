# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.postschedulerrequestbody_log import PostschedulerrequestbodyLog  # noqa: F401,E501
from swagger_server import util


class JobsRequestbody(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, log: PostschedulerrequestbodyLog=None):  # noqa: E501
        """JobsRequestbody - a model defined in Swagger

        :param log: The log of this JobsRequestbody.  # noqa: E501
        :type log: PostschedulerrequestbodyLog
        """
        self.swagger_types = {
            'log': PostschedulerrequestbodyLog
        }

        self.attribute_map = {
            'log': 'log'
        }
        self._log = log

    @classmethod
    def from_dict(cls, dikt) -> 'JobsRequestbody':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The jobs-requestbody of this JobsRequestbody.  # noqa: E501
        :rtype: JobsRequestbody
        """
        return util.deserialize_model(dikt, cls)

    @property
    def log(self) -> PostschedulerrequestbodyLog:
        """Gets the log of this JobsRequestbody.


        :return: The log of this JobsRequestbody.
        :rtype: PostschedulerrequestbodyLog
        """
        return self._log

    @log.setter
    def log(self, log: PostschedulerrequestbodyLog):
        """Sets the log of this JobsRequestbody.


        :param log: The log of this JobsRequestbody.
        :type log: PostschedulerrequestbodyLog
        """
        if log is None:
            raise ValueError("Invalid value for `log`, must not be `None`")  # noqa: E501

        self._log = log
