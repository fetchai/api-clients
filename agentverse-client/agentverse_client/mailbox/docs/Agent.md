# Agent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Bech32 address of the agent | 
**prefix** | **str** | Prefix to distinguish agent&#39;s environment (e.g., &#39;test-agent&#39;) | 
**name** | **str** | Name of the agent | 
**pending_messages** | **int** | Number of pending messages for the agent | 
**bytes_transferred** | **int** | Total bytes transferred for this agent | 
**previous_bytes_transferred** | **int** | Previously recorded transferred bytes | 
**readme** | **str** |  | [optional] 
**avatar_url** | **str** |  | [optional] 
**short_description** | **str** |  | [optional] 
**agent_type** | **str** |  | [optional] 

## Example

```python
from agentverse_client.mailbox.models.agent import Agent

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


