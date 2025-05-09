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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from agentverse_client.search.aio.models.function_type import FunctionType
from typing import Optional, Set
from typing_extensions import Self

class Function(BaseModel):
    """
    Function
    """ # noqa: E501
    id: StrictStr = Field(description="the identifier of the function")
    type: FunctionType = Field(description="the type of the function / action")
    name: StrictStr = Field(description="the name of the function")
    agent: StrictStr = Field(description="the agent that the function belongs to")
    description: StrictStr = Field(description="the description of the function")
    is_primary: StrictBool = Field(description="denotes if a function is primary or not")
    groups: Optional[List[StrictStr]] = Field(default=None, description="group that the function belongs to")
    total_interactions: StrictInt = Field(description="the total interactions for this function")
    recent_interactions: StrictInt = Field(description="the number of interactions in the last 90 days")
    rating: Optional[Union[StrictFloat, StrictInt]] = None
    featured: Optional[StrictBool] = Field(default=False, description="signaled if the function is featured or not")
    last_updated: datetime = Field(description="the time at which the function was last updated at")
    created_at: datetime = Field(description="the time at which the function was first visible or created")
    __properties: ClassVar[List[str]] = ["id", "type", "name", "agent", "description", "is_primary", "groups", "total_interactions", "recent_interactions", "rating", "featured", "last_updated", "created_at"]

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
        """Create an instance of Function from a JSON string"""
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
        # set to None if rating (nullable) is None
        # and model_fields_set contains the field
        if self.rating is None and "rating" in self.model_fields_set:
            _dict['rating'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Function from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "type": obj.get("type"),
            "name": obj.get("name"),
            "agent": obj.get("agent"),
            "description": obj.get("description"),
            "is_primary": obj.get("is_primary"),
            "groups": obj.get("groups"),
            "total_interactions": obj.get("total_interactions"),
            "recent_interactions": obj.get("recent_interactions"),
            "rating": obj.get("rating"),
            "featured": obj.get("featured") if obj.get("featured") is not None else False,
            "last_updated": obj.get("last_updated"),
            "created_at": obj.get("created_at")
        })
        return _obj


