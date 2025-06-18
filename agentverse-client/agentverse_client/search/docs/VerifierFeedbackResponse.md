# VerifierFeedbackResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**n_total** | **int** | How many interactions with the target agents were performed | 
**n_success** | **int** | How many interactions were considered a success | 

## Example

```python
from agentverse_client.search.models.verifier_feedback_response import VerifierFeedbackResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VerifierFeedbackResponse from a JSON string
verifier_feedback_response_instance = VerifierFeedbackResponse.from_json(json)
# print the JSON string representation of the object
print(VerifierFeedbackResponse.to_json())

# convert the object into a dict
verifier_feedback_response_dict = verifier_feedback_response_instance.to_dict()
# create an instance of VerifierFeedbackResponse from a dict
verifier_feedback_response_from_dict = VerifierFeedbackResponse.from_dict(verifier_feedback_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


