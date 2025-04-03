# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from agentverse_client.almanac.models.agent_search import AgentSearch

class TestAgentSearch(unittest.TestCase):
    """AgentSearch unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AgentSearch:
        """Test AgentSearch
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AgentSearch`
        """
        model = AgentSearch()
        if include_optional:
            return AgentSearch(
                text = '',
                protocols = [
                    ''
                    ],
                types = [
                    'Local'
                    ],
                status = [
                    'Active'
                    ],
                dev_categories = [
                    'Community'
                    ],
                limit = 56,
                network = 'mainnet',
                sort = 'Recent'
            )
        else:
            return AgentSearch(
                text = '',
        )
        """

    def testAgentSearch(self):
        """Test AgentSearch"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
