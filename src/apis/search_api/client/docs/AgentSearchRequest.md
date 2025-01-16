# AgentSearchRequest

The agent search request object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**AgentFilters**](AgentFilters.md) |  | [optional] 
**sort** | [**SortType**](SortType.md) |  | [optional] 
**direction** | [**Direction**](Direction.md) |  | [optional] 
**search_text** | **str** |  | [optional] 
**offset** | **int** | The offset of the search results for pagination | [optional] [default to 0]
**limit** | **int** | The limit of the search results for pagination | [optional] [default to 30]
**search_id** | **str** | Unique identifier of the search in question (search id generated before (previous search)). | [optional] 
**source** | **str** | The source where the request is sent from. Ideally should be one of the following: &#39;&#39;, &#39;agentverse&#39;, &#39;flockx&#39;, an agent address | [optional] [default to '']
**only_current_campaign_eligible** | **bool** |  | [optional] [default to False]

## Example

```python
from search_api.models.agent_search_request import AgentSearchRequest

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


