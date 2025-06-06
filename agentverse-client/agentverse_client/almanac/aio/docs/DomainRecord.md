# DomainRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the domain | 
**agents** | [**List[AgentRecord]**](AgentRecord.md) | List of agents associated with the domain | 

## Example

```python
from agentverse_client.almanac.aio.models.domain_record import DomainRecord

# TODO update the JSON string below
json = "{}"
# create an instance of DomainRecord from a JSON string
domain_record_instance = DomainRecord.from_json(json)
# print the JSON string representation of the object
print(DomainRecord.to_json())

# convert the object into a dict
domain_record_dict = domain_record_instance.to_dict()
# create an instance of DomainRecord from a dict
domain_record_from_dict = DomainRecord.from_dict(domain_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


