# AgentTagSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prefix** | **str** |  | [optional] 
**limit** | **int** | The limit of search results to return (5 by default) | [optional] [default to 5]

## Example

```python
from search_api.models.agent_tag_search_request import AgentTagSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgentTagSearchRequest from a JSON string
agent_tag_search_request_instance = AgentTagSearchRequest.from_json(json)
# print the JSON string representation of the object
print(AgentTagSearchRequest.to_json())

# convert the object into a dict
agent_tag_search_request_dict = agent_tag_search_request_instance.to_dict()
# create an instance of AgentTagSearchRequest from a dict
agent_tag_search_request_from_dict = AgentTagSearchRequest.from_dict(agent_tag_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


