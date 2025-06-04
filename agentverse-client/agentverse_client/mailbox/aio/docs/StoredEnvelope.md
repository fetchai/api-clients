# StoredEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | 
**envelope** | [**Envelope**](Envelope.md) |  | 
**received_at** | **datetime** |  | 
**expires_at** | **datetime** |  | 

## Example

```python
from agentverse_client.mailbox.aio.models.stored_envelope import StoredEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of StoredEnvelope from a JSON string
stored_envelope_instance = StoredEnvelope.from_json(json)
# print the JSON string representation of the object
print(StoredEnvelope.to_json())

# convert the object into a dict
stored_envelope_dict = stored_envelope_instance.to_dict()
# create an instance of StoredEnvelope from a dict
stored_envelope_from_dict = StoredEnvelope.from_dict(stored_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


