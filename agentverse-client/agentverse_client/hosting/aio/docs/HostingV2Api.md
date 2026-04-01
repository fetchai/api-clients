# agentverse_client.hosting.aio.HostingV2Api

All URIs are relative to *https://agentverse.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**agent_readiness_probe_v2**](HostingV2Api.md#agent_readiness_probe_v2) | **HEAD** /v2/hosting/submit | Agent Readiness Probe
[**create_hosted_agent_v2**](HostingV2Api.md#create_hosted_agent_v2) | **POST** /v2/hosting | Create Hosted Agent
[**delete_agent_logs_v2**](HostingV2Api.md#delete_agent_logs_v2) | **DELETE** /v2/hosting/{address}/logs | Delete Agent Logs
[**delete_agent_secret_v2**](HostingV2Api.md#delete_agent_secret_v2) | **DELETE** /v2/hosting/{address}/secrets/{name} | Delete Secret Endpoint
[**delete_agent_storage_v2**](HostingV2Api.md#delete_agent_storage_v2) | **DELETE** /v2/hosting/{address}/storage/{key} | Delete Storage
[**delete_hosted_agent_v2**](HostingV2Api.md#delete_hosted_agent_v2) | **DELETE** /v2/hosting/{address} | Delete Agent
[**get_agent_code_v2**](HostingV2Api.md#get_agent_code_v2) | **GET** /v2/hosting/{address}/code | Get Code
[**get_agent_logs_v2**](HostingV2Api.md#get_agent_logs_v2) | **GET** /v2/hosting/{address}/logs | Get Agent Logs
[**get_agent_secrets_v2**](HostingV2Api.md#get_agent_secrets_v2) | **GET** /v2/hosting/{address}/secrets | Get Secrets
[**get_agent_storage_by_key_v2**](HostingV2Api.md#get_agent_storage_by_key_v2) | **GET** /v2/hosting/{address}/storage/{key} | Get Storage By Key
[**get_agent_storage_v2**](HostingV2Api.md#get_agent_storage_v2) | **GET** /v2/hosting/{address}/storage | Get Storage
[**get_all_user_secrets_v2**](HostingV2Api.md#get_all_user_secrets_v2) | **GET** /v2/hosting/secrets | Get All Secrets
[**get_all_user_storage_v2**](HostingV2Api.md#get_all_user_storage_v2) | **GET** /v2/hosting/storage | Get All Storage
[**get_hosted_agent_v2**](HostingV2Api.md#get_hosted_agent_v2) | **GET** /v2/hosting/{address} | Get Hosted Agent
[**get_specific_secret_v2**](HostingV2Api.md#get_specific_secret_v2) | **GET** /v2/hosting/{address}/secrets/{name} | Get Specific Secret
[**list_hosted_agents_v2**](HostingV2Api.md#list_hosted_agents_v2) | **GET** /v2/hosting | List Hosted Agents
[**start_hosted_agent_v2**](HostingV2Api.md#start_hosted_agent_v2) | **POST** /v2/hosting/{address}/start | Start Agent
[**stop_hosted_agent_v2**](HostingV2Api.md#stop_hosted_agent_v2) | **POST** /v2/hosting/{address}/stop | Stop Agent
[**submit_message_envelope_v2**](HostingV2Api.md#submit_message_envelope_v2) | **POST** /v2/hosting/submit | Submit Message Envelope
[**update_agent_code_v2**](HostingV2Api.md#update_agent_code_v2) | **PUT** /v2/hosting/{address}/code | Update Code
[**update_agent_secret_v2**](HostingV2Api.md#update_agent_secret_v2) | **PUT** /v2/hosting/{address}/secrets/{name} | Update Secret
[**update_agent_storage_v2**](HostingV2Api.md#update_agent_storage_v2) | **PUT** /v2/hosting/{address}/storage/{key} | Update Storage


# **agent_readiness_probe_v2**
> object agent_readiness_probe_v2(no_cache=no_cache)

Agent Readiness Probe

Check if an agent is ready to receive messages.

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
    api_instance = agentverse_client.hosting.aio.HostingV2Api(api_client)
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Agent Readiness Probe
        api_response = await api_instance.agent_readiness_probe_v2(no_cache=no_cache)
        print("The response of HostingV2Api->agent_readiness_probe_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingV2Api->agent_readiness_probe_v2: %s\n" % e)
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

# **create_hosted_agent_v2**
> AgentV2 create_hosted_agent_v2(no_cache=no_cache)

Create Hosted Agent

Create a new hosted agent without profile information.  Profile data (name, readme, avatar, description) should be managed via the hub API. This endpoint only creates the agent identity and address in the hosting service and then proves ownership of the agent to the hub service.

### Example


```python
import agentverse_client.hosting.aio
from agentverse_client.hosting.aio.models.agent_v2 import AgentV2
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
    api_instance = agentverse_client.hosting.aio.HostingV2Api(api_client)
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Create Hosted Agent
        api_response = await api_instance.create_hosted_agent_v2(no_cache=no_cache)
        print("The response of HostingV2Api->create_hosted_agent_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingV2Api->create_hosted_agent_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **no_cache** | **bool**|  | [optional] [default to False]

### Return type

[**AgentV2**](AgentV2.md)

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

# **delete_agent_logs_v2**
> object delete_agent_logs_v2(address, no_cache=no_cache)

Delete Agent Logs

Delete all logs for a hosted agent.

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
    api_instance = agentverse_client.hosting.aio.HostingV2Api(api_client)
    address = 'address_example' # str | 
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Delete Agent Logs
        api_response = await api_instance.delete_agent_logs_v2(address, no_cache=no_cache)
        print("The response of HostingV2Api->delete_agent_logs_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingV2Api->delete_agent_logs_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**|  | 
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

# **delete_agent_secret_v2**
> object delete_agent_secret_v2(address, name, no_cache=no_cache)

Delete Secret Endpoint

Delete a secret for an agent.

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
    api_instance = agentverse_client.hosting.aio.HostingV2Api(api_client)
    address = 'address_example' # str | 
    name = 'name_example' # str | 
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Delete Secret Endpoint
        api_response = await api_instance.delete_agent_secret_v2(address, name, no_cache=no_cache)
        print("The response of HostingV2Api->delete_agent_secret_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingV2Api->delete_agent_secret_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**|  | 
 **name** | **str**|  | 
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

# **delete_agent_storage_v2**
> object delete_agent_storage_v2(address, key, no_cache=no_cache)

Delete Storage

Delete a storage item for an agent.

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
    api_instance = agentverse_client.hosting.aio.HostingV2Api(api_client)
    address = 'address_example' # str | 
    key = 'key_example' # str | 
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Delete Storage
        api_response = await api_instance.delete_agent_storage_v2(address, key, no_cache=no_cache)
        print("The response of HostingV2Api->delete_agent_storage_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingV2Api->delete_agent_storage_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**|  | 
 **key** | **str**|  | 
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

# **delete_hosted_agent_v2**
> Dict[str, object] delete_hosted_agent_v2(address, no_cache=no_cache)

Delete Agent

Delete a hosted agent (v2 - also removes profile from hub if migrated).

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
    api_instance = agentverse_client.hosting.aio.HostingV2Api(api_client)
    address = 'address_example' # str | 
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Delete Agent
        api_response = await api_instance.delete_hosted_agent_v2(address, no_cache=no_cache)
        print("The response of HostingV2Api->delete_hosted_agent_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingV2Api->delete_hosted_agent_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**|  | 
 **no_cache** | **bool**|  | [optional] [default to False]

### Return type

**Dict[str, object]**

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

# **get_agent_code_v2**
> AgentCode get_agent_code_v2(address, no_cache=no_cache)

Get Code

Get the current code for an agent.

### Example


```python
import agentverse_client.hosting.aio
from agentverse_client.hosting.aio.models.agent_code import AgentCode
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
    api_instance = agentverse_client.hosting.aio.HostingV2Api(api_client)
    address = 'address_example' # str | 
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Get Code
        api_response = await api_instance.get_agent_code_v2(address, no_cache=no_cache)
        print("The response of HostingV2Api->get_agent_code_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingV2Api->get_agent_code_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**|  | 
 **no_cache** | **bool**|  | [optional] [default to False]

### Return type

[**AgentCode**](AgentCode.md)

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

# **get_agent_logs_v2**
> List[AgentLog] get_agent_logs_v2(address, no_cache=no_cache)

Get Agent Logs

Get the latest logs for a hosted agent.

### Example


```python
import agentverse_client.hosting.aio
from agentverse_client.hosting.aio.models.agent_log import AgentLog
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
    api_instance = agentverse_client.hosting.aio.HostingV2Api(api_client)
    address = 'address_example' # str | 
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Get Agent Logs
        api_response = await api_instance.get_agent_logs_v2(address, no_cache=no_cache)
        print("The response of HostingV2Api->get_agent_logs_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingV2Api->get_agent_logs_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**|  | 
 **no_cache** | **bool**|  | [optional] [default to False]

### Return type

[**List[AgentLog]**](AgentLog.md)

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

# **get_agent_secrets_v2**
> SecretList get_agent_secrets_v2(address, no_cache=no_cache)

Get Secrets

Get all secrets for an agent.

### Example


```python
import agentverse_client.hosting.aio
from agentverse_client.hosting.aio.models.secret_list import SecretList
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
    api_instance = agentverse_client.hosting.aio.HostingV2Api(api_client)
    address = 'address_example' # str | 
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Get Secrets
        api_response = await api_instance.get_agent_secrets_v2(address, no_cache=no_cache)
        print("The response of HostingV2Api->get_agent_secrets_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingV2Api->get_agent_secrets_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**|  | 
 **no_cache** | **bool**|  | [optional] [default to False]

### Return type

[**SecretList**](SecretList.md)

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

# **get_agent_storage_by_key_v2**
> StorageItem get_agent_storage_by_key_v2(address, key, no_cache=no_cache)

Get Storage By Key

Get a specific storage item by key.

### Example


```python
import agentverse_client.hosting.aio
from agentverse_client.hosting.aio.models.storage_item import StorageItem
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
    api_instance = agentverse_client.hosting.aio.HostingV2Api(api_client)
    address = 'address_example' # str | 
    key = 'key_example' # str | 
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Get Storage By Key
        api_response = await api_instance.get_agent_storage_by_key_v2(address, key, no_cache=no_cache)
        print("The response of HostingV2Api->get_agent_storage_by_key_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingV2Api->get_agent_storage_by_key_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**|  | 
 **key** | **str**|  | 
 **no_cache** | **bool**|  | [optional] [default to False]

### Return type

[**StorageItem**](StorageItem.md)

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

# **get_agent_storage_v2**
> WithPaginationStorageItem get_agent_storage_v2(address, cursor=cursor, no_cache=no_cache)

Get Storage

Get all storage items for an agent.

### Example


```python
import agentverse_client.hosting.aio
from agentverse_client.hosting.aio.models.with_pagination_storage_item import WithPaginationStorageItem
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
    api_instance = agentverse_client.hosting.aio.HostingV2Api(api_client)
    address = 'address_example' # str | 
    cursor = 'cursor_example' # str |  (optional)
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Get Storage
        api_response = await api_instance.get_agent_storage_v2(address, cursor=cursor, no_cache=no_cache)
        print("The response of HostingV2Api->get_agent_storage_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingV2Api->get_agent_storage_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**|  | 
 **cursor** | **str**|  | [optional] 
 **no_cache** | **bool**|  | [optional] [default to False]

### Return type

[**WithPaginationStorageItem**](WithPaginationStorageItem.md)

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

# **get_all_user_secrets_v2**
> SecretList get_all_user_secrets_v2(no_cache=no_cache)

Get All Secrets

Get all secrets for the authenticated user across all agents.

### Example


```python
import agentverse_client.hosting.aio
from agentverse_client.hosting.aio.models.secret_list import SecretList
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
    api_instance = agentverse_client.hosting.aio.HostingV2Api(api_client)
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Get All Secrets
        api_response = await api_instance.get_all_user_secrets_v2(no_cache=no_cache)
        print("The response of HostingV2Api->get_all_user_secrets_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingV2Api->get_all_user_secrets_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **no_cache** | **bool**|  | [optional] [default to False]

### Return type

[**SecretList**](SecretList.md)

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

# **get_all_user_storage_v2**
> WithPaginationStorageItem get_all_user_storage_v2(cursor=cursor, no_cache=no_cache)

Get All Storage

Get all storage items for the authenticated user across all agents.

### Example


```python
import agentverse_client.hosting.aio
from agentverse_client.hosting.aio.models.with_pagination_storage_item import WithPaginationStorageItem
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
    api_instance = agentverse_client.hosting.aio.HostingV2Api(api_client)
    cursor = 'cursor_example' # str |  (optional)
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Get All Storage
        api_response = await api_instance.get_all_user_storage_v2(cursor=cursor, no_cache=no_cache)
        print("The response of HostingV2Api->get_all_user_storage_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingV2Api->get_all_user_storage_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**|  | [optional] 
 **no_cache** | **bool**|  | [optional] [default to False]

### Return type

[**WithPaginationStorageItem**](WithPaginationStorageItem.md)

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

# **get_hosted_agent_v2**
> AgentV2 get_hosted_agent_v2(address, no_cache=no_cache)

Get Hosted Agent

Get a specific hosted agent by address.  Note: Profile data (name, readme, etc.) should be fetched from the hub API. This endpoint returns agent hosting metadata only.

### Example


```python
import agentverse_client.hosting.aio
from agentverse_client.hosting.aio.models.agent_v2 import AgentV2
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
    api_instance = agentverse_client.hosting.aio.HostingV2Api(api_client)
    address = 'address_example' # str | 
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Get Hosted Agent
        api_response = await api_instance.get_hosted_agent_v2(address, no_cache=no_cache)
        print("The response of HostingV2Api->get_hosted_agent_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingV2Api->get_hosted_agent_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**|  | 
 **no_cache** | **bool**|  | [optional] [default to False]

### Return type

[**AgentV2**](AgentV2.md)

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

# **get_specific_secret_v2**
> Secret get_specific_secret_v2(address, name, no_cache=no_cache)

Get Specific Secret

Get a specific secret by name for an agent.

### Example


```python
import agentverse_client.hosting.aio
from agentverse_client.hosting.aio.models.secret import Secret
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
    api_instance = agentverse_client.hosting.aio.HostingV2Api(api_client)
    address = 'address_example' # str | 
    name = 'name_example' # str | 
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Get Specific Secret
        api_response = await api_instance.get_specific_secret_v2(address, name, no_cache=no_cache)
        print("The response of HostingV2Api->get_specific_secret_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingV2Api->get_specific_secret_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**|  | 
 **name** | **str**|  | 
 **no_cache** | **bool**|  | [optional] [default to False]

### Return type

[**Secret**](Secret.md)

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

# **list_hosted_agents_v2**
> WithPaginationAgentV2 list_hosted_agents_v2(cursor=cursor, no_cache=no_cache)

List Hosted Agents

List all hosted agents for the authenticated user.  Note: Profile data (name, readme, etc.) should be fetched from the hub API. This endpoint returns agent hosting metadata only. Agent lists should primarily be fetched from the hub API for richer profile-based features.

### Example


```python
import agentverse_client.hosting.aio
from agentverse_client.hosting.aio.models.with_pagination_agent_v2 import WithPaginationAgentV2
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
    api_instance = agentverse_client.hosting.aio.HostingV2Api(api_client)
    cursor = 'cursor_example' # str |  (optional)
    no_cache = False # bool |  (optional) (default to False)

    try:
        # List Hosted Agents
        api_response = await api_instance.list_hosted_agents_v2(cursor=cursor, no_cache=no_cache)
        print("The response of HostingV2Api->list_hosted_agents_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingV2Api->list_hosted_agents_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**|  | [optional] 
 **no_cache** | **bool**|  | [optional] [default to False]

### Return type

[**WithPaginationAgentV2**](WithPaginationAgentV2.md)

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

# **start_hosted_agent_v2**
> AgentV2 start_hosted_agent_v2(address, no_cache=no_cache)

Start Agent

Start a hosted agent.

### Example


```python
import agentverse_client.hosting.aio
from agentverse_client.hosting.aio.models.agent_v2 import AgentV2
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
    api_instance = agentverse_client.hosting.aio.HostingV2Api(api_client)
    address = 'address_example' # str | 
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Start Agent
        api_response = await api_instance.start_hosted_agent_v2(address, no_cache=no_cache)
        print("The response of HostingV2Api->start_hosted_agent_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingV2Api->start_hosted_agent_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**|  | 
 **no_cache** | **bool**|  | [optional] [default to False]

### Return type

[**AgentV2**](AgentV2.md)

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

# **stop_hosted_agent_v2**
> AgentV2 stop_hosted_agent_v2(address, no_cache=no_cache)

Stop Agent

Stop a hosted agent.

### Example


```python
import agentverse_client.hosting.aio
from agentverse_client.hosting.aio.models.agent_v2 import AgentV2
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
    api_instance = agentverse_client.hosting.aio.HostingV2Api(api_client)
    address = 'address_example' # str | 
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Stop Agent
        api_response = await api_instance.stop_hosted_agent_v2(address, no_cache=no_cache)
        print("The response of HostingV2Api->stop_hosted_agent_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingV2Api->stop_hosted_agent_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**|  | 
 **no_cache** | **bool**|  | [optional] [default to False]

### Return type

[**AgentV2**](AgentV2.md)

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

# **submit_message_envelope_v2**
> ResponseSubmitMessageEnvelopeV2 submit_message_envelope_v2(envelope, no_cache=no_cache)

Submit Message Envelope

Submit a message envelope to a hosted agent.

### Example


```python
import agentverse_client.hosting.aio
from agentverse_client.hosting.aio.models.envelope import Envelope
from agentverse_client.hosting.aio.models.response_submit_message_envelope_v2 import ResponseSubmitMessageEnvelopeV2
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
    api_instance = agentverse_client.hosting.aio.HostingV2Api(api_client)
    envelope = agentverse_client.hosting.aio.Envelope() # Envelope | 
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Submit Message Envelope
        api_response = await api_instance.submit_message_envelope_v2(envelope, no_cache=no_cache)
        print("The response of HostingV2Api->submit_message_envelope_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingV2Api->submit_message_envelope_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **envelope** | [**Envelope**](Envelope.md)|  | 
 **no_cache** | **bool**|  | [optional] [default to False]

### Return type

[**ResponseSubmitMessageEnvelopeV2**](ResponseSubmitMessageEnvelopeV2.md)

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

# **update_agent_code_v2**
> AgentCodeDigest update_agent_code_v2(address, update_agent_code, no_cache=no_cache)

Update Code

Update the code for a specific agent.

### Example


```python
import agentverse_client.hosting.aio
from agentverse_client.hosting.aio.models.agent_code_digest import AgentCodeDigest
from agentverse_client.hosting.aio.models.update_agent_code import UpdateAgentCode
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
    api_instance = agentverse_client.hosting.aio.HostingV2Api(api_client)
    address = 'address_example' # str | 
    update_agent_code = agentverse_client.hosting.aio.UpdateAgentCode() # UpdateAgentCode | 
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Update Code
        api_response = await api_instance.update_agent_code_v2(address, update_agent_code, no_cache=no_cache)
        print("The response of HostingV2Api->update_agent_code_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingV2Api->update_agent_code_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**|  | 
 **update_agent_code** | [**UpdateAgentCode**](UpdateAgentCode.md)|  | 
 **no_cache** | **bool**|  | [optional] [default to False]

### Return type

[**AgentCodeDigest**](AgentCodeDigest.md)

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

# **update_agent_secret_v2**
> Secret update_agent_secret_v2(address, name, secret_update, no_cache=no_cache)

Update Secret

Create or update a secret for an agent.

### Example


```python
import agentverse_client.hosting.aio
from agentverse_client.hosting.aio.models.secret import Secret
from agentverse_client.hosting.aio.models.secret_update import SecretUpdate
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
    api_instance = agentverse_client.hosting.aio.HostingV2Api(api_client)
    address = 'address_example' # str | 
    name = 'name_example' # str | 
    secret_update = agentverse_client.hosting.aio.SecretUpdate() # SecretUpdate | 
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Update Secret
        api_response = await api_instance.update_agent_secret_v2(address, name, secret_update, no_cache=no_cache)
        print("The response of HostingV2Api->update_agent_secret_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingV2Api->update_agent_secret_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**|  | 
 **name** | **str**|  | 
 **secret_update** | [**SecretUpdate**](SecretUpdate.md)|  | 
 **no_cache** | **bool**|  | [optional] [default to False]

### Return type

[**Secret**](Secret.md)

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

# **update_agent_storage_v2**
> object update_agent_storage_v2(address, key, storage_item_update, no_cache=no_cache)

Update Storage

Update a storage item for an agent.

### Example


```python
import agentverse_client.hosting.aio
from agentverse_client.hosting.aio.models.storage_item_update import StorageItemUpdate
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
    api_instance = agentverse_client.hosting.aio.HostingV2Api(api_client)
    address = 'address_example' # str | 
    key = 'key_example' # str | 
    storage_item_update = agentverse_client.hosting.aio.StorageItemUpdate() # StorageItemUpdate | 
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Update Storage
        api_response = await api_instance.update_agent_storage_v2(address, key, storage_item_update, no_cache=no_cache)
        print("The response of HostingV2Api->update_agent_storage_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingV2Api->update_agent_storage_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**|  | 
 **key** | **str**|  | 
 **storage_item_update** | [**StorageItemUpdate**](StorageItemUpdate.md)|  | 
 **no_cache** | **bool**|  | [optional] [default to False]

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

