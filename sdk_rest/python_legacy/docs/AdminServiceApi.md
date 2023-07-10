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
    api_instance = openapi_client.AdminServiceApi(api_client)
    body = openapi_client.TitaniumOnBoardRequest() # TitaniumOnBoardRequest | 

    try:
        api_response = api_instance.admin_service_on_board(body)
        pprint(api_response)
    except ApiException as e:
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
    api_instance = openapi_client.AdminServiceApi(api_client)
    body = openapi_client.TitaniumRunCalculatorRequest() # TitaniumRunCalculatorRequest | 

    try:
        api_response = api_instance.admin_service_run_calculator(body)
        pprint(api_response)
    except ApiException as e:
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
    api_instance = openapi_client.AdminServiceApi(api_client)
    body = openapi_client.TitaniumRunConsensusRequest() # TitaniumRunConsensusRequest | 

    try:
        api_response = api_instance.admin_service_run_consensus(body)
        pprint(api_response)
    except ApiException as e:
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
    api_instance = openapi_client.AdminServiceApi(api_client)
    body = openapi_client.TitaniumUploadEvaluatedPriceRequest() # TitaniumUploadEvaluatedPriceRequest | 

    try:
        api_response = api_instance.admin_service_upload_evaluated_price(body)
        pprint(api_response)
    except ApiException as e:
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

