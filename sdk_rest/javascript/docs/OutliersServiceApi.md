# ClearconsensusSdk.OutliersServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**outliersServiceOutliers**](OutliersServiceApi.md#outliersServiceOutliers) | **POST** /api/v1/outliers | Outliers returns outliers according to request.



## outliersServiceOutliers

> TitaniumOutliersResponse outliersServiceOutliers(body)

Outliers returns outliers according to request.

### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.OutliersServiceApi();
let body = new ClearconsensusSdk.TitaniumOutliersRequest(); // TitaniumOutliersRequest | 
apiInstance.outliersServiceOutliers(body, (error, data, response) => {
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
 **body** | [**TitaniumOutliersRequest**](TitaniumOutliersRequest.md)|  | 

### Return type

[**TitaniumOutliersResponse**](TitaniumOutliersResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

