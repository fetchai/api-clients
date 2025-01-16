# Agent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | the address of the agent (this should be used as the id of the agent) | 
**prefix** | **str** |  | 
**name** | **str** | the public name of the agent | 
**readme** | **str** | the contents of the readme file | 
**protocols** | [**List[Protocol]**](Protocol.md) | the list of protocols supported by the agent | 
**avatar_href** | **str** |  | [optional] 
**total_interactions** | **int** | the total interactions for this agent | 
**recent_interactions** | **int** | the number of interactions in the last 90 days | 
**rating** | **float** |  | [optional] 
**status** | [**StatusType**](StatusType.md) |  | 
**type** | [**AgentType**](AgentType.md) |  | 
**category** | [**AgentCategory**](AgentCategory.md) |  | 
**featured** | **bool** | signaled if the agent is featured or not | [optional] [default to False]
**geo_location** | [**AgentGeoLocation**](AgentGeoLocation.md) |  | [optional] 
**domain** | **str** |  | [optional] 
**last_updated** | **datetime** | the time at which the agent was last updated at | 
**created_at** | **datetime** | the time at which the agent was first visible or created | 

## Example

```python
from search_api.models.agent import Agent

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


