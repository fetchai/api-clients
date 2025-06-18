# agentverse_client.mailbox.aio.ApiKeysApi

All URIs are relative to *https://agentverse.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_teams_api_key**](ApiKeysApi.md#add_teams_api_key) | **POST** /v1/mailroom/teams/{slug}/api-keys | Add Teams Api Key
[**add_user_api_key**](ApiKeysApi.md#add_user_api_key) | **POST** /v1/api-keys | Add User Api Key
[**delete_teams_api_key**](ApiKeysApi.md#delete_teams_api_key) | **DELETE** /v1/mailroom/teams/{slug}/api-keys/{id} | Delete Teams Api Key
[**delete_user_api_key**](ApiKeysApi.md#delete_user_api_key) | **DELETE** /v1/api-keys/{id} | Delete User Api Key
[**list_team_api_keys**](ApiKeysApi.md#list_team_api_keys) | **GET** /v1/mailroom/teams/{slug}/api-keys | List Team Api Keys
[**list_user_api_keys**](ApiKeysApi.md#list_user_api_keys) | **GET** /v1/api-keys | List User Api Keys
[**update_team_api_key**](ApiKeysApi.md#update_team_api_key) | **PUT** /v1/mailroom/teams/{slug}/api-keys/{id} | Update Teams Api Key
[**update_user_api_key**](ApiKeysApi.md#update_user_api_key) | **PUT** /v1/api-keys/{id} | Update User Api Key


# **add_teams_api_key**
> TortoiseContribPydanticCreatorRelayDbModelsDbApiKeyLeaf add_teams_api_key(slug, new_api_key)

Add Teams Api Key

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.mailbox.aio
from agentverse_client.mailbox.aio.models.new_api_key import NewApiKey
from agentverse_client.mailbox.aio.models.tortoise_contrib_pydantic_creator_relay_db_models_db_api_key_leaf import TortoiseContribPydanticCreatorRelayDbModelsDbApiKeyLeaf
from agentverse_client.mailbox.aio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.mailbox.aio.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with agentverse_client.mailbox.aio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.mailbox.aio.ApiKeysApi(api_client)
    slug = 'slug_example' # str | 
    new_api_key = agentverse_client.mailbox.aio.NewApiKey() # NewApiKey | 

    try:
        # Add Teams Api Key
        api_response = await api_instance.add_teams_api_key(slug, new_api_key)
        print("The response of ApiKeysApi->add_teams_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeysApi->add_teams_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **new_api_key** | [**NewApiKey**](NewApiKey.md)|  | 

### Return type

[**TortoiseContribPydanticCreatorRelayDbModelsDbApiKeyLeaf**](TortoiseContribPydanticCreatorRelayDbModelsDbApiKeyLeaf.md)

### Authorization

[FaunaAuthorizationScheme](../README.md#FaunaAuthorizationScheme)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_user_api_key**
> TortoiseContribPydanticCreatorRelayDbModelsDbApiKeyLeaf add_user_api_key(new_api_key)

Add User Api Key

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.mailbox.aio
from agentverse_client.mailbox.aio.models.new_api_key import NewApiKey
from agentverse_client.mailbox.aio.models.tortoise_contrib_pydantic_creator_relay_db_models_db_api_key_leaf import TortoiseContribPydanticCreatorRelayDbModelsDbApiKeyLeaf
from agentverse_client.mailbox.aio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.mailbox.aio.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with agentverse_client.mailbox.aio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.mailbox.aio.ApiKeysApi(api_client)
    new_api_key = agentverse_client.mailbox.aio.NewApiKey() # NewApiKey | 

    try:
        # Add User Api Key
        api_response = await api_instance.add_user_api_key(new_api_key)
        print("The response of ApiKeysApi->add_user_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeysApi->add_user_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_api_key** | [**NewApiKey**](NewApiKey.md)|  | 

### Return type

[**TortoiseContribPydanticCreatorRelayDbModelsDbApiKeyLeaf**](TortoiseContribPydanticCreatorRelayDbModelsDbApiKeyLeaf.md)

### Authorization

[FaunaAuthorizationScheme](../README.md#FaunaAuthorizationScheme)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_teams_api_key**
> object delete_teams_api_key(slug, id)

Delete Teams Api Key

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.mailbox.aio
from agentverse_client.mailbox.aio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.mailbox.aio.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with agentverse_client.mailbox.aio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.mailbox.aio.ApiKeysApi(api_client)
    slug = 'slug_example' # str | 
    id = 'id_example' # str | 

    try:
        # Delete Teams Api Key
        api_response = await api_instance.delete_teams_api_key(slug, id)
        print("The response of ApiKeysApi->delete_teams_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeysApi->delete_teams_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **id** | **str**|  | 

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

# **delete_user_api_key**
> object delete_user_api_key(id)

Delete User Api Key

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.mailbox.aio
from agentverse_client.mailbox.aio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.mailbox.aio.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with agentverse_client.mailbox.aio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.mailbox.aio.ApiKeysApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete User Api Key
        api_response = await api_instance.delete_user_api_key(id)
        print("The response of ApiKeysApi->delete_user_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeysApi->delete_user_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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

# **list_team_api_keys**
> PageLeaf list_team_api_keys(slug, page=page, size=size)

List Team Api Keys

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.mailbox.aio
from agentverse_client.mailbox.aio.models.page_leaf import PageLeaf
from agentverse_client.mailbox.aio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.mailbox.aio.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with agentverse_client.mailbox.aio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.mailbox.aio.ApiKeysApi(api_client)
    slug = 'slug_example' # str | 
    page = 1 # int | Page number (optional) (default to 1)
    size = 50 # int | Page size (optional) (default to 50)

    try:
        # List Team Api Keys
        api_response = await api_instance.list_team_api_keys(slug, page=page, size=size)
        print("The response of ApiKeysApi->list_team_api_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeysApi->list_team_api_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **page** | **int**| Page number | [optional] [default to 1]
 **size** | **int**| Page size | [optional] [default to 50]

### Return type

[**PageLeaf**](PageLeaf.md)

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

# **list_user_api_keys**
> PageLeaf list_user_api_keys(page=page, size=size)

List User Api Keys

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.mailbox.aio
from agentverse_client.mailbox.aio.models.page_leaf import PageLeaf
from agentverse_client.mailbox.aio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.mailbox.aio.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with agentverse_client.mailbox.aio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.mailbox.aio.ApiKeysApi(api_client)
    page = 1 # int | Page number (optional) (default to 1)
    size = 50 # int | Page size (optional) (default to 50)

    try:
        # List User Api Keys
        api_response = await api_instance.list_user_api_keys(page=page, size=size)
        print("The response of ApiKeysApi->list_user_api_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeysApi->list_user_api_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | [optional] [default to 1]
 **size** | **int**| Page size | [optional] [default to 50]

### Return type

[**PageLeaf**](PageLeaf.md)

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

# **update_team_api_key**
> TortoiseContribPydanticCreatorRelayDbModelsDbApiKeyLeaf update_team_api_key(id, slug, api_key_update)

Update Teams Api Key

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.mailbox.aio
from agentverse_client.mailbox.aio.models.api_key_update import ApiKeyUpdate
from agentverse_client.mailbox.aio.models.tortoise_contrib_pydantic_creator_relay_db_models_db_api_key_leaf import TortoiseContribPydanticCreatorRelayDbModelsDbApiKeyLeaf
from agentverse_client.mailbox.aio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.mailbox.aio.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with agentverse_client.mailbox.aio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.mailbox.aio.ApiKeysApi(api_client)
    id = 'id_example' # str | 
    slug = 'slug_example' # str | 
    api_key_update = agentverse_client.mailbox.aio.ApiKeyUpdate() # ApiKeyUpdate | 

    try:
        # Update Teams Api Key
        api_response = await api_instance.update_team_api_key(id, slug, api_key_update)
        print("The response of ApiKeysApi->update_team_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeysApi->update_team_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **slug** | **str**|  | 
 **api_key_update** | [**ApiKeyUpdate**](ApiKeyUpdate.md)|  | 

### Return type

[**TortoiseContribPydanticCreatorRelayDbModelsDbApiKeyLeaf**](TortoiseContribPydanticCreatorRelayDbModelsDbApiKeyLeaf.md)

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

# **update_user_api_key**
> TortoiseContribPydanticCreatorRelayDbModelsDbApiKeyLeaf update_user_api_key(id, api_key_update)

Update User Api Key

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.mailbox.aio
from agentverse_client.mailbox.aio.models.api_key_update import ApiKeyUpdate
from agentverse_client.mailbox.aio.models.tortoise_contrib_pydantic_creator_relay_db_models_db_api_key_leaf import TortoiseContribPydanticCreatorRelayDbModelsDbApiKeyLeaf
from agentverse_client.mailbox.aio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.mailbox.aio.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with agentverse_client.mailbox.aio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.mailbox.aio.ApiKeysApi(api_client)
    id = 'id_example' # str | 
    api_key_update = agentverse_client.mailbox.aio.ApiKeyUpdate() # ApiKeyUpdate | 

    try:
        # Update User Api Key
        api_response = await api_instance.update_user_api_key(id, api_key_update)
        print("The response of ApiKeysApi->update_user_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeysApi->update_user_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **api_key_update** | [**ApiKeyUpdate**](ApiKeyUpdate.md)|  | 

### Return type

[**TortoiseContribPydanticCreatorRelayDbModelsDbApiKeyLeaf**](TortoiseContribPydanticCreatorRelayDbModelsDbApiKeyLeaf.md)

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

