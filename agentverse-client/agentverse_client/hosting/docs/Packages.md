# Packages


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**packages** | [**List[SupportedPackage]**](SupportedPackage.md) | List of supported packages. | 
**fayer_packages** | [**List[SupportedPackage]**](SupportedPackage.md) |  | [optional] 

## Example

```python
from agentverse_client.hosting.models.packages import Packages

# TODO update the JSON string below
json = "{}"
# create an instance of Packages from a JSON string
packages_instance = Packages.from_json(json)
# print the JSON string representation of the object
print(Packages.to_json())

# convert the object into a dict
packages_dict = packages_instance.to_dict()
# create an instance of Packages from a dict
packages_from_dict = Packages.from_dict(packages_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


