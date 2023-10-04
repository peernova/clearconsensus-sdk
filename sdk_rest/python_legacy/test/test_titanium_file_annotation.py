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
from openapi_client.models.titanium_file_annotation import TitaniumFileAnnotation  # noqa: E501
from openapi_client.rest import ApiException

class TestTitaniumFileAnnotation(unittest.TestCase):
    """TitaniumFileAnnotation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TitaniumFileAnnotation
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.titanium_file_annotation.TitaniumFileAnnotation()  # noqa: E501
        if include_optional :
            return TitaniumFileAnnotation(
                annotation = None, 
                asset = openapi_client.models.titanium_asset_details.titaniumAssetDetails(
                    asset_id = '', 
                    date = '', 
                    name = '', 
                    service = '', 
                    snap_time = '', 
                    sub_asset = '', ), 
                chunks = [
                    openapi_client.models.titanium_chunk.titaniumChunk(
                        annotation = openapi_client.models.annotation.annotation(), 
                        chunk_id = '', 
                        description = '', 
                        original_file_name = '', 
                        rows_count = 56, 
                        start_row = 56, 
                        user = '', )
                    ], 
                client = '', 
                file_name = '', 
                mode = '', 
                upload_time = ''
            )
        else :
            return TitaniumFileAnnotation(
        )

    def testTitaniumFileAnnotation(self):
        """Test TitaniumFileAnnotation"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
