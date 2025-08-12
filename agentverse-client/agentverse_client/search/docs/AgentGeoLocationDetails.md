# AgentGeoLocationDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**latitude** | **float** |  | [optional] 
**longitude** | **float** |  | [optional] 
**street** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 

## Example

```python
from agentverse_client.search.models.agent_geo_location_details import AgentGeoLocationDetails

# TODO update the JSON string below
json = "{}"
# create an instance of AgentGeoLocationDetails from a JSON string
agent_geo_location_details_instance = AgentGeoLocationDetails.from_json(json)
# print the JSON string representation of the object
print(AgentGeoLocationDetails.to_json())

# convert the object into a dict
agent_geo_location_details_dict = agent_geo_location_details_instance.to_dict()
# create an instance of AgentGeoLocationDetails from a dict
agent_geo_location_details_from_dict = AgentGeoLocationDetails.from_dict(agent_geo_location_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


