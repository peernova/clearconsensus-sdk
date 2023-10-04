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


class TitaniumGetWorkflowActionResponse(object):
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
        'description': 'str',
        'input_arguments': 'list[str]',
        'output_argument': 'str'
    }

    attribute_map = {
        'description': 'description',
        'input_arguments': 'inputArguments',
        'output_argument': 'outputArgument'
    }

    def __init__(self, description=None, input_arguments=None, output_argument=None, local_vars_configuration=None):  # noqa: E501
        """TitaniumGetWorkflowActionResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._description = None
        self._input_arguments = None
        self._output_argument = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if input_arguments is not None:
            self.input_arguments = input_arguments
        if output_argument is not None:
            self.output_argument = output_argument

    @property
    def description(self):
        """Gets the description of this TitaniumGetWorkflowActionResponse.  # noqa: E501


        :return: The description of this TitaniumGetWorkflowActionResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TitaniumGetWorkflowActionResponse.


        :param description: The description of this TitaniumGetWorkflowActionResponse.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def input_arguments(self):
        """Gets the input_arguments of this TitaniumGetWorkflowActionResponse.  # noqa: E501


        :return: The input_arguments of this TitaniumGetWorkflowActionResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._input_arguments

    @input_arguments.setter
    def input_arguments(self, input_arguments):
        """Sets the input_arguments of this TitaniumGetWorkflowActionResponse.


        :param input_arguments: The input_arguments of this TitaniumGetWorkflowActionResponse.  # noqa: E501
        :type input_arguments: list[str]
        """

        self._input_arguments = input_arguments

    @property
    def output_argument(self):
        """Gets the output_argument of this TitaniumGetWorkflowActionResponse.  # noqa: E501


        :return: The output_argument of this TitaniumGetWorkflowActionResponse.  # noqa: E501
        :rtype: str
        """
        return self._output_argument

    @output_argument.setter
    def output_argument(self, output_argument):
        """Sets the output_argument of this TitaniumGetWorkflowActionResponse.


        :param output_argument: The output_argument of this TitaniumGetWorkflowActionResponse.  # noqa: E501
        :type output_argument: str
        """

        self._output_argument = output_argument

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
        if not isinstance(other, TitaniumGetWorkflowActionResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TitaniumGetWorkflowActionResponse):
            return True

        return self.to_dict() != other.to_dict()
