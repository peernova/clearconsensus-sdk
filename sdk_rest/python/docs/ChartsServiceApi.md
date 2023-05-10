# openapi_client.ChartsServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**charts_service_charts**](ChartsServiceApi.md#charts_service_charts) | **POST** /api/v1/charts | Charts returns information about specific chart related to the specific asset.
[**charts_service_charts_currencies**](ChartsServiceApi.md#charts_service_charts_currencies) | **POST** /api/v1/charts/currencies | ChartsCurrencies returns information about the chart related to specific currency pair.


# **charts_service_charts**
> TitaniumChartsResponse charts_service_charts(body)

Charts returns information about specific chart related to the specific asset.

### Example


```python
import time
import openapi_client
from openapi_client.api import charts_service_api
from openapi_client.model.titanium_charts_response import TitaniumChartsResponse
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_charts_request import TitaniumChartsRequest
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = charts_service_api.ChartsServiceApi(api_client)
    body = TitaniumChartsRequest(
        asset_id="asset_id_example",
        client="client_example",
        submitted_date="submitted_date_example",
        trace_name="trace_name_example",
        underlying="underlying_example",
    ) # TitaniumChartsRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Charts returns information about specific chart related to the specific asset.
        api_response = api_instance.charts_service_charts(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ChartsServiceApi->charts_service_charts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumChartsRequest**](TitaniumChartsRequest.md)|  |

### Return type

[**TitaniumChartsResponse**](TitaniumChartsResponse.md)

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

# **charts_service_charts_currencies**
> TitaniumChartsCurrenciesResponse charts_service_charts_currencies(body)

ChartsCurrencies returns information about the chart related to specific currency pair.

### Example


```python
import time
import openapi_client
from openapi_client.api import charts_service_api
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_charts_currencies_response import TitaniumChartsCurrenciesResponse
from openapi_client.model.titanium_charts_currencies_request import TitaniumChartsCurrenciesRequest
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = charts_service_api.ChartsServiceApi(api_client)
    body = TitaniumChartsCurrenciesRequest(
        asset_id="asset_id_example",
        submitted_date="submitted_date_example",
        trace_name="trace_name_example",
    ) # TitaniumChartsCurrenciesRequest | 

    # example passing only required values which don't have defaults set
    try:
        # ChartsCurrencies returns information about the chart related to specific currency pair.
        api_response = api_instance.charts_service_charts_currencies(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ChartsServiceApi->charts_service_charts_currencies: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumChartsCurrenciesRequest**](TitaniumChartsCurrenciesRequest.md)|  |

### Return type

[**TitaniumChartsCurrenciesResponse**](TitaniumChartsCurrenciesResponse.md)

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

