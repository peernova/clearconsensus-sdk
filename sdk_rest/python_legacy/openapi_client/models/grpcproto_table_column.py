# coding: utf-8

"""
    clearconsensus-sdk

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from openapi_client.configuration import Configuration


class GrpcprotoTableColumn(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'column_db_type': 'str',
        'column_name': 'str',
        'column_type': 'str',
        'raw_column_name': 'str'
    }

    attribute_map = {
        'column_db_type': 'columnDbType',
        'column_name': 'columnName',
        'column_type': 'columnType',
        'raw_column_name': 'rawColumnName'
    }

    def __init__(self, column_db_type=None, column_name=None, column_type=None, raw_column_name=None, local_vars_configuration=None):  # noqa: E501
        """GrpcprotoTableColumn - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._column_db_type = None
        self._column_name = None
        self._column_type = None
        self._raw_column_name = None
        self.discriminator = None

        if column_db_type is not None:
            self.column_db_type = column_db_type
        if column_name is not None:
            self.column_name = column_name
        if column_type is not None:
            self.column_type = column_type
        if raw_column_name is not None:
            self.raw_column_name = raw_column_name

    @property
    def column_db_type(self):
        """Gets the column_db_type of this GrpcprotoTableColumn.  # noqa: E501


        :return: The column_db_type of this GrpcprotoTableColumn.  # noqa: E501
        :rtype: str
        """
        return self._column_db_type

    @column_db_type.setter
    def column_db_type(self, column_db_type):
        """Sets the column_db_type of this GrpcprotoTableColumn.


        :param column_db_type: The column_db_type of this GrpcprotoTableColumn.  # noqa: E501
        :type column_db_type: str
        """

        self._column_db_type = column_db_type

    @property
    def column_name(self):
        """Gets the column_name of this GrpcprotoTableColumn.  # noqa: E501


        :return: The column_name of this GrpcprotoTableColumn.  # noqa: E501
        :rtype: str
        """
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        """Sets the column_name of this GrpcprotoTableColumn.


        :param column_name: The column_name of this GrpcprotoTableColumn.  # noqa: E501
        :type column_name: str
        """

        self._column_name = column_name

    @property
    def column_type(self):
        """Gets the column_type of this GrpcprotoTableColumn.  # noqa: E501


        :return: The column_type of this GrpcprotoTableColumn.  # noqa: E501
        :rtype: str
        """
        return self._column_type

    @column_type.setter
    def column_type(self, column_type):
        """Sets the column_type of this GrpcprotoTableColumn.


        :param column_type: The column_type of this GrpcprotoTableColumn.  # noqa: E501
        :type column_type: str
        """

        self._column_type = column_type

    @property
    def raw_column_name(self):
        """Gets the raw_column_name of this GrpcprotoTableColumn.  # noqa: E501


        :return: The raw_column_name of this GrpcprotoTableColumn.  # noqa: E501
        :rtype: str
        """
        return self._raw_column_name

    @raw_column_name.setter
    def raw_column_name(self, raw_column_name):
        """Sets the raw_column_name of this GrpcprotoTableColumn.


        :param raw_column_name: The raw_column_name of this GrpcprotoTableColumn.  # noqa: E501
        :type raw_column_name: str
        """

        self._raw_column_name = raw_column_name

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GrpcprotoTableColumn):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GrpcprotoTableColumn):
            return True

        return self.to_dict() != other.to_dict()
