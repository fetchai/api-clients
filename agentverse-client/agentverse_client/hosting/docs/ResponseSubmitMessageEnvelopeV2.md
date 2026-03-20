# ResponseSubmitMessageEnvelopeV2


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
from agentverse_client.hosting.models.response_submit_message_envelope_v2 import ResponseSubmitMessageEnvelopeV2

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseSubmitMessageEnvelopeV2 from a JSON string
response_submit_message_envelope_v2_instance = ResponseSubmitMessageEnvelopeV2.from_json(json)
# print the JSON string representation of the object
print(ResponseSubmitMessageEnvelopeV2.to_json())

# convert the object into a dict
response_submit_message_envelope_v2_dict = response_submit_message_envelope_v2_instance.to_dict()
# create an instance of ResponseSubmitMessageEnvelopeV2 from a dict
response_submit_message_envelope_v2_from_dict = ResponseSubmitMessageEnvelopeV2.from_dict(response_submit_message_envelope_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


