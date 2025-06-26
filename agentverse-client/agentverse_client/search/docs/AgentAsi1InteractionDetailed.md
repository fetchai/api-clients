# AgentAsi1InteractionDetailed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The address of the agent | 
**contract** | [**AgentContract**](AgentContract.md) | The Almanac contract where the agent is registered | [optional] 
**success** | **bool** | Denotes if agent execution by ASI1 was successful or not. | 
**request** | **str** | Message sent to the agent. | 
**response** | **str** | Response received from the agent. | 
**from_verifier** | **bool** | Denotes if the interaction came from the verifier agent. By default it&#39;s False - means it is an actual ASI1-agent interaction. | 
**timestamp** | **str** |  | 

## Example

```python
from agentverse_client.search.models.agent_asi1_interaction_detailed import AgentAsi1InteractionDetailed

# TODO update the JSON string below
json = "{}"
# create an instance of AgentAsi1InteractionDetailed from a JSON string
agent_asi1_interaction_detailed_instance = AgentAsi1InteractionDetailed.from_json(json)
# print the JSON string representation of the object
print(AgentAsi1InteractionDetailed.to_json())

# convert the object into a dict
agent_asi1_interaction_detailed_dict = agent_asi1_interaction_detailed_instance.to_dict()
# create an instance of AgentAsi1InteractionDetailed from a dict
agent_asi1_interaction_detailed_from_dict = AgentAsi1InteractionDetailed.from_dict(agent_asi1_interaction_detailed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


