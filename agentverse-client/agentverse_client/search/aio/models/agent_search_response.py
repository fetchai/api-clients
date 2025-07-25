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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from agentverse_client.search.aio.models.agent import Agent
from typing import Optional, Set
from typing_extensions import Self

class AgentSearchResponse(BaseModel):
    """
    AgentSearchResponse
    """ # noqa: E501
    agents: Optional[List[Agent]] = Field(default=None, description="The list of agents that are returned as part of the search")
    offset: StrictInt = Field(description="The offset of the search results")
    limit: StrictInt = Field(description="The limit of the search results")
    num_hits: StrictInt = Field(description="The number of hits might be smaller than the total number of hits (`total`) when using offset and limit")
    total: StrictInt = Field(description="The total number of hits might be bigger than the actual number of hits (`num_hits`)` when using offset and limit")
    search_id: StrictStr = Field(description="Id passed to the search in the request payload / generated for the search (if not passed in the payload).  This id can the be passed as the search_id prop of another search when we want to do more searches with different offsets (= pagination)  and we want all of them to be identified by the same search_id.  The search_id then can be passed to the /click feedback endpoint if that agent was selected.  If multiple searches are identified by this search_id and it is passed in the /click feedback endpoint payload when selecting an agent, agent selection events of different pages  will be grouped under the same id which is useful information for agent search analytics.")
    __properties: ClassVar[List[str]] = ["agents", "offset", "limit", "num_hits", "total", "search_id"]

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
        """Create an instance of AgentSearchResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in agents (list)
        _items = []
        if self.agents:
            for _item_agents in self.agents:
                if _item_agents:
                    _items.append(_item_agents.to_dict())
            _dict['agents'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AgentSearchResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "agents": [Agent.from_dict(_item) for _item in obj["agents"]] if obj.get("agents") is not None else None,
            "offset": obj.get("offset"),
            "limit": obj.get("limit"),
            "num_hits": obj.get("num_hits"),
            "total": obj.get("total"),
            "search_id": obj.get("search_id")
        })
        return _obj


