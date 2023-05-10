# openapi_client.DbDescriptorServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**db_descriptor_service_add_db_descriptor**](DbDescriptorServiceApi.md#db_descriptor_service_add_db_descriptor) | **POST** /api/v1/db/descriptor/add | 
[**db_descriptor_service_disable_db_descriptor**](DbDescriptorServiceApi.md#db_descriptor_service_disable_db_descriptor) | **POST** /api/v1/db/descriptor/disable | 
[**db_descriptor_service_enable_db_descriptor**](DbDescriptorServiceApi.md#db_descriptor_service_enable_db_descriptor) | **POST** /api/v1/db/descriptor/enable | 
[**db_descriptor_service_get_db_descriptor**](DbDescriptorServiceApi.md#db_descriptor_service_get_db_descriptor) | **POST** /api/v1/db/descriptor/get | 
[**db_descriptor_service_get_db_descriptor_version**](DbDescriptorServiceApi.md#db_descriptor_service_get_db_descriptor_version) | **GET** /api/v1/db/descriptor/version/{name}/{versionId} | 
[**db_descriptor_service_list_db_descriptor_versions**](DbDescriptorServiceApi.md#db_descriptor_service_list_db_descriptor_versions) | **POST** /api/v1/db/descriptor/versions | 
[**db_descriptor_service_list_db_descriptors**](DbDescriptorServiceApi.md#db_descriptor_service_list_db_descriptors) | **POST** /api/v1/db/descriptor/list | 


# **db_descriptor_service_add_db_descriptor**
> TitaniumAcknowledgeResponse db_descriptor_service_add_db_descriptor(body)



### Example


```python
import time
import openapi_client
from openapi_client.api import db_descriptor_service_api
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
    api_instance = db_descriptor_service_api.DbDescriptorServiceApi(api_client)
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
        api_response = api_instance.db_descriptor_service_add_db_descriptor(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DbDescriptorServiceApi->db_descriptor_service_add_db_descriptor: %s\n" % e)
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

# **db_descriptor_service_disable_db_descriptor**
> TitaniumAcknowledgeResponse db_descriptor_service_disable_db_descriptor(body)



### Example


```python
import time
import openapi_client
from openapi_client.api import db_descriptor_service_api
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
    api_instance = db_descriptor_service_api.DbDescriptorServiceApi(api_client)
    body = TitaniumEnableDisableRequest(
        name="name_example",
        scope="scope_example",
    ) # TitaniumEnableDisableRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.db_descriptor_service_disable_db_descriptor(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DbDescriptorServiceApi->db_descriptor_service_disable_db_descriptor: %s\n" % e)
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

# **db_descriptor_service_enable_db_descriptor**
> TitaniumAcknowledgeResponse db_descriptor_service_enable_db_descriptor(body)



### Example


```python
import time
import openapi_client
from openapi_client.api import db_descriptor_service_api
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
    api_instance = db_descriptor_service_api.DbDescriptorServiceApi(api_client)
    body = TitaniumEnableDisableRequest(
        name="name_example",
        scope="scope_example",
    ) # TitaniumEnableDisableRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.db_descriptor_service_enable_db_descriptor(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DbDescriptorServiceApi->db_descriptor_service_enable_db_descriptor: %s\n" % e)
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

# **db_descriptor_service_get_db_descriptor**
> TitaniumDescriptorDefinitionResponse db_descriptor_service_get_db_descriptor(body)



### Example


```python
import time
import openapi_client
from openapi_client.api import db_descriptor_service_api
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
    api_instance = db_descriptor_service_api.DbDescriptorServiceApi(api_client)
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
        api_response = api_instance.db_descriptor_service_get_db_descriptor(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DbDescriptorServiceApi->db_descriptor_service_get_db_descriptor: %s\n" % e)
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

# **db_descriptor_service_get_db_descriptor_version**
> TitaniumDescriptorDefinitionResponse db_descriptor_service_get_db_descriptor_version(name, version_id)



### Example


```python
import time
import openapi_client
from openapi_client.api import db_descriptor_service_api
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
    api_instance = db_descriptor_service_api.DbDescriptorServiceApi(api_client)
    name = "name_example" # str | 
    version_id = "versionId_example" # str | 
    scope = "scope_example" # str |  (optional)
    descriptor_name = "descriptorName_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.db_descriptor_service_get_db_descriptor_version(name, version_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DbDescriptorServiceApi->db_descriptor_service_get_db_descriptor_version: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.db_descriptor_service_get_db_descriptor_version(name, version_id, scope=scope, descriptor_name=descriptor_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DbDescriptorServiceApi->db_descriptor_service_get_db_descriptor_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  |
 **version_id** | **str**|  |
 **scope** | **str**|  | [optional]
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

# **db_descriptor_service_list_db_descriptor_versions**
> TitaniumListVersionResponse db_descriptor_service_list_db_descriptor_versions(body)



### Example


```python
import time
import openapi_client
from openapi_client.api import db_descriptor_service_api
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
    api_instance = db_descriptor_service_api.DbDescriptorServiceApi(api_client)
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
        api_response = api_instance.db_descriptor_service_list_db_descriptor_versions(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DbDescriptorServiceApi->db_descriptor_service_list_db_descriptor_versions: %s\n" % e)
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

# **db_descriptor_service_list_db_descriptors**
> TitaniumDescriptorList db_descriptor_service_list_db_descriptors(body)



### Example


```python
import time
import openapi_client
from openapi_client.api import db_descriptor_service_api
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
    api_instance = db_descriptor_service_api.DbDescriptorServiceApi(api_client)
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
        api_response = api_instance.db_descriptor_service_list_db_descriptors(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DbDescriptorServiceApi->db_descriptor_service_list_db_descriptors: %s\n" % e)
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

