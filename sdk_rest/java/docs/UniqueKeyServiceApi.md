# UniqueKeyServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**uniqueKeyServiceAddUniqueKey**](UniqueKeyServiceApi.md#uniqueKeyServiceAddUniqueKey) | **POST** /api/v1/uniquekey/add | AddUniqueKey is used to add a new unique key definition to the system. |
| [**uniqueKeyServiceGetUniqueKey**](UniqueKeyServiceApi.md#uniqueKeyServiceGetUniqueKey) | **POST** /api/v1/uniquekey/get | GetUniqueKey is used to retrieve a unique key definition by its scope and name. Request: {   \&quot;identifier\&quot;:{      \&quot;name\&quot;:\&quot;foreign_exchange-vanilla-forwards\&quot;   },   \&quot;scope\&quot;:\&quot;global\&quot; } |
| [**uniqueKeyServiceGetUniqueKeyVersion**](UniqueKeyServiceApi.md#uniqueKeyServiceGetUniqueKeyVersion) | **GET** /api/v1/uniquekey/version/{scope}/{name}/{versionId} | GetUniqueKeyVersion is used to retrieve a specific version of a unique key definition by its scope, name, and version ID. Response: {    \&quot;data\&quot;: {        \&quot;name\&quot;: \&quot;foreign_exchange-vanilla-forwards\&quot;,        \&quot;scope\&quot;: \&quot;global\&quot;,        \&quot;uniqueKey\&quot;: [            \&quot;asset\&quot;,            \&quot;service\&quot;,            \&quot;sub-asset\&quot;,            \&quot;instrument_type\&quot;,            \&quot;tenor\&quot;,            \&quot;snap_date\&quot;,            \&quot;snap_time\&quot;,            \&quot;curr_1\&quot;,            \&quot;curr_2\&quot;,            \&quot;onshore_offshore_curr_1\&quot;,            \&quot;onshore_offshore_curr_2\&quot;        ],        \&quot;orderBy\&quot;: [            \&quot;__input_row_num\&quot;        ],        \&quot;order\&quot;: \&quot;ASC\&quot;    } } |
| [**uniqueKeyServiceListUniqueKeyVersions**](UniqueKeyServiceApi.md#uniqueKeyServiceListUniqueKeyVersions) | **POST** /api/v1/uniquekey/versions | ListUniqueKeyVersions is used to retrieve a list of all versions of a specific unique key definition by its scope and name. Request: {   \&quot;scope\&quot;:\&quot;global\&quot;,   \&quot;identifier\&quot;: {        \&quot;name\&quot;: \&quot;foreign_exchange-vanilla-forwards\&quot;    } } |
| [**uniqueKeyServiceListUniqueKeys**](UniqueKeyServiceApi.md#uniqueKeyServiceListUniqueKeys) | **POST** /api/v1/uniquekey/list | ListUniqueKeys is used to retrieve a list of all unique key definitions in the system. Request: {   \&quot;scope\&quot;:\&quot;global\&quot; } |


<a name="uniqueKeyServiceAddUniqueKey"></a>
# **uniqueKeyServiceAddUniqueKey**
> TitaniumAcknowledgeResponse uniqueKeyServiceAddUniqueKey(body)

AddUniqueKey is used to add a new unique key definition to the system.

Example of request : {   \&quot;name\&quot;:\&quot;foreign_exchange-vanilla-forwards\&quot;,   \&quot;scope\&quot;:\&quot;global\&quot;,   \&quot;uniqueKey\&quot;:[      \&quot;snap_date\&quot;,      \&quot;asset\&quot;,      \&quot;service\&quot;,      \&quot;client\&quot;,      \&quot;service\&quot;,      \&quot;tenor\&quot;,      \&quot;snap_time\&quot;,      \&quot;instrument_type\&quot;,      \&quot;spot_reference_price\&quot;,      \&quot;mid_fwrd_outright\&quot;,      \&quot;mid_fwrd_points\&quot;,      \&quot;onshore_offshore_curr_1\&quot;,      \&quot;onshore_offshore_curr_2\&quot;   ] }

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UniqueKeyServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    UniqueKeyServiceApi apiInstance = new UniqueKeyServiceApi(defaultClient);
    TitaniumUniqueKeyDefinition body = new TitaniumUniqueKeyDefinition(); // TitaniumUniqueKeyDefinition | 
    try {
      TitaniumAcknowledgeResponse result = apiInstance.uniqueKeyServiceAddUniqueKey(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UniqueKeyServiceApi#uniqueKeyServiceAddUniqueKey");
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
| **body** | [**TitaniumUniqueKeyDefinition**](TitaniumUniqueKeyDefinition.md)|  | |

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

<a name="uniqueKeyServiceGetUniqueKey"></a>
# **uniqueKeyServiceGetUniqueKey**
> TitaniumUniqueKeyDefinitionResponse uniqueKeyServiceGetUniqueKey(body)

GetUniqueKey is used to retrieve a unique key definition by its scope and name. Request: {   \&quot;identifier\&quot;:{      \&quot;name\&quot;:\&quot;foreign_exchange-vanilla-forwards\&quot;   },   \&quot;scope\&quot;:\&quot;global\&quot; }

Response: {    \&quot;data\&quot;: {        \&quot;name\&quot;: \&quot;foreign_exchange-vanilla-forwards\&quot;,        \&quot;scope\&quot;: \&quot;global\&quot;,        \&quot;uniqueKey\&quot;: [            \&quot;snap_date\&quot;,            \&quot;asset\&quot;,            \&quot;service\&quot;,            \&quot;client\&quot;,            \&quot;service\&quot;,            \&quot;tenor\&quot;,            \&quot;snap_time\&quot;,            \&quot;instrument_type\&quot;,            \&quot;spot_reference_price\&quot;,            \&quot;mid_fwrd_outright\&quot;,            \&quot;mid_fwrd_points\&quot;,            \&quot;onshore_offshore_curr_1\&quot;,            \&quot;onshore_offshore_curr_2\&quot;        ],        \&quot;orderBy\&quot;: [            \&quot;__input_row_num\&quot;        ],        \&quot;order\&quot;: \&quot;ASC\&quot;    } }

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UniqueKeyServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    UniqueKeyServiceApi apiInstance = new UniqueKeyServiceApi(defaultClient);
    TitaniumGetDefinition body = new TitaniumGetDefinition(); // TitaniumGetDefinition | 
    try {
      TitaniumUniqueKeyDefinitionResponse result = apiInstance.uniqueKeyServiceGetUniqueKey(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UniqueKeyServiceApi#uniqueKeyServiceGetUniqueKey");
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

[**TitaniumUniqueKeyDefinitionResponse**](TitaniumUniqueKeyDefinitionResponse.md)

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

<a name="uniqueKeyServiceGetUniqueKeyVersion"></a>
# **uniqueKeyServiceGetUniqueKeyVersion**
> TitaniumUniqueKeyDefinitionResponse uniqueKeyServiceGetUniqueKeyVersion(scope, name, versionId, descriptorName)

GetUniqueKeyVersion is used to retrieve a specific version of a unique key definition by its scope, name, and version ID. Response: {    \&quot;data\&quot;: {        \&quot;name\&quot;: \&quot;foreign_exchange-vanilla-forwards\&quot;,        \&quot;scope\&quot;: \&quot;global\&quot;,        \&quot;uniqueKey\&quot;: [            \&quot;asset\&quot;,            \&quot;service\&quot;,            \&quot;sub-asset\&quot;,            \&quot;instrument_type\&quot;,            \&quot;tenor\&quot;,            \&quot;snap_date\&quot;,            \&quot;snap_time\&quot;,            \&quot;curr_1\&quot;,            \&quot;curr_2\&quot;,            \&quot;onshore_offshore_curr_1\&quot;,            \&quot;onshore_offshore_curr_2\&quot;        ],        \&quot;orderBy\&quot;: [            \&quot;__input_row_num\&quot;        ],        \&quot;order\&quot;: \&quot;ASC\&quot;    } }

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UniqueKeyServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    UniqueKeyServiceApi apiInstance = new UniqueKeyServiceApi(defaultClient);
    String scope = "scope_example"; // String | 
    String name = "name_example"; // String | 
    String versionId = "versionId_example"; // String | 
    String descriptorName = "descriptorName_example"; // String | 
    try {
      TitaniumUniqueKeyDefinitionResponse result = apiInstance.uniqueKeyServiceGetUniqueKeyVersion(scope, name, versionId, descriptorName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UniqueKeyServiceApi#uniqueKeyServiceGetUniqueKeyVersion");
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
| **name** | **String**|  | |
| **versionId** | **String**|  | |
| **descriptorName** | **String**|  | [optional] |

### Return type

[**TitaniumUniqueKeyDefinitionResponse**](TitaniumUniqueKeyDefinitionResponse.md)

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

<a name="uniqueKeyServiceListUniqueKeyVersions"></a>
# **uniqueKeyServiceListUniqueKeyVersions**
> TitaniumListVersionResponse uniqueKeyServiceListUniqueKeyVersions(body)

ListUniqueKeyVersions is used to retrieve a list of all versions of a specific unique key definition by its scope and name. Request: {   \&quot;scope\&quot;:\&quot;global\&quot;,   \&quot;identifier\&quot;: {        \&quot;name\&quot;: \&quot;foreign_exchange-vanilla-forwards\&quot;    } }

Response: {    \&quot;data\&quot;: {        \&quot;versions\&quot;: [            {                \&quot;versionId\&quot;:\&quot;0bmhRR-7hISwkb_H2MvIqafpJCAoy3YgEySZjntZF9o&#x3D;\&quot;,                \&quot;createdAt\&quot;: \&quot;2022-08-22 15:23:44.0\&quot;            }        ]    } }

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UniqueKeyServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    UniqueKeyServiceApi apiInstance = new UniqueKeyServiceApi(defaultClient);
    TitaniumGetDefinition body = new TitaniumGetDefinition(); // TitaniumGetDefinition | 
    try {
      TitaniumListVersionResponse result = apiInstance.uniqueKeyServiceListUniqueKeyVersions(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UniqueKeyServiceApi#uniqueKeyServiceListUniqueKeyVersions");
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

<a name="uniqueKeyServiceListUniqueKeys"></a>
# **uniqueKeyServiceListUniqueKeys**
> TitaniumListUniqueKeysResponse uniqueKeyServiceListUniqueKeys(body)

ListUniqueKeys is used to retrieve a list of all unique key definitions in the system. Request: {   \&quot;scope\&quot;:\&quot;global\&quot; }

Response: {    \&quot;data\&quot;: {        \&quot;results\&quot;: [            {                \&quot;name\&quot;: \&quot;foreign_exchange-vanilla-forwards\&quot;,                \&quot;scope\&quot;: \&quot;global\&quot;,                \&quot;uniqueKey\&quot;: [                    \&quot;asset\&quot;,                    \&quot;service\&quot;,                    \&quot;sub-asset\&quot;,                    \&quot;instrument_type\&quot;,                    \&quot;tenor\&quot;,                    \&quot;snap_date\&quot;,                    \&quot;snap_time\&quot;,                    \&quot;curr_1\&quot;,                    \&quot;curr_2\&quot;,                    \&quot;onshore_offshore_curr_1\&quot;,                    \&quot;onshore_offshore_curr_2\&quot;                ],                \&quot;orderBy\&quot;: [                    \&quot;__input_row_num\&quot;                ],                \&quot;order\&quot;: \&quot;ASC\&quot;            },            {                \&quot;name\&quot;: \&quot;foreign_exchange-vanilla-options\&quot;,                \&quot;scope\&quot;: \&quot;global\&quot;,                \&quot;uniqueKey\&quot;: [                    \&quot;snap_date\&quot;,                    \&quot;asset\&quot;,                    \&quot;service\&quot;,                    \&quot;snap_time\&quot;,                    \&quot;instrument_type\&quot;,                    \&quot;option_instrument_parameter\&quot;,                    \&quot;exercise_style\&quot;,                    \&quot;option_execution_cut_time\&quot;,                    \&quot;curr_1\&quot;,                    \&quot;curr_2\&quot;,                    \&quot;tenor\&quot;,                    \&quot;delta\&quot;,                    \&quot;vol_format\&quot;,                    \&quot;instrument_convention\&quot;,                    \&quot;delta_convention\&quot;,                    \&quot;premium_currency\&quot;,                    \&quot;settlement_convention\&quot;                ],                \&quot;orderBy\&quot;: [                    \&quot;__input_row_num\&quot;                ],                \&quot;order\&quot;: \&quot;ASC\&quot;            }        ]    } }

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UniqueKeyServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    UniqueKeyServiceApi apiInstance = new UniqueKeyServiceApi(defaultClient);
    TitaniumListRequest body = new TitaniumListRequest(); // TitaniumListRequest | 
    try {
      TitaniumListUniqueKeysResponse result = apiInstance.uniqueKeyServiceListUniqueKeys(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UniqueKeyServiceApi#uniqueKeyServiceListUniqueKeys");
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

[**TitaniumListUniqueKeysResponse**](TitaniumListUniqueKeysResponse.md)

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

