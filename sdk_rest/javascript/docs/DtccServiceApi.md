# ClearconsensusSdk.DtccServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dtccServiceGetDtccTable**](DtccServiceApi.md#dtccServiceGetDtccTable) | **POST** /api/v1/dtcc/tab | 



## dtccServiceGetDtccTable

> TitaniumDtccTabResponse dtccServiceGetDtccTable(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.DtccServiceApi();
let body = new ClearconsensusSdk.TitaniumDtccTabRequest(); // TitaniumDtccTabRequest | 
apiInstance.dtccServiceGetDtccTable(body, (error, data, response) => {
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
 **body** | [**TitaniumDtccTabRequest**](TitaniumDtccTabRequest.md)|  | 

### Return type

[**TitaniumDtccTabResponse**](TitaniumDtccTabResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

