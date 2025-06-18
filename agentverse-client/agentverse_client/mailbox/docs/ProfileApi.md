# agentverse_client.mailbox.ProfileApi

All URIs are relative to *https://agentverse.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_team_user_usage**](ProfileApi.md#get_team_user_usage) | **GET** /v1/mailroom/teams/{slug}/profile/usage | Get User Usage
[**get_user_usage**](ProfileApi.md#get_user_usage) | **GET** /v1/profile/usage | Get User Usage


# **get_team_user_usage**
> UserUsage get_team_user_usage(slug)

Get User Usage

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.mailbox
from agentverse_client.mailbox.models.user_usage import UserUsage
from agentverse_client.mailbox.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.mailbox.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with agentverse_client.mailbox.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.mailbox.ProfileApi(api_client)
    slug = 'slug_example' # str | 

    try:
        # Get User Usage
        api_response = api_instance.get_team_user_usage(slug)
        print("The response of ProfileApi->get_team_user_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->get_team_user_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 

### Return type

[**UserUsage**](UserUsage.md)

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
> UserUsage get_user_usage()

Get User Usage

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.mailbox
from agentverse_client.mailbox.models.user_usage import UserUsage
from agentverse_client.mailbox.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.mailbox.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with agentverse_client.mailbox.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.mailbox.ProfileApi(api_client)

    try:
        # Get User Usage
        api_response = api_instance.get_user_usage()
        print("The response of ProfileApi->get_user_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->get_user_usage: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UserUsage**](UserUsage.md)

### Authorization

[FaunaAuthorizationScheme](../README.md#FaunaAuthorizationScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

