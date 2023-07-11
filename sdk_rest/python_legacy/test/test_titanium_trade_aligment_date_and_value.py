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
from openapi_client.models.titanium_trade_aligment_date_and_value import TitaniumTradeAligmentDateAndValue  # noqa: E501
from openapi_client.rest import ApiException

class TestTitaniumTradeAligmentDateAndValue(unittest.TestCase):
    """TitaniumTradeAligmentDateAndValue unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TitaniumTradeAligmentDateAndValue
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.titanium_trade_aligment_date_and_value.TitaniumTradeAligmentDateAndValue()  # noqa: E501
        if include_optional :
            return TitaniumTradeAligmentDateAndValue(
                date = '', 
                score = openapi_client.models.score.score(), 
                score_status = ''
            )
        else :
            return TitaniumTradeAligmentDateAndValue(
        )

    def testTitaniumTradeAligmentDateAndValue(self):
        """Test TitaniumTradeAligmentDateAndValue"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
