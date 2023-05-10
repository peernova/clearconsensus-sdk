# ClearconsensusSdk.AnalyticsControllerApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analyticsControllerFindConsensusAnalytics**](AnalyticsControllerApi.md#analyticsControllerFindConsensusAnalytics) | **POST** /api/v1/analytics/consensus/find | FindConsensusAnalytics returns analytics related to specific consensus according to request.
[**analyticsControllerFindDataQualityErrors**](AnalyticsControllerApi.md#analyticsControllerFindDataQualityErrors) | **POST** /api/v1/analytics/data-quality-errors/find | FindDataQualityErrors returns data quality errors according to request.
[**analyticsControllerGetAllConsensusAnalytics**](AnalyticsControllerApi.md#analyticsControllerGetAllConsensusAnalytics) | **POST** /api/v1/analytics/consensus/get-all | GetAllConsensusAnalytics returns analytics related to all consensuses.
[**analyticsControllerGetAllDataQualityErrors**](AnalyticsControllerApi.md#analyticsControllerGetAllDataQualityErrors) | **POST** /api/v1/analytics/data-quality-errors/get-all | GetAllDataQualityErrors returns all existing data quality errors in the system.
[**analyticsControllerGetHistogram**](AnalyticsControllerApi.md#analyticsControllerGetHistogram) | **POST** /api/v1/analytics/histogram/get-all | GetHistogram returns analytics(submission and consensus) represented by histogram according to request.
[**analyticsControllerGetPredefinedFilter**](AnalyticsControllerApi.md#analyticsControllerGetPredefinedFilter) | **POST** /api/v1/analytics/predefined/filters | GetPredefinedFilter returns pre defined filters according to request.



## analyticsControllerFindConsensusAnalytics

> TitaniumGenericChartMetadataDataQualityResponse analyticsControllerFindConsensusAnalytics(body)

FindConsensusAnalytics returns analytics related to specific consensus according to request.

### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.AnalyticsControllerApi();
let body = new ClearconsensusSdk.TitaniumGenericChartMetadataDataQuality(); // TitaniumGenericChartMetadataDataQuality | 
apiInstance.analyticsControllerFindConsensusAnalytics(body, (error, data, response) => {
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
 **body** | [**TitaniumGenericChartMetadataDataQuality**](TitaniumGenericChartMetadataDataQuality.md)|  | 

### Return type

[**TitaniumGenericChartMetadataDataQualityResponse**](TitaniumGenericChartMetadataDataQualityResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## analyticsControllerFindDataQualityErrors

> TitaniumGenericChartMetadataDataQualityResponse analyticsControllerFindDataQualityErrors(body)

FindDataQualityErrors returns data quality errors according to request.

### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.AnalyticsControllerApi();
let body = new ClearconsensusSdk.TitaniumGenericChartMetadataDataQuality(); // TitaniumGenericChartMetadataDataQuality | 
apiInstance.analyticsControllerFindDataQualityErrors(body, (error, data, response) => {
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
 **body** | [**TitaniumGenericChartMetadataDataQuality**](TitaniumGenericChartMetadataDataQuality.md)|  | 

### Return type

[**TitaniumGenericChartMetadataDataQualityResponse**](TitaniumGenericChartMetadataDataQualityResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## analyticsControllerGetAllConsensusAnalytics

> TitaniumGenericChartMetadataDataQualityResponse analyticsControllerGetAllConsensusAnalytics()

GetAllConsensusAnalytics returns analytics related to all consensuses.

### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.AnalyticsControllerApi();
apiInstance.analyticsControllerGetAllConsensusAnalytics((error, data, response) => {
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

[**TitaniumGenericChartMetadataDataQualityResponse**](TitaniumGenericChartMetadataDataQualityResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## analyticsControllerGetAllDataQualityErrors

> TitaniumGenericChartMetadataDataQualityResponse analyticsControllerGetAllDataQualityErrors()

GetAllDataQualityErrors returns all existing data quality errors in the system.

### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.AnalyticsControllerApi();
apiInstance.analyticsControllerGetAllDataQualityErrors((error, data, response) => {
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

[**TitaniumGenericChartMetadataDataQualityResponse**](TitaniumGenericChartMetadataDataQualityResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## analyticsControllerGetHistogram

> TitaniumHistogramResponse analyticsControllerGetHistogram()

GetHistogram returns analytics(submission and consensus) represented by histogram according to request.

### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.AnalyticsControllerApi();
apiInstance.analyticsControllerGetHistogram((error, data, response) => {
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

[**TitaniumHistogramResponse**](TitaniumHistogramResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## analyticsControllerGetPredefinedFilter

> TitaniumGetPredefinedFiltersResponse analyticsControllerGetPredefinedFilter()

GetPredefinedFilter returns pre defined filters according to request.

### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.AnalyticsControllerApi();
apiInstance.analyticsControllerGetPredefinedFilter((error, data, response) => {
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

[**TitaniumGetPredefinedFiltersResponse**](TitaniumGetPredefinedFiltersResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

