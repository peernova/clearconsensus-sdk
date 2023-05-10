# openapi_client.AssetsServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assets_service_assets**](AssetsServiceApi.md#assets_service_assets) | **POST** /api/v1/assets | Assets returns asset from the system according to request.
[**assets_service_assets_list**](AssetsServiceApi.md#assets_service_assets_list) | **POST** /api/v1/assets/list | AssetsList return list of assets according to snap time.
[**assets_service_recent_assets**](AssetsServiceApi.md#assets_service_recent_assets) | **POST** /api/v1/recentassets | RecentAssets returns recent added assets according to request.
[**assets_service_supported_assets**](AssetsServiceApi.md#assets_service_supported_assets) | **GET** /api/v1/supported/assets | 


# **assets_service_assets**
> TitaniumAssetsResponse assets_service_assets(body)

Assets returns asset from the system according to request.

### Example


```python
import time
import openapi_client
from openapi_client.api import assets_service_api
from openapi_client.model.titanium_assets_request import TitaniumAssetsRequest
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_assets_response import TitaniumAssetsResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = assets_service_api.AssetsServiceApi(api_client)
    body = TitaniumAssetsRequest(
        asset_id="asset_id_example",
        filter="filter_example",
        limit=TitaniumLimit(
            value=1,
        ),
        offset=1,
        order_by=TitaniumOrderBy(
            column="column_example",
            order="order_example",
        ),
        trace_name="trace_name_example",
    ) # TitaniumAssetsRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Assets returns asset from the system according to request.
        api_response = api_instance.assets_service_assets(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AssetsServiceApi->assets_service_assets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumAssetsRequest**](TitaniumAssetsRequest.md)|  |

### Return type

[**TitaniumAssetsResponse**](TitaniumAssetsResponse.md)

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

# **assets_service_assets_list**
> TitaniumAssetsListResponse assets_service_assets_list(body)

AssetsList return list of assets according to snap time.

### Example


```python
import time
import openapi_client
from openapi_client.api import assets_service_api
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_assets_list_request import TitaniumAssetsListRequest
from openapi_client.model.titanium_assets_list_response import TitaniumAssetsListResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = assets_service_api.AssetsServiceApi(api_client)
    body = TitaniumAssetsListRequest(
        snap_time="snap_time_example",
    ) # TitaniumAssetsListRequest | 

    # example passing only required values which don't have defaults set
    try:
        # AssetsList return list of assets according to snap time.
        api_response = api_instance.assets_service_assets_list(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AssetsServiceApi->assets_service_assets_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumAssetsListRequest**](TitaniumAssetsListRequest.md)|  |

### Return type

[**TitaniumAssetsListResponse**](TitaniumAssetsListResponse.md)

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

# **assets_service_recent_assets**
> TitaniumRecentAssetsResponse assets_service_recent_assets(body)

RecentAssets returns recent added assets according to request.

### Example


```python
import time
import openapi_client
from openapi_client.api import assets_service_api
from openapi_client.model.titanium_recent_assets_response import TitaniumRecentAssetsResponse
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_recent_assets_request import TitaniumRecentAssetsRequest
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = assets_service_api.AssetsServiceApi(api_client)
    body = TitaniumRecentAssetsRequest(
        filter="filter_example",
        limit=TitaniumLimit(
            value=1,
        ),
        offset=1,
        order_by=TitaniumOrderBy(
            column="column_example",
            order="order_example",
        ),
    ) # TitaniumRecentAssetsRequest | 

    # example passing only required values which don't have defaults set
    try:
        # RecentAssets returns recent added assets according to request.
        api_response = api_instance.assets_service_recent_assets(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AssetsServiceApi->assets_service_recent_assets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumRecentAssetsRequest**](TitaniumRecentAssetsRequest.md)|  |

### Return type

[**TitaniumRecentAssetsResponse**](TitaniumRecentAssetsResponse.md)

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

# **assets_service_supported_assets**
> TitaniumAssetsListResponse assets_service_supported_assets()



### Example


```python
import time
import openapi_client
from openapi_client.api import assets_service_api
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_assets_list_response import TitaniumAssetsListResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = assets_service_api.AssetsServiceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.assets_service_supported_assets()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AssetsServiceApi->assets_service_supported_assets: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**TitaniumAssetsListResponse**](TitaniumAssetsListResponse.md)

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

