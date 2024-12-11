# AgentGeoFilter

The geo filter that can be applied to the agent search

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latitude** | **float** |  | 
**longitude** | **float** |  | 
**radius** | **float** |  | 

## Example

```python
from search_api_client.models.agent_geo_filter import AgentGeoFilter

# TODO update the JSON string below
json = "{}"
# create an instance of AgentGeoFilter from a JSON string
agent_geo_filter_instance = AgentGeoFilter.from_json(json)
# print the JSON string representation of the object
print(AgentGeoFilter.to_json())

# convert the object into a dict
agent_geo_filter_dict = agent_geo_filter_instance.to_dict()
# create an instance of AgentGeoFilter from a dict
agent_geo_filter_from_dict = AgentGeoFilter.from_dict(agent_geo_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


