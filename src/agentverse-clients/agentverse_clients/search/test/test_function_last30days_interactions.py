# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from agentverse_clients.search.models.function_last30days_interactions import FunctionLast30daysInteractions

class TestFunctionLast30daysInteractions(unittest.TestCase):
    """FunctionLast30daysInteractions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FunctionLast30daysInteractions:
        """Test FunctionLast30daysInteractions
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FunctionLast30daysInteractions`
        """
        model = FunctionLast30daysInteractions()
        if include_optional:
            return FunctionLast30daysInteractions(
                function_id = '',
                total = [
                    56
                    ]
            )
        else:
            return FunctionLast30daysInteractions(
                function_id = '',
                total = [
                    56
                    ],
        )
        """

    def testFunctionLast30daysInteractions(self):
        """Test FunctionLast30daysInteractions"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
