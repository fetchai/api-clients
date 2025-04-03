# AgentRegistrationAttestationBatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attestations** | [**List[AgentRegistrationAttestation]**](AgentRegistrationAttestation.md) | Batch of agent registration attestations | 

## Example

```python
from agentverse_client.almanac.models.agent_registration_attestation_batch import AgentRegistrationAttestationBatch

# TODO update the JSON string below
json = "{}"
# create an instance of AgentRegistrationAttestationBatch from a JSON string
agent_registration_attestation_batch_instance = AgentRegistrationAttestationBatch.from_json(json)
# print the JSON string representation of the object
print(AgentRegistrationAttestationBatch.to_json())

# convert the object into a dict
agent_registration_attestation_batch_dict = agent_registration_attestation_batch_instance.to_dict()
# create an instance of AgentRegistrationAttestationBatch from a dict
agent_registration_attestation_batch_from_dict = AgentRegistrationAttestationBatch.from_dict(agent_registration_attestation_batch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


