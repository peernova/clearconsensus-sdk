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
    api_instance = openapi_client.AssetsServiceApi(api_client)
    body = openapi_client.TitaniumAssetsRequest() # TitaniumAssetsRequest | 

    try:
        # Assets returns asset from the system according to request.
        api_response = api_instance.assets_service_assets(body)
        pprint(api_response)
    except ApiException as e:
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
    api_instance = openapi_client.AssetsServiceApi(api_client)
    body = openapi_client.TitaniumAssetsListRequest() # TitaniumAssetsListRequest | 

    try:
        # AssetsList return list of assets according to snap time.
        api_response = api_instance.assets_service_assets_list(body)
        pprint(api_response)
    except ApiException as e:
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
    api_instance = openapi_client.AssetsServiceApi(api_client)
    body = openapi_client.TitaniumRecentAssetsRequest() # TitaniumRecentAssetsRequest | 

    try:
        # RecentAssets returns recent added assets according to request.
        api_response = api_instance.assets_service_recent_assets(body)
        pprint(api_response)
    except ApiException as e:
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
    api_instance = openapi_client.AssetsServiceApi(api_client)
    
    try:
        api_response = api_instance.assets_service_supported_assets()
        pprint(api_response)
    except ApiException as e:
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

