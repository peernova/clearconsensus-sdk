# openapi_client.LookupTableServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lookup_table_service_add_lookup_table**](LookupTableServiceApi.md#lookup_table_service_add_lookup_table) | **POST** /api/v1/lookuptable/add | 
[**lookup_table_service_disable_lookup_table**](LookupTableServiceApi.md#lookup_table_service_disable_lookup_table) | **POST** /api/v1/lookuptable/disable | 
[**lookup_table_service_enable_lookup_table**](LookupTableServiceApi.md#lookup_table_service_enable_lookup_table) | **POST** /api/v1/lookuptable/enable | 
[**lookup_table_service_get_lookup_table**](LookupTableServiceApi.md#lookup_table_service_get_lookup_table) | **POST** /api/v1/lookuptable/get | 
[**lookup_table_service_list_lookup_table_versions**](LookupTableServiceApi.md#lookup_table_service_list_lookup_table_versions) | **POST** /api/v1/lookuptable/versions | 
[**lookup_table_service_list_lookup_tables**](LookupTableServiceApi.md#lookup_table_service_list_lookup_tables) | **POST** /api/v1/lookuptable/list | 


# **lookup_table_service_add_lookup_table**
> TitaniumAcknowledgeResponse lookup_table_service_add_lookup_table(body)



### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.LookupTableServiceApi(api_client)
    body = openapi_client.TitaniumAddLookupTableRequest() # TitaniumAddLookupTableRequest | 

    try:
        api_response = api_instance.lookup_table_service_add_lookup_table(body)
        pprint(api_response)
    except ApiException as e:
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

# **lookup_table_service_disable_lookup_table**
> TitaniumAcknowledgeResponse lookup_table_service_disable_lookup_table(body)



### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.LookupTableServiceApi(api_client)
    body = openapi_client.TitaniumEnableDisableRequest() # TitaniumEnableDisableRequest | 

    try:
        api_response = api_instance.lookup_table_service_disable_lookup_table(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LookupTableServiceApi->lookup_table_service_disable_lookup_table: %s\n" % e)
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

# **lookup_table_service_enable_lookup_table**
> TitaniumAcknowledgeResponse lookup_table_service_enable_lookup_table(body)



### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.LookupTableServiceApi(api_client)
    body = openapi_client.TitaniumEnableDisableRequest() # TitaniumEnableDisableRequest | 

    try:
        api_response = api_instance.lookup_table_service_enable_lookup_table(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LookupTableServiceApi->lookup_table_service_enable_lookup_table: %s\n" % e)
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

# **lookup_table_service_get_lookup_table**
> TitaniumGetLookupTableResponse lookup_table_service_get_lookup_table(body)



### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.LookupTableServiceApi(api_client)
    body = openapi_client.TitaniumGetDefinition() # TitaniumGetDefinition | 

    try:
        api_response = api_instance.lookup_table_service_get_lookup_table(body)
        pprint(api_response)
    except ApiException as e:
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
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.LookupTableServiceApi(api_client)
    body = openapi_client.TitaniumGetDefinition() # TitaniumGetDefinition | 

    try:
        api_response = api_instance.lookup_table_service_list_lookup_table_versions(body)
        pprint(api_response)
    except ApiException as e:
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
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.LookupTableServiceApi(api_client)
    body = openapi_client.TitaniumListRequest() # TitaniumListRequest | 

    try:
        api_response = api_instance.lookup_table_service_list_lookup_tables(body)
        pprint(api_response)
    except ApiException as e:
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

