# hosting
  ## Overview  The Agent Hosting API helps users deploy agents to the cloud  ## Authentication  The entire API requires that the user authenticate with the ecosystem first before accessing the api 

The `agentverse_client.hosting` package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.1.0
- Package version: 1.0.0
- Generator version: 7.11.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.8+

## Installation & Usage

This python library package is generated without supporting files like setup.py or requirements files

To be able to use it, you will need these dependencies in your own package that uses this library:

* urllib3 >= 1.25.3, < 3.0.0
* python-dateutil >= 2.8.2
* pydantic >= 2
* typing-extensions >= 4.7.1

## Getting Started

In your own code, to use this library to connect and interact with hosting,
you can run the following:

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
    new_agent = agentverse_client.hosting.NewAgent() # NewAgent | 
    no_cache = False # bool |  (optional) (default to False)

    try:
        # Create New Team Agent
        api_response = api_instance.create_team_agent(slug, new_agent, no_cache=no_cache)
        print("The response of HostingApi->create_team_agent:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling HostingApi->create_team_agent: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*HostingApi* | [**create_team_agent**](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/HostingApi.md#create_team_agent) | **POST** /v1/hosting/teams/{slug}/agents | Create New Team Agent
*HostingApi* | [**create_team_agent_secret**](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/HostingApi.md#create_team_agent_secret) | **POST** /v1/hosting/teams/{slug}/secrets | Create Team Secret
*HostingApi* | [**create_user_agent**](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/HostingApi.md#create_user_agent) | **POST** /v1/hosting/agents | Create New User Agent
*HostingApi* | [**create_user_agent_secret**](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/HostingApi.md#create_user_agent_secret) | **POST** /v1/hosting/secrets | Create User Secret
*HostingApi* | [**delete_all_team_data**](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/HostingApi.md#delete_all_team_data) | **DELETE** /v1/hosting/teams/{slug}/remove-all-data | Delete All Team Data
*HostingApi* | [**delete_all_user_data**](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/HostingApi.md#delete_all_user_data) | **DELETE** /v1/hosting/remove-all-data | Delete All User Data
*HostingApi* | [**delete_logs_for_team_agent**](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/HostingApi.md#delete_logs_for_team_agent) | **DELETE** /v1/hosting/teams/{slug}/agents/{address}/logs | Delete Logs For Team Agent
*HostingApi* | [**delete_logs_for_user_agent**](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/HostingApi.md#delete_logs_for_user_agent) | **DELETE** /v1/hosting/agents/{address}/logs | Delete Logs For User Agent
*HostingApi* | [**delete_team_agent**](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/HostingApi.md#delete_team_agent) | **DELETE** /v1/hosting/teams/{slug}/agents/{address} | Delete Specific Team Agent
*HostingApi* | [**delete_team_agent_storage**](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/HostingApi.md#delete_team_agent_storage) | **DELETE** /v1/hosting/teams/{slug}/agents/{address}/storage/{key} | Delete Team Agent Storage
*HostingApi* | [**delete_team_secret**](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/HostingApi.md#delete_team_secret) | **DELETE** /v1/hosting/teams/{slug}/secrets/{address}/{name} | Delete User Secret
*HostingApi* | [**delete_user_agent**](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/HostingApi.md#delete_user_agent) | **DELETE** /v1/hosting/agents/{address} | Delete Specific User Agent
*HostingApi* | [**delete_user_agent_storage**](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/HostingApi.md#delete_user_agent_storage) | **DELETE** /v1/hosting/agents/{address}/storage/{key} | Delete User Agent Storage
*HostingApi* | [**delete_user_secret**](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/HostingApi.md#delete_user_secret) | **DELETE** /v1/hosting/secrets/{address}/{name} | Delete User Secret
*HostingApi* | [**duplicate_team_agent**](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/HostingApi.md#duplicate_team_agent) | **POST** /v1/hosting/teams/{slug}/agents/{address}/duplicate | Duplicate Specific Team Agent
*HostingApi* | [**duplicate_user_agent**](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/HostingApi.md#duplicate_user_agent) | **POST** /v1/hosting/agents/{address}/duplicate | Duplicate Specific User Agent
*HostingApi* | [**get_latest_logs_for_team_agent**](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/HostingApi.md#get_latest_logs_for_team_agent) | **GET** /v1/hosting/teams/{slug}/agents/{address}/logs/latest | Get Latest Logs For Team Agent
*HostingApi* | [**get_latest_logs_for_user_agent**](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/HostingApi.md#get_latest_logs_for_user_agent) | **GET** /v1/hosting/agents/{address}/logs/latest | Get Latest Logs For User Agent
*HostingApi* | [**get_new_achievements**](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/HostingApi.md#get_new_achievements) | **GET** /v1/hosting/achievements/new | Get New Achievements
*HostingApi* | [**get_supported_packages**](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/HostingApi.md#get_supported_packages) | **GET** /v1/hosting/packages | Get Supported Packages
*HostingApi* | [**get_team_agent_code**](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/HostingApi.md#get_team_agent_code) | **GET** /v1/hosting/teams/{slug}/agents/{address}/code | Get Team Agent Code
*HostingApi* | [**get_team_agent_details**](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/HostingApi.md#get_team_agent_details) | **GET** /v1/hosting/teams/{slug}/agents/{address} | Get Specific Teams Agent
*HostingApi* | [**get_team_agent_interactions**](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/HostingApi.md#get_team_agent_interactions) | **GET** /v1/hosting/teams/{slug}/agents/{address}/interactions | Get Agent Team Interactions
*HostingApi* | [**get_team_agent_metadata**](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/HostingApi.md#get_team_agent_metadata) | **GET** /v1/hosting/teams/{slug}/agents/{address}/metadata | Get Team Agent Metadata
*HostingApi* | [**get_team_agent_profile**](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/HostingApi.md#get_team_agent_profile) | **GET** /v1/hosting/teams/{slug}/agents/{address}/profile | Get Team Agent Public Profile
*HostingApi* | [**get_team_agent_secrets**](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/HostingApi.md#get_team_agent_secrets) | **GET** /v1/hosting/teams/{slug}/{address}/secrets | Get Team Agent Secrets
*HostingApi* | [**get_team_agent_storage**](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/HostingApi.md#get_team_agent_storage) | **GET** /v1/hosting/teams/{slug}/agents/{address}/storage | Get Team Agent Storage
*HostingApi* | [**get_team_agent_storage_by_key**](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/HostingApi.md#get_team_agent_storage_by_key) | **GET** /v1/hosting/teams/{slug}/agents/{address}/storage/{key} | Get Team Agent Storage By Key
*HostingApi* | [**get_unlocked_achievements**](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/HostingApi.md#get_unlocked_achievements) | **GET** /v1/hosting/achievements/unlocked | Get Unlocked Achievements
*HostingApi* | [**get_user_agent_code**](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/HostingApi.md#get_user_agent_code) | **GET** /v1/hosting/agents/{address}/code | Get User Agent Code
*HostingApi* | [**get_user_agent_details**](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/HostingApi.md#get_user_agent_details) | **GET** /v1/hosting/agents/{address} | Get Specific User Agent
*HostingApi* | [**get_user_agent_interactions**](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/HostingApi.md#get_user_agent_interactions) | **GET** /v1/hosting/agents/{address}/interactions | Get Agent User Interactions
*HostingApi* | [**get_user_agent_metadata**](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/HostingApi.md#get_user_agent_metadata) | **GET** /v1/hosting/agents/{address}/metadata | Get User Agent Metadata
*HostingApi* | [**get_user_agent_profile**](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/HostingApi.md#get_user_agent_profile) | **GET** /v1/hosting/agents/{address}/profile | Get User Agent Public Profile
*HostingApi* | [**get_user_agent_secrets**](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/HostingApi.md#get_user_agent_secrets) | **GET** /v1/hosting/{address}/secrets | Get User Agent Secrets
*HostingApi* | [**get_user_agent_storage**](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/HostingApi.md#get_user_agent_storage) | **GET** /v1/hosting/agents/{address}/storage | Get User Agent Storage
*HostingApi* | [**get_user_agent_storage_by_key**](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/HostingApi.md#get_user_agent_storage_by_key) | **GET** /v1/hosting/agents/{address}/storage/{key} | Get User Agent Storage By Key
*HostingApi* | [**get_user_secret**](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/HostingApi.md#get_user_secret) | **GET** /v1/hosting/teams/{slug}/secrets | Get User Secret
*HostingApi* | [**get_user_secrets**](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/HostingApi.md#get_user_secrets) | **GET** /v1/hosting/secrets | Get User Secret
*HostingApi* | [**list_team_agents**](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/HostingApi.md#list_team_agents) | **GET** /v1/hosting/teams/{slug}/agents | Get Team Agents
*HostingApi* | [**list_user_agents**](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/HostingApi.md#list_user_agents) | **GET** /v1/hosting/agents | Get User Agents
*HostingApi* | [**register_new_team_domain_name**](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/HostingApi.md#register_new_team_domain_name) | **POST** /v1/hosting/teams/{slug}/agents/{address}/domains/register | Register New Team Domain Name
*HostingApi* | [**register_new_user_domain_name**](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/HostingApi.md#register_new_user_domain_name) | **POST** /v1/hosting/agents/{address}/domains/register | Register New User Domain Name
*HostingApi* | [**start_specific_team_agent**](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/HostingApi.md#start_specific_team_agent) | **POST** /v1/hosting/teams/{slug}/agents/{address}/start | Start Specific Team Agent
*HostingApi* | [**start_specific_user_agent**](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/HostingApi.md#start_specific_user_agent) | **POST** /v1/hosting/agents/{address}/start | Start Specific User Agent
*HostingApi* | [**stop_specific_team_agent**](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/HostingApi.md#stop_specific_team_agent) | **POST** /v1/hosting/teams/{slug}/agents/{address}/stop | Stop Specific Team Agent
*HostingApi* | [**stop_specific_user_agent**](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/HostingApi.md#stop_specific_user_agent) | **POST** /v1/hosting/agents/{address}/stop | Stop Specific User Agent
*HostingApi* | [**update_team_agent**](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/HostingApi.md#update_team_agent) | **PUT** /v1/hosting/teams/{slug}/agents/{address} | Update Specific Team Agent
*HostingApi* | [**update_team_agent_code**](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/HostingApi.md#update_team_agent_code) | **PUT** /v1/hosting/teams/{slug}/agents/{address}/code | Update Team Agent Code
*HostingApi* | [**update_team_agent_metadata**](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/HostingApi.md#update_team_agent_metadata) | **PATCH** /v1/hosting/teams/{slug}/agents/{address}/metadata | Update Team Agent Metadata
*HostingApi* | [**update_team_agent_network**](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/HostingApi.md#update_team_agent_network) | **PUT** /v1/hosting/teams/{slug}/agents/{address}/network | Update Team Agent Network
*HostingApi* | [**update_team_agent_storage**](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/HostingApi.md#update_team_agent_storage) | **PUT** /v1/hosting/teams/{slug}/agents/{address}/storage/{key} | Update Team Agent Storage
*HostingApi* | [**update_user_agent**](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/HostingApi.md#update_user_agent) | **PUT** /v1/hosting/agents/{address} | Update Specific User Agent
*HostingApi* | [**update_user_agent_code**](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/HostingApi.md#update_user_agent_code) | **PUT** /v1/hosting/agents/{address}/code | Update User Agent Code
*HostingApi* | [**update_user_agent_metadata**](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/HostingApi.md#update_user_agent_metadata) | **PATCH** /v1/hosting/agents/{address}/metadata | Update User Agent Metadata
*HostingApi* | [**update_user_agent_network**](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/HostingApi.md#update_user_agent_network) | **PUT** /v1/hosting/agents/{address}/network | Update User Agent Network
*HostingApi* | [**update_user_agent_storage**](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/HostingApi.md#update_user_agent_storage) | **PUT** /v1/hosting/agents/{address}/storage/{key} | Update User Agent Storage


## Documentation For Models

 - [Agent](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/Agent.md)
 - [AgentCode](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/AgentCode.md)
 - [AgentCodeDigest](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/AgentCodeDigest.md)
 - [AgentLog](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/AgentLog.md)
 - [AgentMetadata](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/AgentMetadata.md)
 - [AgentMetadataUpdates](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/AgentMetadataUpdates.md)
 - [AgentNetwork](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/AgentNetwork.md)
 - [AgentSummary](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/AgentSummary.md)
 - [Envelope](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/Envelope.md)
 - [HTTPValidationError](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/HTTPValidationError.md)
 - [HistoricalInteractions](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/HistoricalInteractions.md)
 - [HostingQuotaSetEvent](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/HostingQuotaSetEvent.md)
 - [HostingQuotaTopUpEvent](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/HostingQuotaTopUpEvent.md)
 - [HostingQuotas](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/HostingQuotas.md)
 - [InteractionPeriod](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/InteractionPeriod.md)
 - [LocationInner](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/LocationInner.md)
 - [LogLevel](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/LogLevel.md)
 - [LogType](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/LogType.md)
 - [NewAgent](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/NewAgent.md)
 - [NewDomainName](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/NewDomainName.md)
 - [Packages](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/Packages.md)
 - [PublicAgent](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/PublicAgent.md)
 - [ResponseSubmitMessageEnvelope](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/ResponseSubmitMessageEnvelope.md)
 - [Secret](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/Secret.md)
 - [SecretCreate](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/SecretCreate.md)
 - [SecretList](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/SecretList.md)
 - [StorageItem](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/StorageItem.md)
 - [StorageItemUpdate](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/StorageItemUpdate.md)
 - [SubscriptionResponse](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/SubscriptionResponse.md)
 - [SupportedPackage](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/SupportedPackage.md)
 - [UpdateAgent](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/UpdateAgent.md)
 - [UpdateAgentCode](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/UpdateAgentCode.md)
 - [UpdateAgentNetwork](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/UpdateAgentNetwork.md)
 - [ValidationError](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/ValidationError.md)
 - [WithPaginationAgentSummary](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/WithPaginationAgentSummary.md)
 - [WithPaginationStorageItem](https://github.com/fetchai/api-clients/blob/main/agentverse-client/agentverse_client/hosting/docs/WithPaginationStorageItem.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="FaunaAuthorizationScheme"></a>
### FaunaAuthorizationScheme

- **Type**: OAuth
- **Flow**: accessCode
- **Authorization URL**: 
- **Scopes**: N/A


## Author




