# coding: utf-8

"""
    Agentverse Mailbox API

    The Mailbox API handles agent message delivery, registration, storage quotas, and usage tracking within the Agentverse platform. It supports secure agent communication through cryptographic authentication

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from agentverse_client.mailbox.api.api_keys_api import ApiKeysApi


class TestApiKeysApi(unittest.TestCase):
    """ApiKeysApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ApiKeysApi()

    def tearDown(self) -> None:
        pass

    def test_add_teams_api_key(self) -> None:
        """Test case for add_teams_api_key

        Add Teams Api Key
        """
        pass

    def test_add_user_api_key(self) -> None:
        """Test case for add_user_api_key

        Add User Api Key
        """
        pass

    def test_delete_teams_api_key(self) -> None:
        """Test case for delete_teams_api_key

        Delete Teams Api Key
        """
        pass

    def test_delete_user_api_key(self) -> None:
        """Test case for delete_user_api_key

        Delete User Api Key
        """
        pass

    def test_list_team_api_keys(self) -> None:
        """Test case for list_team_api_keys

        List Team Api Keys
        """
        pass

    def test_list_user_api_keys(self) -> None:
        """Test case for list_user_api_keys

        List User Api Keys
        """
        pass

    def test_update_team_api_key(self) -> None:
        """Test case for update_team_api_key

        Update Teams Api Key
        """
        pass

    def test_update_user_api_key(self) -> None:
        """Test case for update_user_api_key

        Update User Api Key
        """
        pass


if __name__ == '__main__':
    unittest.main()
