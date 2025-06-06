# TortoiseContribPydanticCreatorRelayDbModelsDbUserLeaf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** |  | 
**registered_at** | **datetime** |  | [optional] 
**username** | **str** |  | [optional] 
**bytes_stored** | **int** |  | [optional] 
**bytes_transferred** | **int** |  | [optional] 
**developer_category** | **str** |  | [optional] 
**email** | **str** |  | [optional] 

## Example

```python
from agentverse_client.mailbox.aio.models.tortoise_contrib_pydantic_creator_relay_db_models_db_user_leaf import TortoiseContribPydanticCreatorRelayDbModelsDbUserLeaf

# TODO update the JSON string below
json = "{}"
# create an instance of TortoiseContribPydanticCreatorRelayDbModelsDbUserLeaf from a JSON string
tortoise_contrib_pydantic_creator_relay_db_models_db_user_leaf_instance = TortoiseContribPydanticCreatorRelayDbModelsDbUserLeaf.from_json(json)
# print the JSON string representation of the object
print(TortoiseContribPydanticCreatorRelayDbModelsDbUserLeaf.to_json())

# convert the object into a dict
tortoise_contrib_pydantic_creator_relay_db_models_db_user_leaf_dict = tortoise_contrib_pydantic_creator_relay_db_models_db_user_leaf_instance.to_dict()
# create an instance of TortoiseContribPydanticCreatorRelayDbModelsDbUserLeaf from a dict
tortoise_contrib_pydantic_creator_relay_db_models_db_user_leaf_from_dict = TortoiseContribPydanticCreatorRelayDbModelsDbUserLeaf.from_dict(tortoise_contrib_pydantic_creator_relay_db_models_db_user_leaf_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


