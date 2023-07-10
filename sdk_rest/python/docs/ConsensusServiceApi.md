# openapi_client.ConsensusServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**consensus_service_consensus**](ConsensusServiceApi.md#consensus_service_consensus) | **POST** /api/v1/consensus | Consensus return information about consensus according to request. Need to specify consensus run timestamp, asset ID and etc.(See ConsensusRequest definition) Returns ConsensusResponse that contains information about column and rows related to consensus.
[**consensus_service_consensus_active**](ConsensusServiceApi.md#consensus_service_consensus_active) | **POST** /api/v1/operator/consensus/active | 
[**consensus_service_consensus_decision**](ConsensusServiceApi.md#consensus_service_consensus_decision) | **POST** /api/v1/operator/consensus/decision | 
[**consensus_service_consensus_explorer_instrument_details**](ConsensusServiceApi.md#consensus_service_consensus_explorer_instrument_details) | **POST** /api/v1/consensus-explorer/details | 
[**consensus_service_consensus_explorer_ranges**](ConsensusServiceApi.md#consensus_service_consensus_explorer_ranges) | **POST** /api/v1/consensus-explorer/range | 
[**consensus_service_consensus_explorer_table**](ConsensusServiceApi.md#consensus_service_consensus_explorer_table) | **POST** /api/v1/consensus-explorer/table | 
[**consensus_service_consensus_history**](ConsensusServiceApi.md#consensus_service_consensus_history) | **POST** /api/v1/operator/consensus/history | 
[**consensus_service_consensus_outliers**](ConsensusServiceApi.md#consensus_service_consensus_outliers) | **POST** /api/v1/outliers-list | ConsensusOutliers return list of outliers according to specified consensus. Need to identify consensus tun timestamp and etc.(Described in OutliersListRequest) Return ConsensusActiveResponse that contains active consensuses with specified run timestamp.
[**consensus_service_consensus_publish**](ConsensusServiceApi.md#consensus_service_consensus_publish) | **POST** /api/v1/operator/consensus/publish | 
[**consensus_service_consensus_result_set_values**](ConsensusServiceApi.md#consensus_service_consensus_result_set_values) | **POST** /api/v1/consensus-result-set-view | 
[**consensus_service_consensus_timestamps**](ConsensusServiceApi.md#consensus_service_consensus_timestamps) | **POST** /api/v1/consensus/timestamps | ConsensusTimestamps returns timestamps when it was submitted. Need to specify asset ID and trace name. Returns ConsensusTimestampsResponse that contains all the timestamps related to specified asset ID.
[**consensus_service_consensus_to_publish**](ConsensusServiceApi.md#consensus_service_consensus_to_publish) | **POST** /api/v1/operator/consensus/to-publish | 
[**consensus_service_evaluated_price**](ConsensusServiceApi.md#consensus_service_evaluated_price) | **POST** /api/v1/evaluated-price | 
[**consensus_service_get_consensus_runs**](ConsensusServiceApi.md#consensus_service_get_consensus_runs) | **POST** /api/v1/consensus-runs-view | Get Consensus Run&#39;s consensus result sets


# **consensus_service_consensus**
> TitaniumConsensusResponse consensus_service_consensus(body)

Consensus return information about consensus according to request. Need to specify consensus run timestamp, asset ID and etc.(See ConsensusRequest definition) Returns ConsensusResponse that contains information about column and rows related to consensus.

This is a test of a different commenting type: Below we will be shown a placeholder for the Consensus RPC request. *sample input**  >`{`<br> >`   \"asset_id\": \"238917-2131-341ff\",`<br> >`   \"trace_name\": \"placeholder value\",`<br> >`   \"submitted_date\": \"238472301213\"`<br> >`}`

### Example


```python
import time
import openapi_client
from openapi_client.api import consensus_service_api
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_consensus_response import TitaniumConsensusResponse
from openapi_client.model.titanium_consensus_request import TitaniumConsensusRequest
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = consensus_service_api.ConsensusServiceApi(api_client)
    body = TitaniumConsensusRequest(
        asset_id="asset_id_example",
        consensus_run_timestamp="consensus_run_timestamp_example",
        filter="filter_example",
        limit=TitaniumLimit(
            value=1,
        ),
        offset=1,
        order_by=TitaniumOrderBy(
            column="column_example",
            order="order_example",
        ),
        submitted_date="submitted_date_example",
        trace_name="trace_name_example",
    ) # TitaniumConsensusRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Consensus return information about consensus according to request. Need to specify consensus run timestamp, asset ID and etc.(See ConsensusRequest definition) Returns ConsensusResponse that contains information about column and rows related to consensus.
        api_response = api_instance.consensus_service_consensus(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConsensusServiceApi->consensus_service_consensus: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumConsensusRequest**](TitaniumConsensusRequest.md)|  |

### Return type

[**TitaniumConsensusResponse**](TitaniumConsensusResponse.md)

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

# **consensus_service_consensus_active**
> TitaniumConsensusActiveResponse consensus_service_consensus_active(body)



### Example


```python
import time
import openapi_client
from openapi_client.api import consensus_service_api
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_consensus_active_response import TitaniumConsensusActiveResponse
from openapi_client.model.titanium_consensus_active_request import TitaniumConsensusActiveRequest
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = consensus_service_api.ConsensusServiceApi(api_client)
    body = TitaniumConsensusActiveRequest(
        filter="filter_example",
        limit=TitaniumLimit(
            value=1,
        ),
        offset=1,
        order_by=TitaniumOrderBy(
            column="column_example",
            order="order_example",
        ),
    ) # TitaniumConsensusActiveRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.consensus_service_consensus_active(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConsensusServiceApi->consensus_service_consensus_active: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumConsensusActiveRequest**](TitaniumConsensusActiveRequest.md)|  |

### Return type

[**TitaniumConsensusActiveResponse**](TitaniumConsensusActiveResponse.md)

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

# **consensus_service_consensus_decision**
> TitaniumMessageResponse consensus_service_consensus_decision(body)



### Example


```python
import time
import openapi_client
from openapi_client.api import consensus_service_api
from openapi_client.model.titanium_message_response import TitaniumMessageResponse
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_consensus_decision_request import TitaniumConsensusDecisionRequest
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = consensus_service_api.ConsensusServiceApi(api_client)
    body = TitaniumConsensusDecisionRequest(
        consensus_tracking_id="consensus_tracking_id_example",
        decision="decision_example",
    ) # TitaniumConsensusDecisionRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.consensus_service_consensus_decision(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConsensusServiceApi->consensus_service_consensus_decision: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumConsensusDecisionRequest**](TitaniumConsensusDecisionRequest.md)|  |

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

# **consensus_service_consensus_explorer_instrument_details**
> TitaniumConsensusExplorerInstrumentDetailsResponse consensus_service_consensus_explorer_instrument_details()



### Example


```python
import time
import openapi_client
from openapi_client.api import consensus_service_api
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_consensus_explorer_instrument_details_response import TitaniumConsensusExplorerInstrumentDetailsResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = consensus_service_api.ConsensusServiceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.consensus_service_consensus_explorer_instrument_details()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConsensusServiceApi->consensus_service_consensus_explorer_instrument_details: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**TitaniumConsensusExplorerInstrumentDetailsResponse**](TitaniumConsensusExplorerInstrumentDetailsResponse.md)

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

# **consensus_service_consensus_explorer_ranges**
> TitaniumConsensusExplorerRangeResponse consensus_service_consensus_explorer_ranges()



### Example


```python
import time
import openapi_client
from openapi_client.api import consensus_service_api
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_consensus_explorer_range_response import TitaniumConsensusExplorerRangeResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = consensus_service_api.ConsensusServiceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.consensus_service_consensus_explorer_ranges()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConsensusServiceApi->consensus_service_consensus_explorer_ranges: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**TitaniumConsensusExplorerRangeResponse**](TitaniumConsensusExplorerRangeResponse.md)

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

# **consensus_service_consensus_explorer_table**
> TitaniumConsensusExplorerTableResponse consensus_service_consensus_explorer_table()



### Example


```python
import time
import openapi_client
from openapi_client.api import consensus_service_api
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_consensus_explorer_table_response import TitaniumConsensusExplorerTableResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = consensus_service_api.ConsensusServiceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.consensus_service_consensus_explorer_table()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConsensusServiceApi->consensus_service_consensus_explorer_table: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**TitaniumConsensusExplorerTableResponse**](TitaniumConsensusExplorerTableResponse.md)

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

# **consensus_service_consensus_history**
> TitaniumConsensusHistoryResponse consensus_service_consensus_history(body)



### Example


```python
import time
import openapi_client
from openapi_client.api import consensus_service_api
from openapi_client.model.titanium_consensus_history_request import TitaniumConsensusHistoryRequest
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_consensus_history_response import TitaniumConsensusHistoryResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = consensus_service_api.ConsensusServiceApi(api_client)
    body = TitaniumConsensusHistoryRequest(
        filter="filter_example",
        limit=TitaniumLimit(
            value=1,
        ),
        offset=1,
        order_by=TitaniumOrderBy(
            column="column_example",
            order="order_example",
        ),
    ) # TitaniumConsensusHistoryRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.consensus_service_consensus_history(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConsensusServiceApi->consensus_service_consensus_history: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumConsensusHistoryRequest**](TitaniumConsensusHistoryRequest.md)|  |

### Return type

[**TitaniumConsensusHistoryResponse**](TitaniumConsensusHistoryResponse.md)

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

# **consensus_service_consensus_outliers**
> TitaniumConsensusActiveResponse consensus_service_consensus_outliers(body)

ConsensusOutliers return list of outliers according to specified consensus. Need to identify consensus tun timestamp and etc.(Described in OutliersListRequest) Return ConsensusActiveResponse that contains active consensuses with specified run timestamp.

### Example


```python
import time
import openapi_client
from openapi_client.api import consensus_service_api
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_consensus_active_response import TitaniumConsensusActiveResponse
from openapi_client.model.titanium_outliers_list_request import TitaniumOutliersListRequest
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = consensus_service_api.ConsensusServiceApi(api_client)
    body = TitaniumOutliersListRequest(
        asset_id="asset_id_example",
        consensus_run_timestamp="consensus_run_timestamp_example",
        filter="filter_example",
        limit=TitaniumLimit(
            value=1,
        ),
        offset=1,
        order_by=TitaniumOrderBy(
            column="column_example",
            order="order_example",
        ),
        submitted_date="submitted_date_example",
        submitted_id="submitted_id_example",
        trace_name="trace_name_example",
    ) # TitaniumOutliersListRequest | 

    # example passing only required values which don't have defaults set
    try:
        # ConsensusOutliers return list of outliers according to specified consensus. Need to identify consensus tun timestamp and etc.(Described in OutliersListRequest) Return ConsensusActiveResponse that contains active consensuses with specified run timestamp.
        api_response = api_instance.consensus_service_consensus_outliers(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConsensusServiceApi->consensus_service_consensus_outliers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumOutliersListRequest**](TitaniumOutliersListRequest.md)|  |

### Return type

[**TitaniumConsensusActiveResponse**](TitaniumConsensusActiveResponse.md)

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

# **consensus_service_consensus_publish**
> TitaniumMessageResponse consensus_service_consensus_publish(body)



### Example


```python
import time
import openapi_client
from openapi_client.api import consensus_service_api
from openapi_client.model.titanium_message_response import TitaniumMessageResponse
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_consensus_publish_request import TitaniumConsensusPublishRequest
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = consensus_service_api.ConsensusServiceApi(api_client)
    body = TitaniumConsensusPublishRequest(
        asset_id="asset_id_example",
        consensus_tracking_id="consensus_tracking_id_example",
        trace_name="trace_name_example",
    ) # TitaniumConsensusPublishRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.consensus_service_consensus_publish(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConsensusServiceApi->consensus_service_consensus_publish: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumConsensusPublishRequest**](TitaniumConsensusPublishRequest.md)|  |

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

# **consensus_service_consensus_result_set_values**
> TitaniumConsensusResultSetValuesResponse consensus_service_consensus_result_set_values(body)



### Example


```python
import time
import openapi_client
from openapi_client.api import consensus_service_api
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_consensus_result_set_values_request import TitaniumConsensusResultSetValuesRequest
from openapi_client.model.titanium_consensus_result_set_values_response import TitaniumConsensusResultSetValuesResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = consensus_service_api.ConsensusServiceApi(api_client)
    body = TitaniumConsensusResultSetValuesRequest(
        asset_id="asset_id_example",
        client="client_example",
        consensus_run_timestamp="consensus_run_timestamp_example",
        filter_pack=TitaniumFilterPack(
            filter_packs=[
                TitaniumFilterPack(),
            ],
            filters=[
                TitaniumFilter(
                    key="key_example",
                    operator="operator_example",
                    value={},
                ),
            ],
            logical_operation="logical_operation_example",
        ),
        order_by=TitaniumOrderBy(
            column="column_example",
            order="order_example",
        ),
        page=TitaniumPage(
            page_number=1,
            size=1,
            total_number_of_elements="total_number_of_elements_example",
        ),
        submitted_date="submitted_date_example",
        trace_name="trace_name_example",
    ) # TitaniumConsensusResultSetValuesRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.consensus_service_consensus_result_set_values(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConsensusServiceApi->consensus_service_consensus_result_set_values: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumConsensusResultSetValuesRequest**](TitaniumConsensusResultSetValuesRequest.md)|  |

### Return type

[**TitaniumConsensusResultSetValuesResponse**](TitaniumConsensusResultSetValuesResponse.md)

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

# **consensus_service_consensus_timestamps**
> TitaniumConsensusTimestampsResponse consensus_service_consensus_timestamps(body)

ConsensusTimestamps returns timestamps when it was submitted. Need to specify asset ID and trace name. Returns ConsensusTimestampsResponse that contains all the timestamps related to specified asset ID.

This is a test to see how detailed we can make a RPC method's documentation using this commenting type: Below we will be shown sample input for the ConsensusTimestamps endpoint. **sample input**  >`{`<br> >`   \"asset_id\": \"238917-2131-341ff\",`<br> >`   \"trace_name\": \"placeholder value\"`<br> >`}`

### Example


```python
import time
import openapi_client
from openapi_client.api import consensus_service_api
from openapi_client.model.titanium_consensus_timestamps_response import TitaniumConsensusTimestampsResponse
from openapi_client.model.titanium_consensus_timestamps_request import TitaniumConsensusTimestampsRequest
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
    api_instance = consensus_service_api.ConsensusServiceApi(api_client)
    body = TitaniumConsensusTimestampsRequest(
        asset_id="asset_id_example",
        trace_name="trace_name_example",
    ) # TitaniumConsensusTimestampsRequest | 

    # example passing only required values which don't have defaults set
    try:
        # ConsensusTimestamps returns timestamps when it was submitted. Need to specify asset ID and trace name. Returns ConsensusTimestampsResponse that contains all the timestamps related to specified asset ID.
        api_response = api_instance.consensus_service_consensus_timestamps(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConsensusServiceApi->consensus_service_consensus_timestamps: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumConsensusTimestampsRequest**](TitaniumConsensusTimestampsRequest.md)|  |

### Return type

[**TitaniumConsensusTimestampsResponse**](TitaniumConsensusTimestampsResponse.md)

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

# **consensus_service_consensus_to_publish**
> TitaniumConsensusToPublishResponse consensus_service_consensus_to_publish(body)



### Example


```python
import time
import openapi_client
from openapi_client.api import consensus_service_api
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_consensus_to_publish_response import TitaniumConsensusToPublishResponse
from openapi_client.model.titanium_consensus_to_publish_request import TitaniumConsensusToPublishRequest
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = consensus_service_api.ConsensusServiceApi(api_client)
    body = TitaniumConsensusToPublishRequest(
        filter="filter_example",
        limit=TitaniumLimit(
            value=1,
        ),
        offset=1,
        order_by=TitaniumOrderBy(
            column="column_example",
            order="order_example",
        ),
    ) # TitaniumConsensusToPublishRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.consensus_service_consensus_to_publish(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConsensusServiceApi->consensus_service_consensus_to_publish: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumConsensusToPublishRequest**](TitaniumConsensusToPublishRequest.md)|  |

### Return type

[**TitaniumConsensusToPublishResponse**](TitaniumConsensusToPublishResponse.md)

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

# **consensus_service_evaluated_price**
> TitaniumEVPResponse consensus_service_evaluated_price(body)



### Example


```python
import time
import openapi_client
from openapi_client.api import consensus_service_api
from openapi_client.model.titanium_evp_response import TitaniumEVPResponse
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_evp_request import TitaniumEVPRequest
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = consensus_service_api.ConsensusServiceApi(api_client)
    body = TitaniumEVPRequest(
        asset_id="asset_id_example",
        consensus_run_timestamp="consensus_run_timestamp_example",
        filter_pack=TitaniumFilterPack(
            filter_packs=[
                TitaniumFilterPack(),
            ],
            filters=[
                TitaniumFilter(
                    key="key_example",
                    operator="operator_example",
                    value={},
                ),
            ],
            logical_operation="logical_operation_example",
        ),
        order_by=TitaniumOrderBy(
            column="column_example",
            order="order_example",
        ),
        page=TitaniumPage(
            page_number=1,
            size=1,
            total_number_of_elements="total_number_of_elements_example",
        ),
        submitted_date="submitted_date_example",
        trace_name="trace_name_example",
    ) # TitaniumEVPRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.consensus_service_evaluated_price(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConsensusServiceApi->consensus_service_evaluated_price: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumEVPRequest**](TitaniumEVPRequest.md)|  |

### Return type

[**TitaniumEVPResponse**](TitaniumEVPResponse.md)

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

# **consensus_service_get_consensus_runs**
> TitaniumGetConsensusRunsResponse consensus_service_get_consensus_runs(body)

Get Consensus Run's consensus result sets

### Example


```python
import time
import openapi_client
from openapi_client.api import consensus_service_api
from openapi_client.model.titanium_get_consensus_runs_request import TitaniumGetConsensusRunsRequest
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_get_consensus_runs_response import TitaniumGetConsensusRunsResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = consensus_service_api.ConsensusServiceApi(api_client)
    body = TitaniumGetConsensusRunsRequest(
        asset_id="asset_id_example",
        filter_pack=TitaniumFilterPack(
            filter_packs=[
                TitaniumFilterPack(),
            ],
            filters=[
                TitaniumFilter(
                    key="key_example",
                    operator="operator_example",
                    value={},
                ),
            ],
            logical_operation="logical_operation_example",
        ),
        order_by=TitaniumOrderBy(
            column="column_example",
            order="order_example",
        ),
        page=TitaniumPage(
            page_number=1,
            size=1,
            total_number_of_elements="total_number_of_elements_example",
        ),
        participant="participant_example",
        show_archived=True,
        snap_date_from="snap_date_from_example",
        snap_date_to="snap_date_to_example",
        trace_name="trace_name_example",
    ) # TitaniumGetConsensusRunsRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get Consensus Run's consensus result sets
        api_response = api_instance.consensus_service_get_consensus_runs(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConsensusServiceApi->consensus_service_get_consensus_runs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumGetConsensusRunsRequest**](TitaniumGetConsensusRunsRequest.md)|  |

### Return type

[**TitaniumGetConsensusRunsResponse**](TitaniumGetConsensusRunsResponse.md)

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

