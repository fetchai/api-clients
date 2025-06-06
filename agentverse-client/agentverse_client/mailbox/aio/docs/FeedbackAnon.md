# FeedbackAnon


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | Source identifier | 
**feedback** | **str** | Anonymous user feedback or comment. | 

## Example

```python
from agentverse_client.mailbox.aio.models.feedback_anon import FeedbackAnon

# TODO update the JSON string below
json = "{}"
# create an instance of FeedbackAnon from a JSON string
feedback_anon_instance = FeedbackAnon.from_json(json)
# print the JSON string representation of the object
print(FeedbackAnon.to_json())

# convert the object into a dict
feedback_anon_dict = feedback_anon_instance.to_dict()
# create an instance of FeedbackAnon from a dict
feedback_anon_from_dict = FeedbackAnon.from_dict(feedback_anon_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


