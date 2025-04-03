# coding: utf-8

"""
    FastAPI

    A simple fastapi application that services registered agents information.

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from agentverse_client.almanac.models.interaction_type import InteractionType
from typing import Optional, Set
from typing_extensions import Self

class Interaction(BaseModel):
    """
    Interaction
    """ # noqa: E501
    type: InteractionType
    request: Annotated[str, Field(strict=True)] = Field(description="Model reference hash for the request")
    responses: List[Annotated[str, Field(strict=True)]] = Field(description="List of model reference hashes for the responses")
    __properties: ClassVar[List[str]] = ["type", "request", "responses"]

    @field_validator('request')
    def request_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^model:[0-9a-f]{64}$", value):
            raise ValueError(r"must validate the regular expression /^model:[0-9a-f]{64}$/")
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
        """Create an instance of Interaction from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Interaction from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "request": obj.get("request"),
            "responses": obj.get("responses")
        })
        return _obj


