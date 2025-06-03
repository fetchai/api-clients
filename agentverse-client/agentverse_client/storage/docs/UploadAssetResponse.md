# UploadAssetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **str** | Unique identifier of the uploaded asset. | 
**reference** | **str** | Internal reference string pointing to the stored asset. | 

## Example

```python
from agentverse_client.storage.models.upload_asset_response import UploadAssetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UploadAssetResponse from a JSON string
upload_asset_response_instance = UploadAssetResponse.from_json(json)
# print the JSON string representation of the object
print(UploadAssetResponse.to_json())

# convert the object into a dict
upload_asset_response_dict = upload_asset_response_instance.to_dict()
# create an instance of UploadAssetResponse from a dict
upload_asset_response_from_dict = UploadAssetResponse.from_dict(upload_asset_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


