# search_api.AgentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_current_campaign_eligibility**](AgentsApi.md#check_current_campaign_eligibility) | **GET** /v1/search/agents/current-campaign-eligibility/{address} | Check Current Campaign Eligibility
[**get_agent_interactions_count**](AgentsApi.md#get_agent_interactions_count) | **GET** /v1/search/agents/interactions/{address} | Get Interaction Counts Of Agent
[**search_agent_by_geolocation**](AgentsApi.md#search_agent_by_geolocation) | **POST** /v1/search/agents/geo | Search Agent By Geolocation
[**search_agent_tags**](AgentsApi.md#search_agent_tags) | **GET** /v1/search/agents/tags | Search Agent Tags
[**search_agents**](AgentsApi.md#search_agents) | **POST** /v1/search/agents | Search Agents
[**select_agent**](AgentsApi.md#select_agent) | **POST** /v1/search/agents/click | Select Agent


# **check_current_campaign_eligibility**
> Dict[str, bool] check_current_campaign_eligibility(address)

Check Current Campaign Eligibility

Retrieves a dictionary that shows eligibility status of the agent in current campaign  A key in the dictionary is the condition name  and the corresponding value shows if the condition is met/unmet (True/False) by the agent

### Example


```python
import search_api
from search_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = search_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with search_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = search_api.AgentsApi(api_client)
    address = 'address_example' # str | 

    try:
        # Check Current Campaign Eligibility
        api_response = api_instance.check_current_campaign_eligibility(address)
        print("The response of AgentsApi->check_current_campaign_eligibility:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->check_current_campaign_eligibility: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**|  | 

### Return type

**Dict[str, bool]**

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

# **get_agent_interactions_count**
> AgentInteractionCountsResponse get_agent_interactions_count(address)

Get Interaction Counts Of Agent

Retrieves interaction count histories and all-time interaction counts of the agent

### Example


```python
import search_api
from search_api.models.agent_interaction_counts_response import AgentInteractionCountsResponse
from search_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = search_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with search_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = search_api.AgentsApi(api_client)
    address = 'address_example' # str | The address of the agent

    try:
        # Get Interaction Counts Of Agent
        api_response = api_instance.get_agent_interactions_count(address)
        print("The response of AgentsApi->get_agent_interactions_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->get_agent_interactions_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| The address of the agent | 

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

# **search_agent_by_geolocation**
> AgentSearchResponse search_agent_by_geolocation(agent_geo_search_request)

Search Agent By Geolocation

### Example


```python
import search_api
from search_api.models.agent_geo_search_request import AgentGeoSearchRequest
from search_api.models.agent_search_response import AgentSearchResponse
from search_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = search_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with search_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = search_api.AgentsApi(api_client)
    agent_geo_search_request = search_api.AgentGeoSearchRequest() # AgentGeoSearchRequest | 

    try:
        # Search Agent By Geolocation
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

# **search_agent_tags**
> AgentTagSearchResponse search_agent_tags(prefix=prefix, limit=limit)

Search Agent Tags

### Example


```python
import search_api
from search_api.models.agent_tag_search_response import AgentTagSearchResponse
from search_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = search_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with search_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = search_api.AgentsApi(api_client)
    prefix = 'prefix_example' # str |  (optional)
    limit = 5 # int |  (optional) (default to 5)

    try:
        # Search Agent Tags
        api_response = api_instance.search_agent_tags(prefix=prefix, limit=limit)
        print("The response of AgentsApi->search_agent_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->search_agent_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prefix** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 5]

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
import search_api
from search_api.models.agent_search_request import AgentSearchRequest
from search_api.models.agent_search_response import AgentSearchResponse
from search_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = search_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with search_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = search_api.AgentsApi(api_client)
    agent_search_request = search_api.AgentSearchRequest() # AgentSearchRequest | 

    try:
        # Search Agents
        api_response = api_instance.search_agents(agent_search_request)
        print("The response of AgentsApi->search_agents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->search_agents: %s\n" % e)
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

# **select_agent**
> object select_agent(agent_clicked_request)

Select Agent

### Example


```python
import search_api
from search_api.models.agent_clicked_request import AgentClickedRequest
from search_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = search_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with search_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = search_api.AgentsApi(api_client)
    agent_clicked_request = search_api.AgentClickedRequest() # AgentClickedRequest | 

    try:
        # Select Agent
        api_response = api_instance.select_agent(agent_clicked_request)
        print("The response of AgentsApi->select_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->select_agent: %s\n" % e)
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

