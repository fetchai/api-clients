# DelegationList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | **List[str]** | Agent addresses the authenticated owner has delegated to. | 

## Example

```python
from agentverse_client.storage.models.delegation_list import DelegationList

# TODO update the JSON string below
json = "{}"
# create an instance of DelegationList from a JSON string
delegation_list_instance = DelegationList.from_json(json)
# print the JSON string representation of the object
print(DelegationList.to_json())

# convert the object into a dict
delegation_list_dict = delegation_list_instance.to_dict()
# create an instance of DelegationList from a dict
delegation_list_from_dict = DelegationList.from_dict(delegation_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


