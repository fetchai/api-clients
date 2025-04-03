# Interaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**InteractionType**](InteractionType.md) |  | 
**request** | **str** |  | 
**responses** | **List[str]** |  | 

## Example

```python
from agentverse_client.almanac.models.interaction import Interaction

# TODO update the JSON string below
json = "{}"
# create an instance of Interaction from a JSON string
interaction_instance = Interaction.from_json(json)
# print the JSON string representation of the object
print(Interaction.to_json())

# convert the object into a dict
interaction_dict = interaction_instance.to_dict()
# create an instance of Interaction from a dict
interaction_from_dict = Interaction.from_dict(interaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


