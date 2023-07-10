# OperatorServicePrivateApi

All URIs are relative to *http://api-dev.clearconsensus.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**operatorServicePrivateAddAsset**](OperatorServicePrivateApi.md#operatorServicePrivateAddAsset) | **POST** /api/v1/operator/assets/add | AddAsset adds asset to the system. |
| [**operatorServicePrivateAddClient**](OperatorServicePrivateApi.md#operatorServicePrivateAddClient) | **POST** /api/v1/operator/client/add |  |
| [**operatorServicePrivateAddSupportedFields**](OperatorServicePrivateApi.md#operatorServicePrivateAddSupportedFields) | **POST** /api/v1/operator/add/field-values |  |
| [**operatorServicePrivateAssets**](OperatorServicePrivateApi.md#operatorServicePrivateAssets) | **POST** /api/v1/operator/assets |  |
| [**operatorServicePrivateCreateSupportedFields**](OperatorServicePrivateApi.md#operatorServicePrivateCreateSupportedFields) | **POST** /api/v1/operator/create/field-values |  |
| [**operatorServicePrivateDeleteSupportedFields**](OperatorServicePrivateApi.md#operatorServicePrivateDeleteSupportedFields) | **POST** /api/v1/operator/delete/field-values |  |
| [**operatorServicePrivateEvpStatuses**](OperatorServicePrivateApi.md#operatorServicePrivateEvpStatuses) | **POST** /api/v1/operator/evaluated-prices/slice |  |
| [**operatorServicePrivateExportReport**](OperatorServicePrivateApi.md#operatorServicePrivateExportReport) | **POST** /api/v1/operator/report | ExportReport returns pre signed s3 urls which can be used for export report(and compression type) |
| [**operatorServicePrivateListClients**](OperatorServicePrivateApi.md#operatorServicePrivateListClients) | **GET** /api/v1/operator/client/list |  |
| [**operatorServicePrivateOperatorOutliers**](OperatorServicePrivateApi.md#operatorServicePrivateOperatorOutliers) | **POST** /api/v1/operator-outliers |  |
| [**operatorServicePrivateOutliers**](OperatorServicePrivateApi.md#operatorServicePrivateOutliers) | **POST** /api/v1/operator/outliers |  |
| [**operatorServicePrivateRecentAssets**](OperatorServicePrivateApi.md#operatorServicePrivateRecentAssets) | **POST** /api/v1/operator/recentassets |  |
| [**operatorServicePrivateUploadDTCC**](OperatorServicePrivateApi.md#operatorServicePrivateUploadDTCC) | **POST** /api/v1/operator/dtcc-trades/upload |  |
| [**operatorServicePrivateUploadEVP**](OperatorServicePrivateApi.md#operatorServicePrivateUploadEVP) | **POST** /api/v1/operator/evp/upload |  |


<a name="operatorServicePrivateAddAsset"></a>
# **operatorServicePrivateAddAsset**
> TitaniumMessageResponse operatorServicePrivateAddAsset(body)

AddAsset adds asset to the system.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OperatorServicePrivateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    OperatorServicePrivateApi apiInstance = new OperatorServicePrivateApi(defaultClient);
    TitaniumAddAssetRequest body = new TitaniumAddAssetRequest(); // TitaniumAddAssetRequest | 
    try {
      TitaniumMessageResponse result = apiInstance.operatorServicePrivateAddAsset(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OperatorServicePrivateApi#operatorServicePrivateAddAsset");
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
| **body** | [**TitaniumAddAssetRequest**](TitaniumAddAssetRequest.md)|  | |

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

<a name="operatorServicePrivateAddClient"></a>
# **operatorServicePrivateAddClient**
> TitaniumMessageResponse operatorServicePrivateAddClient(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OperatorServicePrivateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    OperatorServicePrivateApi apiInstance = new OperatorServicePrivateApi(defaultClient);
    TitaniumClientName body = new TitaniumClientName(); // TitaniumClientName | 
    try {
      TitaniumMessageResponse result = apiInstance.operatorServicePrivateAddClient(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OperatorServicePrivateApi#operatorServicePrivateAddClient");
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
| **body** | [**TitaniumClientName**](TitaniumClientName.md)|  | |

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

<a name="operatorServicePrivateAddSupportedFields"></a>
# **operatorServicePrivateAddSupportedFields**
> TitaniumMessageResponse operatorServicePrivateAddSupportedFields(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OperatorServicePrivateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    OperatorServicePrivateApi apiInstance = new OperatorServicePrivateApi(defaultClient);
    TitaniumSupportedFieldsValues body = new TitaniumSupportedFieldsValues(); // TitaniumSupportedFieldsValues | 
    try {
      TitaniumMessageResponse result = apiInstance.operatorServicePrivateAddSupportedFields(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OperatorServicePrivateApi#operatorServicePrivateAddSupportedFields");
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
| **body** | [**TitaniumSupportedFieldsValues**](TitaniumSupportedFieldsValues.md)|  | |

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

<a name="operatorServicePrivateAssets"></a>
# **operatorServicePrivateAssets**
> TitaniumAssetsResponse operatorServicePrivateAssets(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OperatorServicePrivateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    OperatorServicePrivateApi apiInstance = new OperatorServicePrivateApi(defaultClient);
    TitaniumAssetsRequest body = new TitaniumAssetsRequest(); // TitaniumAssetsRequest | 
    try {
      TitaniumAssetsResponse result = apiInstance.operatorServicePrivateAssets(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OperatorServicePrivateApi#operatorServicePrivateAssets");
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
| **body** | [**TitaniumAssetsRequest**](TitaniumAssetsRequest.md)|  | |

### Return type

[**TitaniumAssetsResponse**](TitaniumAssetsResponse.md)

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

<a name="operatorServicePrivateCreateSupportedFields"></a>
# **operatorServicePrivateCreateSupportedFields**
> TitaniumMessageResponse operatorServicePrivateCreateSupportedFields(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OperatorServicePrivateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    OperatorServicePrivateApi apiInstance = new OperatorServicePrivateApi(defaultClient);
    TitaniumSupportedFieldsValues body = new TitaniumSupportedFieldsValues(); // TitaniumSupportedFieldsValues | 
    try {
      TitaniumMessageResponse result = apiInstance.operatorServicePrivateCreateSupportedFields(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OperatorServicePrivateApi#operatorServicePrivateCreateSupportedFields");
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
| **body** | [**TitaniumSupportedFieldsValues**](TitaniumSupportedFieldsValues.md)|  | |

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

<a name="operatorServicePrivateDeleteSupportedFields"></a>
# **operatorServicePrivateDeleteSupportedFields**
> TitaniumMessageResponse operatorServicePrivateDeleteSupportedFields(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OperatorServicePrivateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    OperatorServicePrivateApi apiInstance = new OperatorServicePrivateApi(defaultClient);
    TitaniumSupportedFieldsValues body = new TitaniumSupportedFieldsValues(); // TitaniumSupportedFieldsValues | 
    try {
      TitaniumMessageResponse result = apiInstance.operatorServicePrivateDeleteSupportedFields(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OperatorServicePrivateApi#operatorServicePrivateDeleteSupportedFields");
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
| **body** | [**TitaniumSupportedFieldsValues**](TitaniumSupportedFieldsValues.md)|  | |

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

<a name="operatorServicePrivateEvpStatuses"></a>
# **operatorServicePrivateEvpStatuses**
> TitaniumEvpStatusesResponse operatorServicePrivateEvpStatuses(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OperatorServicePrivateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    OperatorServicePrivateApi apiInstance = new OperatorServicePrivateApi(defaultClient);
    TitaniumEvpStatusesRequest body = new TitaniumEvpStatusesRequest(); // TitaniumEvpStatusesRequest | 
    try {
      TitaniumEvpStatusesResponse result = apiInstance.operatorServicePrivateEvpStatuses(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OperatorServicePrivateApi#operatorServicePrivateEvpStatuses");
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
| **body** | [**TitaniumEvpStatusesRequest**](TitaniumEvpStatusesRequest.md)|  | |

### Return type

[**TitaniumEvpStatusesResponse**](TitaniumEvpStatusesResponse.md)

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

<a name="operatorServicePrivateExportReport"></a>
# **operatorServicePrivateExportReport**
> TitaniumExportResponse operatorServicePrivateExportReport(body)

ExportReport returns pre signed s3 urls which can be used for export report(and compression type)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OperatorServicePrivateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    OperatorServicePrivateApi apiInstance = new OperatorServicePrivateApi(defaultClient);
    TitaniumExportReportRequest body = new TitaniumExportReportRequest(); // TitaniumExportReportRequest | 
    try {
      TitaniumExportResponse result = apiInstance.operatorServicePrivateExportReport(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OperatorServicePrivateApi#operatorServicePrivateExportReport");
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
| **body** | [**TitaniumExportReportRequest**](TitaniumExportReportRequest.md)|  | |

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

<a name="operatorServicePrivateListClients"></a>
# **operatorServicePrivateListClients**
> TitaniumListClientsResponse operatorServicePrivateListClients()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OperatorServicePrivateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    OperatorServicePrivateApi apiInstance = new OperatorServicePrivateApi(defaultClient);
    try {
      TitaniumListClientsResponse result = apiInstance.operatorServicePrivateListClients();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OperatorServicePrivateApi#operatorServicePrivateListClients");
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

[**TitaniumListClientsResponse**](TitaniumListClientsResponse.md)

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

<a name="operatorServicePrivateOperatorOutliers"></a>
# **operatorServicePrivateOperatorOutliers**
> TitaniumOperatorOutliersResponse operatorServicePrivateOperatorOutliers(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OperatorServicePrivateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    OperatorServicePrivateApi apiInstance = new OperatorServicePrivateApi(defaultClient);
    TitaniumOperatorOutliersRequest body = new TitaniumOperatorOutliersRequest(); // TitaniumOperatorOutliersRequest | 
    try {
      TitaniumOperatorOutliersResponse result = apiInstance.operatorServicePrivateOperatorOutliers(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OperatorServicePrivateApi#operatorServicePrivateOperatorOutliers");
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
| **body** | [**TitaniumOperatorOutliersRequest**](TitaniumOperatorOutliersRequest.md)|  | |

### Return type

[**TitaniumOperatorOutliersResponse**](TitaniumOperatorOutliersResponse.md)

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

<a name="operatorServicePrivateOutliers"></a>
# **operatorServicePrivateOutliers**
> TitaniumOutliersResponse operatorServicePrivateOutliers(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OperatorServicePrivateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    OperatorServicePrivateApi apiInstance = new OperatorServicePrivateApi(defaultClient);
    TitaniumOutliersRequest body = new TitaniumOutliersRequest(); // TitaniumOutliersRequest | 
    try {
      TitaniumOutliersResponse result = apiInstance.operatorServicePrivateOutliers(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OperatorServicePrivateApi#operatorServicePrivateOutliers");
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
| **body** | [**TitaniumOutliersRequest**](TitaniumOutliersRequest.md)|  | |

### Return type

[**TitaniumOutliersResponse**](TitaniumOutliersResponse.md)

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

<a name="operatorServicePrivateRecentAssets"></a>
# **operatorServicePrivateRecentAssets**
> TitaniumRecentAssetsResponse operatorServicePrivateRecentAssets(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OperatorServicePrivateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    OperatorServicePrivateApi apiInstance = new OperatorServicePrivateApi(defaultClient);
    TitaniumRecentAssetsRequest body = new TitaniumRecentAssetsRequest(); // TitaniumRecentAssetsRequest | 
    try {
      TitaniumRecentAssetsResponse result = apiInstance.operatorServicePrivateRecentAssets(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OperatorServicePrivateApi#operatorServicePrivateRecentAssets");
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
| **body** | [**TitaniumRecentAssetsRequest**](TitaniumRecentAssetsRequest.md)|  | |

### Return type

[**TitaniumRecentAssetsResponse**](TitaniumRecentAssetsResponse.md)

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

<a name="operatorServicePrivateUploadDTCC"></a>
# **operatorServicePrivateUploadDTCC**
> TitaniumUploadURLResponse operatorServicePrivateUploadDTCC(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OperatorServicePrivateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    OperatorServicePrivateApi apiInstance = new OperatorServicePrivateApi(defaultClient);
    TitaniumUploadDTCCRequest body = new TitaniumUploadDTCCRequest(); // TitaniumUploadDTCCRequest | 
    try {
      TitaniumUploadURLResponse result = apiInstance.operatorServicePrivateUploadDTCC(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OperatorServicePrivateApi#operatorServicePrivateUploadDTCC");
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
| **body** | [**TitaniumUploadDTCCRequest**](TitaniumUploadDTCCRequest.md)|  | |

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

<a name="operatorServicePrivateUploadEVP"></a>
# **operatorServicePrivateUploadEVP**
> TitaniumUploadURLResponse operatorServicePrivateUploadEVP(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OperatorServicePrivateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    OperatorServicePrivateApi apiInstance = new OperatorServicePrivateApi(defaultClient);
    TitaniumUploadEVPRequest body = new TitaniumUploadEVPRequest(); // TitaniumUploadEVPRequest | 
    try {
      TitaniumUploadURLResponse result = apiInstance.operatorServicePrivateUploadEVP(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OperatorServicePrivateApi#operatorServicePrivateUploadEVP");
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
| **body** | [**TitaniumUploadEVPRequest**](TitaniumUploadEVPRequest.md)|  | |

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

