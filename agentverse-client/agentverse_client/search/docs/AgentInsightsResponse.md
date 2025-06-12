# AgentInsightsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The address of the agent | 
**contract** | [**AgentContract**](AgentContract.md) | The Almanac contract where the agent is registered | [optional] 
**asi1_total_interactions** | **int** | The total number of interactions with ASI:One. | 
**asi1_total_success_interactions** | **int** | The total number of interactions with ASI:One that were deemed successful. | 
**asi1_recent_interactions** | **int** | The number of interactions with ASI:One in the last 30 days. | 
**asi1_recent_success_interactions** | **int** | The number of interactions with ASI:One in the last 30 days that were deemed successful. | 
**verifier_total_interactions** | **int** | The total number of interactions with the verifier agent. | 
**verifier_total_success_interactions** | **int** | The total number of interactions with the verifier agent that were deemed successful. | 
**verifier_recent_interactions** | **int** | The number of interactions with the verifier agent in the last 30 days. | 
**verifier_recent_success_interactions** | **int** | The number of interactions with the verifier agent in the last 30 days that were deemed successful. | 
**readme_uniqueness_score** | **float** |  | [optional] 
**readme_quality_score** | **float** |  | [optional] 
**interactions_score** | **float** |  | [optional] 
**rating** | **float** | A score from 0 to 5, representing the rating of the agent. It takes different factors into account. | 

## Example

```python
from agentverse_client.search.models.agent_insights_response import AgentInsightsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AgentInsightsResponse from a JSON string
agent_insights_response_instance = AgentInsightsResponse.from_json(json)
# print the JSON string representation of the object
print(AgentInsightsResponse.to_json())

# convert the object into a dict
agent_insights_response_dict = agent_insights_response_instance.to_dict()
# create an instance of AgentInsightsResponse from a dict
agent_insights_response_from_dict = AgentInsightsResponse.from_dict(agent_insights_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


