# HistoricalInteractions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_points** | **Dict[str, int]** | Dictionary mapping dates to interaction counts. | 
**total_interactions** | **int** | Total number of interactions. | 

## Example

```python
from agentverse_client.hosting.models.historical_interactions import HistoricalInteractions

# TODO update the JSON string below
json = "{}"
# create an instance of HistoricalInteractions from a JSON string
historical_interactions_instance = HistoricalInteractions.from_json(json)
# print the JSON string representation of the object
print(HistoricalInteractions.to_json())

# convert the object into a dict
historical_interactions_dict = historical_interactions_instance.to_dict()
# create an instance of HistoricalInteractions from a dict
historical_interactions_from_dict = HistoricalInteractions.from_dict(historical_interactions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


