# ASI1ExecutionFeedbackRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The address of the agent | 
**contract** | [**AgentContract**](AgentContract.md) | The Almanac contract where the agent is registered | [optional] 
**success** | **bool** | denotes if agent execution by ASI1 was successful or not | 
**request** | **str** | message sent to the agent | 
**response** | **str** | response received from the agent | 
**from_verifier** | **bool** | denotes if the feedback is coming from the interaction verifier agent | [optional] [default to False]

## Example

```python
from agentverse_client.search.models.asi1_execution_feedback_request import ASI1ExecutionFeedbackRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ASI1ExecutionFeedbackRequest from a JSON string
asi1_execution_feedback_request_instance = ASI1ExecutionFeedbackRequest.from_json(json)
# print the JSON string representation of the object
print(ASI1ExecutionFeedbackRequest.to_json())

# convert the object into a dict
asi1_execution_feedback_request_dict = asi1_execution_feedback_request_instance.to_dict()
# create an instance of ASI1ExecutionFeedbackRequest from a dict
asi1_execution_feedback_request_from_dict = ASI1ExecutionFeedbackRequest.from_dict(asi1_execution_feedback_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


