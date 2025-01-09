# SearchTermPercentage

Percentage of searches when the agent was retrieved using this search term

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**term** | **str** |  | 
**last_24h_percentage** | **float** |  | 
**last_7d_percentage** | **float** |  | 
**last_30d_percentage** | **float** |  | 

## Example

```python
from search_api_client.models.search_term_percentage import SearchTermPercentage

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


