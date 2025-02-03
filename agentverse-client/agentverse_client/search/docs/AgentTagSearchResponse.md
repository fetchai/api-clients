# AgentTagSearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tags** | [**List[AgentTag]**](AgentTag.md) | The list of tags that are returned as part of the search | [optional] 

## Example

```python
from agentverse_client.search.models.agent_tag_search_response import AgentTagSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AgentTagSearchResponse from a JSON string
agent_tag_search_response_instance = AgentTagSearchResponse.from_json(json)
# print the JSON string representation of the object
print(AgentTagSearchResponse.to_json())

# convert the object into a dict
agent_tag_search_response_dict = agent_tag_search_response_instance.to_dict()
# create an instance of AgentTagSearchResponse from a dict
agent_tag_search_response_from_dict = AgentTagSearchResponse.from_dict(agent_tag_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


