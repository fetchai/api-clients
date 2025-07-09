# MultiSEOEvaluationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_days** | **int** | For finding search queries to use, consider searches from up to &#x60;max_days&#x60; days ago (default: 10) | [optional] [default to 10]
**max_searches** | **int** | How many top searches to use at most, which determines how many messages we&#39;ll send at most (default: 100) | [optional] [default to 100]

## Example

```python
from agentverse_client.search.models.multi_seo_evaluation_request import MultiSEOEvaluationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MultiSEOEvaluationRequest from a JSON string
multi_seo_evaluation_request_instance = MultiSEOEvaluationRequest.from_json(json)
# print the JSON string representation of the object
print(MultiSEOEvaluationRequest.to_json())

# convert the object into a dict
multi_seo_evaluation_request_dict = multi_seo_evaluation_request_instance.to_dict()
# create an instance of MultiSEOEvaluationRequest from a dict
multi_seo_evaluation_request_from_dict = MultiSEOEvaluationRequest.from_dict(multi_seo_evaluation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


