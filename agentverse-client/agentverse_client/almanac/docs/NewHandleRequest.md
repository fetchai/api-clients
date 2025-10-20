# NewHandleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_address** | **str** | The address of the agent. | 
**handle** | **str** | The handle to be used for the agent. | 

## Example

```python
from agentverse_client.almanac.models.new_handle_request import NewHandleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NewHandleRequest from a JSON string
new_handle_request_instance = NewHandleRequest.from_json(json)
# print the JSON string representation of the object
print(NewHandleRequest.to_json())

# convert the object into a dict
new_handle_request_dict = new_handle_request_instance.to_dict()
# create an instance of NewHandleRequest from a dict
new_handle_request_from_dict = NewHandleRequest.from_dict(new_handle_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


