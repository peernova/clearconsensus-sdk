# openapi_client.ChartServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chart_service_get_chart_data**](ChartServiceApi.md#chart_service_get_chart_data) | **POST** /api/v1/analytics/chart-data | 
[**chart_service_get_table_data**](ChartServiceApi.md#chart_service_get_table_data) | **POST** /api/v1/analytics/table | 


# **chart_service_get_chart_data**
> TitaniumGetChartDataResponse chart_service_get_chart_data(body)



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
    api_instance = openapi_client.ChartServiceApi(api_client)
    body = openapi_client.TitaniumGetChartDataRequest() # TitaniumGetChartDataRequest | 

    try:
        api_response = api_instance.chart_service_get_chart_data(body)
        pprint(api_response)
    except ApiException as e:
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

# **chart_service_get_table_data**
> TitaniumGetTableResponse chart_service_get_table_data(body)



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
    api_instance = openapi_client.ChartServiceApi(api_client)
    body = openapi_client.TitaniumGetChartDataRequest() # TitaniumGetChartDataRequest | 

    try:
        api_response = api_instance.chart_service_get_table_data(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChartServiceApi->chart_service_get_table_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumGetChartDataRequest**](TitaniumGetChartDataRequest.md)|  | 

### Return type

[**TitaniumGetTableResponse**](TitaniumGetTableResponse.md)

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

