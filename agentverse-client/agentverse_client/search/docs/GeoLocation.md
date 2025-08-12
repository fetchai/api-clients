# GeoLocation

the geolocation of the agent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latitude** | **float** |  | 
**longitude** | **float** |  | 
**radius** | **float** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**street** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 

## Example

```python
from agentverse_client.search.models.geo_location import GeoLocation

# TODO update the JSON string below
json = "{}"
# create an instance of GeoLocation from a JSON string
geo_location_instance = GeoLocation.from_json(json)
# print the JSON string representation of the object
print(GeoLocation.to_json())

# convert the object into a dict
geo_location_dict = geo_location_instance.to_dict()
# create an instance of GeoLocation from a dict
geo_location_from_dict = GeoLocation.from_dict(geo_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


