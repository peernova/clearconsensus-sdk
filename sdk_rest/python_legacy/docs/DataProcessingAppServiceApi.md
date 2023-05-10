# openapi_client.DataProcessingAppServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**data_processing_app_service_run_data_processing_app**](DataProcessingAppServiceApi.md#data_processing_app_service_run_data_processing_app) | **POST** /api/v1/dataprocessingapp/run | RunDataProcessingApp triggers jobs that are responsible to processing of received data.


# **data_processing_app_service_run_data_processing_app**
> TitaniumRunDataProcessingAppResponse data_processing_app_service_run_data_processing_app(body)

RunDataProcessingApp triggers jobs that are responsible to processing of received data.

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
    api_instance = openapi_client.DataProcessingAppServiceApi(api_client)
    body = openapi_client.TitaniumRunDataProcessingAppRequest() # TitaniumRunDataProcessingAppRequest | 

    try:
        # RunDataProcessingApp triggers jobs that are responsible to processing of received data.
        api_response = api_instance.data_processing_app_service_run_data_processing_app(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataProcessingAppServiceApi->data_processing_app_service_run_data_processing_app: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumRunDataProcessingAppRequest**](TitaniumRunDataProcessingAppRequest.md)|  | 

### Return type

[**TitaniumRunDataProcessingAppResponse**](TitaniumRunDataProcessingAppResponse.md)

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

