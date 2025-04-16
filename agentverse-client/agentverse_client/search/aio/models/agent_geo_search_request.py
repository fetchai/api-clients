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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from agentverse_client.search.aio.models.agent_filters import AgentFilters
from agentverse_client.search.aio.models.agent_geo_filter import AgentGeoFilter
from agentverse_client.search.aio.models.direction import Direction
from agentverse_client.search.aio.models.relevancy_cutoff import RelevancyCutoff
from agentverse_client.search.aio.models.sort_type import SortType
from typing import Optional, Set
from typing_extensions import Self

class AgentGeoSearchRequest(BaseModel):
    """
    The agent geo search request object
    """ # noqa: E501
    filters: Optional[AgentFilters] = None
    sort: Optional[SortType] = Field(default=None, description="The type of sorting that should be applied to the search results")
    direction: Optional[Direction] = Field(default=None, description="The direction of the sorting, ascending or descending")
    cutoff: Optional[RelevancyCutoff] = Field(default=None, description="Controls how strictly the search results should be filtered based on their relevancy")
    search_text: Optional[StrictStr] = None
    semantic_search: Optional[StrictBool] = Field(default=False, description="Whether to perform semantic-based search, where agents semantically close to the search text rank highest. If not enabled, a keywords-based search is performed instead.")
    offset: Optional[StrictInt] = Field(default=0, description="The offset of the search results for pagination")
    limit: Optional[StrictInt] = Field(default=30, description="The limit of the search results for pagination")
    geo_filter: AgentGeoFilter = Field(description="The geo filter that can be applied to the search")
    search_id: Optional[StrictStr] = Field(default=None, description="Unique identifier of the search in question (search id generated before (previous search)).")
    source: Optional[StrictStr] = Field(default='', description="The source where the request is sent from. Ideally should be one of the following: '', 'agentverse', 'flockx', an agent address")
    __properties: ClassVar[List[str]] = ["filters", "sort", "direction", "cutoff", "search_text", "semantic_search", "offset", "limit", "geo_filter", "search_id", "source"]

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
        """Create an instance of AgentGeoSearchRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of filters
        if self.filters:
            _dict['filters'] = self.filters.to_dict()
        # override the default output from pydantic by calling `to_dict()` of geo_filter
        if self.geo_filter:
            _dict['geo_filter'] = self.geo_filter.to_dict()
        # set to None if search_text (nullable) is None
        # and model_fields_set contains the field
        if self.search_text is None and "search_text" in self.model_fields_set:
            _dict['search_text'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AgentGeoSearchRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "filters": AgentFilters.from_dict(obj["filters"]) if obj.get("filters") is not None else None,
            "sort": obj.get("sort"),
            "direction": obj.get("direction"),
            "cutoff": obj.get("cutoff"),
            "search_text": obj.get("search_text"),
            "semantic_search": obj.get("semantic_search") if obj.get("semantic_search") is not None else False,
            "offset": obj.get("offset") if obj.get("offset") is not None else 0,
            "limit": obj.get("limit") if obj.get("limit") is not None else 30,
            "geo_filter": AgentGeoFilter.from_dict(obj["geo_filter"]) if obj.get("geo_filter") is not None else None,
            "search_id": obj.get("search_id"),
            "source": obj.get("source") if obj.get("source") is not None else ''
        })
        return _obj


