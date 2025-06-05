# agentverse_client.hosting.HostingApi

All URIs are relative to *https://agentverse.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_team_agent**](HostingApi.md#create_team_agent) | **POST** /v1/hosting/teams/{slug}/agents | Create New Team Agent
[**create_team_agent_secret**](HostingApi.md#create_team_agent_secret) | **POST** /v1/hosting/teams/{slug}/secrets | Create Team Secret
[**create_user_agent**](HostingApi.md#create_user_agent) | **POST** /v1/hosting/agents | Create New User Agent
[**create_user_agent_secret**](HostingApi.md#create_user_agent_secret) | **POST** /v1/hosting/secrets | Create User Secret
[**delete_all_team_data**](HostingApi.md#delete_all_team_data) | **DELETE** /v1/hosting/teams/{slug}/remove-all-data | Delete All Team Data
[**delete_all_user_data**](HostingApi.md#delete_all_user_data) | **DELETE** /v1/hosting/remove-all-data | Delete All User Data
[**delete_logs_for_team_agent**](HostingApi.md#delete_logs_for_team_agent) | **DELETE** /v1/hosting/teams/{slug}/agents/{address}/logs | Delete Logs For Team Agent
[**delete_logs_for_user_agent**](HostingApi.md#delete_logs_for_user_agent) | **DELETE** /v1/hosting/agents/{address}/logs | Delete Logs For User Agent
[**delete_team_agent**](HostingApi.md#delete_team_agent) | **DELETE** /v1/hosting/teams/{slug}/agents/{address} | Delete Specific Team Agent
[**delete_team_agent_storage**](HostingApi.md#delete_team_agent_storage) | **DELETE** /v1/hosting/teams/{slug}/agents/{address}/storage/{key} | Delete Team Agent Storage
[**delete_team_secret**](HostingApi.md#delete_team_secret) | **DELETE** /v1/hosting/teams/{slug}/secrets/{address}/{name} | Delete User Secret
[**delete_user_agent**](HostingApi.md#delete_user_agent) | **DELETE** /v1/hosting/agents/{address} | Delete Specific User Agent
[**delete_user_agent_storage**](HostingApi.md#delete_user_agent_storage) | **DELETE** /v1/hosting/agents/{address}/storage/{key} | Delete User Agent Storage
[**delete_user_secret**](HostingApi.md#delete_user_secret) | **DELETE** /v1/hosting/secrets/{address}/{name} | Delete User Secret
[**duplicate_team_agent**](HostingApi.md#duplicate_team_agent) | **POST** /v1/hosting/teams/{slug}/agents/{address}/duplicate | Duplicate Specific Team Agent
[**duplicate_user_agent**](HostingApi.md#duplicate_user_agent) | **POST** /v1/hosting/agents/{address}/duplicate | Duplicate Specific User Agent
[**get_latest_logs_for_team_agent**](HostingApi.md#get_latest_logs_for_team_agent) | **GET** /v1/hosting/teams/{slug}/agents/{address}/logs/latest | Get Latest Logs For Team Agent
[**get_latest_logs_for_user_agent**](HostingApi.md#get_latest_logs_for_user_agent) | **GET** /v1/hosting/agents/{address}/logs/latest | Get Latest Logs For User Agent
[**get_new_achievements**](HostingApi.md#get_new_achievements) | **GET** /v1/hosting/achievements/new | Get New Achievements
[**get_supported_packages**](HostingApi.md#get_supported_packages) | **GET** /v1/hosting/packages | Get Supported Packages
[**get_team_agent_code**](HostingApi.md#get_team_agent_code) | **GET** /v1/hosting/teams/{slug}/agents/{address}/code | Get Team Agent Code
[**get_team_agent_details**](HostingApi.md#get_team_agent_details) | **GET** /v1/hosting/teams/{slug}/agents/{address} | Get Specific Teams Agent
[**get_team_agent_interactions**](HostingApi.md#get_team_agent_interactions) | **GET** /v1/hosting/teams/{slug}/agents/{address}/interactions | Get Agent Team Interactions
[**get_team_agent_metadata**](HostingApi.md#get_team_agent_metadata) | **GET** /v1/hosting/teams/{slug}/agents/{address}/metadata | Get Team Agent Metadata
[**get_team_agent_profile**](HostingApi.md#get_team_agent_profile) | **GET** /v1/hosting/teams/{slug}/agents/{address}/profile | Get Team Agent Public Profile
[**get_team_agent_secrets**](HostingApi.md#get_team_agent_secrets) | **GET** /v1/hosting/teams/{slug}/{address}/secrets | Get Team Agent Secrets
[**get_team_agent_storage**](HostingApi.md#get_team_agent_storage) | **GET** /v1/hosting/teams/{slug}/agents/{address}/storage | Get Team Agent Storage
[**get_team_agent_storage_by_key**](HostingApi.md#get_team_agent_storage_by_key) | **GET** /v1/hosting/teams/{slug}/agents/{address}/storage/{key} | Get Team Agent Storage By Key
[**get_unlocked_achievements**](HostingApi.md#get_unlocked_achievements) | **GET** /v1/hosting/achievements/unlocked | Get Unlocked Achievements
[**get_user_agent_code**](HostingApi.md#get_user_agent_code) | **GET** /v1/hosting/agents/{address}/code | Get User Agent Code
[**get_user_agent_details**](HostingApi.md#get_user_agent_details) | **GET** /v1/hosting/agents/{address} | Get Specific User Agent
[**get_user_agent_interactions**](HostingApi.md#get_user_agent_interactions) | **GET** /v1/hosting/agents/{address}/interactions | Get Agent User Interactions
[**get_user_agent_metadata**](HostingApi.md#get_user_agent_metadata) | **GET** /v1/hosting/agents/{address}/metadata | Get User Agent Metadata
[**get_user_agent_profile**](HostingApi.md#get_user_agent_profile) | **GET** /v1/hosting/agents/{address}/profile | Get User Agent Public Profile
[**get_user_agent_secrets**](HostingApi.md#get_user_agent_secrets) | **GET** /v1/hosting/{address}/secrets | Get User Agent Secrets
[**get_user_agent_storage**](HostingApi.md#get_user_agent_storage) | **GET** /v1/hosting/agents/{address}/storage | Get User Agent Storage
[**get_user_agent_storage_by_key**](HostingApi.md#get_user_agent_storage_by_key) | **GET** /v1/hosting/agents/{address}/storage/{key} | Get User Agent Storage By Key
[**get_user_secret**](HostingApi.md#get_user_secret) | **GET** /v1/hosting/teams/{slug}/secrets | Get User Secret
[**get_user_secrets**](HostingApi.md#get_user_secrets) | **GET** /v1/hosting/secrets | Get User Secret
[**list_team_agents**](HostingApi.md#list_team_agents) | **GET** /v1/hosting/teams/{slug}/agents | Get Team Agents
[**list_user_agents**](HostingApi.md#list_user_agents) | **GET** /v1/hosting/agents | Get User Agents
[**register_new_team_domain_name**](HostingApi.md#register_new_team_domain_name) | **POST** /v1/hosting/teams/{slug}/agents/{address}/domains/register | Register New Team Domain Name
[**register_new_user_domain_name**](HostingApi.md#register_new_user_domain_name) | **POST** /v1/hosting/agents/{address}/domains/register | Register New User Domain Name
[**start_specific_team_agent**](HostingApi.md#start_specific_team_agent) | **POST** /v1/hosting/teams/{slug}/agents/{address}/start | Start Specific Team Agent
[**start_specific_user_agent**](HostingApi.md#start_specific_user_agent) | **POST** /v1/hosting/agents/{address}/start | Start Specific User Agent
[**stop_specific_team_agent**](HostingApi.md#stop_specific_team_agent) | **POST** /v1/hosting/teams/{slug}/agents/{address}/stop | Stop Specific Team Agent
[**stop_specific_user_agent**](HostingApi.md#stop_specific_user_agent) | **POST** /v1/hosting/agents/{address}/stop | Stop Specific User Agent
[**update_team_agent**](HostingApi.md#update_team_agent) | **PUT** /v1/hosting/teams/{slug}/agents/{address} | Update Specific Team Agent
[**update_team_agent_code**](HostingApi.md#update_team_agent_code) | **PUT** /v1/hosting/teams/{slug}/agents/{address}/code | Update Team Agent Code
[**update_team_agent_metadata**](HostingApi.md#update_team_agent_metadata) | **PATCH** /v1/hosting/teams/{slug}/agents/{address}/metadata | Update Team Agent Metadata
[**update_team_agent_network**](HostingApi.md#update_team_agent_network) | **PUT** /v1/hosting/teams/{slug}/agents/{address}/network | Update Team Agent Network
[**update_team_agent_storage**](HostingApi.md#update_team_agent_storage) | **PUT** /v1/hosting/teams/{slug}/agents/{address}/storage/{key} | Update Team Agent Storage
[**update_user_agent**](HostingApi.md#update_user_agent) | **PUT** /v1/hosting/agents/{address} | Update Specific User Agent
[**update_user_agent_code**](HostingApi.md#update_user_agent_code) | **PUT** /v1/hosting/agents/{address}/code | Update User Agent Code
[**update_user_agent_metadata**](HostingApi.md#update_user_agent_metadata) | **PATCH** /v1/hosting/agents/{address}/metadata | Update User Agent Metadata
[**update_user_agent_network**](HostingApi.md#update_user_agent_network) | **PUT** /v1/hosting/agents/{address}/network | Update User Agent Network
[**update_user_agent_storage**](HostingApi.md#update_user_agent_storage) | **PUT** /v1/hosting/agents/{address}/storage/{key} | Update User Agent Storage


# **create_team_agent**
> Agent create_team_agent(slug, new_agent, no_cache=no_cache)

Create New Team Agent

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.hosting
from agentverse_client.hosting.models.agent import Agent
from agentverse_client.hosting.models.new_agent import NewAgent
from agentverse_client.hosting.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.hosting.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with agentverse_client.hosting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.hosting.HostingApi(api_client)
    slug = 'slug_example' # str | 
    new_agent = agentverse_client.hosting.NewAgent() # NewAgent | 
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Create New Team Agent
        api_response = api_instance.create_team_agent(slug, new_agent, no_cache=no_cache)
        print("The response of HostingApi->create_team_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingApi->create_team_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **new_agent** | [**NewAgent**](NewAgent.md)|  | 
 **no_cache** | **bool**|  | [optional] [default to False]

### Return type

[**Agent**](Agent.md)

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

# **create_team_agent_secret**
> Secret create_team_agent_secret(slug, secret_create, no_cache=no_cache)

Create Team Secret

Creates a new secret for the given agent.

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.hosting
from agentverse_client.hosting.models.secret import Secret
from agentverse_client.hosting.models.secret_create import SecretCreate
from agentverse_client.hosting.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.hosting.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with agentverse_client.hosting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.hosting.HostingApi(api_client)
    slug = 'slug_example' # str | 
    secret_create = agentverse_client.hosting.SecretCreate() # SecretCreate | 
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Create Team Secret
        api_response = api_instance.create_team_agent_secret(slug, secret_create, no_cache=no_cache)
        print("The response of HostingApi->create_team_agent_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingApi->create_team_agent_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **secret_create** | [**SecretCreate**](SecretCreate.md)|  | 
 **no_cache** | **bool**|  | [optional] [default to False]

### Return type

[**Secret**](Secret.md)

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

# **create_user_agent**
> Agent create_user_agent(new_agent, no_cache=no_cache)

Create New User Agent

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.hosting
from agentverse_client.hosting.models.agent import Agent
from agentverse_client.hosting.models.new_agent import NewAgent
from agentverse_client.hosting.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.hosting.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with agentverse_client.hosting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.hosting.HostingApi(api_client)
    new_agent = agentverse_client.hosting.NewAgent() # NewAgent | 
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Create New User Agent
        api_response = api_instance.create_user_agent(new_agent, no_cache=no_cache)
        print("The response of HostingApi->create_user_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingApi->create_user_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_agent** | [**NewAgent**](NewAgent.md)|  | 
 **no_cache** | **bool**|  | [optional] [default to False]

### Return type

[**Agent**](Agent.md)

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

# **create_user_agent_secret**
> Secret create_user_agent_secret(secret_create, no_cache=no_cache)

Create User Secret

Creates a new secret for the given agent.

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.hosting
from agentverse_client.hosting.models.secret import Secret
from agentverse_client.hosting.models.secret_create import SecretCreate
from agentverse_client.hosting.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.hosting.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with agentverse_client.hosting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.hosting.HostingApi(api_client)
    secret_create = agentverse_client.hosting.SecretCreate() # SecretCreate | 
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Create User Secret
        api_response = api_instance.create_user_agent_secret(secret_create, no_cache=no_cache)
        print("The response of HostingApi->create_user_agent_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingApi->create_user_agent_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_create** | [**SecretCreate**](SecretCreate.md)|  | 
 **no_cache** | **bool**|  | [optional] [default to False]

### Return type

[**Secret**](Secret.md)

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

# **delete_all_team_data**
> object delete_all_team_data(slug, no_cache=no_cache)

Delete All Team Data

Deletes all agents, achievements etc. for a team

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.hosting
from agentverse_client.hosting.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.hosting.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with agentverse_client.hosting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.hosting.HostingApi(api_client)
    slug = 'slug_example' # str | 
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Delete All Team Data
        api_response = api_instance.delete_all_team_data(slug, no_cache=no_cache)
        print("The response of HostingApi->delete_all_team_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingApi->delete_all_team_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **no_cache** | **bool**|  | [optional] [default to False]

### Return type

**object**

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

# **delete_all_user_data**
> object delete_all_user_data(no_cache=no_cache)

Delete All User Data

Deletes all agents, achievements etc. for a user

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.hosting
from agentverse_client.hosting.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.hosting.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with agentverse_client.hosting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.hosting.HostingApi(api_client)
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Delete All User Data
        api_response = api_instance.delete_all_user_data(no_cache=no_cache)
        print("The response of HostingApi->delete_all_user_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingApi->delete_all_user_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **no_cache** | **bool**|  | [optional] [default to False]

### Return type

**object**

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

# **delete_logs_for_team_agent**
> object delete_logs_for_team_agent(slug, address, no_cache=no_cache)

Delete Logs For Team Agent

Deletes all the logs for a specific agent, identified by address

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.hosting
from agentverse_client.hosting.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.hosting.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with agentverse_client.hosting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.hosting.HostingApi(api_client)
    slug = 'slug_example' # str | 
    address = 'address_example' # str | 
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Delete Logs For Team Agent
        api_response = api_instance.delete_logs_for_team_agent(slug, address, no_cache=no_cache)
        print("The response of HostingApi->delete_logs_for_team_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingApi->delete_logs_for_team_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **address** | **str**|  | 
 **no_cache** | **bool**|  | [optional] [default to False]

### Return type

**object**

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

# **delete_logs_for_user_agent**
> object delete_logs_for_user_agent(address, no_cache=no_cache)

Delete Logs For User Agent

Deletes all the logs for a specific agent, identified by address

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.hosting
from agentverse_client.hosting.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.hosting.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with agentverse_client.hosting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.hosting.HostingApi(api_client)
    address = 'address_example' # str | 
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Delete Logs For User Agent
        api_response = api_instance.delete_logs_for_user_agent(address, no_cache=no_cache)
        print("The response of HostingApi->delete_logs_for_user_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingApi->delete_logs_for_user_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**|  | 
 **no_cache** | **bool**|  | [optional] [default to False]

### Return type

**object**

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

# **delete_team_agent**
> object delete_team_agent(slug, address, no_cache=no_cache)

Delete Specific Team Agent

Deletes a specific agent, by address from the platform

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.hosting
from agentverse_client.hosting.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.hosting.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with agentverse_client.hosting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.hosting.HostingApi(api_client)
    slug = 'slug_example' # str | 
    address = 'address_example' # str | 
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Delete Specific Team Agent
        api_response = api_instance.delete_team_agent(slug, address, no_cache=no_cache)
        print("The response of HostingApi->delete_team_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingApi->delete_team_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **address** | **str**|  | 
 **no_cache** | **bool**|  | [optional] [default to False]

### Return type

**object**

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

# **delete_team_agent_storage**
> object delete_team_agent_storage(slug, address, key, no_cache=no_cache)

Delete Team Agent Storage

Updates the storage for a specific agent, identified by address

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.hosting
from agentverse_client.hosting.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.hosting.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with agentverse_client.hosting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.hosting.HostingApi(api_client)
    slug = 'slug_example' # str | 
    address = 'address_example' # str | 
    key = 'key_example' # str | 
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Delete Team Agent Storage
        api_response = api_instance.delete_team_agent_storage(slug, address, key, no_cache=no_cache)
        print("The response of HostingApi->delete_team_agent_storage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingApi->delete_team_agent_storage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **address** | **str**|  | 
 **key** | **str**|  | 
 **no_cache** | **bool**|  | [optional] [default to False]

### Return type

**object**

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

# **delete_team_secret**
> object delete_team_secret(slug, address, name, no_cache=no_cache)

Delete User Secret

Deletes a secret for the given address and name.

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.hosting
from agentverse_client.hosting.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.hosting.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with agentverse_client.hosting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.hosting.HostingApi(api_client)
    slug = 'slug_example' # str | 
    address = 'address_example' # str | 
    name = 'name_example' # str | 
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Delete User Secret
        api_response = api_instance.delete_team_secret(slug, address, name, no_cache=no_cache)
        print("The response of HostingApi->delete_team_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingApi->delete_team_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **address** | **str**|  | 
 **name** | **str**|  | 
 **no_cache** | **bool**|  | [optional] [default to False]

### Return type

**object**

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

# **delete_user_agent**
> object delete_user_agent(address, no_cache=no_cache)

Delete Specific User Agent

Deletes a specific agent, by address from the platform

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.hosting
from agentverse_client.hosting.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.hosting.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with agentverse_client.hosting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.hosting.HostingApi(api_client)
    address = 'address_example' # str | 
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Delete Specific User Agent
        api_response = api_instance.delete_user_agent(address, no_cache=no_cache)
        print("The response of HostingApi->delete_user_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingApi->delete_user_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**|  | 
 **no_cache** | **bool**|  | [optional] [default to False]

### Return type

**object**

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

# **delete_user_agent_storage**
> object delete_user_agent_storage(address, key, no_cache=no_cache)

Delete User Agent Storage

Updates the storage for a specific agent, identified by address

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.hosting
from agentverse_client.hosting.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.hosting.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with agentverse_client.hosting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.hosting.HostingApi(api_client)
    address = 'address_example' # str | 
    key = 'key_example' # str | 
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Delete User Agent Storage
        api_response = api_instance.delete_user_agent_storage(address, key, no_cache=no_cache)
        print("The response of HostingApi->delete_user_agent_storage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingApi->delete_user_agent_storage: %s\n" % e)
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

# **delete_user_secret**
> object delete_user_secret(address, name, no_cache=no_cache)

Delete User Secret

Deletes a secret for the given address and name.

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.hosting
from agentverse_client.hosting.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.hosting.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with agentverse_client.hosting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.hosting.HostingApi(api_client)
    address = 'address_example' # str | 
    name = 'name_example' # str | 
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Delete User Secret
        api_response = api_instance.delete_user_secret(address, name, no_cache=no_cache)
        print("The response of HostingApi->delete_user_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingApi->delete_user_secret: %s\n" % e)
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

# **duplicate_team_agent**
> Agent duplicate_team_agent(slug, address, new_agent, no_cache=no_cache)

Duplicate Specific Team Agent

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.hosting
from agentverse_client.hosting.models.agent import Agent
from agentverse_client.hosting.models.new_agent import NewAgent
from agentverse_client.hosting.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.hosting.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with agentverse_client.hosting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.hosting.HostingApi(api_client)
    slug = 'slug_example' # str | 
    address = 'address_example' # str | 
    new_agent = agentverse_client.hosting.NewAgent() # NewAgent | 
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Duplicate Specific Team Agent
        api_response = api_instance.duplicate_team_agent(slug, address, new_agent, no_cache=no_cache)
        print("The response of HostingApi->duplicate_team_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingApi->duplicate_team_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **address** | **str**|  | 
 **new_agent** | [**NewAgent**](NewAgent.md)|  | 
 **no_cache** | **bool**|  | [optional] [default to False]

### Return type

[**Agent**](Agent.md)

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

# **duplicate_user_agent**
> Agent duplicate_user_agent(address, new_agent, no_cache=no_cache)

Duplicate Specific User Agent

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.hosting
from agentverse_client.hosting.models.agent import Agent
from agentverse_client.hosting.models.new_agent import NewAgent
from agentverse_client.hosting.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.hosting.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with agentverse_client.hosting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.hosting.HostingApi(api_client)
    address = 'address_example' # str | 
    new_agent = agentverse_client.hosting.NewAgent() # NewAgent | 
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Duplicate Specific User Agent
        api_response = api_instance.duplicate_user_agent(address, new_agent, no_cache=no_cache)
        print("The response of HostingApi->duplicate_user_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingApi->duplicate_user_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**|  | 
 **new_agent** | [**NewAgent**](NewAgent.md)|  | 
 **no_cache** | **bool**|  | [optional] [default to False]

### Return type

[**Agent**](Agent.md)

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

# **get_latest_logs_for_team_agent**
> List[AgentLog] get_latest_logs_for_team_agent(slug, address, no_cache=no_cache)

Get Latest Logs For Team Agent

Gets the latest logs for a specific agent, identified by address

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.hosting
from agentverse_client.hosting.models.agent_log import AgentLog
from agentverse_client.hosting.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.hosting.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with agentverse_client.hosting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.hosting.HostingApi(api_client)
    slug = 'slug_example' # str | 
    address = 'address_example' # str | 
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Get Latest Logs For Team Agent
        api_response = api_instance.get_latest_logs_for_team_agent(slug, address, no_cache=no_cache)
        print("The response of HostingApi->get_latest_logs_for_team_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingApi->get_latest_logs_for_team_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **address** | **str**|  | 
 **no_cache** | **bool**|  | [optional] [default to False]

### Return type

[**List[AgentLog]**](AgentLog.md)

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

# **get_latest_logs_for_user_agent**
> List[AgentLog] get_latest_logs_for_user_agent(address, no_cache=no_cache)

Get Latest Logs For User Agent

Gets the latest logs for a specific agent, identified by address

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.hosting
from agentverse_client.hosting.models.agent_log import AgentLog
from agentverse_client.hosting.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.hosting.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with agentverse_client.hosting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.hosting.HostingApi(api_client)
    address = 'address_example' # str | 
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Get Latest Logs For User Agent
        api_response = api_instance.get_latest_logs_for_user_agent(address, no_cache=no_cache)
        print("The response of HostingApi->get_latest_logs_for_user_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingApi->get_latest_logs_for_user_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**|  | 
 **no_cache** | **bool**|  | [optional] [default to False]

### Return type

[**List[AgentLog]**](AgentLog.md)

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

# **get_new_achievements**
> List[str] get_new_achievements(no_cache=no_cache)

Get New Achievements

Stores and returns new achievement ids to the user.

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.hosting
from agentverse_client.hosting.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.hosting.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with agentverse_client.hosting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.hosting.HostingApi(api_client)
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Get New Achievements
        api_response = api_instance.get_new_achievements(no_cache=no_cache)
        print("The response of HostingApi->get_new_achievements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingApi->get_new_achievements: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **no_cache** | **bool**|  | [optional] [default to False]

### Return type

**List[str]**

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

# **get_supported_packages**
> Packages get_supported_packages(x_api_version=x_api_version)

Get Supported Packages

Returns a list of supported packages and their versions for agents.

### Example


```python
import agentverse_client.hosting
from agentverse_client.hosting.models.packages import Packages
from agentverse_client.hosting.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.hosting.Configuration(
    host = "https://agentverse.ai"
)


# Enter a context with an instance of the API client
with agentverse_client.hosting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.hosting.HostingApi(api_client)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get Supported Packages
        api_response = api_instance.get_supported_packages(x_api_version=x_api_version)
        print("The response of HostingApi->get_supported_packages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingApi->get_supported_packages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**|  | [optional] 

### Return type

[**Packages**](Packages.md)

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

# **get_team_agent_code**
> AgentCode get_team_agent_code(slug, address, no_cache=no_cache)

Get Team Agent Code

Gets the current code for an agent, specified by address

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.hosting
from agentverse_client.hosting.models.agent_code import AgentCode
from agentverse_client.hosting.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.hosting.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with agentverse_client.hosting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.hosting.HostingApi(api_client)
    slug = 'slug_example' # str | 
    address = 'address_example' # str | 
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Get Team Agent Code
        api_response = api_instance.get_team_agent_code(slug, address, no_cache=no_cache)
        print("The response of HostingApi->get_team_agent_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingApi->get_team_agent_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **address** | **str**|  | 
 **no_cache** | **bool**|  | [optional] [default to False]

### Return type

[**AgentCode**](AgentCode.md)

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

# **get_team_agent_details**
> Agent get_team_agent_details(slug, address, no_cache=no_cache)

Get Specific Teams Agent

Looks up a specific agent by address on the hosting platform

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.hosting
from agentverse_client.hosting.models.agent import Agent
from agentverse_client.hosting.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.hosting.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with agentverse_client.hosting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.hosting.HostingApi(api_client)
    slug = 'slug_example' # str | 
    address = 'address_example' # str | 
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Get Specific Teams Agent
        api_response = api_instance.get_team_agent_details(slug, address, no_cache=no_cache)
        print("The response of HostingApi->get_team_agent_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingApi->get_team_agent_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **address** | **str**|  | 
 **no_cache** | **bool**|  | [optional] [default to False]

### Return type

[**Agent**](Agent.md)

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

# **get_team_agent_interactions**
> HistoricalInteractions get_team_agent_interactions(slug, address, period=period, no_cache=no_cache)

Get Agent Team Interactions

### Example


```python
import agentverse_client.hosting
from agentverse_client.hosting.models.historical_interactions import HistoricalInteractions
from agentverse_client.hosting.models.interaction_period import InteractionPeriod
from agentverse_client.hosting.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.hosting.Configuration(
    host = "https://agentverse.ai"
)


# Enter a context with an instance of the API client
with agentverse_client.hosting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.hosting.HostingApi(api_client)
    slug = 'slug_example' # str | 
    address = 'address_example' # str | 
    period = agentverse_client.hosting.InteractionPeriod() # InteractionPeriod |  (optional)
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Get Agent Team Interactions
        api_response = api_instance.get_team_agent_interactions(slug, address, period=period, no_cache=no_cache)
        print("The response of HostingApi->get_team_agent_interactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingApi->get_team_agent_interactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **address** | **str**|  | 
 **period** | [**InteractionPeriod**](.md)|  | [optional] 
 **no_cache** | **bool**|  | [optional] [default to False]

### Return type

[**HistoricalInteractions**](HistoricalInteractions.md)

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

# **get_team_agent_metadata**
> AgentMetadata get_team_agent_metadata(slug, address, no_cache=no_cache, x_api_version=x_api_version)

Get Team Agent Metadata

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.hosting
from agentverse_client.hosting.models.agent_metadata import AgentMetadata
from agentverse_client.hosting.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.hosting.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with agentverse_client.hosting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.hosting.HostingApi(api_client)
    slug = 'slug_example' # str | 
    address = 'address_example' # str | 
    no_cache = False # bool |  (optional) (default to False)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get Team Agent Metadata
        api_response = api_instance.get_team_agent_metadata(slug, address, no_cache=no_cache, x_api_version=x_api_version)
        print("The response of HostingApi->get_team_agent_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingApi->get_team_agent_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **address** | **str**|  | 
 **no_cache** | **bool**|  | [optional] [default to False]
 **x_api_version** | **str**|  | [optional] 

### Return type

[**AgentMetadata**](AgentMetadata.md)

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

# **get_team_agent_profile**
> PublicAgent get_team_agent_profile(slug, address, no_cache=no_cache)

Get Team Agent Public Profile

### Example


```python
import agentverse_client.hosting
from agentverse_client.hosting.models.public_agent import PublicAgent
from agentverse_client.hosting.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.hosting.Configuration(
    host = "https://agentverse.ai"
)


# Enter a context with an instance of the API client
with agentverse_client.hosting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.hosting.HostingApi(api_client)
    slug = 'slug_example' # str | 
    address = 'address_example' # str | 
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Get Team Agent Public Profile
        api_response = api_instance.get_team_agent_profile(slug, address, no_cache=no_cache)
        print("The response of HostingApi->get_team_agent_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingApi->get_team_agent_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **address** | **str**|  | 
 **no_cache** | **bool**|  | [optional] [default to False]

### Return type

[**PublicAgent**](PublicAgent.md)

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

# **get_team_agent_secrets**
> SecretList get_team_agent_secrets(slug, address, no_cache=no_cache)

Get Team Agent Secrets

Returns all secrets for the given agent address.

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.hosting
from agentverse_client.hosting.models.secret_list import SecretList
from agentverse_client.hosting.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.hosting.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with agentverse_client.hosting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.hosting.HostingApi(api_client)
    slug = 'slug_example' # str | 
    address = 'address_example' # str | 
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Get Team Agent Secrets
        api_response = api_instance.get_team_agent_secrets(slug, address, no_cache=no_cache)
        print("The response of HostingApi->get_team_agent_secrets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingApi->get_team_agent_secrets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **address** | **str**|  | 
 **no_cache** | **bool**|  | [optional] [default to False]

### Return type

[**SecretList**](SecretList.md)

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

# **get_team_agent_storage**
> WithPaginationStorageItem get_team_agent_storage(slug, address, cursor=cursor, no_cache=no_cache)

Get Team Agent Storage

Gets the storage for an agent, specified by address

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.hosting
from agentverse_client.hosting.models.with_pagination_storage_item import WithPaginationStorageItem
from agentverse_client.hosting.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.hosting.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with agentverse_client.hosting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.hosting.HostingApi(api_client)
    slug = 'slug_example' # str | 
    address = 'address_example' # str | 
    cursor = 'cursor_example' # str |  (optional)
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Get Team Agent Storage
        api_response = api_instance.get_team_agent_storage(slug, address, cursor=cursor, no_cache=no_cache)
        print("The response of HostingApi->get_team_agent_storage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingApi->get_team_agent_storage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **address** | **str**|  | 
 **cursor** | **str**|  | [optional] 
 **no_cache** | **bool**|  | [optional] [default to False]

### Return type

[**WithPaginationStorageItem**](WithPaginationStorageItem.md)

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

# **get_team_agent_storage_by_key**
> StorageItem get_team_agent_storage_by_key(slug, address, key, no_cache=no_cache)

Get Team Agent Storage By Key

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.hosting
from agentverse_client.hosting.models.storage_item import StorageItem
from agentverse_client.hosting.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.hosting.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with agentverse_client.hosting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.hosting.HostingApi(api_client)
    slug = 'slug_example' # str | 
    address = 'address_example' # str | 
    key = 'key_example' # str | 
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Get Team Agent Storage By Key
        api_response = api_instance.get_team_agent_storage_by_key(slug, address, key, no_cache=no_cache)
        print("The response of HostingApi->get_team_agent_storage_by_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingApi->get_team_agent_storage_by_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **address** | **str**|  | 
 **key** | **str**|  | 
 **no_cache** | **bool**|  | [optional] [default to False]

### Return type

[**StorageItem**](StorageItem.md)

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

# **get_unlocked_achievements**
> List[str] get_unlocked_achievements(no_cache=no_cache)

Get Unlocked Achievements

Returns already unlocked achievement ids to the user.

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.hosting
from agentverse_client.hosting.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.hosting.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with agentverse_client.hosting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.hosting.HostingApi(api_client)
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Get Unlocked Achievements
        api_response = api_instance.get_unlocked_achievements(no_cache=no_cache)
        print("The response of HostingApi->get_unlocked_achievements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingApi->get_unlocked_achievements: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **no_cache** | **bool**|  | [optional] [default to False]

### Return type

**List[str]**

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

# **get_user_agent_code**
> AgentCode get_user_agent_code(address, no_cache=no_cache)

Get User Agent Code

Gets the current code for an agent, specified by address

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.hosting
from agentverse_client.hosting.models.agent_code import AgentCode
from agentverse_client.hosting.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.hosting.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with agentverse_client.hosting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.hosting.HostingApi(api_client)
    address = 'address_example' # str | 
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Get User Agent Code
        api_response = api_instance.get_user_agent_code(address, no_cache=no_cache)
        print("The response of HostingApi->get_user_agent_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingApi->get_user_agent_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**|  | 
 **no_cache** | **bool**|  | [optional] [default to False]

### Return type

[**AgentCode**](AgentCode.md)

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

# **get_user_agent_details**
> Agent get_user_agent_details(address, no_cache=no_cache)

Get Specific User Agent

Looks up a specific agent by address on the hosting platform

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.hosting
from agentverse_client.hosting.models.agent import Agent
from agentverse_client.hosting.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.hosting.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with agentverse_client.hosting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.hosting.HostingApi(api_client)
    address = 'address_example' # str | 
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Get Specific User Agent
        api_response = api_instance.get_user_agent_details(address, no_cache=no_cache)
        print("The response of HostingApi->get_user_agent_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingApi->get_user_agent_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**|  | 
 **no_cache** | **bool**|  | [optional] [default to False]

### Return type

[**Agent**](Agent.md)

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

# **get_user_agent_interactions**
> HistoricalInteractions get_user_agent_interactions(address, period=period, no_cache=no_cache)

Get Agent User Interactions

### Example


```python
import agentverse_client.hosting
from agentverse_client.hosting.models.historical_interactions import HistoricalInteractions
from agentverse_client.hosting.models.interaction_period import InteractionPeriod
from agentverse_client.hosting.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.hosting.Configuration(
    host = "https://agentverse.ai"
)


# Enter a context with an instance of the API client
with agentverse_client.hosting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.hosting.HostingApi(api_client)
    address = 'address_example' # str | 
    period = agentverse_client.hosting.InteractionPeriod() # InteractionPeriod |  (optional)
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Get Agent User Interactions
        api_response = api_instance.get_user_agent_interactions(address, period=period, no_cache=no_cache)
        print("The response of HostingApi->get_user_agent_interactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingApi->get_user_agent_interactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**|  | 
 **period** | [**InteractionPeriod**](.md)|  | [optional] 
 **no_cache** | **bool**|  | [optional] [default to False]

### Return type

[**HistoricalInteractions**](HistoricalInteractions.md)

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

# **get_user_agent_metadata**
> AgentMetadata get_user_agent_metadata(address, no_cache=no_cache, x_api_version=x_api_version)

Get User Agent Metadata

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.hosting
from agentverse_client.hosting.models.agent_metadata import AgentMetadata
from agentverse_client.hosting.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.hosting.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with agentverse_client.hosting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.hosting.HostingApi(api_client)
    address = 'address_example' # str | 
    no_cache = False # bool |  (optional) (default to False)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Get User Agent Metadata
        api_response = api_instance.get_user_agent_metadata(address, no_cache=no_cache, x_api_version=x_api_version)
        print("The response of HostingApi->get_user_agent_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingApi->get_user_agent_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**|  | 
 **no_cache** | **bool**|  | [optional] [default to False]
 **x_api_version** | **str**|  | [optional] 

### Return type

[**AgentMetadata**](AgentMetadata.md)

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

# **get_user_agent_profile**
> PublicAgent get_user_agent_profile(address, no_cache=no_cache)

Get User Agent Public Profile

### Example


```python
import agentverse_client.hosting
from agentverse_client.hosting.models.public_agent import PublicAgent
from agentverse_client.hosting.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.hosting.Configuration(
    host = "https://agentverse.ai"
)


# Enter a context with an instance of the API client
with agentverse_client.hosting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.hosting.HostingApi(api_client)
    address = 'address_example' # str | 
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Get User Agent Public Profile
        api_response = api_instance.get_user_agent_profile(address, no_cache=no_cache)
        print("The response of HostingApi->get_user_agent_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingApi->get_user_agent_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**|  | 
 **no_cache** | **bool**|  | [optional] [default to False]

### Return type

[**PublicAgent**](PublicAgent.md)

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

# **get_user_agent_secrets**
> SecretList get_user_agent_secrets(address, no_cache=no_cache)

Get User Agent Secrets

Returns all secrets for the given agent address.

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.hosting
from agentverse_client.hosting.models.secret_list import SecretList
from agentverse_client.hosting.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.hosting.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with agentverse_client.hosting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.hosting.HostingApi(api_client)
    address = 'address_example' # str | 
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Get User Agent Secrets
        api_response = api_instance.get_user_agent_secrets(address, no_cache=no_cache)
        print("The response of HostingApi->get_user_agent_secrets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingApi->get_user_agent_secrets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**|  | 
 **no_cache** | **bool**|  | [optional] [default to False]

### Return type

[**SecretList**](SecretList.md)

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

# **get_user_agent_storage**
> WithPaginationStorageItem get_user_agent_storage(address, cursor=cursor, no_cache=no_cache)

Get User Agent Storage

Gets the storage for an agent, specified by address

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.hosting
from agentverse_client.hosting.models.with_pagination_storage_item import WithPaginationStorageItem
from agentverse_client.hosting.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.hosting.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with agentverse_client.hosting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.hosting.HostingApi(api_client)
    address = 'address_example' # str | 
    cursor = 'cursor_example' # str |  (optional)
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Get User Agent Storage
        api_response = api_instance.get_user_agent_storage(address, cursor=cursor, no_cache=no_cache)
        print("The response of HostingApi->get_user_agent_storage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingApi->get_user_agent_storage: %s\n" % e)
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

# **get_user_agent_storage_by_key**
> StorageItem get_user_agent_storage_by_key(address, key, no_cache=no_cache)

Get User Agent Storage By Key

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.hosting
from agentverse_client.hosting.models.storage_item import StorageItem
from agentverse_client.hosting.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.hosting.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with agentverse_client.hosting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.hosting.HostingApi(api_client)
    address = 'address_example' # str | 
    key = 'key_example' # str | 
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Get User Agent Storage By Key
        api_response = api_instance.get_user_agent_storage_by_key(address, key, no_cache=no_cache)
        print("The response of HostingApi->get_user_agent_storage_by_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingApi->get_user_agent_storage_by_key: %s\n" % e)
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

# **get_user_secret**
> SecretList get_user_secret(slug, no_cache=no_cache)

Get User Secret

Returns all secrets for the given team.

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.hosting
from agentverse_client.hosting.models.secret_list import SecretList
from agentverse_client.hosting.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.hosting.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with agentverse_client.hosting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.hosting.HostingApi(api_client)
    slug = 'slug_example' # str | 
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Get User Secret
        api_response = api_instance.get_user_secret(slug, no_cache=no_cache)
        print("The response of HostingApi->get_user_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingApi->get_user_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **no_cache** | **bool**|  | [optional] [default to False]

### Return type

[**SecretList**](SecretList.md)

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

# **get_user_secrets**
> SecretList get_user_secrets(no_cache=no_cache)

Get User Secret

Returns all secrets for the given user.

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.hosting
from agentverse_client.hosting.models.secret_list import SecretList
from agentverse_client.hosting.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.hosting.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with agentverse_client.hosting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.hosting.HostingApi(api_client)
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Get User Secret
        api_response = api_instance.get_user_secrets(no_cache=no_cache)
        print("The response of HostingApi->get_user_secrets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingApi->get_user_secrets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **no_cache** | **bool**|  | [optional] [default to False]

### Return type

[**SecretList**](SecretList.md)

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

# **list_team_agents**
> WithPaginationAgentSummary list_team_agents(slug, cursor=cursor, name=name, no_cache=no_cache, sort_by=sort_by, direction=direction)

Get Team Agents

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.hosting
from agentverse_client.hosting.models.with_pagination_agent_summary import WithPaginationAgentSummary
from agentverse_client.hosting.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.hosting.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with agentverse_client.hosting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.hosting.HostingApi(api_client)
    slug = 'slug_example' # str | 
    cursor = 'cursor_example' # str |  (optional)
    name = 'name_example' # str |  (optional)
    no_cache = False # bool |  (optional) (default to False)
    sort_by = 'sort_by_example' # str |  (optional)
    direction = 'asc' # str |  (optional) (default to 'asc')

    try:
        # Get Team Agents
        api_response = api_instance.list_team_agents(slug, cursor=cursor, name=name, no_cache=no_cache, sort_by=sort_by, direction=direction)
        print("The response of HostingApi->list_team_agents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingApi->list_team_agents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **cursor** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **no_cache** | **bool**|  | [optional] [default to False]
 **sort_by** | **str**|  | [optional] 
 **direction** | **str**|  | [optional] [default to &#39;asc&#39;]

### Return type

[**WithPaginationAgentSummary**](WithPaginationAgentSummary.md)

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

# **list_user_agents**
> WithPaginationAgentSummary list_user_agents(cursor=cursor, name=name, no_cache=no_cache, sort_by=sort_by, direction=direction)

Get User Agents

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.hosting
from agentverse_client.hosting.models.with_pagination_agent_summary import WithPaginationAgentSummary
from agentverse_client.hosting.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.hosting.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with agentverse_client.hosting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.hosting.HostingApi(api_client)
    cursor = 'cursor_example' # str |  (optional)
    name = 'name_example' # str |  (optional)
    no_cache = False # bool |  (optional) (default to False)
    sort_by = 'sort_by_example' # str |  (optional)
    direction = 'asc' # str |  (optional) (default to 'asc')

    try:
        # Get User Agents
        api_response = api_instance.list_user_agents(cursor=cursor, name=name, no_cache=no_cache, sort_by=sort_by, direction=direction)
        print("The response of HostingApi->list_user_agents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingApi->list_user_agents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **no_cache** | **bool**|  | [optional] [default to False]
 **sort_by** | **str**|  | [optional] 
 **direction** | **str**|  | [optional] [default to &#39;asc&#39;]

### Return type

[**WithPaginationAgentSummary**](WithPaginationAgentSummary.md)

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

# **register_new_team_domain_name**
> object register_new_team_domain_name(slug, address, new_domain_name, no_cache=no_cache)

Register New Team Domain Name

Register agent name on name service contract

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.hosting
from agentverse_client.hosting.models.new_domain_name import NewDomainName
from agentverse_client.hosting.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.hosting.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with agentverse_client.hosting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.hosting.HostingApi(api_client)
    slug = 'slug_example' # str | 
    address = 'address_example' # str | 
    new_domain_name = agentverse_client.hosting.NewDomainName() # NewDomainName | 
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Register New Team Domain Name
        api_response = api_instance.register_new_team_domain_name(slug, address, new_domain_name, no_cache=no_cache)
        print("The response of HostingApi->register_new_team_domain_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingApi->register_new_team_domain_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **address** | **str**|  | 
 **new_domain_name** | [**NewDomainName**](NewDomainName.md)|  | 
 **no_cache** | **bool**|  | [optional] [default to False]

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

# **register_new_user_domain_name**
> object register_new_user_domain_name(address, new_domain_name, no_cache=no_cache)

Register New User Domain Name

Register agent name on name service contract

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.hosting
from agentverse_client.hosting.models.new_domain_name import NewDomainName
from agentverse_client.hosting.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.hosting.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with agentverse_client.hosting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.hosting.HostingApi(api_client)
    address = 'address_example' # str | 
    new_domain_name = agentverse_client.hosting.NewDomainName() # NewDomainName | 
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Register New User Domain Name
        api_response = api_instance.register_new_user_domain_name(address, new_domain_name, no_cache=no_cache)
        print("The response of HostingApi->register_new_user_domain_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingApi->register_new_user_domain_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**|  | 
 **new_domain_name** | [**NewDomainName**](NewDomainName.md)|  | 
 **no_cache** | **bool**|  | [optional] [default to False]

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

# **start_specific_team_agent**
> Agent start_specific_team_agent(slug, address, no_cache=no_cache)

Start Specific Team Agent

Starts a specific agent, identified by address

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.hosting
from agentverse_client.hosting.models.agent import Agent
from agentverse_client.hosting.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.hosting.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with agentverse_client.hosting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.hosting.HostingApi(api_client)
    slug = 'slug_example' # str | 
    address = 'address_example' # str | 
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Start Specific Team Agent
        api_response = api_instance.start_specific_team_agent(slug, address, no_cache=no_cache)
        print("The response of HostingApi->start_specific_team_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingApi->start_specific_team_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **address** | **str**|  | 
 **no_cache** | **bool**|  | [optional] [default to False]

### Return type

[**Agent**](Agent.md)

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

# **start_specific_user_agent**
> Agent start_specific_user_agent(address, no_cache=no_cache)

Start Specific User Agent

Starts a specific agent, identified by address

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.hosting
from agentverse_client.hosting.models.agent import Agent
from agentverse_client.hosting.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.hosting.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with agentverse_client.hosting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.hosting.HostingApi(api_client)
    address = 'address_example' # str | 
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Start Specific User Agent
        api_response = api_instance.start_specific_user_agent(address, no_cache=no_cache)
        print("The response of HostingApi->start_specific_user_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingApi->start_specific_user_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**|  | 
 **no_cache** | **bool**|  | [optional] [default to False]

### Return type

[**Agent**](Agent.md)

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

# **stop_specific_team_agent**
> Agent stop_specific_team_agent(slug, address, no_cache=no_cache)

Stop Specific Team Agent

Stops a specific agent, identified by address

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.hosting
from agentverse_client.hosting.models.agent import Agent
from agentverse_client.hosting.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.hosting.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with agentverse_client.hosting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.hosting.HostingApi(api_client)
    slug = 'slug_example' # str | 
    address = 'address_example' # str | 
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Stop Specific Team Agent
        api_response = api_instance.stop_specific_team_agent(slug, address, no_cache=no_cache)
        print("The response of HostingApi->stop_specific_team_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingApi->stop_specific_team_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **address** | **str**|  | 
 **no_cache** | **bool**|  | [optional] [default to False]

### Return type

[**Agent**](Agent.md)

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

# **stop_specific_user_agent**
> Agent stop_specific_user_agent(address, no_cache=no_cache)

Stop Specific User Agent

Stops a specific agent, identified by address

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.hosting
from agentverse_client.hosting.models.agent import Agent
from agentverse_client.hosting.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.hosting.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with agentverse_client.hosting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.hosting.HostingApi(api_client)
    address = 'address_example' # str | 
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Stop Specific User Agent
        api_response = api_instance.stop_specific_user_agent(address, no_cache=no_cache)
        print("The response of HostingApi->stop_specific_user_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingApi->stop_specific_user_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**|  | 
 **no_cache** | **bool**|  | [optional] [default to False]

### Return type

[**Agent**](Agent.md)

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

# **update_team_agent**
> object update_team_agent(slug, address, update_agent, no_cache=no_cache)

Update Specific Team Agent

Updates a specific agent, by address from the platform

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.hosting
from agentverse_client.hosting.models.update_agent import UpdateAgent
from agentverse_client.hosting.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.hosting.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with agentverse_client.hosting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.hosting.HostingApi(api_client)
    slug = 'slug_example' # str | 
    address = 'address_example' # str | 
    update_agent = agentverse_client.hosting.UpdateAgent() # UpdateAgent | 
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Update Specific Team Agent
        api_response = api_instance.update_team_agent(slug, address, update_agent, no_cache=no_cache)
        print("The response of HostingApi->update_team_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingApi->update_team_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **address** | **str**|  | 
 **update_agent** | [**UpdateAgent**](UpdateAgent.md)|  | 
 **no_cache** | **bool**|  | [optional] [default to False]

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

# **update_team_agent_code**
> AgentCodeDigest update_team_agent_code(slug, address, update_agent_code, no_cache=no_cache)

Update Team Agent Code

Updates the code for a specific agent, identified by address

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.hosting
from agentverse_client.hosting.models.agent_code_digest import AgentCodeDigest
from agentverse_client.hosting.models.update_agent_code import UpdateAgentCode
from agentverse_client.hosting.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.hosting.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with agentverse_client.hosting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.hosting.HostingApi(api_client)
    slug = 'slug_example' # str | 
    address = 'address_example' # str | 
    update_agent_code = agentverse_client.hosting.UpdateAgentCode() # UpdateAgentCode | 
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Update Team Agent Code
        api_response = api_instance.update_team_agent_code(slug, address, update_agent_code, no_cache=no_cache)
        print("The response of HostingApi->update_team_agent_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingApi->update_team_agent_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **address** | **str**|  | 
 **update_agent_code** | [**UpdateAgentCode**](UpdateAgentCode.md)|  | 
 **no_cache** | **bool**|  | [optional] [default to False]

### Return type

[**AgentCodeDigest**](AgentCodeDigest.md)

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

# **update_team_agent_metadata**
> AgentMetadata update_team_agent_metadata(slug, address, agent_metadata_updates, no_cache=no_cache, x_api_version=x_api_version)

Update Team Agent Metadata

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.hosting
from agentverse_client.hosting.models.agent_metadata import AgentMetadata
from agentverse_client.hosting.models.agent_metadata_updates import AgentMetadataUpdates
from agentverse_client.hosting.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.hosting.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with agentverse_client.hosting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.hosting.HostingApi(api_client)
    slug = 'slug_example' # str | 
    address = 'address_example' # str | 
    agent_metadata_updates = agentverse_client.hosting.AgentMetadataUpdates() # AgentMetadataUpdates | 
    no_cache = False # bool |  (optional) (default to False)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Update Team Agent Metadata
        api_response = api_instance.update_team_agent_metadata(slug, address, agent_metadata_updates, no_cache=no_cache, x_api_version=x_api_version)
        print("The response of HostingApi->update_team_agent_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingApi->update_team_agent_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **address** | **str**|  | 
 **agent_metadata_updates** | [**AgentMetadataUpdates**](AgentMetadataUpdates.md)|  | 
 **no_cache** | **bool**|  | [optional] [default to False]
 **x_api_version** | **str**|  | [optional] 

### Return type

[**AgentMetadata**](AgentMetadata.md)

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

# **update_team_agent_network**
> object update_team_agent_network(slug, address, update_agent_network, no_cache=no_cache)

Update Team Agent Network

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.hosting
from agentverse_client.hosting.models.update_agent_network import UpdateAgentNetwork
from agentverse_client.hosting.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.hosting.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with agentverse_client.hosting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.hosting.HostingApi(api_client)
    slug = 'slug_example' # str | 
    address = 'address_example' # str | 
    update_agent_network = agentverse_client.hosting.UpdateAgentNetwork() # UpdateAgentNetwork | 
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Update Team Agent Network
        api_response = api_instance.update_team_agent_network(slug, address, update_agent_network, no_cache=no_cache)
        print("The response of HostingApi->update_team_agent_network:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingApi->update_team_agent_network: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **address** | **str**|  | 
 **update_agent_network** | [**UpdateAgentNetwork**](UpdateAgentNetwork.md)|  | 
 **no_cache** | **bool**|  | [optional] [default to False]

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

# **update_team_agent_storage**
> object update_team_agent_storage(slug, address, key, storage_item_update, no_cache=no_cache)

Update Team Agent Storage

Updates the storage for a specific agent, identified by address

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.hosting
from agentverse_client.hosting.models.storage_item_update import StorageItemUpdate
from agentverse_client.hosting.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.hosting.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with agentverse_client.hosting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.hosting.HostingApi(api_client)
    slug = 'slug_example' # str | 
    address = 'address_example' # str | 
    key = 'key_example' # str | 
    storage_item_update = agentverse_client.hosting.StorageItemUpdate() # StorageItemUpdate | 
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Update Team Agent Storage
        api_response = api_instance.update_team_agent_storage(slug, address, key, storage_item_update, no_cache=no_cache)
        print("The response of HostingApi->update_team_agent_storage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingApi->update_team_agent_storage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **address** | **str**|  | 
 **key** | **str**|  | 
 **storage_item_update** | [**StorageItemUpdate**](StorageItemUpdate.md)|  | 
 **no_cache** | **bool**|  | [optional] [default to False]

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

# **update_user_agent**
> object update_user_agent(address, update_agent, no_cache=no_cache)

Update Specific User Agent

Updates a specific agent, by address from the platform

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.hosting
from agentverse_client.hosting.models.update_agent import UpdateAgent
from agentverse_client.hosting.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.hosting.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with agentverse_client.hosting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.hosting.HostingApi(api_client)
    address = 'address_example' # str | 
    update_agent = agentverse_client.hosting.UpdateAgent() # UpdateAgent | 
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Update Specific User Agent
        api_response = api_instance.update_user_agent(address, update_agent, no_cache=no_cache)
        print("The response of HostingApi->update_user_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingApi->update_user_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**|  | 
 **update_agent** | [**UpdateAgent**](UpdateAgent.md)|  | 
 **no_cache** | **bool**|  | [optional] [default to False]

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

# **update_user_agent_code**
> AgentCodeDigest update_user_agent_code(address, update_agent_code, no_cache=no_cache)

Update User Agent Code

Updates the code for a specific agent, identified by address

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.hosting
from agentverse_client.hosting.models.agent_code_digest import AgentCodeDigest
from agentverse_client.hosting.models.update_agent_code import UpdateAgentCode
from agentverse_client.hosting.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.hosting.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with agentverse_client.hosting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.hosting.HostingApi(api_client)
    address = 'address_example' # str | 
    update_agent_code = agentverse_client.hosting.UpdateAgentCode() # UpdateAgentCode | 
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Update User Agent Code
        api_response = api_instance.update_user_agent_code(address, update_agent_code, no_cache=no_cache)
        print("The response of HostingApi->update_user_agent_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingApi->update_user_agent_code: %s\n" % e)
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

# **update_user_agent_metadata**
> AgentMetadata update_user_agent_metadata(address, agent_metadata_updates, no_cache=no_cache, x_api_version=x_api_version)

Update User Agent Metadata

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.hosting
from agentverse_client.hosting.models.agent_metadata import AgentMetadata
from agentverse_client.hosting.models.agent_metadata_updates import AgentMetadataUpdates
from agentverse_client.hosting.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.hosting.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with agentverse_client.hosting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.hosting.HostingApi(api_client)
    address = 'address_example' # str | 
    agent_metadata_updates = agentverse_client.hosting.AgentMetadataUpdates() # AgentMetadataUpdates | 
    no_cache = False # bool |  (optional) (default to False)
    x_api_version = 'x_api_version_example' # str |  (optional)

    try:
        # Update User Agent Metadata
        api_response = api_instance.update_user_agent_metadata(address, agent_metadata_updates, no_cache=no_cache, x_api_version=x_api_version)
        print("The response of HostingApi->update_user_agent_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingApi->update_user_agent_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**|  | 
 **agent_metadata_updates** | [**AgentMetadataUpdates**](AgentMetadataUpdates.md)|  | 
 **no_cache** | **bool**|  | [optional] [default to False]
 **x_api_version** | **str**|  | [optional] 

### Return type

[**AgentMetadata**](AgentMetadata.md)

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

# **update_user_agent_network**
> object update_user_agent_network(address, update_agent_network, no_cache=no_cache)

Update User Agent Network

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.hosting
from agentverse_client.hosting.models.update_agent_network import UpdateAgentNetwork
from agentverse_client.hosting.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.hosting.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with agentverse_client.hosting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.hosting.HostingApi(api_client)
    address = 'address_example' # str | 
    update_agent_network = agentverse_client.hosting.UpdateAgentNetwork() # UpdateAgentNetwork | 
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Update User Agent Network
        api_response = api_instance.update_user_agent_network(address, update_agent_network, no_cache=no_cache)
        print("The response of HostingApi->update_user_agent_network:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingApi->update_user_agent_network: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**|  | 
 **update_agent_network** | [**UpdateAgentNetwork**](UpdateAgentNetwork.md)|  | 
 **no_cache** | **bool**|  | [optional] [default to False]

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

# **update_user_agent_storage**
> object update_user_agent_storage(address, key, storage_item_update, no_cache=no_cache)

Update User Agent Storage

Updates the storage for a specific agent, identified by address

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.hosting
from agentverse_client.hosting.models.storage_item_update import StorageItemUpdate
from agentverse_client.hosting.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.hosting.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with agentverse_client.hosting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.hosting.HostingApi(api_client)
    address = 'address_example' # str | 
    key = 'key_example' # str | 
    storage_item_update = agentverse_client.hosting.StorageItemUpdate() # StorageItemUpdate | 
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Update User Agent Storage
        api_response = api_instance.update_user_agent_storage(address, key, storage_item_update, no_cache=no_cache)
        print("The response of HostingApi->update_user_agent_storage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingApi->update_user_agent_storage: %s\n" % e)
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

