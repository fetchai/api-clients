# DuplicateHostedAgentOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_secrets** | **bool** | Whether to copy secrets from the source agent to the duplicate. | [optional] [default to False]
**include_storage** | **bool** | Whether to copy storage from the source agent to the duplicate. | [optional] [default to False]

## Example

```python
from agentverse_client.hosting.models.duplicate_hosted_agent_options import DuplicateHostedAgentOptions

# TODO update the JSON string below
json = "{}"
# create an instance of DuplicateHostedAgentOptions from a JSON string
duplicate_hosted_agent_options_instance = DuplicateHostedAgentOptions.from_json(json)
# print the JSON string representation of the object
print(DuplicateHostedAgentOptions.to_json())

# convert the object into a dict
duplicate_hosted_agent_options_dict = duplicate_hosted_agent_options_instance.to_dict()
# create an instance of DuplicateHostedAgentOptions from a dict
duplicate_hosted_agent_options_from_dict = DuplicateHostedAgentOptions.from_dict(duplicate_hosted_agent_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


