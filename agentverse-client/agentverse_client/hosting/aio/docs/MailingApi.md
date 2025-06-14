# agentverse_client.hosting.aio.MailingApi

All URIs are relative to *https://agentverse.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subscribe_to_newsletter**](MailingApi.md#subscribe_to_newsletter) | **POST** /v1/hosting/mailing-list/subscribe | Subscribe To Newsletter


# **subscribe_to_newsletter**
> SubscriptionResponse subscribe_to_newsletter(email)

Subscribe To Newsletter

### Example


```python
import agentverse_client.hosting.aio
from agentverse_client.hosting.aio.models.subscription_response import SubscriptionResponse
from agentverse_client.hosting.aio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.hosting.aio.Configuration(
    host = "https://agentverse.ai"
)


# Enter a context with an instance of the API client
async with agentverse_client.hosting.aio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.hosting.aio.MailingApi(api_client)
    email = 'email_example' # str | 

    try:
        # Subscribe To Newsletter
        api_response = await api_instance.subscribe_to_newsletter(email)
        print("The response of MailingApi->subscribe_to_newsletter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailingApi->subscribe_to_newsletter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 

### Return type

[**SubscriptionResponse**](SubscriptionResponse.md)

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

