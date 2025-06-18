# agentverse_client.mailbox.aio.AuthApi

All URIs are relative to *https://agentverse.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**register_agent**](AuthApi.md#register_agent) | **POST** /v1/agents | Register
[**request_challenge**](AuthApi.md#request_challenge) | **POST** /v1/auth/challenge | Handle Challenge Request
[**submit_proof**](AuthApi.md#submit_proof) | **POST** /v1/auth/prove | Submit Proof


# **register_agent**
> RegistrationResponse register_agent(registration_request)

Register

### Example

* OAuth Authentication (FaunaAuthorizationScheme):

```python
import agentverse_client.mailbox.aio
from agentverse_client.mailbox.aio.models.registration_request import RegistrationRequest
from agentverse_client.mailbox.aio.models.registration_response import RegistrationResponse
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
    api_instance = agentverse_client.mailbox.aio.AuthApi(api_client)
    registration_request = agentverse_client.mailbox.aio.RegistrationRequest() # RegistrationRequest | 

    try:
        # Register
        api_response = await api_instance.register_agent(registration_request)
        print("The response of AuthApi->register_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->register_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_request** | [**RegistrationRequest**](RegistrationRequest.md)|  | 

### Return type

[**RegistrationResponse**](RegistrationResponse.md)

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

# **request_challenge**
> ChallengeResponse request_challenge(challenge_request)

Handle Challenge Request

### Example


```python
import agentverse_client.mailbox.aio
from agentverse_client.mailbox.aio.models.challenge_request import ChallengeRequest
from agentverse_client.mailbox.aio.models.challenge_response import ChallengeResponse
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
    api_instance = agentverse_client.mailbox.aio.AuthApi(api_client)
    challenge_request = agentverse_client.mailbox.aio.ChallengeRequest() # ChallengeRequest | 

    try:
        # Handle Challenge Request
        api_response = await api_instance.request_challenge(challenge_request)
        print("The response of AuthApi->request_challenge:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->request_challenge: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **challenge_request** | [**ChallengeRequest**](ChallengeRequest.md)|  | 

### Return type

[**ChallengeResponse**](ChallengeResponse.md)

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

# **submit_proof**
> ProofResponse submit_proof(proof_request)

Submit Proof

### Example


```python
import agentverse_client.mailbox.aio
from agentverse_client.mailbox.aio.models.proof_request import ProofRequest
from agentverse_client.mailbox.aio.models.proof_response import ProofResponse
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
    api_instance = agentverse_client.mailbox.aio.AuthApi(api_client)
    proof_request = agentverse_client.mailbox.aio.ProofRequest() # ProofRequest | 

    try:
        # Submit Proof
        api_response = await api_instance.submit_proof(proof_request)
        print("The response of AuthApi->submit_proof:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->submit_proof: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proof_request** | [**ProofRequest**](ProofRequest.md)|  | 

### Return type

[**ProofResponse**](ProofResponse.md)

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

