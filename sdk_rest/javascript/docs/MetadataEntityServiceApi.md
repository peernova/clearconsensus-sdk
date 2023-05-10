# ClearconsensusSdk.MetadataEntityServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**metadataEntityServiceAddEntity**](MetadataEntityServiceApi.md#metadataEntityServiceAddEntity) | **POST** /api/v1/entity/add | 
[**metadataEntityServiceDisableEntity**](MetadataEntityServiceApi.md#metadataEntityServiceDisableEntity) | **POST** /api/v1/entity/disable | 
[**metadataEntityServiceEnableEntity**](MetadataEntityServiceApi.md#metadataEntityServiceEnableEntity) | **POST** /api/v1/entity/enable | 
[**metadataEntityServiceGetEntity**](MetadataEntityServiceApi.md#metadataEntityServiceGetEntity) | **POST** /api/v1/entity/get | 



## metadataEntityServiceAddEntity

> TitaniumAcknowledgeResponse metadataEntityServiceAddEntity(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.MetadataEntityServiceApi();
let body = new ClearconsensusSdk.TitaniumEntityDefinition(); // TitaniumEntityDefinition | 
apiInstance.metadataEntityServiceAddEntity(body, (error, data, response) => {
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
 **body** | [**TitaniumEntityDefinition**](TitaniumEntityDefinition.md)|  | 

### Return type

[**TitaniumAcknowledgeResponse**](TitaniumAcknowledgeResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## metadataEntityServiceDisableEntity

> TitaniumAcknowledgeResponse metadataEntityServiceDisableEntity(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.MetadataEntityServiceApi();
let body = new ClearconsensusSdk.TitaniumEntityIdentifier(); // TitaniumEntityIdentifier | 
apiInstance.metadataEntityServiceDisableEntity(body, (error, data, response) => {
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
 **body** | [**TitaniumEntityIdentifier**](TitaniumEntityIdentifier.md)|  | 

### Return type

[**TitaniumAcknowledgeResponse**](TitaniumAcknowledgeResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## metadataEntityServiceEnableEntity

> TitaniumAcknowledgeResponse metadataEntityServiceEnableEntity(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.MetadataEntityServiceApi();
let body = new ClearconsensusSdk.TitaniumEntityIdentifier(); // TitaniumEntityIdentifier | 
apiInstance.metadataEntityServiceEnableEntity(body, (error, data, response) => {
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
 **body** | [**TitaniumEntityIdentifier**](TitaniumEntityIdentifier.md)|  | 

### Return type

[**TitaniumAcknowledgeResponse**](TitaniumAcknowledgeResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## metadataEntityServiceGetEntity

> TitaniumEntityDefinition metadataEntityServiceGetEntity(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.MetadataEntityServiceApi();
let body = new ClearconsensusSdk.TitaniumEntityIdentifier(); // TitaniumEntityIdentifier | 
apiInstance.metadataEntityServiceGetEntity(body, (error, data, response) => {
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
 **body** | [**TitaniumEntityIdentifier**](TitaniumEntityIdentifier.md)|  | 

### Return type

[**TitaniumEntityDefinition**](TitaniumEntityDefinition.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

