# search_api_client.InternalApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**is_healthy**](InternalApi.md#is_healthy) | **GET** /internal/alive | Liveness Probe
[**is_ready**](InternalApi.md#is_ready) | **GET** /internal/ready | Readiness Probe


# **is_healthy**
> object is_healthy()

Liveness Probe

### Example


```python
import search_api_client
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
    api_instance = search_api_client.InternalApi(api_client)

    try:
        # Liveness Probe
        api_response = api_instance.is_healthy()
        print("The response of InternalApi->is_healthy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalApi->is_healthy: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

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

# **is_ready**
> object is_ready()

Readiness Probe

### Example


```python
import search_api_client
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
    api_instance = search_api_client.InternalApi(api_client)

    try:
        # Readiness Probe
        api_response = api_instance.is_ready()
        print("The response of InternalApi->is_ready:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalApi->is_ready: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

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

