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
> ProtoOperationSuccess policy_service_check_policy(body)



### Example


```python
import time
import openapi_client
from openapi_client.api import policy_service_api
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.proto_operation_success import ProtoOperationSuccess
from openapi_client.model.proto_policy_dto import ProtoPolicyDto
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = policy_service_api.PolicyServiceApi(api_client)
    body = ProtoPolicyDto(
        addon="addon_example",
        api="api_example",
        api_permission="api_permission_example",
        asset="asset_example",
        asset_permission="asset_permission_example",
        type="type_example",
        username="username_example",
    ) # ProtoPolicyDto | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.policy_service_check_policy(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PolicyServiceApi->policy_service_check_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProtoPolicyDto**](ProtoPolicyDto.md)|  |

### Return type

[**ProtoOperationSuccess**](ProtoOperationSuccess.md)

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
> ProtoOperationSuccess policy_service_create(body)



### Example


```python
import time
import openapi_client
from openapi_client.api import policy_service_api
from openapi_client.model.proto_policies import ProtoPolicies
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.proto_operation_success import ProtoOperationSuccess
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = policy_service_api.PolicyServiceApi(api_client)
    body = ProtoPolicies(
        policy_dto=[
            ProtoPolicyDto(
                addon="addon_example",
                api="api_example",
                api_permission="api_permission_example",
                asset="asset_example",
                asset_permission="asset_permission_example",
                type="type_example",
                username="username_example",
            ),
        ],
    ) # ProtoPolicies | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.policy_service_create(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PolicyServiceApi->policy_service_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProtoPolicies**](ProtoPolicies.md)|  |

### Return type

[**ProtoOperationSuccess**](ProtoOperationSuccess.md)

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
> ProtoPoliciesListResponse policy_service_get_addons(body)



### Example


```python
import time
import openapi_client
from openapi_client.api import policy_service_api
from openapi_client.model.proto_policies_list_response import ProtoPoliciesListResponse
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.proto_username_permission_request import ProtoUsernamePermissionRequest
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = policy_service_api.PolicyServiceApi(api_client)
    body = ProtoUsernamePermissionRequest(
        permission="permission_example",
        username="username_example",
    ) # ProtoUsernamePermissionRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.policy_service_get_addons(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PolicyServiceApi->policy_service_get_addons: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProtoUsernamePermissionRequest**](ProtoUsernamePermissionRequest.md)|  |

### Return type

[**ProtoPoliciesListResponse**](ProtoPoliciesListResponse.md)

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
> ProtoPoliciesListResponse policy_service_get_apis(body)



### Example


```python
import time
import openapi_client
from openapi_client.api import policy_service_api
from openapi_client.model.proto_policies_list_response import ProtoPoliciesListResponse
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.proto_username_permission_request import ProtoUsernamePermissionRequest
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = policy_service_api.PolicyServiceApi(api_client)
    body = ProtoUsernamePermissionRequest(
        permission="permission_example",
        username="username_example",
    ) # ProtoUsernamePermissionRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.policy_service_get_apis(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PolicyServiceApi->policy_service_get_apis: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProtoUsernamePermissionRequest**](ProtoUsernamePermissionRequest.md)|  |

### Return type

[**ProtoPoliciesListResponse**](ProtoPoliciesListResponse.md)

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
> ProtoPoliciesListResponse policy_service_get_assets(body)



### Example


```python
import time
import openapi_client
from openapi_client.api import policy_service_api
from openapi_client.model.proto_policies_list_response import ProtoPoliciesListResponse
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.proto_username_permission_request import ProtoUsernamePermissionRequest
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = policy_service_api.PolicyServiceApi(api_client)
    body = ProtoUsernamePermissionRequest(
        permission="permission_example",
        username="username_example",
    ) # ProtoUsernamePermissionRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.policy_service_get_assets(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PolicyServiceApi->policy_service_get_assets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProtoUsernamePermissionRequest**](ProtoUsernamePermissionRequest.md)|  |

### Return type

[**ProtoPoliciesListResponse**](ProtoPoliciesListResponse.md)

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
> ProtoPoliciesResponse policy_service_get_policies(body)



### Example


```python
import time
import openapi_client
from openapi_client.api import policy_service_api
from openapi_client.model.proto_policy_type import ProtoPolicyType
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.proto_policies_response import ProtoPoliciesResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = policy_service_api.PolicyServiceApi(api_client)
    body = ProtoPolicyType(
        type="type_example",
    ) # ProtoPolicyType | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.policy_service_get_policies(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PolicyServiceApi->policy_service_get_policies: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProtoPolicyType**](ProtoPolicyType.md)|  |

### Return type

[**ProtoPoliciesResponse**](ProtoPoliciesResponse.md)

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
> ProtoOperationSuccess policy_service_remove_policy(body)



### Example


```python
import time
import openapi_client
from openapi_client.api import policy_service_api
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.proto_operation_success import ProtoOperationSuccess
from openapi_client.model.proto_policy_dto import ProtoPolicyDto
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = policy_service_api.PolicyServiceApi(api_client)
    body = ProtoPolicyDto(
        addon="addon_example",
        api="api_example",
        api_permission="api_permission_example",
        asset="asset_example",
        asset_permission="asset_permission_example",
        type="type_example",
        username="username_example",
    ) # ProtoPolicyDto | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.policy_service_remove_policy(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PolicyServiceApi->policy_service_remove_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProtoPolicyDto**](ProtoPolicyDto.md)|  |

### Return type

[**ProtoOperationSuccess**](ProtoOperationSuccess.md)

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

