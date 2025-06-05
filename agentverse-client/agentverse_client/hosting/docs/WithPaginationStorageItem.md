# WithPaginationStorageItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[StorageItem]**](StorageItem.md) |  | 
**next_cursor** | **str** |  | [optional] 

## Example

```python
from agentverse_client.hosting.models.with_pagination_storage_item import WithPaginationStorageItem

# TODO update the JSON string below
json = "{}"
# create an instance of WithPaginationStorageItem from a JSON string
with_pagination_storage_item_instance = WithPaginationStorageItem.from_json(json)
# print the JSON string representation of the object
print(WithPaginationStorageItem.to_json())

# convert the object into a dict
with_pagination_storage_item_dict = with_pagination_storage_item_instance.to_dict()
# create an instance of WithPaginationStorageItem from a dict
with_pagination_storage_item_from_dict = WithPaginationStorageItem.from_dict(with_pagination_storage_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


