# AssetsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Asset]**](Asset.md) | List of assets retrieved. | 
**pagination** | [**Pagination**](Pagination.md) |  | 

## Example

```python
from agentverse_client.storage.aio.models.assets_list import AssetsList

# TODO update the JSON string below
json = "{}"
# create an instance of AssetsList from a JSON string
assets_list_instance = AssetsList.from_json(json)
# print the JSON string representation of the object
print(AssetsList.to_json())

# convert the object into a dict
assets_list_dict = assets_list_instance.to_dict()
# create an instance of AssetsList from a dict
assets_list_from_dict = AssetsList.from_dict(assets_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


