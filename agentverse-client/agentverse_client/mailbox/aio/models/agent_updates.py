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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class AgentUpdates(BaseModel):
    """
    AgentUpdates
    """ # noqa: E501
    name: Annotated[str, Field(min_length=1, strict=True, max_length=80)] = Field(description="Updated name of the agent.")
    readme: Optional[Annotated[str, Field(strict=True, max_length=80000)]] = None
    avatar_url: Optional[Annotated[str, Field(strict=True, max_length=4000)]] = None
    short_description: Optional[Annotated[str, Field(strict=True, max_length=300)]] = None
    agent_type: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["name", "readme", "avatar_url", "short_description", "agent_type"]

    @field_validator('agent_type')
    def agent_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

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
        """Create an instance of AgentUpdates from a JSON string"""
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
        # set to None if readme (nullable) is None
        # and model_fields_set contains the field
        if self.readme is None and "readme" in self.model_fields_set:
            _dict['readme'] = None

        # set to None if avatar_url (nullable) is None
        # and model_fields_set contains the field
        if self.avatar_url is None and "avatar_url" in self.model_fields_set:
            _dict['avatar_url'] = None

        # set to None if short_description (nullable) is None
        # and model_fields_set contains the field
        if self.short_description is None and "short_description" in self.model_fields_set:
            _dict['short_description'] = None

        # set to None if agent_type (nullable) is None
        # and model_fields_set contains the field
        if self.agent_type is None and "agent_type" in self.model_fields_set:
            _dict['agent_type'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AgentUpdates from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "readme": obj.get("readme"),
            "avatar_url": obj.get("avatar_url"),
            "short_description": obj.get("short_description"),
            "agent_type": obj.get("agent_type")
        })
        return _obj


