# AgentSearchTermAnalyticsRequest

The agent search term analytics request object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The address of the agent | 
**contract** | [**AgentContract**](AgentContract.md) | The Almanac contract where the agent is registered | [optional] 
**top** | **int** | How many of the top mostly used search terms we want to retrieve analytics for | [optional] [default to 10]

## Example

```python
from agentverse_client.search.aio.models.agent_search_term_analytics_request import AgentSearchTermAnalyticsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgentSearchTermAnalyticsRequest from a JSON string
agent_search_term_analytics_request_instance = AgentSearchTermAnalyticsRequest.from_json(json)
# print the JSON string representation of the object
print(AgentSearchTermAnalyticsRequest.to_json())

# convert the object into a dict
agent_search_term_analytics_request_dict = agent_search_term_analytics_request_instance.to_dict()
# create an instance of AgentSearchTermAnalyticsRequest from a dict
agent_search_term_analytics_request_from_dict = AgentSearchTermAnalyticsRequest.from_dict(agent_search_term_analytics_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


