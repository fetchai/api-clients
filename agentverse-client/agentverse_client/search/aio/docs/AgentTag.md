# AgentTag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag** | **str** | The tag of the agent (e.g.: llm, geo, travel, utility, finance, ...) | 

## Example

```python
from agentverse_client.search.aio.models.agent_tag import AgentTag

# TODO update the JSON string below
json = "{}"
# create an instance of AgentTag from a JSON string
agent_tag_instance = AgentTag.from_json(json)
# print the JSON string representation of the object
print(AgentTag.to_json())

# convert the object into a dict
agent_tag_dict = agent_tag_instance.to_dict()
# create an instance of AgentTag from a dict
agent_tag_from_dict = AgentTag.from_dict(agent_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


