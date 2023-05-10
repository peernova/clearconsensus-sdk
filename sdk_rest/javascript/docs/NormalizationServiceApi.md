# ClearconsensusSdk.NormalizationServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**normalizationServiceAddNormalizationRule**](NormalizationServiceApi.md#normalizationServiceAddNormalizationRule) | **POST** /api/v1/normalization/rule/add | 
[**normalizationServiceDisableNormalizationRule**](NormalizationServiceApi.md#normalizationServiceDisableNormalizationRule) | **POST** /api/v1/normalization/rule/disable | 
[**normalizationServiceEnableNormalizationRule**](NormalizationServiceApi.md#normalizationServiceEnableNormalizationRule) | **POST** /api/v1/normalization/rule/enable | 
[**normalizationServiceGetNormalizationRule**](NormalizationServiceApi.md#normalizationServiceGetNormalizationRule) | **POST** /api/v1/normalization/rule/get | 
[**normalizationServiceGetNormalizationRuleVersion**](NormalizationServiceApi.md#normalizationServiceGetNormalizationRuleVersion) | **GET** /api/v1/normalization/rule/version/{descriptorName}/{versionId} | 
[**normalizationServiceListNormalizationRuleVersions**](NormalizationServiceApi.md#normalizationServiceListNormalizationRuleVersions) | **POST** /api/v1/normalization/rule/versions | 
[**normalizationServiceListNormalizationRules**](NormalizationServiceApi.md#normalizationServiceListNormalizationRules) | **POST** /api/v1/normalization/rule/list | 



## normalizationServiceAddNormalizationRule

> TitaniumAcknowledgeResponse normalizationServiceAddNormalizationRule(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.NormalizationServiceApi();
let body = new ClearconsensusSdk.TitaniumNormalizationRuleDefinition(); // TitaniumNormalizationRuleDefinition | 
apiInstance.normalizationServiceAddNormalizationRule(body, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumNormalizationRuleDefinition**](TitaniumNormalizationRuleDefinition.md)|  | 

### Return type

[**TitaniumAcknowledgeResponse**](TitaniumAcknowledgeResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## normalizationServiceDisableNormalizationRule

> TitaniumAcknowledgeResponse normalizationServiceDisableNormalizationRule(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.NormalizationServiceApi();
let body = new ClearconsensusSdk.TitaniumGetDefinition(); // TitaniumGetDefinition | 
apiInstance.normalizationServiceDisableNormalizationRule(body, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumGetDefinition**](TitaniumGetDefinition.md)|  | 

### Return type

[**TitaniumAcknowledgeResponse**](TitaniumAcknowledgeResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## normalizationServiceEnableNormalizationRule

> TitaniumAcknowledgeResponse normalizationServiceEnableNormalizationRule(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.NormalizationServiceApi();
let body = new ClearconsensusSdk.TitaniumGetDefinition(); // TitaniumGetDefinition | 
apiInstance.normalizationServiceEnableNormalizationRule(body, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumGetDefinition**](TitaniumGetDefinition.md)|  | 

### Return type

[**TitaniumAcknowledgeResponse**](TitaniumAcknowledgeResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## normalizationServiceGetNormalizationRule

> TitaniumNormalizationRuleResponse normalizationServiceGetNormalizationRule(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.NormalizationServiceApi();
let body = new ClearconsensusSdk.TitaniumGetDefinition(); // TitaniumGetDefinition | 
apiInstance.normalizationServiceGetNormalizationRule(body, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumGetDefinition**](TitaniumGetDefinition.md)|  | 

### Return type

[**TitaniumNormalizationRuleResponse**](TitaniumNormalizationRuleResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## normalizationServiceGetNormalizationRuleVersion

> TitaniumNormalizationRuleResponse normalizationServiceGetNormalizationRuleVersion(descriptorName, versionId, opts)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.NormalizationServiceApi();
let descriptorName = "descriptorName_example"; // String | 
let versionId = "versionId_example"; // String | 
let opts = {
  'name': "name_example", // String | 
  'scope': "scope_example" // String | 
};
apiInstance.normalizationServiceGetNormalizationRuleVersion(descriptorName, versionId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **descriptorName** | **String**|  | 
 **versionId** | **String**|  | 
 **name** | **String**|  | [optional] 
 **scope** | **String**|  | [optional] 

### Return type

[**TitaniumNormalizationRuleResponse**](TitaniumNormalizationRuleResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## normalizationServiceListNormalizationRuleVersions

> TitaniumListVersionResponse normalizationServiceListNormalizationRuleVersions(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.NormalizationServiceApi();
let body = new ClearconsensusSdk.TitaniumGetDefinition(); // TitaniumGetDefinition | 
apiInstance.normalizationServiceListNormalizationRuleVersions(body, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumGetDefinition**](TitaniumGetDefinition.md)|  | 

### Return type

[**TitaniumListVersionResponse**](TitaniumListVersionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## normalizationServiceListNormalizationRules

> TitaniumListRuleResponse normalizationServiceListNormalizationRules(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.NormalizationServiceApi();
let body = new ClearconsensusSdk.TitaniumListRequest(); // TitaniumListRequest | 
apiInstance.normalizationServiceListNormalizationRules(body, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumListRequest**](TitaniumListRequest.md)|  | 

### Return type

[**TitaniumListRuleResponse**](TitaniumListRuleResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

