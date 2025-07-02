# SearchFeedbackRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The address of the agent | 
**contract** | [**AgentContract**](AgentContract.md) | The Almanac contract where the agent is registered | [optional] 
**search_id** | **str** | search id generated before (during search) | 
**page_index** | **int** | page index (should start from 0) | 

## Example

```python
from agentverse_client.search.models.search_feedback_request import SearchFeedbackRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SearchFeedbackRequest from a JSON string
search_feedback_request_instance = SearchFeedbackRequest.from_json(json)
# print the JSON string representation of the object
print(SearchFeedbackRequest.to_json())

# convert the object into a dict
search_feedback_request_dict = search_feedback_request_instance.to_dict()
# create an instance of SearchFeedbackRequest from a dict
search_feedback_request_from_dict = SearchFeedbackRequest.from_dict(search_feedback_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


