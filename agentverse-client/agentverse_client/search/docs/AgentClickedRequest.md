# AgentClickedRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_id** | **str** | search id generated before (during search) | 
**page_index** | **int** | page index (should start from 0) | 
**address** | **str** | the address of the agent that was clicked on | 

## Example

```python
from agentverse_client.search.models.agent_clicked_request import AgentClickedRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgentClickedRequest from a JSON string
agent_clicked_request_instance = AgentClickedRequest.from_json(json)
# print the JSON string representation of the object
print(AgentClickedRequest.to_json())

# convert the object into a dict
agent_clicked_request_dict = agent_clicked_request_instance.to_dict()
# create an instance of AgentClickedRequest from a dict
agent_clicked_request_from_dict = AgentClickedRequest.from_dict(agent_clicked_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


