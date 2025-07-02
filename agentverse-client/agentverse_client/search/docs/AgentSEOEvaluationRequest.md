# AgentSEOEvaluationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The address of the agent | 
**contract** | [**AgentContract**](AgentContract.md) | The Almanac contract where the agent is registered | [optional] 
**num_messages** | **int** | How many messages to send to the agent (default: 1) | [optional] [default to 1]

## Example

```python
from agentverse_client.search.models.agent_seo_evaluation_request import AgentSEOEvaluationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgentSEOEvaluationRequest from a JSON string
agent_seo_evaluation_request_instance = AgentSEOEvaluationRequest.from_json(json)
# print the JSON string representation of the object
print(AgentSEOEvaluationRequest.to_json())

# convert the object into a dict
agent_seo_evaluation_request_dict = agent_seo_evaluation_request_instance.to_dict()
# create an instance of AgentSEOEvaluationRequest from a dict
agent_seo_evaluation_request_from_dict = AgentSEOEvaluationRequest.from_dict(agent_seo_evaluation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


