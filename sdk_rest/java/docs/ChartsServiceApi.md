# ChartsServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**chartsServiceCharts**](ChartsServiceApi.md#chartsServiceCharts) | **POST** /api/v1/charts | Charts returns information about specific chart related to the specific asset. |
| [**chartsServiceChartsCurrencies**](ChartsServiceApi.md#chartsServiceChartsCurrencies) | **POST** /api/v1/charts/currencies | ChartsCurrencies returns information about the chart related to specific currency pair. |


<a name="chartsServiceCharts"></a>
# **chartsServiceCharts**
> TitaniumChartsResponse chartsServiceCharts(body)

Charts returns information about specific chart related to the specific asset.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChartsServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    ChartsServiceApi apiInstance = new ChartsServiceApi(defaultClient);
    TitaniumChartsRequest body = new TitaniumChartsRequest(); // TitaniumChartsRequest | 
    try {
      TitaniumChartsResponse result = apiInstance.chartsServiceCharts(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChartsServiceApi#chartsServiceCharts");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **body** | [**TitaniumChartsRequest**](TitaniumChartsRequest.md)|  | |

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
| **200** | A successful response. |  -  |
| **0** | An unexpected error response. |  -  |

<a name="chartsServiceChartsCurrencies"></a>
# **chartsServiceChartsCurrencies**
> TitaniumChartsCurrenciesResponse chartsServiceChartsCurrencies(body)

ChartsCurrencies returns information about the chart related to specific currency pair.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChartsServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    ChartsServiceApi apiInstance = new ChartsServiceApi(defaultClient);
    TitaniumChartsCurrenciesRequest body = new TitaniumChartsCurrenciesRequest(); // TitaniumChartsCurrenciesRequest | 
    try {
      TitaniumChartsCurrenciesResponse result = apiInstance.chartsServiceChartsCurrencies(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChartsServiceApi#chartsServiceChartsCurrencies");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **body** | [**TitaniumChartsCurrenciesRequest**](TitaniumChartsCurrenciesRequest.md)|  | |

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
| **200** | A successful response. |  -  |
| **0** | An unexpected error response. |  -  |

