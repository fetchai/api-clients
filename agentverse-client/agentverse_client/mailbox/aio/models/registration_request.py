# coding: utf-8

"""
    Agentverse Mailbox API

    The Mailbox API handles agent message delivery, registration, storage quotas, and usage tracking within the Agentverse platform. It supports secure agent communication through cryptographic authentication

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class RegistrationRequest(BaseModel):
    """
    RegistrationRequest
    """ # noqa: E501
    address: StrictStr
    prefix: Optional[StrictStr] = None
    challenge: StrictStr
    challenge_response: StrictStr
    agent_type: StrictStr
    endpoint: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["address", "prefix", "challenge", "challenge_response", "agent_type", "endpoint"]

    @field_validator('prefix')
    def prefix_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['agent', 'test-agent']):
            raise ValueError("must be one of enum values ('agent', 'test-agent')")
        return value

    @field_validator('agent_type')
    def agent_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['mailbox', 'proxy', 'custom']):
            raise ValueError("must be one of enum values ('mailbox', 'proxy', 'custom')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of RegistrationRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if prefix (nullable) is None
        # and model_fields_set contains the field
        if self.prefix is None and "prefix" in self.model_fields_set:
            _dict['prefix'] = None

        # set to None if endpoint (nullable) is None
        # and model_fields_set contains the field
        if self.endpoint is None and "endpoint" in self.model_fields_set:
            _dict['endpoint'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RegistrationRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "address": obj.get("address"),
            "prefix": obj.get("prefix"),
            "challenge": obj.get("challenge"),
            "challenge_response": obj.get("challenge_response"),
            "agent_type": obj.get("agent_type"),
            "endpoint": obj.get("endpoint")
        })
        return _obj


