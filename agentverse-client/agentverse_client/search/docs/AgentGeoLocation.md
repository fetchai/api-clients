# AgentGeoLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latitude** | **float** | the latitude of the agent | 
**longitude** | **float** | the longitude of the agent | 
**radius** | **float** |  | [optional] 

## Example

```python
from agentverse_client.search.models.agent_geo_location import AgentGeoLocation

# TODO update the JSON string below
json = "{}"
# create an instance of AgentGeoLocation from a JSON string
agent_geo_location_instance = AgentGeoLocation.from_json(json)
# print the JSON string representation of the object
print(AgentGeoLocation.to_json())

# convert the object into a dict
agent_geo_location_dict = agent_geo_location_instance.to_dict()
# create an instance of AgentGeoLocation from a dict
agent_geo_location_from_dict = AgentGeoLocation.from_dict(agent_geo_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


