# UdfServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**udfServiceDisableUdf**](UdfServiceApi.md#udfServiceDisableUdf) | **POST** /api/v1/udf/disable |  |
| [**udfServiceGetUdfDefinition**](UdfServiceApi.md#udfServiceGetUdfDefinition) | **GET** /api/v1/udf/{name} |  |
| [**udfServiceListUdfs**](UdfServiceApi.md#udfServiceListUdfs) | **POST** /api/v1/udf/list |  |


<a name="udfServiceDisableUdf"></a>
# **udfServiceDisableUdf**
> TitaniumMessageResponse udfServiceDisableUdf(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UdfServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    UdfServiceApi apiInstance = new UdfServiceApi(defaultClient);
    TitaniumUdfNameRequest body = new TitaniumUdfNameRequest(); // TitaniumUdfNameRequest | 
    try {
      TitaniumMessageResponse result = apiInstance.udfServiceDisableUdf(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UdfServiceApi#udfServiceDisableUdf");
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
| **body** | [**TitaniumUdfNameRequest**](TitaniumUdfNameRequest.md)|  | |

### Return type

[**TitaniumMessageResponse**](TitaniumMessageResponse.md)

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

<a name="udfServiceGetUdfDefinition"></a>
# **udfServiceGetUdfDefinition**
> TitaniumGetUdfResponse udfServiceGetUdfDefinition(name, scope)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UdfServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    UdfServiceApi apiInstance = new UdfServiceApi(defaultClient);
    String name = "name_example"; // String | 
    String scope = "scope_example"; // String | 
    try {
      TitaniumGetUdfResponse result = apiInstance.udfServiceGetUdfDefinition(name, scope);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UdfServiceApi#udfServiceGetUdfDefinition");
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
| **name** | **String**|  | |
| **scope** | **String**|  | [optional] |

### Return type

[**TitaniumGetUdfResponse**](TitaniumGetUdfResponse.md)

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

<a name="udfServiceListUdfs"></a>
# **udfServiceListUdfs**
> TitaniumListUdfResponse udfServiceListUdfs(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UdfServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    UdfServiceApi apiInstance = new UdfServiceApi(defaultClient);
    TitaniumListRequest body = new TitaniumListRequest(); // TitaniumListRequest | 
    try {
      TitaniumListUdfResponse result = apiInstance.udfServiceListUdfs(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UdfServiceApi#udfServiceListUdfs");
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
| **body** | [**TitaniumListRequest**](TitaniumListRequest.md)|  | |

### Return type

[**TitaniumListUdfResponse**](TitaniumListUdfResponse.md)

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

