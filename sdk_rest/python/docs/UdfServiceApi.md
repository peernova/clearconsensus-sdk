# openapi_client.UdfServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**udf_service_disable_udf**](UdfServiceApi.md#udf_service_disable_udf) | **POST** /api/v1/udf/disable | 
[**udf_service_get_udf_definition**](UdfServiceApi.md#udf_service_get_udf_definition) | **GET** /api/v1/udf/{name} | 
[**udf_service_list_udfs**](UdfServiceApi.md#udf_service_list_udfs) | **POST** /api/v1/udf/list | 


# **udf_service_disable_udf**
> TitaniumMessageResponse udf_service_disable_udf(body)



### Example


```python
import time
import openapi_client
from openapi_client.api import udf_service_api
from openapi_client.model.titanium_message_response import TitaniumMessageResponse
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_udf_name_request import TitaniumUdfNameRequest
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = udf_service_api.UdfServiceApi(api_client)
    body = TitaniumUdfNameRequest(
        name="name_example",
        scope="scope_example",
    ) # TitaniumUdfNameRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.udf_service_disable_udf(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UdfServiceApi->udf_service_disable_udf: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumUdfNameRequest**](TitaniumUdfNameRequest.md)|  |

### Return type

[**TitaniumMessageResponse**](TitaniumMessageResponse.md)

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

# **udf_service_get_udf_definition**
> TitaniumGetUdfResponse udf_service_get_udf_definition(name)



### Example


```python
import time
import openapi_client
from openapi_client.api import udf_service_api
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_get_udf_response import TitaniumGetUdfResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = udf_service_api.UdfServiceApi(api_client)
    name = "name_example" # str | 
    scope = "scope_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.udf_service_get_udf_definition(name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UdfServiceApi->udf_service_get_udf_definition: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.udf_service_get_udf_definition(name, scope=scope)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UdfServiceApi->udf_service_get_udf_definition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  |
 **scope** | **str**|  | [optional]

### Return type

[**TitaniumGetUdfResponse**](TitaniumGetUdfResponse.md)

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

# **udf_service_list_udfs**
> TitaniumListUdfResponse udf_service_list_udfs(body)



### Example


```python
import time
import openapi_client
from openapi_client.api import udf_service_api
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_list_udf_response import TitaniumListUdfResponse
from openapi_client.model.titanium_list_request import TitaniumListRequest
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = udf_service_api.UdfServiceApi(api_client)
    body = TitaniumListRequest(
        filter="filter_example",
        limit=TitaniumLimit(
            value=1,
        ),
        offset=1,
        order_by=TitaniumOrderBy(
            column="column_example",
            order="order_example",
        ),
        scope="scope_example",
    ) # TitaniumListRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.udf_service_list_udfs(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UdfServiceApi->udf_service_list_udfs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumListRequest**](TitaniumListRequest.md)|  |

### Return type

[**TitaniumListUdfResponse**](TitaniumListUdfResponse.md)

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

