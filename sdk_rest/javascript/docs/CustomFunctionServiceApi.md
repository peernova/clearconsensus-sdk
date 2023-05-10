# ClearconsensusSdk.CustomFunctionServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customFunctionServiceAddCustomFunction**](CustomFunctionServiceApi.md#customFunctionServiceAddCustomFunction) | **POST** /api/v1/customfunction/add | AddCustomFunction allows the user to create a new custom function by sending a CustomFunction message. It returns an AcknowledgeResponse indicating whether the custom function was successfully added or not.
[**customFunctionServiceGetCustomFunction**](CustomFunctionServiceApi.md#customFunctionServiceGetCustomFunction) | **POST** /api/v1/customfunction/get | GetCustomFunction retrieves the definition of a specific custom function. The custom function is specified in the CustomFunctionGetDefinition message, which includes its ID and scope. The method returns a CustomFunctionDefinitionResponse that contains either the custom function definition or an error.
[**customFunctionServiceListCustomFunctionVersions**](CustomFunctionServiceApi.md#customFunctionServiceListCustomFunctionVersions) | **POST** /api/v1/customfunction/versions | ListCustomFunctionVersions lists all the versions of a specific custom function. The custom function is specified in the GetDefinition message, which includes its ID and scope. The method returns a ListVersionResponse that contains either a list of versions or an error.
[**customFunctionServiceListCustomFunctions**](CustomFunctionServiceApi.md#customFunctionServiceListCustomFunctions) | **POST** /api/v1/customfunction/list | ListCustomFunctions lists all the custom functions that match the specified criteria. The criteria are defined in the ListCustomFunctionRequest message, which includes the descriptor name and the type of the custom function descriptor. The method returns a ListCustomFunctionResponse that contains either a list of custom functions or an error.



## customFunctionServiceAddCustomFunction

> TitaniumAcknowledgeResponse customFunctionServiceAddCustomFunction(body)

AddCustomFunction allows the user to create a new custom function by sending a CustomFunction message. It returns an AcknowledgeResponse indicating whether the custom function was successfully added or not.

### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.CustomFunctionServiceApi();
let body = new ClearconsensusSdk.TitaniumCustomFunction(); // TitaniumCustomFunction | 
apiInstance.customFunctionServiceAddCustomFunction(body, (error, data, response) => {
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
 **body** | [**TitaniumCustomFunction**](TitaniumCustomFunction.md)|  | 

### Return type

[**TitaniumAcknowledgeResponse**](TitaniumAcknowledgeResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## customFunctionServiceGetCustomFunction

> TitaniumCustomFunctionDefinitionResponse customFunctionServiceGetCustomFunction(body)

GetCustomFunction retrieves the definition of a specific custom function. The custom function is specified in the CustomFunctionGetDefinition message, which includes its ID and scope. The method returns a CustomFunctionDefinitionResponse that contains either the custom function definition or an error.

### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.CustomFunctionServiceApi();
let body = new ClearconsensusSdk.TitaniumCustomFunctionGetDefinition(); // TitaniumCustomFunctionGetDefinition | 
apiInstance.customFunctionServiceGetCustomFunction(body, (error, data, response) => {
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
 **body** | [**TitaniumCustomFunctionGetDefinition**](TitaniumCustomFunctionGetDefinition.md)|  | 

### Return type

[**TitaniumCustomFunctionDefinitionResponse**](TitaniumCustomFunctionDefinitionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## customFunctionServiceListCustomFunctionVersions

> TitaniumListVersionResponse customFunctionServiceListCustomFunctionVersions(body)

ListCustomFunctionVersions lists all the versions of a specific custom function. The custom function is specified in the GetDefinition message, which includes its ID and scope. The method returns a ListVersionResponse that contains either a list of versions or an error.

### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.CustomFunctionServiceApi();
let body = new ClearconsensusSdk.TitaniumGetDefinition(); // TitaniumGetDefinition | 
apiInstance.customFunctionServiceListCustomFunctionVersions(body, (error, data, response) => {
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


## customFunctionServiceListCustomFunctions

> TitaniumListCustomFunctionResponse customFunctionServiceListCustomFunctions(body)

ListCustomFunctions lists all the custom functions that match the specified criteria. The criteria are defined in the ListCustomFunctionRequest message, which includes the descriptor name and the type of the custom function descriptor. The method returns a ListCustomFunctionResponse that contains either a list of custom functions or an error.

### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.CustomFunctionServiceApi();
let body = new ClearconsensusSdk.TitaniumListCustomFunctionRequest(); // TitaniumListCustomFunctionRequest | 
apiInstance.customFunctionServiceListCustomFunctions(body, (error, data, response) => {
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
 **body** | [**TitaniumListCustomFunctionRequest**](TitaniumListCustomFunctionRequest.md)|  | 

### Return type

[**TitaniumListCustomFunctionResponse**](TitaniumListCustomFunctionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

