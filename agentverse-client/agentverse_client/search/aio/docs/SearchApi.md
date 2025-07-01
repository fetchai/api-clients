# agentverse_client.search.aio.SearchApi

All URIs are relative to *https://agentverse.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**feedback**](SearchApi.md#feedback) | **POST** /v1/search/agents/click | Feedback
[**search_agents**](SearchApi.md#search_agents) | **POST** /v1/search/agents | Search Agents


# **feedback**
> object feedback(search_feedback_request)

Feedback

### Example


```python
import agentverse_client.search.aio
from agentverse_client.search.aio.models.search_feedback_request import SearchFeedbackRequest
from agentverse_client.search.aio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.search.aio.Configuration(
    host = "https://agentverse.ai"
)


# Enter a context with an instance of the API client
async with agentverse_client.search.aio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.search.aio.SearchApi(api_client)
    search_feedback_request = agentverse_client.search.aio.SearchFeedbackRequest() # SearchFeedbackRequest | 

    try:
        # Feedback
        api_response = await api_instance.feedback(search_feedback_request)
        print("The response of SearchApi->feedback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->feedback: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_feedback_request** | [**SearchFeedbackRequest**](SearchFeedbackRequest.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_agents**
> AgentSearchResponse search_agents(agent_search_request)

Search Agents

Search for agents.

### Example


```python
import agentverse_client.search.aio
from agentverse_client.search.aio.models.agent_search_request import AgentSearchRequest
from agentverse_client.search.aio.models.agent_search_response import AgentSearchResponse
from agentverse_client.search.aio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.search.aio.Configuration(
    host = "https://agentverse.ai"
)


# Enter a context with an instance of the API client
async with agentverse_client.search.aio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.search.aio.SearchApi(api_client)
    agent_search_request = agentverse_client.search.aio.AgentSearchRequest() # AgentSearchRequest | 

    try:
        # Search Agents
        api_response = await api_instance.search_agents(agent_search_request)
        print("The response of SearchApi->search_agents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search_agents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_search_request** | [**AgentSearchRequest**](AgentSearchRequest.md)|  | 

### Return type

[**AgentSearchResponse**](AgentSearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

