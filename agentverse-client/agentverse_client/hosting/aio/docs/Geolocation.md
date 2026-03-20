# Geolocation


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
from agentverse_client.hosting.aio.models.geolocation import Geolocation

# TODO update the JSON string below
json = "{}"
# create an instance of Geolocation from a JSON string
geolocation_instance = Geolocation.from_json(json)
# print the JSON string representation of the object
print(Geolocation.to_json())

# convert the object into a dict
geolocation_dict = geolocation_instance.to_dict()
# create an instance of Geolocation from a dict
geolocation_from_dict = Geolocation.from_dict(geolocation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


