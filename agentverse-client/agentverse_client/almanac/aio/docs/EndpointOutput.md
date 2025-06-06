# EndpointOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Endpoint URL | 
**weight** | **int** | Relative weight for load balancing or priority | 

## Example

```python
from agentverse_client.almanac.aio.models.endpoint_output import EndpointOutput

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointOutput from a JSON string
endpoint_output_instance = EndpointOutput.from_json(json)
# print the JSON string representation of the object
print(EndpointOutput.to_json())

# convert the object into a dict
endpoint_output_dict = endpoint_output_instance.to_dict()
# create an instance of EndpointOutput from a dict
endpoint_output_from_dict = EndpointOutput.from_dict(endpoint_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


