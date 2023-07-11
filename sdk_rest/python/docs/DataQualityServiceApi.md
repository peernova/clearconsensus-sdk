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
import time
import openapi_client
from openapi_client.api import data_quality_service_api
from openapi_client.model.titanium_dq_errors_response import TitaniumDQErrorsResponse
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_dq_errors_request import TitaniumDQErrorsRequest
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_quality_service_api.DataQualityServiceApi(api_client)
    body = TitaniumDQErrorsRequest(
        asset_id="asset_id_example",
        filter="filter_example",
        filter_pack=TitaniumFilterPack(
            filter_packs=[
                TitaniumFilterPack(),
            ],
            filters=[
                TitaniumFilter(
                    key="key_example",
                    operator="operator_example",
                    value={},
                ),
            ],
            logical_operation="logical_operation_example",
        ),
        order_by=TitaniumOrderBy(
            column="column_example",
            order="order_example",
        ),
        page=TitaniumPage(
            page_number=1,
            size=1,
            total_number_of_elements="total_number_of_elements_example",
        ),
        submitted_date="submitted_date_example",
        submitted_id="submitted_id_example",
        trace_name="trace_name_example",
    ) # TitaniumDQErrorsRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.data_quality_service_dq_errors(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
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
import time
import openapi_client
from openapi_client.api import data_quality_service_api
from openapi_client.model.titanium_get_data_quality_errors_response import TitaniumGetDataQualityErrorsResponse
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_get_data_quality_errors_request import TitaniumGetDataQualityErrorsRequest
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_quality_service_api.DataQualityServiceApi(api_client)
    body = TitaniumGetDataQualityErrorsRequest(
        asset_id="asset_id_example",
        group_keys=TitaniumFilterPack(
            filter_packs=[
                TitaniumFilterPack(),
            ],
            filters=[
                TitaniumFilter(
                    key="key_example",
                    operator="operator_example",
                    value={},
                ),
            ],
            logical_operation="logical_operation_example",
        ),
        submission_id="submission_id_example",
        submitted_date="submitted_date_example",
        trace_name="trace_name_example",
    ) # TitaniumGetDataQualityErrorsRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.data_quality_service_get_data_quality_errors(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
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

