# ClearconsensusSdk.UdfServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**udfServiceDisableUdf**](UdfServiceApi.md#udfServiceDisableUdf) | **POST** /api/v1/udf/disable | 
[**udfServiceGetUdfDefinition**](UdfServiceApi.md#udfServiceGetUdfDefinition) | **GET** /api/v1/udf/{name} | 
[**udfServiceListUdfs**](UdfServiceApi.md#udfServiceListUdfs) | **POST** /api/v1/udf/list | 



## udfServiceDisableUdf

> TitaniumMessageResponse udfServiceDisableUdf(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.UdfServiceApi();
let body = new ClearconsensusSdk.TitaniumUdfNameRequest(); // TitaniumUdfNameRequest | 
apiInstance.udfServiceDisableUdf(body, (error, data, response) => {
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
 **body** | [**TitaniumUdfNameRequest**](TitaniumUdfNameRequest.md)|  | 

### Return type

[**TitaniumMessageResponse**](TitaniumMessageResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## udfServiceGetUdfDefinition

> TitaniumGetUdfResponse udfServiceGetUdfDefinition(name, opts)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.UdfServiceApi();
let name = "name_example"; // String | 
let opts = {
  'scope': "scope_example" // String | 
};
apiInstance.udfServiceGetUdfDefinition(name, opts, (error, data, response) => {
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
 **name** | **String**|  | 
 **scope** | **String**|  | [optional] 

### Return type

[**TitaniumGetUdfResponse**](TitaniumGetUdfResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## udfServiceListUdfs

> TitaniumListUdfResponse udfServiceListUdfs(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.UdfServiceApi();
let body = new ClearconsensusSdk.TitaniumListRequest(); // TitaniumListRequest | 
apiInstance.udfServiceListUdfs(body, (error, data, response) => {
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

[**TitaniumListUdfResponse**](TitaniumListUdfResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

