# coding: utf-8

"""
    Agentverse Mailbox API

    The Mailbox API handles agent message delivery, registration, storage quotas, and usage tracking within the Agentverse platform. It supports secure agent communication through cryptographic authentication

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from agentverse_client.mailbox.aio.models.stored_envelope import StoredEnvelope

class TestStoredEnvelope(unittest.TestCase):
    """StoredEnvelope unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StoredEnvelope:
        """Test StoredEnvelope
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StoredEnvelope`
        """
        model = StoredEnvelope()
        if include_optional:
            return StoredEnvelope(
                uuid = '',
                envelope = agentverse_client.mailbox.aio.models.envelope.Envelope(
                    version = 56, 
                    sender = '', 
                    target = '', 
                    session = '', 
                    schema_digest = '', 
                    protocol_digest = '', 
                    payload = '', 
                    expires = 56, 
                    nonce = 56, 
                    signature = '', ),
                received_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                expires_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return StoredEnvelope(
                uuid = '',
                envelope = agentverse_client.mailbox.aio.models.envelope.Envelope(
                    version = 56, 
                    sender = '', 
                    target = '', 
                    session = '', 
                    schema_digest = '', 
                    protocol_digest = '', 
                    payload = '', 
                    expires = 56, 
                    nonce = 56, 
                    signature = '', ),
                received_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                expires_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testStoredEnvelope(self):
        """Test StoredEnvelope"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
