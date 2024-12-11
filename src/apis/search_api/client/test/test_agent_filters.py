# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from search_api_client.models.agent_filters import AgentFilters

class TestAgentFilters(unittest.TestCase):
    """AgentFilters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AgentFilters:
        """Test AgentFilters
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AgentFilters`
        """
        model = AgentFilters()
        if include_optional:
            return AgentFilters(
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
                    ]
            )
        else:
            return AgentFilters(
        )
        """

    def testAgentFilters(self):
        """Test AgentFilters"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
