# openapi_client.DataQualityServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**data_quality_service_dq_errors**](DataQualityServiceApi.md#data_quality_service_dq_errors) | **POST** /api/v1/dqerrors | 
[**data_quality_service_get_data_quality_errors**](DataQualityServiceApi.md#data_quality_service_get_data_quality_errors) | **POST** /api/v1/data-quality-errors | 


# **data_quality_service_dq_errors**
> TitaniumDQErrorsResponse data_quality_service_dq_errors(body)



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
    api_instance = openapi_client.DataQualityServiceApi(api_client)
    body = openapi_client.TitaniumDQErrorsRequest() # TitaniumDQErrorsRequest | 

    try:
        api_response = api_instance.data_quality_service_dq_errors(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataQualityServiceApi->data_quality_service_dq_errors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumDQErrorsRequest**](TitaniumDQErrorsRequest.md)|  | 

### Return type

[**TitaniumDQErrorsResponse**](TitaniumDQErrorsResponse.md)

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

# **data_quality_service_get_data_quality_errors**
> TitaniumGetDataQualityErrorsResponse data_quality_service_get_data_quality_errors(body)



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
    api_instance = openapi_client.DataQualityServiceApi(api_client)
    body = openapi_client.TitaniumGetDataQualityErrorsRequest() # TitaniumGetDataQualityErrorsRequest | 

    try:
        api_response = api_instance.data_quality_service_get_data_quality_errors(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataQualityServiceApi->data_quality_service_get_data_quality_errors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumGetDataQualityErrorsRequest**](TitaniumGetDataQualityErrorsRequest.md)|  | 

### Return type

[**TitaniumGetDataQualityErrorsResponse**](TitaniumGetDataQualityErrorsResponse.md)

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

