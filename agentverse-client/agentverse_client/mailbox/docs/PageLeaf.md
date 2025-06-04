# PageLeaf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[TortoiseContribPydanticCreatorRelayDbModelsDbApiKeyLeaf]**](TortoiseContribPydanticCreatorRelayDbModelsDbApiKeyLeaf.md) |  | 
**total** | **int** |  | 
**page** | **int** |  | 
**size** | **int** |  | 
**pages** | **int** |  | [optional] 

## Example

```python
from agentverse_client.mailbox.models.page_leaf import PageLeaf

# TODO update the JSON string below
json = "{}"
# create an instance of PageLeaf from a JSON string
page_leaf_instance = PageLeaf.from_json(json)
# print the JSON string representation of the object
print(PageLeaf.to_json())

# convert the object into a dict
page_leaf_dict = page_leaf_instance.to_dict()
# create an instance of PageLeaf from a dict
page_leaf_from_dict = PageLeaf.from_dict(page_leaf_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


