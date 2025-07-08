# AgentSearchRequest

The agent search request object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**AgentFilters**](AgentFilters.md) |  | [optional] 
**sort** | [**SortType**](SortType.md) | The type of sorting that should be applied to the search results | [optional] 
**direction** | [**Direction**](Direction.md) | The direction of the sorting, ascending or descending | [optional] 
**cutoff** | [**RelevancyCutoff**](RelevancyCutoff.md) | Controls how strictly the search results should be filtered based on their relevancy | [optional] 
**search_text** | **str** |  | [optional] 
**semantic_search** | **bool** | Whether to perform semantic-based search, where agents semantically close to the search text rank highest. If not enabled, a keywords-based search is performed instead. | [optional] [default to False]
**offset** | **int** | The offset of the search results for pagination | [optional] [default to 0]
**limit** | **int** | The limit of the search results for pagination | [optional] [default to 30]
**exclude_geo_agents** | **bool** | Whether to exclude agents that have a geo location specified | [optional] [default to True]
**search_id** | **str** | Search id of a previous search, will be generated if not passed.  This id can the be passed as the search_id prop of another search when we want to do more searches with different offsets (&#x3D; pagination)  and we want all of them to be identified by the same search_id.  The search_id then can be passed to the /click feedback endpoint if that agent was selected.  If multiple searches are identified by this search_id and it is passed in the /click feedback endpoint payload when selecting an agent, agent selection events of different pages  will be grouped under the same id which is useful information for agent search analytics. | [optional] 
**source** | **str** | The source where the request is sent from. Ideally should be one of the following:   &#39;&#39;, &#39;agentverse&#39;, &#39;flockx&#39;, an agent address but technically can also be a domain or any arbitrary string. | [optional] [default to '']

## Example

```python
from agentverse_client.search.aio.models.agent_search_request import AgentSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgentSearchRequest from a JSON string
agent_search_request_instance = AgentSearchRequest.from_json(json)
# print the JSON string representation of the object
print(AgentSearchRequest.to_json())

# convert the object into a dict
agent_search_request_dict = agent_search_request_instance.to_dict()
# create an instance of AgentSearchRequest from a dict
agent_search_request_from_dict = AgentSearchRequest.from_dict(agent_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


