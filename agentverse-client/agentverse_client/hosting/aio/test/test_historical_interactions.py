# coding: utf-8

"""
    Agent Hosting API

      ## Overview  The Agent Hosting API helps users deploy agents to the cloud  ## Authentication  The entire API requires that the user authenticate with the ecosystem first before accessing the api 

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from agentverse_client.hosting.aio.models.historical_interactions import HistoricalInteractions

class TestHistoricalInteractions(unittest.TestCase):
    """HistoricalInteractions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HistoricalInteractions:
        """Test HistoricalInteractions
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HistoricalInteractions`
        """
        model = HistoricalInteractions()
        if include_optional:
            return HistoricalInteractions(
                data_points = {
                    'key' : 56
                    },
                total_interactions = 56
            )
        else:
            return HistoricalInteractions(
                data_points = {
                    'key' : 56
                    },
                total_interactions = 56,
        )
        """

    def testHistoricalInteractions(self):
        """Test HistoricalInteractions"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
