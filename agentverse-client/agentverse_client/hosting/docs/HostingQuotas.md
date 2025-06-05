# HostingQuotas

Class for representing Agentverse hosting user quotas

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**computation_time** | **int** |  | 
**num_messages** | **int** |  | 
**num_message_bytes** | **int** |  | 
**num_storage_bytes** | **int** |  | 
**num_agents** | **int** |  | 

## Example

```python
from agentverse_client.hosting.models.hosting_quotas import HostingQuotas

# TODO update the JSON string below
json = "{}"
# create an instance of HostingQuotas from a JSON string
hosting_quotas_instance = HostingQuotas.from_json(json)
# print the JSON string representation of the object
print(HostingQuotas.to_json())

# convert the object into a dict
hosting_quotas_dict = hosting_quotas_instance.to_dict()
# create an instance of HostingQuotas from a dict
hosting_quotas_from_dict = HostingQuotas.from_dict(hosting_quotas_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


