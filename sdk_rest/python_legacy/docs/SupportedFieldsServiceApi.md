# openapi_client.SupportedFieldsServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**supported_fields_service_get_supported_fields_values**](SupportedFieldsServiceApi.md#supported_fields_service_get_supported_fields_values) | **POST** /api/v1/list/field-values | 
[**supported_fields_service_list_supported_fields**](SupportedFieldsServiceApi.md#supported_fields_service_list_supported_fields) | **POST** /api/v1/list/fields | 


# **supported_fields_service_get_supported_fields_values**
> TitaniumGetFieldValuesResponse supported_fields_service_get_supported_fields_values(body)



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
    api_instance = openapi_client.SupportedFieldsServiceApi(api_client)
    body = openapi_client.TitaniumSupportedField() # TitaniumSupportedField | 

    try:
        api_response = api_instance.supported_fields_service_get_supported_fields_values(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SupportedFieldsServiceApi->supported_fields_service_get_supported_fields_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumSupportedField**](TitaniumSupportedField.md)|  | 

### Return type

[**TitaniumGetFieldValuesResponse**](TitaniumGetFieldValuesResponse.md)

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

# **supported_fields_service_list_supported_fields**
> TitaniumGetSupportedFieldsResponse supported_fields_service_list_supported_fields(body)



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
    api_instance = openapi_client.SupportedFieldsServiceApi(api_client)
    body = openapi_client.TitaniumGetSupportedFields() # TitaniumGetSupportedFields | 

    try:
        api_response = api_instance.supported_fields_service_list_supported_fields(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SupportedFieldsServiceApi->supported_fields_service_list_supported_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumGetSupportedFields**](TitaniumGetSupportedFields.md)|  | 

### Return type

[**TitaniumGetSupportedFieldsResponse**](TitaniumGetSupportedFieldsResponse.md)

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

