# agentverse_client.storage.aio.DefaultApi

All URIs are relative to *https://agentverse.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_asset_permission**](DefaultApi.md#add_asset_permission) | **PUT** /v1/storage/assets/{asset_id}/permissions/ | Add Permission
[**create_asset_metadata**](DefaultApi.md#create_asset_metadata) | **POST** /v1/storage/assets/ | Create Asset Metadata
[**delete_asset**](DefaultApi.md#delete_asset) | **DELETE** /v1/storage/assets/{asset_id}/ | Delete Asset
[**delete_asset_permission**](DefaultApi.md#delete_asset_permission) | **DELETE** /v1/storage/assets/{asset_id}/permissions/ | Delete Asset Permission For An Agent
[**download_asset_contents**](DefaultApi.md#download_asset_contents) | **GET** /v1/storage/assets/{asset_id}/contents/ | Download Asset
[**get_asset_metadata**](DefaultApi.md#get_asset_metadata) | **GET** /v1/storage/assets/{identifier}/ | Retrieve Asset
[**list_asset_permissions**](DefaultApi.md#list_asset_permissions) | **GET** /v1/storage/assets/{asset_id}/permissions/ | List Asset Permissions
[**list_user_assets**](DefaultApi.md#list_user_assets) | **GET** /v1/storage/assets/ | List Assets
[**upload_asset_contents**](DefaultApi.md#upload_asset_contents) | **PUT** /v1/storage/assets/{asset_id}/contents/ | Upload Asset Contents


# **add_asset_permission**
> Permission add_asset_permission(asset_id, new_permission)

Add Permission

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.storage.aio
from agentverse_client.storage.aio.models.new_permission import NewPermission
from agentverse_client.storage.aio.models.permission import Permission
from agentverse_client.storage.aio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.storage.aio.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with agentverse_client.storage.aio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.storage.aio.DefaultApi(api_client)
    asset_id = 'asset_id_example' # str | 
    new_permission = agentverse_client.storage.aio.NewPermission() # NewPermission | 

    try:
        # Add Permission
        api_response = await api_instance.add_asset_permission(asset_id, new_permission)
        print("The response of DefaultApi->add_asset_permission:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->add_asset_permission: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**|  | 
 **new_permission** | [**NewPermission**](NewPermission.md)|  | 

### Return type

[**Permission**](Permission.md)

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

# **create_asset_metadata**
> Asset create_asset_metadata(new_asset)

Create Asset Metadata

Create asset metadata, including its object reference.

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.storage.aio
from agentverse_client.storage.aio.models.asset import Asset
from agentverse_client.storage.aio.models.new_asset import NewAsset
from agentverse_client.storage.aio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.storage.aio.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with agentverse_client.storage.aio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.storage.aio.DefaultApi(api_client)
    new_asset = agentverse_client.storage.aio.NewAsset() # NewAsset | 

    try:
        # Create Asset Metadata
        api_response = await api_instance.create_asset_metadata(new_asset)
        print("The response of DefaultApi->create_asset_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_asset_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_asset** | [**NewAsset**](NewAsset.md)|  | 

### Return type

[**Asset**](Asset.md)

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

# **delete_asset**
> delete_asset(asset_id)

Delete Asset

Delete asset metadata and contents.

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.storage.aio
from agentverse_client.storage.aio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.storage.aio.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with agentverse_client.storage.aio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.storage.aio.DefaultApi(api_client)
    asset_id = 'asset_id_example' # str | 

    try:
        # Delete Asset
        await api_instance.delete_asset(asset_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_asset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[FaunaAuthorizationScheme](../README.md#FaunaAuthorizationScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_asset_permission**
> delete_asset_permission(asset_id, agent_address=agent_address)

Delete Asset Permission For An Agent

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.storage.aio
from agentverse_client.storage.aio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.storage.aio.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with agentverse_client.storage.aio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.storage.aio.DefaultApi(api_client)
    asset_id = 'asset_id_example' # str | 
    agent_address = 'agent_address_example' # str | The agent's address (optional)

    try:
        # Delete Asset Permission For An Agent
        await api_instance.delete_asset_permission(asset_id, agent_address=agent_address)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_asset_permission: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**|  | 
 **agent_address** | **str**| The agent&#39;s address | [optional] 

### Return type

void (empty response body)

### Authorization

[FaunaAuthorizationScheme](../README.md#FaunaAuthorizationScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_asset_contents**
> AssetDownload download_asset_contents(asset_id)

Download Asset

Download asset contents.

### Example


```python
import agentverse_client.storage.aio
from agentverse_client.storage.aio.models.asset_download import AssetDownload
from agentverse_client.storage.aio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.storage.aio.Configuration(
    host = "https://agentverse.ai"
)


# Enter a context with an instance of the API client
async with agentverse_client.storage.aio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.storage.aio.DefaultApi(api_client)
    asset_id = 'asset_id_example' # str | 

    try:
        # Download Asset
        api_response = await api_instance.download_asset_contents(asset_id)
        print("The response of DefaultApi->download_asset_contents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->download_asset_contents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**|  | 

### Return type

[**AssetDownload**](AssetDownload.md)

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

# **get_asset_metadata**
> Asset get_asset_metadata(identifier)

Retrieve Asset

Retrieves asset metadata details.

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.storage.aio
from agentverse_client.storage.aio.models.asset import Asset
from agentverse_client.storage.aio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.storage.aio.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with agentverse_client.storage.aio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.storage.aio.DefaultApi(api_client)
    identifier = 'identifier_example' # str | 

    try:
        # Retrieve Asset
        api_response = await api_instance.get_asset_metadata(identifier)
        print("The response of DefaultApi->get_asset_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_asset_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**|  | 

### Return type

[**Asset**](Asset.md)

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

# **list_asset_permissions**
> PermissionList list_asset_permissions(asset_id, agent_address=agent_address, offset=offset, limit=limit)

List Asset Permissions

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.storage.aio
from agentverse_client.storage.aio.models.permission_list import PermissionList
from agentverse_client.storage.aio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.storage.aio.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with agentverse_client.storage.aio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.storage.aio.DefaultApi(api_client)
    asset_id = 'asset_id_example' # str | 
    agent_address = 'agent_address_example' # str |  (optional)
    offset = 0 # int |  (optional) (default to 0)
    limit = 100 # int |  (optional) (default to 100)

    try:
        # List Asset Permissions
        api_response = await api_instance.list_asset_permissions(asset_id, agent_address=agent_address, offset=offset, limit=limit)
        print("The response of DefaultApi->list_asset_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_asset_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**|  | 
 **agent_address** | **str**|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**PermissionList**](PermissionList.md)

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

# **list_user_assets**
> AssetsList list_user_assets(offset=offset, limit=limit)

List Assets

List user assets.

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.storage.aio
from agentverse_client.storage.aio.models.assets_list import AssetsList
from agentverse_client.storage.aio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.storage.aio.Configuration(
    host = "https://agentverse.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with agentverse_client.storage.aio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.storage.aio.DefaultApi(api_client)
    offset = 0 # int |  (optional) (default to 0)
    limit = 100 # int |  (optional) (default to 100)

    try:
        # List Assets
        api_response = await api_instance.list_user_assets(offset=offset, limit=limit)
        print("The response of DefaultApi->list_user_assets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_user_assets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**AssetsList**](AssetsList.md)

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

# **upload_asset_contents**
> UploadAssetResponse upload_asset_contents(asset_id, asset_content)

Upload Asset Contents

Upload the asset contents.

### Example


```python
import agentverse_client.storage.aio
from agentverse_client.storage.aio.models.asset_content import AssetContent
from agentverse_client.storage.aio.models.upload_asset_response import UploadAssetResponse
from agentverse_client.storage.aio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.storage.aio.Configuration(
    host = "https://agentverse.ai"
)


# Enter a context with an instance of the API client
async with agentverse_client.storage.aio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.storage.aio.DefaultApi(api_client)
    asset_id = 'asset_id_example' # str | 
    asset_content = agentverse_client.storage.aio.AssetContent() # AssetContent | 

    try:
        # Upload Asset Contents
        api_response = await api_instance.upload_asset_contents(asset_id, asset_content)
        print("The response of DefaultApi->upload_asset_contents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->upload_asset_contents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**|  | 
 **asset_content** | [**AssetContent**](AssetContent.md)|  | 

### Return type

[**UploadAssetResponse**](UploadAssetResponse.md)

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

