# coding: utf-8

"""
    Agentverse Mailbox API

    The Mailbox API handles agent message delivery, registration, storage quotas, and usage tracking within the Agentverse platform. It supports secure agent communication through cryptographic authentication

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from agentverse_client.mailbox.models.page_leaf import PageLeaf

class TestPageLeaf(unittest.TestCase):
    """PageLeaf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PageLeaf:
        """Test PageLeaf
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PageLeaf`
        """
        model = PageLeaf()
        if include_optional:
            return PageLeaf(
                items = [
                    agentverse_client.mailbox.models.db_api_key.DbApiKey(
                        id = '', 
                        name = '', 
                        expires_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        scope = '', )
                    ],
                total = 0.0,
                page = 1.0,
                size = 1.0,
                pages = 0.0
            )
        else:
            return PageLeaf(
                items = [
                    agentverse_client.mailbox.models.db_api_key.DbApiKey(
                        id = '', 
                        name = '', 
                        expires_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        scope = '', )
                    ],
                total = 0.0,
                page = 1.0,
                size = 1.0,
        )
        """

    def testPageLeaf(self):
        """Test PageLeaf"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
