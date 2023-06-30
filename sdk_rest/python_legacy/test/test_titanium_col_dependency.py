# coding: utf-8

"""
    clearconsensus-sdk

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.titanium_col_dependency import TitaniumColDependency  # noqa: E501
from openapi_client.rest import ApiException

class TestTitaniumColDependency(unittest.TestCase):
    """TitaniumColDependency unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TitaniumColDependency
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.titanium_col_dependency.TitaniumColDependency()  # noqa: E501
        if include_optional :
            return TitaniumColDependency(
                col = '', 
                dependency = [
                    openapi_client.models.titanium_dependency.titaniumDependency(
                        entity = '', 
                        entity_name = '', 
                        entity_type = '', 
                        scope = '', 
                        usages = [
                            openapi_client.models.titanium_usage.titaniumUsage(
                                usage_name = '', 
                                usage_type = '', )
                            ], 
                        version = '', )
                    ]
            )
        else :
            return TitaniumColDependency(
        )

    def testTitaniumColDependency(self):
        """Test TitaniumColDependency"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
