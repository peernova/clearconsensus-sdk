# LookupTableServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**lookupTableServiceAddLookupTable**](LookupTableServiceApi.md#lookupTableServiceAddLookupTable) | **POST** /api/v1/lookuptable/add |  |
| [**lookupTableServiceGetLookupTable**](LookupTableServiceApi.md#lookupTableServiceGetLookupTable) | **POST** /api/v1/lookuptable/get |  |
| [**lookupTableServiceListLookupTableVersions**](LookupTableServiceApi.md#lookupTableServiceListLookupTableVersions) | **POST** /api/v1/lookuptable/versions |  |
| [**lookupTableServiceListLookupTables**](LookupTableServiceApi.md#lookupTableServiceListLookupTables) | **POST** /api/v1/lookuptable/list |  |


<a name="lookupTableServiceAddLookupTable"></a>
# **lookupTableServiceAddLookupTable**
> TitaniumAcknowledgeResponse lookupTableServiceAddLookupTable(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LookupTableServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    LookupTableServiceApi apiInstance = new LookupTableServiceApi(defaultClient);
    TitaniumAddLookupTableRequest body = new TitaniumAddLookupTableRequest(); // TitaniumAddLookupTableRequest | 
    try {
      TitaniumAcknowledgeResponse result = apiInstance.lookupTableServiceAddLookupTable(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LookupTableServiceApi#lookupTableServiceAddLookupTable");
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
| **body** | [**TitaniumAddLookupTableRequest**](TitaniumAddLookupTableRequest.md)|  | |

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

<a name="lookupTableServiceGetLookupTable"></a>
# **lookupTableServiceGetLookupTable**
> TitaniumGetLookupTableResponse lookupTableServiceGetLookupTable(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LookupTableServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    LookupTableServiceApi apiInstance = new LookupTableServiceApi(defaultClient);
    TitaniumGetDefinition body = new TitaniumGetDefinition(); // TitaniumGetDefinition | 
    try {
      TitaniumGetLookupTableResponse result = apiInstance.lookupTableServiceGetLookupTable(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LookupTableServiceApi#lookupTableServiceGetLookupTable");
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

[**TitaniumGetLookupTableResponse**](TitaniumGetLookupTableResponse.md)

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

<a name="lookupTableServiceListLookupTableVersions"></a>
# **lookupTableServiceListLookupTableVersions**
> TitaniumListVersionResponse lookupTableServiceListLookupTableVersions(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LookupTableServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    LookupTableServiceApi apiInstance = new LookupTableServiceApi(defaultClient);
    TitaniumGetDefinition body = new TitaniumGetDefinition(); // TitaniumGetDefinition | 
    try {
      TitaniumListVersionResponse result = apiInstance.lookupTableServiceListLookupTableVersions(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LookupTableServiceApi#lookupTableServiceListLookupTableVersions");
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

<a name="lookupTableServiceListLookupTables"></a>
# **lookupTableServiceListLookupTables**
> TitaniumListLookupTableResponse lookupTableServiceListLookupTables(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LookupTableServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    LookupTableServiceApi apiInstance = new LookupTableServiceApi(defaultClient);
    TitaniumListRequest body = new TitaniumListRequest(); // TitaniumListRequest | 
    try {
      TitaniumListLookupTableResponse result = apiInstance.lookupTableServiceListLookupTables(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LookupTableServiceApi#lookupTableServiceListLookupTables");
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

[**TitaniumListLookupTableResponse**](TitaniumListLookupTableResponse.md)

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

