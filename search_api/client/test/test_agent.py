# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from search_api_client.models.agent import Agent

class TestAgent(unittest.TestCase):
    """Agent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Agent:
        """Test Agent
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Agent`
        """
        model = Agent()
        if include_optional:
            return Agent(
                address = '',
                name = '',
                readme = '',
                protocols = [
                    search_api_client.models.protocol.Protocol(
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
                category = 'fetch-ai',
                featured = True,
                geo_location = search_api_client.models.agent_geo_location.AgentGeoLocation(
                    latitude = 1.337, 
                    longitude = 1.337, 
                    radius = 1.337, ),
                last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return Agent(
                address = '',
                name = '',
                readme = '',
                protocols = [
                    search_api_client.models.protocol.Protocol(
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
                category = 'fetch-ai',
                geo_location = search_api_client.models.agent_geo_location.AgentGeoLocation(
                    latitude = 1.337, 
                    longitude = 1.337, 
                    radius = 1.337, ),
                last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testAgent(self):
        """Test Agent"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
