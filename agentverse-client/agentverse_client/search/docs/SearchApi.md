# agentverse_client.search.SearchApi

All URIs are relative to *https://agentverse.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**feedback**](SearchApi.md#feedback) | **POST** /v1/search/agents/click | Feedback
[**get_agent_interactions_count**](SearchApi.md#get_agent_interactions_count) | **GET** /v1/search/agents/interactions/{address} | Get Interaction Counts Of Agent
[**get_agent_search_terms_analytics**](SearchApi.md#get_agent_search_terms_analytics) | **POST** /v1/search/analytics/agents/terms | Get Agent Search Term Analytics
[**get_agent_searches_analytics**](SearchApi.md#get_agent_searches_analytics) | **POST** /v1/search/analytics/agents | Get Agent Search Analytics
[**get_function_interactions**](SearchApi.md#get_function_interactions) | **GET** /v1/search/functions/interactions/{function_id} | Get Recent Interactions Of Function
[**search_agent_by_geolocation**](SearchApi.md#search_agent_by_geolocation) | **POST** /v1/search/agents/geo | Search Agent By Geolocation
[**search_agent_tags**](SearchApi.md#search_agent_tags) | **GET** /v1/search/agents/tags | Search Agent Tags
[**search_agents**](SearchApi.md#search_agents) | **POST** /v1/search/agents | Search Agents
[**search_functions**](SearchApi.md#search_functions) | **POST** /v1/search/functions | Search Functions


# **feedback**
> object feedback(search_feedback_request)

Feedback

### Example


```python
import agentverse_client.search
from agentverse_client.search.models.search_feedback_request import SearchFeedbackRequest
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
    api_instance = agentverse_client.search.SearchApi(api_client)
    search_feedback_request = agentverse_client.search.SearchFeedbackRequest() # SearchFeedbackRequest | 

    try:
        # Feedback
        api_response = api_instance.feedback(search_feedback_request)
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

# **get_agent_interactions_count**
> AgentInteractionCountsResponse get_agent_interactions_count(address, contract=contract)

Get Interaction Counts Of Agent

Retrieves interaction count histories and all-time interaction counts of the agent

### Example


```python
import agentverse_client.search
from agentverse_client.search.models.agent_interaction_counts_response import AgentInteractionCountsResponse
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
    api_instance = agentverse_client.search.SearchApi(api_client)
    address = 'address_example' # str | The address of the agent
    contract = agentverse_client.search.AgentContract() # AgentContract | The Almanac contract where the agent is registered (testnet by default) (optional)

    try:
        # Get Interaction Counts Of Agent
        api_response = api_instance.get_agent_interactions_count(address, contract=contract)
        print("The response of SearchApi->get_agent_interactions_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->get_agent_interactions_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| The address of the agent | 
 **contract** | [**AgentContract**](.md)| The Almanac contract where the agent is registered (testnet by default) | [optional] 

### Return type

[**AgentInteractionCountsResponse**](AgentInteractionCountsResponse.md)

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
    api_instance = agentverse_client.search.SearchApi(api_client)
    agent_search_term_analytics_request = agentverse_client.search.AgentSearchTermAnalyticsRequest() # AgentSearchTermAnalyticsRequest | 

    try:
        # Get Agent Search Term Analytics
        api_response = api_instance.get_agent_search_terms_analytics(agent_search_term_analytics_request)
        print("The response of SearchApi->get_agent_search_terms_analytics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->get_agent_search_terms_analytics: %s\n" % e)
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
    api_instance = agentverse_client.search.SearchApi(api_client)
    agent_search_analytics_request = agentverse_client.search.AgentSearchAnalyticsRequest() # AgentSearchAnalyticsRequest | 

    try:
        # Get Agent Search Analytics
        api_response = api_instance.get_agent_searches_analytics(agent_search_analytics_request)
        print("The response of SearchApi->get_agent_searches_analytics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->get_agent_searches_analytics: %s\n" % e)
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

# **get_function_interactions**
> FunctionLast30daysInteractions get_function_interactions(function_id)

Get Recent Interactions Of Function

### Example


```python
import agentverse_client.search
from agentverse_client.search.models.function_last30days_interactions import FunctionLast30daysInteractions
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
    api_instance = agentverse_client.search.SearchApi(api_client)
    function_id = 'function_id_example' # str | Unique identifier of the function

    try:
        # Get Recent Interactions Of Function
        api_response = api_instance.get_function_interactions(function_id)
        print("The response of SearchApi->get_function_interactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->get_function_interactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_id** | **str**| Unique identifier of the function | 

### Return type

[**FunctionLast30daysInteractions**](FunctionLast30daysInteractions.md)

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

# **search_agent_by_geolocation**
> AgentSearchResponse search_agent_by_geolocation(agent_geo_search_request)

Search Agent By Geolocation

### Example


```python
import agentverse_client.search
from agentverse_client.search.models.agent_geo_search_request import AgentGeoSearchRequest
from agentverse_client.search.models.agent_search_response import AgentSearchResponse
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
    api_instance = agentverse_client.search.SearchApi(api_client)
    agent_geo_search_request = agentverse_client.search.AgentGeoSearchRequest() # AgentGeoSearchRequest | 

    try:
        # Search Agent By Geolocation
        api_response = api_instance.search_agent_by_geolocation(agent_geo_search_request)
        print("The response of SearchApi->search_agent_by_geolocation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search_agent_by_geolocation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_geo_search_request** | [**AgentGeoSearchRequest**](AgentGeoSearchRequest.md)|  | 

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

# **search_agent_tags**
> AgentTagSearchResponse search_agent_tags(prefix=prefix, limit=limit)

Search Agent Tags

### Example


```python
import agentverse_client.search
from agentverse_client.search.models.agent_tag_search_response import AgentTagSearchResponse
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
    api_instance = agentverse_client.search.SearchApi(api_client)
    prefix = 'prefix_example' # str | The prefix to use for searching tags (optional)
    limit = 5 # int | The limit of search results to return (5 by default) (optional) (default to 5)

    try:
        # Search Agent Tags
        api_response = api_instance.search_agent_tags(prefix=prefix, limit=limit)
        print("The response of SearchApi->search_agent_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search_agent_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prefix** | **str**| The prefix to use for searching tags | [optional] 
 **limit** | **int**| The limit of search results to return (5 by default) | [optional] [default to 5]

### Return type

[**AgentTagSearchResponse**](AgentTagSearchResponse.md)

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

# **search_agents**
> AgentSearchResponse search_agents(agent_search_request)

Search Agents

Search for agents.

### Example


```python
import agentverse_client.search
from agentverse_client.search.models.agent_search_request import AgentSearchRequest
from agentverse_client.search.models.agent_search_response import AgentSearchResponse
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
    api_instance = agentverse_client.search.SearchApi(api_client)
    agent_search_request = agentverse_client.search.AgentSearchRequest() # AgentSearchRequest | 

    try:
        # Search Agents
        api_response = api_instance.search_agents(agent_search_request)
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

# **search_functions**
> FunctionSearchResponse search_functions(function_search_request)

Search Functions

### Example


```python
import agentverse_client.search
from agentverse_client.search.models.function_search_request import FunctionSearchRequest
from agentverse_client.search.models.function_search_response import FunctionSearchResponse
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
    api_instance = agentverse_client.search.SearchApi(api_client)
    function_search_request = agentverse_client.search.FunctionSearchRequest() # FunctionSearchRequest | 

    try:
        # Search Functions
        api_response = api_instance.search_functions(function_search_request)
        print("The response of SearchApi->search_functions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search_functions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_search_request** | [**FunctionSearchRequest**](FunctionSearchRequest.md)|  | 

### Return type

[**FunctionSearchResponse**](FunctionSearchResponse.md)

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

