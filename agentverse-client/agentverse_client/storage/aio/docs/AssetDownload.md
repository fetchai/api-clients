# AssetDownload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **str** | Unique identifier of the asset. | 
**contents** | **str** |  | [optional] 
**mime_type** | **str** | MIME type of the asset (e.g., &#39;application/pdf&#39;). | 
**expires_at** | **datetime** | Datetime when the asset will expire. | 
**reference** | **str** |  | [optional] 

## Example

```python
from agentverse_client.storage.aio.models.asset_download import AssetDownload

# TODO update the JSON string below
json = "{}"
# create an instance of AssetDownload from a JSON string
asset_download_instance = AssetDownload.from_json(json)
# print the JSON string representation of the object
print(AssetDownload.to_json())

# convert the object into a dict
asset_download_dict = asset_download_instance.to_dict()
# create an instance of AssetDownload from a dict
asset_download_from_dict = AssetDownload.from_dict(asset_download_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


