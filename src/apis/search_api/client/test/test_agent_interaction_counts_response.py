# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from search_api_client.models.agent_interaction_counts_response import AgentInteractionCountsResponse

class TestAgentInteractionCountsResponse(unittest.TestCase):
    """AgentInteractionCountsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AgentInteractionCountsResponse:
        """Test AgentInteractionCountsResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AgentInteractionCountsResponse`
        """
        model = AgentInteractionCountsResponse()
        if include_optional:
            return AgentInteractionCountsResponse(
                address = '',
                interval = [
                    56
                    ],
                message = [
                    56
                    ],
                total = [
                    56
                    ],
                num_all_time_interactions = search_api_client.models.agent_all_time_interaction_counts.AgentAllTimeInteractionCounts(
                    interval = 0.0, 
                    message = 0.0, 
                    total = 0.0, )
            )
        else:
            return AgentInteractionCountsResponse(
                address = '',
                interval = [
                    56
                    ],
                message = [
                    56
                    ],
                total = [
                    56
                    ],
                num_all_time_interactions = search_api_client.models.agent_all_time_interaction_counts.AgentAllTimeInteractionCounts(
                    interval = 0.0, 
                    message = 0.0, 
                    total = 0.0, ),
        )
        """

    def testAgentInteractionCountsResponse(self):
        """Test AgentInteractionCountsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
