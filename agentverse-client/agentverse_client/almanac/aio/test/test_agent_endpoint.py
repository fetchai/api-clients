# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from agentverse_client.almanac.aio.models.agent_endpoint import AgentEndpoint

class TestAgentEndpoint(unittest.TestCase):
    """AgentEndpoint unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AgentEndpoint:
        """Test AgentEndpoint
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AgentEndpoint`
        """
        model = AgentEndpoint()
        if include_optional:
            return AgentEndpoint(
                url = '',
                weight = 56
            )
        else:
            return AgentEndpoint(
                url = '',
                weight = 56,
        )
        """

    def testAgentEndpoint(self):
        """Test AgentEndpoint"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
