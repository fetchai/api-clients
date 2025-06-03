# NewAsset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lifetime_hours** | **int** | Asset lifetime in hours (1–24). | 
**mime_type** | **str** |  | [optional] 
**contents** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from agentverse_client.storage.aio.models.new_asset import NewAsset

# TODO update the JSON string below
json = "{}"
# create an instance of NewAsset from a JSON string
new_asset_instance = NewAsset.from_json(json)
# print the JSON string representation of the object
print(NewAsset.to_json())

# convert the object into a dict
new_asset_dict = new_asset_instance.to_dict()
# create an instance of NewAsset from a dict
new_asset_from_dict = NewAsset.from_dict(new_asset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


