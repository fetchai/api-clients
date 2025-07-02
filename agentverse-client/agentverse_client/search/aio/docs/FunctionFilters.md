# FunctionFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**function_type** | [**List[FunctionType]**](FunctionType.md) | The type of the function to search for | [optional] 

## Example

```python
from agentverse_client.search.aio.models.function_filters import FunctionFilters

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionFilters from a JSON string
function_filters_instance = FunctionFilters.from_json(json)
# print the JSON string representation of the object
print(FunctionFilters.to_json())

# convert the object into a dict
function_filters_dict = function_filters_instance.to_dict()
# create an instance of FunctionFilters from a dict
function_filters_from_dict = FunctionFilters.from_dict(function_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


