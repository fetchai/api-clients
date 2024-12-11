# AgentSearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agents** | [**List[Agent]**](Agent.md) |  | [optional] 
**offset** | **int** |  | 
**limit** | **int** |  | 
**num_hits** | **int** |  | 
**total** | **int** |  | 
**search_id** | **str** |  | 

## Example

```python
from search_api_client.models.agent_search_response import AgentSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AgentSearchResponse from a JSON string
agent_search_response_instance = AgentSearchResponse.from_json(json)
# print the JSON string representation of the object
print(AgentSearchResponse.to_json())

# convert the object into a dict
agent_search_response_dict = agent_search_response_instance.to_dict()
# create an instance of AgentSearchResponse from a dict
agent_search_response_from_dict = AgentSearchResponse.from_dict(agent_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


