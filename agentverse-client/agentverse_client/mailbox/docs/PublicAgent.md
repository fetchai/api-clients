# PublicAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Bech32 address of the public agent. | 
**prefix** | **str** | Environment prefix, typically &#39;test-agent&#39;. | [optional] [default to 'test-agent']
**name** | **str** | Name of the public agent. | 
**readme** | **str** |  | [optional] 
**avatar_url** | **str** |  | [optional] 
**short_description** | **str** |  | [optional] 

## Example

```python
from agentverse_client.mailbox.models.public_agent import PublicAgent

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


