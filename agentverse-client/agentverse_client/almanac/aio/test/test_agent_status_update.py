# coding: utf-8

"""
    FastAPI

    A simple fastapi application that services registered agents information. 

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from agentverse_client.almanac.aio.models.agent_status_update import AgentStatusUpdate

class TestAgentStatusUpdate(unittest.TestCase):
    """AgentStatusUpdate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AgentStatusUpdate:
        """Test AgentStatusUpdate
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AgentStatusUpdate`
        """
        model = AgentStatusUpdate()
        if include_optional:
            return AgentStatusUpdate(
                agent_identifier = '',
                signature = '',
                timestamp = 56,
                is_active = True
            )
        else:
            return AgentStatusUpdate(
                agent_identifier = '',
                is_active = True,
        )
        """

    def testAgentStatusUpdate(self):
        """Test AgentStatusUpdate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
