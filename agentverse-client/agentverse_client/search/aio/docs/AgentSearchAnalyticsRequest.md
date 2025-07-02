# AgentSearchAnalyticsRequest

The agent search analytics request object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The address of the agent | 
**contract** | [**AgentContract**](AgentContract.md) | The Almanac contract where the agent is registered | [optional] 

## Example

```python
from agentverse_client.search.aio.models.agent_search_analytics_request import AgentSearchAnalyticsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgentSearchAnalyticsRequest from a JSON string
agent_search_analytics_request_instance = AgentSearchAnalyticsRequest.from_json(json)
# print the JSON string representation of the object
print(AgentSearchAnalyticsRequest.to_json())

# convert the object into a dict
agent_search_analytics_request_dict = agent_search_analytics_request_instance.to_dict()
# create an instance of AgentSearchAnalyticsRequest from a dict
agent_search_analytics_request_from_dict = AgentSearchAnalyticsRequest.from_dict(agent_search_analytics_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


