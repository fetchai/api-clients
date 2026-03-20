# WithPaginationAgentSummaryV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[AgentSummaryV1]**](AgentSummaryV1.md) |  | 
**next_cursor** | **str** |  | [optional] 

## Example

```python
from agentverse_client.hosting.models.with_pagination_agent_summary_v1 import WithPaginationAgentSummaryV1

# TODO update the JSON string below
json = "{}"
# create an instance of WithPaginationAgentSummaryV1 from a JSON string
with_pagination_agent_summary_v1_instance = WithPaginationAgentSummaryV1.from_json(json)
# print the JSON string representation of the object
print(WithPaginationAgentSummaryV1.to_json())

# convert the object into a dict
with_pagination_agent_summary_v1_dict = with_pagination_agent_summary_v1_instance.to_dict()
# create an instance of WithPaginationAgentSummaryV1 from a dict
with_pagination_agent_summary_v1_from_dict = WithPaginationAgentSummaryV1.from_dict(with_pagination_agent_summary_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


