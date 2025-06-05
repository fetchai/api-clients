# SupportedPackage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the package. | 
**version** | **str** | Version string of the package. | 

## Example

```python
from agentverse_client.hosting.models.supported_package import SupportedPackage

# TODO update the JSON string below
json = "{}"
# create an instance of SupportedPackage from a JSON string
supported_package_instance = SupportedPackage.from_json(json)
# print the JSON string representation of the object
print(SupportedPackage.to_json())

# convert the object into a dict
supported_package_dict = supported_package_instance.to_dict()
# create an instance of SupportedPackage from a dict
supported_package_from_dict = SupportedPackage.from_dict(supported_package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


