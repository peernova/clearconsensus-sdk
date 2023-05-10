# ClearconsensusSdk.ScopeServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**scopeServiceAddScope**](ScopeServiceApi.md#scopeServiceAddScope) | **POST** /api/v1/scope/add | AddScope creates scope in the system.
[**scopeServiceExistScope**](ScopeServiceApi.md#scopeServiceExistScope) | **POST** /api/v1/scope/exist | ExistScope return boolean value about existence of scope according to request.
[**scopeServiceListScope**](ScopeServiceApi.md#scopeServiceListScope) | **POST** /api/v1/scope/list | ListScope returns list of all existing scopes.



## scopeServiceAddScope

> TitaniumAcknowledgeResponse scopeServiceAddScope(body)

AddScope creates scope in the system.

### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.ScopeServiceApi();
let body = new ClearconsensusSdk.TitaniumScopeIdentifier(); // TitaniumScopeIdentifier | 
apiInstance.scopeServiceAddScope(body, (error, data, response) => {
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
 **body** | [**TitaniumScopeIdentifier**](TitaniumScopeIdentifier.md)|  | 

### Return type

[**TitaniumAcknowledgeResponse**](TitaniumAcknowledgeResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## scopeServiceExistScope

> TitaniumScopeExistResponse scopeServiceExistScope(body)

ExistScope return boolean value about existence of scope according to request.

### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.ScopeServiceApi();
let body = new ClearconsensusSdk.TitaniumScopeIdentifier(); // TitaniumScopeIdentifier | 
apiInstance.scopeServiceExistScope(body, (error, data, response) => {
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
 **body** | [**TitaniumScopeIdentifier**](TitaniumScopeIdentifier.md)|  | 

### Return type

[**TitaniumScopeExistResponse**](TitaniumScopeExistResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## scopeServiceListScope

> TitaniumScopeListResponse scopeServiceListScope(body)

ListScope returns list of all existing scopes.

### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.ScopeServiceApi();
let body = {key: null}; // Object | 
apiInstance.scopeServiceListScope(body, (error, data, response) => {
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
 **body** | **Object**|  | 

### Return type

[**TitaniumScopeListResponse**](TitaniumScopeListResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

