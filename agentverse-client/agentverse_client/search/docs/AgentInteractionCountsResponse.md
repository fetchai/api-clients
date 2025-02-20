# AgentInteractionCountsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The address of the agent | 
**contract** | [**AgentContract**](AgentContract.md) | The Almanac contract where the agent is registered | [optional] 
**interval** | **List[int]** | the number of on_interval interactions for each day | 
**message** | **List[int]** | the number of on_message interactions for each day | 
**total** | **List[int]** | the sum of on_interval and on_message interaction counts for each day | 
**num_all_time_interactions** | [**AgentAllTimeInteractionCounts**](AgentAllTimeInteractionCounts.md) | number of on_interval, on_message and total (sum of on_interval and on_message) interactions | 

## Example

```python
from agentverse_client.search.models.agent_interaction_counts_response import AgentInteractionCountsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AgentInteractionCountsResponse from a JSON string
agent_interaction_counts_response_instance = AgentInteractionCountsResponse.from_json(json)
# print the JSON string representation of the object
print(AgentInteractionCountsResponse.to_json())

# convert the object into a dict
agent_interaction_counts_response_dict = agent_interaction_counts_response_instance.to_dict()
# create an instance of AgentInteractionCountsResponse from a dict
agent_interaction_counts_response_from_dict = AgentInteractionCountsResponse.from_dict(agent_interaction_counts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


