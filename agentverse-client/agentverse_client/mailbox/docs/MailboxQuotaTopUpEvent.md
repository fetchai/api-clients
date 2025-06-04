# MailboxQuotaTopUpEvent

Event to top up quotas for the specified Mailbox user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**quotas** | [**MailboxQuotas**](MailboxQuotas.md) |  | 

## Example

```python
from agentverse_client.mailbox.models.mailbox_quota_top_up_event import MailboxQuotaTopUpEvent

# TODO update the JSON string below
json = "{}"
# create an instance of MailboxQuotaTopUpEvent from a JSON string
mailbox_quota_top_up_event_instance = MailboxQuotaTopUpEvent.from_json(json)
# print the JSON string representation of the object
print(MailboxQuotaTopUpEvent.to_json())

# convert the object into a dict
mailbox_quota_top_up_event_dict = mailbox_quota_top_up_event_instance.to_dict()
# create an instance of MailboxQuotaTopUpEvent from a dict
mailbox_quota_top_up_event_from_dict = MailboxQuotaTopUpEvent.from_dict(mailbox_quota_top_up_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


