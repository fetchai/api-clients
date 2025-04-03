# DomainDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_name** | **str** | Registered domain name | 
**trnsx_height** | **int** | Blockchain height of the last update | 
**permissions** | **str** | Serialized permissions associated with the domain | 
**account_address** | **str** | Address of the domain-owning account | 
**updated_by** | **str** | Identifier of the last updater | 

## Example

```python
from agentverse_client.almanac.models.domain_details import DomainDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DomainDetails from a JSON string
domain_details_instance = DomainDetails.from_json(json)
# print the JSON string representation of the object
print(DomainDetails.to_json())

# convert the object into a dict
domain_details_dict = domain_details_instance.to_dict()
# create an instance of DomainDetails from a dict
domain_details_from_dict = DomainDetails.from_dict(domain_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


