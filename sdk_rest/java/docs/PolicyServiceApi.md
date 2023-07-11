# PolicyServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**policyServiceCheckPolicy**](PolicyServiceApi.md#policyServiceCheckPolicy) | **POST** /api/v1/user-management/policies/checkPolicy |  |
| [**policyServiceCreate**](PolicyServiceApi.md#policyServiceCreate) | **POST** /api/v1/user-management/policies/create |  |
| [**policyServiceGetAddons**](PolicyServiceApi.md#policyServiceGetAddons) | **POST** /api/v1/user-management/policies/getAddons |  |
| [**policyServiceGetApis**](PolicyServiceApi.md#policyServiceGetApis) | **POST** /api/v1/user-management/policies/getApis |  |
| [**policyServiceGetAssets**](PolicyServiceApi.md#policyServiceGetAssets) | **POST** /api/v1/user-management/policies/getAssets |  |
| [**policyServiceGetPolicies**](PolicyServiceApi.md#policyServiceGetPolicies) | **POST** /api/v1/user-management/policies/getPolicies |  |
| [**policyServiceRemovePolicy**](PolicyServiceApi.md#policyServiceRemovePolicy) | **POST** /api/v1/user-management/policies/removePolicy |  |


<a name="policyServiceCheckPolicy"></a>
# **policyServiceCheckPolicy**
> ProtoServiceResponse policyServiceCheckPolicy(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PolicyServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    PolicyServiceApi apiInstance = new PolicyServiceApi(defaultClient);
    ProtoPolicyDto body = new ProtoPolicyDto(); // ProtoPolicyDto | 
    try {
      ProtoServiceResponse result = apiInstance.policyServiceCheckPolicy(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PolicyServiceApi#policyServiceCheckPolicy");
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
| **body** | [**ProtoPolicyDto**](ProtoPolicyDto.md)|  | |

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

<a name="policyServiceCreate"></a>
# **policyServiceCreate**
> ProtoServiceResponse policyServiceCreate(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PolicyServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    PolicyServiceApi apiInstance = new PolicyServiceApi(defaultClient);
    ProtoPolicies body = new ProtoPolicies(); // ProtoPolicies | 
    try {
      ProtoServiceResponse result = apiInstance.policyServiceCreate(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PolicyServiceApi#policyServiceCreate");
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
| **body** | [**ProtoPolicies**](ProtoPolicies.md)|  | |

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

<a name="policyServiceGetAddons"></a>
# **policyServiceGetAddons**
> ProtoServiceResponse policyServiceGetAddons(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PolicyServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    PolicyServiceApi apiInstance = new PolicyServiceApi(defaultClient);
    ProtoUsernamePermissionRequest body = new ProtoUsernamePermissionRequest(); // ProtoUsernamePermissionRequest | 
    try {
      ProtoServiceResponse result = apiInstance.policyServiceGetAddons(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PolicyServiceApi#policyServiceGetAddons");
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
| **body** | [**ProtoUsernamePermissionRequest**](ProtoUsernamePermissionRequest.md)|  | |

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

<a name="policyServiceGetApis"></a>
# **policyServiceGetApis**
> ProtoServiceResponse policyServiceGetApis(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PolicyServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    PolicyServiceApi apiInstance = new PolicyServiceApi(defaultClient);
    ProtoUsernamePermissionRequest body = new ProtoUsernamePermissionRequest(); // ProtoUsernamePermissionRequest | 
    try {
      ProtoServiceResponse result = apiInstance.policyServiceGetApis(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PolicyServiceApi#policyServiceGetApis");
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
| **body** | [**ProtoUsernamePermissionRequest**](ProtoUsernamePermissionRequest.md)|  | |

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

<a name="policyServiceGetAssets"></a>
# **policyServiceGetAssets**
> ProtoServiceResponse policyServiceGetAssets(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PolicyServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    PolicyServiceApi apiInstance = new PolicyServiceApi(defaultClient);
    ProtoUsernamePermissionRequest body = new ProtoUsernamePermissionRequest(); // ProtoUsernamePermissionRequest | 
    try {
      ProtoServiceResponse result = apiInstance.policyServiceGetAssets(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PolicyServiceApi#policyServiceGetAssets");
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
| **body** | [**ProtoUsernamePermissionRequest**](ProtoUsernamePermissionRequest.md)|  | |

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

<a name="policyServiceGetPolicies"></a>
# **policyServiceGetPolicies**
> ProtoServiceResponse policyServiceGetPolicies(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PolicyServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    PolicyServiceApi apiInstance = new PolicyServiceApi(defaultClient);
    ProtoPolicyType body = new ProtoPolicyType(); // ProtoPolicyType | 
    try {
      ProtoServiceResponse result = apiInstance.policyServiceGetPolicies(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PolicyServiceApi#policyServiceGetPolicies");
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
| **body** | [**ProtoPolicyType**](ProtoPolicyType.md)|  | |

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

<a name="policyServiceRemovePolicy"></a>
# **policyServiceRemovePolicy**
> ProtoServiceResponse policyServiceRemovePolicy(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PolicyServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    PolicyServiceApi apiInstance = new PolicyServiceApi(defaultClient);
    ProtoPolicyDto body = new ProtoPolicyDto(); // ProtoPolicyDto | 
    try {
      ProtoServiceResponse result = apiInstance.policyServiceRemovePolicy(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PolicyServiceApi#policyServiceRemovePolicy");
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
| **body** | [**ProtoPolicyDto**](ProtoPolicyDto.md)|  | |

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

