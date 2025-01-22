# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from agentverse_clients.search.models.function_search_request import FunctionSearchRequest

class TestFunctionSearchRequest(unittest.TestCase):
    """FunctionSearchRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FunctionSearchRequest:
        """Test FunctionSearchRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FunctionSearchRequest`
        """
        model = FunctionSearchRequest()
        if include_optional:
            return FunctionSearchRequest(
                filters = agentverse_clients.search.models.function_filters.FunctionFilters(
                    function_type = [
                        'function'
                        ], ),
                sort = 'relevancy',
                direction = 'asc',
                search_text = '',
                offset = 56,
                limit = 56
            )
        else:
            return FunctionSearchRequest(
        )
        """

    def testFunctionSearchRequest(self):
        """Test FunctionSearchRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
