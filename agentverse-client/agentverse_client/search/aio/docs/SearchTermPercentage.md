# SearchTermPercentage

Percentage of searches when the agent was retrieved using this search term

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**term** | **str** | Search term that was used when the agent was retrieved | 
**last_24h_percentage** | **float** | Percentage of searches in last 24h when the agent was retrieved using this search term | 
**last_7d_percentage** | **float** | Percentage of searches in last 7 days when the agent was retrieved using this search term | 
**last_30d_percentage** | **float** | Percentage of searches in last 30 days when the agent was retrieved using this search term | 

## Example

```python
from agentverse_client.search.aio.models.search_term_percentage import SearchTermPercentage

# TODO update the JSON string below
json = "{}"
# create an instance of SearchTermPercentage from a JSON string
search_term_percentage_instance = SearchTermPercentage.from_json(json)
# print the JSON string representation of the object
print(SearchTermPercentage.to_json())

# convert the object into a dict
search_term_percentage_dict = search_term_percentage_instance.to_dict()
# create an instance of SearchTermPercentage from a dict
search_term_percentage_from_dict = SearchTermPercentage.from_dict(search_term_percentage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


