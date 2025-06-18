# agentverse_client.mailbox.aio.ExchangeApi

All URIs are relative to *https://agentverse.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**agent_readiness_probe**](ExchangeApi.md#agent_readiness_probe) | **HEAD** /v1/submit | Agent Readiness Probe
[**proxy_agent_readiness_probe**](ExchangeApi.md#proxy_agent_readiness_probe) | **HEAD** /v1/proxy/submit | Agent Readiness Probe
[**submit_message_envelope**](ExchangeApi.md#submit_message_envelope) | **POST** /v1/submit | Submit Message Envelope
[**submit_proxy_message_envelope**](ExchangeApi.md#submit_proxy_message_envelope) | **POST** /v1/proxy/submit | Submit Message Envelope


# **agent_readiness_probe**
> object agent_readiness_probe()

Agent Readiness Probe

### Example


```python
import agentverse_client.mailbox.aio
from agentverse_client.mailbox.aio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.mailbox.aio.Configuration(
    host = "https://agentverse.ai"
)


# Enter a context with an instance of the API client
async with agentverse_client.mailbox.aio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.mailbox.aio.ExchangeApi(api_client)

    try:
        # Agent Readiness Probe
        api_response = await api_instance.agent_readiness_probe()
        print("The response of ExchangeApi->agent_readiness_probe:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExchangeApi->agent_readiness_probe: %s\n" % e)
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

# **proxy_agent_readiness_probe**
> object proxy_agent_readiness_probe()

Agent Readiness Probe

### Example


```python
import agentverse_client.mailbox.aio
from agentverse_client.mailbox.aio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.mailbox.aio.Configuration(
    host = "https://agentverse.ai"
)


# Enter a context with an instance of the API client
async with agentverse_client.mailbox.aio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.mailbox.aio.ExchangeApi(api_client)

    try:
        # Agent Readiness Probe
        api_response = await api_instance.proxy_agent_readiness_probe()
        print("The response of ExchangeApi->proxy_agent_readiness_probe:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExchangeApi->proxy_agent_readiness_probe: %s\n" % e)
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

# **submit_message_envelope**
> object submit_message_envelope(envelope)

Submit Message Envelope

### Example


```python
import agentverse_client.mailbox.aio
from agentverse_client.mailbox.aio.models.envelope import Envelope
from agentverse_client.mailbox.aio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.mailbox.aio.Configuration(
    host = "https://agentverse.ai"
)


# Enter a context with an instance of the API client
async with agentverse_client.mailbox.aio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.mailbox.aio.ExchangeApi(api_client)
    envelope = agentverse_client.mailbox.aio.Envelope() # Envelope | 

    try:
        # Submit Message Envelope
        api_response = await api_instance.submit_message_envelope(envelope)
        print("The response of ExchangeApi->submit_message_envelope:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExchangeApi->submit_message_envelope: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **envelope** | [**Envelope**](Envelope.md)|  | 

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

# **submit_proxy_message_envelope**
> object submit_proxy_message_envelope(envelope)

Submit Message Envelope

### Example


```python
import agentverse_client.mailbox.aio
from agentverse_client.mailbox.aio.models.envelope import Envelope
from agentverse_client.mailbox.aio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.mailbox.aio.Configuration(
    host = "https://agentverse.ai"
)


# Enter a context with an instance of the API client
async with agentverse_client.mailbox.aio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.mailbox.aio.ExchangeApi(api_client)
    envelope = agentverse_client.mailbox.aio.Envelope() # Envelope | 

    try:
        # Submit Message Envelope
        api_response = await api_instance.submit_proxy_message_envelope(envelope)
        print("The response of ExchangeApi->submit_proxy_message_envelope:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExchangeApi->submit_proxy_message_envelope: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **envelope** | [**Envelope**](Envelope.md)|  | 

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

