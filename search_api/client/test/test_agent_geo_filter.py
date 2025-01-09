# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from search_api_client.models.agent_geo_filter import AgentGeoFilter

class TestAgentGeoFilter(unittest.TestCase):
    """AgentGeoFilter unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AgentGeoFilter:
        """Test AgentGeoFilter
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AgentGeoFilter`
        """
        model = AgentGeoFilter()
        if include_optional:
            return AgentGeoFilter(
                latitude = -90.0,
                longitude = -180.0,
                radius = 1.337
            )
        else:
            return AgentGeoFilter(
                latitude = -90.0,
                longitude = -180.0,
                radius = 1.337,
        )
        """

    def testAgentGeoFilter(self):
        """Test AgentGeoFilter"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
