# SupportedFieldsServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**supportedFieldsServiceGetSupportedFieldsValues**](SupportedFieldsServiceApi.md#supportedFieldsServiceGetSupportedFieldsValues) | **POST** /api/v1/list/field-values |  |
| [**supportedFieldsServiceListSupportedFields**](SupportedFieldsServiceApi.md#supportedFieldsServiceListSupportedFields) | **POST** /api/v1/list/fields |  |


<a name="supportedFieldsServiceGetSupportedFieldsValues"></a>
# **supportedFieldsServiceGetSupportedFieldsValues**
> TitaniumGetFieldValuesResponse supportedFieldsServiceGetSupportedFieldsValues(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SupportedFieldsServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    SupportedFieldsServiceApi apiInstance = new SupportedFieldsServiceApi(defaultClient);
    TitaniumSupportedField body = new TitaniumSupportedField(); // TitaniumSupportedField | 
    try {
      TitaniumGetFieldValuesResponse result = apiInstance.supportedFieldsServiceGetSupportedFieldsValues(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SupportedFieldsServiceApi#supportedFieldsServiceGetSupportedFieldsValues");
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
| **body** | [**TitaniumSupportedField**](TitaniumSupportedField.md)|  | |

### Return type

[**TitaniumGetFieldValuesResponse**](TitaniumGetFieldValuesResponse.md)

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

<a name="supportedFieldsServiceListSupportedFields"></a>
# **supportedFieldsServiceListSupportedFields**
> TitaniumGetSupportedFieldsResponse supportedFieldsServiceListSupportedFields(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SupportedFieldsServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    SupportedFieldsServiceApi apiInstance = new SupportedFieldsServiceApi(defaultClient);
    TitaniumGetSupportedFields body = new TitaniumGetSupportedFields(); // TitaniumGetSupportedFields | 
    try {
      TitaniumGetSupportedFieldsResponse result = apiInstance.supportedFieldsServiceListSupportedFields(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SupportedFieldsServiceApi#supportedFieldsServiceListSupportedFields");
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
| **body** | [**TitaniumGetSupportedFields**](TitaniumGetSupportedFields.md)|  | |

### Return type

[**TitaniumGetSupportedFieldsResponse**](TitaniumGetSupportedFieldsResponse.md)

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

