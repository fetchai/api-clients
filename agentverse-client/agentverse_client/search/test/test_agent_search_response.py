# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from agentverse_client.search.models.agent_search_response import AgentSearchResponse

class TestAgentSearchResponse(unittest.TestCase):
    """AgentSearchResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AgentSearchResponse:
        """Test AgentSearchResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AgentSearchResponse`
        """
        model = AgentSearchResponse()
        if include_optional:
            return AgentSearchResponse(
                agents = [
                    agentverse_client.search.models.agent.Agent(
                        address = '', 
                        prefix = 'agent', 
                        name = '', 
                        readme = '', 
                        protocols = [
                            agentverse_client.search.models.protocol.Protocol(
                                name = '', 
                                version = '', 
                                digest = '', )
                            ], 
                        avatar_href = '', 
                        total_interactions = 56, 
                        recent_interactions = 56, 
                        rating = 1.337, 
                        status = 'active', 
                        type = 'hosted', 
                        featured = True, 
                        category = 'fetch-ai', 
                        system_wide_tags = [
                            ''
                            ], 
                        geo_location = agentverse_client.search.models.agent_geo_location.AgentGeoLocation(
                            latitude = 1.337, 
                            longitude = 1.337, 
                            radius = 1.337, ), 
                        domain = '', 
                        last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        current_campaign_eligible = True, )
                    ],
                offset = 56,
                limit = 56,
                num_hits = 56,
                total = 56,
                search_id = ''
            )
        else:
            return AgentSearchResponse(
                offset = 56,
                limit = 56,
                num_hits = 56,
                total = 56,
                search_id = '',
        )
        """

    def testAgentSearchResponse(self):
        """Test AgentSearchResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
