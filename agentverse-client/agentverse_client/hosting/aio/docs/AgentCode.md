# AgentCode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**digest** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 

## Example

```python
from agentverse_client.hosting.aio.models.agent_code import AgentCode

# TODO update the JSON string below
json = "{}"
# create an instance of AgentCode from a JSON string
agent_code_instance = AgentCode.from_json(json)
# print the JSON string representation of the object
print(AgentCode.to_json())

# convert the object into a dict
agent_code_dict = agent_code_instance.to_dict()
# create an instance of AgentCode from a dict
agent_code_from_dict = AgentCode.from_dict(agent_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


