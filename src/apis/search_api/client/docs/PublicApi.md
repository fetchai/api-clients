# search_api_client.PublicApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**agent_selected**](PublicApi.md#agent_selected) | **POST** /v1/search/agents/click | Mark Agent Clicked
[**get_agent_interactions**](PublicApi.md#get_agent_interactions) | **GET** /v1/search/agents/interactions/{address} | Get Interaction Counts Of Agent
[**get_agent_search_terms_analytics**](PublicApi.md#get_agent_search_terms_analytics) | **POST** /v1/search/analytics/agents/terms | Get Agent Search Term Analytics
[**get_agent_searches_analytics**](PublicApi.md#get_agent_searches_analytics) | **POST** /v1/search/analytics/agents | Get Agent Search Analytics
[**get_function_interactions**](PublicApi.md#get_function_interactions) | **GET** /v1/search/functions/interactions/{function_id} | Get Recent Interactions Of Function
[**search_agent**](PublicApi.md#search_agent) | **POST** /v1/search/agents | Search Agents
[**search_agent_by_geolocation**](PublicApi.md#search_agent_by_geolocation) | **POST** /v1/search/agents/geo | Search Agents Geo
[**search_functions**](PublicApi.md#search_functions) | **POST** /v1/search/functions | Search Functions


# **agent_selected**
> object agent_selected(agent_clicked_request)

Mark Agent Clicked

### Example


```python
import search_api_client
from search_api_client.models.agent_clicked_request import AgentClickedRequest
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
    api_instance = search_api_client.PublicApi(api_client)
    agent_clicked_request = search_api_client.AgentClickedRequest() # AgentClickedRequest | 

    try:
        # Mark Agent Clicked
        api_response = api_instance.agent_selected(agent_clicked_request)
        print("The response of PublicApi->agent_selected:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->agent_selected: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_clicked_request** | [**AgentClickedRequest**](AgentClickedRequest.md)|  | 

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

# **get_agent_interactions**
> AgentInteractionCountsResponse get_agent_interactions(address)

Get Interaction Counts Of Agent

Retrieves interaction count histories and all-time interaction counts of the agent

### Example


```python
import search_api_client
from search_api_client.models.agent_interaction_counts_response import AgentInteractionCountsResponse
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
    api_instance = search_api_client.PublicApi(api_client)
    address = 'address_example' # str | 

    try:
        # Get Interaction Counts Of Agent
        api_response = api_instance.get_agent_interactions(address)
        print("The response of PublicApi->get_agent_interactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->get_agent_interactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**|  | 

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
    api_instance = search_api_client.PublicApi(api_client)
    agent_search_term_analytics_request = search_api_client.AgentSearchTermAnalyticsRequest() # AgentSearchTermAnalyticsRequest | 

    try:
        # Get Agent Search Term Analytics
        api_response = api_instance.get_agent_search_terms_analytics(agent_search_term_analytics_request)
        print("The response of PublicApi->get_agent_search_terms_analytics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->get_agent_search_terms_analytics: %s\n" % e)
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
    api_instance = search_api_client.PublicApi(api_client)
    agent_search_analytics_request = search_api_client.AgentSearchAnalyticsRequest() # AgentSearchAnalyticsRequest | 

    try:
        # Get Agent Search Analytics
        api_response = api_instance.get_agent_searches_analytics(agent_search_analytics_request)
        print("The response of PublicApi->get_agent_searches_analytics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->get_agent_searches_analytics: %s\n" % e)
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
import search_api_client
from search_api_client.models.function_last30days_interactions import FunctionLast30daysInteractions
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
    api_instance = search_api_client.PublicApi(api_client)
    function_id = 'function_id_example' # str | 

    try:
        # Get Recent Interactions Of Function
        api_response = api_instance.get_function_interactions(function_id)
        print("The response of PublicApi->get_function_interactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->get_function_interactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_id** | **str**|  | 

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

# **search_agent**
> AgentSearchResponse search_agent(agent_search_request)

Search Agents

### Example


```python
import search_api_client
from search_api_client.models.agent_search_request import AgentSearchRequest
from search_api_client.models.agent_search_response import AgentSearchResponse
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
    api_instance = search_api_client.PublicApi(api_client)
    agent_search_request = search_api_client.AgentSearchRequest() # AgentSearchRequest | 

    try:
        # Search Agents
        api_response = api_instance.search_agent(agent_search_request)
        print("The response of PublicApi->search_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->search_agent: %s\n" % e)
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

# **search_agent_by_geolocation**
> AgentSearchResponse search_agent_by_geolocation(agent_geo_search_request)

Search Agents Geo

### Example


```python
import search_api_client
from search_api_client.models.agent_geo_search_request import AgentGeoSearchRequest
from search_api_client.models.agent_search_response import AgentSearchResponse
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
    api_instance = search_api_client.PublicApi(api_client)
    agent_geo_search_request = search_api_client.AgentGeoSearchRequest() # AgentGeoSearchRequest | 

    try:
        # Search Agents Geo
        api_response = api_instance.search_agent_by_geolocation(agent_geo_search_request)
        print("The response of PublicApi->search_agent_by_geolocation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->search_agent_by_geolocation: %s\n" % e)
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

# **search_functions**
> FunctionSearchResponse search_functions(function_search_request)

Search Functions

### Example


```python
import search_api_client
from search_api_client.models.function_search_request import FunctionSearchRequest
from search_api_client.models.function_search_response import FunctionSearchResponse
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
    api_instance = search_api_client.PublicApi(api_client)
    function_search_request = search_api_client.FunctionSearchRequest() # FunctionSearchRequest | 

    try:
        # Search Functions
        api_response = api_instance.search_functions(function_search_request)
        print("The response of PublicApi->search_functions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->search_functions: %s\n" % e)
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

