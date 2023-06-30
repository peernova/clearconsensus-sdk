# openapi_client.ChartServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chart_service_get_chart_data**](ChartServiceApi.md#chart_service_get_chart_data) | **POST** /api/v1/analytics/chart-data | 


# **chart_service_get_chart_data**
> TitaniumGetChartDataResponse chart_service_get_chart_data(body)



### Example


```python
import time
import openapi_client
from openapi_client.api import chart_service_api
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_get_chart_data_response import TitaniumGetChartDataResponse
from openapi_client.model.titanium_get_chart_data_request import TitaniumGetChartDataRequest
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = chart_service_api.ChartServiceApi(api_client)
    body = TitaniumGetChartDataRequest(
        asset_id="asset_id_example",
        chart_id="chart_id_example",
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
        invalidate_cache=True,
        parameters={},
        slice_id="slice_id_example",
        trace_name="trace_name_example",
    ) # TitaniumGetChartDataRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.chart_service_get_chart_data(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ChartServiceApi->chart_service_get_chart_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumGetChartDataRequest**](TitaniumGetChartDataRequest.md)|  |

### Return type

[**TitaniumGetChartDataResponse**](TitaniumGetChartDataResponse.md)

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

