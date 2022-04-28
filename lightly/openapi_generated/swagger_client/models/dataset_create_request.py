# coding: utf-8

"""
    Lightly API

    Lightly.ai enables you to do self-supervised learning in an easy and intuitive way. The lightly.ai OpenAPI spec defines how one can interact with our REST API to unleash the full potential of lightly.ai  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: support@lightly.ai
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from lightly.openapi_generated.swagger_client.configuration import Configuration


class DatasetCreateRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'DatasetName',
        'type': 'DatasetType',
        'img_type': 'ImageType',
        'parent_dataset_id': 'MongoObjectID'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'img_type': 'imgType',
        'parent_dataset_id': 'parentDatasetId'
    }

    def __init__(self, name=None, type=None, img_type=None, parent_dataset_id=None, _configuration=None):  # noqa: E501
        """DatasetCreateRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._type = None
        self._img_type = None
        self._parent_dataset_id = None
        self.discriminator = None

        self.name = name
        if type is not None:
            self.type = type
        if img_type is not None:
            self.img_type = img_type
        if parent_dataset_id is not None:
            self.parent_dataset_id = parent_dataset_id

    @property
    def name(self):
        """Gets the name of this DatasetCreateRequest.  # noqa: E501


        :return: The name of this DatasetCreateRequest.  # noqa: E501
        :rtype: DatasetName
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DatasetCreateRequest.


        :param name: The name of this DatasetCreateRequest.  # noqa: E501
        :type: DatasetName
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def type(self):
        """Gets the type of this DatasetCreateRequest.  # noqa: E501


        :return: The type of this DatasetCreateRequest.  # noqa: E501
        :rtype: DatasetType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DatasetCreateRequest.


        :param type: The type of this DatasetCreateRequest.  # noqa: E501
        :type: DatasetType
        """

        self._type = type

    @property
    def img_type(self):
        """Gets the img_type of this DatasetCreateRequest.  # noqa: E501


        :return: The img_type of this DatasetCreateRequest.  # noqa: E501
        :rtype: ImageType
        """
        return self._img_type

    @img_type.setter
    def img_type(self, img_type):
        """Sets the img_type of this DatasetCreateRequest.


        :param img_type: The img_type of this DatasetCreateRequest.  # noqa: E501
        :type: ImageType
        """

        self._img_type = img_type

    @property
    def parent_dataset_id(self):
        """Gets the parent_dataset_id of this DatasetCreateRequest.  # noqa: E501


        :return: The parent_dataset_id of this DatasetCreateRequest.  # noqa: E501
        :rtype: MongoObjectID
        """
        return self._parent_dataset_id

    @parent_dataset_id.setter
    def parent_dataset_id(self, parent_dataset_id):
        """Sets the parent_dataset_id of this DatasetCreateRequest.


        :param parent_dataset_id: The parent_dataset_id of this DatasetCreateRequest.  # noqa: E501
        :type: MongoObjectID
        """

        self._parent_dataset_id = parent_dataset_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(DatasetCreateRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DatasetCreateRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DatasetCreateRequest):
            return True

        return self.to_dict() != other.to_dict()