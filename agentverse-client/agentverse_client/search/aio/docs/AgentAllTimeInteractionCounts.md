# AgentAllTimeInteractionCounts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval** | **int** | number of on_interval interactions | 
**message** | **int** | number of on_message interactions | 
**total** | **int** | the sum of on_interval and on_message interaction counts | 

## Example

```python
from agentverse_client.search.aio.models.agent_all_time_interaction_counts import AgentAllTimeInteractionCounts

# TODO update the JSON string below
json = "{}"
# create an instance of AgentAllTimeInteractionCounts from a JSON string
agent_all_time_interaction_counts_instance = AgentAllTimeInteractionCounts.from_json(json)
# print the JSON string representation of the object
print(AgentAllTimeInteractionCounts.to_json())

# convert the object into a dict
agent_all_time_interaction_counts_dict = agent_all_time_interaction_counts_instance.to_dict()
# create an instance of AgentAllTimeInteractionCounts from a dict
agent_all_time_interaction_counts_from_dict = AgentAllTimeInteractionCounts.from_dict(agent_all_time_interaction_counts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


