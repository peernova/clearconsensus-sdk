# openapi_client.PolicyServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**policy_service_check_policy**](PolicyServiceApi.md#policy_service_check_policy) | **POST** /api/v1/user-management/policies/checkPolicy | 
[**policy_service_create**](PolicyServiceApi.md#policy_service_create) | **POST** /api/v1/user-management/policies/create | 
[**policy_service_get_addons**](PolicyServiceApi.md#policy_service_get_addons) | **POST** /api/v1/user-management/policies/getAddons | 
[**policy_service_get_apis**](PolicyServiceApi.md#policy_service_get_apis) | **POST** /api/v1/user-management/policies/getApis | 
[**policy_service_get_assets**](PolicyServiceApi.md#policy_service_get_assets) | **POST** /api/v1/user-management/policies/getAssets | 
[**policy_service_get_policies**](PolicyServiceApi.md#policy_service_get_policies) | **POST** /api/v1/user-management/policies/getPolicies | 
[**policy_service_remove_policy**](PolicyServiceApi.md#policy_service_remove_policy) | **POST** /api/v1/user-management/policies/removePolicy | 


# **policy_service_check_policy**
> ProtoServiceResponse policy_service_check_policy(body)



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
    api_instance = openapi_client.PolicyServiceApi(api_client)
    body = openapi_client.ProtoPolicyDto() # ProtoPolicyDto | 

    try:
        api_response = api_instance.policy_service_check_policy(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PolicyServiceApi->policy_service_check_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProtoPolicyDto**](ProtoPolicyDto.md)|  | 

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
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **policy_service_create**
> ProtoServiceResponse policy_service_create(body)



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
    api_instance = openapi_client.PolicyServiceApi(api_client)
    body = openapi_client.ProtoPolicies() # ProtoPolicies | 

    try:
        api_response = api_instance.policy_service_create(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PolicyServiceApi->policy_service_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProtoPolicies**](ProtoPolicies.md)|  | 

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
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **policy_service_get_addons**
> ProtoServiceResponse policy_service_get_addons(body)



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
    api_instance = openapi_client.PolicyServiceApi(api_client)
    body = openapi_client.ProtoUsernamePermissionRequest() # ProtoUsernamePermissionRequest | 

    try:
        api_response = api_instance.policy_service_get_addons(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PolicyServiceApi->policy_service_get_addons: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProtoUsernamePermissionRequest**](ProtoUsernamePermissionRequest.md)|  | 

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
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **policy_service_get_apis**
> ProtoServiceResponse policy_service_get_apis(body)



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
    api_instance = openapi_client.PolicyServiceApi(api_client)
    body = openapi_client.ProtoUsernamePermissionRequest() # ProtoUsernamePermissionRequest | 

    try:
        api_response = api_instance.policy_service_get_apis(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PolicyServiceApi->policy_service_get_apis: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProtoUsernamePermissionRequest**](ProtoUsernamePermissionRequest.md)|  | 

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
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **policy_service_get_assets**
> ProtoServiceResponse policy_service_get_assets(body)



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
    api_instance = openapi_client.PolicyServiceApi(api_client)
    body = openapi_client.ProtoUsernamePermissionRequest() # ProtoUsernamePermissionRequest | 

    try:
        api_response = api_instance.policy_service_get_assets(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PolicyServiceApi->policy_service_get_assets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProtoUsernamePermissionRequest**](ProtoUsernamePermissionRequest.md)|  | 

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
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **policy_service_get_policies**
> ProtoServiceResponse policy_service_get_policies(body)



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
    api_instance = openapi_client.PolicyServiceApi(api_client)
    body = openapi_client.ProtoPolicyType() # ProtoPolicyType | 

    try:
        api_response = api_instance.policy_service_get_policies(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PolicyServiceApi->policy_service_get_policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProtoPolicyType**](ProtoPolicyType.md)|  | 

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
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **policy_service_remove_policy**
> ProtoServiceResponse policy_service_remove_policy(body)



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
    api_instance = openapi_client.PolicyServiceApi(api_client)
    body = openapi_client.ProtoPolicyDto() # ProtoPolicyDto | 

    try:
        api_response = api_instance.policy_service_remove_policy(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PolicyServiceApi->policy_service_remove_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProtoPolicyDto**](ProtoPolicyDto.md)|  | 

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
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

