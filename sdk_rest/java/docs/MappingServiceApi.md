# MappingServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**mappingServiceAddMappingRule**](MappingServiceApi.md#mappingServiceAddMappingRule) | **POST** /api/v1/mapping/rule/add | AddMappingRule AddMappingRule is an API used to add a specific mapping rule to the system. The name provided for the mapping rule must match the asset class and descriptor names. If a mapping rule with the same name already exists, it will be updated. This API accepts a MappingRuleDefinition object as its parameter,which includes information about the mapping rule being added. The response from this API is a DescriptorPairBasedAcknowledgeResponse,which acknowledges the addition of the mapping rule. |
| [**mappingServiceDisableMappingRule**](MappingServiceApi.md#mappingServiceDisableMappingRule) | **POST** /api/v1/mapping/rule/disable | DisableMappingRule is used to disable a mapping rule for a given descriptor pair. It accepts a DescriptorPairBasedGetDefinition object as its parameter, which specifies the source and destination descriptors for the mapping rule. The response from this it is a DescriptorPairBasedAcknowledgeResponse, which acknowledges the disablement of the mapping rule. |
| [**mappingServiceEnableMappingRule**](MappingServiceApi.md#mappingServiceEnableMappingRule) | **POST** /api/v1/mapping/rule/enable | EnableMappingRule is used to enable a mapping rule for a given descriptor pair. It accepts a DescriptorPairBasedGetDefinition object as its parameter, which specifies the source and destination descriptors for the mapping rule. The response from this it is a DescriptorPairBasedAcknowledgeResponse, which acknowledges the enablement of the mapping rule. |
| [**mappingServiceGetMappingRule**](MappingServiceApi.md#mappingServiceGetMappingRule) | **POST** /api/v1/mapping/rule/get | GetMappingRule is used to retrieve a mapping rule for a given descriptor pair. It accepts a DescriptorPairBasedGetDefinition object as its parameter, which specifies the source and destination descriptors for the mapping rule. The response from this it is a MappingRuleResponse, which includes information about the retrieved mapping rule. |
| [**mappingServiceGetMappingRuleVersion**](MappingServiceApi.md#mappingServiceGetMappingRuleVersion) | **GET** /api/v1/mapping/rule/version/{scope}/{srcDescriptor}/{destDescriptor}/{versionId} | GetMappingRuleVersion is used to retrieve a specific version of a mapping rule for a given descriptor pair. It accepts a DescriptorPairBasedVersionRequest object as its parameter, which includes the scope, source descriptor, destination descriptor, and version ID for the mapping rule. The response from it is a MappingRuleResponse, which includes information about the retrieved version of the mapping rule. |
| [**mappingServiceListMappingRuleVersions**](MappingServiceApi.md#mappingServiceListMappingRuleVersions) | **POST** /api/v1/mapping/rule/versions | ListMappingRuleVersions is used to retrieve a list of all versions of a mapping rule for a given descriptor pair. It accepts a DescriptorPairBasedGetDefinition object as its parameter, which specifies the source and destination descriptors for the mapping rule. The response from this it is a ListVersionResponse, which includes information about all versions of the mapping rule. |
| [**mappingServiceListMappingRules**](MappingServiceApi.md#mappingServiceListMappingRules) | **POST** /api/v1/mapping/rule/list | ListMappingRules is used to retrieve a list of all mapping rules in the system. It accepts a ListRequest object as its parameter, which includes optional parameters for filtering the results. The response from this it is a MappingRuleList, which includes information about all mapping rules in the system that match the provided filter parameters. |


<a name="mappingServiceAddMappingRule"></a>
# **mappingServiceAddMappingRule**
> TitaniumDescriptorPairBasedAcknowledgeResponse mappingServiceAddMappingRule(body)

AddMappingRule AddMappingRule is an API used to add a specific mapping rule to the system. The name provided for the mapping rule must match the asset class and descriptor names. If a mapping rule with the same name already exists, it will be updated. This API accepts a MappingRuleDefinition object as its parameter,which includes information about the mapping rule being added. The response from this API is a DescriptorPairBasedAcknowledgeResponse,which acknowledges the addition of the mapping rule.

Example of request for regular user : {   \&quot;src_descriptor\&quot;:\&quot;foreign_exchange-vanilla-forwards\&quot;,   \&quot;dest_descriptor\&quot;:\&quot;foreign_exchange-vanilla-forwards\&quot;,   \&quot;transformations\&quot;:[      {         \&quot;targetColumn\&quot;:\&quot;submission_date\&quot;,         \&quot;sourceColumn\&quot;:\&quot;date\&quot;      },      {         \&quot;targetColumn\&quot;:\&quot;submission_asset\&quot;,         \&quot;rule\&quot;:\&quot;{ \\\&quot;$to_upper\\\&quot;: { \\\&quot;$trim\\\&quot; : \\\&quot;fx_test_for_bank1.submission_asset\\\&quot; }}\&quot;,         \&quot;name\&quot;: \&quot;upper case asset\&quot;,         \&quot;description\&quot;: \&quot;i am optional...\&quot;      }   ] }  Example of request for Back Office : {   \&quot;src_descriptor\&quot;:\&quot;foreign_exchange-vanilla-forwards\&quot;,   \&quot;dest_descriptor\&quot;:\&quot;foreign_exchange-vanilla-forwards\&quot;,   \&quot;scope\&quot;:\&quot;global\&quot;,   \&quot;transformations\&quot;:[      {         \&quot;targetColumn\&quot;:\&quot;submission_date\&quot;,         \&quot;sourceColumn\&quot;:\&quot;another_date\&quot;      },      {         \&quot;targetColumn\&quot;:\&quot;submission_asset\&quot;,         \&quot;rule\&quot;:\&quot;{ \\\&quot;$to_upper\\\&quot;: { \\\&quot;$trim\\\&quot; : \\\&quot;fx_test_for_bank1.submission_asset\\\&quot; }}\&quot;,         \&quot;name\&quot;: \&quot;upper case asset\&quot;,         \&quot;description\&quot;: \&quot;i am optional...\&quot;      }   ] }  Example of response : {   \&quot;data\&quot;:{      \&quot;uid\&quot;:\&quot;fc8b57b7-cc90-11ec-b784-8dfc726b351f\&quot;,      \&quot;src_descriptor\&quot;:\&quot;foreign_exchange-vanilla-forwards\&quot;,      \&quot;dest_descriptor\&quot;:\&quot;foreign_exchange-vanilla-forwards\&quot;   } }  Example of error response : {   \&quot;error\&quot;:{      \&quot;code\&quot;:70,      \&quot;message\&quot;:\&quot;Missing argument: rule name.\&quot;   } }

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MappingServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    MappingServiceApi apiInstance = new MappingServiceApi(defaultClient);
    TitaniumMappingRuleDefinition body = new TitaniumMappingRuleDefinition(); // TitaniumMappingRuleDefinition | 
    try {
      TitaniumDescriptorPairBasedAcknowledgeResponse result = apiInstance.mappingServiceAddMappingRule(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MappingServiceApi#mappingServiceAddMappingRule");
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
| **body** | [**TitaniumMappingRuleDefinition**](TitaniumMappingRuleDefinition.md)|  | |

### Return type

[**TitaniumDescriptorPairBasedAcknowledgeResponse**](TitaniumDescriptorPairBasedAcknowledgeResponse.md)

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

<a name="mappingServiceDisableMappingRule"></a>
# **mappingServiceDisableMappingRule**
> TitaniumDescriptorPairBasedAcknowledgeResponse mappingServiceDisableMappingRule(body)

DisableMappingRule is used to disable a mapping rule for a given descriptor pair. It accepts a DescriptorPairBasedGetDefinition object as its parameter, which specifies the source and destination descriptors for the mapping rule. The response from this it is a DescriptorPairBasedAcknowledgeResponse, which acknowledges the disablement of the mapping rule.

Request: {  \&quot;src_descriptor\&quot;:\&quot;foreign_exchange-vanilla-options\&quot;,  \&quot;dest_descriptor\&quot;:\&quot;foreign_exchange-vanilla-options\&quot;  \&quot;scope\&quot;: \&quot;Zbank1\&quot; }  Response: {    \&quot;data\&quot;: {        \&quot;uid\&quot;: \&quot;\&quot;,        \&quot;src_descriptor\&quot;:\&quot;foreign_exchange-vanilla-options\&quot;,        \&quot;dest_descriptor\&quot;:\&quot;foreign_exchange-vanilla-options\&quot;    } }

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MappingServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    MappingServiceApi apiInstance = new MappingServiceApi(defaultClient);
    TitaniumDescriptorPairBasedGetDefinition body = new TitaniumDescriptorPairBasedGetDefinition(); // TitaniumDescriptorPairBasedGetDefinition | 
    try {
      TitaniumDescriptorPairBasedAcknowledgeResponse result = apiInstance.mappingServiceDisableMappingRule(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MappingServiceApi#mappingServiceDisableMappingRule");
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
| **body** | [**TitaniumDescriptorPairBasedGetDefinition**](TitaniumDescriptorPairBasedGetDefinition.md)|  | |

### Return type

[**TitaniumDescriptorPairBasedAcknowledgeResponse**](TitaniumDescriptorPairBasedAcknowledgeResponse.md)

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

<a name="mappingServiceEnableMappingRule"></a>
# **mappingServiceEnableMappingRule**
> TitaniumDescriptorPairBasedAcknowledgeResponse mappingServiceEnableMappingRule(body)

EnableMappingRule is used to enable a mapping rule for a given descriptor pair. It accepts a DescriptorPairBasedGetDefinition object as its parameter, which specifies the source and destination descriptors for the mapping rule. The response from this it is a DescriptorPairBasedAcknowledgeResponse, which acknowledges the enablement of the mapping rule.

Request: {  \&quot;src_descriptor\&quot;:\&quot;foreign_exchange-vanilla-options\&quot;,  \&quot;dest_descriptor\&quot;:\&quot;foreign_exchange-vanilla-options\&quot;  \&quot;scope\&quot;: \&quot;Zbank1\&quot; }  Response: {    \&quot;data\&quot;: {        \&quot;uid\&quot;: \&quot;\&quot;,        \&quot;src_descriptor\&quot;:\&quot;foreign_exchange-vanilla-options\&quot;,        \&quot;dest_descriptor\&quot;:\&quot;foreign_exchange-vanilla-options\&quot;    } }

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MappingServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    MappingServiceApi apiInstance = new MappingServiceApi(defaultClient);
    TitaniumDescriptorPairBasedGetDefinition body = new TitaniumDescriptorPairBasedGetDefinition(); // TitaniumDescriptorPairBasedGetDefinition | 
    try {
      TitaniumDescriptorPairBasedAcknowledgeResponse result = apiInstance.mappingServiceEnableMappingRule(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MappingServiceApi#mappingServiceEnableMappingRule");
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
| **body** | [**TitaniumDescriptorPairBasedGetDefinition**](TitaniumDescriptorPairBasedGetDefinition.md)|  | |

### Return type

[**TitaniumDescriptorPairBasedAcknowledgeResponse**](TitaniumDescriptorPairBasedAcknowledgeResponse.md)

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

<a name="mappingServiceGetMappingRule"></a>
# **mappingServiceGetMappingRule**
> TitaniumMappingRuleResponse mappingServiceGetMappingRule(body)

GetMappingRule is used to retrieve a mapping rule for a given descriptor pair. It accepts a DescriptorPairBasedGetDefinition object as its parameter, which specifies the source and destination descriptors for the mapping rule. The response from this it is a MappingRuleResponse, which includes information about the retrieved mapping rule.

Example of request for regular user : {   \&quot;identifier\&quot;:{      \&quot;uid\&quot;:\&quot;fc8b57b7-cc90-11ec-b784-8dfc726b351f\&quot;   } } Or : {      \&quot;src_descriptor\&quot;:\&quot;foreign_exchange-vanilla-forwards\&quot;,      \&quot;dest_descriptor\&quot;:\&quot;foreign_exchange-vanilla-forwards\&quot; }  Example of request for Back Office : {   \&quot;identifier\&quot;:{       \&quot;uid\&quot;:\&quot;fc8b57b7-cc90-11ec-b784-8dfc726b351f\&quot;   },   \&quot;scope\&quot;:\&quot;bank1\&quot; } Or : {   \&quot;src_descriptor\&quot;:\&quot;foreign_exchange-vanilla-forwards\&quot;,   \&quot;dest_descriptor\&quot;:\&quot;foreign_exchange-vanilla-forwards\&quot;,   \&quot;scope\&quot;:\&quot;bank1\&quot; }  Example of response : { \&quot;data\&quot;: {  \&quot;uid\&quot;: \&quot;\&quot;,  \&quot;srcDescriptor\&quot;: \&quot;foreign_exchange-vanilla-options\&quot;,  \&quot;destDescriptor\&quot;: \&quot;foreign_exchange-vanilla-options\&quot;,  \&quot;transformations\&quot;: [   {    \&quot;name\&quot;: \&quot;\&quot;,    \&quot;targetColumn\&quot;: \&quot;snap_date\&quot;,    \&quot;sourceColumn\&quot;: \&quot;submission_date\&quot;,    \&quot;rule\&quot;: \&quot;\&quot;,    \&quot;description\&quot;: \&quot;\&quot;   }  ],  \&quot;scope\&quot;: \&quot;\&quot; } }  Example of error response : {   \&quot;error\&quot;:{      \&quot;code\&quot;:70,      \&quot;message\&quot;:\&quot;Can&#39;t get mapping rule: [[empty] of service [MAPPINGRULESET] does not exist in namespace [bank1]].\&quot;   } }

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MappingServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    MappingServiceApi apiInstance = new MappingServiceApi(defaultClient);
    TitaniumDescriptorPairBasedGetDefinition body = new TitaniumDescriptorPairBasedGetDefinition(); // TitaniumDescriptorPairBasedGetDefinition | 
    try {
      TitaniumMappingRuleResponse result = apiInstance.mappingServiceGetMappingRule(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MappingServiceApi#mappingServiceGetMappingRule");
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
| **body** | [**TitaniumDescriptorPairBasedGetDefinition**](TitaniumDescriptorPairBasedGetDefinition.md)|  | |

### Return type

[**TitaniumMappingRuleResponse**](TitaniumMappingRuleResponse.md)

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

<a name="mappingServiceGetMappingRuleVersion"></a>
# **mappingServiceGetMappingRuleVersion**
> TitaniumMappingRuleResponse mappingServiceGetMappingRuleVersion(scope, srcDescriptor, destDescriptor, versionId)

GetMappingRuleVersion is used to retrieve a specific version of a mapping rule for a given descriptor pair. It accepts a DescriptorPairBasedVersionRequest object as its parameter, which includes the scope, source descriptor, destination descriptor, and version ID for the mapping rule. The response from it is a MappingRuleResponse, which includes information about the retrieved version of the mapping rule.

Example of request : GET /api/v1/validation/rule/version/fx_fwd_1/fx_fwd_2/teTYb9Fs_lIOoPQJukM6dY3aJdiMqT-SdBPdvYfJAjk&#x3D;  Example of response : {   \&quot;definition\&quot;:\&quot;{\\\&quot;src_descriptor\\\&quot;:\\\&quot;foreign_exchange-vanilla-forwards\\\&quot;,\\\&quot;dest_descriptor\\\&quot;:\\\&quot;foreign_exchange-vanilla-forwards\\\&quot;,\\\&quot;transformations\\\&quot;:[{\\\&quot;targetColumnName\\\&quot;:\\\&quot;submission_date\\\&quot;,\\\&quot;sourceColumnName\\\&quot;:\\\&quot;another_date\\\&quot;},{\\\&quot;rule\\\&quot;:\\\&quot;{ \\\\\\\&quot;$to_upper\\\\\\\&quot;: { \\\\\\\&quot;$trim\\\\\\\&quot; : \\\\\\\&quot;fx_test_for_bank1.submission_asset\\\\\\\&quot; }}\\\&quot;,\\\&quot;targetColumnName\\\&quot;:\\\&quot;submission_asset\\\&quot;, \\\&quot;name\\\&quot;: \\\&quot;upper case asset\\\&quot;, \\\&quot;description\\\&quot;: \\\&quot;i am optional...\\\&quot;}]}\&quot; }

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MappingServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    MappingServiceApi apiInstance = new MappingServiceApi(defaultClient);
    String scope = "scope_example"; // String | 
    String srcDescriptor = "srcDescriptor_example"; // String | 
    String destDescriptor = "destDescriptor_example"; // String | 
    String versionId = "versionId_example"; // String | 
    try {
      TitaniumMappingRuleResponse result = apiInstance.mappingServiceGetMappingRuleVersion(scope, srcDescriptor, destDescriptor, versionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MappingServiceApi#mappingServiceGetMappingRuleVersion");
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
| **scope** | **String**|  | |
| **srcDescriptor** | **String**|  | |
| **destDescriptor** | **String**|  | |
| **versionId** | **String**|  | |

### Return type

[**TitaniumMappingRuleResponse**](TitaniumMappingRuleResponse.md)

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

<a name="mappingServiceListMappingRuleVersions"></a>
# **mappingServiceListMappingRuleVersions**
> TitaniumListVersionResponse mappingServiceListMappingRuleVersions(body)

ListMappingRuleVersions is used to retrieve a list of all versions of a mapping rule for a given descriptor pair. It accepts a DescriptorPairBasedGetDefinition object as its parameter, which specifies the source and destination descriptors for the mapping rule. The response from this it is a ListVersionResponse, which includes information about all versions of the mapping rule.

Example of request : {  \&quot;scope\&quot;: \&quot;global\&quot;,  \&quot;src_descriptor\&quot;:\&quot;foreign_exchange-vanilla-options\&quot;,  \&quot;dest_descriptor\&quot;:\&quot;foreign_exchange-vanilla-options\&quot; }  Example of response : {   \&quot;data\&quot;:{      \&quot;versions\&quot;:[         {            \&quot;versionId\&quot;:\&quot;EKc9bpBGCbLJmBqOpP0FTqtNusxgZrgCheGXj_MTj7A&#x3D;\&quot;,            \&quot;createdAt\&quot;:\&quot;2022-05-05 11:33:59.0\&quot;         },         {            \&quot;versionId\&quot;:\&quot;JKLFLkhV3SC-fqO0L-WTswr5ttHLfnvF8rMlLnkafAc&#x3D;\&quot;,            \&quot;createdAt\&quot;:\&quot;2022-05-05 11:32:42.0\&quot;         }      ]   } }

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MappingServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    MappingServiceApi apiInstance = new MappingServiceApi(defaultClient);
    TitaniumDescriptorPairBasedGetDefinition body = new TitaniumDescriptorPairBasedGetDefinition(); // TitaniumDescriptorPairBasedGetDefinition | 
    try {
      TitaniumListVersionResponse result = apiInstance.mappingServiceListMappingRuleVersions(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MappingServiceApi#mappingServiceListMappingRuleVersions");
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
| **body** | [**TitaniumDescriptorPairBasedGetDefinition**](TitaniumDescriptorPairBasedGetDefinition.md)|  | |

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

<a name="mappingServiceListMappingRules"></a>
# **mappingServiceListMappingRules**
> TitaniumMappingRuleList mappingServiceListMappingRules(body)

ListMappingRules is used to retrieve a list of all mapping rules in the system. It accepts a ListRequest object as its parameter, which includes optional parameters for filtering the results. The response from this it is a MappingRuleList, which includes information about all mapping rules in the system that match the provided filter parameters.

Example of request : {   \&quot;scope\&quot;:\&quot;global\&quot; } Or optionally use filter: {   \&quot;scope\&quot;:\&quot;global\&quot;,   \&quot;filter\&quot;: \&quot;.*vanilla.*__.*vanilla.*\&quot; // all mapping rules from any vanilla to any vanilla }  Example of response : {    \&quot;data\&quot;: {        \&quot;results\&quot;: [            {                \&quot;uid\&quot;: \&quot;Djqreg7gTs7CV2rSyyucOWCFjK7ldgS9yQX0o0rEiV0&#x3D;\&quot;,                \&quot;src_descriptor\&quot;: \&quot;foreign_exchange-vanilla-forwards\&quot;,                \&quot;dest_descriptor\&quot;: \&quot;foreign_exchange-vanilla-forwards\&quot;             },            {                \&quot;uid\&quot;: \&quot;Djqreg7gTs7CV2rSyyucOWCFjK7ldgS9yQX0o0rEiV0&#x3D;\&quot;,                \&quot;src_descriptor\&quot;: \&quot;foreign_exchange-vanilla-options\&quot;,                \&quot;dest_descriptor\&quot;: \&quot;foreign_exchange-vanilla-options\&quot;            }        ]    } }

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MappingServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    MappingServiceApi apiInstance = new MappingServiceApi(defaultClient);
    TitaniumListRequest body = new TitaniumListRequest(); // TitaniumListRequest | 
    try {
      TitaniumMappingRuleList result = apiInstance.mappingServiceListMappingRules(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MappingServiceApi#mappingServiceListMappingRules");
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

[**TitaniumMappingRuleList**](TitaniumMappingRuleList.md)

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

