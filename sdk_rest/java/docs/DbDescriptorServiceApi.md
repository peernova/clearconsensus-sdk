# DbDescriptorServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**dbDescriptorServiceAddDbDescriptor**](DbDescriptorServiceApi.md#dbDescriptorServiceAddDbDescriptor) | **POST** /api/v1/db/descriptor/add |  |
| [**dbDescriptorServiceDisableDbDescriptor**](DbDescriptorServiceApi.md#dbDescriptorServiceDisableDbDescriptor) | **POST** /api/v1/db/descriptor/disable |  |
| [**dbDescriptorServiceEnableDbDescriptor**](DbDescriptorServiceApi.md#dbDescriptorServiceEnableDbDescriptor) | **POST** /api/v1/db/descriptor/enable |  |
| [**dbDescriptorServiceGetDbDescriptor**](DbDescriptorServiceApi.md#dbDescriptorServiceGetDbDescriptor) | **POST** /api/v1/db/descriptor/get |  |
| [**dbDescriptorServiceGetDbDescriptorVersion**](DbDescriptorServiceApi.md#dbDescriptorServiceGetDbDescriptorVersion) | **GET** /api/v1/db/descriptor/version/{name}/{versionId} |  |
| [**dbDescriptorServiceListDbDescriptorVersions**](DbDescriptorServiceApi.md#dbDescriptorServiceListDbDescriptorVersions) | **POST** /api/v1/db/descriptor/versions |  |
| [**dbDescriptorServiceListDbDescriptors**](DbDescriptorServiceApi.md#dbDescriptorServiceListDbDescriptors) | **POST** /api/v1/db/descriptor/list |  |


<a name="dbDescriptorServiceAddDbDescriptor"></a>
# **dbDescriptorServiceAddDbDescriptor**
> TitaniumAcknowledgeResponse dbDescriptorServiceAddDbDescriptor(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DbDescriptorServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    DbDescriptorServiceApi apiInstance = new DbDescriptorServiceApi(defaultClient);
    TitaniumDescriptorDefinition body = new TitaniumDescriptorDefinition(); // TitaniumDescriptorDefinition | 
    try {
      TitaniumAcknowledgeResponse result = apiInstance.dbDescriptorServiceAddDbDescriptor(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DbDescriptorServiceApi#dbDescriptorServiceAddDbDescriptor");
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
| **body** | [**TitaniumDescriptorDefinition**](TitaniumDescriptorDefinition.md)|  | |

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

<a name="dbDescriptorServiceDisableDbDescriptor"></a>
# **dbDescriptorServiceDisableDbDescriptor**
> TitaniumAcknowledgeResponse dbDescriptorServiceDisableDbDescriptor(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DbDescriptorServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    DbDescriptorServiceApi apiInstance = new DbDescriptorServiceApi(defaultClient);
    TitaniumEnableDisableRequest body = new TitaniumEnableDisableRequest(); // TitaniumEnableDisableRequest | 
    try {
      TitaniumAcknowledgeResponse result = apiInstance.dbDescriptorServiceDisableDbDescriptor(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DbDescriptorServiceApi#dbDescriptorServiceDisableDbDescriptor");
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
| **body** | [**TitaniumEnableDisableRequest**](TitaniumEnableDisableRequest.md)|  | |

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

<a name="dbDescriptorServiceEnableDbDescriptor"></a>
# **dbDescriptorServiceEnableDbDescriptor**
> TitaniumAcknowledgeResponse dbDescriptorServiceEnableDbDescriptor(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DbDescriptorServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    DbDescriptorServiceApi apiInstance = new DbDescriptorServiceApi(defaultClient);
    TitaniumEnableDisableRequest body = new TitaniumEnableDisableRequest(); // TitaniumEnableDisableRequest | 
    try {
      TitaniumAcknowledgeResponse result = apiInstance.dbDescriptorServiceEnableDbDescriptor(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DbDescriptorServiceApi#dbDescriptorServiceEnableDbDescriptor");
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
| **body** | [**TitaniumEnableDisableRequest**](TitaniumEnableDisableRequest.md)|  | |

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

<a name="dbDescriptorServiceGetDbDescriptor"></a>
# **dbDescriptorServiceGetDbDescriptor**
> TitaniumDescriptorDefinitionResponse dbDescriptorServiceGetDbDescriptor(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DbDescriptorServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    DbDescriptorServiceApi apiInstance = new DbDescriptorServiceApi(defaultClient);
    TitaniumGetDefinition body = new TitaniumGetDefinition(); // TitaniumGetDefinition | 
    try {
      TitaniumDescriptorDefinitionResponse result = apiInstance.dbDescriptorServiceGetDbDescriptor(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DbDescriptorServiceApi#dbDescriptorServiceGetDbDescriptor");
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

[**TitaniumDescriptorDefinitionResponse**](TitaniumDescriptorDefinitionResponse.md)

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

<a name="dbDescriptorServiceGetDbDescriptorVersion"></a>
# **dbDescriptorServiceGetDbDescriptorVersion**
> TitaniumDescriptorDefinitionResponse dbDescriptorServiceGetDbDescriptorVersion(name, versionId, scope, descriptorName)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DbDescriptorServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    DbDescriptorServiceApi apiInstance = new DbDescriptorServiceApi(defaultClient);
    String name = "name_example"; // String | 
    String versionId = "versionId_example"; // String | 
    String scope = "scope_example"; // String | 
    String descriptorName = "descriptorName_example"; // String | 
    try {
      TitaniumDescriptorDefinitionResponse result = apiInstance.dbDescriptorServiceGetDbDescriptorVersion(name, versionId, scope, descriptorName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DbDescriptorServiceApi#dbDescriptorServiceGetDbDescriptorVersion");
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
| **versionId** | **String**|  | |
| **scope** | **String**|  | [optional] |
| **descriptorName** | **String**|  | [optional] |

### Return type

[**TitaniumDescriptorDefinitionResponse**](TitaniumDescriptorDefinitionResponse.md)

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

<a name="dbDescriptorServiceListDbDescriptorVersions"></a>
# **dbDescriptorServiceListDbDescriptorVersions**
> TitaniumListVersionResponse dbDescriptorServiceListDbDescriptorVersions(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DbDescriptorServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    DbDescriptorServiceApi apiInstance = new DbDescriptorServiceApi(defaultClient);
    TitaniumGetDefinition body = new TitaniumGetDefinition(); // TitaniumGetDefinition | 
    try {
      TitaniumListVersionResponse result = apiInstance.dbDescriptorServiceListDbDescriptorVersions(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DbDescriptorServiceApi#dbDescriptorServiceListDbDescriptorVersions");
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

<a name="dbDescriptorServiceListDbDescriptors"></a>
# **dbDescriptorServiceListDbDescriptors**
> TitaniumDescriptorList dbDescriptorServiceListDbDescriptors(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DbDescriptorServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    DbDescriptorServiceApi apiInstance = new DbDescriptorServiceApi(defaultClient);
    TitaniumListRequest body = new TitaniumListRequest(); // TitaniumListRequest | 
    try {
      TitaniumDescriptorList result = apiInstance.dbDescriptorServiceListDbDescriptors(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DbDescriptorServiceApi#dbDescriptorServiceListDbDescriptors");
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

[**TitaniumDescriptorList**](TitaniumDescriptorList.md)

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

