# PageAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Agent]**](Agent.md) |  | 
**total** | **int** |  | 
**page** | **int** |  | 
**size** | **int** |  | 
**pages** | **int** |  | [optional] 

## Example

```python
from agentverse_client.mailbox.models.page_agent import PageAgent

# TODO update the JSON string below
json = "{}"
# create an instance of PageAgent from a JSON string
page_agent_instance = PageAgent.from_json(json)
# print the JSON string representation of the object
print(PageAgent.to_json())

# convert the object into a dict
page_agent_dict = page_agent_instance.to_dict()
# create an instance of PageAgent from a dict
page_agent_from_dict = PageAgent.from_dict(page_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


