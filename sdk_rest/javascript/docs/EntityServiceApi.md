# ClearconsensusSdk.EntityServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**entityServiceCreate**](EntityServiceApi.md#entityServiceCreate) | **POST** /api/v1/user-management/entities/create | 
[**entityServiceFind**](EntityServiceApi.md#entityServiceFind) | **POST** /api/v1/user-management/entities/find | 
[**entityServiceGetAllEnabledOnly**](EntityServiceApi.md#entityServiceGetAllEnabledOnly) | **POST** /api/v1/user-management/entities/getAllByEnabled | 
[**entityServiceGetById**](EntityServiceApi.md#entityServiceGetById) | **POST** /api/v1/user-management/entities/getById | 
[**entityServiceUpdate**](EntityServiceApi.md#entityServiceUpdate) | **POST** /api/v1/user-management/entities/update | 



## entityServiceCreate

> ProtoServiceResponse entityServiceCreate(body)



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

[**ProtoServiceResponse**](ProtoServiceResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## entityServiceFind

> ProtoServiceResponse entityServiceFind(body)



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

[**ProtoServiceResponse**](ProtoServiceResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## entityServiceGetAllEnabledOnly

> ProtoServiceResponse entityServiceGetAllEnabledOnly(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.EntityServiceApi();
let body = true; // Boolean | 
apiInstance.entityServiceGetAllEnabledOnly(body, (error, data, response) => {
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
 **body** | **Boolean**|  | 

### Return type

[**ProtoServiceResponse**](ProtoServiceResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## entityServiceGetById

> ProtoServiceResponse entityServiceGetById(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.EntityServiceApi();
let body = "body_example"; // String | 
apiInstance.entityServiceGetById(body, (error, data, response) => {
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
 **body** | **String**|  | 

### Return type

[**ProtoServiceResponse**](ProtoServiceResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## entityServiceUpdate

> ProtoServiceResponse entityServiceUpdate(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.EntityServiceApi();
let body = new ClearconsensusSdk.ProtoEntityDto(); // ProtoEntityDto | 
apiInstance.entityServiceUpdate(body, (error, data, response) => {
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

[**ProtoServiceResponse**](ProtoServiceResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

