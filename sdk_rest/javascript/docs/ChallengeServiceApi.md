# ClearconsensusSdk.ChallengeServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**challengeServiceChallengeActive**](ChallengeServiceApi.md#challengeServiceChallengeActive) | **POST** /api/v1/operator/challenge/active | ChallengeActive returns active challenges(according to request) in active status(challenge process is active).
[**challengeServiceChallengeCreate**](ChallengeServiceApi.md#challengeServiceChallengeCreate) | **POST** /api/v1/challenge/create | ChallengeCreate creates challenge in the system.(Initiate process by dealer) To create \&quot;challenger\&quot; needs to be authorised and challenge can be created only if one of their own submitted data points has been declared an outlier in the published Consensus. Need to specify asset and fill out evidence information. Returns response that contains ticket ID of the Challenge or the Error.
[**challengeServiceChallengeDecision**](ChallengeServiceApi.md#challengeServiceChallengeDecision) | **POST** /api/v1/operator/challenge/decision | ChallengeDecision sets decision of the challenge according to request.
[**challengeServiceChallengeFormMeta**](ChallengeServiceApi.md#challengeServiceChallengeFormMeta) | **POST** /api/v1/challenge/form-meta | ChallengeFormMeta is used to request information(template) about the form fields required to submit a challenge for a specific asset and evidence type. Returns response with template with pre-filled data.
[**challengeServiceChallengeFreezeAction**](ChallengeServiceApi.md#challengeServiceChallengeFreezeAction) | **POST** /api/v1/operator/challenge/freeze | ChallengeFreezeAction makes challenge process stopped or not according to request.
[**challengeServiceChallengeFreezeStatus**](ChallengeServiceApi.md#challengeServiceChallengeFreezeStatus) | **POST** /api/v1/challenge/freeze/status | ChallengeFreezeStatus returns StatusResponse that contains string that represents freeze status of challenges if the challenge process is stopped and nothing if the one is not. Challenge can be stopped by operator.Dealer can see the freeze status using this method. Need to specify consensus(where outliers exists) run timestamp.
[**challengeServiceChallengeHistory**](ChallengeServiceApi.md#challengeServiceChallengeHistory) | **POST** /api/v1/operator/challenge/history | ChallengeHistory return already closed challenges according to request.
[**challengeServiceChallengeList**](ChallengeServiceApi.md#challengeServiceChallengeList) | **POST** /api/v1/operator/challenge/list | ChallengeList returns list of challenges according to request.
[**challengeServiceGetChallengeAttachmentUploadUrl**](ChallengeServiceApi.md#challengeServiceGetChallengeAttachmentUploadUrl) | **POST** /api/v1/challenge/attachment_upload_urls | GetChallengeAttachmentUploadUrl returns string that represents s3 URL that can be used to upload attachment for the challenge. The file in attachment can be any file that provides additional information about the disputable outlier. Need to specify asset ID, submitted ID and file name.
[**challengeServiceGetChallengeDetails**](ChallengeServiceApi.md#challengeServiceGetChallengeDetails) | **POST** /api/v1/challenge-details | 



## challengeServiceChallengeActive

> TitaniumChallengeActiveResponse challengeServiceChallengeActive(body)

ChallengeActive returns active challenges(according to request) in active status(challenge process is active).

### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.ChallengeServiceApi();
let body = new ClearconsensusSdk.TitaniumChallengeActiveRequest(); // TitaniumChallengeActiveRequest | 
apiInstance.challengeServiceChallengeActive(body, (error, data, response) => {
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
 **body** | [**TitaniumChallengeActiveRequest**](TitaniumChallengeActiveRequest.md)|  | 

### Return type

[**TitaniumChallengeActiveResponse**](TitaniumChallengeActiveResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## challengeServiceChallengeCreate

> TitaniumChallengeCreateResponse challengeServiceChallengeCreate(body)

ChallengeCreate creates challenge in the system.(Initiate process by dealer) To create \&quot;challenger\&quot; needs to be authorised and challenge can be created only if one of their own submitted data points has been declared an outlier in the published Consensus. Need to specify asset and fill out evidence information. Returns response that contains ticket ID of the Challenge or the Error.

### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.ChallengeServiceApi();
let body = new ClearconsensusSdk.TitaniumChallengeCreateRequest(); // TitaniumChallengeCreateRequest | 
apiInstance.challengeServiceChallengeCreate(body, (error, data, response) => {
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
 **body** | [**TitaniumChallengeCreateRequest**](TitaniumChallengeCreateRequest.md)|  | 

### Return type

[**TitaniumChallengeCreateResponse**](TitaniumChallengeCreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## challengeServiceChallengeDecision

> TitaniumMessageResponse challengeServiceChallengeDecision(body)

ChallengeDecision sets decision of the challenge according to request.

### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.ChallengeServiceApi();
let body = new ClearconsensusSdk.TitaniumChallengeDecisionRequest(); // TitaniumChallengeDecisionRequest | 
apiInstance.challengeServiceChallengeDecision(body, (error, data, response) => {
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
 **body** | [**TitaniumChallengeDecisionRequest**](TitaniumChallengeDecisionRequest.md)|  | 

### Return type

[**TitaniumMessageResponse**](TitaniumMessageResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## challengeServiceChallengeFormMeta

> TitaniumChallengeFormMetaResponse challengeServiceChallengeFormMeta(body)

ChallengeFormMeta is used to request information(template) about the form fields required to submit a challenge for a specific asset and evidence type. Returns response with template with pre-filled data.

### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.ChallengeServiceApi();
let body = new ClearconsensusSdk.TitaniumChallengeFormMetaRequest(); // TitaniumChallengeFormMetaRequest | 
apiInstance.challengeServiceChallengeFormMeta(body, (error, data, response) => {
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
 **body** | [**TitaniumChallengeFormMetaRequest**](TitaniumChallengeFormMetaRequest.md)|  | 

### Return type

[**TitaniumChallengeFormMetaResponse**](TitaniumChallengeFormMetaResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## challengeServiceChallengeFreezeAction

> TitaniumMessageResponse challengeServiceChallengeFreezeAction(body)

ChallengeFreezeAction makes challenge process stopped or not according to request.

### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.ChallengeServiceApi();
let body = new ClearconsensusSdk.TitaniumChallengeFreezeActionRequest(); // TitaniumChallengeFreezeActionRequest | 
apiInstance.challengeServiceChallengeFreezeAction(body, (error, data, response) => {
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
 **body** | [**TitaniumChallengeFreezeActionRequest**](TitaniumChallengeFreezeActionRequest.md)|  | 

### Return type

[**TitaniumMessageResponse**](TitaniumMessageResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## challengeServiceChallengeFreezeStatus

> TitaniumStatusResponse challengeServiceChallengeFreezeStatus(body)

ChallengeFreezeStatus returns StatusResponse that contains string that represents freeze status of challenges if the challenge process is stopped and nothing if the one is not. Challenge can be stopped by operator.Dealer can see the freeze status using this method. Need to specify consensus(where outliers exists) run timestamp.

### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.ChallengeServiceApi();
let body = new ClearconsensusSdk.TitaniumChallengeFreezeStatusRequest(); // TitaniumChallengeFreezeStatusRequest | 
apiInstance.challengeServiceChallengeFreezeStatus(body, (error, data, response) => {
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
 **body** | [**TitaniumChallengeFreezeStatusRequest**](TitaniumChallengeFreezeStatusRequest.md)|  | 

### Return type

[**TitaniumStatusResponse**](TitaniumStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## challengeServiceChallengeHistory

> TitaniumChallengeHistoryResponse challengeServiceChallengeHistory(body)

ChallengeHistory return already closed challenges according to request.

### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.ChallengeServiceApi();
let body = new ClearconsensusSdk.TitaniumChallengeHistoryRequest(); // TitaniumChallengeHistoryRequest | 
apiInstance.challengeServiceChallengeHistory(body, (error, data, response) => {
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
 **body** | [**TitaniumChallengeHistoryRequest**](TitaniumChallengeHistoryRequest.md)|  | 

### Return type

[**TitaniumChallengeHistoryResponse**](TitaniumChallengeHistoryResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## challengeServiceChallengeList

> TitaniumChallengeListResponse challengeServiceChallengeList(body)

ChallengeList returns list of challenges according to request.

### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.ChallengeServiceApi();
let body = new ClearconsensusSdk.TitaniumChallengeListRequest(); // TitaniumChallengeListRequest | 
apiInstance.challengeServiceChallengeList(body, (error, data, response) => {
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
 **body** | [**TitaniumChallengeListRequest**](TitaniumChallengeListRequest.md)|  | 

### Return type

[**TitaniumChallengeListResponse**](TitaniumChallengeListResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## challengeServiceGetChallengeAttachmentUploadUrl

> TitaniumGetAttachmentUploadUrlResponse challengeServiceGetChallengeAttachmentUploadUrl(body)

GetChallengeAttachmentUploadUrl returns string that represents s3 URL that can be used to upload attachment for the challenge. The file in attachment can be any file that provides additional information about the disputable outlier. Need to specify asset ID, submitted ID and file name.

### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.ChallengeServiceApi();
let body = new ClearconsensusSdk.TitaniumGetAttachmentUploadUrlRequest(); // TitaniumGetAttachmentUploadUrlRequest | 
apiInstance.challengeServiceGetChallengeAttachmentUploadUrl(body, (error, data, response) => {
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
 **body** | [**TitaniumGetAttachmentUploadUrlRequest**](TitaniumGetAttachmentUploadUrlRequest.md)|  | 

### Return type

[**TitaniumGetAttachmentUploadUrlResponse**](TitaniumGetAttachmentUploadUrlResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## challengeServiceGetChallengeDetails

> TitaniumGetChallengeDetailsResponse challengeServiceGetChallengeDetails(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.ChallengeServiceApi();
let body = new ClearconsensusSdk.TitaniumGetChallengeDetailsRequest(); // TitaniumGetChallengeDetailsRequest | 
apiInstance.challengeServiceGetChallengeDetails(body, (error, data, response) => {
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
 **body** | [**TitaniumGetChallengeDetailsRequest**](TitaniumGetChallengeDetailsRequest.md)|  | 

### Return type

[**TitaniumGetChallengeDetailsResponse**](TitaniumGetChallengeDetailsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

