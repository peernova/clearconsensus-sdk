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
import time
import openapi_client
from openapi_client.api import data_processing_app_service_api
from openapi_client.model.titanium_run_data_processing_app_request import TitaniumRunDataProcessingAppRequest
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_run_data_processing_app_response import TitaniumRunDataProcessingAppResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_processing_app_service_api.DataProcessingAppServiceApi(api_client)
    body = TitaniumRunDataProcessingAppRequest(
        asset="asset_example",
        date="date_example",
        descriptor_name="descriptor_name_example",
        file_name="file_name_example",
        input="input_example",
        instrument_type="instrument_type_example",
        mapper_rule="mapper_rule_example",
        service="service_example",
        snap_time="snap_time_example",
        validation_rule="validation_rule_example",
    ) # TitaniumRunDataProcessingAppRequest | 

    # example passing only required values which don't have defaults set
    try:
        # RunDataProcessingApp triggers jobs that are responsible to processing of received data.
        api_response = api_instance.data_processing_app_service_run_data_processing_app(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
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

