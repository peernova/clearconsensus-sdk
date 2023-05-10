# openapi_client.UserServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_service_add_user_notification**](UserServiceApi.md#user_service_add_user_notification) | **POST** /api/v1/user/notifications/add | 
[**user_service_delete_user_notification**](UserServiceApi.md#user_service_delete_user_notification) | **POST** /api/v1/user/notifications/delete | 
[**user_service_get_user**](UserServiceApi.md#user_service_get_user) | **POST** /api/v1/user | 
[**user_service_get_user_notifications**](UserServiceApi.md#user_service_get_user_notifications) | **POST** /api/v1/user/notifications | 
[**user_service_get_user_notifications_by_market**](UserServiceApi.md#user_service_get_user_notifications_by_market) | **POST** /api/v1/user/notifications/market | 
[**user_service_get_user_permissions**](UserServiceApi.md#user_service_get_user_permissions) | **POST** /api/v1/user/permissions | 
[**user_service_update_user_notification**](UserServiceApi.md#user_service_update_user_notification) | **POST** /api/v1/user/notifications/update | 


# **user_service_add_user_notification**
> TitaniumUserNotificationResponse user_service_add_user_notification(body)



### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.UserServiceApi(api_client)
    body = openapi_client.TitaniumUserNotificationRequest() # TitaniumUserNotificationRequest | 

    try:
        api_response = api_instance.user_service_add_user_notification(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserServiceApi->user_service_add_user_notification: %s\n" % e)
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_service_delete_user_notification**
> TitaniumUserNotificationResponse user_service_delete_user_notification(body)



### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.UserServiceApi(api_client)
    body = openapi_client.TitaniumUserNotificationRequest() # TitaniumUserNotificationRequest | 

    try:
        api_response = api_instance.user_service_delete_user_notification(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserServiceApi->user_service_delete_user_notification: %s\n" % e)
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_service_get_user**
> TitaniumUserResponse user_service_get_user(body)



### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.UserServiceApi(api_client)
    body = openapi_client.TitaniumGetUserRequest() # TitaniumGetUserRequest | 

    try:
        api_response = api_instance.user_service_get_user(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserServiceApi->user_service_get_user: %s\n" % e)
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_service_get_user_notifications**
> TitaniumUserNotificationsResponse user_service_get_user_notifications(body)



### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.UserServiceApi(api_client)
    body = openapi_client.TitaniumGetUserNotificationRequest() # TitaniumGetUserNotificationRequest | 

    try:
        api_response = api_instance.user_service_get_user_notifications(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserServiceApi->user_service_get_user_notifications: %s\n" % e)
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_service_get_user_notifications_by_market**
> TitaniumUserNotificationsResponse user_service_get_user_notifications_by_market(body)



### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.UserServiceApi(api_client)
    body = openapi_client.TitaniumGetUserNotificationByMarketRequest() # TitaniumGetUserNotificationByMarketRequest | 

    try:
        api_response = api_instance.user_service_get_user_notifications_by_market(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserServiceApi->user_service_get_user_notifications_by_market: %s\n" % e)
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_service_get_user_permissions**
> TitaniumUserPermissionsResponse user_service_get_user_permissions(body)



### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.UserServiceApi(api_client)
    body = openapi_client.TitaniumGetUserPermissionsRequest() # TitaniumGetUserPermissionsRequest | 

    try:
        api_response = api_instance.user_service_get_user_permissions(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserServiceApi->user_service_get_user_permissions: %s\n" % e)
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_service_update_user_notification**
> TitaniumUserNotificationResponse user_service_update_user_notification(body)



### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.UserServiceApi(api_client)
    body = openapi_client.TitaniumUserNotificationRequest() # TitaniumUserNotificationRequest | 

    try:
        api_response = api_instance.user_service_update_user_notification(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserServiceApi->user_service_update_user_notification: %s\n" % e)
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

