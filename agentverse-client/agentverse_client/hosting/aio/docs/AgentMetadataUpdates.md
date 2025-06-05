# AgentMetadataUpdates


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_messaging** | **bool** |  | [optional] 
**fire_hosting** | **bool** |  | [optional] 

## Example

```python
from agentverse_client.hosting.aio.models.agent_metadata_updates import AgentMetadataUpdates

# TODO update the JSON string below
json = "{}"
# create an instance of AgentMetadataUpdates from a JSON string
agent_metadata_updates_instance = AgentMetadataUpdates.from_json(json)
# print the JSON string representation of the object
print(AgentMetadataUpdates.to_json())

# convert the object into a dict
agent_metadata_updates_dict = agent_metadata_updates_instance.to_dict()
# create an instance of AgentMetadataUpdates from a dict
agent_metadata_updates_from_dict = AgentMetadataUpdates.from_dict(agent_metadata_updates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


