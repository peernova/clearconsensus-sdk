# openapi_client.KVServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**k_v_service_add_key**](KVServiceApi.md#k_v_service_add_key) | **POST** /api/v1/kv/add | 
[**k_v_service_delete_key**](KVServiceApi.md#k_v_service_delete_key) | **POST** /api/v1/kv/delete | 
[**k_v_service_get_key**](KVServiceApi.md#k_v_service_get_key) | **POST** /api/v1/kv/get | 
[**k_v_service_list_keys**](KVServiceApi.md#k_v_service_list_keys) | **POST** /api/v1/kv/list | 
[**k_v_service_update_key**](KVServiceApi.md#k_v_service_update_key) | **POST** /api/v1/kv/update | 


# **k_v_service_add_key**
> TitaniumKVOperationResponse k_v_service_add_key(body)



### Example


```python
import time
import openapi_client
from openapi_client.api import kv_service_api
from openapi_client.model.titanium_kv_asset import TitaniumKVAsset
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_kv_operation_response import TitaniumKVOperationResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = kv_service_api.KVServiceApi(api_client)
    body = TitaniumKVAsset(
        key="key_example",
        ttl="ttl_example",
        ttl_date="ttl_date_example",
        ttl_from="ttl_from_example",
        value={},
    ) # TitaniumKVAsset | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.k_v_service_add_key(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KVServiceApi->k_v_service_add_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumKVAsset**](TitaniumKVAsset.md)|  |

### Return type

[**TitaniumKVOperationResponse**](TitaniumKVOperationResponse.md)

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

# **k_v_service_delete_key**
> TitaniumKVOperationResponse k_v_service_delete_key(body)



### Example


```python
import time
import openapi_client
from openapi_client.api import kv_service_api
from openapi_client.model.titanium_kv_request import TitaniumKVRequest
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_kv_operation_response import TitaniumKVOperationResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = kv_service_api.KVServiceApi(api_client)
    body = TitaniumKVRequest(
        key="key_example",
    ) # TitaniumKVRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.k_v_service_delete_key(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KVServiceApi->k_v_service_delete_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumKVRequest**](TitaniumKVRequest.md)|  |

### Return type

[**TitaniumKVOperationResponse**](TitaniumKVOperationResponse.md)

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

# **k_v_service_get_key**
> TitaniumGetKVResponse k_v_service_get_key(body)



### Example


```python
import time
import openapi_client
from openapi_client.api import kv_service_api
from openapi_client.model.titanium_kv_request import TitaniumKVRequest
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_get_kv_response import TitaniumGetKVResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = kv_service_api.KVServiceApi(api_client)
    body = TitaniumKVRequest(
        key="key_example",
    ) # TitaniumKVRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.k_v_service_get_key(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KVServiceApi->k_v_service_get_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumKVRequest**](TitaniumKVRequest.md)|  |

### Return type

[**TitaniumGetKVResponse**](TitaniumGetKVResponse.md)

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

# **k_v_service_list_keys**
> TitaniumListKVResponse k_v_service_list_keys(body)



### Example


```python
import time
import openapi_client
from openapi_client.api import kv_service_api
from openapi_client.model.titanium_list_kv_request import TitaniumListKVRequest
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_list_kv_response import TitaniumListKVResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = kv_service_api.KVServiceApi(api_client)
    body = TitaniumListKVRequest(
        filter="filter_example",
    ) # TitaniumListKVRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.k_v_service_list_keys(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KVServiceApi->k_v_service_list_keys: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumListKVRequest**](TitaniumListKVRequest.md)|  |

### Return type

[**TitaniumListKVResponse**](TitaniumListKVResponse.md)

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

# **k_v_service_update_key**
> TitaniumKVOperationResponse k_v_service_update_key(body)



### Example


```python
import time
import openapi_client
from openapi_client.api import kv_service_api
from openapi_client.model.titanium_kv_asset import TitaniumKVAsset
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_kv_operation_response import TitaniumKVOperationResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = kv_service_api.KVServiceApi(api_client)
    body = TitaniumKVAsset(
        key="key_example",
        ttl="ttl_example",
        ttl_date="ttl_date_example",
        ttl_from="ttl_from_example",
        value={},
    ) # TitaniumKVAsset | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.k_v_service_update_key(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling KVServiceApi->k_v_service_update_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumKVAsset**](TitaniumKVAsset.md)|  |

### Return type

[**TitaniumKVOperationResponse**](TitaniumKVOperationResponse.md)

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

