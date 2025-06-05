# AgentLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log_timestamp** | **datetime** |  | 
**log_entry** | **str** |  | 
**log_type** | [**LogType**](LogType.md) |  | [optional] 
**log_level** | [**LogLevel**](LogLevel.md) |  | [optional] 

## Example

```python
from agentverse_client.hosting.aio.models.agent_log import AgentLog

# TODO update the JSON string below
json = "{}"
# create an instance of AgentLog from a JSON string
agent_log_instance = AgentLog.from_json(json)
# print the JSON string representation of the object
print(AgentLog.to_json())

# convert the object into a dict
agent_log_dict = agent_log_instance.to_dict()
# create an instance of AgentLog from a dict
agent_log_from_dict = AgentLog.from_dict(agent_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


