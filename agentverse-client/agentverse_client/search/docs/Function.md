# Function


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the identifier of the function | 
**type** | [**FunctionType**](FunctionType.md) | the type of the function / action | 
**name** | **str** | the name of the function | 
**agent** | **str** | the agent that the function belongs to | 
**description** | **str** | the description of the function | 
**is_primary** | **bool** | denotes if a function is primary or not | 
**groups** | **List[str]** | group that the function belongs to | [optional] 
**total_interactions** | **int** | the total interactions for this function | 
**recent_interactions** | **int** | the number of interactions in the last 90 days | 
**rating** | **float** |  | [optional] 
**featured** | **bool** | signaled if the function is featured or not | [optional] [default to False]
**last_updated** | **datetime** | the time at which the function was last updated at | 
**created_at** | **datetime** | the time at which the function was first visible or created | 

## Example

```python
from agentverse_client.search.models.function import Function

# TODO update the JSON string below
json = "{}"
# create an instance of Function from a JSON string
function_instance = Function.from_json(json)
# print the JSON string representation of the object
print(Function.to_json())

# convert the object into a dict
function_dict = function_instance.to_dict()
# create an instance of Function from a dict
function_from_dict = Function.from_dict(function_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


