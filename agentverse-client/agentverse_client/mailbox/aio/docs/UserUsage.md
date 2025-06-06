# UserUsage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bytes_transferred** | **int** | Number of bytes transferred by the user. | 
**bytes_transferred_limit** | **int** | Maximum allowed bytes transferred. | 
**num_messages** | **int** | Total number of messages sent. | 
**num_messages_limit** | **int** | Maximum number of messages allowed. | 
**bytes_stored** | **int** | Current number of bytes stored by the user. | 
**bytes_stored_limit** | **int** | Maximum allowed stored bytes. | 
**num_agents** | **int** | Number of agents owned by the user. | 
**num_agents_limit** | **int** | Maximum number of agents allowed. | 
**expiry** | **datetime** |  | [optional] 

## Example

```python
from agentverse_client.mailbox.aio.models.user_usage import UserUsage

# TODO update the JSON string below
json = "{}"
# create an instance of UserUsage from a JSON string
user_usage_instance = UserUsage.from_json(json)
# print the JSON string representation of the object
print(UserUsage.to_json())

# convert the object into a dict
user_usage_dict = user_usage_instance.to_dict()
# create an instance of UserUsage from a dict
user_usage_from_dict = UserUsage.from_dict(user_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


