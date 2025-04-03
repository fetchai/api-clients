# ServiceRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_address** | **str** |  | 
**protocols** | **List[str]** |  | 
**endpoints** | [**List[EndpointInput]**](EndpointInput.md) |  | 
**expiry** | **datetime** |  | 

## Example

```python
from agentverse_client.almanac.models.service_record import ServiceRecord

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceRecord from a JSON string
service_record_instance = ServiceRecord.from_json(json)
# print the JSON string representation of the object
print(ServiceRecord.to_json())

# convert the object into a dict
service_record_dict = service_record_instance.to_dict()
# create an instance of ServiceRecord from a dict
service_record_from_dict = ServiceRecord.from_dict(service_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


