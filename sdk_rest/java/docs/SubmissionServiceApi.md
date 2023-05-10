# SubmissionServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**submissionServiceGetFilesView**](SubmissionServiceApi.md#submissionServiceGetFilesView) | **POST** /api/v1/submission/files-view | GetFilesView returns information about submitted to s3 storage files. |


<a name="submissionServiceGetFilesView"></a>
# **submissionServiceGetFilesView**
> TitaniumGetSubmissionFilesResponse submissionServiceGetFilesView(body)

GetFilesView returns information about submitted to s3 storage files.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubmissionServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    SubmissionServiceApi apiInstance = new SubmissionServiceApi(defaultClient);
    TitaniumGetSubmissionFilesRequest body = new TitaniumGetSubmissionFilesRequest(); // TitaniumGetSubmissionFilesRequest | 
    try {
      TitaniumGetSubmissionFilesResponse result = apiInstance.submissionServiceGetFilesView(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubmissionServiceApi#submissionServiceGetFilesView");
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
| **body** | [**TitaniumGetSubmissionFilesRequest**](TitaniumGetSubmissionFilesRequest.md)|  | |

### Return type

[**TitaniumGetSubmissionFilesResponse**](TitaniumGetSubmissionFilesResponse.md)

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

