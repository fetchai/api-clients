# coding: utf-8

"""
    FastAPI

    An API for our smart search engine that provides the agent that best fits your needs.

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from agentverse_client.search.aio.models.agent_search_request import AgentSearchRequest

class TestAgentSearchRequest(unittest.TestCase):
    """AgentSearchRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AgentSearchRequest:
        """Test AgentSearchRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AgentSearchRequest`
        """
        model = AgentSearchRequest()
        if include_optional:
            return AgentSearchRequest(
                filters = agentverse_client.search.aio.models.agent_filters.AgentFilters(
                    state = [
                        'active'
                        ], 
                    category = [
                        'fetch-ai'
                        ], 
                    agent_type = [
                        'hosted'
                        ], 
                    protocol_digest = [
                        ''
                        ], 
                    has_location = True, 
                    has_readme = True, 
                    n_interactions = '1k', 
                    tags = [
                        ''
                        ], ),
                sort = 'relevancy',
                direction = 'asc',
                cutoff = 'none',
                search_text = '',
                offset = 56,
                limit = 56,
                search_id = '',
                source = '',
                only_current_campaign_eligible = True
            )
        else:
            return AgentSearchRequest(
        )
        """

    def testAgentSearchRequest(self):
        """Test AgentSearchRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
