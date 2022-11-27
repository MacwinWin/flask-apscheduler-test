# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class PostschedulerrequestbodyLog(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, app_id: str=None, entry_id: str=None, data_id: str=None):  # noqa: E501
        """PostschedulerrequestbodyLog - a model defined in Swagger

        :param app_id: The app_id of this PostschedulerrequestbodyLog.  # noqa: E501
        :type app_id: str
        :param entry_id: The entry_id of this PostschedulerrequestbodyLog.  # noqa: E501
        :type entry_id: str
        :param data_id: The data_id of this PostschedulerrequestbodyLog.  # noqa: E501
        :type data_id: str
        """
        self.swagger_types = {
            'app_id': str,
            'entry_id': str,
            'data_id': str
        }

        self.attribute_map = {
            'app_id': 'appId',
            'entry_id': 'entryId',
            'data_id': 'dataId'
        }
        self._app_id = app_id
        self._entry_id = entry_id
        self._data_id = data_id

    @classmethod
    def from_dict(cls, dikt) -> 'PostschedulerrequestbodyLog':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The postschedulerrequestbody_log of this PostschedulerrequestbodyLog.  # noqa: E501
        :rtype: PostschedulerrequestbodyLog
        """
        return util.deserialize_model(dikt, cls)

    @property
    def app_id(self) -> str:
        """Gets the app_id of this PostschedulerrequestbodyLog.

        应用ID  # noqa: E501

        :return: The app_id of this PostschedulerrequestbodyLog.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id: str):
        """Sets the app_id of this PostschedulerrequestbodyLog.

        应用ID  # noqa: E501

        :param app_id: The app_id of this PostschedulerrequestbodyLog.
        :type app_id: str
        """
        if app_id is None:
            raise ValueError("Invalid value for `app_id`, must not be `None`")  # noqa: E501

        self._app_id = app_id

    @property
    def entry_id(self) -> str:
        """Gets the entry_id of this PostschedulerrequestbodyLog.

        表单ID  # noqa: E501

        :return: The entry_id of this PostschedulerrequestbodyLog.
        :rtype: str
        """
        return self._entry_id

    @entry_id.setter
    def entry_id(self, entry_id: str):
        """Sets the entry_id of this PostschedulerrequestbodyLog.

        表单ID  # noqa: E501

        :param entry_id: The entry_id of this PostschedulerrequestbodyLog.
        :type entry_id: str
        """
        if entry_id is None:
            raise ValueError("Invalid value for `entry_id`, must not be `None`")  # noqa: E501

        self._entry_id = entry_id

    @property
    def data_id(self) -> str:
        """Gets the data_id of this PostschedulerrequestbodyLog.

        数据ID  # noqa: E501

        :return: The data_id of this PostschedulerrequestbodyLog.
        :rtype: str
        """
        return self._data_id

    @data_id.setter
    def data_id(self, data_id: str):
        """Sets the data_id of this PostschedulerrequestbodyLog.

        数据ID  # noqa: E501

        :param data_id: The data_id of this PostschedulerrequestbodyLog.
        :type data_id: str
        """
        if data_id is None:
            raise ValueError("Invalid value for `data_id`, must not be `None`")  # noqa: E501

        self._data_id = data_id
