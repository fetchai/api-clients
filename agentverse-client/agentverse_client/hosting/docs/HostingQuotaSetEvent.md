# HostingQuotaSetEvent

Event to set quotas for the specified Agentverse hosting user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**quotas** | [**HostingQuotas**](HostingQuotas.md) |  | 
**expiry** | **datetime** |  | 

## Example

```python
from agentverse_client.hosting.models.hosting_quota_set_event import HostingQuotaSetEvent

# TODO update the JSON string below
json = "{}"
# create an instance of HostingQuotaSetEvent from a JSON string
hosting_quota_set_event_instance = HostingQuotaSetEvent.from_json(json)
# print the JSON string representation of the object
print(HostingQuotaSetEvent.to_json())

# convert the object into a dict
hosting_quota_set_event_dict = hosting_quota_set_event_instance.to_dict()
# create an instance of HostingQuotaSetEvent from a dict
hosting_quota_set_event_from_dict = HostingQuotaSetEvent.from_dict(hosting_quota_set_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


