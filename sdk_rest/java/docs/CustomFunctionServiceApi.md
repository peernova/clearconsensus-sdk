# CustomFunctionServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**customFunctionServiceAddCustomFunction**](CustomFunctionServiceApi.md#customFunctionServiceAddCustomFunction) | **POST** /api/v1/customfunction/add | AddCustomFunction allows the user to create a new custom function by sending a CustomFunction message. It returns an AcknowledgeResponse indicating whether the custom function was successfully added or not. |
| [**customFunctionServiceGetCustomFunction**](CustomFunctionServiceApi.md#customFunctionServiceGetCustomFunction) | **POST** /api/v1/customfunction/get | GetCustomFunction retrieves the definition of a specific custom function. The custom function is specified in the CustomFunctionGetDefinition message, which includes its ID and scope. The method returns a CustomFunctionDefinitionResponse that contains either the custom function definition or an error. |
| [**customFunctionServiceListCustomFunctionVersions**](CustomFunctionServiceApi.md#customFunctionServiceListCustomFunctionVersions) | **POST** /api/v1/customfunction/versions | ListCustomFunctionVersions lists all the versions of a specific custom function. The custom function is specified in the GetDefinition message, which includes its ID and scope. The method returns a ListVersionResponse that contains either a list of versions or an error. |
| [**customFunctionServiceListCustomFunctions**](CustomFunctionServiceApi.md#customFunctionServiceListCustomFunctions) | **POST** /api/v1/customfunction/list | ListCustomFunctions lists all the custom functions that match the specified criteria. The criteria are defined in the ListCustomFunctionRequest message, which includes the descriptor name and the type of the custom function descriptor. The method returns a ListCustomFunctionResponse that contains either a list of custom functions or an error. |


<a name="customFunctionServiceAddCustomFunction"></a>
# **customFunctionServiceAddCustomFunction**
> TitaniumAcknowledgeResponse customFunctionServiceAddCustomFunction(body)

AddCustomFunction allows the user to create a new custom function by sending a CustomFunction message. It returns an AcknowledgeResponse indicating whether the custom function was successfully added or not.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomFunctionServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    CustomFunctionServiceApi apiInstance = new CustomFunctionServiceApi(defaultClient);
    TitaniumCustomFunction body = new TitaniumCustomFunction(); // TitaniumCustomFunction | 
    try {
      TitaniumAcknowledgeResponse result = apiInstance.customFunctionServiceAddCustomFunction(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomFunctionServiceApi#customFunctionServiceAddCustomFunction");
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
| **body** | [**TitaniumCustomFunction**](TitaniumCustomFunction.md)|  | |

### Return type

[**TitaniumAcknowledgeResponse**](TitaniumAcknowledgeResponse.md)

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

<a name="customFunctionServiceGetCustomFunction"></a>
# **customFunctionServiceGetCustomFunction**
> TitaniumCustomFunctionDefinitionResponse customFunctionServiceGetCustomFunction(body)

GetCustomFunction retrieves the definition of a specific custom function. The custom function is specified in the CustomFunctionGetDefinition message, which includes its ID and scope. The method returns a CustomFunctionDefinitionResponse that contains either the custom function definition or an error.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomFunctionServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    CustomFunctionServiceApi apiInstance = new CustomFunctionServiceApi(defaultClient);
    TitaniumCustomFunctionGetDefinition body = new TitaniumCustomFunctionGetDefinition(); // TitaniumCustomFunctionGetDefinition | 
    try {
      TitaniumCustomFunctionDefinitionResponse result = apiInstance.customFunctionServiceGetCustomFunction(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomFunctionServiceApi#customFunctionServiceGetCustomFunction");
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
| **body** | [**TitaniumCustomFunctionGetDefinition**](TitaniumCustomFunctionGetDefinition.md)|  | |

### Return type

[**TitaniumCustomFunctionDefinitionResponse**](TitaniumCustomFunctionDefinitionResponse.md)

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

<a name="customFunctionServiceListCustomFunctionVersions"></a>
# **customFunctionServiceListCustomFunctionVersions**
> TitaniumListVersionResponse customFunctionServiceListCustomFunctionVersions(body)

ListCustomFunctionVersions lists all the versions of a specific custom function. The custom function is specified in the GetDefinition message, which includes its ID and scope. The method returns a ListVersionResponse that contains either a list of versions or an error.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomFunctionServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    CustomFunctionServiceApi apiInstance = new CustomFunctionServiceApi(defaultClient);
    TitaniumGetDefinition body = new TitaniumGetDefinition(); // TitaniumGetDefinition | 
    try {
      TitaniumListVersionResponse result = apiInstance.customFunctionServiceListCustomFunctionVersions(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomFunctionServiceApi#customFunctionServiceListCustomFunctionVersions");
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
| **body** | [**TitaniumGetDefinition**](TitaniumGetDefinition.md)|  | |

### Return type

[**TitaniumListVersionResponse**](TitaniumListVersionResponse.md)

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

<a name="customFunctionServiceListCustomFunctions"></a>
# **customFunctionServiceListCustomFunctions**
> TitaniumListCustomFunctionResponse customFunctionServiceListCustomFunctions(body)

ListCustomFunctions lists all the custom functions that match the specified criteria. The criteria are defined in the ListCustomFunctionRequest message, which includes the descriptor name and the type of the custom function descriptor. The method returns a ListCustomFunctionResponse that contains either a list of custom functions or an error.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomFunctionServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    CustomFunctionServiceApi apiInstance = new CustomFunctionServiceApi(defaultClient);
    TitaniumListCustomFunctionRequest body = new TitaniumListCustomFunctionRequest(); // TitaniumListCustomFunctionRequest | 
    try {
      TitaniumListCustomFunctionResponse result = apiInstance.customFunctionServiceListCustomFunctions(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomFunctionServiceApi#customFunctionServiceListCustomFunctions");
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
| **body** | [**TitaniumListCustomFunctionRequest**](TitaniumListCustomFunctionRequest.md)|  | |

### Return type

[**TitaniumListCustomFunctionResponse**](TitaniumListCustomFunctionResponse.md)

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

