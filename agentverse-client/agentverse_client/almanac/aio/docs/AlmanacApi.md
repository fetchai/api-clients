# agentverse_client.almanac.aio.AlmanacApi

All URIs are relative to *https://agentverse.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_agent**](AlmanacApi.md#get_agent) | **GET** /v1/almanac/agents/{address} | Get Specific Agent
[**get_recently_registered_agents**](AlmanacApi.md#get_recently_registered_agents) | **GET** /v1/almanac/recent | Get Recently Registered Agents
[**register_agent**](AlmanacApi.md#register_agent) | **POST** /v1/almanac/agents | Register Agent
[**register_agents_batch_v1_almanac_agents_batch_post**](AlmanacApi.md#register_agents_batch_v1_almanac_agents_batch_post) | **POST** /v1/almanac/agents/batch | Register Agents Batch
[**update_agent_status**](AlmanacApi.md#update_agent_status) | **POST** /v1/almanac/agents/{agent_address}/status | Update Agent Status


# **get_agent**
> Agent get_agent(address, prefix=prefix)

Get Specific Agent

### Example


```python
import agentverse_client.almanac.aio
from agentverse_client.almanac.aio.models.agent import Agent
from agentverse_client.almanac.aio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.almanac.aio.Configuration(
    host = "https://agentverse.ai"
)


# Enter a context with an instance of the API client
async with agentverse_client.almanac.aio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.almanac.aio.AlmanacApi(api_client)
    address = 'address_example' # str | 
    prefix = 'prefix_example' # str |  (optional)

    try:
        # Get Specific Agent
        api_response = await api_instance.get_agent(address, prefix=prefix)
        print("The response of AlmanacApi->get_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlmanacApi->get_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**|  | 
 **prefix** | **str**|  | [optional] 

### Return type

[**Agent**](Agent.md)

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

# **get_recently_registered_agents**
> List[Agent] get_recently_registered_agents()

Get Recently Registered Agents

### Example


```python
import agentverse_client.almanac.aio
from agentverse_client.almanac.aio.models.agent import Agent
from agentverse_client.almanac.aio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.almanac.aio.Configuration(
    host = "https://agentverse.ai"
)


# Enter a context with an instance of the API client
async with agentverse_client.almanac.aio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.almanac.aio.AlmanacApi(api_client)

    try:
        # Get Recently Registered Agents
        api_response = await api_instance.get_recently_registered_agents()
        print("The response of AlmanacApi->get_recently_registered_agents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlmanacApi->get_recently_registered_agents: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Agent]**](Agent.md)

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

# **register_agent**
> object register_agent(agent_registration_attestation)

Register Agent

### Example


```python
import agentverse_client.almanac.aio
from agentverse_client.almanac.aio.models.agent_registration_attestation import AgentRegistrationAttestation
from agentverse_client.almanac.aio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.almanac.aio.Configuration(
    host = "https://agentverse.ai"
)


# Enter a context with an instance of the API client
async with agentverse_client.almanac.aio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.almanac.aio.AlmanacApi(api_client)
    agent_registration_attestation = agentverse_client.almanac.aio.AgentRegistrationAttestation() # AgentRegistrationAttestation | 

    try:
        # Register Agent
        api_response = await api_instance.register_agent(agent_registration_attestation)
        print("The response of AlmanacApi->register_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlmanacApi->register_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_registration_attestation** | [**AgentRegistrationAttestation**](AgentRegistrationAttestation.md)|  | 

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

# **register_agents_batch_v1_almanac_agents_batch_post**
> object register_agents_batch_v1_almanac_agents_batch_post(agent_registration_attestation_batch)

Register Agents Batch

### Example


```python
import agentverse_client.almanac.aio
from agentverse_client.almanac.aio.models.agent_registration_attestation_batch import AgentRegistrationAttestationBatch
from agentverse_client.almanac.aio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.almanac.aio.Configuration(
    host = "https://agentverse.ai"
)


# Enter a context with an instance of the API client
async with agentverse_client.almanac.aio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.almanac.aio.AlmanacApi(api_client)
    agent_registration_attestation_batch = agentverse_client.almanac.aio.AgentRegistrationAttestationBatch() # AgentRegistrationAttestationBatch | 

    try:
        # Register Agents Batch
        api_response = await api_instance.register_agents_batch_v1_almanac_agents_batch_post(agent_registration_attestation_batch)
        print("The response of AlmanacApi->register_agents_batch_v1_almanac_agents_batch_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlmanacApi->register_agents_batch_v1_almanac_agents_batch_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_registration_attestation_batch** | [**AgentRegistrationAttestationBatch**](AgentRegistrationAttestationBatch.md)|  | 

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

# **update_agent_status**
> object update_agent_status(agent_address, agent_status_update)

Update Agent Status

### Example


```python
import agentverse_client.almanac.aio
from agentverse_client.almanac.aio.models.agent_status_update import AgentStatusUpdate
from agentverse_client.almanac.aio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.almanac.aio.Configuration(
    host = "https://agentverse.ai"
)


# Enter a context with an instance of the API client
async with agentverse_client.almanac.aio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.almanac.aio.AlmanacApi(api_client)
    agent_address = 'agent_address_example' # str | 
    agent_status_update = agentverse_client.almanac.aio.AgentStatusUpdate() # AgentStatusUpdate | 

    try:
        # Update Agent Status
        api_response = await api_instance.update_agent_status(agent_address, agent_status_update)
        print("The response of AlmanacApi->update_agent_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlmanacApi->update_agent_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_address** | **str**|  | 
 **agent_status_update** | [**AgentStatusUpdate**](AgentStatusUpdate.md)|  | 

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

