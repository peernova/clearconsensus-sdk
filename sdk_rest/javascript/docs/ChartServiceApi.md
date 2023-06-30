# ClearconsensusSdk.ChartServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chartServiceGetChartData**](ChartServiceApi.md#chartServiceGetChartData) | **POST** /api/v1/analytics/chart-data | 



## chartServiceGetChartData

> TitaniumGetChartDataResponse chartServiceGetChartData(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.ChartServiceApi();
let body = new ClearconsensusSdk.TitaniumGetChartDataRequest(); // TitaniumGetChartDataRequest | 
apiInstance.chartServiceGetChartData(body, (error, data, response) => {
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
 **body** | [**TitaniumGetChartDataRequest**](TitaniumGetChartDataRequest.md)|  | 

### Return type

[**TitaniumGetChartDataResponse**](TitaniumGetChartDataResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

