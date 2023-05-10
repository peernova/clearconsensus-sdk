# PopUpServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**popUpServicePopUpView**](PopUpServiceApi.md#popUpServicePopUpView) | **POST** /api/v1/popup-view | PopUpView returns information according to request for the popup view. |


<a name="popUpServicePopUpView"></a>
# **popUpServicePopUpView**
> TitaniumPopUpViewResponse popUpServicePopUpView(body)

PopUpView returns information according to request for the popup view.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PopUpServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    PopUpServiceApi apiInstance = new PopUpServiceApi(defaultClient);
    TitaniumPopUpViewRequest body = new TitaniumPopUpViewRequest(); // TitaniumPopUpViewRequest | 
    try {
      TitaniumPopUpViewResponse result = apiInstance.popUpServicePopUpView(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PopUpServiceApi#popUpServicePopUpView");
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
| **body** | [**TitaniumPopUpViewRequest**](TitaniumPopUpViewRequest.md)|  | |

### Return type

[**TitaniumPopUpViewResponse**](TitaniumPopUpViewResponse.md)

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

