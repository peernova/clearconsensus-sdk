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
import time
import openapi_client
from openapi_client.api import supported_fields_service_api
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_supported_field import TitaniumSupportedField
from openapi_client.model.titanium_get_field_values_response import TitaniumGetFieldValuesResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = supported_fields_service_api.SupportedFieldsServiceApi(api_client)
    body = TitaniumSupportedField(
        asset="asset_example",
        asset_id="asset_id_example",
        field="field_example",
        filter="filter_example",
        instrument_type="instrument_type_example",
        limit=TitaniumLimit(
            value=1,
        ),
        match_pattern="match_pattern_example",
        offset=1,
        service="service_example",
        submitted_date="submitted_date_example",
        trace_name="trace_name_example",
    ) # TitaniumSupportedField | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.supported_fields_service_get_supported_fields_values(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
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
import time
import openapi_client
from openapi_client.api import supported_fields_service_api
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_get_supported_fields_response import TitaniumGetSupportedFieldsResponse
from openapi_client.model.titanium_get_supported_fields import TitaniumGetSupportedFields
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = supported_fields_service_api.SupportedFieldsServiceApi(api_client)
    body = TitaniumGetSupportedFields(
        asset_id="asset_id_example",
        limit=TitaniumLimit(
            value=1,
        ),
        offset=1,
        trace_name="trace_name_example",
    ) # TitaniumGetSupportedFields | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.supported_fields_service_list_supported_fields(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
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

