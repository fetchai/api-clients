# WithPaginationAgentSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[AgentSummary]**](AgentSummary.md) |  | 
**next_cursor** | **str** |  | [optional] 

## Example

```python
from agentverse_client.hosting.aio.models.with_pagination_agent_summary import WithPaginationAgentSummary

# TODO update the JSON string below
json = "{}"
# create an instance of WithPaginationAgentSummary from a JSON string
with_pagination_agent_summary_instance = WithPaginationAgentSummary.from_json(json)
# print the JSON string representation of the object
print(WithPaginationAgentSummary.to_json())

# convert the object into a dict
with_pagination_agent_summary_dict = with_pagination_agent_summary_instance.to_dict()
# create an instance of WithPaginationAgentSummary from a dict
with_pagination_agent_summary_from_dict = WithPaginationAgentSummary.from_dict(with_pagination_agent_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


