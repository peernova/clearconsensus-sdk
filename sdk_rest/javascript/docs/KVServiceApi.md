# ClearconsensusSdk.KVServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**kVServiceAddKey**](KVServiceApi.md#kVServiceAddKey) | **POST** /api/v1/kv/add | 
[**kVServiceDeleteKey**](KVServiceApi.md#kVServiceDeleteKey) | **POST** /api/v1/kv/delete | 
[**kVServiceGetKey**](KVServiceApi.md#kVServiceGetKey) | **POST** /api/v1/kv/get | 
[**kVServiceListKeys**](KVServiceApi.md#kVServiceListKeys) | **POST** /api/v1/kv/list | 
[**kVServiceUpdateKey**](KVServiceApi.md#kVServiceUpdateKey) | **POST** /api/v1/kv/update | 



## kVServiceAddKey

> TitaniumKVOperationResponse kVServiceAddKey(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.KVServiceApi();
let body = new ClearconsensusSdk.TitaniumKVAsset(); // TitaniumKVAsset | 
apiInstance.kVServiceAddKey(body, (error, data, response) => {
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
 **body** | [**TitaniumKVAsset**](TitaniumKVAsset.md)|  | 

### Return type

[**TitaniumKVOperationResponse**](TitaniumKVOperationResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## kVServiceDeleteKey

> TitaniumKVOperationResponse kVServiceDeleteKey(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.KVServiceApi();
let body = new ClearconsensusSdk.TitaniumKVRequest(); // TitaniumKVRequest | 
apiInstance.kVServiceDeleteKey(body, (error, data, response) => {
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
 **body** | [**TitaniumKVRequest**](TitaniumKVRequest.md)|  | 

### Return type

[**TitaniumKVOperationResponse**](TitaniumKVOperationResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## kVServiceGetKey

> TitaniumGetKVResponse kVServiceGetKey(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.KVServiceApi();
let body = new ClearconsensusSdk.TitaniumKVRequest(); // TitaniumKVRequest | 
apiInstance.kVServiceGetKey(body, (error, data, response) => {
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
 **body** | [**TitaniumKVRequest**](TitaniumKVRequest.md)|  | 

### Return type

[**TitaniumGetKVResponse**](TitaniumGetKVResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## kVServiceListKeys

> TitaniumListKVResponse kVServiceListKeys(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.KVServiceApi();
let body = new ClearconsensusSdk.TitaniumListKVRequest(); // TitaniumListKVRequest | 
apiInstance.kVServiceListKeys(body, (error, data, response) => {
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
 **body** | [**TitaniumListKVRequest**](TitaniumListKVRequest.md)|  | 

### Return type

[**TitaniumListKVResponse**](TitaniumListKVResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## kVServiceUpdateKey

> TitaniumKVOperationResponse kVServiceUpdateKey(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.KVServiceApi();
let body = new ClearconsensusSdk.TitaniumKVAsset(); // TitaniumKVAsset | 
apiInstance.kVServiceUpdateKey(body, (error, data, response) => {
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
 **body** | [**TitaniumKVAsset**](TitaniumKVAsset.md)|  | 

### Return type

[**TitaniumKVOperationResponse**](TitaniumKVOperationResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

