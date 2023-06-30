# DtccServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**dtccServiceGetDtccTable**](DtccServiceApi.md#dtccServiceGetDtccTable) | **POST** /api/v1/dtcc/tab |  |


<a name="dtccServiceGetDtccTable"></a>
# **dtccServiceGetDtccTable**
> TitaniumDtccTabResponse dtccServiceGetDtccTable(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DtccServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    DtccServiceApi apiInstance = new DtccServiceApi(defaultClient);
    TitaniumDtccTabRequest body = new TitaniumDtccTabRequest(); // TitaniumDtccTabRequest | 
    try {
      TitaniumDtccTabResponse result = apiInstance.dtccServiceGetDtccTable(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DtccServiceApi#dtccServiceGetDtccTable");
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
| **body** | [**TitaniumDtccTabRequest**](TitaniumDtccTabRequest.md)|  | |

### Return type

[**TitaniumDtccTabResponse**](TitaniumDtccTabResponse.md)

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

