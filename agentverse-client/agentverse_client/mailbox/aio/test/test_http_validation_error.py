# coding: utf-8

"""
    Agentverse Mailbox API

    The Mailbox API handles agent message delivery, registration, storage quotas, and usage tracking within the Agentverse platform. It supports secure agent communication through cryptographic authentication

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from agentverse_client.mailbox.aio.models.http_validation_error import HTTPValidationError

class TestHTTPValidationError(unittest.TestCase):
    """HTTPValidationError unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HTTPValidationError:
        """Test HTTPValidationError
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HTTPValidationError`
        """
        model = HTTPValidationError()
        if include_optional:
            return HTTPValidationError(
                detail = [
                    agentverse_client.mailbox.aio.models.validation_error.ValidationError(
                        loc = [
                            null
                            ], 
                        msg = '', 
                        type = '', )
                    ]
            )
        else:
            return HTTPValidationError(
        )
        """

    def testHTTPValidationError(self):
        """Test HTTPValidationError"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
