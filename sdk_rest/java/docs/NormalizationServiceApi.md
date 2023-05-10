# NormalizationServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**normalizationServiceAddNormalizationRule**](NormalizationServiceApi.md#normalizationServiceAddNormalizationRule) | **POST** /api/v1/normalization/rule/add |  |
| [**normalizationServiceDisableNormalizationRule**](NormalizationServiceApi.md#normalizationServiceDisableNormalizationRule) | **POST** /api/v1/normalization/rule/disable |  |
| [**normalizationServiceEnableNormalizationRule**](NormalizationServiceApi.md#normalizationServiceEnableNormalizationRule) | **POST** /api/v1/normalization/rule/enable |  |
| [**normalizationServiceGetNormalizationRule**](NormalizationServiceApi.md#normalizationServiceGetNormalizationRule) | **POST** /api/v1/normalization/rule/get |  |
| [**normalizationServiceGetNormalizationRuleVersion**](NormalizationServiceApi.md#normalizationServiceGetNormalizationRuleVersion) | **GET** /api/v1/normalization/rule/version/{descriptorName}/{versionId} |  |
| [**normalizationServiceListNormalizationRuleVersions**](NormalizationServiceApi.md#normalizationServiceListNormalizationRuleVersions) | **POST** /api/v1/normalization/rule/versions |  |
| [**normalizationServiceListNormalizationRules**](NormalizationServiceApi.md#normalizationServiceListNormalizationRules) | **POST** /api/v1/normalization/rule/list |  |


<a name="normalizationServiceAddNormalizationRule"></a>
# **normalizationServiceAddNormalizationRule**
> TitaniumAcknowledgeResponse normalizationServiceAddNormalizationRule(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NormalizationServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    NormalizationServiceApi apiInstance = new NormalizationServiceApi(defaultClient);
    TitaniumNormalizationRuleDefinition body = new TitaniumNormalizationRuleDefinition(); // TitaniumNormalizationRuleDefinition | 
    try {
      TitaniumAcknowledgeResponse result = apiInstance.normalizationServiceAddNormalizationRule(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NormalizationServiceApi#normalizationServiceAddNormalizationRule");
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
| **body** | [**TitaniumNormalizationRuleDefinition**](TitaniumNormalizationRuleDefinition.md)|  | |

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

<a name="normalizationServiceDisableNormalizationRule"></a>
# **normalizationServiceDisableNormalizationRule**
> TitaniumAcknowledgeResponse normalizationServiceDisableNormalizationRule(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NormalizationServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    NormalizationServiceApi apiInstance = new NormalizationServiceApi(defaultClient);
    TitaniumGetDefinition body = new TitaniumGetDefinition(); // TitaniumGetDefinition | 
    try {
      TitaniumAcknowledgeResponse result = apiInstance.normalizationServiceDisableNormalizationRule(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NormalizationServiceApi#normalizationServiceDisableNormalizationRule");
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
| **body** | [**TitaniumGetDefinition**](TitaniumGetDefinition.md)|  | |

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

<a name="normalizationServiceEnableNormalizationRule"></a>
# **normalizationServiceEnableNormalizationRule**
> TitaniumAcknowledgeResponse normalizationServiceEnableNormalizationRule(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NormalizationServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    NormalizationServiceApi apiInstance = new NormalizationServiceApi(defaultClient);
    TitaniumGetDefinition body = new TitaniumGetDefinition(); // TitaniumGetDefinition | 
    try {
      TitaniumAcknowledgeResponse result = apiInstance.normalizationServiceEnableNormalizationRule(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NormalizationServiceApi#normalizationServiceEnableNormalizationRule");
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
| **body** | [**TitaniumGetDefinition**](TitaniumGetDefinition.md)|  | |

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

<a name="normalizationServiceGetNormalizationRule"></a>
# **normalizationServiceGetNormalizationRule**
> TitaniumNormalizationRuleResponse normalizationServiceGetNormalizationRule(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NormalizationServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    NormalizationServiceApi apiInstance = new NormalizationServiceApi(defaultClient);
    TitaniumGetDefinition body = new TitaniumGetDefinition(); // TitaniumGetDefinition | 
    try {
      TitaniumNormalizationRuleResponse result = apiInstance.normalizationServiceGetNormalizationRule(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NormalizationServiceApi#normalizationServiceGetNormalizationRule");
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
| **body** | [**TitaniumGetDefinition**](TitaniumGetDefinition.md)|  | |

### Return type

[**TitaniumNormalizationRuleResponse**](TitaniumNormalizationRuleResponse.md)

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

<a name="normalizationServiceGetNormalizationRuleVersion"></a>
# **normalizationServiceGetNormalizationRuleVersion**
> TitaniumNormalizationRuleResponse normalizationServiceGetNormalizationRuleVersion(descriptorName, versionId, name, scope)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NormalizationServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    NormalizationServiceApi apiInstance = new NormalizationServiceApi(defaultClient);
    String descriptorName = "descriptorName_example"; // String | 
    String versionId = "versionId_example"; // String | 
    String name = "name_example"; // String | 
    String scope = "scope_example"; // String | 
    try {
      TitaniumNormalizationRuleResponse result = apiInstance.normalizationServiceGetNormalizationRuleVersion(descriptorName, versionId, name, scope);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NormalizationServiceApi#normalizationServiceGetNormalizationRuleVersion");
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
| **descriptorName** | **String**|  | |
| **versionId** | **String**|  | |
| **name** | **String**|  | [optional] |
| **scope** | **String**|  | [optional] |

### Return type

[**TitaniumNormalizationRuleResponse**](TitaniumNormalizationRuleResponse.md)

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

<a name="normalizationServiceListNormalizationRuleVersions"></a>
# **normalizationServiceListNormalizationRuleVersions**
> TitaniumListVersionResponse normalizationServiceListNormalizationRuleVersions(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NormalizationServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    NormalizationServiceApi apiInstance = new NormalizationServiceApi(defaultClient);
    TitaniumGetDefinition body = new TitaniumGetDefinition(); // TitaniumGetDefinition | 
    try {
      TitaniumListVersionResponse result = apiInstance.normalizationServiceListNormalizationRuleVersions(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NormalizationServiceApi#normalizationServiceListNormalizationRuleVersions");
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
| **body** | [**TitaniumGetDefinition**](TitaniumGetDefinition.md)|  | |

### Return type

[**TitaniumListVersionResponse**](TitaniumListVersionResponse.md)

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

<a name="normalizationServiceListNormalizationRules"></a>
# **normalizationServiceListNormalizationRules**
> TitaniumListRuleResponse normalizationServiceListNormalizationRules(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NormalizationServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    NormalizationServiceApi apiInstance = new NormalizationServiceApi(defaultClient);
    TitaniumListRequest body = new TitaniumListRequest(); // TitaniumListRequest | 
    try {
      TitaniumListRuleResponse result = apiInstance.normalizationServiceListNormalizationRules(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NormalizationServiceApi#normalizationServiceListNormalizationRules");
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

[**TitaniumListRuleResponse**](TitaniumListRuleResponse.md)

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

