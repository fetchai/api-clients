# PublicAgentV1

V1 Public agent model with profile fields.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the agent. | 
**author_username** | **str** | Username of the agent&#39;s author. | 
**address** | **str** | Bech32 address of the agent. | 
**domain** | **str** |  | [optional] 
**prefix** | **str** |  | [optional] 
**running** | **bool** | Indicates if the agent is currently running. | 
**readme** | **str** |  | [optional] 
**short_description** | **str** |  | [optional] 
**last_updated_at** | **datetime** | Timestamp when the agent was last updated. | 
**created_at** | **datetime** | Timestamp when the agent was created. | 
**maintainer_id** | **str** |  | [optional] 
**avatar_url** | **str** |  | [optional] 
**metadata** | [**AgentMetadata**](AgentMetadata.md) |  | [optional] 

## Example

```python
from agentverse_client.hosting.aio.models.public_agent_v1 import PublicAgentV1

# TODO update the JSON string below
json = "{}"
# create an instance of PublicAgentV1 from a JSON string
public_agent_v1_instance = PublicAgentV1.from_json(json)
# print the JSON string representation of the object
print(PublicAgentV1.to_json())

# convert the object into a dict
public_agent_v1_dict = public_agent_v1_instance.to_dict()
# create an instance of PublicAgentV1 from a dict
public_agent_v1_from_dict = PublicAgentV1.from_dict(public_agent_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


