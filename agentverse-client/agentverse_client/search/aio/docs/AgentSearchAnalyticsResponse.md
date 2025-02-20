# AgentSearchAnalyticsResponse

The agent search analytics response object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The address of the agent | 
**contract** | [**AgentContract**](AgentContract.md) | The Almanac contract where the agent is registered | [optional] 
**num_searches** | **int** | Total number of searches when this agent was retrieved | 
**last_24h_num_searches** | **int** | Number of searches in the last 24 hours when this agent was retrieved | 
**last_30d_num_searches** | **int** | Number of searches in the last 30 days when this agent was retrieved | 
**last_30d_history** | **List[int]** | Number of searches per day in the last 30 days when this agent was retrieved | 

## Example

```python
from agentverse_client.search.aio.models.agent_search_analytics_response import AgentSearchAnalyticsResponse

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


