# FunctionSearchRequest

The function search request object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**FunctionFilters**](FunctionFilters.md) |  | [optional] 
**sort** | **str** |  | [optional] [default to 'relevancy']
**direction** | **str** |  | [optional] [default to 'asc']
**search_text** | **str** |  | [optional] 
**offset** | **int** |  | [optional] [default to 0]
**limit** | **int** |  | [optional] [default to 30]

## Example

```python
from search_api_client.models.function_search_request import FunctionSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionSearchRequest from a JSON string
function_search_request_instance = FunctionSearchRequest.from_json(json)
# print the JSON string representation of the object
print(FunctionSearchRequest.to_json())

# convert the object into a dict
function_search_request_dict = function_search_request_instance.to_dict()
# create an instance of FunctionSearchRequest from a dict
function_search_request_from_dict = FunctionSearchRequest.from_dict(function_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


