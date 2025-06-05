# Envelope

Represents an envelope for message communication between agents.  Attributes:  version (int): The envelope version.  sender (str): The sender's address.  target (str): The target's address.  session (UUID4): The session UUID that persists for back-and-forth  dialogues between agents.  schema_digest (str): The schema digest for the enclosed message.  protocol_digest (str | None): The digest of the protocol associated with the message  (optional).  payload (str | None): The encoded message payload of the envelope (optional).  expires (int | None): The expiration timestamp (optional).  nonce (int | None): The nonce value (optional).  signature (str | None): The envelope signature (optional).

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
from agentverse_client.hosting.models.envelope import Envelope

# TODO update the JSON string below
json = "{}"
# create an instance of Envelope from a JSON string
envelope_instance = Envelope.from_json(json)
# print the JSON string representation of the object
print(Envelope.to_json())

# convert the object into a dict
envelope_dict = envelope_instance.to_dict()
# create an instance of Envelope from a dict
envelope_from_dict = Envelope.from_dict(envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


