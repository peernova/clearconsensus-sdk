# DataProcessingAppServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**dataProcessingAppServiceRunDataProcessingApp**](DataProcessingAppServiceApi.md#dataProcessingAppServiceRunDataProcessingApp) | **POST** /api/v1/dataprocessingapp/run | RunDataProcessingApp triggers jobs that are responsible to processing of received data. |


<a name="dataProcessingAppServiceRunDataProcessingApp"></a>
# **dataProcessingAppServiceRunDataProcessingApp**
> TitaniumRunDataProcessingAppResponse dataProcessingAppServiceRunDataProcessingApp(body)

RunDataProcessingApp triggers jobs that are responsible to processing of received data.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataProcessingAppServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    DataProcessingAppServiceApi apiInstance = new DataProcessingAppServiceApi(defaultClient);
    TitaniumRunDataProcessingAppRequest body = new TitaniumRunDataProcessingAppRequest(); // TitaniumRunDataProcessingAppRequest | 
    try {
      TitaniumRunDataProcessingAppResponse result = apiInstance.dataProcessingAppServiceRunDataProcessingApp(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataProcessingAppServiceApi#dataProcessingAppServiceRunDataProcessingApp");
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
| **body** | [**TitaniumRunDataProcessingAppRequest**](TitaniumRunDataProcessingAppRequest.md)|  | |

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
| **200** | A successful response. |  -  |
| **0** | An unexpected error response. |  -  |

