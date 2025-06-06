# ProofRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Address of the agent requesting authentication. | 
**challenge** | **str** | Challenge string previously issued to this agent. | 
**challenge_response** | **str** | Response proving ownership of the address. | 

## Example

```python
from agentverse_client.mailbox.aio.models.proof_request import ProofRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProofRequest from a JSON string
proof_request_instance = ProofRequest.from_json(json)
# print the JSON string representation of the object
print(ProofRequest.to_json())

# convert the object into a dict
proof_request_dict = proof_request_instance.to_dict()
# create an instance of ProofRequest from a dict
proof_request_from_dict = ProofRequest.from_dict(proof_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


