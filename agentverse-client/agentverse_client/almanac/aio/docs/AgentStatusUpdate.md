# AgentStatusUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_identifier** | **str** |  | 
**signature** | **str** |  | [optional] 
**timestamp** | **int** |  | [optional] 
**is_active** | **bool** | Indicates whether the agent is currently active | 

## Example

```python
from agentverse_client.almanac.aio.models.agent_status_update import AgentStatusUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of AgentStatusUpdate from a JSON string
agent_status_update_instance = AgentStatusUpdate.from_json(json)
# print the JSON string representation of the object
print(AgentStatusUpdate.to_json())

# convert the object into a dict
agent_status_update_dict = agent_status_update_instance.to_dict()
# create an instance of AgentStatusUpdate from a dict
agent_status_update_from_dict = AgentStatusUpdate.from_dict(agent_status_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


