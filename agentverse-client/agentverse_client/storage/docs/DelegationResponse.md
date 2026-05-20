# DelegationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_address** | **str** | Agent address granted asset creation rights. | 
**owner** | **str** | User or team identifier that owns the delegation. | 

## Example

```python
from agentverse_client.storage.models.delegation_response import DelegationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DelegationResponse from a JSON string
delegation_response_instance = DelegationResponse.from_json(json)
# print the JSON string representation of the object
print(DelegationResponse.to_json())

# convert the object into a dict
delegation_response_dict = delegation_response_instance.to_dict()
# create an instance of DelegationResponse from a dict
delegation_response_from_dict = DelegationResponse.from_dict(delegation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


