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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from agentverse_client.search.aio.models.function import Function
from typing import Optional, Set
from typing_extensions import Self

class FunctionSearchResponse(BaseModel):
    """
    The function search response object
    """ # noqa: E501
    functions: Optional[List[Function]] = Field(default=None, description="The list of functions that match the search criteria")
    offset: StrictInt = Field(description="The offset of the first function in the search results for pagination")
    limit: StrictInt = Field(description="The limit of the search results for pagination")
    num_hits: StrictInt = Field(description="The number of hits might be smaller than the total number of hits (`total`) when using offset and limit")
    total: StrictInt = Field(description="The total number of hits might be bigger than the actual number of hits (`num_hits`) when using offset and limit")
    __properties: ClassVar[List[str]] = ["functions", "offset", "limit", "num_hits", "total"]

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
        """Create an instance of FunctionSearchResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in functions (list)
        _items = []
        if self.functions:
            for _item_functions in self.functions:
                if _item_functions:
                    _items.append(_item_functions.to_dict())
            _dict['functions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FunctionSearchResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "functions": [Function.from_dict(_item) for _item in obj["functions"]] if obj.get("functions") is not None else None,
            "offset": obj.get("offset"),
            "limit": obj.get("limit"),
            "num_hits": obj.get("num_hits"),
            "total": obj.get("total")
        })
        return _obj


