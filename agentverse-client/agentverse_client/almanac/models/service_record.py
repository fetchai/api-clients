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
from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List
from agentverse_client.almanac.models.endpoint_input import EndpointInput
from typing import Optional, Set
from typing_extensions import Self

class ServiceRecord(BaseModel):
    """
    ServiceRecord
    """ # noqa: E501
    agent_address: StrictStr
    protocols: List[StrictStr]
    endpoints: List[EndpointInput]
    expiry: datetime
    __properties: ClassVar[List[str]] = ["agent_address", "protocols", "endpoints", "expiry"]

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
        """Create an instance of ServiceRecord from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in endpoints (list)
        _items = []
        if self.endpoints:
            for _item_endpoints in self.endpoints:
                if _item_endpoints:
                    _items.append(_item_endpoints.to_dict())
            _dict['endpoints'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ServiceRecord from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "agent_address": obj.get("agent_address"),
            "protocols": obj.get("protocols"),
            "endpoints": [EndpointInput.from_dict(_item) for _item in obj["endpoints"]] if obj.get("endpoints") is not None else None,
            "expiry": obj.get("expiry")
        })
        return _obj


