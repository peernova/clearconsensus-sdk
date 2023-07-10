# openapi_client.AdminServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_service_on_board**](AdminServiceApi.md#admin_service_on_board) | **POST** /api/v1/onboard | 
[**admin_service_run_calculator**](AdminServiceApi.md#admin_service_run_calculator) | **POST** /api/v1/calculator/run | 
[**admin_service_run_consensus**](AdminServiceApi.md#admin_service_run_consensus) | **POST** /api/v1/consensus/run | 
[**admin_service_upload_evaluated_price**](AdminServiceApi.md#admin_service_upload_evaluated_price) | **POST** /api/v1/upload/evaluated-price | 


# **admin_service_on_board**
> TitaniumMessageResponse admin_service_on_board(body)



### Example


```python
import time
import openapi_client
from openapi_client.api import admin_service_api
from openapi_client.model.titanium_message_response import TitaniumMessageResponse
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_on_board_request import TitaniumOnBoardRequest
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = admin_service_api.AdminServiceApi(api_client)
    body = TitaniumOnBoardRequest(
        authorized=TitaniumAssetsList(
            assets=[
                TitaniumAsset(
                    name="name_example",
                    services=[
                        TitaniumService(
                            name="name_example",
                            sub_assets=[
                                TitaniumSubAsset(
                                    id="id_example",
                                    name="name_example",
                                    trace_name="trace_name_example",
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        ),
        client="client_example",
        password="password_example",
        public_key="public_key_example",
        username="username_example",
    ) # TitaniumOnBoardRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.admin_service_on_board(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AdminServiceApi->admin_service_on_board: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumOnBoardRequest**](TitaniumOnBoardRequest.md)|  |

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

# **admin_service_run_calculator**
> TitaniumMessageResponse admin_service_run_calculator(body)



### Example


```python
import time
import openapi_client
from openapi_client.api import admin_service_api
from openapi_client.model.titanium_message_response import TitaniumMessageResponse
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_run_calculator_request import TitaniumRunCalculatorRequest
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = admin_service_api.AdminServiceApi(api_client)
    body = TitaniumRunCalculatorRequest(
        asset_id="asset_id_example",
        clients=[
            "clients_example",
        ],
        consensus_run_reason="consensus_run_reason_example",
        dates=[
            "dates_example",
        ],
        description="description_example",
        trace_name="trace_name_example",
    ) # TitaniumRunCalculatorRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.admin_service_run_calculator(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AdminServiceApi->admin_service_run_calculator: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumRunCalculatorRequest**](TitaniumRunCalculatorRequest.md)|  |

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

# **admin_service_run_consensus**
> TitaniumMessageResponse admin_service_run_consensus(body)



### Example


```python
import time
import openapi_client
from openapi_client.api import admin_service_api
from openapi_client.model.titanium_message_response import TitaniumMessageResponse
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_run_consensus_request import TitaniumRunConsensusRequest
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = admin_service_api.AdminServiceApi(api_client)
    body = TitaniumRunConsensusRequest(
        asset_id="asset_id_example",
        clients=[
            "clients_example",
        ],
        dates=[
            "dates_example",
        ],
        description="description_example",
        trace_name="trace_name_example",
    ) # TitaniumRunConsensusRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.admin_service_run_consensus(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AdminServiceApi->admin_service_run_consensus: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumRunConsensusRequest**](TitaniumRunConsensusRequest.md)|  |

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

# **admin_service_upload_evaluated_price**
> TitaniumMessageResponse admin_service_upload_evaluated_price(body)



### Example


```python
import time
import openapi_client
from openapi_client.api import admin_service_api
from openapi_client.model.titanium_message_response import TitaniumMessageResponse
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_upload_evaluated_price_request import TitaniumUploadEvaluatedPriceRequest
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = admin_service_api.AdminServiceApi(api_client)
    body = TitaniumUploadEvaluatedPriceRequest(
        asset_id="asset_id_example",
        date="date_example",
        file="file_example",
        file_name="file_name_example",
        trace_name="trace_name_example",
    ) # TitaniumUploadEvaluatedPriceRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.admin_service_upload_evaluated_price(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AdminServiceApi->admin_service_upload_evaluated_price: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumUploadEvaluatedPriceRequest**](TitaniumUploadEvaluatedPriceRequest.md)|  |

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

