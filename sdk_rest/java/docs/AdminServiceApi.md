# AdminServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**adminServiceOnBoard**](AdminServiceApi.md#adminServiceOnBoard) | **POST** /api/v1/onboard |  |
| [**adminServiceRunCalculator**](AdminServiceApi.md#adminServiceRunCalculator) | **POST** /api/v1/calculator/run |  |
| [**adminServiceRunConsensus**](AdminServiceApi.md#adminServiceRunConsensus) | **POST** /api/v1/consensus/run |  |
| [**adminServiceUploadEvaluatedPrice**](AdminServiceApi.md#adminServiceUploadEvaluatedPrice) | **POST** /api/v1/upload/evaluated-price |  |


<a name="adminServiceOnBoard"></a>
# **adminServiceOnBoard**
> TitaniumMessageResponse adminServiceOnBoard(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdminServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    AdminServiceApi apiInstance = new AdminServiceApi(defaultClient);
    TitaniumOnBoardRequest body = new TitaniumOnBoardRequest(); // TitaniumOnBoardRequest | 
    try {
      TitaniumMessageResponse result = apiInstance.adminServiceOnBoard(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdminServiceApi#adminServiceOnBoard");
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
| **body** | [**TitaniumOnBoardRequest**](TitaniumOnBoardRequest.md)|  | |

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

<a name="adminServiceRunCalculator"></a>
# **adminServiceRunCalculator**
> TitaniumMessageResponse adminServiceRunCalculator(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdminServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    AdminServiceApi apiInstance = new AdminServiceApi(defaultClient);
    TitaniumRunCalculatorRequest body = new TitaniumRunCalculatorRequest(); // TitaniumRunCalculatorRequest | 
    try {
      TitaniumMessageResponse result = apiInstance.adminServiceRunCalculator(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdminServiceApi#adminServiceRunCalculator");
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
| **body** | [**TitaniumRunCalculatorRequest**](TitaniumRunCalculatorRequest.md)|  | |

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

<a name="adminServiceRunConsensus"></a>
# **adminServiceRunConsensus**
> TitaniumMessageResponse adminServiceRunConsensus(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdminServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    AdminServiceApi apiInstance = new AdminServiceApi(defaultClient);
    TitaniumRunConsensusRequest body = new TitaniumRunConsensusRequest(); // TitaniumRunConsensusRequest | 
    try {
      TitaniumMessageResponse result = apiInstance.adminServiceRunConsensus(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdminServiceApi#adminServiceRunConsensus");
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
| **body** | [**TitaniumRunConsensusRequest**](TitaniumRunConsensusRequest.md)|  | |

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

<a name="adminServiceUploadEvaluatedPrice"></a>
# **adminServiceUploadEvaluatedPrice**
> TitaniumMessageResponse adminServiceUploadEvaluatedPrice(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdminServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    AdminServiceApi apiInstance = new AdminServiceApi(defaultClient);
    TitaniumUploadEvaluatedPriceRequest body = new TitaniumUploadEvaluatedPriceRequest(); // TitaniumUploadEvaluatedPriceRequest | 
    try {
      TitaniumMessageResponse result = apiInstance.adminServiceUploadEvaluatedPrice(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdminServiceApi#adminServiceUploadEvaluatedPrice");
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
| **body** | [**TitaniumUploadEvaluatedPriceRequest**](TitaniumUploadEvaluatedPriceRequest.md)|  | |

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

