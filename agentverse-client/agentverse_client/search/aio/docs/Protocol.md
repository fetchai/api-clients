# Protocol


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | the name of the protocol | 
**version** | **str** | the version of the protocol | 
**digest** | **str** | the digest of the protocol | 

## Example

```python
from agentverse_client.search.aio.models.protocol import Protocol

# TODO update the JSON string below
json = "{}"
# create an instance of Protocol from a JSON string
protocol_instance = Protocol.from_json(json)
# print the JSON string representation of the object
print(Protocol.to_json())

# convert the object into a dict
protocol_dict = protocol_instance.to_dict()
# create an instance of Protocol from a dict
protocol_from_dict = Protocol.from_dict(protocol_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


