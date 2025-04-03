# AgentRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Blockchain address of the agent | 
**weight** | **float** | Weight assigned to the agent within the domain | 

## Example

```python
from agentverse_client.almanac.models.agent_record import AgentRecord

# TODO update the JSON string below
json = "{}"
# create an instance of AgentRecord from a JSON string
agent_record_instance = AgentRecord.from_json(json)
# print the JSON string representation of the object
print(AgentRecord.to_json())

# convert the object into a dict
agent_record_dict = agent_record_instance.to_dict()
# create an instance of AgentRecord from a dict
agent_record_from_dict = AgentRecord.from_dict(agent_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


