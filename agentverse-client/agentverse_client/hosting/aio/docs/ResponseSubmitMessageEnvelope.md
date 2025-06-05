# ResponseSubmitMessageEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **int** |  | 
**sender** | **str** |  | 
**target** | **str** |  | 
**session** | **str** |  | 
**schema_digest** | **str** |  | 
**protocol_digest** | **str** |  | [optional] 
**payload** | **str** |  | [optional] 
**expires** | **int** |  | [optional] 
**nonce** | **int** |  | [optional] 
**signature** | **str** |  | [optional] 

## Example

```python
from agentverse_client.hosting.aio.models.response_submit_message_envelope import ResponseSubmitMessageEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseSubmitMessageEnvelope from a JSON string
response_submit_message_envelope_instance = ResponseSubmitMessageEnvelope.from_json(json)
# print the JSON string representation of the object
print(ResponseSubmitMessageEnvelope.to_json())

# convert the object into a dict
response_submit_message_envelope_dict = response_submit_message_envelope_instance.to_dict()
# create an instance of ResponseSubmitMessageEnvelope from a dict
response_submit_message_envelope_from_dict = ResponseSubmitMessageEnvelope.from_dict(response_submit_message_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


