# agentverse_client.almanac.AlmanacV2Api

All URIs are relative to *https://agentverse.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_handle_availability_v2**](AlmanacV2Api.md#check_handle_availability_v2) | **GET** /v2/almanac/handles/{handle}/available | Check Handle Availability V2
[**generate_handle_v2**](AlmanacV2Api.md#generate_handle_v2) | **GET** /v2/almanac/handles/{handle}/generate | Generate Handle V2
[**get_manifest_by_name_v2**](AlmanacV2Api.md#get_manifest_by_name_v2) | **GET** /v2/almanac/manifest/name/{name} | Get Manifest By Name V2
[**get_manifest_v2**](AlmanacV2Api.md#get_manifest_v2) | **GET** /v2/almanac/manifest/{digest} | Get Manifest V2
[**get_protocol_model_v2**](AlmanacV2Api.md#get_protocol_model_v2) | **GET** /v2/almanac/manifest/model/{digest} | Get Protocol Model V2
[**resolve_identifier_v2**](AlmanacV2Api.md#resolve_identifier_v2) | **GET** /v2/almanac/resolve/{identifier} | Resolve Identifier V2
[**upload_manifest_v2**](AlmanacV2Api.md#upload_manifest_v2) | **POST** /v2/almanac/manifest | Upload Manifest V2


# **check_handle_availability_v2**
> HandleAvailabilityResponse check_handle_availability_v2(handle)

Check Handle Availability V2

Check if a handle is available

### Example


```python
import agentverse_client.almanac
from agentverse_client.almanac.models.handle_availability_response import HandleAvailabilityResponse
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
    api_instance = agentverse_client.almanac.AlmanacV2Api(api_client)
    handle = 'handle_example' # str | Handle to check for availability

    try:
        # Check Handle Availability V2
        api_response = api_instance.check_handle_availability_v2(handle)
        print("The response of AlmanacV2Api->check_handle_availability_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlmanacV2Api->check_handle_availability_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **handle** | **str**| Handle to check for availability | 

### Return type

[**HandleAvailabilityResponse**](HandleAvailabilityResponse.md)

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

# **generate_handle_v2**
> HandleGenerateResponse generate_handle_v2(handle)

Generate Handle V2

Generate a unique handle based on the provided name

### Example


```python
import agentverse_client.almanac
from agentverse_client.almanac.models.handle_generate_response import HandleGenerateResponse
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
    api_instance = agentverse_client.almanac.AlmanacV2Api(api_client)
    handle = 'handle_example' # str | Base name for handle generation

    try:
        # Generate Handle V2
        api_response = api_instance.generate_handle_v2(handle)
        print("The response of AlmanacV2Api->generate_handle_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlmanacV2Api->generate_handle_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **handle** | **str**| Base name for handle generation | 

### Return type

[**HandleGenerateResponse**](HandleGenerateResponse.md)

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

# **get_manifest_by_name_v2**
> Manifest get_manifest_by_name_v2(name)

Get Manifest By Name V2

Get a manifest by name (returns the latest version)

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
    api_instance = agentverse_client.almanac.AlmanacV2Api(api_client)
    name = 'name_example' # str | 

    try:
        # Get Manifest By Name V2
        api_response = api_instance.get_manifest_by_name_v2(name)
        print("The response of AlmanacV2Api->get_manifest_by_name_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlmanacV2Api->get_manifest_by_name_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

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

# **get_manifest_v2**
> Manifest get_manifest_v2(digest)

Get Manifest V2

Get a manifest by protocol digest

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
    api_instance = agentverse_client.almanac.AlmanacV2Api(api_client)
    digest = 'digest_example' # str | 

    try:
        # Get Manifest V2
        api_response = api_instance.get_manifest_v2(digest)
        print("The response of AlmanacV2Api->get_manifest_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlmanacV2Api->get_manifest_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **digest** | **str**|  | 

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

# **get_protocol_model_v2**
> object get_protocol_model_v2(digest)

Get Protocol Model V2

Get a model by digest

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
    api_instance = agentverse_client.almanac.AlmanacV2Api(api_client)
    digest = 'digest_example' # str | 

    try:
        # Get Protocol Model V2
        api_response = api_instance.get_protocol_model_v2(digest)
        print("The response of AlmanacV2Api->get_protocol_model_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlmanacV2Api->get_protocol_model_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **digest** | **str**|  | 

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

# **resolve_identifier_v2**
> Agent resolve_identifier_v2(identifier)

Resolve Identifier V2

Resolve any agent identifier (address, handle, or domain) to agent details with endpoints. This is a unified resolver that can handle: - Agent addresses (agent1q...) - Handles (my-agent) - Domain names (my-agent.agentverse.ai)

### Example


```python
import agentverse_client.almanac
from agentverse_client.almanac.models.agent import Agent
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
    api_instance = agentverse_client.almanac.AlmanacV2Api(api_client)
    identifier = 'identifier_example' # str | Agent identifier (address, handle, or domain)

    try:
        # Resolve Identifier V2
        api_response = api_instance.resolve_identifier_v2(identifier)
        print("The response of AlmanacV2Api->resolve_identifier_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlmanacV2Api->resolve_identifier_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Agent identifier (address, handle, or domain) | 

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

# **upload_manifest_v2**
> object upload_manifest_v2(body)

Upload Manifest V2

Upload a new manifest

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
    api_instance = agentverse_client.almanac.AlmanacV2Api(api_client)
    body = None # object | 

    try:
        # Upload Manifest V2
        api_response = api_instance.upload_manifest_v2(body)
        print("The response of AlmanacV2Api->upload_manifest_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlmanacV2Api->upload_manifest_v2: %s\n" % e)
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

