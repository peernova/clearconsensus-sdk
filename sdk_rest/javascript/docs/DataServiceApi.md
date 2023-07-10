# ClearconsensusSdk.DataServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dataServiceAuthorizeUpload**](DataServiceApi.md#dataServiceAuthorizeUpload) | **POST** /api/v1/internal/upload/authorize | AuthorizeUpload shows availability of uploading for user.
[**dataServiceExport**](DataServiceApi.md#dataServiceExport) | **POST** /api/v1/export | Export exports data according to the request.
[**dataServiceNotifyUpload**](DataServiceApi.md#dataServiceNotifyUpload) | **POST** /api/v1/internal/upload/notify | NotifyUpload returns message with notify that data was uploaded according to url in request.
[**dataServiceSubmitted**](DataServiceApi.md#dataServiceSubmitted) | **POST** /api/v1/submitted | Submitted returns submitted data based on the request made.
[**dataServiceUploadURL**](DataServiceApi.md#dataServiceUploadURL) | **POST** /api/v1/upload/url | UploadURL returns a pre-signed S3 URL for uploading data.



## dataServiceAuthorizeUpload

> TitaniumUploadAuthorizationResponse dataServiceAuthorizeUpload(body)

AuthorizeUpload shows availability of uploading for user.

### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.DataServiceApi();
let body = new ClearconsensusSdk.TitaniumUploadURLRequest(); // TitaniumUploadURLRequest | 
apiInstance.dataServiceAuthorizeUpload(body, (error, data, response) => {
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
 **body** | [**TitaniumUploadURLRequest**](TitaniumUploadURLRequest.md)|  | 

### Return type

[**TitaniumUploadAuthorizationResponse**](TitaniumUploadAuthorizationResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## dataServiceExport

> TitaniumExportResponse dataServiceExport(body)

Export exports data according to the request.

### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.DataServiceApi();
let body = new ClearconsensusSdk.TitaniumExportRequest(); // TitaniumExportRequest | 
apiInstance.dataServiceExport(body, (error, data, response) => {
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
 **body** | [**TitaniumExportRequest**](TitaniumExportRequest.md)|  | 

### Return type

[**TitaniumExportResponse**](TitaniumExportResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## dataServiceNotifyUpload

> TitaniumMessageResponse dataServiceNotifyUpload(body)

NotifyUpload returns message with notify that data was uploaded according to url in request.

### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.DataServiceApi();
let body = new ClearconsensusSdk.TitaniumUploadNotifyRequest(); // TitaniumUploadNotifyRequest | 
apiInstance.dataServiceNotifyUpload(body, (error, data, response) => {
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
 **body** | [**TitaniumUploadNotifyRequest**](TitaniumUploadNotifyRequest.md)|  | 

### Return type

[**TitaniumMessageResponse**](TitaniumMessageResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## dataServiceSubmitted

> TitaniumSubmittedResponse dataServiceSubmitted(body)

Submitted returns submitted data based on the request made.

### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.DataServiceApi();
let body = new ClearconsensusSdk.TitaniumSubmittedRequest(); // TitaniumSubmittedRequest | 
apiInstance.dataServiceSubmitted(body, (error, data, response) => {
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
 **body** | [**TitaniumSubmittedRequest**](TitaniumSubmittedRequest.md)|  | 

### Return type

[**TitaniumSubmittedResponse**](TitaniumSubmittedResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## dataServiceUploadURL

> TitaniumUploadURLResponse dataServiceUploadURL(body)

UploadURL returns a pre-signed S3 URL for uploading data.

### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.DataServiceApi();
let body = new ClearconsensusSdk.TitaniumUploadURLRequest(); // TitaniumUploadURLRequest | 
apiInstance.dataServiceUploadURL(body, (error, data, response) => {
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
 **body** | [**TitaniumUploadURLRequest**](TitaniumUploadURLRequest.md)|  | 

### Return type

[**TitaniumUploadURLResponse**](TitaniumUploadURLResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

