# AgentSearchAnalyticsResponse

The agent search analytics response object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | 
**num_searches** | **int** |  | 
**last_24h_num_searches** | **int** |  | 
**last_30d_num_searches** | **int** |  | 
**last_30d_history** | **List[int]** |  | 

## Example

```python
from search_api_client.models.agent_search_analytics_response import AgentSearchAnalyticsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AgentSearchAnalyticsResponse from a JSON string
agent_search_analytics_response_instance = AgentSearchAnalyticsResponse.from_json(json)
# print the JSON string representation of the object
print(AgentSearchAnalyticsResponse.to_json())

# convert the object into a dict
agent_search_analytics_response_dict = agent_search_analytics_response_instance.to_dict()
# create an instance of AgentSearchAnalyticsResponse from a dict
agent_search_analytics_response_from_dict = AgentSearchAnalyticsResponse.from_dict(agent_search_analytics_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


