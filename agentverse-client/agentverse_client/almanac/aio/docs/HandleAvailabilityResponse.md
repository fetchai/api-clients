# HandleAvailabilityResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available** | **bool** |  | 
**handle** | **str** | The handle to be used for the agent. | 
**alternative** | **str** |  | [optional] 

## Example

```python
from agentverse_client.almanac.aio.models.handle_availability_response import HandleAvailabilityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HandleAvailabilityResponse from a JSON string
handle_availability_response_instance = HandleAvailabilityResponse.from_json(json)
# print the JSON string representation of the object
print(HandleAvailabilityResponse.to_json())

# convert the object into a dict
handle_availability_response_dict = handle_availability_response_instance.to_dict()
# create an instance of HandleAvailabilityResponse from a dict
handle_availability_response_from_dict = HandleAvailabilityResponse.from_dict(handle_availability_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


