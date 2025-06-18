# agentverse_client.mailbox.aio.UsersApi

All URIs are relative to *https://agentverse.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_username_availability**](UsersApi.md#check_username_availability) | **GET** /v1/users/username/{username} | User Name Available
[**delete_user**](UsersApi.md#delete_user) | **DELETE** /v1/users/{uid} | Delete User
[**get_user_by_agent_address**](UsersApi.md#get_user_by_agent_address) | **GET** /v1/users/agent/{agent_address} | Get User By Agent
[**get_user_by_id**](UsersApi.md#get_user_by_id) | **GET** /v1/users/{uid} | Get User By Id
[**get_user_list**](UsersApi.md#get_user_list) | **GET** /v1/user_list/ | Get User List
[**get_user_public_profile**](UsersApi.md#get_user_public_profile) | **GET** /v1/users/public/{uid} | Get User Public
[**search_users_by_username**](UsersApi.md#search_users_by_username) | **GET** /v1/users/username/search/{username} | Search User
[**update_user_email**](UsersApi.md#update_user_email) | **PUT** /v1/users/mail/{uid} | Update User Mail
[**update_username**](UsersApi.md#update_username) | **PUT** /v1/users | Update User


# **check_username_availability**
> bool check_username_availability(username)

User Name Available

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
    api_instance = agentverse_client.mailbox.aio.UsersApi(api_client)
    username = 'username_example' # str | 

    try:
        # User Name Available
        api_response = await api_instance.check_username_availability(username)
        print("The response of UsersApi->check_username_availability:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->check_username_availability: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 

### Return type

**bool**

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

# **delete_user**
> object delete_user(uid)

Delete User

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
    api_instance = agentverse_client.mailbox.aio.UsersApi(api_client)
    uid = 'uid_example' # str | 

    try:
        # Delete User
        api_response = await api_instance.delete_user(uid)
        print("The response of UsersApi->delete_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->delete_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**|  | 

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

# **get_user_by_agent_address**
> TortoiseContribPydanticCreatorRelayDbModelsDbUserLeaf get_user_by_agent_address(agent_address)

Get User By Agent

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.mailbox.aio
from agentverse_client.mailbox.aio.models.tortoise_contrib_pydantic_creator_relay_db_models_db_user_leaf import TortoiseContribPydanticCreatorRelayDbModelsDbUserLeaf
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
    api_instance = agentverse_client.mailbox.aio.UsersApi(api_client)
    agent_address = 'agent_address_example' # str | 

    try:
        # Get User By Agent
        api_response = await api_instance.get_user_by_agent_address(agent_address)
        print("The response of UsersApi->get_user_by_agent_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_by_agent_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_address** | **str**|  | 

### Return type

[**TortoiseContribPydanticCreatorRelayDbModelsDbUserLeaf**](TortoiseContribPydanticCreatorRelayDbModelsDbUserLeaf.md)

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

# **get_user_by_id**
> TortoiseContribPydanticCreatorRelayDbModelsDbUserLeaf get_user_by_id(uid)

Get User By Id

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.mailbox.aio
from agentverse_client.mailbox.aio.models.tortoise_contrib_pydantic_creator_relay_db_models_db_user_leaf import TortoiseContribPydanticCreatorRelayDbModelsDbUserLeaf
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
    api_instance = agentverse_client.mailbox.aio.UsersApi(api_client)
    uid = 'uid_example' # str | 

    try:
        # Get User By Id
        api_response = await api_instance.get_user_by_id(uid)
        print("The response of UsersApi->get_user_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**|  | 

### Return type

[**TortoiseContribPydanticCreatorRelayDbModelsDbUserLeaf**](TortoiseContribPydanticCreatorRelayDbModelsDbUserLeaf.md)

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

# **get_user_list**
> List[TortoiseContribPydanticCreatorRelayDbModelsDbUserLeaf] get_user_list(uids=uids)

Get User List

### Example


```python
import agentverse_client.mailbox.aio
from agentverse_client.mailbox.aio.models.tortoise_contrib_pydantic_creator_relay_db_models_db_user_leaf import TortoiseContribPydanticCreatorRelayDbModelsDbUserLeaf
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
    api_instance = agentverse_client.mailbox.aio.UsersApi(api_client)
    uids = [] # List[str] |  (optional) (default to [])

    try:
        # Get User List
        api_response = await api_instance.get_user_list(uids=uids)
        print("The response of UsersApi->get_user_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uids** | [**List[str]**](str.md)|  | [optional] [default to []]

### Return type

[**List[TortoiseContribPydanticCreatorRelayDbModelsDbUserLeaf]**](TortoiseContribPydanticCreatorRelayDbModelsDbUserLeaf.md)

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

# **get_user_public_profile**
> TortoiseContribPydanticCreatorRelayDbModelsDbUserLeaf get_user_public_profile(uid)

Get User Public

### Example


```python
import agentverse_client.mailbox.aio
from agentverse_client.mailbox.aio.models.tortoise_contrib_pydantic_creator_relay_db_models_db_user_leaf import TortoiseContribPydanticCreatorRelayDbModelsDbUserLeaf
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
    api_instance = agentverse_client.mailbox.aio.UsersApi(api_client)
    uid = 'uid_example' # str | 

    try:
        # Get User Public
        api_response = await api_instance.get_user_public_profile(uid)
        print("The response of UsersApi->get_user_public_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_public_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**|  | 

### Return type

[**TortoiseContribPydanticCreatorRelayDbModelsDbUserLeaf**](TortoiseContribPydanticCreatorRelayDbModelsDbUserLeaf.md)

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

# **search_users_by_username**
> List[TortoiseContribPydanticCreatorRelayDbModelsDbUserLeaf] search_users_by_username(username)

Search User

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.mailbox.aio
from agentverse_client.mailbox.aio.models.tortoise_contrib_pydantic_creator_relay_db_models_db_user_leaf import TortoiseContribPydanticCreatorRelayDbModelsDbUserLeaf
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
    api_instance = agentverse_client.mailbox.aio.UsersApi(api_client)
    username = 'username_example' # str | 

    try:
        # Search User
        api_response = await api_instance.search_users_by_username(username)
        print("The response of UsersApi->search_users_by_username:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->search_users_by_username: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 

### Return type

[**List[TortoiseContribPydanticCreatorRelayDbModelsDbUserLeaf]**](TortoiseContribPydanticCreatorRelayDbModelsDbUserLeaf.md)

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

# **update_user_email**
> object update_user_email(uid, user_mail_update)

Update User Mail

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.mailbox.aio
from agentverse_client.mailbox.aio.models.user_mail_update import UserMailUpdate
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
    api_instance = agentverse_client.mailbox.aio.UsersApi(api_client)
    uid = 'uid_example' # str | 
    user_mail_update = agentverse_client.mailbox.aio.UserMailUpdate() # UserMailUpdate | 

    try:
        # Update User Mail
        api_response = await api_instance.update_user_email(uid, user_mail_update)
        print("The response of UsersApi->update_user_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->update_user_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**|  | 
 **user_mail_update** | [**UserMailUpdate**](UserMailUpdate.md)|  | 

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

# **update_username**
> TortoiseContribPydanticCreatorRelayDbModelsDbUserLeaf update_username(user_update)

Update User

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.mailbox.aio
from agentverse_client.mailbox.aio.models.tortoise_contrib_pydantic_creator_relay_db_models_db_user_leaf import TortoiseContribPydanticCreatorRelayDbModelsDbUserLeaf
from agentverse_client.mailbox.aio.models.user_update import UserUpdate
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
    api_instance = agentverse_client.mailbox.aio.UsersApi(api_client)
    user_update = agentverse_client.mailbox.aio.UserUpdate() # UserUpdate | 

    try:
        # Update User
        api_response = await api_instance.update_username(user_update)
        print("The response of UsersApi->update_username:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->update_username: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_update** | [**UserUpdate**](UserUpdate.md)|  | 

### Return type

[**TortoiseContribPydanticCreatorRelayDbModelsDbUserLeaf**](TortoiseContribPydanticCreatorRelayDbModelsDbUserLeaf.md)

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

