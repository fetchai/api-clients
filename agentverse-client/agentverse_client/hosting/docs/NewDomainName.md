# NewDomainName


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_name** | **str** | The new domain name to register for the agent. | 

## Example

```python
from agentverse_client.hosting.models.new_domain_name import NewDomainName

# TODO update the JSON string below
json = "{}"
# create an instance of NewDomainName from a JSON string
new_domain_name_instance = NewDomainName.from_json(json)
# print the JSON string representation of the object
print(NewDomainName.to_json())

# convert the object into a dict
new_domain_name_dict = new_domain_name_instance.to_dict()
# create an instance of NewDomainName from a dict
new_domain_name_from_dict = NewDomainName.from_dict(new_domain_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


