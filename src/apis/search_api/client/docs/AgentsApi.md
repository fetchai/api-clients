# search_api_client.AgentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**agent_selected**](AgentsApi.md#agent_selected) | **POST** /v1/search/agents/click | Mark Agent Clicked
[**get_agent_interactions**](AgentsApi.md#get_agent_interactions) | **GET** /v1/search/agents/interactions/{address} | Get Interaction Counts Of Agent
[**search_agent**](AgentsApi.md#search_agent) | **POST** /v1/search/agents | Search Agents
[**search_agent_by_geolocation**](AgentsApi.md#search_agent_by_geolocation) | **POST** /v1/search/agents/geo | Search Agents Geo


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
    api_instance = search_api_client.AgentsApi(api_client)
    agent_clicked_request = search_api_client.AgentClickedRequest() # AgentClickedRequest | 

    try:
        # Mark Agent Clicked
        api_response = api_instance.agent_selected(agent_clicked_request)
        print("The response of AgentsApi->agent_selected:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->agent_selected: %s\n" % e)
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
    api_instance = search_api_client.AgentsApi(api_client)
    address = 'address_example' # str | 

    try:
        # Get Interaction Counts Of Agent
        api_response = api_instance.get_agent_interactions(address)
        print("The response of AgentsApi->get_agent_interactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->get_agent_interactions: %s\n" % e)
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
    api_instance = search_api_client.AgentsApi(api_client)
    agent_search_request = search_api_client.AgentSearchRequest() # AgentSearchRequest | 

    try:
        # Search Agents
        api_response = api_instance.search_agent(agent_search_request)
        print("The response of AgentsApi->search_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->search_agent: %s\n" % e)
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
    api_instance = search_api_client.AgentsApi(api_client)
    agent_geo_search_request = search_api_client.AgentGeoSearchRequest() # AgentGeoSearchRequest | 

    try:
        # Search Agents Geo
        api_response = api_instance.search_agent_by_geolocation(agent_geo_search_request)
        print("The response of AgentsApi->search_agent_by_geolocation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->search_agent_by_geolocation: %s\n" % e)
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

