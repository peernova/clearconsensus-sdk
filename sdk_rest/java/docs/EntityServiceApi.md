# EntityServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**entityServiceCreate**](EntityServiceApi.md#entityServiceCreate) | **POST** /api/v1/user-management/entities/create |  |
| [**entityServiceFind**](EntityServiceApi.md#entityServiceFind) | **POST** /api/v1/user-management/entities |  |
| [**entityServiceGetAllEnabledOnly**](EntityServiceApi.md#entityServiceGetAllEnabledOnly) | **GET** /api/v1/user-management/entities |  |
| [**entityServiceGetById**](EntityServiceApi.md#entityServiceGetById) | **GET** /api/v1/user-management/entities/{id} |  |
| [**entityServiceUpdate**](EntityServiceApi.md#entityServiceUpdate) | **PUT** /api/v1/user-management/entities/{id} |  |


<a name="entityServiceCreate"></a>
# **entityServiceCreate**
> ProtoEntityResponse entityServiceCreate(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntityServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    EntityServiceApi apiInstance = new EntityServiceApi(defaultClient);
    ProtoEntityDto body = new ProtoEntityDto(); // ProtoEntityDto | 
    try {
      ProtoEntityResponse result = apiInstance.entityServiceCreate(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntityServiceApi#entityServiceCreate");
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
| **body** | [**ProtoEntityDto**](ProtoEntityDto.md)|  | |

### Return type

[**ProtoEntityResponse**](ProtoEntityResponse.md)

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

<a name="entityServiceFind"></a>
# **entityServiceFind**
> ProtoTableResponse entityServiceFind(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntityServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    EntityServiceApi apiInstance = new EntityServiceApi(defaultClient);
    ProtoSearchCriteria body = new ProtoSearchCriteria(); // ProtoSearchCriteria | 
    try {
      ProtoTableResponse result = apiInstance.entityServiceFind(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntityServiceApi#entityServiceFind");
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
| **body** | [**ProtoSearchCriteria**](ProtoSearchCriteria.md)|  | |

### Return type

[**ProtoTableResponse**](ProtoTableResponse.md)

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

<a name="entityServiceGetAllEnabledOnly"></a>
# **entityServiceGetAllEnabledOnly**
> ProtoEntitiesResponse entityServiceGetAllEnabledOnly()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntityServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    EntityServiceApi apiInstance = new EntityServiceApi(defaultClient);
    try {
      ProtoEntitiesResponse result = apiInstance.entityServiceGetAllEnabledOnly();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntityServiceApi#entityServiceGetAllEnabledOnly");
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

[**ProtoEntitiesResponse**](ProtoEntitiesResponse.md)

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

<a name="entityServiceGetById"></a>
# **entityServiceGetById**
> ProtoEntityResponse entityServiceGetById(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntityServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    EntityServiceApi apiInstance = new EntityServiceApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      ProtoEntityResponse result = apiInstance.entityServiceGetById(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntityServiceApi#entityServiceGetById");
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
| **id** | **String**|  | |

### Return type

[**ProtoEntityResponse**](ProtoEntityResponse.md)

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

<a name="entityServiceUpdate"></a>
# **entityServiceUpdate**
> ProtoEntityResponse entityServiceUpdate(id, body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntityServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    EntityServiceApi apiInstance = new EntityServiceApi(defaultClient);
    String id = "id_example"; // String | 
    EntityServiceUpdateRequest body = new EntityServiceUpdateRequest(); // EntityServiceUpdateRequest | 
    try {
      ProtoEntityResponse result = apiInstance.entityServiceUpdate(id, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntityServiceApi#entityServiceUpdate");
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
| **id** | **String**|  | |
| **body** | [**EntityServiceUpdateRequest**](EntityServiceUpdateRequest.md)|  | |

### Return type

[**ProtoEntityResponse**](ProtoEntityResponse.md)

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

