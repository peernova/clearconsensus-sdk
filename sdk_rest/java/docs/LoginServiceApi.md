# LoginServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**loginServiceLogin**](LoginServiceApi.md#loginServiceLogin) | **POST** /api/v1/login |  |


<a name="loginServiceLogin"></a>
# **loginServiceLogin**
> TitaniumLoginResponse loginServiceLogin(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LoginServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    LoginServiceApi apiInstance = new LoginServiceApi(defaultClient);
    TitaniumLoginRequest body = new TitaniumLoginRequest(); // TitaniumLoginRequest | 
    try {
      TitaniumLoginResponse result = apiInstance.loginServiceLogin(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LoginServiceApi#loginServiceLogin");
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
| **body** | [**TitaniumLoginRequest**](TitaniumLoginRequest.md)|  | |

### Return type

[**TitaniumLoginResponse**](TitaniumLoginResponse.md)

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

