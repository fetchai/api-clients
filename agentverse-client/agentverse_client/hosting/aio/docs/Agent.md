# Agent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the agent. | 
**address** | **str** | Bech32 address of the agent. | 
**domain** | **str** |  | [optional] 
**prefix** | **str** |  | [optional] 
**running** | **bool** | Whether the agent is currently running. | 
**compiled** | **bool** |  | [optional] 
**code_digest** | **str** |  | [optional] 
**wallet_address** | **str** |  | [optional] 
**code_update_timestamp** | **datetime** |  | [optional] 
**creation_timestamp** | **datetime** |  | [optional] 
**avatar_url** | **str** |  | [optional] 
**maintainer_id** | **str** |  | [optional] 
**revision** | **int** | Revision number of the agent. | 
**readme** | **str** |  | [optional] 
**short_description** | **str** |  | [optional] 
**wallet_messaging_enabled** | **bool** |  | [optional] 
**fire_hosting_enabled** | **bool** |  | [optional] 
**total_interactions** | **int** |  | [optional] 

## Example

```python
from agentverse_client.hosting.aio.models.agent import Agent

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


