# UpdateAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**readme** | **str** |  | [optional] 
**avatar_url** | **str** |  | [optional] 
**short_description** | **str** |  | [optional] 

## Example

```python
from agentverse_client.hosting.aio.models.update_agent import UpdateAgent

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAgent from a JSON string
update_agent_instance = UpdateAgent.from_json(json)
# print the JSON string representation of the object
print(UpdateAgent.to_json())

# convert the object into a dict
update_agent_dict = update_agent_instance.to_dict()
# create an instance of UpdateAgent from a dict
update_agent_from_dict = UpdateAgent.from_dict(update_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


