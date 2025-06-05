# HostingQuotaTopUpEvent

Event to top up quotas for the specified Agentverse hosting user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**quotas** | [**HostingQuotas**](HostingQuotas.md) |  | 

## Example

```python
from agentverse_client.hosting.models.hosting_quota_top_up_event import HostingQuotaTopUpEvent

# TODO update the JSON string below
json = "{}"
# create an instance of HostingQuotaTopUpEvent from a JSON string
hosting_quota_top_up_event_instance = HostingQuotaTopUpEvent.from_json(json)
# print the JSON string representation of the object
print(HostingQuotaTopUpEvent.to_json())

# convert the object into a dict
hosting_quota_top_up_event_dict = hosting_quota_top_up_event_instance.to_dict()
# create an instance of HostingQuotaTopUpEvent from a dict
hosting_quota_top_up_event_from_dict = HostingQuotaTopUpEvent.from_dict(hosting_quota_top_up_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


