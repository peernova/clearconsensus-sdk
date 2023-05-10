# ClearconsensusSdk.MarketServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**marketServiceMarketSnapTime**](MarketServiceApi.md#marketServiceMarketSnapTime) | **GET** /api/v1/market/snap-time | MarketSnapTime returns time for which the prices(calculated in consensus) are valid.(Time of market closing)



## marketServiceMarketSnapTime

> TitaniumMarketSnapTimeResponse marketServiceMarketSnapTime()

MarketSnapTime returns time for which the prices(calculated in consensus) are valid.(Time of market closing)

### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.MarketServiceApi();
apiInstance.marketServiceMarketSnapTime((error, data, response) => {
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

[**TitaniumMarketSnapTimeResponse**](TitaniumMarketSnapTimeResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

