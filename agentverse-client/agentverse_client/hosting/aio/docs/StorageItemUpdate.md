# StorageItemUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The new value to update for the specified storage key. | 

## Example

```python
from agentverse_client.hosting.aio.models.storage_item_update import StorageItemUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of StorageItemUpdate from a JSON string
storage_item_update_instance = StorageItemUpdate.from_json(json)
# print the JSON string representation of the object
print(StorageItemUpdate.to_json())

# convert the object into a dict
storage_item_update_dict = storage_item_update_instance.to_dict()
# create an instance of StorageItemUpdate from a dict
storage_item_update_from_dict = StorageItemUpdate.from_dict(storage_item_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


