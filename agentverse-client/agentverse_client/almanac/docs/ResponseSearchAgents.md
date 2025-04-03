# ResponseSearchAgents


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**List[Agent]**](Agent.md) |  | 
**total** | **int** |  | 
**page_size** | **int** |  | 
**tracker_last_update** | **datetime** |  | [optional] 

## Example

```python
from agentverse_client.almanac.models.response_search_agents import ResponseSearchAgents

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseSearchAgents from a JSON string
response_search_agents_instance = ResponseSearchAgents.from_json(json)
# print the JSON string representation of the object
print(ResponseSearchAgents.to_json())

# convert the object into a dict
response_search_agents_dict = response_search_agents_instance.to_dict()
# create an instance of ResponseSearchAgents from a dict
response_search_agents_from_dict = ResponseSearchAgents.from_dict(response_search_agents_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


