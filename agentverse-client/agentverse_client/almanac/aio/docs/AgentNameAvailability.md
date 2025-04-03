# AgentNameAvailability


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name_prefix** | **str** | Agent name prefix | 
**domain** | **str** | Domain associated with the name | 
**status** | [**AgentNameAvailabilityStatus**](AgentNameAvailabilityStatus.md) |  | 

## Example

```python
from agentverse_client.almanac.aio.models.agent_name_availability import AgentNameAvailability

# TODO update the JSON string below
json = "{}"
# create an instance of AgentNameAvailability from a JSON string
agent_name_availability_instance = AgentNameAvailability.from_json(json)
# print the JSON string representation of the object
print(AgentNameAvailability.to_json())

# convert the object into a dict
agent_name_availability_dict = agent_name_availability_instance.to_dict()
# create an instance of AgentNameAvailability from a dict
agent_name_availability_from_dict = AgentNameAvailability.from_dict(agent_name_availability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


