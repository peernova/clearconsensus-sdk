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


class TitaniumEvpAlignmentScore(object):
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
        'evp_alignment_dispersion_score': 'object',
        'evp_mid': 'object',
        'history': 'list[TitaniumEvpAlignmentScoreWithDate]',
        'score': 'object',
        'score_status': 'str',
        'submission_mean': 'object',
        'submission_std_dev': 'object'
    }

    attribute_map = {
        'evp_alignment_dispersion_score': 'evpAlignmentDispersionScore',
        'evp_mid': 'evpMid',
        'history': 'history',
        'score': 'score',
        'score_status': 'scoreStatus',
        'submission_mean': 'submissionMean',
        'submission_std_dev': 'submissionStdDev'
    }

    def __init__(self, evp_alignment_dispersion_score=None, evp_mid=None, history=None, score=None, score_status=None, submission_mean=None, submission_std_dev=None, local_vars_configuration=None):  # noqa: E501
        """TitaniumEvpAlignmentScore - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._evp_alignment_dispersion_score = None
        self._evp_mid = None
        self._history = None
        self._score = None
        self._score_status = None
        self._submission_mean = None
        self._submission_std_dev = None
        self.discriminator = None

        if evp_alignment_dispersion_score is not None:
            self.evp_alignment_dispersion_score = evp_alignment_dispersion_score
        if evp_mid is not None:
            self.evp_mid = evp_mid
        if history is not None:
            self.history = history
        if score is not None:
            self.score = score
        if score_status is not None:
            self.score_status = score_status
        if submission_mean is not None:
            self.submission_mean = submission_mean
        if submission_std_dev is not None:
            self.submission_std_dev = submission_std_dev

    @property
    def evp_alignment_dispersion_score(self):
        """Gets the evp_alignment_dispersion_score of this TitaniumEvpAlignmentScore.  # noqa: E501


        :return: The evp_alignment_dispersion_score of this TitaniumEvpAlignmentScore.  # noqa: E501
        :rtype: object
        """
        return self._evp_alignment_dispersion_score

    @evp_alignment_dispersion_score.setter
    def evp_alignment_dispersion_score(self, evp_alignment_dispersion_score):
        """Sets the evp_alignment_dispersion_score of this TitaniumEvpAlignmentScore.


        :param evp_alignment_dispersion_score: The evp_alignment_dispersion_score of this TitaniumEvpAlignmentScore.  # noqa: E501
        :type evp_alignment_dispersion_score: object
        """

        self._evp_alignment_dispersion_score = evp_alignment_dispersion_score

    @property
    def evp_mid(self):
        """Gets the evp_mid of this TitaniumEvpAlignmentScore.  # noqa: E501


        :return: The evp_mid of this TitaniumEvpAlignmentScore.  # noqa: E501
        :rtype: object
        """
        return self._evp_mid

    @evp_mid.setter
    def evp_mid(self, evp_mid):
        """Sets the evp_mid of this TitaniumEvpAlignmentScore.


        :param evp_mid: The evp_mid of this TitaniumEvpAlignmentScore.  # noqa: E501
        :type evp_mid: object
        """

        self._evp_mid = evp_mid

    @property
    def history(self):
        """Gets the history of this TitaniumEvpAlignmentScore.  # noqa: E501


        :return: The history of this TitaniumEvpAlignmentScore.  # noqa: E501
        :rtype: list[TitaniumEvpAlignmentScoreWithDate]
        """
        return self._history

    @history.setter
    def history(self, history):
        """Sets the history of this TitaniumEvpAlignmentScore.


        :param history: The history of this TitaniumEvpAlignmentScore.  # noqa: E501
        :type history: list[TitaniumEvpAlignmentScoreWithDate]
        """

        self._history = history

    @property
    def score(self):
        """Gets the score of this TitaniumEvpAlignmentScore.  # noqa: E501


        :return: The score of this TitaniumEvpAlignmentScore.  # noqa: E501
        :rtype: object
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this TitaniumEvpAlignmentScore.


        :param score: The score of this TitaniumEvpAlignmentScore.  # noqa: E501
        :type score: object
        """

        self._score = score

    @property
    def score_status(self):
        """Gets the score_status of this TitaniumEvpAlignmentScore.  # noqa: E501


        :return: The score_status of this TitaniumEvpAlignmentScore.  # noqa: E501
        :rtype: str
        """
        return self._score_status

    @score_status.setter
    def score_status(self, score_status):
        """Sets the score_status of this TitaniumEvpAlignmentScore.


        :param score_status: The score_status of this TitaniumEvpAlignmentScore.  # noqa: E501
        :type score_status: str
        """

        self._score_status = score_status

    @property
    def submission_mean(self):
        """Gets the submission_mean of this TitaniumEvpAlignmentScore.  # noqa: E501


        :return: The submission_mean of this TitaniumEvpAlignmentScore.  # noqa: E501
        :rtype: object
        """
        return self._submission_mean

    @submission_mean.setter
    def submission_mean(self, submission_mean):
        """Sets the submission_mean of this TitaniumEvpAlignmentScore.


        :param submission_mean: The submission_mean of this TitaniumEvpAlignmentScore.  # noqa: E501
        :type submission_mean: object
        """

        self._submission_mean = submission_mean

    @property
    def submission_std_dev(self):
        """Gets the submission_std_dev of this TitaniumEvpAlignmentScore.  # noqa: E501


        :return: The submission_std_dev of this TitaniumEvpAlignmentScore.  # noqa: E501
        :rtype: object
        """
        return self._submission_std_dev

    @submission_std_dev.setter
    def submission_std_dev(self, submission_std_dev):
        """Sets the submission_std_dev of this TitaniumEvpAlignmentScore.


        :param submission_std_dev: The submission_std_dev of this TitaniumEvpAlignmentScore.  # noqa: E501
        :type submission_std_dev: object
        """

        self._submission_std_dev = submission_std_dev

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
        if not isinstance(other, TitaniumEvpAlignmentScore):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TitaniumEvpAlignmentScore):
            return True

        return self.to_dict() != other.to_dict()
