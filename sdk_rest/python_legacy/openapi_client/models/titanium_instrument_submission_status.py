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


class TitaniumInstrumentSubmissionStatus(object):
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
        'bimodality': 'str',
        'bimodality_history': 'list[TitaniumDateAndValue]',
        'consensus_status': 'str',
        'consensus_status_details': 'str',
        'consensus_status_details_history': 'list[TitaniumDateAndValue]',
        'consensus_status_history': 'list[TitaniumDateAndValue]',
        'dqe_history': 'list[TitaniumDateAndValue]',
        'highest_dqe': 'str',
        'participant_consensus_status': 'str',
        'participant_consensus_status_details': 'str',
        'participant_consensus_status_details_history': 'list[TitaniumDateAndValue]',
        'participant_consensus_status_history': 'list[TitaniumDateAndValue]'
    }

    attribute_map = {
        'bimodality': 'bimodality',
        'bimodality_history': 'bimodalityHistory',
        'consensus_status': 'consensusStatus',
        'consensus_status_details': 'consensusStatusDetails',
        'consensus_status_details_history': 'consensusStatusDetailsHistory',
        'consensus_status_history': 'consensusStatusHistory',
        'dqe_history': 'dqeHistory',
        'highest_dqe': 'highestDqe',
        'participant_consensus_status': 'participantConsensusStatus',
        'participant_consensus_status_details': 'participantConsensusStatusDetails',
        'participant_consensus_status_details_history': 'participantConsensusStatusDetailsHistory',
        'participant_consensus_status_history': 'participantConsensusStatusHistory'
    }

    def __init__(self, bimodality=None, bimodality_history=None, consensus_status=None, consensus_status_details=None, consensus_status_details_history=None, consensus_status_history=None, dqe_history=None, highest_dqe=None, participant_consensus_status=None, participant_consensus_status_details=None, participant_consensus_status_details_history=None, participant_consensus_status_history=None, local_vars_configuration=None):  # noqa: E501
        """TitaniumInstrumentSubmissionStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._bimodality = None
        self._bimodality_history = None
        self._consensus_status = None
        self._consensus_status_details = None
        self._consensus_status_details_history = None
        self._consensus_status_history = None
        self._dqe_history = None
        self._highest_dqe = None
        self._participant_consensus_status = None
        self._participant_consensus_status_details = None
        self._participant_consensus_status_details_history = None
        self._participant_consensus_status_history = None
        self.discriminator = None

        if bimodality is not None:
            self.bimodality = bimodality
        if bimodality_history is not None:
            self.bimodality_history = bimodality_history
        if consensus_status is not None:
            self.consensus_status = consensus_status
        if consensus_status_details is not None:
            self.consensus_status_details = consensus_status_details
        if consensus_status_details_history is not None:
            self.consensus_status_details_history = consensus_status_details_history
        if consensus_status_history is not None:
            self.consensus_status_history = consensus_status_history
        if dqe_history is not None:
            self.dqe_history = dqe_history
        if highest_dqe is not None:
            self.highest_dqe = highest_dqe
        if participant_consensus_status is not None:
            self.participant_consensus_status = participant_consensus_status
        if participant_consensus_status_details is not None:
            self.participant_consensus_status_details = participant_consensus_status_details
        if participant_consensus_status_details_history is not None:
            self.participant_consensus_status_details_history = participant_consensus_status_details_history
        if participant_consensus_status_history is not None:
            self.participant_consensus_status_history = participant_consensus_status_history

    @property
    def bimodality(self):
        """Gets the bimodality of this TitaniumInstrumentSubmissionStatus.  # noqa: E501


        :return: The bimodality of this TitaniumInstrumentSubmissionStatus.  # noqa: E501
        :rtype: str
        """
        return self._bimodality

    @bimodality.setter
    def bimodality(self, bimodality):
        """Sets the bimodality of this TitaniumInstrumentSubmissionStatus.


        :param bimodality: The bimodality of this TitaniumInstrumentSubmissionStatus.  # noqa: E501
        :type bimodality: str
        """

        self._bimodality = bimodality

    @property
    def bimodality_history(self):
        """Gets the bimodality_history of this TitaniumInstrumentSubmissionStatus.  # noqa: E501


        :return: The bimodality_history of this TitaniumInstrumentSubmissionStatus.  # noqa: E501
        :rtype: list[TitaniumDateAndValue]
        """
        return self._bimodality_history

    @bimodality_history.setter
    def bimodality_history(self, bimodality_history):
        """Sets the bimodality_history of this TitaniumInstrumentSubmissionStatus.


        :param bimodality_history: The bimodality_history of this TitaniumInstrumentSubmissionStatus.  # noqa: E501
        :type bimodality_history: list[TitaniumDateAndValue]
        """

        self._bimodality_history = bimodality_history

    @property
    def consensus_status(self):
        """Gets the consensus_status of this TitaniumInstrumentSubmissionStatus.  # noqa: E501


        :return: The consensus_status of this TitaniumInstrumentSubmissionStatus.  # noqa: E501
        :rtype: str
        """
        return self._consensus_status

    @consensus_status.setter
    def consensus_status(self, consensus_status):
        """Sets the consensus_status of this TitaniumInstrumentSubmissionStatus.


        :param consensus_status: The consensus_status of this TitaniumInstrumentSubmissionStatus.  # noqa: E501
        :type consensus_status: str
        """

        self._consensus_status = consensus_status

    @property
    def consensus_status_details(self):
        """Gets the consensus_status_details of this TitaniumInstrumentSubmissionStatus.  # noqa: E501


        :return: The consensus_status_details of this TitaniumInstrumentSubmissionStatus.  # noqa: E501
        :rtype: str
        """
        return self._consensus_status_details

    @consensus_status_details.setter
    def consensus_status_details(self, consensus_status_details):
        """Sets the consensus_status_details of this TitaniumInstrumentSubmissionStatus.


        :param consensus_status_details: The consensus_status_details of this TitaniumInstrumentSubmissionStatus.  # noqa: E501
        :type consensus_status_details: str
        """

        self._consensus_status_details = consensus_status_details

    @property
    def consensus_status_details_history(self):
        """Gets the consensus_status_details_history of this TitaniumInstrumentSubmissionStatus.  # noqa: E501


        :return: The consensus_status_details_history of this TitaniumInstrumentSubmissionStatus.  # noqa: E501
        :rtype: list[TitaniumDateAndValue]
        """
        return self._consensus_status_details_history

    @consensus_status_details_history.setter
    def consensus_status_details_history(self, consensus_status_details_history):
        """Sets the consensus_status_details_history of this TitaniumInstrumentSubmissionStatus.


        :param consensus_status_details_history: The consensus_status_details_history of this TitaniumInstrumentSubmissionStatus.  # noqa: E501
        :type consensus_status_details_history: list[TitaniumDateAndValue]
        """

        self._consensus_status_details_history = consensus_status_details_history

    @property
    def consensus_status_history(self):
        """Gets the consensus_status_history of this TitaniumInstrumentSubmissionStatus.  # noqa: E501


        :return: The consensus_status_history of this TitaniumInstrumentSubmissionStatus.  # noqa: E501
        :rtype: list[TitaniumDateAndValue]
        """
        return self._consensus_status_history

    @consensus_status_history.setter
    def consensus_status_history(self, consensus_status_history):
        """Sets the consensus_status_history of this TitaniumInstrumentSubmissionStatus.


        :param consensus_status_history: The consensus_status_history of this TitaniumInstrumentSubmissionStatus.  # noqa: E501
        :type consensus_status_history: list[TitaniumDateAndValue]
        """

        self._consensus_status_history = consensus_status_history

    @property
    def dqe_history(self):
        """Gets the dqe_history of this TitaniumInstrumentSubmissionStatus.  # noqa: E501


        :return: The dqe_history of this TitaniumInstrumentSubmissionStatus.  # noqa: E501
        :rtype: list[TitaniumDateAndValue]
        """
        return self._dqe_history

    @dqe_history.setter
    def dqe_history(self, dqe_history):
        """Sets the dqe_history of this TitaniumInstrumentSubmissionStatus.


        :param dqe_history: The dqe_history of this TitaniumInstrumentSubmissionStatus.  # noqa: E501
        :type dqe_history: list[TitaniumDateAndValue]
        """

        self._dqe_history = dqe_history

    @property
    def highest_dqe(self):
        """Gets the highest_dqe of this TitaniumInstrumentSubmissionStatus.  # noqa: E501


        :return: The highest_dqe of this TitaniumInstrumentSubmissionStatus.  # noqa: E501
        :rtype: str
        """
        return self._highest_dqe

    @highest_dqe.setter
    def highest_dqe(self, highest_dqe):
        """Sets the highest_dqe of this TitaniumInstrumentSubmissionStatus.


        :param highest_dqe: The highest_dqe of this TitaniumInstrumentSubmissionStatus.  # noqa: E501
        :type highest_dqe: str
        """

        self._highest_dqe = highest_dqe

    @property
    def participant_consensus_status(self):
        """Gets the participant_consensus_status of this TitaniumInstrumentSubmissionStatus.  # noqa: E501


        :return: The participant_consensus_status of this TitaniumInstrumentSubmissionStatus.  # noqa: E501
        :rtype: str
        """
        return self._participant_consensus_status

    @participant_consensus_status.setter
    def participant_consensus_status(self, participant_consensus_status):
        """Sets the participant_consensus_status of this TitaniumInstrumentSubmissionStatus.


        :param participant_consensus_status: The participant_consensus_status of this TitaniumInstrumentSubmissionStatus.  # noqa: E501
        :type participant_consensus_status: str
        """

        self._participant_consensus_status = participant_consensus_status

    @property
    def participant_consensus_status_details(self):
        """Gets the participant_consensus_status_details of this TitaniumInstrumentSubmissionStatus.  # noqa: E501


        :return: The participant_consensus_status_details of this TitaniumInstrumentSubmissionStatus.  # noqa: E501
        :rtype: str
        """
        return self._participant_consensus_status_details

    @participant_consensus_status_details.setter
    def participant_consensus_status_details(self, participant_consensus_status_details):
        """Sets the participant_consensus_status_details of this TitaniumInstrumentSubmissionStatus.


        :param participant_consensus_status_details: The participant_consensus_status_details of this TitaniumInstrumentSubmissionStatus.  # noqa: E501
        :type participant_consensus_status_details: str
        """

        self._participant_consensus_status_details = participant_consensus_status_details

    @property
    def participant_consensus_status_details_history(self):
        """Gets the participant_consensus_status_details_history of this TitaniumInstrumentSubmissionStatus.  # noqa: E501


        :return: The participant_consensus_status_details_history of this TitaniumInstrumentSubmissionStatus.  # noqa: E501
        :rtype: list[TitaniumDateAndValue]
        """
        return self._participant_consensus_status_details_history

    @participant_consensus_status_details_history.setter
    def participant_consensus_status_details_history(self, participant_consensus_status_details_history):
        """Sets the participant_consensus_status_details_history of this TitaniumInstrumentSubmissionStatus.


        :param participant_consensus_status_details_history: The participant_consensus_status_details_history of this TitaniumInstrumentSubmissionStatus.  # noqa: E501
        :type participant_consensus_status_details_history: list[TitaniumDateAndValue]
        """

        self._participant_consensus_status_details_history = participant_consensus_status_details_history

    @property
    def participant_consensus_status_history(self):
        """Gets the participant_consensus_status_history of this TitaniumInstrumentSubmissionStatus.  # noqa: E501


        :return: The participant_consensus_status_history of this TitaniumInstrumentSubmissionStatus.  # noqa: E501
        :rtype: list[TitaniumDateAndValue]
        """
        return self._participant_consensus_status_history

    @participant_consensus_status_history.setter
    def participant_consensus_status_history(self, participant_consensus_status_history):
        """Sets the participant_consensus_status_history of this TitaniumInstrumentSubmissionStatus.


        :param participant_consensus_status_history: The participant_consensus_status_history of this TitaniumInstrumentSubmissionStatus.  # noqa: E501
        :type participant_consensus_status_history: list[TitaniumDateAndValue]
        """

        self._participant_consensus_status_history = participant_consensus_status_history

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
        if not isinstance(other, TitaniumInstrumentSubmissionStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TitaniumInstrumentSubmissionStatus):
            return True

        return self.to_dict() != other.to_dict()
