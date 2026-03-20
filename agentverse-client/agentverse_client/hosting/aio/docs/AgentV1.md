# AgentV1

V1 Agent model with complete profile information.

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
**metadata** | [**AgentMetadata**](AgentMetadata.md) |  | [optional] 

## Example

```python
from agentverse_client.hosting.aio.models.agent_v1 import AgentV1

# TODO update the JSON string below
json = "{}"
# create an instance of AgentV1 from a JSON string
agent_v1_instance = AgentV1.from_json(json)
# print the JSON string representation of the object
print(AgentV1.to_json())

# convert the object into a dict
agent_v1_dict = agent_v1_instance.to_dict()
# create an instance of AgentV1 from a dict
agent_v1_from_dict = AgentV1.from_dict(agent_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


