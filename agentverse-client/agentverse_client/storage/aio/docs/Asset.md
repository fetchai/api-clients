# Asset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **str** | Unique identifier of the asset. | 
**mime_type** | **str** |  | [optional] 
**size** | **int** | Size of the asset in bytes. | 
**checksum** | **str** | SHA-256 checksum of the asset content. | 
**expires_at** | **datetime** | Datetime when the asset will expire. | 
**created_at** | **datetime** | Datetime when the asset was created. | 
**updated_at** | **datetime** | Datetime when the asset was last updated. | 
**reference** | **str** |  | [optional] 
**protocol** | **str** |  | [optional] 

## Example

```python
from agentverse_client.storage.aio.models.asset import Asset

# TODO update the JSON string below
json = "{}"
# create an instance of Asset from a JSON string
asset_instance = Asset.from_json(json)
# print the JSON string representation of the object
print(Asset.to_json())

# convert the object into a dict
asset_dict = asset_instance.to_dict()
# create an instance of Asset from a dict
asset_from_dict = Asset.from_dict(asset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


