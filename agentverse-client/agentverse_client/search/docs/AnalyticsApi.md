# agentverse_client.search.AnalyticsApi

All URIs are relative to *https://agentverse.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_agent_insights**](AnalyticsApi.md#get_agent_insights) | **GET** /v1/search/analytics/insights/{address} | Get Agent Insights
[**get_agent_search_terms_analytics**](AnalyticsApi.md#get_agent_search_terms_analytics) | **POST** /v1/search/analytics/agents/terms | Get Agent Search Term Analytics
[**get_agent_searches_analytics**](AnalyticsApi.md#get_agent_searches_analytics) | **POST** /v1/search/analytics/agents | Get Agent Search Analytics
[**get_analytics_summary**](AnalyticsApi.md#get_analytics_summary) | **GET** /v1/search/analytics/summary | Get Analytics Summary


# **get_agent_insights**
> AgentInsightsResponse get_agent_insights(address, contract=contract)

Get Agent Insights

Returns various insights for the agent given, related to search and interactions

### Example


```python
import agentverse_client.search
from agentverse_client.search.models.agent_insights_response import AgentInsightsResponse
from agentverse_client.search.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.search.Configuration(
    host = "https://agentverse.ai"
)


# Enter a context with an instance of the API client
with agentverse_client.search.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.search.AnalyticsApi(api_client)
    address = 'address_example' # str | The address of the agent
    contract = agentverse_client.search.AgentContract() # AgentContract | The Almanac contract where the agent is registered (testnet by default) (optional)

    try:
        # Get Agent Insights
        api_response = api_instance.get_agent_insights(address, contract=contract)
        print("The response of AnalyticsApi->get_agent_insights:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->get_agent_insights: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| The address of the agent | 
 **contract** | [**AgentContract**](.md)| The Almanac contract where the agent is registered (testnet by default) | [optional] 

### Return type

[**AgentInsightsResponse**](AgentInsightsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_search_terms_analytics**
> AgentSearchTermAnalyticsResponse get_agent_search_terms_analytics(agent_search_term_analytics_request)

Get Agent Search Term Analytics

It provides data about the search terms that led to the agent in question (agent address in the payload).

### Example


```python
import agentverse_client.search
from agentverse_client.search.models.agent_search_term_analytics_request import AgentSearchTermAnalyticsRequest
from agentverse_client.search.models.agent_search_term_analytics_response import AgentSearchTermAnalyticsResponse
from agentverse_client.search.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.search.Configuration(
    host = "https://agentverse.ai"
)


# Enter a context with an instance of the API client
with agentverse_client.search.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.search.AnalyticsApi(api_client)
    agent_search_term_analytics_request = agentverse_client.search.AgentSearchTermAnalyticsRequest() # AgentSearchTermAnalyticsRequest | 

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
import agentverse_client.search
from agentverse_client.search.models.agent_search_analytics_request import AgentSearchAnalyticsRequest
from agentverse_client.search.models.agent_search_analytics_response import AgentSearchAnalyticsResponse
from agentverse_client.search.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.search.Configuration(
    host = "https://agentverse.ai"
)


# Enter a context with an instance of the API client
with agentverse_client.search.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.search.AnalyticsApi(api_client)
    agent_search_analytics_request = agentverse_client.search.AgentSearchAnalyticsRequest() # AgentSearchAnalyticsRequest | 

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

# **get_analytics_summary**
> AnalyticsSummary get_analytics_summary()

Get Analytics Summary

### Example


```python
import agentverse_client.search
from agentverse_client.search.models.analytics_summary import AnalyticsSummary
from agentverse_client.search.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.search.Configuration(
    host = "https://agentverse.ai"
)


# Enter a context with an instance of the API client
with agentverse_client.search.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.search.AnalyticsApi(api_client)

    try:
        # Get Analytics Summary
        api_response = api_instance.get_analytics_summary()
        print("The response of AnalyticsApi->get_analytics_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->get_analytics_summary: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AnalyticsSummary**](AnalyticsSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

