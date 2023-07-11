# ClearconsensusSdk.GroupPolicyServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**groupPolicyServiceCreate**](GroupPolicyServiceApi.md#groupPolicyServiceCreate) | **POST** /api/v1/user-management/group-policies/create | 
[**groupPolicyServiceGetPolicies**](GroupPolicyServiceApi.md#groupPolicyServiceGetPolicies) | **POST** /api/v1/user-management/group-policies/getPolicies | 



## groupPolicyServiceCreate

> ProtoServiceResponse groupPolicyServiceCreate(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.GroupPolicyServiceApi();
let body = new ClearconsensusSdk.ProtoGroupPolicies(); // ProtoGroupPolicies | 
apiInstance.groupPolicyServiceCreate(body, (error, data, response) => {
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
 **body** | [**ProtoGroupPolicies**](ProtoGroupPolicies.md)|  | 

### Return type

[**ProtoServiceResponse**](ProtoServiceResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## groupPolicyServiceGetPolicies

> ProtoServiceResponse groupPolicyServiceGetPolicies(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.GroupPolicyServiceApi();
let body = new ClearconsensusSdk.ProtoPolicyType(); // ProtoPolicyType | 
apiInstance.groupPolicyServiceGetPolicies(body, (error, data, response) => {
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

[**ProtoServiceResponse**](ProtoServiceResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

