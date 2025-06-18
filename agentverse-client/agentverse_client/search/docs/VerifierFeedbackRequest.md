# VerifierFeedbackRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The address of the agent | 
**contract** | [**AgentContract**](AgentContract.md) | The Almanac contract where the agent is registered | [optional] 
**num_messages** | **int** | How many messages to send to the agent (default: 1) | [optional] [default to 1]

## Example

```python
from agentverse_client.search.models.verifier_feedback_request import VerifierFeedbackRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VerifierFeedbackRequest from a JSON string
verifier_feedback_request_instance = VerifierFeedbackRequest.from_json(json)
# print the JSON string representation of the object
print(VerifierFeedbackRequest.to_json())

# convert the object into a dict
verifier_feedback_request_dict = verifier_feedback_request_instance.to_dict()
# create an instance of VerifierFeedbackRequest from a dict
verifier_feedback_request_from_dict = VerifierFeedbackRequest.from_dict(verifier_feedback_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


