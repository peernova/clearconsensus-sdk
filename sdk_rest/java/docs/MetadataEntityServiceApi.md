# MetadataEntityServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**metadataEntityServiceAddEntity**](MetadataEntityServiceApi.md#metadataEntityServiceAddEntity) | **POST** /api/v1/entity/add |  |
| [**metadataEntityServiceDisableEntity**](MetadataEntityServiceApi.md#metadataEntityServiceDisableEntity) | **POST** /api/v1/entity/disable |  |
| [**metadataEntityServiceEnableEntity**](MetadataEntityServiceApi.md#metadataEntityServiceEnableEntity) | **POST** /api/v1/entity/enable |  |
| [**metadataEntityServiceGetEntity**](MetadataEntityServiceApi.md#metadataEntityServiceGetEntity) | **POST** /api/v1/entity/get |  |


<a name="metadataEntityServiceAddEntity"></a>
# **metadataEntityServiceAddEntity**
> TitaniumAcknowledgeResponse metadataEntityServiceAddEntity(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetadataEntityServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    MetadataEntityServiceApi apiInstance = new MetadataEntityServiceApi(defaultClient);
    TitaniumEntityDefinition body = new TitaniumEntityDefinition(); // TitaniumEntityDefinition | 
    try {
      TitaniumAcknowledgeResponse result = apiInstance.metadataEntityServiceAddEntity(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetadataEntityServiceApi#metadataEntityServiceAddEntity");
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
| **body** | [**TitaniumEntityDefinition**](TitaniumEntityDefinition.md)|  | |

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

<a name="metadataEntityServiceDisableEntity"></a>
# **metadataEntityServiceDisableEntity**
> TitaniumAcknowledgeResponse metadataEntityServiceDisableEntity(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetadataEntityServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    MetadataEntityServiceApi apiInstance = new MetadataEntityServiceApi(defaultClient);
    TitaniumEntityIdentifier body = new TitaniumEntityIdentifier(); // TitaniumEntityIdentifier | 
    try {
      TitaniumAcknowledgeResponse result = apiInstance.metadataEntityServiceDisableEntity(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetadataEntityServiceApi#metadataEntityServiceDisableEntity");
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
| **body** | [**TitaniumEntityIdentifier**](TitaniumEntityIdentifier.md)|  | |

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

<a name="metadataEntityServiceEnableEntity"></a>
# **metadataEntityServiceEnableEntity**
> TitaniumAcknowledgeResponse metadataEntityServiceEnableEntity(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetadataEntityServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    MetadataEntityServiceApi apiInstance = new MetadataEntityServiceApi(defaultClient);
    TitaniumEntityIdentifier body = new TitaniumEntityIdentifier(); // TitaniumEntityIdentifier | 
    try {
      TitaniumAcknowledgeResponse result = apiInstance.metadataEntityServiceEnableEntity(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetadataEntityServiceApi#metadataEntityServiceEnableEntity");
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
| **body** | [**TitaniumEntityIdentifier**](TitaniumEntityIdentifier.md)|  | |

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

<a name="metadataEntityServiceGetEntity"></a>
# **metadataEntityServiceGetEntity**
> TitaniumEntityDefinition metadataEntityServiceGetEntity(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetadataEntityServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    MetadataEntityServiceApi apiInstance = new MetadataEntityServiceApi(defaultClient);
    TitaniumEntityIdentifier body = new TitaniumEntityIdentifier(); // TitaniumEntityIdentifier | 
    try {
      TitaniumEntityDefinition result = apiInstance.metadataEntityServiceGetEntity(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetadataEntityServiceApi#metadataEntityServiceGetEntity");
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
| **body** | [**TitaniumEntityIdentifier**](TitaniumEntityIdentifier.md)|  | |

### Return type

[**TitaniumEntityDefinition**](TitaniumEntityDefinition.md)

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

