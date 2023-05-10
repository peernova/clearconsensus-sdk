# DataQualityServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**dataQualityServiceDQErrors**](DataQualityServiceApi.md#dataQualityServiceDQErrors) | **POST** /api/v1/dqerrors |  |
| [**dataQualityServiceGetDataQualityErrors**](DataQualityServiceApi.md#dataQualityServiceGetDataQualityErrors) | **POST** /api/v1/data-quality-errors |  |


<a name="dataQualityServiceDQErrors"></a>
# **dataQualityServiceDQErrors**
> TitaniumDQErrorsResponse dataQualityServiceDQErrors(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataQualityServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    DataQualityServiceApi apiInstance = new DataQualityServiceApi(defaultClient);
    TitaniumDQErrorsRequest body = new TitaniumDQErrorsRequest(); // TitaniumDQErrorsRequest | 
    try {
      TitaniumDQErrorsResponse result = apiInstance.dataQualityServiceDQErrors(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataQualityServiceApi#dataQualityServiceDQErrors");
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
| **body** | [**TitaniumDQErrorsRequest**](TitaniumDQErrorsRequest.md)|  | |

### Return type

[**TitaniumDQErrorsResponse**](TitaniumDQErrorsResponse.md)

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

<a name="dataQualityServiceGetDataQualityErrors"></a>
# **dataQualityServiceGetDataQualityErrors**
> TitaniumGetDataQualityErrorsResponse dataQualityServiceGetDataQualityErrors(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataQualityServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    DataQualityServiceApi apiInstance = new DataQualityServiceApi(defaultClient);
    TitaniumGetDataQualityErrorsRequest body = new TitaniumGetDataQualityErrorsRequest(); // TitaniumGetDataQualityErrorsRequest | 
    try {
      TitaniumGetDataQualityErrorsResponse result = apiInstance.dataQualityServiceGetDataQualityErrors(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataQualityServiceApi#dataQualityServiceGetDataQualityErrors");
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
| **body** | [**TitaniumGetDataQualityErrorsRequest**](TitaniumGetDataQualityErrorsRequest.md)|  | |

### Return type

[**TitaniumGetDataQualityErrorsResponse**](TitaniumGetDataQualityErrorsResponse.md)

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

