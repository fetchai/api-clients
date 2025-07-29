# agentverse_client.almanac.ManifestsApi

All URIs are relative to *https://agentverse.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_manifest**](ManifestsApi.md#get_manifest) | **GET** /v1/almanac/manifests/protocols/{protocol_digest} | Get Protocol Manifest
[**get_protocol_models**](ManifestsApi.md#get_protocol_models) | **GET** /v1/almanac/manifests/models/{model_digest} | Get Protocol Models
[**list_manifests**](ManifestsApi.md#list_manifests) | **POST** /v1/almanac/manifests | Upload Manifest
[**resolve_protocol_digest**](ManifestsApi.md#resolve_protocol_digest) | **GET** /v1/almanac/manifests/digests/ | Resolve Procotol Digests
[**search_protocol_digests**](ManifestsApi.md#search_protocol_digests) | **GET** /v1/almanac/manifests/digests/search/ | Search Procotol Digests


# **get_manifest**
> Manifest get_manifest(protocol_digest)

Get Protocol Manifest

### Example


```python
import agentverse_client.almanac
from agentverse_client.almanac.models.manifest import Manifest
from agentverse_client.almanac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.almanac.Configuration(
    host = "https://agentverse.ai"
)


# Enter a context with an instance of the API client
with agentverse_client.almanac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.almanac.ManifestsApi(api_client)
    protocol_digest = 'protocol_digest_example' # str | 

    try:
        # Get Protocol Manifest
        api_response = api_instance.get_manifest(protocol_digest)
        print("The response of ManifestsApi->get_manifest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManifestsApi->get_manifest: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **protocol_digest** | **str**|  | 

### Return type

[**Manifest**](Manifest.md)

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

# **get_protocol_models**
> object get_protocol_models(model_digest)

Get Protocol Models

### Example


```python
import agentverse_client.almanac
from agentverse_client.almanac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.almanac.Configuration(
    host = "https://agentverse.ai"
)


# Enter a context with an instance of the API client
with agentverse_client.almanac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.almanac.ManifestsApi(api_client)
    model_digest = 'model_digest_example' # str | 

    try:
        # Get Protocol Models
        api_response = api_instance.get_protocol_models(model_digest)
        print("The response of ManifestsApi->get_protocol_models:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManifestsApi->get_protocol_models: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_digest** | **str**|  | 

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

# **list_manifests**
> object list_manifests(body)

Upload Manifest

### Example


```python
import agentverse_client.almanac
from agentverse_client.almanac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.almanac.Configuration(
    host = "https://agentverse.ai"
)


# Enter a context with an instance of the API client
with agentverse_client.almanac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.almanac.ManifestsApi(api_client)
    body = None # object | 

    try:
        # Upload Manifest
        api_response = api_instance.list_manifests(body)
        print("The response of ManifestsApi->list_manifests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManifestsApi->list_manifests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**|  | 

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

# **resolve_protocol_digest**
> List[ResolvedProtocolDigest] resolve_protocol_digest(protocol_digest=protocol_digest)

Resolve Procotol Digests

### Example


```python
import agentverse_client.almanac
from agentverse_client.almanac.models.resolved_protocol_digest import ResolvedProtocolDigest
from agentverse_client.almanac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.almanac.Configuration(
    host = "https://agentverse.ai"
)


# Enter a context with an instance of the API client
with agentverse_client.almanac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.almanac.ManifestsApi(api_client)
    protocol_digest = ['protocol_digest_example'] # List[str] |  (optional)

    try:
        # Resolve Procotol Digests
        api_response = api_instance.resolve_protocol_digest(protocol_digest=protocol_digest)
        print("The response of ManifestsApi->resolve_protocol_digest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManifestsApi->resolve_protocol_digest: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **protocol_digest** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**List[ResolvedProtocolDigest]**](ResolvedProtocolDigest.md)

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

# **search_protocol_digests**
> List[ResolvedProtocolDigest] search_protocol_digests(name=name)

Search Procotol Digests

### Example


```python
import agentverse_client.almanac
from agentverse_client.almanac.models.resolved_protocol_digest import ResolvedProtocolDigest
from agentverse_client.almanac.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agentverse.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = agentverse_client.almanac.Configuration(
    host = "https://agentverse.ai"
)


# Enter a context with an instance of the API client
with agentverse_client.almanac.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agentverse_client.almanac.ManifestsApi(api_client)
    name = 'name_example' # str |  (optional)

    try:
        # Search Procotol Digests
        api_response = api_instance.search_protocol_digests(name=name)
        print("The response of ManifestsApi->search_protocol_digests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManifestsApi->search_protocol_digests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 

### Return type

[**List[ResolvedProtocolDigest]**](ResolvedProtocolDigest.md)

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

