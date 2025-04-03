# coding: utf-8

"""
    FastAPI

    A simple fastapi application that services registered agents information.

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from agentverse_client.almanac.aio.models.domain_record import DomainRecord

class TestDomainRecord(unittest.TestCase):
    """DomainRecord unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DomainRecord:
        """Test DomainRecord
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DomainRecord`
        """
        model = DomainRecord()
        if include_optional:
            return DomainRecord(
                name = '',
                agents = [
                    agentverse_client.almanac.aio.models.agent_record.AgentRecord(
                        address = '', 
                        weight = 1.337, )
                    ]
            )
        else:
            return DomainRecord(
                name = '',
                agents = [
                    agentverse_client.almanac.aio.models.agent_record.AgentRecord(
                        address = '', 
                        weight = 1.337, )
                    ],
        )
        """

    def testDomainRecord(self):
        """Test DomainRecord"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
