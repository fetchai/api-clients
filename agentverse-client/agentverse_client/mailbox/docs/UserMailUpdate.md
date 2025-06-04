# UserMailUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | New email address for the user. | 

## Example

```python
from agentverse_client.mailbox.models.user_mail_update import UserMailUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of UserMailUpdate from a JSON string
user_mail_update_instance = UserMailUpdate.from_json(json)
# print the JSON string representation of the object
print(UserMailUpdate.to_json())

# convert the object into a dict
user_mail_update_dict = user_mail_update_instance.to_dict()
# create an instance of UserMailUpdate from a dict
user_mail_update_from_dict = UserMailUpdate.from_dict(user_mail_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


