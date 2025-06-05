# PublicAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the agent. | 
**author_username** | **str** | Username of the agent&#39;s author. | 
**address** | **str** | Bech32 address of the agent. | 
**domain** | **str** |  | [optional] 
**prefix** | **str** |  | [optional] 
**running** | **bool** | Indicates if the agent is currently running. | 
**readme** | **str** |  | [optional] 
**short_description** | **str** |  | [optional] 
**total_interactions** | **int** | Number of total interactions the agent has had. | 
**last_updated_at** | **datetime** | Timestamp when the agent was last updated. | 
**created_at** | **datetime** | Timestamp when the agent was created. | 
**maintainer_id** | **str** |  | [optional] 
**avatar_url** | **str** |  | [optional] 

## Example

```python
from agentverse_client.hosting.aio.models.public_agent import PublicAgent

# TODO update the JSON string below
json = "{}"
# create an instance of PublicAgent from a JSON string
public_agent_instance = PublicAgent.from_json(json)
# print the JSON string representation of the object
print(PublicAgent.to_json())

# convert the object into a dict
public_agent_dict = public_agent_instance.to_dict()
# create an instance of PublicAgent from a dict
public_agent_from_dict = PublicAgent.from_dict(public_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


