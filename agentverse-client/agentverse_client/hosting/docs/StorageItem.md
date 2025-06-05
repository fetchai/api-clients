# StorageItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key identifying the storage item. | 
**value** | **str** | The stored value corresponding to the key. | 

## Example

```python
from agentverse_client.hosting.models.storage_item import StorageItem

# TODO update the JSON string below
json = "{}"
# create an instance of StorageItem from a JSON string
storage_item_instance = StorageItem.from_json(json)
# print the JSON string representation of the object
print(StorageItem.to_json())

# convert the object into a dict
storage_item_dict = storage_item_instance.to_dict()
# create an instance of StorageItem from a dict
storage_item_from_dict = StorageItem.from_dict(storage_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


