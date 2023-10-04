# ClearconsensusSdk.UniqueKeyServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**uniqueKeyServiceAddUniqueKey**](UniqueKeyServiceApi.md#uniqueKeyServiceAddUniqueKey) | **POST** /api/v1/uniquekey/add | AddUniqueKey is used to add a new unique key definition to the system.
[**uniqueKeyServiceDisableUniqueKey**](UniqueKeyServiceApi.md#uniqueKeyServiceDisableUniqueKey) | **POST** /api/v1/uniquekey/disable | 
[**uniqueKeyServiceEnableUniqueKey**](UniqueKeyServiceApi.md#uniqueKeyServiceEnableUniqueKey) | **POST** /api/v1/uniquekey/enable | 
[**uniqueKeyServiceGetUniqueKey**](UniqueKeyServiceApi.md#uniqueKeyServiceGetUniqueKey) | **POST** /api/v1/uniquekey/get | GetUniqueKey is used to retrieve a unique key definition by its scope and name. Request: {   \&quot;identifier\&quot;:{      \&quot;name\&quot;:\&quot;foreign_exchange-vanilla-forwards\&quot;   },   \&quot;scope\&quot;:\&quot;global\&quot; }
[**uniqueKeyServiceGetUniqueKeyVersion**](UniqueKeyServiceApi.md#uniqueKeyServiceGetUniqueKeyVersion) | **GET** /api/v1/uniquekey/version/{scope}/{name}/{versionId} | GetUniqueKeyVersion is used to retrieve a specific version of a unique key definition by its scope, name, and version ID. Response: {    \&quot;data\&quot;: {        \&quot;name\&quot;: \&quot;foreign_exchange-vanilla-forwards\&quot;,        \&quot;scope\&quot;: \&quot;global\&quot;,        \&quot;uniqueKey\&quot;: [            \&quot;asset\&quot;,            \&quot;service\&quot;,            \&quot;sub-asset\&quot;,            \&quot;instrument_type\&quot;,            \&quot;tenor\&quot;,            \&quot;snap_date\&quot;,            \&quot;snap_time\&quot;,            \&quot;curr_1\&quot;,            \&quot;curr_2\&quot;,            \&quot;onshore_offshore_curr_1\&quot;,            \&quot;onshore_offshore_curr_2\&quot;        ],        \&quot;orderBy\&quot;: [            \&quot;__input_row_num\&quot;        ],        \&quot;order\&quot;: \&quot;ASC\&quot;    } }
[**uniqueKeyServiceListUniqueKeyVersions**](UniqueKeyServiceApi.md#uniqueKeyServiceListUniqueKeyVersions) | **POST** /api/v1/uniquekey/versions | ListUniqueKeyVersions is used to retrieve a list of all versions of a specific unique key definition by its scope and name. Request: {   \&quot;scope\&quot;:\&quot;global\&quot;,   \&quot;identifier\&quot;: {        \&quot;name\&quot;: \&quot;foreign_exchange-vanilla-forwards\&quot;    } }
[**uniqueKeyServiceListUniqueKeys**](UniqueKeyServiceApi.md#uniqueKeyServiceListUniqueKeys) | **POST** /api/v1/uniquekey/list | ListUniqueKeys is used to retrieve a list of all unique key definitions in the system. Request: {   \&quot;scope\&quot;:\&quot;global\&quot; }



## uniqueKeyServiceAddUniqueKey

> TitaniumAcknowledgeResponse uniqueKeyServiceAddUniqueKey(body)

AddUniqueKey is used to add a new unique key definition to the system.

Example of request : {   \&quot;name\&quot;:\&quot;foreign_exchange-vanilla-forwards\&quot;,   \&quot;scope\&quot;:\&quot;global\&quot;,   \&quot;uniqueKey\&quot;:[      \&quot;snap_date\&quot;,      \&quot;asset\&quot;,      \&quot;service\&quot;,      \&quot;client\&quot;,      \&quot;service\&quot;,      \&quot;tenor\&quot;,      \&quot;snap_time\&quot;,      \&quot;instrument_type\&quot;,      \&quot;spot_reference_price\&quot;,      \&quot;mid_fwrd_outright\&quot;,      \&quot;mid_fwrd_points\&quot;,      \&quot;onshore_offshore_curr_1\&quot;,      \&quot;onshore_offshore_curr_2\&quot;   ] }

### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.UniqueKeyServiceApi();
let body = new ClearconsensusSdk.TitaniumUniqueKeyDefinition(); // TitaniumUniqueKeyDefinition | 
apiInstance.uniqueKeyServiceAddUniqueKey(body, (error, data, response) => {
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
 **body** | [**TitaniumUniqueKeyDefinition**](TitaniumUniqueKeyDefinition.md)|  | 

### Return type

[**TitaniumAcknowledgeResponse**](TitaniumAcknowledgeResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## uniqueKeyServiceDisableUniqueKey

> TitaniumAcknowledgeResponse uniqueKeyServiceDisableUniqueKey(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.UniqueKeyServiceApi();
let body = new ClearconsensusSdk.TitaniumEnableDisableRequest(); // TitaniumEnableDisableRequest | 
apiInstance.uniqueKeyServiceDisableUniqueKey(body, (error, data, response) => {
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


## uniqueKeyServiceEnableUniqueKey

> TitaniumAcknowledgeResponse uniqueKeyServiceEnableUniqueKey(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.UniqueKeyServiceApi();
let body = new ClearconsensusSdk.TitaniumEnableDisableRequest(); // TitaniumEnableDisableRequest | 
apiInstance.uniqueKeyServiceEnableUniqueKey(body, (error, data, response) => {
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


## uniqueKeyServiceGetUniqueKey

> TitaniumUniqueKeyDefinitionResponse uniqueKeyServiceGetUniqueKey(body)

GetUniqueKey is used to retrieve a unique key definition by its scope and name. Request: {   \&quot;identifier\&quot;:{      \&quot;name\&quot;:\&quot;foreign_exchange-vanilla-forwards\&quot;   },   \&quot;scope\&quot;:\&quot;global\&quot; }

Response: {    \&quot;data\&quot;: {        \&quot;name\&quot;: \&quot;foreign_exchange-vanilla-forwards\&quot;,        \&quot;scope\&quot;: \&quot;global\&quot;,        \&quot;uniqueKey\&quot;: [            \&quot;snap_date\&quot;,            \&quot;asset\&quot;,            \&quot;service\&quot;,            \&quot;client\&quot;,            \&quot;service\&quot;,            \&quot;tenor\&quot;,            \&quot;snap_time\&quot;,            \&quot;instrument_type\&quot;,            \&quot;spot_reference_price\&quot;,            \&quot;mid_fwrd_outright\&quot;,            \&quot;mid_fwrd_points\&quot;,            \&quot;onshore_offshore_curr_1\&quot;,            \&quot;onshore_offshore_curr_2\&quot;        ],        \&quot;orderBy\&quot;: [            \&quot;__input_row_num\&quot;        ],        \&quot;order\&quot;: \&quot;ASC\&quot;    } }

### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.UniqueKeyServiceApi();
let body = new ClearconsensusSdk.TitaniumGetDefinition(); // TitaniumGetDefinition | 
apiInstance.uniqueKeyServiceGetUniqueKey(body, (error, data, response) => {
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

[**TitaniumUniqueKeyDefinitionResponse**](TitaniumUniqueKeyDefinitionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## uniqueKeyServiceGetUniqueKeyVersion

> TitaniumUniqueKeyDefinitionResponse uniqueKeyServiceGetUniqueKeyVersion(scope, name, versionId, opts)

GetUniqueKeyVersion is used to retrieve a specific version of a unique key definition by its scope, name, and version ID. Response: {    \&quot;data\&quot;: {        \&quot;name\&quot;: \&quot;foreign_exchange-vanilla-forwards\&quot;,        \&quot;scope\&quot;: \&quot;global\&quot;,        \&quot;uniqueKey\&quot;: [            \&quot;asset\&quot;,            \&quot;service\&quot;,            \&quot;sub-asset\&quot;,            \&quot;instrument_type\&quot;,            \&quot;tenor\&quot;,            \&quot;snap_date\&quot;,            \&quot;snap_time\&quot;,            \&quot;curr_1\&quot;,            \&quot;curr_2\&quot;,            \&quot;onshore_offshore_curr_1\&quot;,            \&quot;onshore_offshore_curr_2\&quot;        ],        \&quot;orderBy\&quot;: [            \&quot;__input_row_num\&quot;        ],        \&quot;order\&quot;: \&quot;ASC\&quot;    } }

### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.UniqueKeyServiceApi();
let scope = "scope_example"; // String | 
let name = "name_example"; // String | 
let versionId = "versionId_example"; // String | 
let opts = {
  'descriptorName': "descriptorName_example" // String | 
};
apiInstance.uniqueKeyServiceGetUniqueKeyVersion(scope, name, versionId, opts, (error, data, response) => {
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
 **scope** | **String**|  | 
 **name** | **String**|  | 
 **versionId** | **String**|  | 
 **descriptorName** | **String**|  | [optional] 

### Return type

[**TitaniumUniqueKeyDefinitionResponse**](TitaniumUniqueKeyDefinitionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## uniqueKeyServiceListUniqueKeyVersions

> TitaniumListVersionResponse uniqueKeyServiceListUniqueKeyVersions(body)

ListUniqueKeyVersions is used to retrieve a list of all versions of a specific unique key definition by its scope and name. Request: {   \&quot;scope\&quot;:\&quot;global\&quot;,   \&quot;identifier\&quot;: {        \&quot;name\&quot;: \&quot;foreign_exchange-vanilla-forwards\&quot;    } }

Response: {    \&quot;data\&quot;: {        \&quot;versions\&quot;: [            {                \&quot;versionId\&quot;:\&quot;0bmhRR-7hISwkb_H2MvIqafpJCAoy3YgEySZjntZF9o&#x3D;\&quot;,                \&quot;createdAt\&quot;: \&quot;2022-08-22 15:23:44.0\&quot;            }        ]    } }

### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.UniqueKeyServiceApi();
let body = new ClearconsensusSdk.TitaniumGetDefinition(); // TitaniumGetDefinition | 
apiInstance.uniqueKeyServiceListUniqueKeyVersions(body, (error, data, response) => {
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


## uniqueKeyServiceListUniqueKeys

> TitaniumListUniqueKeysResponse uniqueKeyServiceListUniqueKeys(body)

ListUniqueKeys is used to retrieve a list of all unique key definitions in the system. Request: {   \&quot;scope\&quot;:\&quot;global\&quot; }

Response: {    \&quot;data\&quot;: {        \&quot;results\&quot;: [            {                \&quot;name\&quot;: \&quot;foreign_exchange-vanilla-forwards\&quot;,                \&quot;scope\&quot;: \&quot;global\&quot;,                \&quot;uniqueKey\&quot;: [                    \&quot;asset\&quot;,                    \&quot;service\&quot;,                    \&quot;sub-asset\&quot;,                    \&quot;instrument_type\&quot;,                    \&quot;tenor\&quot;,                    \&quot;snap_date\&quot;,                    \&quot;snap_time\&quot;,                    \&quot;curr_1\&quot;,                    \&quot;curr_2\&quot;,                    \&quot;onshore_offshore_curr_1\&quot;,                    \&quot;onshore_offshore_curr_2\&quot;                ],                \&quot;orderBy\&quot;: [                    \&quot;__input_row_num\&quot;                ],                \&quot;order\&quot;: \&quot;ASC\&quot;            },            {                \&quot;name\&quot;: \&quot;foreign_exchange-vanilla-options\&quot;,                \&quot;scope\&quot;: \&quot;global\&quot;,                \&quot;uniqueKey\&quot;: [                    \&quot;snap_date\&quot;,                    \&quot;asset\&quot;,                    \&quot;service\&quot;,                    \&quot;snap_time\&quot;,                    \&quot;instrument_type\&quot;,                    \&quot;option_instrument_parameter\&quot;,                    \&quot;exercise_style\&quot;,                    \&quot;option_execution_cut_time\&quot;,                    \&quot;curr_1\&quot;,                    \&quot;curr_2\&quot;,                    \&quot;tenor\&quot;,                    \&quot;delta\&quot;,                    \&quot;vol_format\&quot;,                    \&quot;instrument_convention\&quot;,                    \&quot;delta_convention\&quot;,                    \&quot;premium_currency\&quot;,                    \&quot;settlement_convention\&quot;                ],                \&quot;orderBy\&quot;: [                    \&quot;__input_row_num\&quot;                ],                \&quot;order\&quot;: \&quot;ASC\&quot;            }        ]    } }

### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.UniqueKeyServiceApi();
let body = new ClearconsensusSdk.TitaniumListRequest(); // TitaniumListRequest | 
apiInstance.uniqueKeyServiceListUniqueKeys(body, (error, data, response) => {
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

[**TitaniumListUniqueKeysResponse**](TitaniumListUniqueKeysResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

