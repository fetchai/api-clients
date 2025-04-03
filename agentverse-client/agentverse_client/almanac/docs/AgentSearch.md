# AgentSearch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | Free-text search query | 
**protocols** | **List[str]** |  | [optional] 
**types** | [**List[AgentType]**](AgentType.md) |  | [optional] 
**status** | [**List[AgentStatusFilter]**](AgentStatusFilter.md) |  | [optional] 
**dev_categories** | [**List[DeveloperCategory]**](DeveloperCategory.md) |  | [optional] 
**limit** | **int** |  | [optional] 
**network** | [**AgentNetwork**](AgentNetwork.md) |  | [optional] 
**sort** | [**SortAgents**](SortAgents.md) |  | [optional] 

## Example

```python
from agentverse_client.almanac.models.agent_search import AgentSearch

# TODO update the JSON string below
json = "{}"
# create an instance of AgentSearch from a JSON string
agent_search_instance = AgentSearch.from_json(json)
# print the JSON string representation of the object
print(AgentSearch.to_json())

# convert the object into a dict
agent_search_dict = agent_search_instance.to_dict()
# create an instance of AgentSearch from a dict
agent_search_from_dict = AgentSearch.from_dict(agent_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


