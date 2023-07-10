# ClearconsensusSdk.OperatorServicePrivateApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**operatorServicePrivateAddAsset**](OperatorServicePrivateApi.md#operatorServicePrivateAddAsset) | **POST** /api/v1/operator/assets/add | AddAsset adds asset to the system.
[**operatorServicePrivateAddClient**](OperatorServicePrivateApi.md#operatorServicePrivateAddClient) | **POST** /api/v1/operator/client/add | 
[**operatorServicePrivateAddSupportedFields**](OperatorServicePrivateApi.md#operatorServicePrivateAddSupportedFields) | **POST** /api/v1/operator/add/field-values | 
[**operatorServicePrivateAssets**](OperatorServicePrivateApi.md#operatorServicePrivateAssets) | **POST** /api/v1/operator/assets | 
[**operatorServicePrivateCreateSupportedFields**](OperatorServicePrivateApi.md#operatorServicePrivateCreateSupportedFields) | **POST** /api/v1/operator/create/field-values | 
[**operatorServicePrivateDeleteSupportedFields**](OperatorServicePrivateApi.md#operatorServicePrivateDeleteSupportedFields) | **POST** /api/v1/operator/delete/field-values | 
[**operatorServicePrivateEvpStatuses**](OperatorServicePrivateApi.md#operatorServicePrivateEvpStatuses) | **POST** /api/v1/operator/evaluated-prices/slice | 
[**operatorServicePrivateExportReport**](OperatorServicePrivateApi.md#operatorServicePrivateExportReport) | **POST** /api/v1/operator/report | ExportReport returns pre signed s3 urls which can be used for export report(and compression type)
[**operatorServicePrivateListClients**](OperatorServicePrivateApi.md#operatorServicePrivateListClients) | **GET** /api/v1/operator/client/list | 
[**operatorServicePrivateOperatorOutliers**](OperatorServicePrivateApi.md#operatorServicePrivateOperatorOutliers) | **POST** /api/v1/operator-outliers | 
[**operatorServicePrivateOutliers**](OperatorServicePrivateApi.md#operatorServicePrivateOutliers) | **POST** /api/v1/operator/outliers | 
[**operatorServicePrivateRecentAssets**](OperatorServicePrivateApi.md#operatorServicePrivateRecentAssets) | **POST** /api/v1/operator/recentassets | 
[**operatorServicePrivateUploadDTCC**](OperatorServicePrivateApi.md#operatorServicePrivateUploadDTCC) | **POST** /api/v1/operator/dtcc-trades/upload | 
[**operatorServicePrivateUploadEVP**](OperatorServicePrivateApi.md#operatorServicePrivateUploadEVP) | **POST** /api/v1/operator/evp/upload | 



## operatorServicePrivateAddAsset

> TitaniumMessageResponse operatorServicePrivateAddAsset(body)

AddAsset adds asset to the system.

### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.OperatorServicePrivateApi();
let body = new ClearconsensusSdk.TitaniumAddAssetRequest(); // TitaniumAddAssetRequest | 
apiInstance.operatorServicePrivateAddAsset(body, (error, data, response) => {
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
 **body** | [**TitaniumAddAssetRequest**](TitaniumAddAssetRequest.md)|  | 

### Return type

[**TitaniumMessageResponse**](TitaniumMessageResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## operatorServicePrivateAddClient

> TitaniumMessageResponse operatorServicePrivateAddClient(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.OperatorServicePrivateApi();
let body = new ClearconsensusSdk.TitaniumClientName(); // TitaniumClientName | 
apiInstance.operatorServicePrivateAddClient(body, (error, data, response) => {
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
 **body** | [**TitaniumClientName**](TitaniumClientName.md)|  | 

### Return type

[**TitaniumMessageResponse**](TitaniumMessageResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## operatorServicePrivateAddSupportedFields

> TitaniumMessageResponse operatorServicePrivateAddSupportedFields(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.OperatorServicePrivateApi();
let body = new ClearconsensusSdk.TitaniumSupportedFieldsValues(); // TitaniumSupportedFieldsValues | 
apiInstance.operatorServicePrivateAddSupportedFields(body, (error, data, response) => {
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
 **body** | [**TitaniumSupportedFieldsValues**](TitaniumSupportedFieldsValues.md)|  | 

### Return type

[**TitaniumMessageResponse**](TitaniumMessageResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## operatorServicePrivateAssets

> TitaniumAssetsResponse operatorServicePrivateAssets(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.OperatorServicePrivateApi();
let body = new ClearconsensusSdk.TitaniumAssetsRequest(); // TitaniumAssetsRequest | 
apiInstance.operatorServicePrivateAssets(body, (error, data, response) => {
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
 **body** | [**TitaniumAssetsRequest**](TitaniumAssetsRequest.md)|  | 

### Return type

[**TitaniumAssetsResponse**](TitaniumAssetsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## operatorServicePrivateCreateSupportedFields

> TitaniumMessageResponse operatorServicePrivateCreateSupportedFields(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.OperatorServicePrivateApi();
let body = new ClearconsensusSdk.TitaniumSupportedFieldsValues(); // TitaniumSupportedFieldsValues | 
apiInstance.operatorServicePrivateCreateSupportedFields(body, (error, data, response) => {
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
 **body** | [**TitaniumSupportedFieldsValues**](TitaniumSupportedFieldsValues.md)|  | 

### Return type

[**TitaniumMessageResponse**](TitaniumMessageResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## operatorServicePrivateDeleteSupportedFields

> TitaniumMessageResponse operatorServicePrivateDeleteSupportedFields(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.OperatorServicePrivateApi();
let body = new ClearconsensusSdk.TitaniumSupportedFieldsValues(); // TitaniumSupportedFieldsValues | 
apiInstance.operatorServicePrivateDeleteSupportedFields(body, (error, data, response) => {
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
 **body** | [**TitaniumSupportedFieldsValues**](TitaniumSupportedFieldsValues.md)|  | 

### Return type

[**TitaniumMessageResponse**](TitaniumMessageResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## operatorServicePrivateEvpStatuses

> TitaniumEvpStatusesResponse operatorServicePrivateEvpStatuses(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.OperatorServicePrivateApi();
let body = new ClearconsensusSdk.TitaniumEvpStatusesRequest(); // TitaniumEvpStatusesRequest | 
apiInstance.operatorServicePrivateEvpStatuses(body, (error, data, response) => {
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
 **body** | [**TitaniumEvpStatusesRequest**](TitaniumEvpStatusesRequest.md)|  | 

### Return type

[**TitaniumEvpStatusesResponse**](TitaniumEvpStatusesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## operatorServicePrivateExportReport

> TitaniumExportResponse operatorServicePrivateExportReport(body)

ExportReport returns pre signed s3 urls which can be used for export report(and compression type)

### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.OperatorServicePrivateApi();
let body = new ClearconsensusSdk.TitaniumExportReportRequest(); // TitaniumExportReportRequest | 
apiInstance.operatorServicePrivateExportReport(body, (error, data, response) => {
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
 **body** | [**TitaniumExportReportRequest**](TitaniumExportReportRequest.md)|  | 

### Return type

[**TitaniumExportResponse**](TitaniumExportResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## operatorServicePrivateListClients

> TitaniumListClientsResponse operatorServicePrivateListClients()



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.OperatorServicePrivateApi();
apiInstance.operatorServicePrivateListClients((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**TitaniumListClientsResponse**](TitaniumListClientsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## operatorServicePrivateOperatorOutliers

> TitaniumOperatorOutliersResponse operatorServicePrivateOperatorOutliers(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.OperatorServicePrivateApi();
let body = new ClearconsensusSdk.TitaniumOperatorOutliersRequest(); // TitaniumOperatorOutliersRequest | 
apiInstance.operatorServicePrivateOperatorOutliers(body, (error, data, response) => {
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
 **body** | [**TitaniumOperatorOutliersRequest**](TitaniumOperatorOutliersRequest.md)|  | 

### Return type

[**TitaniumOperatorOutliersResponse**](TitaniumOperatorOutliersResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## operatorServicePrivateOutliers

> TitaniumOutliersResponse operatorServicePrivateOutliers(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.OperatorServicePrivateApi();
let body = new ClearconsensusSdk.TitaniumOutliersRequest(); // TitaniumOutliersRequest | 
apiInstance.operatorServicePrivateOutliers(body, (error, data, response) => {
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


## operatorServicePrivateRecentAssets

> TitaniumRecentAssetsResponse operatorServicePrivateRecentAssets(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.OperatorServicePrivateApi();
let body = new ClearconsensusSdk.TitaniumRecentAssetsRequest(); // TitaniumRecentAssetsRequest | 
apiInstance.operatorServicePrivateRecentAssets(body, (error, data, response) => {
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
 **body** | [**TitaniumRecentAssetsRequest**](TitaniumRecentAssetsRequest.md)|  | 

### Return type

[**TitaniumRecentAssetsResponse**](TitaniumRecentAssetsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## operatorServicePrivateUploadDTCC

> TitaniumUploadURLResponse operatorServicePrivateUploadDTCC(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.OperatorServicePrivateApi();
let body = new ClearconsensusSdk.TitaniumUploadDTCCRequest(); // TitaniumUploadDTCCRequest | 
apiInstance.operatorServicePrivateUploadDTCC(body, (error, data, response) => {
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
 **body** | [**TitaniumUploadDTCCRequest**](TitaniumUploadDTCCRequest.md)|  | 

### Return type

[**TitaniumUploadURLResponse**](TitaniumUploadURLResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## operatorServicePrivateUploadEVP

> TitaniumUploadURLResponse operatorServicePrivateUploadEVP(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.OperatorServicePrivateApi();
let body = new ClearconsensusSdk.TitaniumUploadEVPRequest(); // TitaniumUploadEVPRequest | 
apiInstance.operatorServicePrivateUploadEVP(body, (error, data, response) => {
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
 **body** | [**TitaniumUploadEVPRequest**](TitaniumUploadEVPRequest.md)|  | 

### Return type

[**TitaniumUploadURLResponse**](TitaniumUploadURLResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

