# SecretUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret** | **str** | Sensitive data to be stored securely. | 

## Example

```python
from agentverse_client.hosting.aio.models.secret_update import SecretUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of SecretUpdate from a JSON string
secret_update_instance = SecretUpdate.from_json(json)
# print the JSON string representation of the object
print(SecretUpdate.to_json())

# convert the object into a dict
secret_update_dict = secret_update_instance.to_dict()
# create an instance of SecretUpdate from a dict
secret_update_from_dict = SecretUpdate.from_dict(secret_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


