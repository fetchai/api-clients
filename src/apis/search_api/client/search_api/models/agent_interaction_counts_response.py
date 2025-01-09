# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from search_api.models.agent_all_time_interaction_counts import AgentAllTimeInteractionCounts
from typing import Optional, Set
from typing_extensions import Self

class AgentInteractionCountsResponse(BaseModel):
    """
    AgentInteractionCountsResponse
    """ # noqa: E501
    address: StrictStr = Field(description="the address of the agent")
    interval: Annotated[List[StrictInt], Field(min_length=30, max_length=30)] = Field(description="the number of on_interval interactions for each day")
    message: Annotated[List[StrictInt], Field(min_length=30, max_length=30)] = Field(description="the number of on_message interactions for each day")
    total: Annotated[List[StrictInt], Field(min_length=30, max_length=30)] = Field(description="the sum of on_interval and on_message interaction counts for each day")
    num_all_time_interactions: AgentAllTimeInteractionCounts = Field(description="number of on_interval, on_message and total (sum of on_interval and on_message) interactions")
    __properties: ClassVar[List[str]] = ["address", "interval", "message", "total", "num_all_time_interactions"]

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
        """Create an instance of AgentInteractionCountsResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of num_all_time_interactions
        if self.num_all_time_interactions:
            _dict['num_all_time_interactions'] = self.num_all_time_interactions.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AgentInteractionCountsResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "address": obj.get("address"),
            "interval": obj.get("interval"),
            "message": obj.get("message"),
            "total": obj.get("total"),
            "num_all_time_interactions": AgentAllTimeInteractionCounts.from_dict(obj["num_all_time_interactions"]) if obj.get("num_all_time_interactions") is not None else None
        })
        return _obj


