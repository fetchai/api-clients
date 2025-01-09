# AgentFilters

The set of filters that should be applied to the agent search entries

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **List[str]** |  | [optional] 
**category** | **List[str]** |  | [optional] 
**agent_type** | **List[str]** |  | [optional] 
**protocol_digest** | **List[str]** |  | [optional] 

## Example

```python
from search_api_client.models.agent_filters import AgentFilters

# TODO update the JSON string below
json = "{}"
# create an instance of AgentFilters from a JSON string
agent_filters_instance = AgentFilters.from_json(json)
# print the JSON string representation of the object
print(AgentFilters.to_json())

# convert the object into a dict
agent_filters_dict = agent_filters_instance.to_dict()
# create an instance of AgentFilters from a dict
agent_filters_from_dict = AgentFilters.from_dict(agent_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


