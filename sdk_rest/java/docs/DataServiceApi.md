# DataServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**dataServiceAuthorizeUpload**](DataServiceApi.md#dataServiceAuthorizeUpload) | **POST** /api/v1/internal/upload/authorize | AuthorizeUpload shows availability of uploading for user. |
| [**dataServiceExport**](DataServiceApi.md#dataServiceExport) | **POST** /api/v1/export | Export exports data according to the request. |
| [**dataServiceNotifyUpload**](DataServiceApi.md#dataServiceNotifyUpload) | **POST** /api/v1/internal/upload/notify | NotifyUpload returns message with notify that data was uploaded according to url in request. |
| [**dataServiceSubmitted**](DataServiceApi.md#dataServiceSubmitted) | **POST** /api/v1/submitted | Submitted returns submitted data based on the request made. |
| [**dataServiceUploadURL**](DataServiceApi.md#dataServiceUploadURL) | **POST** /api/v1/upload/url | UploadURL returns a pre-signed S3 URL for uploading data. |


<a name="dataServiceAuthorizeUpload"></a>
# **dataServiceAuthorizeUpload**
> TitaniumUploadAuthorizationResponse dataServiceAuthorizeUpload(body)

AuthorizeUpload shows availability of uploading for user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    DataServiceApi apiInstance = new DataServiceApi(defaultClient);
    TitaniumUploadURLRequest body = new TitaniumUploadURLRequest(); // TitaniumUploadURLRequest | 
    try {
      TitaniumUploadAuthorizationResponse result = apiInstance.dataServiceAuthorizeUpload(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataServiceApi#dataServiceAuthorizeUpload");
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
| **body** | [**TitaniumUploadURLRequest**](TitaniumUploadURLRequest.md)|  | |

### Return type

[**TitaniumUploadAuthorizationResponse**](TitaniumUploadAuthorizationResponse.md)

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

<a name="dataServiceExport"></a>
# **dataServiceExport**
> TitaniumExportResponse dataServiceExport(body)

Export exports data according to the request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    DataServiceApi apiInstance = new DataServiceApi(defaultClient);
    TitaniumExportRequest body = new TitaniumExportRequest(); // TitaniumExportRequest | 
    try {
      TitaniumExportResponse result = apiInstance.dataServiceExport(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataServiceApi#dataServiceExport");
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
| **body** | [**TitaniumExportRequest**](TitaniumExportRequest.md)|  | |

### Return type

[**TitaniumExportResponse**](TitaniumExportResponse.md)

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

<a name="dataServiceNotifyUpload"></a>
# **dataServiceNotifyUpload**
> TitaniumMessageResponse dataServiceNotifyUpload(body)

NotifyUpload returns message with notify that data was uploaded according to url in request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    DataServiceApi apiInstance = new DataServiceApi(defaultClient);
    TitaniumUploadNotifyRequest body = new TitaniumUploadNotifyRequest(); // TitaniumUploadNotifyRequest | 
    try {
      TitaniumMessageResponse result = apiInstance.dataServiceNotifyUpload(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataServiceApi#dataServiceNotifyUpload");
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
| **body** | [**TitaniumUploadNotifyRequest**](TitaniumUploadNotifyRequest.md)|  | |

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

<a name="dataServiceSubmitted"></a>
# **dataServiceSubmitted**
> TitaniumSubmittedResponse dataServiceSubmitted(body)

Submitted returns submitted data based on the request made.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    DataServiceApi apiInstance = new DataServiceApi(defaultClient);
    TitaniumSubmittedRequest body = new TitaniumSubmittedRequest(); // TitaniumSubmittedRequest | 
    try {
      TitaniumSubmittedResponse result = apiInstance.dataServiceSubmitted(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataServiceApi#dataServiceSubmitted");
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
| **body** | [**TitaniumSubmittedRequest**](TitaniumSubmittedRequest.md)|  | |

### Return type

[**TitaniumSubmittedResponse**](TitaniumSubmittedResponse.md)

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

<a name="dataServiceUploadURL"></a>
# **dataServiceUploadURL**
> TitaniumUploadURLResponse dataServiceUploadURL(body)

UploadURL returns a pre-signed S3 URL for uploading data.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    DataServiceApi apiInstance = new DataServiceApi(defaultClient);
    TitaniumUploadURLRequest body = new TitaniumUploadURLRequest(); // TitaniumUploadURLRequest | 
    try {
      TitaniumUploadURLResponse result = apiInstance.dataServiceUploadURL(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataServiceApi#dataServiceUploadURL");
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
| **body** | [**TitaniumUploadURLRequest**](TitaniumUploadURLRequest.md)|  | |

### Return type

[**TitaniumUploadURLResponse**](TitaniumUploadURLResponse.md)

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

