# ClearconsensusSdk.EntityServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**entityServiceCreate**](EntityServiceApi.md#entityServiceCreate) | **POST** /api/v1/user-management/entities/create | 
[**entityServiceFind**](EntityServiceApi.md#entityServiceFind) | **POST** /api/v1/user-management/entities | 
[**entityServiceGetAllEnabledOnly**](EntityServiceApi.md#entityServiceGetAllEnabledOnly) | **GET** /api/v1/user-management/entities | 
[**entityServiceGetById**](EntityServiceApi.md#entityServiceGetById) | **GET** /api/v1/user-management/entities/{id} | 
[**entityServiceUpdate**](EntityServiceApi.md#entityServiceUpdate) | **PUT** /api/v1/user-management/entities/{id} | 



## entityServiceCreate

> ProtoEntityResponse entityServiceCreate(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.EntityServiceApi();
let body = new ClearconsensusSdk.ProtoEntityDto(); // ProtoEntityDto | 
apiInstance.entityServiceCreate(body, (error, data, response) => {
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
 **body** | [**ProtoEntityDto**](ProtoEntityDto.md)|  | 

### Return type

[**ProtoEntityResponse**](ProtoEntityResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## entityServiceFind

> ProtoTableResponse entityServiceFind(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.EntityServiceApi();
let body = new ClearconsensusSdk.ProtoSearchCriteria(); // ProtoSearchCriteria | 
apiInstance.entityServiceFind(body, (error, data, response) => {
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
 **body** | [**ProtoSearchCriteria**](ProtoSearchCriteria.md)|  | 

### Return type

[**ProtoTableResponse**](ProtoTableResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## entityServiceGetAllEnabledOnly

> ProtoEntitiesResponse entityServiceGetAllEnabledOnly()



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.EntityServiceApi();
apiInstance.entityServiceGetAllEnabledOnly((error, data, response) => {
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

[**ProtoEntitiesResponse**](ProtoEntitiesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## entityServiceGetById

> ProtoEntityResponse entityServiceGetById(id)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.EntityServiceApi();
let id = "id_example"; // String | 
apiInstance.entityServiceGetById(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

[**ProtoEntityResponse**](ProtoEntityResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## entityServiceUpdate

> ProtoEntityResponse entityServiceUpdate(id, body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.EntityServiceApi();
let id = "id_example"; // String | 
let body = new ClearconsensusSdk.EntityServiceUpdateRequest(); // EntityServiceUpdateRequest | 
apiInstance.entityServiceUpdate(id, body, (error, data, response) => {
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
 **id** | **String**|  | 
 **body** | [**EntityServiceUpdateRequest**](EntityServiceUpdateRequest.md)|  | 

### Return type

[**ProtoEntityResponse**](ProtoEntityResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

