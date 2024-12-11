# AgentGeoSearchRequest

The agent geo search request object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**AgentFilters**](AgentFilters.md) |  | [optional] 
**sort** | **str** |  | [optional] [default to 'relevancy']
**direction** | **str** |  | [optional] [default to 'asc']
**search_text** | **str** |  | [optional] 
**offset** | **int** |  | [optional] [default to 0]
**limit** | **int** |  | [optional] [default to 30]
**geo_filter** | [**AgentGeoFilter**](AgentGeoFilter.md) |  | 
**search_id** | **str** |  | [optional] 
**source** | **str** |  | [optional] [default to '']

## Example

```python
from search_api_client.models.agent_geo_search_request import AgentGeoSearchRequest

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


