# coding: utf-8

"""
    FastAPI

    A simple fastapi application that services registered agents information

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from agentverse_client.almanac.aio.models.with_pagination_list_agent import WithPaginationListAgent

class TestWithPaginationListAgent(unittest.TestCase):
    """WithPaginationListAgent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WithPaginationListAgent:
        """Test WithPaginationListAgent
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WithPaginationListAgent`
        """
        model = WithPaginationListAgent()
        if include_optional:
            return WithPaginationListAgent(
                objects = [
                    agentverse_client.almanac.aio.models.agent.Agent(
                        status = 'active', 
                        type = 'Local', 
                        address = '', 
                        domain_name = '', 
                        prefix = 'agent', 
                        endpoints = [
                            agentverse_client.almanac.aio.models.endpoint.Endpoint(
                                url = '', 
                                weight = 56, )
                            ], 
                        metadata = { }, 
                        protocols = [
                            ''
                            ], 
                        expiry = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        developer_category = 'Community', 
                        name = '', 
                        running = True, 
                        maintainer_id = '', 
                        username = '', 
                        code_update_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        total_interactions = 56, 
                        trust_score = 1.337, )
                    ],
                total = 56,
                page_size = 56,
                tracker_last_update = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return WithPaginationListAgent(
                objects = [
                    agentverse_client.almanac.aio.models.agent.Agent(
                        status = 'active', 
                        type = 'Local', 
                        address = '', 
                        domain_name = '', 
                        prefix = 'agent', 
                        endpoints = [
                            agentverse_client.almanac.aio.models.endpoint.Endpoint(
                                url = '', 
                                weight = 56, )
                            ], 
                        metadata = { }, 
                        protocols = [
                            ''
                            ], 
                        expiry = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        developer_category = 'Community', 
                        name = '', 
                        running = True, 
                        maintainer_id = '', 
                        username = '', 
                        code_update_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        total_interactions = 56, 
                        trust_score = 1.337, )
                    ],
                total = 56,
                page_size = 56,
        )
        """

    def testWithPaginationListAgent(self):
        """Test WithPaginationListAgent"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
