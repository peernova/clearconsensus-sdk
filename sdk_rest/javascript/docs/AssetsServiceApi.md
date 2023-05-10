# ClearconsensusSdk.AssetsServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assetsServiceAssets**](AssetsServiceApi.md#assetsServiceAssets) | **POST** /api/v1/assets | Assets returns asset from the system according to request.
[**assetsServiceAssetsList**](AssetsServiceApi.md#assetsServiceAssetsList) | **POST** /api/v1/assets/list | AssetsList return list of assets according to snap time.
[**assetsServiceRecentAssets**](AssetsServiceApi.md#assetsServiceRecentAssets) | **POST** /api/v1/recentassets | RecentAssets returns recent added assets according to request.
[**assetsServiceSupportedAssets**](AssetsServiceApi.md#assetsServiceSupportedAssets) | **GET** /api/v1/supported/assets | 



## assetsServiceAssets

> TitaniumAssetsResponse assetsServiceAssets(body)

Assets returns asset from the system according to request.

### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.AssetsServiceApi();
let body = new ClearconsensusSdk.TitaniumAssetsRequest(); // TitaniumAssetsRequest | 
apiInstance.assetsServiceAssets(body, (error, data, response) => {
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


## assetsServiceAssetsList

> TitaniumAssetsListResponse assetsServiceAssetsList(body)

AssetsList return list of assets according to snap time.

### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.AssetsServiceApi();
let body = new ClearconsensusSdk.TitaniumAssetsListRequest(); // TitaniumAssetsListRequest | 
apiInstance.assetsServiceAssetsList(body, (error, data, response) => {
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
 **body** | [**TitaniumAssetsListRequest**](TitaniumAssetsListRequest.md)|  | 

### Return type

[**TitaniumAssetsListResponse**](TitaniumAssetsListResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## assetsServiceRecentAssets

> TitaniumRecentAssetsResponse assetsServiceRecentAssets(body)

RecentAssets returns recent added assets according to request.

### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.AssetsServiceApi();
let body = new ClearconsensusSdk.TitaniumRecentAssetsRequest(); // TitaniumRecentAssetsRequest | 
apiInstance.assetsServiceRecentAssets(body, (error, data, response) => {
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


## assetsServiceSupportedAssets

> TitaniumAssetsListResponse assetsServiceSupportedAssets()



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.AssetsServiceApi();
apiInstance.assetsServiceSupportedAssets((error, data, response) => {
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

[**TitaniumAssetsListResponse**](TitaniumAssetsListResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

