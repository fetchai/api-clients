# AgentSearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agents** | [**List[Agent]**](Agent.md) | The list of agents that are returned as part of the search | [optional] 
**offset** | **int** | The offset of the search results | 
**limit** | **int** | The limit of the search results | 
**num_hits** | **int** | The number of hits might be smaller than the total number of hits (&#x60;total&#x60;) when using offset and limit | 
**total** | **int** | The total number of hits might be bigger than the actual number of hits (&#x60;num_hits&#x60;)&#x60; when using offset and limit | 
**search_id** | **str** | Id passed to the search in the request payload / generated for the search (if not passed in the payload).  This id can the be passed as the search_id prop of another search when we want to do more searches with different offsets (&#x3D; pagination)  and we want all of them to be identified by the same search_id.  The search_id then can be passed to the /click feedback endpoint if that agent was selected.  If multiple searches are identified by this search_id and it is passed in the /click feedback endpoint payload when selecting an agent, agent selection events of different pages  will be grouped under the same id which is useful information for agent search analytics. | 

## Example

```python
from agentverse_client.search.aio.models.agent_search_response import AgentSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AgentSearchResponse from a JSON string
agent_search_response_instance = AgentSearchResponse.from_json(json)
# print the JSON string representation of the object
print(AgentSearchResponse.to_json())

# convert the object into a dict
agent_search_response_dict = agent_search_response_instance.to_dict()
# create an instance of AgentSearchResponse from a dict
agent_search_response_from_dict = AgentSearchResponse.from_dict(agent_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


