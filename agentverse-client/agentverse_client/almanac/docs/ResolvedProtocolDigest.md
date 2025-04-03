# ResolvedProtocolDigest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**digest** | **str** |  | 
**name** | **str** |  | 
**version** | **str** |  | 

## Example

```python
from agentverse_client.almanac.models.resolved_protocol_digest import ResolvedProtocolDigest

# TODO update the JSON string below
json = "{}"
# create an instance of ResolvedProtocolDigest from a JSON string
resolved_protocol_digest_instance = ResolvedProtocolDigest.from_json(json)
# print the JSON string representation of the object
print(ResolvedProtocolDigest.to_json())

# convert the object into a dict
resolved_protocol_digest_dict = resolved_protocol_digest_instance.to_dict()
# create an instance of ResolvedProtocolDigest from a dict
resolved_protocol_digest_from_dict = ResolvedProtocolDigest.from_dict(resolved_protocol_digest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


