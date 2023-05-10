# ClearconsensusSdk.FileServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fileServiceFileHistory**](FileServiceApi.md#fileServiceFileHistory) | **POST** /api/v1/file-history | FileHistory retrieves the history for a specified file.
[**fileServiceFileSubmission**](FileServiceApi.md#fileServiceFileSubmission) | **POST** /api/v1/file-submission | FileSubmission submits a file for processing.
[**fileServiceGetFileDelimiter**](FileServiceApi.md#fileServiceGetFileDelimiter) | **POST** /api/v1/import/{filename}/delimiter | GetFileDelimiter retrieves the delimiter for a specified file.
[**fileServiceGetFileDescriptor**](FileServiceApi.md#fileServiceGetFileDescriptor) | **POST** /api/v1/import/{filename}/descriptor | GetFileDescriptor retrieves the descriptor for a specified file.
[**fileServiceGetFileExportUrl**](FileServiceApi.md#fileServiceGetFileExportUrl) | **POST** /api/v1/raw-file | GetFileExportUrl retrieves the export URL for a specified file.
[**fileServiceGetFilePreview**](FileServiceApi.md#fileServiceGetFilePreview) | **POST** /api/v1/import/{filename} | GetFilePreview retrieves a preview of a specified file.
[**fileServiceListFiles**](FileServiceApi.md#fileServiceListFiles) | **POST** /api/v1/import/list | ListFiles retrieves a list of files.
[**fileServiceSetFileDelimiter**](FileServiceApi.md#fileServiceSetFileDelimiter) | **POST** /api/v1/import/{fileIdentifier.filename}/delimiter | SetFileDelimiter sets the delimiter for a specified file.
[**fileServiceSetFileDescriptor**](FileServiceApi.md#fileServiceSetFileDescriptor) | **POST** /api/v1/import/{fileIdentifier.filename}/descriptor | SetFileDescriptor sets the descriptor for a specified file.



## fileServiceFileHistory

> TitaniumFileHistoryResponse fileServiceFileHistory(body)

FileHistory retrieves the history for a specified file.

### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.FileServiceApi();
let body = new ClearconsensusSdk.TitaniumFileHistoryRequest(); // TitaniumFileHistoryRequest | 
apiInstance.fileServiceFileHistory(body, (error, data, response) => {
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
 **body** | [**TitaniumFileHistoryRequest**](TitaniumFileHistoryRequest.md)|  | 

### Return type

[**TitaniumFileHistoryResponse**](TitaniumFileHistoryResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## fileServiceFileSubmission

> TitaniumMessageResponse fileServiceFileSubmission(body)

FileSubmission submits a file for processing.

### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.FileServiceApi();
let body = new ClearconsensusSdk.TitaniumFileSubmissionRequest(); // TitaniumFileSubmissionRequest | 
apiInstance.fileServiceFileSubmission(body, (error, data, response) => {
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
 **body** | [**TitaniumFileSubmissionRequest**](TitaniumFileSubmissionRequest.md)|  | 

### Return type

[**TitaniumMessageResponse**](TitaniumMessageResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## fileServiceGetFileDelimiter

> TitaniumFileDelimiterSetting fileServiceGetFileDelimiter(filename, body)

GetFileDelimiter retrieves the delimiter for a specified file.

### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.FileServiceApi();
let filename = "filename_example"; // String | 
let body = new ClearconsensusSdk.FileServiceGetFilePreviewRequest(); // FileServiceGetFilePreviewRequest | 
apiInstance.fileServiceGetFileDelimiter(filename, body, (error, data, response) => {
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
 **filename** | **String**|  | 
 **body** | [**FileServiceGetFilePreviewRequest**](FileServiceGetFilePreviewRequest.md)|  | 

### Return type

[**TitaniumFileDelimiterSetting**](TitaniumFileDelimiterSetting.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## fileServiceGetFileDescriptor

> TitaniumFileDescriptorSetting fileServiceGetFileDescriptor(filename, body)

GetFileDescriptor retrieves the descriptor for a specified file.

### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.FileServiceApi();
let filename = "filename_example"; // String | 
let body = new ClearconsensusSdk.FileServiceGetFilePreviewRequest(); // FileServiceGetFilePreviewRequest | 
apiInstance.fileServiceGetFileDescriptor(filename, body, (error, data, response) => {
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
 **filename** | **String**|  | 
 **body** | [**FileServiceGetFilePreviewRequest**](FileServiceGetFilePreviewRequest.md)|  | 

### Return type

[**TitaniumFileDescriptorSetting**](TitaniumFileDescriptorSetting.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## fileServiceGetFileExportUrl

> TitaniumGetFileExportUrlResponse fileServiceGetFileExportUrl(body)

GetFileExportUrl retrieves the export URL for a specified file.

### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.FileServiceApi();
let body = new ClearconsensusSdk.TitaniumGetFileExportUrlRequest(); // TitaniumGetFileExportUrlRequest | 
apiInstance.fileServiceGetFileExportUrl(body, (error, data, response) => {
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
 **body** | [**TitaniumGetFileExportUrlRequest**](TitaniumGetFileExportUrlRequest.md)|  | 

### Return type

[**TitaniumGetFileExportUrlResponse**](TitaniumGetFileExportUrlResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## fileServiceGetFilePreview

> TitaniumFilePreview fileServiceGetFilePreview(filename, body)

GetFilePreview retrieves a preview of a specified file.

### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.FileServiceApi();
let filename = "filename_example"; // String | 
let body = new ClearconsensusSdk.FileServiceGetFilePreviewRequest(); // FileServiceGetFilePreviewRequest | 
apiInstance.fileServiceGetFilePreview(filename, body, (error, data, response) => {
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
 **filename** | **String**|  | 
 **body** | [**FileServiceGetFilePreviewRequest**](FileServiceGetFilePreviewRequest.md)|  | 

### Return type

[**TitaniumFilePreview**](TitaniumFilePreview.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## fileServiceListFiles

> TitaniumFileList fileServiceListFiles(body)

ListFiles retrieves a list of files.

### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.FileServiceApi();
let body = new ClearconsensusSdk.TitaniumListRequest(); // TitaniumListRequest | 
apiInstance.fileServiceListFiles(body, (error, data, response) => {
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

[**TitaniumFileList**](TitaniumFileList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## fileServiceSetFileDelimiter

> Object fileServiceSetFileDelimiter(fileIdentifierFilename, body)

SetFileDelimiter sets the delimiter for a specified file.

### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.FileServiceApi();
let fileIdentifierFilename = "fileIdentifierFilename_example"; // String | 
let body = new ClearconsensusSdk.TitaniumSetFileDelimiterRequest(); // TitaniumSetFileDelimiterRequest | 
apiInstance.fileServiceSetFileDelimiter(fileIdentifierFilename, body, (error, data, response) => {
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
 **fileIdentifierFilename** | **String**|  | 
 **body** | [**TitaniumSetFileDelimiterRequest**](TitaniumSetFileDelimiterRequest.md)|  | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## fileServiceSetFileDescriptor

> Object fileServiceSetFileDescriptor(fileIdentifierFilename, body)

SetFileDescriptor sets the descriptor for a specified file.

### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.FileServiceApi();
let fileIdentifierFilename = "fileIdentifierFilename_example"; // String | 
let body = new ClearconsensusSdk.TitaniumSetFileDescriptorRequest(); // TitaniumSetFileDescriptorRequest | 
apiInstance.fileServiceSetFileDescriptor(fileIdentifierFilename, body, (error, data, response) => {
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
 **fileIdentifierFilename** | **String**|  | 
 **body** | [**TitaniumSetFileDescriptorRequest**](TitaniumSetFileDescriptorRequest.md)|  | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

