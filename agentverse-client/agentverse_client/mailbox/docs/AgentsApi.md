# agentverse_client.mailbox.AgentsApi

All URIs are relative to *https://agentverse.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_team_agent**](AgentsApi.md#delete_team_agent) | **DELETE** /v1/mailroom/teams/{slug}/agents/{address} | Delete Specific Team Agent
[**delete_user_agent**](AgentsApi.md#delete_user_agent) | **DELETE** /v1/agents/{address} | Delete Specific User Agent
[**get_public_agent_profile**](AgentsApi.md#get_public_agent_profile) | **GET** /v1/agents/{address}/profile | Get Public Agent Profile
[**get_team_agent**](AgentsApi.md#get_team_agent) | **GET** /v1/mailroom/teams/{slug}/agents/{address} | Get Specific Team Agent
[**get_user_agent**](AgentsApi.md#get_user_agent) | **GET** /v1/agents/{address} | Get Specific User Agent
[**list_team_agents**](AgentsApi.md#list_team_agents) | **GET** /v1/mailroom/teams/{slug}/agents | List Team Agents
[**list_user_agents**](AgentsApi.md#list_user_agents) | **GET** /v1/agents | List User Agents
[**update_team_agent**](AgentsApi.md#update_team_agent) | **PUT** /v1/mailroom/teams/{slug}/agents/{address} | Update Specific Team Agent
[**update_user_agent**](AgentsApi.md#update_user_agent) | **PUT** /v1/agents/{address} | Update Specific User Agent


# **delete_team_agent**
> object delete_team_agent(slug, address)

Delete Specific Team Agent

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.mailbox
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
    api_instance = agentverse_client.mailbox.AgentsApi(api_client)
    slug = 'slug_example' # str | 
    address = 'address_example' # str | 

    try:
        # Delete Specific Team Agent
        api_response = api_instance.delete_team_agent(slug, address)
        print("The response of AgentsApi->delete_team_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->delete_team_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **address** | **str**|  | 

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
> object delete_user_agent(address)

Delete Specific User Agent

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.mailbox
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
    api_instance = agentverse_client.mailbox.AgentsApi(api_client)
    address = 'address_example' # str | 

    try:
        # Delete Specific User Agent
        api_response = api_instance.delete_user_agent(address)
        print("The response of AgentsApi->delete_user_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->delete_user_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**|  | 

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

# **get_public_agent_profile**
> PublicAgent get_public_agent_profile(address)

Get Public Agent Profile

### Example


```python
import agentverse_client.mailbox
from agentverse_client.mailbox.models.public_agent import PublicAgent
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
    api_instance = agentverse_client.mailbox.AgentsApi(api_client)
    address = 'address_example' # str | 

    try:
        # Get Public Agent Profile
        api_response = api_instance.get_public_agent_profile(address)
        print("The response of AgentsApi->get_public_agent_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->get_public_agent_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**|  | 

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

# **get_team_agent**
> Agent get_team_agent(slug, address)

Get Specific Team Agent

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.mailbox
from agentverse_client.mailbox.models.agent import Agent
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
    api_instance = agentverse_client.mailbox.AgentsApi(api_client)
    slug = 'slug_example' # str | 
    address = 'address_example' # str | 

    try:
        # Get Specific Team Agent
        api_response = api_instance.get_team_agent(slug, address)
        print("The response of AgentsApi->get_team_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->get_team_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **address** | **str**|  | 

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

# **get_user_agent**
> Agent get_user_agent(address)

Get Specific User Agent

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.mailbox
from agentverse_client.mailbox.models.agent import Agent
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
    api_instance = agentverse_client.mailbox.AgentsApi(api_client)
    address = 'address_example' # str | 

    try:
        # Get Specific User Agent
        api_response = api_instance.get_user_agent(address)
        print("The response of AgentsApi->get_user_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->get_user_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**|  | 

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

# **list_team_agents**
> PageAgent list_team_agents(slug, page=page, size=size)

List Team Agents

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.mailbox
from agentverse_client.mailbox.models.page_agent import PageAgent
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
    api_instance = agentverse_client.mailbox.AgentsApi(api_client)
    slug = 'slug_example' # str | 
    page = 1 # int | Page number (optional) (default to 1)
    size = 50 # int | Page size (optional) (default to 50)

    try:
        # List Team Agents
        api_response = api_instance.list_team_agents(slug, page=page, size=size)
        print("The response of AgentsApi->list_team_agents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->list_team_agents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **page** | **int**| Page number | [optional] [default to 1]
 **size** | **int**| Page size | [optional] [default to 50]

### Return type

[**PageAgent**](PageAgent.md)

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
> PageAgent list_user_agents(page=page, size=size)

List User Agents

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.mailbox
from agentverse_client.mailbox.models.page_agent import PageAgent
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
    api_instance = agentverse_client.mailbox.AgentsApi(api_client)
    page = 1 # int | Page number (optional) (default to 1)
    size = 50 # int | Page size (optional) (default to 50)

    try:
        # List User Agents
        api_response = api_instance.list_user_agents(page=page, size=size)
        print("The response of AgentsApi->list_user_agents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->list_user_agents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | [optional] [default to 1]
 **size** | **int**| Page size | [optional] [default to 50]

### Return type

[**PageAgent**](PageAgent.md)

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
> Agent update_team_agent(slug, address, agent_updates)

Update Specific Team Agent

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.mailbox
from agentverse_client.mailbox.models.agent import Agent
from agentverse_client.mailbox.models.agent_updates import AgentUpdates
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
    api_instance = agentverse_client.mailbox.AgentsApi(api_client)
    slug = 'slug_example' # str | 
    address = 'address_example' # str | 
    agent_updates = agentverse_client.mailbox.AgentUpdates() # AgentUpdates | 

    try:
        # Update Specific Team Agent
        api_response = api_instance.update_team_agent(slug, address, agent_updates)
        print("The response of AgentsApi->update_team_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->update_team_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **address** | **str**|  | 
 **agent_updates** | [**AgentUpdates**](AgentUpdates.md)|  | 

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

# **update_user_agent**
> Agent update_user_agent(address, agent_updates)

Update Specific User Agent

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.mailbox
from agentverse_client.mailbox.models.agent import Agent
from agentverse_client.mailbox.models.agent_updates import AgentUpdates
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
    api_instance = agentverse_client.mailbox.AgentsApi(api_client)
    address = 'address_example' # str | 
    agent_updates = agentverse_client.mailbox.AgentUpdates() # AgentUpdates | 

    try:
        # Update Specific User Agent
        api_response = api_instance.update_user_agent(address, agent_updates)
        print("The response of AgentsApi->update_user_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->update_user_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**|  | 
 **agent_updates** | [**AgentUpdates**](AgentUpdates.md)|  | 

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

