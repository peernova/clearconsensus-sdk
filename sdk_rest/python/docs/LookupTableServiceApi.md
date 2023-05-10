# openapi_client.LookupTableServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lookup_table_service_add_lookup_table**](LookupTableServiceApi.md#lookup_table_service_add_lookup_table) | **POST** /api/v1/lookuptable/add | 
[**lookup_table_service_get_lookup_table**](LookupTableServiceApi.md#lookup_table_service_get_lookup_table) | **POST** /api/v1/lookuptable/get | 
[**lookup_table_service_list_lookup_table_versions**](LookupTableServiceApi.md#lookup_table_service_list_lookup_table_versions) | **POST** /api/v1/lookuptable/versions | 
[**lookup_table_service_list_lookup_tables**](LookupTableServiceApi.md#lookup_table_service_list_lookup_tables) | **POST** /api/v1/lookuptable/list | 


# **lookup_table_service_add_lookup_table**
> TitaniumAcknowledgeResponse lookup_table_service_add_lookup_table(body)



### Example


```python
import time
import openapi_client
from openapi_client.api import lookup_table_service_api
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_add_lookup_table_request import TitaniumAddLookupTableRequest
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
    api_instance = lookup_table_service_api.LookupTableServiceApi(api_client)
    body = TitaniumAddLookupTableRequest(
        lookuptable=TitaniumLookupTableDefinition(
            fields=[
                TitaniumLutField(
                    key=True,
                    name="name_example",
                    type="type_example",
                ),
            ],
            name="name_example",
            rows=[
                TitaniumLutEntry(
                    values=[
                        {},
                    ],
                ),
            ],
            total_records=1,
            type="type_example",
        ),
        scope="scope_example",
    ) # TitaniumAddLookupTableRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.lookup_table_service_add_lookup_table(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LookupTableServiceApi->lookup_table_service_add_lookup_table: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumAddLookupTableRequest**](TitaniumAddLookupTableRequest.md)|  |

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

# **lookup_table_service_get_lookup_table**
> TitaniumGetLookupTableResponse lookup_table_service_get_lookup_table(body)



### Example


```python
import time
import openapi_client
from openapi_client.api import lookup_table_service_api
from openapi_client.model.titanium_get_definition import TitaniumGetDefinition
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_get_lookup_table_response import TitaniumGetLookupTableResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = lookup_table_service_api.LookupTableServiceApi(api_client)
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
        api_response = api_instance.lookup_table_service_get_lookup_table(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LookupTableServiceApi->lookup_table_service_get_lookup_table: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumGetDefinition**](TitaniumGetDefinition.md)|  |

### Return type

[**TitaniumGetLookupTableResponse**](TitaniumGetLookupTableResponse.md)

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

# **lookup_table_service_list_lookup_table_versions**
> TitaniumListVersionResponse lookup_table_service_list_lookup_table_versions(body)



### Example


```python
import time
import openapi_client
from openapi_client.api import lookup_table_service_api
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
    api_instance = lookup_table_service_api.LookupTableServiceApi(api_client)
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
        api_response = api_instance.lookup_table_service_list_lookup_table_versions(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LookupTableServiceApi->lookup_table_service_list_lookup_table_versions: %s\n" % e)
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

# **lookup_table_service_list_lookup_tables**
> TitaniumListLookupTableResponse lookup_table_service_list_lookup_tables(body)



### Example


```python
import time
import openapi_client
from openapi_client.api import lookup_table_service_api
from openapi_client.model.titanium_list_lookup_table_response import TitaniumListLookupTableResponse
from openapi_client.model.rpc_status import RpcStatus
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
    api_instance = lookup_table_service_api.LookupTableServiceApi(api_client)
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
        api_response = api_instance.lookup_table_service_list_lookup_tables(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LookupTableServiceApi->lookup_table_service_list_lookup_tables: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumListRequest**](TitaniumListRequest.md)|  |

### Return type

[**TitaniumListLookupTableResponse**](TitaniumListLookupTableResponse.md)

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

