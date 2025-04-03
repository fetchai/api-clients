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

from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class Model(BaseModel):
    """
    Model
    """ # noqa: E501
    digest: Annotated[str, Field(strict=True)] = Field(description="Content-addressed hash of the model")
    var_schema: Optional[Any] = Field(default=None, description="JSON schema definition of the model", alias="schema")
    __properties: ClassVar[List[str]] = ["digest", "schema"]

    @field_validator('digest')
    def digest_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^model:[0-9a-f]{64}$", value):
            raise ValueError(r"must validate the regular expression /^model:[0-9a-f]{64}$/")
        return value

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
        """Create an instance of Model from a JSON string"""
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
        # set to None if var_schema (nullable) is None
        # and model_fields_set contains the field
        if self.var_schema is None and "var_schema" in self.model_fields_set:
            _dict['schema'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Model from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "digest": obj.get("digest"),
            "schema": obj.get("schema")
        })
        return _obj


