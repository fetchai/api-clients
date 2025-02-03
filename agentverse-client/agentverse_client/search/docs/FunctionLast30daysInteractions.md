# FunctionLast30daysInteractions

The function last 30 days interactions response object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**function_id** | **str** | Unique identifier of the function | 
**total** | **List[int]** | the total number of interactions for each day | 

## Example

```python
from agentverse_client.search.models.function_last30days_interactions import FunctionLast30daysInteractions

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionLast30daysInteractions from a JSON string
function_last30days_interactions_instance = FunctionLast30daysInteractions.from_json(json)
# print the JSON string representation of the object
print(FunctionLast30daysInteractions.to_json())

# convert the object into a dict
function_last30days_interactions_dict = function_last30days_interactions_instance.to_dict()
# create an instance of FunctionLast30daysInteractions from a dict
function_last30days_interactions_from_dict = FunctionLast30daysInteractions.from_dict(function_last30days_interactions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


