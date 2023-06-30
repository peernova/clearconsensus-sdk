# openapi_client.DescriptorServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**descriptor_service_add_descriptor**](DescriptorServiceApi.md#descriptor_service_add_descriptor) | **POST** /api/v1/descriptor/add | AddDescriptor is used to add specific descriptor with specific definition to the system. Regular users can store a descriptor within their own scope, and any attempts to push it to a different scope will be declined. Back office users can store descriptors in any scope, provided that a scope key is provided. The name of the descriptor must match the name of the asset class to be mapped correctly. If a descriptor with the same name already exists, it will be updated.
[**descriptor_service_descriptor_dependencies**](DescriptorServiceApi.md#descriptor_service_descriptor_dependencies) | **POST** /api/v1/descriptor/dependencies | 
[**descriptor_service_disable_descriptor**](DescriptorServiceApi.md#descriptor_service_disable_descriptor) | **POST** /api/v1/descriptor/disable | DisableDescriptor is used to disable specific descriptor. Example of response : {    \&quot;data\&quot;: {        \&quot;uid\&quot;: \&quot;\&quot;,        \&quot;name\&quot;: \&quot;foreign_exchange-vanilla-forwards\&quot;    } }
[**descriptor_service_enable_descriptor**](DescriptorServiceApi.md#descriptor_service_enable_descriptor) | **POST** /api/v1/descriptor/enable | EnableDescriptor is used to enable specific descriptor.
[**descriptor_service_get_descriptor**](DescriptorServiceApi.md#descriptor_service_get_descriptor) | **POST** /api/v1/descriptor/get | GetDescriptor is used to get specific descriptor definition based on get definition. Regular users can retrieve only their own descriptors and descriptors associated with asset classes. Back office users can retrieve any of the existing descriptors.
[**descriptor_service_get_descriptor_version**](DescriptorServiceApi.md#descriptor_service_get_descriptor_version) | **GET** /api/v1/descriptor/version/{scope}/{name}/{versionId} | GetDescriptorVersion returns current version of the specific descriptor.
[**descriptor_service_list_descriptor_versions**](DescriptorServiceApi.md#descriptor_service_list_descriptor_versions) | **POST** /api/v1/descriptor/versions | ListDescriptorVersions returns list of version of the specific descriptor versions.
[**descriptor_service_list_descriptors**](DescriptorServiceApi.md#descriptor_service_list_descriptors) | **POST** /api/v1/descriptor/list | ListDescriptors returns list of specific descriptors according to request.


# **descriptor_service_add_descriptor**
> TitaniumAcknowledgeResponse descriptor_service_add_descriptor(body)

AddDescriptor is used to add specific descriptor with specific definition to the system. Regular users can store a descriptor within their own scope, and any attempts to push it to a different scope will be declined. Back office users can store descriptors in any scope, provided that a scope key is provided. The name of the descriptor must match the name of the asset class to be mapped correctly. If a descriptor with the same name already exists, it will be updated.

Example of request for regular user : {   \"name\":\"foreign_exchange-vanilla-forwards\",   \"fields\":[      { [data]=\"typeEnumToDisplayName[cellData]\"v        \"name\":\"submission_date\",         \"nullable\":true,         \"type\":\"string\"      },      {         \"name\":\"submission_asset\",         \"nullable\":true,         \"type\":\"string\"      }   ] }  Example of request for Back Office : {   \"name\":\"foreign_exchange-vanilla-forwards\",   \"scope\": \"global\",   \"fields\":[      {         \"name\":\"snap_date\",         \"alias\":\"snap_date\",         \"type\":\"date\",         \"options\":{            \"format\":\"MM/dd/yy\"         }      },      {         \"name\":\"asset\",         \"alias\":\"asset\",         \"type\":\"string\"      },      {        \"name\": \"sub-asset\",        \"alias\": \"sub-asset\",        \"type\": \"string\"      }   ] }  Example of response : {   \"data\":{      \"uid\":\"98fd0526-cc88-11ec-b784-0fe7a41b45e0\",      \"name\":\"foreign_exchange-vanilla-forwards\"   } }  Example of error response : {   \"error\":{      \"code\":70,      \"message\":\"Can't add descriptor: [com.peernova.api.searchmetadata.metadata.exceptions.MetaDataServiceException: Namespace [bank11] is not valid].\"   } }

### Example


```python
import time
import openapi_client
from openapi_client.api import descriptor_service_api
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_descriptor_definition import TitaniumDescriptorDefinition
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
    api_instance = descriptor_service_api.DescriptorServiceApi(api_client)
    body = TitaniumDescriptorDefinition(
        fields=[
            TitaniumDescriptorField(
                alias="alias_example",
                name="name_example",
                nullable=True,
                options={},
                type="type_example",
            ),
        ],
        name="name_example",
        options={},
        scope="scope_example",
    ) # TitaniumDescriptorDefinition | 

    # example passing only required values which don't have defaults set
    try:
        # AddDescriptor is used to add specific descriptor with specific definition to the system. Regular users can store a descriptor within their own scope, and any attempts to push it to a different scope will be declined. Back office users can store descriptors in any scope, provided that a scope key is provided. The name of the descriptor must match the name of the asset class to be mapped correctly. If a descriptor with the same name already exists, it will be updated.
        api_response = api_instance.descriptor_service_add_descriptor(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DescriptorServiceApi->descriptor_service_add_descriptor: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumDescriptorDefinition**](TitaniumDescriptorDefinition.md)|  |

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

# **descriptor_service_descriptor_dependencies**
> TitaniumDescriptorDependenciesResponse descriptor_service_descriptor_dependencies(body)



### Example


```python
import time
import openapi_client
from openapi_client.api import descriptor_service_api
from openapi_client.model.titanium_get_definition import TitaniumGetDefinition
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_descriptor_dependencies_response import TitaniumDescriptorDependenciesResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = descriptor_service_api.DescriptorServiceApi(api_client)
    body = TitaniumGetDefinition(
        descriptor_name="descriptor_name_example",
        identifier=TitaniumIdentifier(
            name="name_example",
            uid="uid_example",
        ),
        scope="scope_example",
    ) # TitaniumGetDefinition | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.descriptor_service_descriptor_dependencies(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DescriptorServiceApi->descriptor_service_descriptor_dependencies: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumGetDefinition**](TitaniumGetDefinition.md)|  |

### Return type

[**TitaniumDescriptorDependenciesResponse**](TitaniumDescriptorDependenciesResponse.md)

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

# **descriptor_service_disable_descriptor**
> TitaniumAcknowledgeResponse descriptor_service_disable_descriptor(body)

DisableDescriptor is used to disable specific descriptor. Example of response : {    \"data\": {        \"uid\": \"\",        \"name\": \"foreign_exchange-vanilla-forwards\"    } }

### Example


```python
import time
import openapi_client
from openapi_client.api import descriptor_service_api
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_enable_disable_request import TitaniumEnableDisableRequest
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
    api_instance = descriptor_service_api.DescriptorServiceApi(api_client)
    body = TitaniumEnableDisableRequest(
        name="name_example",
        scope="scope_example",
    ) # TitaniumEnableDisableRequest | 

    # example passing only required values which don't have defaults set
    try:
        # DisableDescriptor is used to disable specific descriptor. Example of response : {    \"data\": {        \"uid\": \"\",        \"name\": \"foreign_exchange-vanilla-forwards\"    } }
        api_response = api_instance.descriptor_service_disable_descriptor(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DescriptorServiceApi->descriptor_service_disable_descriptor: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumEnableDisableRequest**](TitaniumEnableDisableRequest.md)|  |

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

# **descriptor_service_enable_descriptor**
> TitaniumAcknowledgeResponse descriptor_service_enable_descriptor(body)

EnableDescriptor is used to enable specific descriptor.

Example of request : {  \"name\" : \"foreign_exchange-vanilla-forwards\",  \"scope\": \"global\" }  Example of response : {    \"data\": {        \"uid\": \"\",        \"name\": \"foreign_exchange-vanilla-forwards\"    } }

### Example


```python
import time
import openapi_client
from openapi_client.api import descriptor_service_api
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_enable_disable_request import TitaniumEnableDisableRequest
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
    api_instance = descriptor_service_api.DescriptorServiceApi(api_client)
    body = TitaniumEnableDisableRequest(
        name="name_example",
        scope="scope_example",
    ) # TitaniumEnableDisableRequest | 

    # example passing only required values which don't have defaults set
    try:
        # EnableDescriptor is used to enable specific descriptor.
        api_response = api_instance.descriptor_service_enable_descriptor(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DescriptorServiceApi->descriptor_service_enable_descriptor: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumEnableDisableRequest**](TitaniumEnableDisableRequest.md)|  |

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

# **descriptor_service_get_descriptor**
> TitaniumDescriptorDefinitionResponse descriptor_service_get_descriptor(body)

GetDescriptor is used to get specific descriptor definition based on get definition. Regular users can retrieve only their own descriptors and descriptors associated with asset classes. Back office users can retrieve any of the existing descriptors.

Example of request : {   \"identifier\":{      \"name\":\"foreign_exchange-vanilla-forwards\"   },   \"scope\":\"global\" }  Example of response : {    \"data\": \"{\\\"name\\\":\\\"foreign_exchange-vanilla-forwards\\\",\\\"fields\\\":[{\\\"name\\\":\\\"snap_date\\\",\\\"type\\\":\\\"date\\\",\\\"options\\\":{\\\"format\\\":\\\"MM/dd/yy\\\"},\\\"alias\\\":\\\"snap_date\\\"},{\\\"name\\\":\\\"asset\\\",\\\"type\\\":\\\"string\\\",\\\"alias\\\":\\\"asset\\\"},{\\\"name\\\":\\\"sub-asset\\\",\\\"type\\\":\\\"string\\\",\\\"alias\\\":\\\"sub-asset\\\"},{\\\"name\\\":\\\"service\\\",\\\"type\\\":\\\"string\\\",\\\"nullable\\\":true,\\\"alias\\\":\\\"service\\\"},{\\\"name\\\":\\\"snap_time\\\",\\\"type\\\":\\\"string\\\",\\\"alias\\\":\\\"snap_time\\\"},{\\\"name\\\":\\\"curr_1\\\",\\\"type\\\":\\\"string\\\",\\\"alias\\\":\\\"curr_1\\\"},{\\\"name\\\":\\\"curr_2\\\",\\\"type\\\":\\\"string\\\",\\\"alias\\\":\\\"curr_2\\\"},{\\\"name\\\":\\\"onshore_offshore_curr_1\\\",\\\"type\\\":\\\"string\\\",\\\"nullable\\\":true,\\\"alias\\\":\\\"onshore_offshore_curr_1\\\"},{\\\"name\\\":\\\"onshore_offshore_curr_2\\\",\\\"type\\\":\\\"string\\\",\\\"nullable\\\":true,\\\"alias\\\":\\\"onshore_offshore_curr_2\\\"},{\\\"name\\\":\\\"instrument_type\\\",\\\"type\\\":\\\"string\\\",\\\"alias\\\":\\\"instrument_type\\\"},{\\\"name\\\":\\\"tenor\\\",\\\"type\\\":\\\"string\\\",\\\"nullable\\\":true,\\\"alias\\\":\\\"tenor\\\"},{\\\"name\\\":\\\"value_source\\\",\\\"type\\\":\\\"string\\\",\\\"nullable\\\":true,\\\"alias\\\":\\\"value_source\\\"},{\\\"name\\\":\\\"fwrd_conversion_factor\\\",\\\"type\\\":\\\"double\\\",\\\"nullable\\\":true,\\\"alias\\\":\\\"fwrd_conversion_factor\\\"},{\\\"name\\\":\\\"mid_fwrd_outright\\\",\\\"type\\\":\\\"double\\\",\\\"nullable\\\":true,\\\"alias\\\":\\\"mid_fwrd_outright\\\"},{\\\"name\\\":\\\"value_source_ref_id\\\",\\\"type\\\":\\\"string\\\",\\\"nullable\\\":true,\\\"alias\\\":\\\"value_source_ref_id\\\"},{\\\"name\\\":\\\"client\\\",\\\"type\\\":\\\"string\\\",\\\"alias\\\":\\\"client\\\"},{\\\"name\\\":\\\"spot_reference_price\\\",\\\"type\\\":\\\"double\\\",\\\"nullable\\\":true,\\\"alias\\\":\\\"spot_reference_price\\\"},{\\\"name\\\":\\\"mid_fwrd_points\\\",\\\"type\\\":\\\"double\\\",\\\"alias\\\":\\\"mid_fwrd_points\\\"}]}\" }  Example of error response : {    \"error\": {        \"code\": 70,        \"message\": \"Can't get descriptor: [[foreign_exchange-vanilla-forwards1] of service [DESCRIPTOR] does not exist in namespace [global]].\"    } }

### Example


```python
import time
import openapi_client
from openapi_client.api import descriptor_service_api
from openapi_client.model.titanium_descriptor_definition_response import TitaniumDescriptorDefinitionResponse
from openapi_client.model.titanium_get_definition import TitaniumGetDefinition
from openapi_client.model.rpc_status import RpcStatus
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = descriptor_service_api.DescriptorServiceApi(api_client)
    body = TitaniumGetDefinition(
        descriptor_name="descriptor_name_example",
        identifier=TitaniumIdentifier(
            name="name_example",
            uid="uid_example",
        ),
        scope="scope_example",
    ) # TitaniumGetDefinition | 

    # example passing only required values which don't have defaults set
    try:
        # GetDescriptor is used to get specific descriptor definition based on get definition. Regular users can retrieve only their own descriptors and descriptors associated with asset classes. Back office users can retrieve any of the existing descriptors.
        api_response = api_instance.descriptor_service_get_descriptor(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DescriptorServiceApi->descriptor_service_get_descriptor: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumGetDefinition**](TitaniumGetDefinition.md)|  |

### Return type

[**TitaniumDescriptorDefinitionResponse**](TitaniumDescriptorDefinitionResponse.md)

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

# **descriptor_service_get_descriptor_version**
> TitaniumDescriptorDefinitionResponse descriptor_service_get_descriptor_version(scope, name, version_id)

GetDescriptorVersion returns current version of the specific descriptor.

Example of response : { \"data\":\"{\\\"name\\\":\\\"fx_test_for_bank1\\\",\\\"fields\\\":[{\\\"name\\\":\\\"submission_date\\\",\\\"type\\\":\\\"date\\\",\\\"options\\\":{\\\"format\\\":\\\"MM/dd/yyyy\\\"},\\\"alias\\\":\\\"date12\\\"},{\\\"name\\\":\\\"submission_asset\\\",\\\"type\\\":\\\"string\\\",\\\"nullable\\\":true}],\\\"options\\\":{\\\"DEDUPLICATION\\\":{\\\"GROUP_BY\\\":[\\\"submission_date\\\",\\\"submission_asset\\\"]}}}\" }

### Example


```python
import time
import openapi_client
from openapi_client.api import descriptor_service_api
from openapi_client.model.titanium_descriptor_definition_response import TitaniumDescriptorDefinitionResponse
from openapi_client.model.rpc_status import RpcStatus
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = descriptor_service_api.DescriptorServiceApi(api_client)
    scope = "scope_example" # str | 
    name = "name_example" # str | 
    version_id = "versionId_example" # str | 
    descriptor_name = "descriptorName_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # GetDescriptorVersion returns current version of the specific descriptor.
        api_response = api_instance.descriptor_service_get_descriptor_version(scope, name, version_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DescriptorServiceApi->descriptor_service_get_descriptor_version: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # GetDescriptorVersion returns current version of the specific descriptor.
        api_response = api_instance.descriptor_service_get_descriptor_version(scope, name, version_id, descriptor_name=descriptor_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DescriptorServiceApi->descriptor_service_get_descriptor_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**|  |
 **name** | **str**|  |
 **version_id** | **str**|  |
 **descriptor_name** | **str**|  | [optional]

### Return type

[**TitaniumDescriptorDefinitionResponse**](TitaniumDescriptorDefinitionResponse.md)

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

# **descriptor_service_list_descriptor_versions**
> TitaniumListVersionResponse descriptor_service_list_descriptor_versions(body)

ListDescriptorVersions returns list of version of the specific descriptor versions.

Example of request : {   \"scope\":\"global\",   \"identifier\":{      \"name\":\"foreign_exchange-vanilla-forwards\"   } }  Example of response : {    \"data\": {        \"versions\": [            {                \"versionId\": \"fM9AukEqTJXKOcbW_tQ7Sfr4Clp5qinKq_liXZYzyiI=\",                \"createdAt\": \"2022-06-14 10:57:42.0\"            },            {                \"versionId\": \"LmVlkPbnsUKFBw8qIbUHEzBsRrcnG_BSMnopA5Ptd7I=\",                \"createdAt\": \"2022-06-14 10:20:48.0\"            }        ]    } }

### Example


```python
import time
import openapi_client
from openapi_client.api import descriptor_service_api
from openapi_client.model.titanium_get_definition import TitaniumGetDefinition
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_list_version_response import TitaniumListVersionResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = descriptor_service_api.DescriptorServiceApi(api_client)
    body = TitaniumGetDefinition(
        descriptor_name="descriptor_name_example",
        identifier=TitaniumIdentifier(
            name="name_example",
            uid="uid_example",
        ),
        scope="scope_example",
    ) # TitaniumGetDefinition | 

    # example passing only required values which don't have defaults set
    try:
        # ListDescriptorVersions returns list of version of the specific descriptor versions.
        api_response = api_instance.descriptor_service_list_descriptor_versions(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DescriptorServiceApi->descriptor_service_list_descriptor_versions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumGetDefinition**](TitaniumGetDefinition.md)|  |

### Return type

[**TitaniumListVersionResponse**](TitaniumListVersionResponse.md)

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

# **descriptor_service_list_descriptors**
> TitaniumDescriptorList descriptor_service_list_descriptors(body)

ListDescriptors returns list of specific descriptors according to request.

Example of request : {   \"scope\":\"global\" }  Example of response : {    \"data\": {        \"results\": [            {                \"uid\": \"\",                \"name\": \"foreign_exchange-vanilla-options\"            },            {                \"uid\": \"\",                \"name\": \"foreign_exchange-exotics-barriers_and_digitals\"            },            {                \"uid\": \"\",                \"name\": \"foreign_exchange-exotics-tarfs\"            }        ]    } }

### Example


```python
import time
import openapi_client
from openapi_client.api import descriptor_service_api
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_descriptor_list import TitaniumDescriptorList
from openapi_client.model.titanium_list_request import TitaniumListRequest
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = descriptor_service_api.DescriptorServiceApi(api_client)
    body = TitaniumListRequest(
        filter="filter_example",
        limit=TitaniumLimit(
            value=1,
        ),
        offset=1,
        order_by=TitaniumOrderBy(
            column="column_example",
            order="order_example",
        ),
        scope="scope_example",
    ) # TitaniumListRequest | 

    # example passing only required values which don't have defaults set
    try:
        # ListDescriptors returns list of specific descriptors according to request.
        api_response = api_instance.descriptor_service_list_descriptors(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DescriptorServiceApi->descriptor_service_list_descriptors: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumListRequest**](TitaniumListRequest.md)|  |

### Return type

[**TitaniumDescriptorList**](TitaniumDescriptorList.md)

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

