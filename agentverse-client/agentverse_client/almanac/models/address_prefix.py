# coding: utf-8

"""
    FastAPI

    A simple fastapi application that services registered agents information. 

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class AddressPrefix(str, Enum):
    """
    AddressPrefix
    """

    """
    allowed enum values
    """
    AGENT = 'agent'
    TEST_MINUS_AGENT = 'test-agent'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AddressPrefix from a JSON string"""
        return cls(json.loads(json_str))


