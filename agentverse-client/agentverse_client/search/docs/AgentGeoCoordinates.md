# AgentGeoCoordinates


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latitude** | **float** | the latitude of the agent | 
**longitude** | **float** | the longitude of the agent | 

## Example

```python
from agentverse_client.search.models.agent_geo_coordinates import AgentGeoCoordinates

# TODO update the JSON string below
json = "{}"
# create an instance of AgentGeoCoordinates from a JSON string
agent_geo_coordinates_instance = AgentGeoCoordinates.from_json(json)
# print the JSON string representation of the object
print(AgentGeoCoordinates.to_json())

# convert the object into a dict
agent_geo_coordinates_dict = agent_geo_coordinates_instance.to_dict()
# create an instance of AgentGeoCoordinates from a dict
agent_geo_coordinates_from_dict = AgentGeoCoordinates.from_dict(agent_geo_coordinates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


