# NewAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the new agent. | 
**readme** | **str** |  | [optional] 
**avatar_url** | **str** |  | [optional] 
**short_description** | **str** |  | [optional] 
**network** | [**AgentNetwork**](AgentNetwork.md) |  | [optional] 

## Example

```python
from agentverse_client.hosting.aio.models.new_agent import NewAgent

# TODO update the JSON string below
json = "{}"
# create an instance of NewAgent from a JSON string
new_agent_instance = NewAgent.from_json(json)
# print the JSON string representation of the object
print(NewAgent.to_json())

# convert the object into a dict
new_agent_dict = new_agent_instance.to_dict()
# create an instance of NewAgent from a dict
new_agent_from_dict = NewAgent.from_dict(new_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


