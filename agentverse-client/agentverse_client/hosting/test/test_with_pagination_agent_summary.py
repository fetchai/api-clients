# coding: utf-8

"""
    Agent Hosting API

      ## Overview  The Agent Hosting API helps users deploy agents to the cloud  ## Authentication  The entire API requires that the user authenticate with the ecosystem first before accessing the api 

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from agentverse_client.hosting.models.with_pagination_agent_summary import WithPaginationAgentSummary

class TestWithPaginationAgentSummary(unittest.TestCase):
    """WithPaginationAgentSummary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WithPaginationAgentSummary:
        """Test WithPaginationAgentSummary
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WithPaginationAgentSummary`
        """
        model = WithPaginationAgentSummary()
        if include_optional:
            return WithPaginationAgentSummary(
                items = [
                    agentverse_client.hosting.models.agent_summary.AgentSummary(
                        name = '', 
                        address = '', 
                        domain = '', 
                        prefix = 'agent', 
                        running = True, 
                        compiled = True, 
                        code_digest = '', 
                        wallet_address = '', 
                        code_update_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        creation_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        avatar_url = '', )
                    ],
                next_cursor = ''
            )
        else:
            return WithPaginationAgentSummary(
                items = [
                    agentverse_client.hosting.models.agent_summary.AgentSummary(
                        name = '', 
                        address = '', 
                        domain = '', 
                        prefix = 'agent', 
                        running = True, 
                        compiled = True, 
                        code_digest = '', 
                        wallet_address = '', 
                        code_update_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        creation_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        avatar_url = '', )
                    ],
        )
        """

    def testWithPaginationAgentSummary(self):
        """Test WithPaginationAgentSummary"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
