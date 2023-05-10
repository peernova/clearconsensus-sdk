# AnalyticsControllerApi

All URIs are relative to *http://api-dev.clearconsensus.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**analyticsControllerFindConsensusAnalytics**](AnalyticsControllerApi.md#analyticsControllerFindConsensusAnalytics) | **POST** /api/v1/analytics/consensus/find | FindConsensusAnalytics returns analytics related to specific consensus according to request. |
| [**analyticsControllerFindDataQualityErrors**](AnalyticsControllerApi.md#analyticsControllerFindDataQualityErrors) | **POST** /api/v1/analytics/data-quality-errors/find | FindDataQualityErrors returns data quality errors according to request. |
| [**analyticsControllerGetAllConsensusAnalytics**](AnalyticsControllerApi.md#analyticsControllerGetAllConsensusAnalytics) | **POST** /api/v1/analytics/consensus/get-all | GetAllConsensusAnalytics returns analytics related to all consensuses. |
| [**analyticsControllerGetAllDataQualityErrors**](AnalyticsControllerApi.md#analyticsControllerGetAllDataQualityErrors) | **POST** /api/v1/analytics/data-quality-errors/get-all | GetAllDataQualityErrors returns all existing data quality errors in the system. |
| [**analyticsControllerGetHistogram**](AnalyticsControllerApi.md#analyticsControllerGetHistogram) | **POST** /api/v1/analytics/histogram/get-all | GetHistogram returns analytics(submission and consensus) represented by histogram according to request. |
| [**analyticsControllerGetPredefinedFilter**](AnalyticsControllerApi.md#analyticsControllerGetPredefinedFilter) | **POST** /api/v1/analytics/predefined/filters | GetPredefinedFilter returns pre defined filters according to request. |


<a name="analyticsControllerFindConsensusAnalytics"></a>
# **analyticsControllerFindConsensusAnalytics**
> TitaniumGenericChartMetadataDataQualityResponse analyticsControllerFindConsensusAnalytics(body)

FindConsensusAnalytics returns analytics related to specific consensus according to request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    AnalyticsControllerApi apiInstance = new AnalyticsControllerApi(defaultClient);
    TitaniumGenericChartMetadataDataQuality body = new TitaniumGenericChartMetadataDataQuality(); // TitaniumGenericChartMetadataDataQuality | 
    try {
      TitaniumGenericChartMetadataDataQualityResponse result = apiInstance.analyticsControllerFindConsensusAnalytics(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsControllerApi#analyticsControllerFindConsensusAnalytics");
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
| **body** | [**TitaniumGenericChartMetadataDataQuality**](TitaniumGenericChartMetadataDataQuality.md)|  | |

### Return type

[**TitaniumGenericChartMetadataDataQualityResponse**](TitaniumGenericChartMetadataDataQualityResponse.md)

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

<a name="analyticsControllerFindDataQualityErrors"></a>
# **analyticsControllerFindDataQualityErrors**
> TitaniumGenericChartMetadataDataQualityResponse analyticsControllerFindDataQualityErrors(body)

FindDataQualityErrors returns data quality errors according to request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    AnalyticsControllerApi apiInstance = new AnalyticsControllerApi(defaultClient);
    TitaniumGenericChartMetadataDataQuality body = new TitaniumGenericChartMetadataDataQuality(); // TitaniumGenericChartMetadataDataQuality | 
    try {
      TitaniumGenericChartMetadataDataQualityResponse result = apiInstance.analyticsControllerFindDataQualityErrors(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsControllerApi#analyticsControllerFindDataQualityErrors");
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
| **body** | [**TitaniumGenericChartMetadataDataQuality**](TitaniumGenericChartMetadataDataQuality.md)|  | |

### Return type

[**TitaniumGenericChartMetadataDataQualityResponse**](TitaniumGenericChartMetadataDataQualityResponse.md)

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

<a name="analyticsControllerGetAllConsensusAnalytics"></a>
# **analyticsControllerGetAllConsensusAnalytics**
> TitaniumGenericChartMetadataDataQualityResponse analyticsControllerGetAllConsensusAnalytics()

GetAllConsensusAnalytics returns analytics related to all consensuses.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    AnalyticsControllerApi apiInstance = new AnalyticsControllerApi(defaultClient);
    try {
      TitaniumGenericChartMetadataDataQualityResponse result = apiInstance.analyticsControllerGetAllConsensusAnalytics();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsControllerApi#analyticsControllerGetAllConsensusAnalytics");
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

[**TitaniumGenericChartMetadataDataQualityResponse**](TitaniumGenericChartMetadataDataQualityResponse.md)

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

<a name="analyticsControllerGetAllDataQualityErrors"></a>
# **analyticsControllerGetAllDataQualityErrors**
> TitaniumGenericChartMetadataDataQualityResponse analyticsControllerGetAllDataQualityErrors()

GetAllDataQualityErrors returns all existing data quality errors in the system.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    AnalyticsControllerApi apiInstance = new AnalyticsControllerApi(defaultClient);
    try {
      TitaniumGenericChartMetadataDataQualityResponse result = apiInstance.analyticsControllerGetAllDataQualityErrors();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsControllerApi#analyticsControllerGetAllDataQualityErrors");
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

[**TitaniumGenericChartMetadataDataQualityResponse**](TitaniumGenericChartMetadataDataQualityResponse.md)

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

<a name="analyticsControllerGetHistogram"></a>
# **analyticsControllerGetHistogram**
> TitaniumHistogramResponse analyticsControllerGetHistogram()

GetHistogram returns analytics(submission and consensus) represented by histogram according to request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    AnalyticsControllerApi apiInstance = new AnalyticsControllerApi(defaultClient);
    try {
      TitaniumHistogramResponse result = apiInstance.analyticsControllerGetHistogram();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsControllerApi#analyticsControllerGetHistogram");
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

[**TitaniumHistogramResponse**](TitaniumHistogramResponse.md)

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

<a name="analyticsControllerGetPredefinedFilter"></a>
# **analyticsControllerGetPredefinedFilter**
> TitaniumGetPredefinedFiltersResponse analyticsControllerGetPredefinedFilter()

GetPredefinedFilter returns pre defined filters according to request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    AnalyticsControllerApi apiInstance = new AnalyticsControllerApi(defaultClient);
    try {
      TitaniumGetPredefinedFiltersResponse result = apiInstance.analyticsControllerGetPredefinedFilter();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsControllerApi#analyticsControllerGetPredefinedFilter");
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

[**TitaniumGetPredefinedFiltersResponse**](TitaniumGetPredefinedFiltersResponse.md)

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

