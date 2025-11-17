# AlmanacUsage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_domains** | **int** | Number of domains registered by the user | [optional] [default to 0]
**max_domains** | **int** | Max allowed domains for the user | [optional] [default to 0]

## Example

```python
from agentverse_client.almanac.models.almanac_usage import AlmanacUsage

# TODO update the JSON string below
json = "{}"
# create an instance of AlmanacUsage from a JSON string
almanac_usage_instance = AlmanacUsage.from_json(json)
# print the JSON string representation of the object
print(AlmanacUsage.to_json())

# convert the object into a dict
almanac_usage_dict = almanac_usage_instance.to_dict()
# create an instance of AlmanacUsage from a dict
almanac_usage_from_dict = AlmanacUsage.from_dict(almanac_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


