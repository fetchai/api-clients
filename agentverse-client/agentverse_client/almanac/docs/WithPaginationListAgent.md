# WithPaginationListAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**List[Agent]**](Agent.md) |  | 
**total** | **int** |  | 
**page_size** | **int** |  | 
**tracker_last_update** | **datetime** |  | [optional] 

## Example

```python
from agentverse_client.almanac.models.with_pagination_list_agent import WithPaginationListAgent

# TODO update the JSON string below
json = "{}"
# create an instance of WithPaginationListAgent from a JSON string
with_pagination_list_agent_instance = WithPaginationListAgent.from_json(json)
# print the JSON string representation of the object
print(WithPaginationListAgent.to_json())

# convert the object into a dict
with_pagination_list_agent_dict = with_pagination_list_agent_instance.to_dict()
# create an instance of WithPaginationListAgent from a dict
with_pagination_list_agent_from_dict = WithPaginationListAgent.from_dict(with_pagination_list_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


