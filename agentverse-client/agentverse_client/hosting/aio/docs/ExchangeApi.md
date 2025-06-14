# agentverse_client.hosting.aio.ExchangeApi

All URIs are relative to *https://agentverse.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**agent_readiness_probe**](ExchangeApi.md#agent_readiness_probe) | **HEAD** /v1/hosting/submit | Agent Readiness Probe
[**submit_message_envelope**](ExchangeApi.md#submit_message_envelope) | **POST** /v1/hosting/submit | Submit Message Envelope


# **agent_readiness_probe**
> object agent_readiness_probe(no_cache=no_cache)

Agent Readiness Probe

### Example


```python
import agentverse_client.hosting.aio
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
    api_instance = agentverse_client.hosting.aio.ExchangeApi(api_client)
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Agent Readiness Probe
        api_response = await api_instance.agent_readiness_probe(no_cache=no_cache)
        print("The response of ExchangeApi->agent_readiness_probe:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExchangeApi->agent_readiness_probe: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **no_cache** | **bool**|  | [optional] [default to False]

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

# **submit_message_envelope**
> ResponseSubmitMessageEnvelope submit_message_envelope(envelope, no_cache=no_cache)

Submit Message Envelope

### Example


```python
import agentverse_client.hosting.aio
from agentverse_client.hosting.aio.models.envelope import Envelope
from agentverse_client.hosting.aio.models.response_submit_message_envelope import ResponseSubmitMessageEnvelope
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
    api_instance = agentverse_client.hosting.aio.ExchangeApi(api_client)
    envelope = agentverse_client.hosting.aio.Envelope() # Envelope | 
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Submit Message Envelope
        api_response = await api_instance.submit_message_envelope(envelope, no_cache=no_cache)
        print("The response of ExchangeApi->submit_message_envelope:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExchangeApi->submit_message_envelope: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **envelope** | [**Envelope**](Envelope.md)|  | 
 **no_cache** | **bool**|  | [optional] [default to False]

### Return type

[**ResponseSubmitMessageEnvelope**](ResponseSubmitMessageEnvelope.md)

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

