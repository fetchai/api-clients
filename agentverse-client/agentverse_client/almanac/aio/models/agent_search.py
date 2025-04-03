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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from agentverse_client.almanac.aio.models.agent_network import AgentNetwork
from agentverse_client.almanac.aio.models.agent_status_filter import AgentStatusFilter
from agentverse_client.almanac.aio.models.agent_type import AgentType
from agentverse_client.almanac.aio.models.developer_category import DeveloperCategory
from agentverse_client.almanac.aio.models.sort_agents import SortAgents
from typing import Optional, Set
from typing_extensions import Self

class AgentSearch(BaseModel):
    """
    AgentSearch
    """ # noqa: E501
    text: StrictStr = Field(description="Free-text search query")
    protocols: Optional[List[StrictStr]] = None
    types: Optional[List[AgentType]] = None
    status: Optional[List[AgentStatusFilter]] = None
    dev_categories: Optional[List[DeveloperCategory]] = None
    limit: Optional[StrictInt] = None
    network: Optional[AgentNetwork] = None
    sort: Optional[SortAgents] = None
    __properties: ClassVar[List[str]] = ["text", "protocols", "types", "status", "dev_categories", "limit", "network", "sort"]

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
        """Create an instance of AgentSearch from a JSON string"""
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
        # set to None if protocols (nullable) is None
        # and model_fields_set contains the field
        if self.protocols is None and "protocols" in self.model_fields_set:
            _dict['protocols'] = None

        # set to None if types (nullable) is None
        # and model_fields_set contains the field
        if self.types is None and "types" in self.model_fields_set:
            _dict['types'] = None

        # set to None if status (nullable) is None
        # and model_fields_set contains the field
        if self.status is None and "status" in self.model_fields_set:
            _dict['status'] = None

        # set to None if dev_categories (nullable) is None
        # and model_fields_set contains the field
        if self.dev_categories is None and "dev_categories" in self.model_fields_set:
            _dict['dev_categories'] = None

        # set to None if limit (nullable) is None
        # and model_fields_set contains the field
        if self.limit is None and "limit" in self.model_fields_set:
            _dict['limit'] = None

        # set to None if network (nullable) is None
        # and model_fields_set contains the field
        if self.network is None and "network" in self.model_fields_set:
            _dict['network'] = None

        # set to None if sort (nullable) is None
        # and model_fields_set contains the field
        if self.sort is None and "sort" in self.model_fields_set:
            _dict['sort'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AgentSearch from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "text": obj.get("text"),
            "protocols": obj.get("protocols"),
            "types": obj.get("types"),
            "status": obj.get("status"),
            "dev_categories": obj.get("dev_categories"),
            "limit": obj.get("limit"),
            "network": obj.get("network"),
            "sort": obj.get("sort")
        })
        return _obj


