# AgentClickedRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_id** | **str** |  | 
**page_index** | **int** |  | 
**address** | **str** |  | 

## Example

```python
from search_api_client.models.agent_clicked_request import AgentClickedRequest

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


