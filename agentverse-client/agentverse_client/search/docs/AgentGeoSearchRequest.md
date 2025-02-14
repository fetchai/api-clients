# AgentGeoSearchRequest

The agent geo search request object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**AgentFilters**](AgentFilters.md) |  | [optional] 
**sort** | [**SortType**](SortType.md) | The type of sorting that should be applied to the search results | [optional] 
**direction** | [**Direction**](Direction.md) | The direction of the sorting, ascending or descending | [optional] 
**cutoff** | [**RelevancyCutoff**](RelevancyCutoff.md) | Controls how strictly the search results should be filtered based on their relevancy | [optional] 
**search_text** | **str** |  | [optional] 
**offset** | **int** | The offset of the search results for pagination | [optional] [default to 0]
**limit** | **int** | The limit of the search results for pagination | [optional] [default to 30]
**geo_filter** | [**AgentGeoFilter**](AgentGeoFilter.md) | The geo filter that can be applied to the search | 
**search_id** | **str** | Unique identifier of the search in question (search id generated before (previous search)). | [optional] 
**source** | **str** | The source where the request is sent from. Ideally should be one of the following: &#39;&#39;, &#39;agentverse&#39;, &#39;flockx&#39;, an agent address | [optional] [default to '']

## Example

```python
from agentverse_client.search.models.agent_geo_search_request import AgentGeoSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgentGeoSearchRequest from a JSON string
agent_geo_search_request_instance = AgentGeoSearchRequest.from_json(json)
# print the JSON string representation of the object
print(AgentGeoSearchRequest.to_json())

# convert the object into a dict
agent_geo_search_request_dict = agent_geo_search_request_instance.to_dict()
# create an instance of AgentGeoSearchRequest from a dict
agent_geo_search_request_from_dict = AgentGeoSearchRequest.from_dict(agent_geo_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


