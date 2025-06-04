# MailboxQuotaSetEvent

Event to set quotas for the specified Mailbox user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**quotas** | [**MailboxQuotas**](MailboxQuotas.md) |  | 
**expiry** | **datetime** |  | 

## Example

```python
from agentverse_client.mailbox.models.mailbox_quota_set_event import MailboxQuotaSetEvent

# TODO update the JSON string below
json = "{}"
# create an instance of MailboxQuotaSetEvent from a JSON string
mailbox_quota_set_event_instance = MailboxQuotaSetEvent.from_json(json)
# print the JSON string representation of the object
print(MailboxQuotaSetEvent.to_json())

# convert the object into a dict
mailbox_quota_set_event_dict = mailbox_quota_set_event_instance.to_dict()
# create an instance of MailboxQuotaSetEvent from a dict
mailbox_quota_set_event_from_dict = MailboxQuotaSetEvent.from_dict(mailbox_quota_set_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


