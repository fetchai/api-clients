# agentverse_client.almanac.AlmanacApi

All URIs are relative to *https://agentverse.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_agents_by_domain_v1_almanac_search_agents_by_domain_domain_name_get**](AlmanacApi.md#get_agents_by_domain_v1_almanac_search_agents_by_domain_domain_name_get) | **GET** /v1/almanac/search/agents-by-domain/{domain_name} | Get Agents By Domain
[**get_domain_details_v1_almanac_search_domain_details_domain_name_get**](AlmanacApi.md#get_domain_details_v1_almanac_search_domain_details_domain_name_get) | **GET** /v1/almanac/search/domain_details/{domain_name} | Get Domain Details
[**get_domain_record_v1_almanac_domains_domain_get**](AlmanacApi.md#get_domain_record_v1_almanac_domains_domain_get) | **GET** /v1/almanac/domains/{domain} | Get Domain Record
[**get_domains_v1_almanac_search_domains_address_get**](AlmanacApi.md#get_domains_v1_almanac_search_domains_address_get) | **GET** /v1/almanac/search/domains/{address} | Get Domains
[**get_recently_registered_agents_v1_almanac_recent_get**](AlmanacApi.md#get_recently_registered_agents_v1_almanac_recent_get) | **GET** /v1/almanac/recent | Get Recently Registered Agents
[**get_specific_agent_v1_almanac_agents_address_get**](AlmanacApi.md#get_specific_agent_v1_almanac_agents_address_get) | **GET** /v1/almanac/agents/{address} | Get Specific Agent
[**register_agent_v1_almanac_agents_post**](AlmanacApi.md#register_agent_v1_almanac_agents_post) | **POST** /v1/almanac/agents | Register Agent
[**register_agents_batch_v1_almanac_agents_batch_post**](AlmanacApi.md#register_agents_batch_v1_almanac_agents_batch_post) | **POST** /v1/almanac/agents/batch | Register Agents Batch
[**search_agents_v1_almanac_search_post**](AlmanacApi.md#search_agents_v1_almanac_search_post) | **POST** /v1/almanac/search | Search Agents
[**search_available_agent_name_v1_almanac_search_available_name_get**](AlmanacApi.md#search_available_agent_name_v1_almanac_search_available_name_get) | **GET** /v1/almanac/search/available_name | Search Available Agent Name
[**update_agent_status_v1_almanac_agents_agent_address_status_post**](AlmanacApi.md#update_agent_status_v1_almanac_agents_agent_address_status_post) | **POST** /v1/almanac/agents/{agent_address}/status | Update Agent Status


# **get_agents_by_domain_v1_almanac_search_agents_by_domain_domain_name_get**
> List[Agent] get_agents_by_domain_v1_almanac_search_agents_by_domain_domain_name_get(domain_name, network=network)

Get Agents By Domain

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
    api_instance = agentverse_client.almanac.AlmanacApi(api_client)
    domain_name = 'domain_name_example' # str | 
    network = 'testnet' # str |  (optional) (default to 'testnet')

    try:
        # Get Agents By Domain
        api_response = api_instance.get_agents_by_domain_v1_almanac_search_agents_by_domain_domain_name_get(domain_name, network=network)
        print("The response of AlmanacApi->get_agents_by_domain_v1_almanac_search_agents_by_domain_domain_name_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlmanacApi->get_agents_by_domain_v1_almanac_search_agents_by_domain_domain_name_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_name** | **str**|  | 
 **network** | **str**|  | [optional] [default to &#39;testnet&#39;]

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_domain_details_v1_almanac_search_domain_details_domain_name_get**
> List[DomainDetails] get_domain_details_v1_almanac_search_domain_details_domain_name_get(domain_name, network=network)

Get Domain Details

### Example


```python
import agentverse_client.almanac
from agentverse_client.almanac.models.domain_details import DomainDetails
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
    api_instance = agentverse_client.almanac.AlmanacApi(api_client)
    domain_name = 'domain_name_example' # str | 
    network = 'testnet' # str |  (optional) (default to 'testnet')

    try:
        # Get Domain Details
        api_response = api_instance.get_domain_details_v1_almanac_search_domain_details_domain_name_get(domain_name, network=network)
        print("The response of AlmanacApi->get_domain_details_v1_almanac_search_domain_details_domain_name_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlmanacApi->get_domain_details_v1_almanac_search_domain_details_domain_name_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_name** | **str**|  | 
 **network** | **str**|  | [optional] [default to &#39;testnet&#39;]

### Return type

[**List[DomainDetails]**](DomainDetails.md)

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

# **get_domain_record_v1_almanac_domains_domain_get**
> DomainRecord get_domain_record_v1_almanac_domains_domain_get(domain)

Get Domain Record

### Example


```python
import agentverse_client.almanac
from agentverse_client.almanac.models.domain_record import DomainRecord
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
    api_instance = agentverse_client.almanac.AlmanacApi(api_client)
    domain = 'domain_example' # str | 

    try:
        # Get Domain Record
        api_response = api_instance.get_domain_record_v1_almanac_domains_domain_get(domain)
        print("The response of AlmanacApi->get_domain_record_v1_almanac_domains_domain_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlmanacApi->get_domain_record_v1_almanac_domains_domain_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**|  | 

### Return type

[**DomainRecord**](DomainRecord.md)

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

# **get_domains_v1_almanac_search_domains_address_get**
> List[DomainDetails] get_domains_v1_almanac_search_domains_address_get(address, network=network)

Get Domains

### Example


```python
import agentverse_client.almanac
from agentverse_client.almanac.models.domain_details import DomainDetails
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
    api_instance = agentverse_client.almanac.AlmanacApi(api_client)
    address = 'address_example' # str | 
    network = 'testnet' # str |  (optional) (default to 'testnet')

    try:
        # Get Domains
        api_response = api_instance.get_domains_v1_almanac_search_domains_address_get(address, network=network)
        print("The response of AlmanacApi->get_domains_v1_almanac_search_domains_address_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlmanacApi->get_domains_v1_almanac_search_domains_address_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**|  | 
 **network** | **str**|  | [optional] [default to &#39;testnet&#39;]

### Return type

[**List[DomainDetails]**](DomainDetails.md)

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

# **get_recently_registered_agents_v1_almanac_recent_get**
> List[Agent] get_recently_registered_agents_v1_almanac_recent_get()

Get Recently Registered Agents

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
    api_instance = agentverse_client.almanac.AlmanacApi(api_client)

    try:
        # Get Recently Registered Agents
        api_response = api_instance.get_recently_registered_agents_v1_almanac_recent_get()
        print("The response of AlmanacApi->get_recently_registered_agents_v1_almanac_recent_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlmanacApi->get_recently_registered_agents_v1_almanac_recent_get: %s\n" % e)
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

# **get_specific_agent_v1_almanac_agents_address_get**
> object get_specific_agent_v1_almanac_agents_address_get(address)

Get Specific Agent

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
    api_instance = agentverse_client.almanac.AlmanacApi(api_client)
    address = 'address_example' # str | 

    try:
        # Get Specific Agent
        api_response = api_instance.get_specific_agent_v1_almanac_agents_address_get(address)
        print("The response of AlmanacApi->get_specific_agent_v1_almanac_agents_address_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlmanacApi->get_specific_agent_v1_almanac_agents_address_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**|  | 

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

# **register_agent_v1_almanac_agents_post**
> object register_agent_v1_almanac_agents_post(agent_registration_attestation)

Register Agent

### Example


```python
import agentverse_client.almanac
from agentverse_client.almanac.models.agent_registration_attestation import AgentRegistrationAttestation
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
    api_instance = agentverse_client.almanac.AlmanacApi(api_client)
    agent_registration_attestation = agentverse_client.almanac.AgentRegistrationAttestation() # AgentRegistrationAttestation | 

    try:
        # Register Agent
        api_response = api_instance.register_agent_v1_almanac_agents_post(agent_registration_attestation)
        print("The response of AlmanacApi->register_agent_v1_almanac_agents_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlmanacApi->register_agent_v1_almanac_agents_post: %s\n" % e)
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
import agentverse_client.almanac
from agentverse_client.almanac.models.agent_registration_attestation_batch import AgentRegistrationAttestationBatch
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
    api_instance = agentverse_client.almanac.AlmanacApi(api_client)
    agent_registration_attestation_batch = agentverse_client.almanac.AgentRegistrationAttestationBatch() # AgentRegistrationAttestationBatch | 

    try:
        # Register Agents Batch
        api_response = api_instance.register_agents_batch_v1_almanac_agents_batch_post(agent_registration_attestation_batch)
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

# **search_agents_v1_almanac_search_post**
> ResponseSearchAgentsV1AlmanacSearchPost search_agents_v1_almanac_search_post(agent_search, page_num=page_num)

Search Agents

### Example


```python
import agentverse_client.almanac
from agentverse_client.almanac.models.agent_search import AgentSearch
from agentverse_client.almanac.models.response_search_agents_v1_almanac_search_post import ResponseSearchAgentsV1AlmanacSearchPost
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
    api_instance = agentverse_client.almanac.AlmanacApi(api_client)
    agent_search = agentverse_client.almanac.AgentSearch() # AgentSearch | 
    page_num = 56 # int |  (optional)

    try:
        # Search Agents
        api_response = api_instance.search_agents_v1_almanac_search_post(agent_search, page_num=page_num)
        print("The response of AlmanacApi->search_agents_v1_almanac_search_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlmanacApi->search_agents_v1_almanac_search_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_search** | [**AgentSearch**](AgentSearch.md)|  | 
 **page_num** | **int**|  | [optional] 

### Return type

[**ResponseSearchAgentsV1AlmanacSearchPost**](ResponseSearchAgentsV1AlmanacSearchPost.md)

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

# **search_available_agent_name_v1_almanac_search_available_name_get**
> List[AgentNameAvailability] search_available_agent_name_v1_almanac_search_available_name_get(name_prefix, network=network)

Search Available Agent Name

### Example


```python
import agentverse_client.almanac
from agentverse_client.almanac.models.agent_name_availability import AgentNameAvailability
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
    api_instance = agentverse_client.almanac.AlmanacApi(api_client)
    name_prefix = 'name_prefix_example' # str | 
    network = 'testnet' # str |  (optional) (default to 'testnet')

    try:
        # Search Available Agent Name
        api_response = api_instance.search_available_agent_name_v1_almanac_search_available_name_get(name_prefix, network=network)
        print("The response of AlmanacApi->search_available_agent_name_v1_almanac_search_available_name_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlmanacApi->search_available_agent_name_v1_almanac_search_available_name_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name_prefix** | **str**|  | 
 **network** | **str**|  | [optional] [default to &#39;testnet&#39;]

### Return type

[**List[AgentNameAvailability]**](AgentNameAvailability.md)

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

# **update_agent_status_v1_almanac_agents_agent_address_status_post**
> object update_agent_status_v1_almanac_agents_agent_address_status_post(agent_address, agent_status_update)

Update Agent Status

### Example


```python
import agentverse_client.almanac
from agentverse_client.almanac.models.agent_status_update import AgentStatusUpdate
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
    api_instance = agentverse_client.almanac.AlmanacApi(api_client)
    agent_address = 'agent_address_example' # str | 
    agent_status_update = agentverse_client.almanac.AgentStatusUpdate() # AgentStatusUpdate | 

    try:
        # Update Agent Status
        api_response = api_instance.update_agent_status_v1_almanac_agents_agent_address_status_post(agent_address, agent_status_update)
        print("The response of AlmanacApi->update_agent_status_v1_almanac_agents_agent_address_status_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlmanacApi->update_agent_status_v1_almanac_agents_agent_address_status_post: %s\n" % e)
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

