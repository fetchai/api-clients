# ApiKeyUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier of the API key to update. | 
**expiry** | **int** | New expiration timestamp in milliseconds since epoch. | 

## Example

```python
from agentverse_client.mailbox.models.api_key_update import ApiKeyUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKeyUpdate from a JSON string
api_key_update_instance = ApiKeyUpdate.from_json(json)
# print the JSON string representation of the object
print(ApiKeyUpdate.to_json())

# convert the object into a dict
api_key_update_dict = api_key_update_instance.to_dict()
# create an instance of ApiKeyUpdate from a dict
api_key_update_from_dict = ApiKeyUpdate.from_dict(api_key_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


