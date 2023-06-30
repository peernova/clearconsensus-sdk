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
from openapi_client.models.grpcproto_error import GrpcprotoError  # noqa: E501
from openapi_client.rest import ApiException

class TestGrpcprotoError(unittest.TestCase):
    """GrpcprotoError unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GrpcprotoError
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.grpcproto_error.GrpcprotoError()  # noqa: E501
        if include_optional :
            return GrpcprotoError(
                code = 56, 
                message = '', 
                validation_error_details = [
                    openapi_client.models.error_validation_error_detail.ErrorValidationErrorDetail(
                        description = '', 
                        field_name = '', )
                    ]
            )
        else :
            return GrpcprotoError(
        )

    def testGrpcprotoError(self):
        """Test GrpcprotoError"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
