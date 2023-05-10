# KvServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**kVServiceAddKey**](KvServiceApi.md#kVServiceAddKey) | **POST** /api/v1/kv/add |  |
| [**kVServiceDeleteKey**](KvServiceApi.md#kVServiceDeleteKey) | **POST** /api/v1/kv/delete |  |
| [**kVServiceGetKey**](KvServiceApi.md#kVServiceGetKey) | **POST** /api/v1/kv/get |  |
| [**kVServiceListKeys**](KvServiceApi.md#kVServiceListKeys) | **POST** /api/v1/kv/list |  |
| [**kVServiceUpdateKey**](KvServiceApi.md#kVServiceUpdateKey) | **POST** /api/v1/kv/update |  |


<a name="kVServiceAddKey"></a>
# **kVServiceAddKey**
> TitaniumKVOperationResponse kVServiceAddKey(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KvServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    KvServiceApi apiInstance = new KvServiceApi(defaultClient);
    TitaniumKVAsset body = new TitaniumKVAsset(); // TitaniumKVAsset | 
    try {
      TitaniumKVOperationResponse result = apiInstance.kVServiceAddKey(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KvServiceApi#kVServiceAddKey");
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
| **body** | [**TitaniumKVAsset**](TitaniumKVAsset.md)|  | |

### Return type

[**TitaniumKVOperationResponse**](TitaniumKVOperationResponse.md)

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

<a name="kVServiceDeleteKey"></a>
# **kVServiceDeleteKey**
> TitaniumKVOperationResponse kVServiceDeleteKey(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KvServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    KvServiceApi apiInstance = new KvServiceApi(defaultClient);
    TitaniumKVRequest body = new TitaniumKVRequest(); // TitaniumKVRequest | 
    try {
      TitaniumKVOperationResponse result = apiInstance.kVServiceDeleteKey(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KvServiceApi#kVServiceDeleteKey");
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
| **body** | [**TitaniumKVRequest**](TitaniumKVRequest.md)|  | |

### Return type

[**TitaniumKVOperationResponse**](TitaniumKVOperationResponse.md)

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

<a name="kVServiceGetKey"></a>
# **kVServiceGetKey**
> TitaniumGetKVResponse kVServiceGetKey(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KvServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    KvServiceApi apiInstance = new KvServiceApi(defaultClient);
    TitaniumKVRequest body = new TitaniumKVRequest(); // TitaniumKVRequest | 
    try {
      TitaniumGetKVResponse result = apiInstance.kVServiceGetKey(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KvServiceApi#kVServiceGetKey");
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
| **body** | [**TitaniumKVRequest**](TitaniumKVRequest.md)|  | |

### Return type

[**TitaniumGetKVResponse**](TitaniumGetKVResponse.md)

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

<a name="kVServiceListKeys"></a>
# **kVServiceListKeys**
> TitaniumListKVResponse kVServiceListKeys(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KvServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    KvServiceApi apiInstance = new KvServiceApi(defaultClient);
    TitaniumListKVRequest body = new TitaniumListKVRequest(); // TitaniumListKVRequest | 
    try {
      TitaniumListKVResponse result = apiInstance.kVServiceListKeys(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KvServiceApi#kVServiceListKeys");
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
| **body** | [**TitaniumListKVRequest**](TitaniumListKVRequest.md)|  | |

### Return type

[**TitaniumListKVResponse**](TitaniumListKVResponse.md)

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

<a name="kVServiceUpdateKey"></a>
# **kVServiceUpdateKey**
> TitaniumKVOperationResponse kVServiceUpdateKey(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KvServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    KvServiceApi apiInstance = new KvServiceApi(defaultClient);
    TitaniumKVAsset body = new TitaniumKVAsset(); // TitaniumKVAsset | 
    try {
      TitaniumKVOperationResponse result = apiInstance.kVServiceUpdateKey(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KvServiceApi#kVServiceUpdateKey");
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
| **body** | [**TitaniumKVAsset**](TitaniumKVAsset.md)|  | |

### Return type

[**TitaniumKVOperationResponse**](TitaniumKVOperationResponse.md)

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

