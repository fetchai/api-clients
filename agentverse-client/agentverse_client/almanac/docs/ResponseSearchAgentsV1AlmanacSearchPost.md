# ResponseSearchAgentsV1AlmanacSearchPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**List[Agent]**](Agent.md) |  | 
**total** | **int** |  | 
**page_size** | **int** |  | 
**tracker_last_update** | **datetime** |  | [optional] 

## Example

```python
from agentverse_client.almanac.models.response_search_agents_v1_almanac_search_post import ResponseSearchAgentsV1AlmanacSearchPost

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseSearchAgentsV1AlmanacSearchPost from a JSON string
response_search_agents_v1_almanac_search_post_instance = ResponseSearchAgentsV1AlmanacSearchPost.from_json(json)
# print the JSON string representation of the object
print(ResponseSearchAgentsV1AlmanacSearchPost.to_json())

# convert the object into a dict
response_search_agents_v1_almanac_search_post_dict = response_search_agents_v1_almanac_search_post_instance.to_dict()
# create an instance of ResponseSearchAgentsV1AlmanacSearchPost from a dict
response_search_agents_v1_almanac_search_post_from_dict = ResponseSearchAgentsV1AlmanacSearchPost.from_dict(response_search_agents_v1_almanac_search_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


