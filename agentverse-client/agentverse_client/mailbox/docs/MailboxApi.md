# agentverse_client.mailbox.MailboxApi

All URIs are relative to *https://agentverse.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_all_mailbox_messages**](MailboxApi.md#delete_all_mailbox_messages) | **DELETE** /v1/mailbox | Delete All Mailbox Messages
[**delete_specific_envelope**](MailboxApi.md#delete_specific_envelope) | **DELETE** /v1/mailbox/{uuid} | Delete Specific Envelope
[**get_specific_envelope**](MailboxApi.md#get_specific_envelope) | **GET** /v1/mailbox/{uuid} | Get Specific Envelope
[**list_mailbox_messages**](MailboxApi.md#list_mailbox_messages) | **GET** /v1/mailbox | List Mailbox Messages


# **delete_all_mailbox_messages**
> object delete_all_mailbox_messages(authorization=authorization)

Delete All Mailbox Messages

### Example


```python
import agentverse_client.mailbox
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
    api_instance = agentverse_client.mailbox.MailboxApi(api_client)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Delete All Mailbox Messages
        api_response = api_instance.delete_all_mailbox_messages(authorization=authorization)
        print("The response of MailboxApi->delete_all_mailbox_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailboxApi->delete_all_mailbox_messages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_specific_envelope**
> object delete_specific_envelope(uuid, authorization=authorization)

Delete Specific Envelope

### Example


```python
import agentverse_client.mailbox
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
    api_instance = agentverse_client.mailbox.MailboxApi(api_client)
    uuid = 'uuid_example' # str | 
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Delete Specific Envelope
        api_response = api_instance.delete_specific_envelope(uuid, authorization=authorization)
        print("The response of MailboxApi->delete_specific_envelope:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailboxApi->delete_specific_envelope: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **authorization** | **str**|  | [optional] 

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_specific_envelope**
> StoredEnvelope get_specific_envelope(uuid, authorization=authorization)

Get Specific Envelope

### Example


```python
import agentverse_client.mailbox
from agentverse_client.mailbox.models.stored_envelope import StoredEnvelope
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
    api_instance = agentverse_client.mailbox.MailboxApi(api_client)
    uuid = 'uuid_example' # str | 
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Get Specific Envelope
        api_response = api_instance.get_specific_envelope(uuid, authorization=authorization)
        print("The response of MailboxApi->get_specific_envelope:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailboxApi->get_specific_envelope: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **authorization** | **str**|  | [optional] 

### Return type

[**StoredEnvelope**](StoredEnvelope.md)

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

# **list_mailbox_messages**
> PageStoredEnvelope list_mailbox_messages(page=page, size=size, authorization=authorization)

List Mailbox Messages

### Example


```python
import agentverse_client.mailbox
from agentverse_client.mailbox.models.page_stored_envelope import PageStoredEnvelope
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
    api_instance = agentverse_client.mailbox.MailboxApi(api_client)
    page = 1 # int | Page number (optional) (default to 1)
    size = 50 # int | Page size (optional) (default to 50)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # List Mailbox Messages
        api_response = api_instance.list_mailbox_messages(page=page, size=size, authorization=authorization)
        print("The response of MailboxApi->list_mailbox_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailboxApi->list_mailbox_messages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | [optional] [default to 1]
 **size** | **int**| Page size | [optional] [default to 50]
 **authorization** | **str**|  | [optional] 

### Return type

[**PageStoredEnvelope**](PageStoredEnvelope.md)

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

