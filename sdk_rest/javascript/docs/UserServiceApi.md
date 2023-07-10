# ClearconsensusSdk.UserServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**userServiceAddUser**](UserServiceApi.md#userServiceAddUser) | **POST** /api/v1/user/add | 
[**userServiceAddUserNotification**](UserServiceApi.md#userServiceAddUserNotification) | **POST** /api/v1/user/notifications/add | 
[**userServiceCreate**](UserServiceApi.md#userServiceCreate) | **POST** /api/v1/user-management/users/create | 
[**userServiceDeleteUser**](UserServiceApi.md#userServiceDeleteUser) | **POST** /api/v1/user/delete | 
[**userServiceDeleteUserNotification**](UserServiceApi.md#userServiceDeleteUserNotification) | **POST** /api/v1/user/notifications/delete | 
[**userServiceGetAll**](UserServiceApi.md#userServiceGetAll) | **POST** /api/v1/user-management/users/getAll | 
[**userServiceGetById**](UserServiceApi.md#userServiceGetById) | **POST** /api/v1/user-management/users/getById | 
[**userServiceGetUser**](UserServiceApi.md#userServiceGetUser) | **POST** /api/v1/user | 
[**userServiceGetUserNotifications**](UserServiceApi.md#userServiceGetUserNotifications) | **POST** /api/v1/user/notifications | 
[**userServiceGetUserNotificationsByMarket**](UserServiceApi.md#userServiceGetUserNotificationsByMarket) | **POST** /api/v1/user/notifications/market | 
[**userServiceGetUserPermissions**](UserServiceApi.md#userServiceGetUserPermissions) | **POST** /api/v1/user/permissions | 
[**userServiceUpdate**](UserServiceApi.md#userServiceUpdate) | **POST** /api/v1/user-management/users/update | 
[**userServiceUpdateUser**](UserServiceApi.md#userServiceUpdateUser) | **POST** /api/v1/user/update | 
[**userServiceUpdateUserNotification**](UserServiceApi.md#userServiceUpdateUserNotification) | **POST** /api/v1/user/notifications/update | 



## userServiceAddUser

> TitaniumUserResponse userServiceAddUser(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.UserServiceApi();
let body = new ClearconsensusSdk.TitaniumUserRequest(); // TitaniumUserRequest | 
apiInstance.userServiceAddUser(body, (error, data, response) => {
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
 **body** | [**TitaniumUserRequest**](TitaniumUserRequest.md)|  | 

### Return type

[**TitaniumUserResponse**](TitaniumUserResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## userServiceAddUserNotification

> TitaniumUserNotificationResponse userServiceAddUserNotification(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.UserServiceApi();
let body = new ClearconsensusSdk.TitaniumUserNotificationRequest(); // TitaniumUserNotificationRequest | 
apiInstance.userServiceAddUserNotification(body, (error, data, response) => {
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
 **body** | [**TitaniumUserNotificationRequest**](TitaniumUserNotificationRequest.md)|  | 

### Return type

[**TitaniumUserNotificationResponse**](TitaniumUserNotificationResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## userServiceCreate

> ProtoServiceResponse userServiceCreate(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.UserServiceApi();
let body = new ClearconsensusSdk.ProtoUserDto(); // ProtoUserDto | 
apiInstance.userServiceCreate(body, (error, data, response) => {
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
 **body** | [**ProtoUserDto**](ProtoUserDto.md)|  | 

### Return type

[**ProtoServiceResponse**](ProtoServiceResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## userServiceDeleteUser

> TitaniumUserResponse userServiceDeleteUser(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.UserServiceApi();
let body = new ClearconsensusSdk.TitaniumUserRequest(); // TitaniumUserRequest | 
apiInstance.userServiceDeleteUser(body, (error, data, response) => {
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
 **body** | [**TitaniumUserRequest**](TitaniumUserRequest.md)|  | 

### Return type

[**TitaniumUserResponse**](TitaniumUserResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## userServiceDeleteUserNotification

> TitaniumUserNotificationResponse userServiceDeleteUserNotification(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.UserServiceApi();
let body = new ClearconsensusSdk.TitaniumUserNotificationRequest(); // TitaniumUserNotificationRequest | 
apiInstance.userServiceDeleteUserNotification(body, (error, data, response) => {
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
 **body** | [**TitaniumUserNotificationRequest**](TitaniumUserNotificationRequest.md)|  | 

### Return type

[**TitaniumUserNotificationResponse**](TitaniumUserNotificationResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## userServiceGetAll

> ProtoServiceResponse userServiceGetAll(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.UserServiceApi();
let body = true; // Boolean | 
apiInstance.userServiceGetAll(body, (error, data, response) => {
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


## userServiceGetById

> ProtoServiceResponse userServiceGetById(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.UserServiceApi();
let body = "body_example"; // String | 
apiInstance.userServiceGetById(body, (error, data, response) => {
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


## userServiceGetUser

> TitaniumUserResponse userServiceGetUser(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.UserServiceApi();
let body = new ClearconsensusSdk.TitaniumGetUserRequest(); // TitaniumGetUserRequest | 
apiInstance.userServiceGetUser(body, (error, data, response) => {
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
 **body** | [**TitaniumGetUserRequest**](TitaniumGetUserRequest.md)|  | 

### Return type

[**TitaniumUserResponse**](TitaniumUserResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## userServiceGetUserNotifications

> TitaniumUserNotificationsResponse userServiceGetUserNotifications(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.UserServiceApi();
let body = new ClearconsensusSdk.TitaniumGetUserNotificationRequest(); // TitaniumGetUserNotificationRequest | 
apiInstance.userServiceGetUserNotifications(body, (error, data, response) => {
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
 **body** | [**TitaniumGetUserNotificationRequest**](TitaniumGetUserNotificationRequest.md)|  | 

### Return type

[**TitaniumUserNotificationsResponse**](TitaniumUserNotificationsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## userServiceGetUserNotificationsByMarket

> TitaniumUserNotificationsResponse userServiceGetUserNotificationsByMarket(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.UserServiceApi();
let body = new ClearconsensusSdk.TitaniumGetUserNotificationByMarketRequest(); // TitaniumGetUserNotificationByMarketRequest | 
apiInstance.userServiceGetUserNotificationsByMarket(body, (error, data, response) => {
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
 **body** | [**TitaniumGetUserNotificationByMarketRequest**](TitaniumGetUserNotificationByMarketRequest.md)|  | 

### Return type

[**TitaniumUserNotificationsResponse**](TitaniumUserNotificationsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## userServiceGetUserPermissions

> TitaniumUserPermissionsResponse userServiceGetUserPermissions(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.UserServiceApi();
let body = new ClearconsensusSdk.TitaniumGetUserPermissionsRequest(); // TitaniumGetUserPermissionsRequest | 
apiInstance.userServiceGetUserPermissions(body, (error, data, response) => {
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
 **body** | [**TitaniumGetUserPermissionsRequest**](TitaniumGetUserPermissionsRequest.md)|  | 

### Return type

[**TitaniumUserPermissionsResponse**](TitaniumUserPermissionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## userServiceUpdate

> ProtoServiceResponse userServiceUpdate(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.UserServiceApi();
let body = new ClearconsensusSdk.ProtoUserDto(); // ProtoUserDto | 
apiInstance.userServiceUpdate(body, (error, data, response) => {
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
 **body** | [**ProtoUserDto**](ProtoUserDto.md)|  | 

### Return type

[**ProtoServiceResponse**](ProtoServiceResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## userServiceUpdateUser

> TitaniumUserResponse userServiceUpdateUser(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.UserServiceApi();
let body = new ClearconsensusSdk.TitaniumUserRequest(); // TitaniumUserRequest | 
apiInstance.userServiceUpdateUser(body, (error, data, response) => {
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
 **body** | [**TitaniumUserRequest**](TitaniumUserRequest.md)|  | 

### Return type

[**TitaniumUserResponse**](TitaniumUserResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## userServiceUpdateUserNotification

> TitaniumUserNotificationResponse userServiceUpdateUserNotification(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.UserServiceApi();
let body = new ClearconsensusSdk.TitaniumUserNotificationRequest(); // TitaniumUserNotificationRequest | 
apiInstance.userServiceUpdateUserNotification(body, (error, data, response) => {
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
 **body** | [**TitaniumUserNotificationRequest**](TitaniumUserNotificationRequest.md)|  | 

### Return type

[**TitaniumUserNotificationResponse**](TitaniumUserNotificationResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

