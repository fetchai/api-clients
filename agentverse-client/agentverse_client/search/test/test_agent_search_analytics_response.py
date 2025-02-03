# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from agentverse_client.search.models.agent_search_analytics_response import AgentSearchAnalyticsResponse

class TestAgentSearchAnalyticsResponse(unittest.TestCase):
    """AgentSearchAnalyticsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AgentSearchAnalyticsResponse:
        """Test AgentSearchAnalyticsResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AgentSearchAnalyticsResponse`
        """
        model = AgentSearchAnalyticsResponse()
        if include_optional:
            return AgentSearchAnalyticsResponse(
                address = '',
                num_searches = 56,
                last_24h_num_searches = 56,
                last_30d_num_searches = 56,
                last_30d_history = [
                    56
                    ]
            )
        else:
            return AgentSearchAnalyticsResponse(
                address = '',
                num_searches = 56,
                last_24h_num_searches = 56,
                last_30d_num_searches = 56,
                last_30d_history = [
                    56
                    ],
        )
        """

    def testAgentSearchAnalyticsResponse(self):
        """Test AgentSearchAnalyticsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
