# ClearconsensusSdk.AdminServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adminServiceOnBoard**](AdminServiceApi.md#adminServiceOnBoard) | **POST** /api/v1/onboard | 
[**adminServiceRunCalculator**](AdminServiceApi.md#adminServiceRunCalculator) | **POST** /api/v1/calculator/run | 
[**adminServiceRunConsensus**](AdminServiceApi.md#adminServiceRunConsensus) | **POST** /api/v1/consensus/run | 
[**adminServiceUploadEvaluatedPrice**](AdminServiceApi.md#adminServiceUploadEvaluatedPrice) | **POST** /api/v1/upload/evaluated-price | 



## adminServiceOnBoard

> TitaniumMessageResponse adminServiceOnBoard(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.AdminServiceApi();
let body = new ClearconsensusSdk.TitaniumOnBoardRequest(); // TitaniumOnBoardRequest | 
apiInstance.adminServiceOnBoard(body, (error, data, response) => {
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
 **body** | [**TitaniumOnBoardRequest**](TitaniumOnBoardRequest.md)|  | 

### Return type

[**TitaniumMessageResponse**](TitaniumMessageResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## adminServiceRunCalculator

> TitaniumMessageResponse adminServiceRunCalculator(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.AdminServiceApi();
let body = new ClearconsensusSdk.TitaniumRunCalculatorRequest(); // TitaniumRunCalculatorRequest | 
apiInstance.adminServiceRunCalculator(body, (error, data, response) => {
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
 **body** | [**TitaniumRunCalculatorRequest**](TitaniumRunCalculatorRequest.md)|  | 

### Return type

[**TitaniumMessageResponse**](TitaniumMessageResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## adminServiceRunConsensus

> TitaniumMessageResponse adminServiceRunConsensus(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.AdminServiceApi();
let body = new ClearconsensusSdk.TitaniumRunConsensusRequest(); // TitaniumRunConsensusRequest | 
apiInstance.adminServiceRunConsensus(body, (error, data, response) => {
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
 **body** | [**TitaniumRunConsensusRequest**](TitaniumRunConsensusRequest.md)|  | 

### Return type

[**TitaniumMessageResponse**](TitaniumMessageResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## adminServiceUploadEvaluatedPrice

> TitaniumMessageResponse adminServiceUploadEvaluatedPrice(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.AdminServiceApi();
let body = new ClearconsensusSdk.TitaniumUploadEvaluatedPriceRequest(); // TitaniumUploadEvaluatedPriceRequest | 
apiInstance.adminServiceUploadEvaluatedPrice(body, (error, data, response) => {
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
 **body** | [**TitaniumUploadEvaluatedPriceRequest**](TitaniumUploadEvaluatedPriceRequest.md)|  | 

### Return type

[**TitaniumMessageResponse**](TitaniumMessageResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

