# AgentCodeDigest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**digest** | **str** | SHA256 digest of the agent&#39;s updated code. | 

## Example

```python
from agentverse_client.hosting.aio.models.agent_code_digest import AgentCodeDigest

# TODO update the JSON string below
json = "{}"
# create an instance of AgentCodeDigest from a JSON string
agent_code_digest_instance = AgentCodeDigest.from_json(json)
# print the JSON string representation of the object
print(AgentCodeDigest.to_json())

# convert the object into a dict
agent_code_digest_dict = agent_code_digest_instance.to_dict()
# create an instance of AgentCodeDigest from a dict
agent_code_digest_from_dict = AgentCodeDigest.from_dict(agent_code_digest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


