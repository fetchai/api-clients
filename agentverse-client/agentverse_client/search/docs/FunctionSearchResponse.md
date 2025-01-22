# FunctionSearchResponse

The function search response object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**functions** | [**List[Function]**](Function.md) | The list of functions that match the search criteria | [optional] 
**offset** | **int** | The offset of the first function in the search results for pagination | 
**limit** | **int** | The limit of the search results for pagination | 
**num_hits** | **int** | The number of hits might be smaller than the total number of hits (&#x60;total&#x60;) when using offset and limit | 
**total** | **int** | The total number of hits might be bigger than the actual number of hits (&#x60;num_hits&#x60;) when using offset and limit | 

## Example

```python
from agentverse_client.search.models.function_search_response import FunctionSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionSearchResponse from a JSON string
function_search_response_instance = FunctionSearchResponse.from_json(json)
# print the JSON string representation of the object
print(FunctionSearchResponse.to_json())

# convert the object into a dict
function_search_response_dict = function_search_response_instance.to_dict()
# create an instance of FunctionSearchResponse from a dict
function_search_response_from_dict = FunctionSearchResponse.from_dict(function_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


