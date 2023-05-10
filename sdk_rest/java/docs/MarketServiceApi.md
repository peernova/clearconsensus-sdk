# MarketServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**marketServiceMarketSnapTime**](MarketServiceApi.md#marketServiceMarketSnapTime) | **GET** /api/v1/market/snap-time | MarketSnapTime returns time for which the prices(calculated in consensus) are valid.(Time of market closing) |


<a name="marketServiceMarketSnapTime"></a>
# **marketServiceMarketSnapTime**
> TitaniumMarketSnapTimeResponse marketServiceMarketSnapTime()

MarketSnapTime returns time for which the prices(calculated in consensus) are valid.(Time of market closing)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    MarketServiceApi apiInstance = new MarketServiceApi(defaultClient);
    try {
      TitaniumMarketSnapTimeResponse result = apiInstance.marketServiceMarketSnapTime();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketServiceApi#marketServiceMarketSnapTime");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TitaniumMarketSnapTimeResponse**](TitaniumMarketSnapTimeResponse.md)

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

