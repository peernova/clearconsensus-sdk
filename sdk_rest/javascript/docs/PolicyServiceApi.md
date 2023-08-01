# ClearconsensusSdk.PolicyServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**policyServiceCheckPolicy**](PolicyServiceApi.md#policyServiceCheckPolicy) | **POST** /api/v1/user-management/policies/checkPolicy | 
[**policyServiceCreate**](PolicyServiceApi.md#policyServiceCreate) | **POST** /api/v1/user-management/policies/create | 
[**policyServiceGetAddons**](PolicyServiceApi.md#policyServiceGetAddons) | **POST** /api/v1/user-management/policies/getAddons | 
[**policyServiceGetApis**](PolicyServiceApi.md#policyServiceGetApis) | **POST** /api/v1/user-management/policies/getApis | 
[**policyServiceGetAssets**](PolicyServiceApi.md#policyServiceGetAssets) | **POST** /api/v1/user-management/policies/getAssets | 
[**policyServiceGetPolicies**](PolicyServiceApi.md#policyServiceGetPolicies) | **POST** /api/v1/user-management/policies/getPolicies | 
[**policyServiceRemovePolicy**](PolicyServiceApi.md#policyServiceRemovePolicy) | **POST** /api/v1/user-management/policies/removePolicy | 



## policyServiceCheckPolicy

> ProtoOperationSuccess policyServiceCheckPolicy(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.PolicyServiceApi();
let body = new ClearconsensusSdk.ProtoPolicyDto(); // ProtoPolicyDto | 
apiInstance.policyServiceCheckPolicy(body, (error, data, response) => {
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
 **body** | [**ProtoPolicyDto**](ProtoPolicyDto.md)|  | 

### Return type

[**ProtoOperationSuccess**](ProtoOperationSuccess.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## policyServiceCreate

> ProtoOperationSuccess policyServiceCreate(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.PolicyServiceApi();
let body = new ClearconsensusSdk.ProtoPolicies(); // ProtoPolicies | 
apiInstance.policyServiceCreate(body, (error, data, response) => {
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
 **body** | [**ProtoPolicies**](ProtoPolicies.md)|  | 

### Return type

[**ProtoOperationSuccess**](ProtoOperationSuccess.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## policyServiceGetAddons

> ProtoPoliciesListResponse policyServiceGetAddons(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.PolicyServiceApi();
let body = new ClearconsensusSdk.ProtoUsernamePermissionRequest(); // ProtoUsernamePermissionRequest | 
apiInstance.policyServiceGetAddons(body, (error, data, response) => {
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
 **body** | [**ProtoUsernamePermissionRequest**](ProtoUsernamePermissionRequest.md)|  | 

### Return type

[**ProtoPoliciesListResponse**](ProtoPoliciesListResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## policyServiceGetApis

> ProtoPoliciesListResponse policyServiceGetApis(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.PolicyServiceApi();
let body = new ClearconsensusSdk.ProtoUsernamePermissionRequest(); // ProtoUsernamePermissionRequest | 
apiInstance.policyServiceGetApis(body, (error, data, response) => {
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
 **body** | [**ProtoUsernamePermissionRequest**](ProtoUsernamePermissionRequest.md)|  | 

### Return type

[**ProtoPoliciesListResponse**](ProtoPoliciesListResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## policyServiceGetAssets

> ProtoPoliciesListResponse policyServiceGetAssets(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.PolicyServiceApi();
let body = new ClearconsensusSdk.ProtoUsernamePermissionRequest(); // ProtoUsernamePermissionRequest | 
apiInstance.policyServiceGetAssets(body, (error, data, response) => {
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
 **body** | [**ProtoUsernamePermissionRequest**](ProtoUsernamePermissionRequest.md)|  | 

### Return type

[**ProtoPoliciesListResponse**](ProtoPoliciesListResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## policyServiceGetPolicies

> ProtoPoliciesResponse policyServiceGetPolicies(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.PolicyServiceApi();
let body = new ClearconsensusSdk.ProtoPolicyType(); // ProtoPolicyType | 
apiInstance.policyServiceGetPolicies(body, (error, data, response) => {
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
 **body** | [**ProtoPolicyType**](ProtoPolicyType.md)|  | 

### Return type

[**ProtoPoliciesResponse**](ProtoPoliciesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## policyServiceRemovePolicy

> ProtoOperationSuccess policyServiceRemovePolicy(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.PolicyServiceApi();
let body = new ClearconsensusSdk.ProtoPolicyDto(); // ProtoPolicyDto | 
apiInstance.policyServiceRemovePolicy(body, (error, data, response) => {
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
 **body** | [**ProtoPolicyDto**](ProtoPolicyDto.md)|  | 

### Return type

[**ProtoOperationSuccess**](ProtoOperationSuccess.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

