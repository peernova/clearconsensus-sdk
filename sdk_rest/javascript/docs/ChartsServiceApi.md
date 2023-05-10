# ClearconsensusSdk.ChartsServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chartsServiceCharts**](ChartsServiceApi.md#chartsServiceCharts) | **POST** /api/v1/charts | Charts returns information about specific chart related to the specific asset.
[**chartsServiceChartsCurrencies**](ChartsServiceApi.md#chartsServiceChartsCurrencies) | **POST** /api/v1/charts/currencies | ChartsCurrencies returns information about the chart related to specific currency pair.



## chartsServiceCharts

> TitaniumChartsResponse chartsServiceCharts(body)

Charts returns information about specific chart related to the specific asset.

### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.ChartsServiceApi();
let body = new ClearconsensusSdk.TitaniumChartsRequest(); // TitaniumChartsRequest | 
apiInstance.chartsServiceCharts(body, (error, data, response) => {
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
 **body** | [**TitaniumChartsRequest**](TitaniumChartsRequest.md)|  | 

### Return type

[**TitaniumChartsResponse**](TitaniumChartsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## chartsServiceChartsCurrencies

> TitaniumChartsCurrenciesResponse chartsServiceChartsCurrencies(body)

ChartsCurrencies returns information about the chart related to specific currency pair.

### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.ChartsServiceApi();
let body = new ClearconsensusSdk.TitaniumChartsCurrenciesRequest(); // TitaniumChartsCurrenciesRequest | 
apiInstance.chartsServiceChartsCurrencies(body, (error, data, response) => {
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
 **body** | [**TitaniumChartsCurrenciesRequest**](TitaniumChartsCurrenciesRequest.md)|  | 

### Return type

[**TitaniumChartsCurrenciesResponse**](TitaniumChartsCurrenciesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

