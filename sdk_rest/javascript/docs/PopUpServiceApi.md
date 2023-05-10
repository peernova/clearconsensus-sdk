# ClearconsensusSdk.PopUpServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**popUpServicePopUpView**](PopUpServiceApi.md#popUpServicePopUpView) | **POST** /api/v1/popup-view | PopUpView returns information according to request for the popup view.



## popUpServicePopUpView

> TitaniumPopUpViewResponse popUpServicePopUpView(body)

PopUpView returns information according to request for the popup view.

### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.PopUpServiceApi();
let body = new ClearconsensusSdk.TitaniumPopUpViewRequest(); // TitaniumPopUpViewRequest | 
apiInstance.popUpServicePopUpView(body, (error, data, response) => {
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
 **body** | [**TitaniumPopUpViewRequest**](TitaniumPopUpViewRequest.md)|  | 

### Return type

[**TitaniumPopUpViewResponse**](TitaniumPopUpViewResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

