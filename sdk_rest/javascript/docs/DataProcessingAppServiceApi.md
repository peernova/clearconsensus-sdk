# ClearconsensusSdk.DataProcessingAppServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dataProcessingAppServiceRunDataProcessingApp**](DataProcessingAppServiceApi.md#dataProcessingAppServiceRunDataProcessingApp) | **POST** /api/v1/dataprocessingapp/run | RunDataProcessingApp triggers jobs that are responsible to processing of received data.



## dataProcessingAppServiceRunDataProcessingApp

> TitaniumRunDataProcessingAppResponse dataProcessingAppServiceRunDataProcessingApp(body)

RunDataProcessingApp triggers jobs that are responsible to processing of received data.

### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.DataProcessingAppServiceApi();
let body = new ClearconsensusSdk.TitaniumRunDataProcessingAppRequest(); // TitaniumRunDataProcessingAppRequest | 
apiInstance.dataProcessingAppServiceRunDataProcessingApp(body, (error, data, response) => {
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
 **body** | [**TitaniumRunDataProcessingAppRequest**](TitaniumRunDataProcessingAppRequest.md)|  | 

### Return type

[**TitaniumRunDataProcessingAppResponse**](TitaniumRunDataProcessingAppResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

