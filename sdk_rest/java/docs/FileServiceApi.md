# FileServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fileServiceFileHistory**](FileServiceApi.md#fileServiceFileHistory) | **POST** /api/v1/file-history | FileHistory retrieves the history for a specified file. |
| [**fileServiceFileSubmission**](FileServiceApi.md#fileServiceFileSubmission) | **POST** /api/v1/file-submission | FileSubmission submits a file for processing. |
| [**fileServiceGetFileDelimiter**](FileServiceApi.md#fileServiceGetFileDelimiter) | **POST** /api/v1/import/{filename}/delimiter | GetFileDelimiter retrieves the delimiter for a specified file. |
| [**fileServiceGetFileDescriptor**](FileServiceApi.md#fileServiceGetFileDescriptor) | **POST** /api/v1/import/{filename}/descriptor | GetFileDescriptor retrieves the descriptor for a specified file. |
| [**fileServiceGetFileExportUrl**](FileServiceApi.md#fileServiceGetFileExportUrl) | **POST** /api/v1/raw-file | GetFileExportUrl retrieves the export URL for a specified file. |
| [**fileServiceGetFilePreview**](FileServiceApi.md#fileServiceGetFilePreview) | **POST** /api/v1/import/{filename} | GetFilePreview retrieves a preview of a specified file. |
| [**fileServiceListFiles**](FileServiceApi.md#fileServiceListFiles) | **POST** /api/v1/import/list | ListFiles retrieves a list of files. |
| [**fileServiceSetFileDelimiter**](FileServiceApi.md#fileServiceSetFileDelimiter) | **POST** /api/v1/import/{fileIdentifier.filename}/delimiter | SetFileDelimiter sets the delimiter for a specified file. |
| [**fileServiceSetFileDescriptor**](FileServiceApi.md#fileServiceSetFileDescriptor) | **POST** /api/v1/import/{fileIdentifier.filename}/descriptor | SetFileDescriptor sets the descriptor for a specified file. |


<a name="fileServiceFileHistory"></a>
# **fileServiceFileHistory**
> TitaniumFileHistoryResponse fileServiceFileHistory(body)

FileHistory retrieves the history for a specified file.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FileServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    FileServiceApi apiInstance = new FileServiceApi(defaultClient);
    TitaniumFileHistoryRequest body = new TitaniumFileHistoryRequest(); // TitaniumFileHistoryRequest | 
    try {
      TitaniumFileHistoryResponse result = apiInstance.fileServiceFileHistory(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FileServiceApi#fileServiceFileHistory");
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
| **body** | [**TitaniumFileHistoryRequest**](TitaniumFileHistoryRequest.md)|  | |

### Return type

[**TitaniumFileHistoryResponse**](TitaniumFileHistoryResponse.md)

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

<a name="fileServiceFileSubmission"></a>
# **fileServiceFileSubmission**
> TitaniumMessageResponse fileServiceFileSubmission(body)

FileSubmission submits a file for processing.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FileServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    FileServiceApi apiInstance = new FileServiceApi(defaultClient);
    TitaniumFileSubmissionRequest body = new TitaniumFileSubmissionRequest(); // TitaniumFileSubmissionRequest | 
    try {
      TitaniumMessageResponse result = apiInstance.fileServiceFileSubmission(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FileServiceApi#fileServiceFileSubmission");
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
| **body** | [**TitaniumFileSubmissionRequest**](TitaniumFileSubmissionRequest.md)|  | |

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

<a name="fileServiceGetFileDelimiter"></a>
# **fileServiceGetFileDelimiter**
> TitaniumFileDelimiterSetting fileServiceGetFileDelimiter(filename, body)

GetFileDelimiter retrieves the delimiter for a specified file.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FileServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    FileServiceApi apiInstance = new FileServiceApi(defaultClient);
    String filename = "filename_example"; // String | 
    FileServiceGetFilePreviewRequest body = new FileServiceGetFilePreviewRequest(); // FileServiceGetFilePreviewRequest | 
    try {
      TitaniumFileDelimiterSetting result = apiInstance.fileServiceGetFileDelimiter(filename, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FileServiceApi#fileServiceGetFileDelimiter");
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
| **filename** | **String**|  | |
| **body** | [**FileServiceGetFilePreviewRequest**](FileServiceGetFilePreviewRequest.md)|  | |

### Return type

[**TitaniumFileDelimiterSetting**](TitaniumFileDelimiterSetting.md)

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

<a name="fileServiceGetFileDescriptor"></a>
# **fileServiceGetFileDescriptor**
> TitaniumFileDescriptorSetting fileServiceGetFileDescriptor(filename, body)

GetFileDescriptor retrieves the descriptor for a specified file.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FileServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    FileServiceApi apiInstance = new FileServiceApi(defaultClient);
    String filename = "filename_example"; // String | 
    FileServiceGetFilePreviewRequest body = new FileServiceGetFilePreviewRequest(); // FileServiceGetFilePreviewRequest | 
    try {
      TitaniumFileDescriptorSetting result = apiInstance.fileServiceGetFileDescriptor(filename, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FileServiceApi#fileServiceGetFileDescriptor");
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
| **filename** | **String**|  | |
| **body** | [**FileServiceGetFilePreviewRequest**](FileServiceGetFilePreviewRequest.md)|  | |

### Return type

[**TitaniumFileDescriptorSetting**](TitaniumFileDescriptorSetting.md)

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

<a name="fileServiceGetFileExportUrl"></a>
# **fileServiceGetFileExportUrl**
> TitaniumGetFileExportUrlResponse fileServiceGetFileExportUrl(body)

GetFileExportUrl retrieves the export URL for a specified file.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FileServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    FileServiceApi apiInstance = new FileServiceApi(defaultClient);
    TitaniumGetFileExportUrlRequest body = new TitaniumGetFileExportUrlRequest(); // TitaniumGetFileExportUrlRequest | 
    try {
      TitaniumGetFileExportUrlResponse result = apiInstance.fileServiceGetFileExportUrl(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FileServiceApi#fileServiceGetFileExportUrl");
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
| **body** | [**TitaniumGetFileExportUrlRequest**](TitaniumGetFileExportUrlRequest.md)|  | |

### Return type

[**TitaniumGetFileExportUrlResponse**](TitaniumGetFileExportUrlResponse.md)

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

<a name="fileServiceGetFilePreview"></a>
# **fileServiceGetFilePreview**
> TitaniumFilePreview fileServiceGetFilePreview(filename, body)

GetFilePreview retrieves a preview of a specified file.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FileServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    FileServiceApi apiInstance = new FileServiceApi(defaultClient);
    String filename = "filename_example"; // String | 
    FileServiceGetFilePreviewRequest body = new FileServiceGetFilePreviewRequest(); // FileServiceGetFilePreviewRequest | 
    try {
      TitaniumFilePreview result = apiInstance.fileServiceGetFilePreview(filename, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FileServiceApi#fileServiceGetFilePreview");
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
| **filename** | **String**|  | |
| **body** | [**FileServiceGetFilePreviewRequest**](FileServiceGetFilePreviewRequest.md)|  | |

### Return type

[**TitaniumFilePreview**](TitaniumFilePreview.md)

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

<a name="fileServiceListFiles"></a>
# **fileServiceListFiles**
> TitaniumFileList fileServiceListFiles(body)

ListFiles retrieves a list of files.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FileServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    FileServiceApi apiInstance = new FileServiceApi(defaultClient);
    TitaniumListRequest body = new TitaniumListRequest(); // TitaniumListRequest | 
    try {
      TitaniumFileList result = apiInstance.fileServiceListFiles(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FileServiceApi#fileServiceListFiles");
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

[**TitaniumFileList**](TitaniumFileList.md)

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

<a name="fileServiceSetFileDelimiter"></a>
# **fileServiceSetFileDelimiter**
> Object fileServiceSetFileDelimiter(fileIdentifierFilename, body)

SetFileDelimiter sets the delimiter for a specified file.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FileServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    FileServiceApi apiInstance = new FileServiceApi(defaultClient);
    String fileIdentifierFilename = "fileIdentifierFilename_example"; // String | 
    TitaniumSetFileDelimiterRequest body = new TitaniumSetFileDelimiterRequest(); // TitaniumSetFileDelimiterRequest | 
    try {
      Object result = apiInstance.fileServiceSetFileDelimiter(fileIdentifierFilename, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FileServiceApi#fileServiceSetFileDelimiter");
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
| **fileIdentifierFilename** | **String**|  | |
| **body** | [**TitaniumSetFileDelimiterRequest**](TitaniumSetFileDelimiterRequest.md)|  | |

### Return type

**Object**

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

<a name="fileServiceSetFileDescriptor"></a>
# **fileServiceSetFileDescriptor**
> Object fileServiceSetFileDescriptor(fileIdentifierFilename, body)

SetFileDescriptor sets the descriptor for a specified file.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FileServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    FileServiceApi apiInstance = new FileServiceApi(defaultClient);
    String fileIdentifierFilename = "fileIdentifierFilename_example"; // String | 
    TitaniumSetFileDescriptorRequest body = new TitaniumSetFileDescriptorRequest(); // TitaniumSetFileDescriptorRequest | 
    try {
      Object result = apiInstance.fileServiceSetFileDescriptor(fileIdentifierFilename, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FileServiceApi#fileServiceSetFileDescriptor");
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
| **fileIdentifierFilename** | **String**|  | |
| **body** | [**TitaniumSetFileDescriptorRequest**](TitaniumSetFileDescriptorRequest.md)|  | |

### Return type

**Object**

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

