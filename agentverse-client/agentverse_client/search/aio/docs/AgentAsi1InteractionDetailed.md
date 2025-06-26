# AgentAsi1InteractionDetailed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_identifier** | **str** |  | 
**from_verifier** | **bool** |  | [optional] [default to False]
**request** | **str** |  | 
**response** | **str** |  | 
**success** | **bool** |  | 
**timestamp** | **str** |  | [optional] 

## Example

```python
from agentverse_client.search.aio.models.agent_asi1_interaction_detailed import AgentAsi1InteractionDetailed

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


