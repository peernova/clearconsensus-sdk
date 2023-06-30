# EntityServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**entityServiceCreate**](EntityServiceApi.md#entityServiceCreate) | **POST** /api/v1/user-management/entities/create |  |
| [**entityServiceFind**](EntityServiceApi.md#entityServiceFind) | **POST** /api/v1/user-management/entities/find |  |
| [**entityServiceGetAllEnabledOnly**](EntityServiceApi.md#entityServiceGetAllEnabledOnly) | **POST** /api/v1/user-management/entities/getAllByEnabled |  |
| [**entityServiceGetById**](EntityServiceApi.md#entityServiceGetById) | **POST** /api/v1/user-management/entities/getById |  |
| [**entityServiceUpdate**](EntityServiceApi.md#entityServiceUpdate) | **POST** /api/v1/user-management/entities/update |  |


<a name="entityServiceCreate"></a>
# **entityServiceCreate**
> ProtoServiceResponse entityServiceCreate(body)



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
      ProtoServiceResponse result = apiInstance.entityServiceCreate(body);
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

[**ProtoServiceResponse**](ProtoServiceResponse.md)

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
> ProtoServiceResponse entityServiceFind(body)



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
      ProtoServiceResponse result = apiInstance.entityServiceFind(body);
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

[**ProtoServiceResponse**](ProtoServiceResponse.md)

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
> ProtoServiceResponse entityServiceGetAllEnabledOnly(body)



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
    Boolean body = true; // Boolean | 
    try {
      ProtoServiceResponse result = apiInstance.entityServiceGetAllEnabledOnly(body);
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

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **body** | **Boolean**|  | |

### Return type

[**ProtoServiceResponse**](ProtoServiceResponse.md)

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
> ProtoServiceResponse entityServiceGetById(body)



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
    String body = "body_example"; // String | 
    try {
      ProtoServiceResponse result = apiInstance.entityServiceGetById(body);
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
| **body** | **String**|  | |

### Return type

[**ProtoServiceResponse**](ProtoServiceResponse.md)

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
> ProtoServiceResponse entityServiceUpdate(body)



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
      ProtoServiceResponse result = apiInstance.entityServiceUpdate(body);
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
| **body** | [**ProtoEntityDto**](ProtoEntityDto.md)|  | |

### Return type

[**ProtoServiceResponse**](ProtoServiceResponse.md)

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

