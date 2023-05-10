# ScopeServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**scopeServiceAddScope**](ScopeServiceApi.md#scopeServiceAddScope) | **POST** /api/v1/scope/add | AddScope creates scope in the system. |
| [**scopeServiceExistScope**](ScopeServiceApi.md#scopeServiceExistScope) | **POST** /api/v1/scope/exist | ExistScope return boolean value about existence of scope according to request. |
| [**scopeServiceListScope**](ScopeServiceApi.md#scopeServiceListScope) | **POST** /api/v1/scope/list | ListScope returns list of all existing scopes. |


<a name="scopeServiceAddScope"></a>
# **scopeServiceAddScope**
> TitaniumAcknowledgeResponse scopeServiceAddScope(body)

AddScope creates scope in the system.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScopeServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    ScopeServiceApi apiInstance = new ScopeServiceApi(defaultClient);
    TitaniumScopeIdentifier body = new TitaniumScopeIdentifier(); // TitaniumScopeIdentifier | 
    try {
      TitaniumAcknowledgeResponse result = apiInstance.scopeServiceAddScope(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScopeServiceApi#scopeServiceAddScope");
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
| **body** | [**TitaniumScopeIdentifier**](TitaniumScopeIdentifier.md)|  | |

### Return type

[**TitaniumAcknowledgeResponse**](TitaniumAcknowledgeResponse.md)

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

<a name="scopeServiceExistScope"></a>
# **scopeServiceExistScope**
> TitaniumScopeExistResponse scopeServiceExistScope(body)

ExistScope return boolean value about existence of scope according to request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScopeServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    ScopeServiceApi apiInstance = new ScopeServiceApi(defaultClient);
    TitaniumScopeIdentifier body = new TitaniumScopeIdentifier(); // TitaniumScopeIdentifier | 
    try {
      TitaniumScopeExistResponse result = apiInstance.scopeServiceExistScope(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScopeServiceApi#scopeServiceExistScope");
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
| **body** | [**TitaniumScopeIdentifier**](TitaniumScopeIdentifier.md)|  | |

### Return type

[**TitaniumScopeExistResponse**](TitaniumScopeExistResponse.md)

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

<a name="scopeServiceListScope"></a>
# **scopeServiceListScope**
> TitaniumScopeListResponse scopeServiceListScope(body)

ListScope returns list of all existing scopes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScopeServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    ScopeServiceApi apiInstance = new ScopeServiceApi(defaultClient);
    Object body = null; // Object | 
    try {
      TitaniumScopeListResponse result = apiInstance.scopeServiceListScope(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScopeServiceApi#scopeServiceListScope");
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
| **body** | **Object**|  | |

### Return type

[**TitaniumScopeListResponse**](TitaniumScopeListResponse.md)

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

