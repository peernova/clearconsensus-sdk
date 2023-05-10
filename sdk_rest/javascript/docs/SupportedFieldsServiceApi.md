# ClearconsensusSdk.SupportedFieldsServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**supportedFieldsServiceGetSupportedFieldsValues**](SupportedFieldsServiceApi.md#supportedFieldsServiceGetSupportedFieldsValues) | **POST** /api/v1/list/field-values | 
[**supportedFieldsServiceListSupportedFields**](SupportedFieldsServiceApi.md#supportedFieldsServiceListSupportedFields) | **POST** /api/v1/list/fields | 



## supportedFieldsServiceGetSupportedFieldsValues

> TitaniumGetFieldValuesResponse supportedFieldsServiceGetSupportedFieldsValues(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.SupportedFieldsServiceApi();
let body = new ClearconsensusSdk.TitaniumSupportedField(); // TitaniumSupportedField | 
apiInstance.supportedFieldsServiceGetSupportedFieldsValues(body, (error, data, response) => {
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
 **body** | [**TitaniumSupportedField**](TitaniumSupportedField.md)|  | 

### Return type

[**TitaniumGetFieldValuesResponse**](TitaniumGetFieldValuesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## supportedFieldsServiceListSupportedFields

> TitaniumGetSupportedFieldsResponse supportedFieldsServiceListSupportedFields(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.SupportedFieldsServiceApi();
let body = new ClearconsensusSdk.TitaniumGetSupportedFields(); // TitaniumGetSupportedFields | 
apiInstance.supportedFieldsServiceListSupportedFields(body, (error, data, response) => {
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
 **body** | [**TitaniumGetSupportedFields**](TitaniumGetSupportedFields.md)|  | 

### Return type

[**TitaniumGetSupportedFieldsResponse**](TitaniumGetSupportedFieldsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

