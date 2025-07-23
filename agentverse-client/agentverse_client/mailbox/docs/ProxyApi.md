# agentverse_client.mailbox.ProxyApi

All URIs are relative to *https://agentverse.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_proxy_agent_endpoint**](ProxyApi.md#get_proxy_agent_endpoint) | **GET** /v1/proxy/resolve/{agent_address} | Get Proxy Agent Endpoint


# **get_proxy_agent_endpoint**
> AgentEndpoint get_proxy_agent_endpoint(agent_address)

Get Proxy Agent Endpoint

Get the endpoint for a proxy agent by its address.

### Example


```python
import agentverse_client.mailbox
from agentverse_client.mailbox.models.agent_endpoint import AgentEndpoint
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
    api_instance = agentverse_client.mailbox.ProxyApi(api_client)
    agent_address = 'agent_address_example' # str | 

    try:
        # Get Proxy Agent Endpoint
        api_response = api_instance.get_proxy_agent_endpoint(agent_address)
        print("The response of ProxyApi->get_proxy_agent_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProxyApi->get_proxy_agent_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_address** | **str**|  | 

### Return type

[**AgentEndpoint**](AgentEndpoint.md)

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

