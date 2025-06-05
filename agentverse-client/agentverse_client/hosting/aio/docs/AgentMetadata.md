# AgentMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_messaging** | **bool** | Enable wallet messaging for the agent. | 
**fire_hosting** | **bool** |  | [optional] 

## Example

```python
from agentverse_client.hosting.aio.models.agent_metadata import AgentMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of AgentMetadata from a JSON string
agent_metadata_instance = AgentMetadata.from_json(json)
# print the JSON string representation of the object
print(AgentMetadata.to_json())

# convert the object into a dict
agent_metadata_dict = agent_metadata_instance.to_dict()
# create an instance of AgentMetadata from a dict
agent_metadata_from_dict = AgentMetadata.from_dict(agent_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


