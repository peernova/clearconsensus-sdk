# UserServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**userServiceAddUser**](UserServiceApi.md#userServiceAddUser) | **POST** /api/v1/user/add |  |
| [**userServiceAddUserNotification**](UserServiceApi.md#userServiceAddUserNotification) | **POST** /api/v1/user/notifications/add |  |
| [**userServiceCreate**](UserServiceApi.md#userServiceCreate) | **POST** /api/v1/user-management/users/create |  |
| [**userServiceDeleteUser**](UserServiceApi.md#userServiceDeleteUser) | **POST** /api/v1/user/delete |  |
| [**userServiceDeleteUserNotification**](UserServiceApi.md#userServiceDeleteUserNotification) | **POST** /api/v1/user/notifications/delete |  |
| [**userServiceGetAll**](UserServiceApi.md#userServiceGetAll) | **POST** /api/v1/user-management/users/getAll |  |
| [**userServiceGetById**](UserServiceApi.md#userServiceGetById) | **POST** /api/v1/user-management/users/getById |  |
| [**userServiceGetUser**](UserServiceApi.md#userServiceGetUser) | **POST** /api/v1/user |  |
| [**userServiceGetUserNotifications**](UserServiceApi.md#userServiceGetUserNotifications) | **POST** /api/v1/user/notifications |  |
| [**userServiceGetUserNotificationsByMarket**](UserServiceApi.md#userServiceGetUserNotificationsByMarket) | **POST** /api/v1/user/notifications/market |  |
| [**userServiceGetUserPermissions**](UserServiceApi.md#userServiceGetUserPermissions) | **POST** /api/v1/user/permissions |  |
| [**userServiceUpdate**](UserServiceApi.md#userServiceUpdate) | **POST** /api/v1/user-management/users/update |  |
| [**userServiceUpdateUser**](UserServiceApi.md#userServiceUpdateUser) | **POST** /api/v1/user/update |  |
| [**userServiceUpdateUserNotification**](UserServiceApi.md#userServiceUpdateUserNotification) | **POST** /api/v1/user/notifications/update |  |


<a name="userServiceAddUser"></a>
# **userServiceAddUser**
> TitaniumUserResponse userServiceAddUser(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    UserServiceApi apiInstance = new UserServiceApi(defaultClient);
    TitaniumUserRequest body = new TitaniumUserRequest(); // TitaniumUserRequest | 
    try {
      TitaniumUserResponse result = apiInstance.userServiceAddUser(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserServiceApi#userServiceAddUser");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **body** | [**TitaniumUserRequest**](TitaniumUserRequest.md)|  | |

### Return type

[**TitaniumUserResponse**](TitaniumUserResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful response. |  -  |
| **0** | An unexpected error response. |  -  |

<a name="userServiceAddUserNotification"></a>
# **userServiceAddUserNotification**
> TitaniumUserNotificationResponse userServiceAddUserNotification(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    UserServiceApi apiInstance = new UserServiceApi(defaultClient);
    TitaniumUserNotificationRequest body = new TitaniumUserNotificationRequest(); // TitaniumUserNotificationRequest | 
    try {
      TitaniumUserNotificationResponse result = apiInstance.userServiceAddUserNotification(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserServiceApi#userServiceAddUserNotification");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **body** | [**TitaniumUserNotificationRequest**](TitaniumUserNotificationRequest.md)|  | |

### Return type

[**TitaniumUserNotificationResponse**](TitaniumUserNotificationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful response. |  -  |
| **0** | An unexpected error response. |  -  |

<a name="userServiceCreate"></a>
# **userServiceCreate**
> ProtoServiceResponse userServiceCreate(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    UserServiceApi apiInstance = new UserServiceApi(defaultClient);
    ProtoUserDto body = new ProtoUserDto(); // ProtoUserDto | 
    try {
      ProtoServiceResponse result = apiInstance.userServiceCreate(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserServiceApi#userServiceCreate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **body** | [**ProtoUserDto**](ProtoUserDto.md)|  | |

### Return type

[**ProtoServiceResponse**](ProtoServiceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful response. |  -  |
| **0** | An unexpected error response. |  -  |

<a name="userServiceDeleteUser"></a>
# **userServiceDeleteUser**
> TitaniumUserResponse userServiceDeleteUser(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    UserServiceApi apiInstance = new UserServiceApi(defaultClient);
    TitaniumUserRequest body = new TitaniumUserRequest(); // TitaniumUserRequest | 
    try {
      TitaniumUserResponse result = apiInstance.userServiceDeleteUser(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserServiceApi#userServiceDeleteUser");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **body** | [**TitaniumUserRequest**](TitaniumUserRequest.md)|  | |

### Return type

[**TitaniumUserResponse**](TitaniumUserResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful response. |  -  |
| **0** | An unexpected error response. |  -  |

<a name="userServiceDeleteUserNotification"></a>
# **userServiceDeleteUserNotification**
> TitaniumUserNotificationResponse userServiceDeleteUserNotification(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    UserServiceApi apiInstance = new UserServiceApi(defaultClient);
    TitaniumUserNotificationRequest body = new TitaniumUserNotificationRequest(); // TitaniumUserNotificationRequest | 
    try {
      TitaniumUserNotificationResponse result = apiInstance.userServiceDeleteUserNotification(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserServiceApi#userServiceDeleteUserNotification");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **body** | [**TitaniumUserNotificationRequest**](TitaniumUserNotificationRequest.md)|  | |

### Return type

[**TitaniumUserNotificationResponse**](TitaniumUserNotificationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful response. |  -  |
| **0** | An unexpected error response. |  -  |

<a name="userServiceGetAll"></a>
# **userServiceGetAll**
> ProtoServiceResponse userServiceGetAll(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    UserServiceApi apiInstance = new UserServiceApi(defaultClient);
    ProtoUserEnabled body = new ProtoUserEnabled(); // ProtoUserEnabled | 
    try {
      ProtoServiceResponse result = apiInstance.userServiceGetAll(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserServiceApi#userServiceGetAll");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **body** | [**ProtoUserEnabled**](ProtoUserEnabled.md)|  | |

### Return type

[**ProtoServiceResponse**](ProtoServiceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful response. |  -  |
| **0** | An unexpected error response. |  -  |

<a name="userServiceGetById"></a>
# **userServiceGetById**
> ProtoServiceResponse userServiceGetById(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    UserServiceApi apiInstance = new UserServiceApi(defaultClient);
    ProtoUserId body = new ProtoUserId(); // ProtoUserId | 
    try {
      ProtoServiceResponse result = apiInstance.userServiceGetById(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserServiceApi#userServiceGetById");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **body** | [**ProtoUserId**](ProtoUserId.md)|  | |

### Return type

[**ProtoServiceResponse**](ProtoServiceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful response. |  -  |
| **0** | An unexpected error response. |  -  |

<a name="userServiceGetUser"></a>
# **userServiceGetUser**
> TitaniumUserResponse userServiceGetUser(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    UserServiceApi apiInstance = new UserServiceApi(defaultClient);
    TitaniumGetUserRequest body = new TitaniumGetUserRequest(); // TitaniumGetUserRequest | 
    try {
      TitaniumUserResponse result = apiInstance.userServiceGetUser(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserServiceApi#userServiceGetUser");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **body** | [**TitaniumGetUserRequest**](TitaniumGetUserRequest.md)|  | |

### Return type

[**TitaniumUserResponse**](TitaniumUserResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful response. |  -  |
| **0** | An unexpected error response. |  -  |

<a name="userServiceGetUserNotifications"></a>
# **userServiceGetUserNotifications**
> TitaniumUserNotificationsResponse userServiceGetUserNotifications(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    UserServiceApi apiInstance = new UserServiceApi(defaultClient);
    TitaniumGetUserNotificationRequest body = new TitaniumGetUserNotificationRequest(); // TitaniumGetUserNotificationRequest | 
    try {
      TitaniumUserNotificationsResponse result = apiInstance.userServiceGetUserNotifications(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserServiceApi#userServiceGetUserNotifications");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **body** | [**TitaniumGetUserNotificationRequest**](TitaniumGetUserNotificationRequest.md)|  | |

### Return type

[**TitaniumUserNotificationsResponse**](TitaniumUserNotificationsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful response. |  -  |
| **0** | An unexpected error response. |  -  |

<a name="userServiceGetUserNotificationsByMarket"></a>
# **userServiceGetUserNotificationsByMarket**
> TitaniumUserNotificationsResponse userServiceGetUserNotificationsByMarket(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    UserServiceApi apiInstance = new UserServiceApi(defaultClient);
    TitaniumGetUserNotificationByMarketRequest body = new TitaniumGetUserNotificationByMarketRequest(); // TitaniumGetUserNotificationByMarketRequest | 
    try {
      TitaniumUserNotificationsResponse result = apiInstance.userServiceGetUserNotificationsByMarket(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserServiceApi#userServiceGetUserNotificationsByMarket");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **body** | [**TitaniumGetUserNotificationByMarketRequest**](TitaniumGetUserNotificationByMarketRequest.md)|  | |

### Return type

[**TitaniumUserNotificationsResponse**](TitaniumUserNotificationsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful response. |  -  |
| **0** | An unexpected error response. |  -  |

<a name="userServiceGetUserPermissions"></a>
# **userServiceGetUserPermissions**
> TitaniumUserPermissionsResponse userServiceGetUserPermissions(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    UserServiceApi apiInstance = new UserServiceApi(defaultClient);
    TitaniumGetUserPermissionsRequest body = new TitaniumGetUserPermissionsRequest(); // TitaniumGetUserPermissionsRequest | 
    try {
      TitaniumUserPermissionsResponse result = apiInstance.userServiceGetUserPermissions(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserServiceApi#userServiceGetUserPermissions");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **body** | [**TitaniumGetUserPermissionsRequest**](TitaniumGetUserPermissionsRequest.md)|  | |

### Return type

[**TitaniumUserPermissionsResponse**](TitaniumUserPermissionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful response. |  -  |
| **0** | An unexpected error response. |  -  |

<a name="userServiceUpdate"></a>
# **userServiceUpdate**
> ProtoServiceResponse userServiceUpdate(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    UserServiceApi apiInstance = new UserServiceApi(defaultClient);
    ProtoUserDto body = new ProtoUserDto(); // ProtoUserDto | 
    try {
      ProtoServiceResponse result = apiInstance.userServiceUpdate(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserServiceApi#userServiceUpdate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **body** | [**ProtoUserDto**](ProtoUserDto.md)|  | |

### Return type

[**ProtoServiceResponse**](ProtoServiceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful response. |  -  |
| **0** | An unexpected error response. |  -  |

<a name="userServiceUpdateUser"></a>
# **userServiceUpdateUser**
> TitaniumUserResponse userServiceUpdateUser(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    UserServiceApi apiInstance = new UserServiceApi(defaultClient);
    TitaniumUserRequest body = new TitaniumUserRequest(); // TitaniumUserRequest | 
    try {
      TitaniumUserResponse result = apiInstance.userServiceUpdateUser(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserServiceApi#userServiceUpdateUser");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **body** | [**TitaniumUserRequest**](TitaniumUserRequest.md)|  | |

### Return type

[**TitaniumUserResponse**](TitaniumUserResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful response. |  -  |
| **0** | An unexpected error response. |  -  |

<a name="userServiceUpdateUserNotification"></a>
# **userServiceUpdateUserNotification**
> TitaniumUserNotificationResponse userServiceUpdateUserNotification(body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api-dev.clearconsensus.io");

    UserServiceApi apiInstance = new UserServiceApi(defaultClient);
    TitaniumUserNotificationRequest body = new TitaniumUserNotificationRequest(); // TitaniumUserNotificationRequest | 
    try {
      TitaniumUserNotificationResponse result = apiInstance.userServiceUpdateUserNotification(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserServiceApi#userServiceUpdateUserNotification");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **body** | [**TitaniumUserNotificationRequest**](TitaniumUserNotificationRequest.md)|  | |

### Return type

[**TitaniumUserNotificationResponse**](TitaniumUserNotificationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful response. |  -  |
| **0** | An unexpected error response. |  -  |

