# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from agentverse_client.almanac.models.metadata import Metadata

class TestMetadata(unittest.TestCase):
    """Metadata unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Metadata:
        """Test Metadata
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Metadata`
        """
        model = Metadata()
        if include_optional:
            return Metadata(
                name = '',
                description = '',
                version = '4.072888001528021798096225500850762068629.9333975650685139102691291732729478',
                digest = 'proto:bf325375e030fccba00917317c574773100bf03b5fc61486286e564b23e9566b'
            )
        else:
            return Metadata(
                name = '',
                version = '4.072888001528021798096225500850762068629.9333975650685139102691291732729478',
                digest = 'proto:bf325375e030fccba00917317c574773100bf03b5fc61486286e564b23e9566b',
        )
        """

    def testMetadata(self):
        """Test Metadata"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
