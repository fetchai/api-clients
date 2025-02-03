# AgentFilters

The set of filters that should be applied to the agent search entries

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | [**List[StatusType]**](StatusType.md) | The state of the agent, i.e. is it alive or not | [optional] 
**category** | [**List[AgentCategory]**](AgentCategory.md) | The category of the creator of the agent | [optional] 
**agent_type** | [**List[AgentType]**](AgentType.md) | The category of how the agent is hosted | [optional] 
**protocol_digest** | **List[str]** | The digest(s) of the protocol(s) that belong(s) to the agent | [optional] 
**has_location** | **bool** | If set to True, it will filter for agents that have a geo location specified | [optional] [default to False]
**has_readme** | **bool** | If set to True, it will filter for agents that have a non-empty readme | [optional] [default to False]
**n_interactions** | [**InteractionsThreshold**](InteractionsThreshold.md) |  | [optional] 
**tags** | **List[str]** | The tag(s) associated to the agent | [optional] 

## Example

```python
from agentverse_client.search.models.agent_filters import AgentFilters

# TODO update the JSON string below
json = "{}"
# create an instance of AgentFilters from a JSON string
agent_filters_instance = AgentFilters.from_json(json)
# print the JSON string representation of the object
print(AgentFilters.to_json())

# convert the object into a dict
agent_filters_dict = agent_filters_instance.to_dict()
# create an instance of AgentFilters from a dict
agent_filters_from_dict = AgentFilters.from_dict(agent_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


