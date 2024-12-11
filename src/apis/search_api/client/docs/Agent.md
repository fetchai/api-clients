# Agent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | 
**name** | **str** |  | 
**readme** | **str** |  | 
**protocols** | [**List[Protocol]**](Protocol.md) |  | 
**avatar_href** | **str** |  | 
**total_interactions** | **int** |  | 
**recent_interactions** | **int** |  | 
**rating** | **float** |  | 
**status** | **str** |  | 
**type** | **str** |  | 
**category** | **str** |  | 
**featured** | **bool** |  | [optional] [default to False]
**geo_location** | [**AgentGeoLocation**](AgentGeoLocation.md) |  | 
**last_updated** | **datetime** |  | 
**created_at** | **datetime** |  | 

## Example

```python
from search_api_client.models.agent import Agent

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


