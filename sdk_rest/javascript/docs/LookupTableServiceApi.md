# ClearconsensusSdk.LookupTableServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lookupTableServiceAddLookupTable**](LookupTableServiceApi.md#lookupTableServiceAddLookupTable) | **POST** /api/v1/lookuptable/add | 
[**lookupTableServiceGetLookupTable**](LookupTableServiceApi.md#lookupTableServiceGetLookupTable) | **POST** /api/v1/lookuptable/get | 
[**lookupTableServiceListLookupTableVersions**](LookupTableServiceApi.md#lookupTableServiceListLookupTableVersions) | **POST** /api/v1/lookuptable/versions | 
[**lookupTableServiceListLookupTables**](LookupTableServiceApi.md#lookupTableServiceListLookupTables) | **POST** /api/v1/lookuptable/list | 



## lookupTableServiceAddLookupTable

> TitaniumAcknowledgeResponse lookupTableServiceAddLookupTable(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.LookupTableServiceApi();
let body = new ClearconsensusSdk.TitaniumAddLookupTableRequest(); // TitaniumAddLookupTableRequest | 
apiInstance.lookupTableServiceAddLookupTable(body, (error, data, response) => {
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
 **body** | [**TitaniumAddLookupTableRequest**](TitaniumAddLookupTableRequest.md)|  | 

### Return type

[**TitaniumAcknowledgeResponse**](TitaniumAcknowledgeResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## lookupTableServiceGetLookupTable

> TitaniumGetLookupTableResponse lookupTableServiceGetLookupTable(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.LookupTableServiceApi();
let body = new ClearconsensusSdk.TitaniumGetDefinition(); // TitaniumGetDefinition | 
apiInstance.lookupTableServiceGetLookupTable(body, (error, data, response) => {
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
 **body** | [**TitaniumGetDefinition**](TitaniumGetDefinition.md)|  | 

### Return type

[**TitaniumGetLookupTableResponse**](TitaniumGetLookupTableResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## lookupTableServiceListLookupTableVersions

> TitaniumListVersionResponse lookupTableServiceListLookupTableVersions(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.LookupTableServiceApi();
let body = new ClearconsensusSdk.TitaniumGetDefinition(); // TitaniumGetDefinition | 
apiInstance.lookupTableServiceListLookupTableVersions(body, (error, data, response) => {
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
 **body** | [**TitaniumGetDefinition**](TitaniumGetDefinition.md)|  | 

### Return type

[**TitaniumListVersionResponse**](TitaniumListVersionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## lookupTableServiceListLookupTables

> TitaniumListLookupTableResponse lookupTableServiceListLookupTables(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.LookupTableServiceApi();
let body = new ClearconsensusSdk.TitaniumListRequest(); // TitaniumListRequest | 
apiInstance.lookupTableServiceListLookupTables(body, (error, data, response) => {
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

[**TitaniumListLookupTableResponse**](TitaniumListLookupTableResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

