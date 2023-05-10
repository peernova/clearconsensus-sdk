# OutliersServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**outliersServiceOutliers**](OutliersServiceApi.md#outliersServiceOutliers) | **POST** /api/v1/outliers | Outliers returns outliers according to request. |


<a name="outliersServiceOutliers"></a>
# **outliersServiceOutliers**
> TitaniumOutliersResponse outliersServiceOutliers(body)

Outliers returns outliers according to request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OutliersServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    OutliersServiceApi apiInstance = new OutliersServiceApi(defaultClient);
    TitaniumOutliersRequest body = new TitaniumOutliersRequest(); // TitaniumOutliersRequest | 
    try {
      TitaniumOutliersResponse result = apiInstance.outliersServiceOutliers(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OutliersServiceApi#outliersServiceOutliers");
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
| **body** | [**TitaniumOutliersRequest**](TitaniumOutliersRequest.md)|  | |

### Return type

[**TitaniumOutliersResponse**](TitaniumOutliersResponse.md)

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

