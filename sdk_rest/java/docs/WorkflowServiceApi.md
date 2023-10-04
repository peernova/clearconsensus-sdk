# WorkflowServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**workflowServiceAddWorkflow**](WorkflowServiceApi.md#workflowServiceAddWorkflow) | **POST** /api/v1/workflow/add |  |
| [**workflowServiceDisableWorkflow**](WorkflowServiceApi.md#workflowServiceDisableWorkflow) | **POST** /api/v1/workflow/disable |  |
| [**workflowServiceEnableWorkflow**](WorkflowServiceApi.md#workflowServiceEnableWorkflow) | **POST** /api/v1/workflow/enable |  |
| [**workflowServiceGetWorkflow**](WorkflowServiceApi.md#workflowServiceGetWorkflow) | **POST** /api/v1/workflow/get |  |
| [**workflowServiceGetWorkflowAction**](WorkflowServiceApi.md#workflowServiceGetWorkflowAction) | **GET** /api/v1/workflow/action/{name} |  |
| [**workflowServiceListWorkflowActions**](WorkflowServiceApi.md#workflowServiceListWorkflowActions) | **POST** /api/v1/workflow/action/list |  |
| [**workflowServiceListWorkflows**](WorkflowServiceApi.md#workflowServiceListWorkflows) | **POST** /api/v1/workflow/list |  |
| [**workflowServiceReprocessWorkflow**](WorkflowServiceApi.md#workflowServiceReprocessWorkflow) | **POST** /api/v1/workflow/reprocess |  |
| [**workflowServiceRunWorkflow**](WorkflowServiceApi.md#workflowServiceRunWorkflow) | **POST** /api/v1/workflow/run |  |


<a name="workflowServiceAddWorkflow"></a>
# **workflowServiceAddWorkflow**
> TitaniumAcknowledgeResponse workflowServiceAddWorkflow(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkflowServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    WorkflowServiceApi apiInstance = new WorkflowServiceApi(defaultClient);
    TitaniumAddWorkflowDefinitionRequest body = new TitaniumAddWorkflowDefinitionRequest(); // TitaniumAddWorkflowDefinitionRequest | 
    try {
      TitaniumAcknowledgeResponse result = apiInstance.workflowServiceAddWorkflow(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkflowServiceApi#workflowServiceAddWorkflow");
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
| **body** | [**TitaniumAddWorkflowDefinitionRequest**](TitaniumAddWorkflowDefinitionRequest.md)|  | |

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

<a name="workflowServiceDisableWorkflow"></a>
# **workflowServiceDisableWorkflow**
> TitaniumAcknowledgeResponse workflowServiceDisableWorkflow(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkflowServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    WorkflowServiceApi apiInstance = new WorkflowServiceApi(defaultClient);
    TitaniumEnableDisableRequest body = new TitaniumEnableDisableRequest(); // TitaniumEnableDisableRequest | 
    try {
      TitaniumAcknowledgeResponse result = apiInstance.workflowServiceDisableWorkflow(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkflowServiceApi#workflowServiceDisableWorkflow");
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
| **body** | [**TitaniumEnableDisableRequest**](TitaniumEnableDisableRequest.md)|  | |

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

<a name="workflowServiceEnableWorkflow"></a>
# **workflowServiceEnableWorkflow**
> TitaniumAcknowledgeResponse workflowServiceEnableWorkflow(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkflowServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    WorkflowServiceApi apiInstance = new WorkflowServiceApi(defaultClient);
    TitaniumEnableDisableRequest body = new TitaniumEnableDisableRequest(); // TitaniumEnableDisableRequest | 
    try {
      TitaniumAcknowledgeResponse result = apiInstance.workflowServiceEnableWorkflow(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkflowServiceApi#workflowServiceEnableWorkflow");
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
| **body** | [**TitaniumEnableDisableRequest**](TitaniumEnableDisableRequest.md)|  | |

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

<a name="workflowServiceGetWorkflow"></a>
# **workflowServiceGetWorkflow**
> TitaniumWorkflowDefinitionResponse workflowServiceGetWorkflow(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkflowServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    WorkflowServiceApi apiInstance = new WorkflowServiceApi(defaultClient);
    TitaniumGetDefinition body = new TitaniumGetDefinition(); // TitaniumGetDefinition | 
    try {
      TitaniumWorkflowDefinitionResponse result = apiInstance.workflowServiceGetWorkflow(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkflowServiceApi#workflowServiceGetWorkflow");
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

[**TitaniumWorkflowDefinitionResponse**](TitaniumWorkflowDefinitionResponse.md)

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

<a name="workflowServiceGetWorkflowAction"></a>
# **workflowServiceGetWorkflowAction**
> TitaniumGetWorkflowActionResponse workflowServiceGetWorkflowAction(name)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkflowServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    WorkflowServiceApi apiInstance = new WorkflowServiceApi(defaultClient);
    String name = "name_example"; // String | 
    try {
      TitaniumGetWorkflowActionResponse result = apiInstance.workflowServiceGetWorkflowAction(name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkflowServiceApi#workflowServiceGetWorkflowAction");
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
| **name** | **String**|  | |

### Return type

[**TitaniumGetWorkflowActionResponse**](TitaniumGetWorkflowActionResponse.md)

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

<a name="workflowServiceListWorkflowActions"></a>
# **workflowServiceListWorkflowActions**
> TitaniumWorkflowList workflowServiceListWorkflowActions(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkflowServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    WorkflowServiceApi apiInstance = new WorkflowServiceApi(defaultClient);
    TitaniumListRequest body = new TitaniumListRequest(); // TitaniumListRequest | 
    try {
      TitaniumWorkflowList result = apiInstance.workflowServiceListWorkflowActions(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkflowServiceApi#workflowServiceListWorkflowActions");
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

[**TitaniumWorkflowList**](TitaniumWorkflowList.md)

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

<a name="workflowServiceListWorkflows"></a>
# **workflowServiceListWorkflows**
> TitaniumWorkflowList workflowServiceListWorkflows(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkflowServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    WorkflowServiceApi apiInstance = new WorkflowServiceApi(defaultClient);
    TitaniumListRequest body = new TitaniumListRequest(); // TitaniumListRequest | 
    try {
      TitaniumWorkflowList result = apiInstance.workflowServiceListWorkflows(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkflowServiceApi#workflowServiceListWorkflows");
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

[**TitaniumWorkflowList**](TitaniumWorkflowList.md)

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

<a name="workflowServiceReprocessWorkflow"></a>
# **workflowServiceReprocessWorkflow**
> TitaniumRunWorkflowResponse workflowServiceReprocessWorkflow(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkflowServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    WorkflowServiceApi apiInstance = new WorkflowServiceApi(defaultClient);
    TitaniumReprocessWorkflowRequest body = new TitaniumReprocessWorkflowRequest(); // TitaniumReprocessWorkflowRequest | 
    try {
      TitaniumRunWorkflowResponse result = apiInstance.workflowServiceReprocessWorkflow(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkflowServiceApi#workflowServiceReprocessWorkflow");
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
| **body** | [**TitaniumReprocessWorkflowRequest**](TitaniumReprocessWorkflowRequest.md)|  | |

### Return type

[**TitaniumRunWorkflowResponse**](TitaniumRunWorkflowResponse.md)

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

<a name="workflowServiceRunWorkflow"></a>
# **workflowServiceRunWorkflow**
> TitaniumRunWorkflowResponse workflowServiceRunWorkflow(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkflowServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    WorkflowServiceApi apiInstance = new WorkflowServiceApi(defaultClient);
    TitaniumRunWorkflowRequest body = new TitaniumRunWorkflowRequest(); // TitaniumRunWorkflowRequest | 
    try {
      TitaniumRunWorkflowResponse result = apiInstance.workflowServiceRunWorkflow(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkflowServiceApi#workflowServiceRunWorkflow");
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
| **body** | [**TitaniumRunWorkflowRequest**](TitaniumRunWorkflowRequest.md)|  | |

### Return type

[**TitaniumRunWorkflowResponse**](TitaniumRunWorkflowResponse.md)

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

