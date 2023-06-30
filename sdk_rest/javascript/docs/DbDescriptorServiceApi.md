# ClearconsensusSdk.DbDescriptorServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dbDescriptorServiceAddDbDescriptor**](DbDescriptorServiceApi.md#dbDescriptorServiceAddDbDescriptor) | **POST** /api/v1/db/descriptor/add | 
[**dbDescriptorServiceDescriptorDependencies**](DbDescriptorServiceApi.md#dbDescriptorServiceDescriptorDependencies) | **POST** /api/v1/db/descriptor/dependencies | 
[**dbDescriptorServiceDisableDbDescriptor**](DbDescriptorServiceApi.md#dbDescriptorServiceDisableDbDescriptor) | **POST** /api/v1/db/descriptor/disable | 
[**dbDescriptorServiceEnableDbDescriptor**](DbDescriptorServiceApi.md#dbDescriptorServiceEnableDbDescriptor) | **POST** /api/v1/db/descriptor/enable | 
[**dbDescriptorServiceGetDbDescriptor**](DbDescriptorServiceApi.md#dbDescriptorServiceGetDbDescriptor) | **POST** /api/v1/db/descriptor/get | 
[**dbDescriptorServiceGetDbDescriptorVersion**](DbDescriptorServiceApi.md#dbDescriptorServiceGetDbDescriptorVersion) | **GET** /api/v1/db/descriptor/version/{name}/{versionId} | 
[**dbDescriptorServiceListDbDescriptorVersions**](DbDescriptorServiceApi.md#dbDescriptorServiceListDbDescriptorVersions) | **POST** /api/v1/db/descriptor/versions | 
[**dbDescriptorServiceListDbDescriptors**](DbDescriptorServiceApi.md#dbDescriptorServiceListDbDescriptors) | **POST** /api/v1/db/descriptor/list | 



## dbDescriptorServiceAddDbDescriptor

> TitaniumAcknowledgeResponse dbDescriptorServiceAddDbDescriptor(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.DbDescriptorServiceApi();
let body = new ClearconsensusSdk.TitaniumDescriptorDefinition(); // TitaniumDescriptorDefinition | 
apiInstance.dbDescriptorServiceAddDbDescriptor(body, (error, data, response) => {
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
 **body** | [**TitaniumDescriptorDefinition**](TitaniumDescriptorDefinition.md)|  | 

### Return type

[**TitaniumAcknowledgeResponse**](TitaniumAcknowledgeResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## dbDescriptorServiceDescriptorDependencies

> TitaniumDescriptorDependenciesResponse dbDescriptorServiceDescriptorDependencies(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.DbDescriptorServiceApi();
let body = new ClearconsensusSdk.TitaniumGetDefinition(); // TitaniumGetDefinition | 
apiInstance.dbDescriptorServiceDescriptorDependencies(body, (error, data, response) => {
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

[**TitaniumDescriptorDependenciesResponse**](TitaniumDescriptorDependenciesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## dbDescriptorServiceDisableDbDescriptor

> TitaniumAcknowledgeResponse dbDescriptorServiceDisableDbDescriptor(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.DbDescriptorServiceApi();
let body = new ClearconsensusSdk.TitaniumEnableDisableRequest(); // TitaniumEnableDisableRequest | 
apiInstance.dbDescriptorServiceDisableDbDescriptor(body, (error, data, response) => {
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
 **body** | [**TitaniumEnableDisableRequest**](TitaniumEnableDisableRequest.md)|  | 

### Return type

[**TitaniumAcknowledgeResponse**](TitaniumAcknowledgeResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## dbDescriptorServiceEnableDbDescriptor

> TitaniumAcknowledgeResponse dbDescriptorServiceEnableDbDescriptor(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.DbDescriptorServiceApi();
let body = new ClearconsensusSdk.TitaniumEnableDisableRequest(); // TitaniumEnableDisableRequest | 
apiInstance.dbDescriptorServiceEnableDbDescriptor(body, (error, data, response) => {
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
 **body** | [**TitaniumEnableDisableRequest**](TitaniumEnableDisableRequest.md)|  | 

### Return type

[**TitaniumAcknowledgeResponse**](TitaniumAcknowledgeResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## dbDescriptorServiceGetDbDescriptor

> TitaniumDescriptorDefinitionResponse dbDescriptorServiceGetDbDescriptor(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.DbDescriptorServiceApi();
let body = new ClearconsensusSdk.TitaniumGetDefinition(); // TitaniumGetDefinition | 
apiInstance.dbDescriptorServiceGetDbDescriptor(body, (error, data, response) => {
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

[**TitaniumDescriptorDefinitionResponse**](TitaniumDescriptorDefinitionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## dbDescriptorServiceGetDbDescriptorVersion

> TitaniumDescriptorDefinitionResponse dbDescriptorServiceGetDbDescriptorVersion(name, versionId, opts)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.DbDescriptorServiceApi();
let name = "name_example"; // String | 
let versionId = "versionId_example"; // String | 
let opts = {
  'scope': "scope_example", // String | 
  'descriptorName': "descriptorName_example" // String | 
};
apiInstance.dbDescriptorServiceGetDbDescriptorVersion(name, versionId, opts, (error, data, response) => {
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
 **name** | **String**|  | 
 **versionId** | **String**|  | 
 **scope** | **String**|  | [optional] 
 **descriptorName** | **String**|  | [optional] 

### Return type

[**TitaniumDescriptorDefinitionResponse**](TitaniumDescriptorDefinitionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## dbDescriptorServiceListDbDescriptorVersions

> TitaniumListVersionResponse dbDescriptorServiceListDbDescriptorVersions(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.DbDescriptorServiceApi();
let body = new ClearconsensusSdk.TitaniumGetDefinition(); // TitaniumGetDefinition | 
apiInstance.dbDescriptorServiceListDbDescriptorVersions(body, (error, data, response) => {
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


## dbDescriptorServiceListDbDescriptors

> TitaniumDescriptorList dbDescriptorServiceListDbDescriptors(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.DbDescriptorServiceApi();
let body = new ClearconsensusSdk.TitaniumListRequest(); // TitaniumListRequest | 
apiInstance.dbDescriptorServiceListDbDescriptors(body, (error, data, response) => {
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

[**TitaniumDescriptorList**](TitaniumDescriptorList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

