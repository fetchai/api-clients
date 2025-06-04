# NewApiKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the API key. | 
**expiry** | **int** | Expiration timestamp in milliseconds since epoch. | 
**name** | **str** | Name for the API key. | 
**scope** | **str** | Scope or permissions granted by the API key. | [optional] [default to '']

## Example

```python
from agentverse_client.mailbox.aio.models.new_api_key import NewApiKey

# TODO update the JSON string below
json = "{}"
# create an instance of NewApiKey from a JSON string
new_api_key_instance = NewApiKey.from_json(json)
# print the JSON string representation of the object
print(NewApiKey.to_json())

# convert the object into a dict
new_api_key_dict = new_api_key_instance.to_dict()
# create an instance of NewApiKey from a dict
new_api_key_from_dict = NewApiKey.from_dict(new_api_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


