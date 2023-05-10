# ConsensusServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**consensusServiceConsensus**](ConsensusServiceApi.md#consensusServiceConsensus) | **POST** /api/v1/consensus | Consensus return information about consensus according to request. Need to specify consensus run timestamp, asset ID and etc.(See ConsensusRequest definition) Returns ConsensusResponse that contains information about column and rows related to consensus. |
| [**consensusServiceConsensusExplorerInstrumentDetails**](ConsensusServiceApi.md#consensusServiceConsensusExplorerInstrumentDetails) | **POST** /api/v1/consensus-explorer/details |  |
| [**consensusServiceConsensusExplorerRanges**](ConsensusServiceApi.md#consensusServiceConsensusExplorerRanges) | **POST** /api/v1/consensus-explorer/range |  |
| [**consensusServiceConsensusExplorerTable**](ConsensusServiceApi.md#consensusServiceConsensusExplorerTable) | **POST** /api/v1/consensus-explorer/table |  |
| [**consensusServiceConsensusOutliers**](ConsensusServiceApi.md#consensusServiceConsensusOutliers) | **POST** /api/v1/outliers-list | ConsensusOutliers return list of outliers according to specified consensus. Need to identify consensus tun timestamp and etc.(Described in OutliersListRequest) Return ConsensusActiveResponse that contains active consensuses with specified run timestamp. |
| [**consensusServiceConsensusResultSetValues**](ConsensusServiceApi.md#consensusServiceConsensusResultSetValues) | **POST** /api/v1/consensus-result-set-view |  |
| [**consensusServiceConsensusTimestamps**](ConsensusServiceApi.md#consensusServiceConsensusTimestamps) | **POST** /api/v1/consensus/timestamps | ConsensusTimestamps returns timestamps when it was submitted. Need to specify asset ID and trace name. Returns ConsensusTimestampsResponse that contains all the timestamps related to specified asset ID. |
| [**consensusServiceEvaluatedPrice**](ConsensusServiceApi.md#consensusServiceEvaluatedPrice) | **POST** /api/v1/evaluated-price |  |
| [**consensusServiceGetConsensusRuns**](ConsensusServiceApi.md#consensusServiceGetConsensusRuns) | **POST** /api/v1/consensus-runs-view | Get Consensus Run&#39;s consensus result sets |


<a name="consensusServiceConsensus"></a>
# **consensusServiceConsensus**
> TitaniumConsensusResponse consensusServiceConsensus(body)

Consensus return information about consensus according to request. Need to specify consensus run timestamp, asset ID and etc.(See ConsensusRequest definition) Returns ConsensusResponse that contains information about column and rows related to consensus.

This is a test of a different commenting type: Below we will be shown a placeholder for the Consensus RPC request. *sample input**  &gt;&#x60;{&#x60;&lt;br&gt; &gt;&#x60;   \&quot;asset_id\&quot;: \&quot;238917-2131-341ff\&quot;,&#x60;&lt;br&gt; &gt;&#x60;   \&quot;trace_name\&quot;: \&quot;placeholder value\&quot;,&#x60;&lt;br&gt; &gt;&#x60;   \&quot;submitted_date\&quot;: \&quot;238472301213\&quot;&#x60;&lt;br&gt; &gt;&#x60;}&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConsensusServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    ConsensusServiceApi apiInstance = new ConsensusServiceApi(defaultClient);
    TitaniumConsensusRequest body = new TitaniumConsensusRequest(); // TitaniumConsensusRequest | 
    try {
      TitaniumConsensusResponse result = apiInstance.consensusServiceConsensus(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConsensusServiceApi#consensusServiceConsensus");
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
| **body** | [**TitaniumConsensusRequest**](TitaniumConsensusRequest.md)|  | |

### Return type

[**TitaniumConsensusResponse**](TitaniumConsensusResponse.md)

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

<a name="consensusServiceConsensusExplorerInstrumentDetails"></a>
# **consensusServiceConsensusExplorerInstrumentDetails**
> TitaniumConsensusExplorerInstrumentDetailsResponse consensusServiceConsensusExplorerInstrumentDetails()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConsensusServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    ConsensusServiceApi apiInstance = new ConsensusServiceApi(defaultClient);
    try {
      TitaniumConsensusExplorerInstrumentDetailsResponse result = apiInstance.consensusServiceConsensusExplorerInstrumentDetails();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConsensusServiceApi#consensusServiceConsensusExplorerInstrumentDetails");
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

[**TitaniumConsensusExplorerInstrumentDetailsResponse**](TitaniumConsensusExplorerInstrumentDetailsResponse.md)

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

<a name="consensusServiceConsensusExplorerRanges"></a>
# **consensusServiceConsensusExplorerRanges**
> TitaniumConsensusExplorerRangeResponse consensusServiceConsensusExplorerRanges()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConsensusServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    ConsensusServiceApi apiInstance = new ConsensusServiceApi(defaultClient);
    try {
      TitaniumConsensusExplorerRangeResponse result = apiInstance.consensusServiceConsensusExplorerRanges();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConsensusServiceApi#consensusServiceConsensusExplorerRanges");
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

[**TitaniumConsensusExplorerRangeResponse**](TitaniumConsensusExplorerRangeResponse.md)

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

<a name="consensusServiceConsensusExplorerTable"></a>
# **consensusServiceConsensusExplorerTable**
> TitaniumConsensusExplorerTableResponse consensusServiceConsensusExplorerTable()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConsensusServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    ConsensusServiceApi apiInstance = new ConsensusServiceApi(defaultClient);
    try {
      TitaniumConsensusExplorerTableResponse result = apiInstance.consensusServiceConsensusExplorerTable();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConsensusServiceApi#consensusServiceConsensusExplorerTable");
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

[**TitaniumConsensusExplorerTableResponse**](TitaniumConsensusExplorerTableResponse.md)

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

<a name="consensusServiceConsensusOutliers"></a>
# **consensusServiceConsensusOutliers**
> TitaniumConsensusActiveResponse consensusServiceConsensusOutliers(body)

ConsensusOutliers return list of outliers according to specified consensus. Need to identify consensus tun timestamp and etc.(Described in OutliersListRequest) Return ConsensusActiveResponse that contains active consensuses with specified run timestamp.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConsensusServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    ConsensusServiceApi apiInstance = new ConsensusServiceApi(defaultClient);
    TitaniumOutliersListRequest body = new TitaniumOutliersListRequest(); // TitaniumOutliersListRequest | 
    try {
      TitaniumConsensusActiveResponse result = apiInstance.consensusServiceConsensusOutliers(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConsensusServiceApi#consensusServiceConsensusOutliers");
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
| **body** | [**TitaniumOutliersListRequest**](TitaniumOutliersListRequest.md)|  | |

### Return type

[**TitaniumConsensusActiveResponse**](TitaniumConsensusActiveResponse.md)

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

<a name="consensusServiceConsensusResultSetValues"></a>
# **consensusServiceConsensusResultSetValues**
> TitaniumConsensusResultSetValuesResponse consensusServiceConsensusResultSetValues(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConsensusServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    ConsensusServiceApi apiInstance = new ConsensusServiceApi(defaultClient);
    TitaniumConsensusResultSetValuesRequest body = new TitaniumConsensusResultSetValuesRequest(); // TitaniumConsensusResultSetValuesRequest | 
    try {
      TitaniumConsensusResultSetValuesResponse result = apiInstance.consensusServiceConsensusResultSetValues(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConsensusServiceApi#consensusServiceConsensusResultSetValues");
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
| **body** | [**TitaniumConsensusResultSetValuesRequest**](TitaniumConsensusResultSetValuesRequest.md)|  | |

### Return type

[**TitaniumConsensusResultSetValuesResponse**](TitaniumConsensusResultSetValuesResponse.md)

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

<a name="consensusServiceConsensusTimestamps"></a>
# **consensusServiceConsensusTimestamps**
> TitaniumConsensusTimestampsResponse consensusServiceConsensusTimestamps(body)

ConsensusTimestamps returns timestamps when it was submitted. Need to specify asset ID and trace name. Returns ConsensusTimestampsResponse that contains all the timestamps related to specified asset ID.

This is a test to see how detailed we can make a RPC method&#39;s documentation using this commenting type: Below we will be shown sample input for the ConsensusTimestamps endpoint. **sample input**  &gt;&#x60;{&#x60;&lt;br&gt; &gt;&#x60;   \&quot;asset_id\&quot;: \&quot;238917-2131-341ff\&quot;,&#x60;&lt;br&gt; &gt;&#x60;   \&quot;trace_name\&quot;: \&quot;placeholder value\&quot;&#x60;&lt;br&gt; &gt;&#x60;}&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConsensusServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    ConsensusServiceApi apiInstance = new ConsensusServiceApi(defaultClient);
    TitaniumConsensusTimestampsRequest body = new TitaniumConsensusTimestampsRequest(); // TitaniumConsensusTimestampsRequest | 
    try {
      TitaniumConsensusTimestampsResponse result = apiInstance.consensusServiceConsensusTimestamps(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConsensusServiceApi#consensusServiceConsensusTimestamps");
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
| **body** | [**TitaniumConsensusTimestampsRequest**](TitaniumConsensusTimestampsRequest.md)|  | |

### Return type

[**TitaniumConsensusTimestampsResponse**](TitaniumConsensusTimestampsResponse.md)

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

<a name="consensusServiceEvaluatedPrice"></a>
# **consensusServiceEvaluatedPrice**
> TitaniumEVPResponse consensusServiceEvaluatedPrice(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConsensusServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    ConsensusServiceApi apiInstance = new ConsensusServiceApi(defaultClient);
    TitaniumEVPRequest body = new TitaniumEVPRequest(); // TitaniumEVPRequest | 
    try {
      TitaniumEVPResponse result = apiInstance.consensusServiceEvaluatedPrice(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConsensusServiceApi#consensusServiceEvaluatedPrice");
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
| **body** | [**TitaniumEVPRequest**](TitaniumEVPRequest.md)|  | |

### Return type

[**TitaniumEVPResponse**](TitaniumEVPResponse.md)

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

<a name="consensusServiceGetConsensusRuns"></a>
# **consensusServiceGetConsensusRuns**
> TitaniumGetConsensusRunsResponse consensusServiceGetConsensusRuns(body)

Get Consensus Run&#39;s consensus result sets

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConsensusServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    ConsensusServiceApi apiInstance = new ConsensusServiceApi(defaultClient);
    TitaniumGetConsensusRunsRequest body = new TitaniumGetConsensusRunsRequest(); // TitaniumGetConsensusRunsRequest | 
    try {
      TitaniumGetConsensusRunsResponse result = apiInstance.consensusServiceGetConsensusRuns(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConsensusServiceApi#consensusServiceGetConsensusRuns");
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
| **body** | [**TitaniumGetConsensusRunsRequest**](TitaniumGetConsensusRunsRequest.md)|  | |

### Return type

[**TitaniumGetConsensusRunsResponse**](TitaniumGetConsensusRunsResponse.md)

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

