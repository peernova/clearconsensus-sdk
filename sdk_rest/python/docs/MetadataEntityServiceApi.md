# openapi_client.MetadataEntityServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**metadata_entity_service_add_entity**](MetadataEntityServiceApi.md#metadata_entity_service_add_entity) | **POST** /api/v1/entity/add | 
[**metadata_entity_service_disable_entity**](MetadataEntityServiceApi.md#metadata_entity_service_disable_entity) | **POST** /api/v1/entity/disable | 
[**metadata_entity_service_enable_entity**](MetadataEntityServiceApi.md#metadata_entity_service_enable_entity) | **POST** /api/v1/entity/enable | 
[**metadata_entity_service_get_entity**](MetadataEntityServiceApi.md#metadata_entity_service_get_entity) | **POST** /api/v1/entity/get | 


# **metadata_entity_service_add_entity**
> TitaniumAcknowledgeResponse metadata_entity_service_add_entity(body)



### Example


```python
import time
import openapi_client
from openapi_client.api import metadata_entity_service_api
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_entity_definition import TitaniumEntityDefinition
from openapi_client.model.titanium_acknowledge_response import TitaniumAcknowledgeResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = metadata_entity_service_api.MetadataEntityServiceApi(api_client)
    body = TitaniumEntityDefinition(
        definition="definition_example",
        name="name_example",
        scope="scope_example",
        type="type_example",
    ) # TitaniumEntityDefinition | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.metadata_entity_service_add_entity(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MetadataEntityServiceApi->metadata_entity_service_add_entity: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumEntityDefinition**](TitaniumEntityDefinition.md)|  |

### Return type

[**TitaniumAcknowledgeResponse**](TitaniumAcknowledgeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metadata_entity_service_disable_entity**
> TitaniumAcknowledgeResponse metadata_entity_service_disable_entity(body)



### Example


```python
import time
import openapi_client
from openapi_client.api import metadata_entity_service_api
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_entity_identifier import TitaniumEntityIdentifier
from openapi_client.model.titanium_acknowledge_response import TitaniumAcknowledgeResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = metadata_entity_service_api.MetadataEntityServiceApi(api_client)
    body = TitaniumEntityIdentifier(
        identifier=TitaniumIdentifier(
            name="name_example",
            uid="uid_example",
        ),
        scope="scope_example",
        type="type_example",
    ) # TitaniumEntityIdentifier | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.metadata_entity_service_disable_entity(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MetadataEntityServiceApi->metadata_entity_service_disable_entity: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumEntityIdentifier**](TitaniumEntityIdentifier.md)|  |

### Return type

[**TitaniumAcknowledgeResponse**](TitaniumAcknowledgeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metadata_entity_service_enable_entity**
> TitaniumAcknowledgeResponse metadata_entity_service_enable_entity(body)



### Example


```python
import time
import openapi_client
from openapi_client.api import metadata_entity_service_api
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_entity_identifier import TitaniumEntityIdentifier
from openapi_client.model.titanium_acknowledge_response import TitaniumAcknowledgeResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = metadata_entity_service_api.MetadataEntityServiceApi(api_client)
    body = TitaniumEntityIdentifier(
        identifier=TitaniumIdentifier(
            name="name_example",
            uid="uid_example",
        ),
        scope="scope_example",
        type="type_example",
    ) # TitaniumEntityIdentifier | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.metadata_entity_service_enable_entity(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MetadataEntityServiceApi->metadata_entity_service_enable_entity: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumEntityIdentifier**](TitaniumEntityIdentifier.md)|  |

### Return type

[**TitaniumAcknowledgeResponse**](TitaniumAcknowledgeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metadata_entity_service_get_entity**
> TitaniumEntityDefinition metadata_entity_service_get_entity(body)



### Example


```python
import time
import openapi_client
from openapi_client.api import metadata_entity_service_api
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_entity_definition import TitaniumEntityDefinition
from openapi_client.model.titanium_entity_identifier import TitaniumEntityIdentifier
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = metadata_entity_service_api.MetadataEntityServiceApi(api_client)
    body = TitaniumEntityIdentifier(
        identifier=TitaniumIdentifier(
            name="name_example",
            uid="uid_example",
        ),
        scope="scope_example",
        type="type_example",
    ) # TitaniumEntityIdentifier | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.metadata_entity_service_get_entity(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MetadataEntityServiceApi->metadata_entity_service_get_entity: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumEntityIdentifier**](TitaniumEntityIdentifier.md)|  |

### Return type

[**TitaniumEntityDefinition**](TitaniumEntityDefinition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

