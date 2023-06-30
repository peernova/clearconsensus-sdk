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


class TitaniumDependency(object):
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
        'entity': 'str',
        'entity_name': 'str',
        'entity_type': 'str',
        'scope': 'str',
        'usages': 'list[TitaniumUsage]',
        'version': 'str'
    }

    attribute_map = {
        'entity': 'entity',
        'entity_name': 'entityName',
        'entity_type': 'entityType',
        'scope': 'scope',
        'usages': 'usages',
        'version': 'version'
    }

    def __init__(self, entity=None, entity_name=None, entity_type=None, scope=None, usages=None, version=None, local_vars_configuration=None):  # noqa: E501
        """TitaniumDependency - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._entity = None
        self._entity_name = None
        self._entity_type = None
        self._scope = None
        self._usages = None
        self._version = None
        self.discriminator = None

        if entity is not None:
            self.entity = entity
        if entity_name is not None:
            self.entity_name = entity_name
        if entity_type is not None:
            self.entity_type = entity_type
        if scope is not None:
            self.scope = scope
        if usages is not None:
            self.usages = usages
        if version is not None:
            self.version = version

    @property
    def entity(self):
        """Gets the entity of this TitaniumDependency.  # noqa: E501


        :return: The entity of this TitaniumDependency.  # noqa: E501
        :rtype: str
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """Sets the entity of this TitaniumDependency.


        :param entity: The entity of this TitaniumDependency.  # noqa: E501
        :type entity: str
        """

        self._entity = entity

    @property
    def entity_name(self):
        """Gets the entity_name of this TitaniumDependency.  # noqa: E501


        :return: The entity_name of this TitaniumDependency.  # noqa: E501
        :rtype: str
        """
        return self._entity_name

    @entity_name.setter
    def entity_name(self, entity_name):
        """Sets the entity_name of this TitaniumDependency.


        :param entity_name: The entity_name of this TitaniumDependency.  # noqa: E501
        :type entity_name: str
        """

        self._entity_name = entity_name

    @property
    def entity_type(self):
        """Gets the entity_type of this TitaniumDependency.  # noqa: E501


        :return: The entity_type of this TitaniumDependency.  # noqa: E501
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this TitaniumDependency.


        :param entity_type: The entity_type of this TitaniumDependency.  # noqa: E501
        :type entity_type: str
        """

        self._entity_type = entity_type

    @property
    def scope(self):
        """Gets the scope of this TitaniumDependency.  # noqa: E501


        :return: The scope of this TitaniumDependency.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this TitaniumDependency.


        :param scope: The scope of this TitaniumDependency.  # noqa: E501
        :type scope: str
        """

        self._scope = scope

    @property
    def usages(self):
        """Gets the usages of this TitaniumDependency.  # noqa: E501


        :return: The usages of this TitaniumDependency.  # noqa: E501
        :rtype: list[TitaniumUsage]
        """
        return self._usages

    @usages.setter
    def usages(self, usages):
        """Sets the usages of this TitaniumDependency.


        :param usages: The usages of this TitaniumDependency.  # noqa: E501
        :type usages: list[TitaniumUsage]
        """

        self._usages = usages

    @property
    def version(self):
        """Gets the version of this TitaniumDependency.  # noqa: E501


        :return: The version of this TitaniumDependency.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this TitaniumDependency.


        :param version: The version of this TitaniumDependency.  # noqa: E501
        :type version: str
        """

        self._version = version

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
        if not isinstance(other, TitaniumDependency):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TitaniumDependency):
            return True

        return self.to_dict() != other.to_dict()
