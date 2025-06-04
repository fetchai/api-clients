# PageStoredEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[StoredEnvelope]**](StoredEnvelope.md) |  | 
**total** | **int** |  | 
**page** | **int** |  | 
**size** | **int** |  | 
**pages** | **int** |  | [optional] 

## Example

```python
from agentverse_client.mailbox.models.page_stored_envelope import PageStoredEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of PageStoredEnvelope from a JSON string
page_stored_envelope_instance = PageStoredEnvelope.from_json(json)
# print the JSON string representation of the object
print(PageStoredEnvelope.to_json())

# convert the object into a dict
page_stored_envelope_dict = page_stored_envelope_instance.to_dict()
# create an instance of PageStoredEnvelope from a dict
page_stored_envelope_from_dict = PageStoredEnvelope.from_dict(page_stored_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


