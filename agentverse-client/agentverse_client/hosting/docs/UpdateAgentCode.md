# UpdateAgentCode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The updated source code for the agent, formatted as a JSON string containing files and content. | 

## Example

```python
from agentverse_client.hosting.models.update_agent_code import UpdateAgentCode

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAgentCode from a JSON string
update_agent_code_instance = UpdateAgentCode.from_json(json)
# print the JSON string representation of the object
print(UpdateAgentCode.to_json())

# convert the object into a dict
update_agent_code_dict = update_agent_code_instance.to_dict()
# create an instance of UpdateAgentCode from a dict
update_agent_code_from_dict = UpdateAgentCode.from_dict(update_agent_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


