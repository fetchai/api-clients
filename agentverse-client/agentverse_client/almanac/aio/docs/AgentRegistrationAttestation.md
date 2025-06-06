# AgentRegistrationAttestation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_identifier** | **str** |  | 
**signature** | **str** |  | [optional] 
**timestamp** | **int** |  | [optional] 
**protocols** | **List[str]** | List of supported protocol identifiers | 
**endpoints** | [**List[AgentEndpoint]**](AgentEndpoint.md) | Declared service endpoints | 
**metadata** | [**Dict[str, AgentRegistrationAttestationMetadataValue]**](AgentRegistrationAttestationMetadataValue.md) |  | [optional] 

## Example

```python
from agentverse_client.almanac.aio.models.agent_registration_attestation import AgentRegistrationAttestation

# TODO update the JSON string below
json = "{}"
# create an instance of AgentRegistrationAttestation from a JSON string
agent_registration_attestation_instance = AgentRegistrationAttestation.from_json(json)
# print the JSON string representation of the object
print(AgentRegistrationAttestation.to_json())

# convert the object into a dict
agent_registration_attestation_dict = agent_registration_attestation_instance.to_dict()
# create an instance of AgentRegistrationAttestation from a dict
agent_registration_attestation_from_dict = AgentRegistrationAttestation.from_dict(agent_registration_attestation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


