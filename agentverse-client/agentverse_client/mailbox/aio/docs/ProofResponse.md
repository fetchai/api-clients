# ProofResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | Access token generated upon successful proof. | 
**expiry** | **datetime** | UTC datetime at which the access token expires. | 

## Example

```python
from agentverse_client.mailbox.aio.models.proof_response import ProofResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProofResponse from a JSON string
proof_response_instance = ProofResponse.from_json(json)
# print the JSON string representation of the object
print(ProofResponse.to_json())

# convert the object into a dict
proof_response_dict = proof_response_instance.to_dict()
# create an instance of ProofResponse from a dict
proof_response_from_dict = ProofResponse.from_dict(proof_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


