# agentverse_client.almanac.aio.UsageApi

All URIs are relative to *https://agentverse.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_usage**](UsageApi.md#get_user_usage) | **GET** /v1/almanac/usage/current | Get User Usage


# **get_user_usage**
> AlmanacUsage get_user_usage()

Get User Usage

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.almanac.aio
from agentverse_client.almanac.aio.models.almanac_usage import AlmanacUsage
from agentverse_client.almanac.aio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.almanac.aio.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with agentverse_client.almanac.aio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.almanac.aio.UsageApi(api_client)

    try:
        # Get User Usage
        api_response = await api_instance.get_user_usage()
        print("The response of UsageApi->get_user_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageApi->get_user_usage: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AlmanacUsage**](AlmanacUsage.md)

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

