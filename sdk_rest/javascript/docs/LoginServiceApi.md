# ClearconsensusSdk.LoginServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**loginServiceLogin**](LoginServiceApi.md#loginServiceLogin) | **POST** /api/v1/login | 



## loginServiceLogin

> TitaniumLoginResponse loginServiceLogin(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.LoginServiceApi();
let body = new ClearconsensusSdk.TitaniumLoginRequest(); // TitaniumLoginRequest | 
apiInstance.loginServiceLogin(body, (error, data, response) => {
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
 **body** | [**TitaniumLoginRequest**](TitaniumLoginRequest.md)|  | 

### Return type

[**TitaniumLoginResponse**](TitaniumLoginResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

