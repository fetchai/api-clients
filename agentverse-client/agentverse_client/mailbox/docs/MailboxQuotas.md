# MailboxQuotas

Class for representing Mailbox user quotas

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bytes_transferred** | **int** |  | 
**num_messages** | **int** |  | 
**bytes_stored** | **int** |  | 
**num_agents** | **int** |  | 

## Example

```python
from agentverse_client.mailbox.models.mailbox_quotas import MailboxQuotas

# TODO update the JSON string below
json = "{}"
# create an instance of MailboxQuotas from a JSON string
mailbox_quotas_instance = MailboxQuotas.from_json(json)
# print the JSON string representation of the object
print(MailboxQuotas.to_json())

# convert the object into a dict
mailbox_quotas_dict = mailbox_quotas_instance.to_dict()
# create an instance of MailboxQuotas from a dict
mailbox_quotas_from_dict = MailboxQuotas.from_dict(mailbox_quotas_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


