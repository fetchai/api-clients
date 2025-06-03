# NewPermission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_address** | **str** | Address of the agent to whom the permission applies. | 
**read** | **bool** | Whether the agent has read access. | 
**write** | **bool** | Whether the agent has write access. | 

## Example

```python
from agentverse_client.storage.models.new_permission import NewPermission

# TODO update the JSON string below
json = "{}"
# create an instance of NewPermission from a JSON string
new_permission_instance = NewPermission.from_json(json)
# print the JSON string representation of the object
print(NewPermission.to_json())

# convert the object into a dict
new_permission_dict = new_permission_instance.to_dict()
# create an instance of NewPermission from a dict
new_permission_from_dict = NewPermission.from_dict(new_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


