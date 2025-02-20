# coding: utf-8

"""
    FastAPI

    An API for our smart search engine that provides the agent that best fits your needs.

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from agentverse_client.search.models.agent_geo_location import AgentGeoLocation

class TestAgentGeoLocation(unittest.TestCase):
    """AgentGeoLocation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AgentGeoLocation:
        """Test AgentGeoLocation
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AgentGeoLocation`
        """
        model = AgentGeoLocation()
        if include_optional:
            return AgentGeoLocation(
                latitude = 1.337,
                longitude = 1.337,
                radius = 1.337
            )
        else:
            return AgentGeoLocation(
                latitude = 1.337,
                longitude = 1.337,
        )
        """

    def testAgentGeoLocation(self):
        """Test AgentGeoLocation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
