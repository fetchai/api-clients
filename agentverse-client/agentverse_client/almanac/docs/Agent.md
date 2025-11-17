# Agent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**AgentStatus**](AgentStatus.md) |  | 
**type** | **str** | Type/category of the agent | 
**address** | **str** | Unique blockchain address of the agent | 
**domain_name** | **str** |  | [optional] 
**endpoints** | [**List[AgentEndpoint]**](AgentEndpoint.md) | List of agent&#39;s endpoints | 
**metadata** | **Dict[str, object]** |  | [optional] 
**protocols** | **List[str]** | Supported protocol identifiers | 
**expiry** | **datetime** | Expiration timestamp of the agent | 

## Example

```python
from agentverse_client.almanac.models.agent import Agent

# TODO update the JSON string below
json = "{}"
# create an instance of Agent from a JSON string
agent_instance = Agent.from_json(json)
# print the JSON string representation of the object
print(Agent.to_json())

# convert the object into a dict
agent_dict = agent_instance.to_dict()
# create an instance of Agent from a dict
agent_from_dict = Agent.from_dict(agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


