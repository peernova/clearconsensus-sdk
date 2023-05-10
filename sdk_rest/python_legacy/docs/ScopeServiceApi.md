# openapi_client.ScopeServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**scope_service_add_scope**](ScopeServiceApi.md#scope_service_add_scope) | **POST** /api/v1/scope/add | AddScope creates scope in the system.
[**scope_service_exist_scope**](ScopeServiceApi.md#scope_service_exist_scope) | **POST** /api/v1/scope/exist | ExistScope return boolean value about existence of scope according to request.
[**scope_service_list_scope**](ScopeServiceApi.md#scope_service_list_scope) | **POST** /api/v1/scope/list | ListScope returns list of all existing scopes.


# **scope_service_add_scope**
> TitaniumAcknowledgeResponse scope_service_add_scope(body)

AddScope creates scope in the system.

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
    api_instance = openapi_client.ScopeServiceApi(api_client)
    body = openapi_client.TitaniumScopeIdentifier() # TitaniumScopeIdentifier | 

    try:
        # AddScope creates scope in the system.
        api_response = api_instance.scope_service_add_scope(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ScopeServiceApi->scope_service_add_scope: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumScopeIdentifier**](TitaniumScopeIdentifier.md)|  | 

### Return type

[**TitaniumAcknowledgeResponse**](TitaniumAcknowledgeResponse.md)

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

# **scope_service_exist_scope**
> TitaniumScopeExistResponse scope_service_exist_scope(body)

ExistScope return boolean value about existence of scope according to request.

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
    api_instance = openapi_client.ScopeServiceApi(api_client)
    body = openapi_client.TitaniumScopeIdentifier() # TitaniumScopeIdentifier | 

    try:
        # ExistScope return boolean value about existence of scope according to request.
        api_response = api_instance.scope_service_exist_scope(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ScopeServiceApi->scope_service_exist_scope: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumScopeIdentifier**](TitaniumScopeIdentifier.md)|  | 

### Return type

[**TitaniumScopeExistResponse**](TitaniumScopeExistResponse.md)

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

# **scope_service_list_scope**
> TitaniumScopeListResponse scope_service_list_scope(body)

ListScope returns list of all existing scopes.

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
    api_instance = openapi_client.ScopeServiceApi(api_client)
    body = None # object | 

    try:
        # ListScope returns list of all existing scopes.
        api_response = api_instance.scope_service_list_scope(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ScopeServiceApi->scope_service_list_scope: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**|  | 

### Return type

[**TitaniumScopeListResponse**](TitaniumScopeListResponse.md)

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

