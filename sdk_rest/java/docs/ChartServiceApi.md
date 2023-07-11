# ChartServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**chartServiceGetChartData**](ChartServiceApi.md#chartServiceGetChartData) | **POST** /api/v1/analytics/chart-data |  |
| [**chartServiceGetTableData**](ChartServiceApi.md#chartServiceGetTableData) | **POST** /api/v1/analytics/table |  |


<a name="chartServiceGetChartData"></a>
# **chartServiceGetChartData**
> TitaniumGetChartDataResponse chartServiceGetChartData(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChartServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    ChartServiceApi apiInstance = new ChartServiceApi(defaultClient);
    TitaniumGetChartDataRequest body = new TitaniumGetChartDataRequest(); // TitaniumGetChartDataRequest | 
    try {
      TitaniumGetChartDataResponse result = apiInstance.chartServiceGetChartData(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChartServiceApi#chartServiceGetChartData");
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
| **body** | [**TitaniumGetChartDataRequest**](TitaniumGetChartDataRequest.md)|  | |

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
| **200** | A successful response. |  -  |
| **0** | An unexpected error response. |  -  |

<a name="chartServiceGetTableData"></a>
# **chartServiceGetTableData**
> TitaniumGetTableResponse chartServiceGetTableData(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChartServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    ChartServiceApi apiInstance = new ChartServiceApi(defaultClient);
    TitaniumGetChartDataRequest body = new TitaniumGetChartDataRequest(); // TitaniumGetChartDataRequest | 
    try {
      TitaniumGetTableResponse result = apiInstance.chartServiceGetTableData(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChartServiceApi#chartServiceGetTableData");
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
| **body** | [**TitaniumGetChartDataRequest**](TitaniumGetChartDataRequest.md)|  | |

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
| **200** | A successful response. |  -  |
| **0** | An unexpected error response. |  -  |

