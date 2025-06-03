# AssetContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mime_type** | **str** | MIME type of the asset content (e.g., &#39;image/png&#39;). | 
**contents** | **str** | Base64-encoded string representing the asset contents. | 

## Example

```python
from agentverse_client.storage.models.asset_content import AssetContent

# TODO update the JSON string below
json = "{}"
# create an instance of AssetContent from a JSON string
asset_content_instance = AssetContent.from_json(json)
# print the JSON string representation of the object
print(AssetContent.to_json())

# convert the object into a dict
asset_content_dict = asset_content_instance.to_dict()
# create an instance of AssetContent from a dict
asset_content_from_dict = AssetContent.from_dict(asset_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


