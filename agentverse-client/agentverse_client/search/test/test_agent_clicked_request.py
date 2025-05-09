# coding: utf-8

"""
    FastAPI

    An API for our smart search engine that provides the agent that best fits your needs.

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from agentverse_client.search.models.agent_clicked_request import AgentClickedRequest

class TestAgentClickedRequest(unittest.TestCase):
    """AgentClickedRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AgentClickedRequest:
        """Test AgentClickedRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AgentClickedRequest`
        """
        model = AgentClickedRequest()
        if include_optional:
            return AgentClickedRequest(
                address = 'agent1rz76d8hdx282zstqn20l3h74hscgagg7422rz28rczse3ajf5kewcfaq67w',
                contract = 'mainnet',
                search_id = '',
                page_index = 0.0
            )
        else:
            return AgentClickedRequest(
                address = 'agent1rz76d8hdx282zstqn20l3h74hscgagg7422rz28rczse3ajf5kewcfaq67w',
                search_id = '',
                page_index = 0.0,
        )
        """

    def testAgentClickedRequest(self):
        """Test AgentClickedRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
