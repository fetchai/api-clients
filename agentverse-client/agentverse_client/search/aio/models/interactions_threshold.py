# coding: utf-8

"""
    FastAPI

    An API for our smart search engine that provides the agent that best fits your needs.

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class InteractionsThreshold(str, Enum):
    """
    InteractionsThreshold
    """

    """
    allowed enum values
    """
    ENUM_10 = '10'
    ENUM_100 = '100'
    ENUM_1K = '1k'
    ENUM_10K = '10k'
    ENUM_100K = '100k'
    ENUM_1M = '1m'
    ENUM_10M = '10m'
    ENUM_100M = '100m'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of InteractionsThreshold from a JSON string"""
        return cls(json.loads(json_str))


