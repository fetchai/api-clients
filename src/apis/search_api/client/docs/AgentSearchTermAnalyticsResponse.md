# AgentSearchTermAnalyticsResponse

The agent search term analytics response object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | 
**term_percentages** | [**List[SearchTermPercentage]**](SearchTermPercentage.md) |  | 

## Example

```python
from search_api_client.models.agent_search_term_analytics_response import AgentSearchTermAnalyticsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AgentSearchTermAnalyticsResponse from a JSON string
agent_search_term_analytics_response_instance = AgentSearchTermAnalyticsResponse.from_json(json)
# print the JSON string representation of the object
print(AgentSearchTermAnalyticsResponse.to_json())

# convert the object into a dict
agent_search_term_analytics_response_dict = agent_search_term_analytics_response_instance.to_dict()
# create an instance of AgentSearchTermAnalyticsResponse from a dict
agent_search_term_analytics_response_from_dict = AgentSearchTermAnalyticsResponse.from_dict(agent_search_term_analytics_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


