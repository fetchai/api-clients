# AgentUpdates


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Updated name of the agent. | 
**readme** | **str** |  | [optional] 
**avatar_url** | **str** |  | [optional] 
**short_description** | **str** |  | [optional] 
**agent_type** | **str** |  | [optional] 

## Example

```python
from agentverse_client.mailbox.models.agent_updates import AgentUpdates

# TODO update the JSON string below
json = "{}"
# create an instance of AgentUpdates from a JSON string
agent_updates_instance = AgentUpdates.from_json(json)
# print the JSON string representation of the object
print(AgentUpdates.to_json())

# convert the object into a dict
agent_updates_dict = agent_updates_instance.to_dict()
# create an instance of AgentUpdates from a dict
agent_updates_from_dict = AgentUpdates.from_dict(agent_updates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


