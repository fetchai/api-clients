# agentverse_client.search.FunctionsApi

All URIs are relative to *https://agentverse.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_function_interactions**](FunctionsApi.md#get_function_interactions) | **GET** /v1/search/functions/interactions/{function_id} | Get Recent Interactions Of Function
[**search_functions**](FunctionsApi.md#search_functions) | **POST** /v1/search/functions | Search Functions


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
    api_instance = agentverse_client.search.FunctionsApi(api_client)
    function_id = 'function_id_example' # str | Unique identifier of the function

    try:
        # Get Recent Interactions Of Function
        api_response = api_instance.get_function_interactions(function_id)
        print("The response of FunctionsApi->get_function_interactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsApi->get_function_interactions: %s\n" % e)
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
    api_instance = agentverse_client.search.FunctionsApi(api_client)
    function_search_request = agentverse_client.search.FunctionSearchRequest() # FunctionSearchRequest | 

    try:
        # Search Functions
        api_response = api_instance.search_functions(function_search_request)
        print("The response of FunctionsApi->search_functions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsApi->search_functions: %s\n" % e)
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

