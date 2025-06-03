# AgentBySimilarityResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agents** | [**List[Agent]**](Agent.md) | The list of agents that are similar to the given one | [optional] 

## Example

```python
from agentverse_client.search.models.agent_by_similarity_response import AgentBySimilarityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AgentBySimilarityResponse from a JSON string
agent_by_similarity_response_instance = AgentBySimilarityResponse.from_json(json)
# print the JSON string representation of the object
print(AgentBySimilarityResponse.to_json())

# convert the object into a dict
agent_by_similarity_response_dict = agent_by_similarity_response_instance.to_dict()
# create an instance of AgentBySimilarityResponse from a dict
agent_by_similarity_response_from_dict = AgentBySimilarityResponse.from_dict(agent_by_similarity_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


