# AgentEndpoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**weight** | **int** |  | 

## Example

```python
from agentverse_client.almanac.aio.models.agent_endpoint import AgentEndpoint

# TODO update the JSON string below
json = "{}"
# create an instance of AgentEndpoint from a JSON string
agent_endpoint_instance = AgentEndpoint.from_json(json)
# print the JSON string representation of the object
print(AgentEndpoint.to_json())

# convert the object into a dict
agent_endpoint_dict = agent_endpoint_instance.to_dict()
# create an instance of AgentEndpoint from a dict
agent_endpoint_from_dict = AgentEndpoint.from_dict(agent_endpoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


