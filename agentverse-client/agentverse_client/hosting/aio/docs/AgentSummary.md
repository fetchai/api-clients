# AgentSummary


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

## Example

```python
from agentverse_client.hosting.aio.models.agent_summary import AgentSummary

# TODO update the JSON string below
json = "{}"
# create an instance of AgentSummary from a JSON string
agent_summary_instance = AgentSummary.from_json(json)
# print the JSON string representation of the object
print(AgentSummary.to_json())

# convert the object into a dict
agent_summary_dict = agent_summary_instance.to_dict()
# create an instance of AgentSummary from a dict
agent_summary_from_dict = AgentSummary.from_dict(agent_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


