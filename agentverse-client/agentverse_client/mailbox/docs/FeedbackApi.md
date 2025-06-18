# agentverse_client.mailbox.FeedbackApi

All URIs are relative to *https://agentverse.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**submit_anonymous_feedback**](FeedbackApi.md#submit_anonymous_feedback) | **POST** /v1/feedback-anon | Submit Anon Feedback
[**submit_authenticated_feedback**](FeedbackApi.md#submit_authenticated_feedback) | **POST** /v1/feedback | Submit Feedback


# **submit_anonymous_feedback**
> object submit_anonymous_feedback(feedback_anon)

Submit Anon Feedback

### Example


```python
import agentverse_client.mailbox
from agentverse_client.mailbox.models.feedback_anon import FeedbackAnon
from agentverse_client.mailbox.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.mailbox.Configuration(
    host = "https://agentverse.ai"
)


# Enter a context with an instance of the API client
with agentverse_client.mailbox.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.mailbox.FeedbackApi(api_client)
    feedback_anon = agentverse_client.mailbox.FeedbackAnon() # FeedbackAnon | 

    try:
        # Submit Anon Feedback
        api_response = api_instance.submit_anonymous_feedback(feedback_anon)
        print("The response of FeedbackApi->submit_anonymous_feedback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeedbackApi->submit_anonymous_feedback: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feedback_anon** | [**FeedbackAnon**](FeedbackAnon.md)|  | 

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

# **submit_authenticated_feedback**
> object submit_authenticated_feedback(feedback)

Submit Feedback

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.mailbox
from agentverse_client.mailbox.models.feedback import Feedback
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
    api_instance = agentverse_client.mailbox.FeedbackApi(api_client)
    feedback = agentverse_client.mailbox.Feedback() # Feedback | 

    try:
        # Submit Feedback
        api_response = api_instance.submit_authenticated_feedback(feedback)
        print("The response of FeedbackApi->submit_authenticated_feedback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeedbackApi->submit_authenticated_feedback: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feedback** | [**Feedback**](Feedback.md)|  | 

### Return type

**object**

### Authorization

[FaunaAuthorizationScheme](../README.md#FaunaAuthorizationScheme)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

