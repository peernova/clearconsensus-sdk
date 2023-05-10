# openapi_client.MarketServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**market_service_market_snap_time**](MarketServiceApi.md#market_service_market_snap_time) | **GET** /api/v1/market/snap-time | MarketSnapTime returns time for which the prices(calculated in consensus) are valid.(Time of market closing)


# **market_service_market_snap_time**
> TitaniumMarketSnapTimeResponse market_service_market_snap_time()

MarketSnapTime returns time for which the prices(calculated in consensus) are valid.(Time of market closing)

### Example


```python
import time
import openapi_client
from openapi_client.api import market_service_api
from openapi_client.model.titanium_market_snap_time_response import TitaniumMarketSnapTimeResponse
from openapi_client.model.rpc_status import RpcStatus
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = market_service_api.MarketServiceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # MarketSnapTime returns time for which the prices(calculated in consensus) are valid.(Time of market closing)
        api_response = api_instance.market_service_market_snap_time()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MarketServiceApi->market_service_market_snap_time: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**TitaniumMarketSnapTimeResponse**](TitaniumMarketSnapTimeResponse.md)

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

