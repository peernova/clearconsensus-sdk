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
from openapi_client.models.titanium_submission_evidence_table_column import TitaniumSubmissionEvidenceTableColumn  # noqa: E501
from openapi_client.rest import ApiException

class TestTitaniumSubmissionEvidenceTableColumn(unittest.TestCase):
    """TitaniumSubmissionEvidenceTableColumn unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TitaniumSubmissionEvidenceTableColumn
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.titanium_submission_evidence_table_column.TitaniumSubmissionEvidenceTableColumn()  # noqa: E501
        if include_optional :
            return TitaniumSubmissionEvidenceTableColumn(
                abs_diff_from_evidence = openapi_client.models.abs_diff_from_evidence.absDiffFromEvidence(), 
                evi_price_abs_diff_from_latest_trade = openapi_client.models.evi_price_abs_diff_from_latest_trade.eviPriceAbsDiffFromLatestTrade(), 
                evidence = openapi_client.models.evidence.evidence(), 
                lower_boundary = openapi_client.models.lower_boundary.lowerBoundary(), 
                participants_count = '', 
                std_dev = openapi_client.models.std_dev.stdDev(), 
                sub_price_diff = openapi_client.models.sub_price_diff.subPriceDiff(), 
                upper_boundary = openapi_client.models.upper_boundary.upperBoundary()
            )
        else :
            return TitaniumSubmissionEvidenceTableColumn(
        )

    def testTitaniumSubmissionEvidenceTableColumn(self):
        """Test TitaniumSubmissionEvidenceTableColumn"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
