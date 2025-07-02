# AgentSEOEvaluationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The address of the agent | 
**contract** | [**AgentContract**](AgentContract.md) | The Almanac contract where the agent is registered | [optional] 
**eval_id** | **str** | Id generated for the current SEO evaluation run | 

## Example

```python
from agentverse_client.search.models.agent_seo_evaluation_response import AgentSEOEvaluationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AgentSEOEvaluationResponse from a JSON string
agent_seo_evaluation_response_instance = AgentSEOEvaluationResponse.from_json(json)
# print the JSON string representation of the object
print(AgentSEOEvaluationResponse.to_json())

# convert the object into a dict
agent_seo_evaluation_response_dict = agent_seo_evaluation_response_instance.to_dict()
# create an instance of AgentSEOEvaluationResponse from a dict
agent_seo_evaluation_response_from_dict = AgentSEOEvaluationResponse.from_dict(agent_seo_evaluation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


