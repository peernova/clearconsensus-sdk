# coding: utf-8

"""
    clearconsensus-sdk

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.policy_service_api import PolicyServiceApi  # noqa: E501
from openapi_client.rest import ApiException


class TestPolicyServiceApi(unittest.TestCase):
    """PolicyServiceApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.policy_service_api.PolicyServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_policy_service_check_policy(self):
        """Test case for policy_service_check_policy

        """
        pass

    def test_policy_service_create(self):
        """Test case for policy_service_create

        """
        pass

    def test_policy_service_get_addons(self):
        """Test case for policy_service_get_addons

        """
        pass

    def test_policy_service_get_apis(self):
        """Test case for policy_service_get_apis

        """
        pass

    def test_policy_service_get_assets(self):
        """Test case for policy_service_get_assets

        """
        pass

    def test_policy_service_get_policies(self):
        """Test case for policy_service_get_policies

        """
        pass

    def test_policy_service_remove_policy(self):
        """Test case for policy_service_remove_policy

        """
        pass


if __name__ == '__main__':
    unittest.main()
