# coding: utf-8

"""
    FastAPI

    An API for our smart search engine that provides the agent that best fits your needs.

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class MultiSEOEvaluationRequest(BaseModel):
    """
    MultiSEOEvaluationRequest
    """ # noqa: E501
    max_days: Optional[StrictInt] = Field(default=10, description="For finding search queries to use, consider searches from up to `max_days` days ago (default: 10)")
    max_searches: Optional[StrictInt] = Field(default=100, description="How many top searches to use at most, which determines how many messages we'll send at most (default: 100)")
    __properties: ClassVar[List[str]] = ["max_days", "max_searches"]

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
        """Create an instance of MultiSEOEvaluationRequest from a JSON string"""
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
        """Create an instance of MultiSEOEvaluationRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "max_days": obj.get("max_days") if obj.get("max_days") is not None else 10,
            "max_searches": obj.get("max_searches") if obj.get("max_searches") is not None else 100
        })
        return _obj


