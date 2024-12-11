# search_api_client.AnalyticsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_agent_search_terms_analytics**](AnalyticsApi.md#get_agent_search_terms_analytics) | **POST** /v1/search/analytics/agents/terms | Get Agent Search Term Analytics
[**get_agent_searches_analytics**](AnalyticsApi.md#get_agent_searches_analytics) | **POST** /v1/search/analytics/agents | Get Agent Search Analytics


# **get_agent_search_terms_analytics**
> AgentSearchTermAnalyticsResponse get_agent_search_terms_analytics(agent_search_term_analytics_request)

Get Agent Search Term Analytics

It provides data about the search terms that led to the agent in question (agent address in the payload).

### Example


```python
import search_api_client
from search_api_client.models.agent_search_term_analytics_request import AgentSearchTermAnalyticsRequest
from search_api_client.models.agent_search_term_analytics_response import AgentSearchTermAnalyticsResponse
from search_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = search_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with search_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = search_api_client.AnalyticsApi(api_client)
    agent_search_term_analytics_request = search_api_client.AgentSearchTermAnalyticsRequest() # AgentSearchTermAnalyticsRequest | 

    try:
        # Get Agent Search Term Analytics
        api_response = api_instance.get_agent_search_terms_analytics(agent_search_term_analytics_request)
        print("The response of AnalyticsApi->get_agent_search_terms_analytics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->get_agent_search_terms_analytics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_search_term_analytics_request** | [**AgentSearchTermAnalyticsRequest**](AgentSearchTermAnalyticsRequest.md)|  | 

### Return type

[**AgentSearchTermAnalyticsResponse**](AgentSearchTermAnalyticsResponse.md)

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

# **get_agent_searches_analytics**
> AgentSearchAnalyticsResponse get_agent_searches_analytics(agent_search_analytics_request)

Get Agent Search Analytics

### Example


```python
import search_api_client
from search_api_client.models.agent_search_analytics_request import AgentSearchAnalyticsRequest
from search_api_client.models.agent_search_analytics_response import AgentSearchAnalyticsResponse
from search_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = search_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with search_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = search_api_client.AnalyticsApi(api_client)
    agent_search_analytics_request = search_api_client.AgentSearchAnalyticsRequest() # AgentSearchAnalyticsRequest | 

    try:
        # Get Agent Search Analytics
        api_response = api_instance.get_agent_searches_analytics(agent_search_analytics_request)
        print("The response of AnalyticsApi->get_agent_searches_analytics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->get_agent_searches_analytics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_search_analytics_request** | [**AgentSearchAnalyticsRequest**](AgentSearchAnalyticsRequest.md)|  | 

### Return type

[**AgentSearchAnalyticsResponse**](AgentSearchAnalyticsResponse.md)

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

