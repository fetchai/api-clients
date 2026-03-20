# AgentV2

Agent model for v2 API - excludes profile fields (name, domain, readme, avatar_url, short_description).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Bech32 address of the agent. | 
**running** | **bool** | Whether the agent is currently running. | 
**compiled** | **bool** |  | [optional] 
**code_digest** | **str** |  | [optional] 
**wallet_address** | **str** |  | [optional] 
**code_update_timestamp** | **datetime** |  | [optional] 
**creation_timestamp** | **datetime** |  | [optional] 
**revision** | **int** | Revision number of the agent. | [optional] [default to 0]
**metadata** | [**AgentMetadata**](AgentMetadata.md) |  | [optional] 

## Example

```python
from agentverse_client.hosting.aio.models.agent_v2 import AgentV2

# TODO update the JSON string below
json = "{}"
# create an instance of AgentV2 from a JSON string
agent_v2_instance = AgentV2.from_json(json)
# print the JSON string representation of the object
print(AgentV2.to_json())

# convert the object into a dict
agent_v2_dict = agent_v2_instance.to_dict()
# create an instance of AgentV2 from a dict
agent_v2_from_dict = AgentV2.from_dict(agent_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


