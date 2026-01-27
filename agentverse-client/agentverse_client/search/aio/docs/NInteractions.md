# NInteractions

If specified, it will filter for agents that have a number of message_recent_interactions greater than the given threshold

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from agentverse_client.search.aio.models.n_interactions import NInteractions

# TODO update the JSON string below
json = "{}"
# create an instance of NInteractions from a JSON string
n_interactions_instance = NInteractions.from_json(json)
# print the JSON string representation of the object
print(NInteractions.to_json())

# convert the object into a dict
n_interactions_dict = n_interactions_instance.to_dict()
# create an instance of NInteractions from a dict
n_interactions_from_dict = NInteractions.from_dict(n_interactions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


