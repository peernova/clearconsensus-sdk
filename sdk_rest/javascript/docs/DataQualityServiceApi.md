# ClearconsensusSdk.DataQualityServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dataQualityServiceDQErrors**](DataQualityServiceApi.md#dataQualityServiceDQErrors) | **POST** /api/v1/dqerrors | 
[**dataQualityServiceGetDataQualityErrors**](DataQualityServiceApi.md#dataQualityServiceGetDataQualityErrors) | **POST** /api/v1/data-quality-errors | 



## dataQualityServiceDQErrors

> TitaniumDQErrorsResponse dataQualityServiceDQErrors(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.DataQualityServiceApi();
let body = new ClearconsensusSdk.TitaniumDQErrorsRequest(); // TitaniumDQErrorsRequest | 
apiInstance.dataQualityServiceDQErrors(body, (error, data, response) => {
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
 **body** | [**TitaniumDQErrorsRequest**](TitaniumDQErrorsRequest.md)|  | 

### Return type

[**TitaniumDQErrorsResponse**](TitaniumDQErrorsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## dataQualityServiceGetDataQualityErrors

> TitaniumGetDataQualityErrorsResponse dataQualityServiceGetDataQualityErrors(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.DataQualityServiceApi();
let body = new ClearconsensusSdk.TitaniumGetDataQualityErrorsRequest(); // TitaniumGetDataQualityErrorsRequest | 
apiInstance.dataQualityServiceGetDataQualityErrors(body, (error, data, response) => {
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
 **body** | [**TitaniumGetDataQualityErrorsRequest**](TitaniumGetDataQualityErrorsRequest.md)|  | 

### Return type

[**TitaniumGetDataQualityErrorsResponse**](TitaniumGetDataQualityErrorsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

