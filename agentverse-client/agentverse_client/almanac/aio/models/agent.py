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
from agentverse_client.almanac.aio.models.address_prefix import AddressPrefix
from agentverse_client.almanac.aio.models.agent_status import AgentStatus
from agentverse_client.almanac.aio.models.agent_type import AgentType
from agentverse_client.almanac.aio.models.developer_category import DeveloperCategory
from agentverse_client.almanac.aio.models.endpoint_output import EndpointOutput
from typing import Optional, Set
from typing_extensions import Self

class Agent(BaseModel):
    """
    Agent
    """ # noqa: E501
    status: AgentStatus
    type: AgentType
    address: StrictStr = Field(description="Unique blockchain address of the agent")
    domain_name: Optional[StrictStr] = None
    prefix: Optional[AddressPrefix] = None
    endpoints: List[EndpointOutput] = Field(description="List of agent's endpoints")
    metadata: Optional[Dict[str, Any]] = None
    protocols: List[StrictStr] = Field(description="Supported protocol identifiers")
    expiry: datetime = Field(description="Expiration timestamp of the agent")
    developer_category: Optional[DeveloperCategory] = None
    name: Optional[StrictStr] = None
    running: Optional[StrictBool] = None
    maintainer_id: Optional[StrictStr] = None
    username: Optional[StrictStr] = None
    code_update_timestamp: Optional[datetime] = None
    total_interactions: Optional[StrictInt] = None
    trust_score: Optional[Union[StrictFloat, StrictInt]] = None
    __properties: ClassVar[List[str]] = ["status", "type", "address", "domain_name", "prefix", "endpoints", "metadata", "protocols", "expiry", "developer_category", "name", "running", "maintainer_id", "username", "code_update_timestamp", "total_interactions", "trust_score"]

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
        # override the default output from pydantic by calling `to_dict()` of each item in endpoints (list)
        _items = []
        if self.endpoints:
            for _item_endpoints in self.endpoints:
                if _item_endpoints:
                    _items.append(_item_endpoints.to_dict())
            _dict['endpoints'] = _items
        # set to None if domain_name (nullable) is None
        # and model_fields_set contains the field
        if self.domain_name is None and "domain_name" in self.model_fields_set:
            _dict['domain_name'] = None

        # set to None if prefix (nullable) is None
        # and model_fields_set contains the field
        if self.prefix is None and "prefix" in self.model_fields_set:
            _dict['prefix'] = None

        # set to None if metadata (nullable) is None
        # and model_fields_set contains the field
        if self.metadata is None and "metadata" in self.model_fields_set:
            _dict['metadata'] = None

        # set to None if developer_category (nullable) is None
        # and model_fields_set contains the field
        if self.developer_category is None and "developer_category" in self.model_fields_set:
            _dict['developer_category'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if running (nullable) is None
        # and model_fields_set contains the field
        if self.running is None and "running" in self.model_fields_set:
            _dict['running'] = None

        # set to None if maintainer_id (nullable) is None
        # and model_fields_set contains the field
        if self.maintainer_id is None and "maintainer_id" in self.model_fields_set:
            _dict['maintainer_id'] = None

        # set to None if username (nullable) is None
        # and model_fields_set contains the field
        if self.username is None and "username" in self.model_fields_set:
            _dict['username'] = None

        # set to None if code_update_timestamp (nullable) is None
        # and model_fields_set contains the field
        if self.code_update_timestamp is None and "code_update_timestamp" in self.model_fields_set:
            _dict['code_update_timestamp'] = None

        # set to None if total_interactions (nullable) is None
        # and model_fields_set contains the field
        if self.total_interactions is None and "total_interactions" in self.model_fields_set:
            _dict['total_interactions'] = None

        # set to None if trust_score (nullable) is None
        # and model_fields_set contains the field
        if self.trust_score is None and "trust_score" in self.model_fields_set:
            _dict['trust_score'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Agent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "status": obj.get("status"),
            "type": obj.get("type"),
            "address": obj.get("address"),
            "domain_name": obj.get("domain_name"),
            "prefix": obj.get("prefix"),
            "endpoints": [EndpointOutput.from_dict(_item) for _item in obj["endpoints"]] if obj.get("endpoints") is not None else None,
            "metadata": obj.get("metadata"),
            "protocols": obj.get("protocols"),
            "expiry": obj.get("expiry"),
            "developer_category": obj.get("developer_category"),
            "name": obj.get("name"),
            "running": obj.get("running"),
            "maintainer_id": obj.get("maintainer_id"),
            "username": obj.get("username"),
            "code_update_timestamp": obj.get("code_update_timestamp"),
            "total_interactions": obj.get("total_interactions"),
            "trust_score": obj.get("trust_score")
        })
        return _obj


