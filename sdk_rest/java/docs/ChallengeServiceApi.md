# ChallengeServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**challengeServiceChallengeCreate**](ChallengeServiceApi.md#challengeServiceChallengeCreate) | **POST** /api/v1/challenge/create | ChallengeCreate creates challenge in the system.(Initiate process by dealer) To create \&quot;challenger\&quot; needs to be authorised and challenge can be created only if one of their own submitted data points has been declared an outlier in the published Consensus. Need to specify asset and fill out evidence information. Returns response that contains ticket ID of the Challenge or the Error. |
| [**challengeServiceChallengeFormMeta**](ChallengeServiceApi.md#challengeServiceChallengeFormMeta) | **POST** /api/v1/challenge/form-meta | ChallengeFormMeta is used to request information(template) about the form fields required to submit a challenge for a specific asset and evidence type. Returns response with template with pre-filled data. |
| [**challengeServiceChallengeFreezeStatus**](ChallengeServiceApi.md#challengeServiceChallengeFreezeStatus) | **POST** /api/v1/challenge/freeze/status | ChallengeFreezeStatus returns StatusResponse that contains string that represents freeze status of challenges if the challenge process is stopped and nothing if the one is not. Challenge can be stopped by operator.Dealer can see the freeze status using this method. Need to specify consensus(where outliers exists) run timestamp. |
| [**challengeServiceGetChallengeAttachmentUploadUrl**](ChallengeServiceApi.md#challengeServiceGetChallengeAttachmentUploadUrl) | **POST** /api/v1/challenge/attachment_upload_urls | GetChallengeAttachmentUploadUrl returns string that represents s3 URL that can be used to upload attachment for the challenge. The file in attachment can be any file that provides additional information about the disputable outlier. Need to specify asset ID, submitted ID and file name. |
| [**challengeServiceGetChallengeDetails**](ChallengeServiceApi.md#challengeServiceGetChallengeDetails) | **POST** /api/v1/challenge-details |  |


<a name="challengeServiceChallengeCreate"></a>
# **challengeServiceChallengeCreate**
> TitaniumChallengeCreateResponse challengeServiceChallengeCreate(body)

ChallengeCreate creates challenge in the system.(Initiate process by dealer) To create \&quot;challenger\&quot; needs to be authorised and challenge can be created only if one of their own submitted data points has been declared an outlier in the published Consensus. Need to specify asset and fill out evidence information. Returns response that contains ticket ID of the Challenge or the Error.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChallengeServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    ChallengeServiceApi apiInstance = new ChallengeServiceApi(defaultClient);
    TitaniumChallengeCreateRequest body = new TitaniumChallengeCreateRequest(); // TitaniumChallengeCreateRequest | 
    try {
      TitaniumChallengeCreateResponse result = apiInstance.challengeServiceChallengeCreate(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChallengeServiceApi#challengeServiceChallengeCreate");
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
| **body** | [**TitaniumChallengeCreateRequest**](TitaniumChallengeCreateRequest.md)|  | |

### Return type

[**TitaniumChallengeCreateResponse**](TitaniumChallengeCreateResponse.md)

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

<a name="challengeServiceChallengeFormMeta"></a>
# **challengeServiceChallengeFormMeta**
> TitaniumChallengeFormMetaResponse challengeServiceChallengeFormMeta(body)

ChallengeFormMeta is used to request information(template) about the form fields required to submit a challenge for a specific asset and evidence type. Returns response with template with pre-filled data.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChallengeServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    ChallengeServiceApi apiInstance = new ChallengeServiceApi(defaultClient);
    TitaniumChallengeFormMetaRequest body = new TitaniumChallengeFormMetaRequest(); // TitaniumChallengeFormMetaRequest | 
    try {
      TitaniumChallengeFormMetaResponse result = apiInstance.challengeServiceChallengeFormMeta(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChallengeServiceApi#challengeServiceChallengeFormMeta");
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
| **body** | [**TitaniumChallengeFormMetaRequest**](TitaniumChallengeFormMetaRequest.md)|  | |

### Return type

[**TitaniumChallengeFormMetaResponse**](TitaniumChallengeFormMetaResponse.md)

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

<a name="challengeServiceChallengeFreezeStatus"></a>
# **challengeServiceChallengeFreezeStatus**
> TitaniumStatusResponse challengeServiceChallengeFreezeStatus(body)

ChallengeFreezeStatus returns StatusResponse that contains string that represents freeze status of challenges if the challenge process is stopped and nothing if the one is not. Challenge can be stopped by operator.Dealer can see the freeze status using this method. Need to specify consensus(where outliers exists) run timestamp.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChallengeServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    ChallengeServiceApi apiInstance = new ChallengeServiceApi(defaultClient);
    TitaniumChallengeFreezeStatusRequest body = new TitaniumChallengeFreezeStatusRequest(); // TitaniumChallengeFreezeStatusRequest | 
    try {
      TitaniumStatusResponse result = apiInstance.challengeServiceChallengeFreezeStatus(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChallengeServiceApi#challengeServiceChallengeFreezeStatus");
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
| **body** | [**TitaniumChallengeFreezeStatusRequest**](TitaniumChallengeFreezeStatusRequest.md)|  | |

### Return type

[**TitaniumStatusResponse**](TitaniumStatusResponse.md)

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

<a name="challengeServiceGetChallengeAttachmentUploadUrl"></a>
# **challengeServiceGetChallengeAttachmentUploadUrl**
> TitaniumGetAttachmentUploadUrlResponse challengeServiceGetChallengeAttachmentUploadUrl(body)

GetChallengeAttachmentUploadUrl returns string that represents s3 URL that can be used to upload attachment for the challenge. The file in attachment can be any file that provides additional information about the disputable outlier. Need to specify asset ID, submitted ID and file name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChallengeServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    ChallengeServiceApi apiInstance = new ChallengeServiceApi(defaultClient);
    TitaniumGetAttachmentUploadUrlRequest body = new TitaniumGetAttachmentUploadUrlRequest(); // TitaniumGetAttachmentUploadUrlRequest | 
    try {
      TitaniumGetAttachmentUploadUrlResponse result = apiInstance.challengeServiceGetChallengeAttachmentUploadUrl(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChallengeServiceApi#challengeServiceGetChallengeAttachmentUploadUrl");
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
| **body** | [**TitaniumGetAttachmentUploadUrlRequest**](TitaniumGetAttachmentUploadUrlRequest.md)|  | |

### Return type

[**TitaniumGetAttachmentUploadUrlResponse**](TitaniumGetAttachmentUploadUrlResponse.md)

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

<a name="challengeServiceGetChallengeDetails"></a>
# **challengeServiceGetChallengeDetails**
> TitaniumGetChallengeDetailsResponse challengeServiceGetChallengeDetails(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChallengeServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    ChallengeServiceApi apiInstance = new ChallengeServiceApi(defaultClient);
    TitaniumGetChallengeDetailsRequest body = new TitaniumGetChallengeDetailsRequest(); // TitaniumGetChallengeDetailsRequest | 
    try {
      TitaniumGetChallengeDetailsResponse result = apiInstance.challengeServiceGetChallengeDetails(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChallengeServiceApi#challengeServiceGetChallengeDetails");
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
| **body** | [**TitaniumGetChallengeDetailsRequest**](TitaniumGetChallengeDetailsRequest.md)|  | |

### Return type

[**TitaniumGetChallengeDetailsResponse**](TitaniumGetChallengeDetailsResponse.md)

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

