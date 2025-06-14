# agentverse_client.hosting.UsageApi

All URIs are relative to *https://agentverse.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_team_usage**](UsageApi.md#get_team_usage) | **GET** /v1/hosting/teams/{slug}/usage/current | Get Team Usage
[**get_team_usage_for_specific_month**](UsageApi.md#get_team_usage_for_specific_month) | **GET** /v1/hosting/teams/{slug}/usage/{year}/{month} | Get Team Usage For Specific Month
[**get_usage_for_specific_month**](UsageApi.md#get_usage_for_specific_month) | **GET** /v1/hosting/usage/{year}/{month} | Get Usage For Specific Month
[**get_user_usage**](UsageApi.md#get_user_usage) | **GET** /v1/hosting/usage/current | Get User Usage


# **get_team_usage**
> object get_team_usage(slug, no_cache=no_cache)

Get Team Usage

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.hosting
from agentverse_client.hosting.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.hosting.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with agentverse_client.hosting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.hosting.UsageApi(api_client)
    slug = 'slug_example' # str | 
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Get Team Usage
        api_response = api_instance.get_team_usage(slug, no_cache=no_cache)
        print("The response of UsageApi->get_team_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageApi->get_team_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **no_cache** | **bool**|  | [optional] [default to False]

### Return type

**object**

### Authorization

[FaunaAuthorizationScheme](../README.md#FaunaAuthorizationScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_usage_for_specific_month**
> object get_team_usage_for_specific_month(slug, year, month, no_cache=no_cache)

Get Team Usage For Specific Month

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.hosting
from agentverse_client.hosting.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.hosting.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with agentverse_client.hosting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.hosting.UsageApi(api_client)
    slug = 'slug_example' # str | 
    year = 56 # int | 
    month = 56 # int | 
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Get Team Usage For Specific Month
        api_response = api_instance.get_team_usage_for_specific_month(slug, year, month, no_cache=no_cache)
        print("The response of UsageApi->get_team_usage_for_specific_month:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageApi->get_team_usage_for_specific_month: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **year** | **int**|  | 
 **month** | **int**|  | 
 **no_cache** | **bool**|  | [optional] [default to False]

### Return type

**object**

### Authorization

[FaunaAuthorizationScheme](../README.md#FaunaAuthorizationScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_usage_for_specific_month**
> object get_usage_for_specific_month(year, month, no_cache=no_cache)

Get Usage For Specific Month

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.hosting
from agentverse_client.hosting.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.hosting.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with agentverse_client.hosting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.hosting.UsageApi(api_client)
    year = 56 # int | 
    month = 56 # int | 
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Get Usage For Specific Month
        api_response = api_instance.get_usage_for_specific_month(year, month, no_cache=no_cache)
        print("The response of UsageApi->get_usage_for_specific_month:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageApi->get_usage_for_specific_month: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**|  | 
 **month** | **int**|  | 
 **no_cache** | **bool**|  | [optional] [default to False]

### Return type

**object**

### Authorization

[FaunaAuthorizationScheme](../README.md#FaunaAuthorizationScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_usage**
> object get_user_usage(no_cache=no_cache)

Get User Usage

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.hosting
from agentverse_client.hosting.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.hosting.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with agentverse_client.hosting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.hosting.UsageApi(api_client)
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Get User Usage
        api_response = api_instance.get_user_usage(no_cache=no_cache)
        print("The response of UsageApi->get_user_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageApi->get_user_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **no_cache** | **bool**|  | [optional] [default to False]

### Return type

**object**

### Authorization

[FaunaAuthorizationScheme](../README.md#FaunaAuthorizationScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

