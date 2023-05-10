# ClearconsensusSdk.SubmissionServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**submissionServiceGetFilesView**](SubmissionServiceApi.md#submissionServiceGetFilesView) | **POST** /api/v1/submission/files-view | GetFilesView returns information about submitted to s3 storage files.



## submissionServiceGetFilesView

> TitaniumGetSubmissionFilesResponse submissionServiceGetFilesView(body)

GetFilesView returns information about submitted to s3 storage files.

### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.SubmissionServiceApi();
let body = new ClearconsensusSdk.TitaniumGetSubmissionFilesRequest(); // TitaniumGetSubmissionFilesRequest | 
apiInstance.submissionServiceGetFilesView(body, (error, data, response) => {
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
 **body** | [**TitaniumGetSubmissionFilesRequest**](TitaniumGetSubmissionFilesRequest.md)|  | 

### Return type

[**TitaniumGetSubmissionFilesResponse**](TitaniumGetSubmissionFilesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

