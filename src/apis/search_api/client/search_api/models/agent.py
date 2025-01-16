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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from search_api.models.agent_category import AgentCategory
from search_api.models.agent_geo_location import AgentGeoLocation
from search_api.models.agent_type import AgentType
from search_api.models.net_type import NetType
from search_api.models.protocol import Protocol
from search_api.models.status_type import StatusType
from typing import Optional, Set
from typing_extensions import Self

class Agent(BaseModel):
    """
    Agent
    """ # noqa: E501
    address: StrictStr = Field(description="the address of the agent (this should be used as the id of the agent)")
    prefix: NetType
    name: StrictStr = Field(description="the public name of the agent")
    readme: StrictStr = Field(description="the contents of the readme file")
    protocols: List[Protocol] = Field(description="the list of protocols supported by the agent")
    avatar_href: Optional[StrictStr] = None
    total_interactions: StrictInt = Field(description="the total interactions for this agent")
    recent_interactions: StrictInt = Field(description="the number of interactions in the last 90 days")
    rating: Optional[Union[StrictFloat, StrictInt]] = None
    status: StatusType
    type: AgentType
    category: AgentCategory
    featured: Optional[StrictBool] = Field(default=False, description="signaled if the agent is featured or not")
    geo_location: Optional[AgentGeoLocation] = None
    domain: Optional[StrictStr] = None
    last_updated: datetime = Field(description="the time at which the agent was last updated at")
    created_at: datetime = Field(description="the time at which the agent was first visible or created")
    current_campaign_eligible: Optional[StrictBool] = False
    __properties: ClassVar[List[str]] = ["address", "prefix", "name", "readme", "protocols", "avatar_href", "total_interactions", "recent_interactions", "rating", "status", "type", "category", "featured", "geo_location", "domain", "last_updated", "created_at", "current_campaign_eligible"]

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
        """Create an instance of Agent from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in protocols (list)
        _items = []
        if self.protocols:
            for _item_protocols in self.protocols:
                if _item_protocols:
                    _items.append(_item_protocols.to_dict())
            _dict['protocols'] = _items
        # override the default output from pydantic by calling `to_dict()` of geo_location
        if self.geo_location:
            _dict['geo_location'] = self.geo_location.to_dict()
        # set to None if avatar_href (nullable) is None
        # and model_fields_set contains the field
        if self.avatar_href is None and "avatar_href" in self.model_fields_set:
            _dict['avatar_href'] = None

        # set to None if rating (nullable) is None
        # and model_fields_set contains the field
        if self.rating is None and "rating" in self.model_fields_set:
            _dict['rating'] = None

        # set to None if geo_location (nullable) is None
        # and model_fields_set contains the field
        if self.geo_location is None and "geo_location" in self.model_fields_set:
            _dict['geo_location'] = None

        # set to None if domain (nullable) is None
        # and model_fields_set contains the field
        if self.domain is None and "domain" in self.model_fields_set:
            _dict['domain'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Agent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "address": obj.get("address"),
            "prefix": obj.get("prefix"),
            "name": obj.get("name"),
            "readme": obj.get("readme"),
            "protocols": [Protocol.from_dict(_item) for _item in obj["protocols"]] if obj.get("protocols") is not None else None,
            "avatar_href": obj.get("avatar_href"),
            "total_interactions": obj.get("total_interactions"),
            "recent_interactions": obj.get("recent_interactions"),
            "rating": obj.get("rating"),
            "status": obj.get("status"),
            "type": obj.get("type"),
            "category": obj.get("category"),
            "featured": obj.get("featured") if obj.get("featured") is not None else False,
            "geo_location": AgentGeoLocation.from_dict(obj["geo_location"]) if obj.get("geo_location") is not None else None,
            "domain": obj.get("domain"),
            "last_updated": obj.get("last_updated"),
            "created_at": obj.get("created_at"),
            "current_campaign_eligible": obj.get("current_campaign_eligible") if obj.get("current_campaign_eligible") is not None else False
        })
        return _obj


