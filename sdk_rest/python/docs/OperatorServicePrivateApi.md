# openapi_client.OperatorServicePrivateApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**operator_service_private_add_asset**](OperatorServicePrivateApi.md#operator_service_private_add_asset) | **POST** /api/v1/operator/assets/add | AddAsset adds asset to the system.
[**operator_service_private_add_client**](OperatorServicePrivateApi.md#operator_service_private_add_client) | **POST** /api/v1/operator/client/add | 
[**operator_service_private_add_supported_fields**](OperatorServicePrivateApi.md#operator_service_private_add_supported_fields) | **POST** /api/v1/operator/add/field-values | 
[**operator_service_private_assets**](OperatorServicePrivateApi.md#operator_service_private_assets) | **POST** /api/v1/operator/assets | 
[**operator_service_private_create_supported_fields**](OperatorServicePrivateApi.md#operator_service_private_create_supported_fields) | **POST** /api/v1/operator/create/field-values | 
[**operator_service_private_delete_supported_fields**](OperatorServicePrivateApi.md#operator_service_private_delete_supported_fields) | **POST** /api/v1/operator/delete/field-values | 
[**operator_service_private_evp_statuses**](OperatorServicePrivateApi.md#operator_service_private_evp_statuses) | **POST** /api/v1/operator/evaluated-prices/slice | 
[**operator_service_private_export_report**](OperatorServicePrivateApi.md#operator_service_private_export_report) | **POST** /api/v1/operator/report | ExportReport returns pre signed s3 urls which can be used for export report(and compression type)
[**operator_service_private_list_clients**](OperatorServicePrivateApi.md#operator_service_private_list_clients) | **GET** /api/v1/operator/client/list | 
[**operator_service_private_operator_outliers**](OperatorServicePrivateApi.md#operator_service_private_operator_outliers) | **POST** /api/v1/operator-outliers | 
[**operator_service_private_outliers**](OperatorServicePrivateApi.md#operator_service_private_outliers) | **POST** /api/v1/operator/outliers | 
[**operator_service_private_recent_assets**](OperatorServicePrivateApi.md#operator_service_private_recent_assets) | **POST** /api/v1/operator/recentassets | 
[**operator_service_private_upload_dtcc**](OperatorServicePrivateApi.md#operator_service_private_upload_dtcc) | **POST** /api/v1/operator/dtcc-trades/upload | 
[**operator_service_private_upload_evp**](OperatorServicePrivateApi.md#operator_service_private_upload_evp) | **POST** /api/v1/operator/evp/upload | 


# **operator_service_private_add_asset**
> TitaniumMessageResponse operator_service_private_add_asset(body)

AddAsset adds asset to the system.

### Example


```python
import time
import openapi_client
from openapi_client.api import operator_service_private_api
from openapi_client.model.titanium_message_response import TitaniumMessageResponse
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_add_asset_request import TitaniumAddAssetRequest
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = operator_service_private_api.OperatorServicePrivateApi(api_client)
    body = TitaniumAddAssetRequest(
        asset="asset_example",
        instrument_type="instrument_type_example",
        service="service_example",
    ) # TitaniumAddAssetRequest | 

    # example passing only required values which don't have defaults set
    try:
        # AddAsset adds asset to the system.
        api_response = api_instance.operator_service_private_add_asset(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OperatorServicePrivateApi->operator_service_private_add_asset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumAddAssetRequest**](TitaniumAddAssetRequest.md)|  |

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

# **operator_service_private_add_client**
> TitaniumMessageResponse operator_service_private_add_client(body)



### Example


```python
import time
import openapi_client
from openapi_client.api import operator_service_private_api
from openapi_client.model.titanium_message_response import TitaniumMessageResponse
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_client_name import TitaniumClientName
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = operator_service_private_api.OperatorServicePrivateApi(api_client)
    body = TitaniumClientName(
        display_name="display_name_example",
        name="name_example",
    ) # TitaniumClientName | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.operator_service_private_add_client(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OperatorServicePrivateApi->operator_service_private_add_client: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumClientName**](TitaniumClientName.md)|  |

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

# **operator_service_private_add_supported_fields**
> TitaniumMessageResponse operator_service_private_add_supported_fields(body)



### Example


```python
import time
import openapi_client
from openapi_client.api import operator_service_private_api
from openapi_client.model.titanium_supported_fields_values import TitaniumSupportedFieldsValues
from openapi_client.model.titanium_message_response import TitaniumMessageResponse
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
    api_instance = operator_service_private_api.OperatorServicePrivateApi(api_client)
    body = TitaniumSupportedFieldsValues(
        asset_id="asset_id_example",
        field="field_example",
        trace_name="trace_name_example",
        values=[
            "values_example",
        ],
    ) # TitaniumSupportedFieldsValues | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.operator_service_private_add_supported_fields(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OperatorServicePrivateApi->operator_service_private_add_supported_fields: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumSupportedFieldsValues**](TitaniumSupportedFieldsValues.md)|  |

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

# **operator_service_private_assets**
> TitaniumAssetsResponse operator_service_private_assets(body)



### Example


```python
import time
import openapi_client
from openapi_client.api import operator_service_private_api
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
    api_instance = operator_service_private_api.OperatorServicePrivateApi(api_client)
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
        api_response = api_instance.operator_service_private_assets(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OperatorServicePrivateApi->operator_service_private_assets: %s\n" % e)
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

# **operator_service_private_create_supported_fields**
> TitaniumMessageResponse operator_service_private_create_supported_fields(body)



### Example


```python
import time
import openapi_client
from openapi_client.api import operator_service_private_api
from openapi_client.model.titanium_supported_fields_values import TitaniumSupportedFieldsValues
from openapi_client.model.titanium_message_response import TitaniumMessageResponse
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
    api_instance = operator_service_private_api.OperatorServicePrivateApi(api_client)
    body = TitaniumSupportedFieldsValues(
        asset_id="asset_id_example",
        field="field_example",
        trace_name="trace_name_example",
        values=[
            "values_example",
        ],
    ) # TitaniumSupportedFieldsValues | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.operator_service_private_create_supported_fields(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OperatorServicePrivateApi->operator_service_private_create_supported_fields: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumSupportedFieldsValues**](TitaniumSupportedFieldsValues.md)|  |

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

# **operator_service_private_delete_supported_fields**
> TitaniumMessageResponse operator_service_private_delete_supported_fields(body)



### Example


```python
import time
import openapi_client
from openapi_client.api import operator_service_private_api
from openapi_client.model.titanium_supported_fields_values import TitaniumSupportedFieldsValues
from openapi_client.model.titanium_message_response import TitaniumMessageResponse
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
    api_instance = operator_service_private_api.OperatorServicePrivateApi(api_client)
    body = TitaniumSupportedFieldsValues(
        asset_id="asset_id_example",
        field="field_example",
        trace_name="trace_name_example",
        values=[
            "values_example",
        ],
    ) # TitaniumSupportedFieldsValues | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.operator_service_private_delete_supported_fields(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OperatorServicePrivateApi->operator_service_private_delete_supported_fields: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumSupportedFieldsValues**](TitaniumSupportedFieldsValues.md)|  |

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

# **operator_service_private_evp_statuses**
> TitaniumEvpStatusesResponse operator_service_private_evp_statuses(body)



### Example


```python
import time
import openapi_client
from openapi_client.api import operator_service_private_api
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_evp_statuses_response import TitaniumEvpStatusesResponse
from openapi_client.model.titanium_evp_statuses_request import TitaniumEvpStatusesRequest
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = operator_service_private_api.OperatorServicePrivateApi(api_client)
    body = TitaniumEvpStatusesRequest(
        slice_request_data=TitaniumSliceRequestData(
            limit=1,
            offset=1,
        ),
    ) # TitaniumEvpStatusesRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.operator_service_private_evp_statuses(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OperatorServicePrivateApi->operator_service_private_evp_statuses: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumEvpStatusesRequest**](TitaniumEvpStatusesRequest.md)|  |

### Return type

[**TitaniumEvpStatusesResponse**](TitaniumEvpStatusesResponse.md)

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

# **operator_service_private_export_report**
> TitaniumExportResponse operator_service_private_export_report(body)

ExportReport returns pre signed s3 urls which can be used for export report(and compression type)

### Example


```python
import time
import openapi_client
from openapi_client.api import operator_service_private_api
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_export_response import TitaniumExportResponse
from openapi_client.model.titanium_export_report_request import TitaniumExportReportRequest
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = operator_service_private_api.OperatorServicePrivateApi(api_client)
    body = TitaniumExportReportRequest(
        asset_id="asset_id_example",
        consensus_run_timestamp="consensus_run_timestamp_example",
        trace_name="trace_name_example",
    ) # TitaniumExportReportRequest | 

    # example passing only required values which don't have defaults set
    try:
        # ExportReport returns pre signed s3 urls which can be used for export report(and compression type)
        api_response = api_instance.operator_service_private_export_report(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OperatorServicePrivateApi->operator_service_private_export_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumExportReportRequest**](TitaniumExportReportRequest.md)|  |

### Return type

[**TitaniumExportResponse**](TitaniumExportResponse.md)

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

# **operator_service_private_list_clients**
> TitaniumListClientsResponse operator_service_private_list_clients()



### Example


```python
import time
import openapi_client
from openapi_client.api import operator_service_private_api
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_list_clients_response import TitaniumListClientsResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = operator_service_private_api.OperatorServicePrivateApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.operator_service_private_list_clients()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OperatorServicePrivateApi->operator_service_private_list_clients: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**TitaniumListClientsResponse**](TitaniumListClientsResponse.md)

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

# **operator_service_private_operator_outliers**
> TitaniumOperatorOutliersResponse operator_service_private_operator_outliers(body)



### Example


```python
import time
import openapi_client
from openapi_client.api import operator_service_private_api
from openapi_client.model.titanium_operator_outliers_response import TitaniumOperatorOutliersResponse
from openapi_client.model.titanium_operator_outliers_request import TitaniumOperatorOutliersRequest
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
    api_instance = operator_service_private_api.OperatorServicePrivateApi(api_client)
    body = TitaniumOperatorOutliersRequest(
        date="date_example",
        filter="filter_example",
        limit=TitaniumLimit(
            value=1,
        ),
        offset=1,
        order_by=TitaniumOrderBy(
            column="column_example",
            order="order_example",
        ),
    ) # TitaniumOperatorOutliersRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.operator_service_private_operator_outliers(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OperatorServicePrivateApi->operator_service_private_operator_outliers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumOperatorOutliersRequest**](TitaniumOperatorOutliersRequest.md)|  |

### Return type

[**TitaniumOperatorOutliersResponse**](TitaniumOperatorOutliersResponse.md)

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

# **operator_service_private_outliers**
> TitaniumOutliersResponse operator_service_private_outliers(body)



### Example


```python
import time
import openapi_client
from openapi_client.api import operator_service_private_api
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_outliers_request import TitaniumOutliersRequest
from openapi_client.model.titanium_outliers_response import TitaniumOutliersResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = operator_service_private_api.OperatorServicePrivateApi(api_client)
    body = TitaniumOutliersRequest(
        filter="filter_example",
        limit=TitaniumLimit(
            value=1,
        ),
        offset=1,
        order_by=TitaniumOrderBy(
            column="column_example",
            order="order_example",
        ),
    ) # TitaniumOutliersRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.operator_service_private_outliers(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OperatorServicePrivateApi->operator_service_private_outliers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumOutliersRequest**](TitaniumOutliersRequest.md)|  |

### Return type

[**TitaniumOutliersResponse**](TitaniumOutliersResponse.md)

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

# **operator_service_private_recent_assets**
> TitaniumRecentAssetsResponse operator_service_private_recent_assets(body)



### Example


```python
import time
import openapi_client
from openapi_client.api import operator_service_private_api
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
    api_instance = operator_service_private_api.OperatorServicePrivateApi(api_client)
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
        api_response = api_instance.operator_service_private_recent_assets(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OperatorServicePrivateApi->operator_service_private_recent_assets: %s\n" % e)
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

# **operator_service_private_upload_dtcc**
> TitaniumUploadURLResponse operator_service_private_upload_dtcc(body)



### Example


```python
import time
import openapi_client
from openapi_client.api import operator_service_private_api
from openapi_client.model.titanium_upload_dtcc_request import TitaniumUploadDTCCRequest
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_upload_url_response import TitaniumUploadURLResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = operator_service_private_api.OperatorServicePrivateApi(api_client)
    body = TitaniumUploadDTCCRequest(
        asset_id="asset_id_example",
        date="date_example",
        file_name="file_name_example",
        trace_name="trace_name_example",
    ) # TitaniumUploadDTCCRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.operator_service_private_upload_dtcc(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OperatorServicePrivateApi->operator_service_private_upload_dtcc: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumUploadDTCCRequest**](TitaniumUploadDTCCRequest.md)|  |

### Return type

[**TitaniumUploadURLResponse**](TitaniumUploadURLResponse.md)

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

# **operator_service_private_upload_evp**
> TitaniumUploadURLResponse operator_service_private_upload_evp(body)



### Example


```python
import time
import openapi_client
from openapi_client.api import operator_service_private_api
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_upload_evp_request import TitaniumUploadEVPRequest
from openapi_client.model.titanium_upload_url_response import TitaniumUploadURLResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = operator_service_private_api.OperatorServicePrivateApi(api_client)
    body = TitaniumUploadEVPRequest(
        asset_id="asset_id_example",
        date="date_example",
        file_name="file_name_example",
        trace_name="trace_name_example",
    ) # TitaniumUploadEVPRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.operator_service_private_upload_evp(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OperatorServicePrivateApi->operator_service_private_upload_evp: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumUploadEVPRequest**](TitaniumUploadEVPRequest.md)|  |

### Return type

[**TitaniumUploadURLResponse**](TitaniumUploadURLResponse.md)

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

