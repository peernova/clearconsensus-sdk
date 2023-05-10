# AssetsServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**assetsServiceAssets**](AssetsServiceApi.md#assetsServiceAssets) | **POST** /api/v1/assets | Assets returns asset from the system according to request. |
| [**assetsServiceAssetsList**](AssetsServiceApi.md#assetsServiceAssetsList) | **POST** /api/v1/assets/list | AssetsList return list of assets according to snap time. |
| [**assetsServiceRecentAssets**](AssetsServiceApi.md#assetsServiceRecentAssets) | **POST** /api/v1/recentassets | RecentAssets returns recent added assets according to request. |
| [**assetsServiceSupportedAssets**](AssetsServiceApi.md#assetsServiceSupportedAssets) | **GET** /api/v1/supported/assets |  |


<a name="assetsServiceAssets"></a>
# **assetsServiceAssets**
> TitaniumAssetsResponse assetsServiceAssets(body)

Assets returns asset from the system according to request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetsServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    AssetsServiceApi apiInstance = new AssetsServiceApi(defaultClient);
    TitaniumAssetsRequest body = new TitaniumAssetsRequest(); // TitaniumAssetsRequest | 
    try {
      TitaniumAssetsResponse result = apiInstance.assetsServiceAssets(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetsServiceApi#assetsServiceAssets");
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
| **body** | [**TitaniumAssetsRequest**](TitaniumAssetsRequest.md)|  | |

### Return type

[**TitaniumAssetsResponse**](TitaniumAssetsResponse.md)

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

<a name="assetsServiceAssetsList"></a>
# **assetsServiceAssetsList**
> TitaniumAssetsListResponse assetsServiceAssetsList(body)

AssetsList return list of assets according to snap time.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetsServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    AssetsServiceApi apiInstance = new AssetsServiceApi(defaultClient);
    TitaniumAssetsListRequest body = new TitaniumAssetsListRequest(); // TitaniumAssetsListRequest | 
    try {
      TitaniumAssetsListResponse result = apiInstance.assetsServiceAssetsList(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetsServiceApi#assetsServiceAssetsList");
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
| **body** | [**TitaniumAssetsListRequest**](TitaniumAssetsListRequest.md)|  | |

### Return type

[**TitaniumAssetsListResponse**](TitaniumAssetsListResponse.md)

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

<a name="assetsServiceRecentAssets"></a>
# **assetsServiceRecentAssets**
> TitaniumRecentAssetsResponse assetsServiceRecentAssets(body)

RecentAssets returns recent added assets according to request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetsServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    AssetsServiceApi apiInstance = new AssetsServiceApi(defaultClient);
    TitaniumRecentAssetsRequest body = new TitaniumRecentAssetsRequest(); // TitaniumRecentAssetsRequest | 
    try {
      TitaniumRecentAssetsResponse result = apiInstance.assetsServiceRecentAssets(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetsServiceApi#assetsServiceRecentAssets");
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
| **body** | [**TitaniumRecentAssetsRequest**](TitaniumRecentAssetsRequest.md)|  | |

### Return type

[**TitaniumRecentAssetsResponse**](TitaniumRecentAssetsResponse.md)

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

<a name="assetsServiceSupportedAssets"></a>
# **assetsServiceSupportedAssets**
> TitaniumAssetsListResponse assetsServiceSupportedAssets()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetsServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    AssetsServiceApi apiInstance = new AssetsServiceApi(defaultClient);
    try {
      TitaniumAssetsListResponse result = apiInstance.assetsServiceSupportedAssets();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetsServiceApi#assetsServiceSupportedAssets");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TitaniumAssetsListResponse**](TitaniumAssetsListResponse.md)

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

