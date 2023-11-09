# openapi_client.DataServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**data_service_authorize_upload**](DataServiceApi.md#data_service_authorize_upload) | **POST** /api/v1/internal/upload/authorize | AuthorizeUpload shows availability of uploading for user.
[**data_service_complete_data_upload**](DataServiceApi.md#data_service_complete_data_upload) | **POST** /api/v1/upload/done | 
[**data_service_export**](DataServiceApi.md#data_service_export) | **POST** /api/v1/export | Export exports data according to the request.
[**data_service_notify_upload**](DataServiceApi.md#data_service_notify_upload) | **POST** /api/v1/internal/upload/notify | NotifyUpload returns message with notify that data was uploaded according to url in request.
[**data_service_submitted**](DataServiceApi.md#data_service_submitted) | **POST** /api/v1/submitted | Submitted returns submitted data based on the request made.
[**data_service_upload_data**](DataServiceApi.md#data_service_upload_data) | **POST** /api/v1/upload/data | 
[**data_service_upload_url**](DataServiceApi.md#data_service_upload_url) | **POST** /api/v1/upload/url | UploadURL returns a pre-signed S3 URL for uploading data.


# **data_service_authorize_upload**
> TitaniumUploadAuthorizationResponse data_service_authorize_upload(body)

AuthorizeUpload shows availability of uploading for user.

### Example


```python
import time
import openapi_client
from openapi_client.api import data_service_api
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_upload_authorization_response import TitaniumUploadAuthorizationResponse
from openapi_client.model.titanium_upload_url_request import TitaniumUploadURLRequest
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_service_api.DataServiceApi(api_client)
    body = TitaniumUploadURLRequest(
        asset_id="asset_id_example",
        client="client_example",
        date="date_example",
        descriptor_name="descriptor_name_example",
        file_annotation=[
            TitaniumFileAnnotation(
                annotation={},
                asset=TitaniumAssetDetails(
                    asset_id="asset_id_example",
                    date="date_example",
                    name="name_example",
                    service="service_example",
                    snap_time="snap_time_example",
                    sub_asset="sub_asset_example",
                ),
                chunks=[
                    TitaniumChunk(
                        annotation={},
                        chunk_id="chunk_id_example",
                        description="description_example",
                        original_file_name="original_file_name_example",
                        rows_count=1,
                        start_row=1,
                        user="user_example",
                    ),
                ],
                client="client_example",
                file_name="file_name_example",
                mode="mode_example",
                upload_time="upload_time_example",
            ),
        ],
        file_name="file_name_example",
        trace_name="trace_name_example",
    ) # TitaniumUploadURLRequest | 

    # example passing only required values which don't have defaults set
    try:
        # AuthorizeUpload shows availability of uploading for user.
        api_response = api_instance.data_service_authorize_upload(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DataServiceApi->data_service_authorize_upload: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumUploadURLRequest**](TitaniumUploadURLRequest.md)|  |

### Return type

[**TitaniumUploadAuthorizationResponse**](TitaniumUploadAuthorizationResponse.md)

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

# **data_service_complete_data_upload**
> TitaniumCompleteDataUploadResponse data_service_complete_data_upload(body)



### Example


```python
import time
import openapi_client
from openapi_client.api import data_service_api
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_complete_data_upload_response import TitaniumCompleteDataUploadResponse
from openapi_client.model.titanium_complete_data_upload_request import TitaniumCompleteDataUploadRequest
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_service_api.DataServiceApi(api_client)
    body = TitaniumCompleteDataUploadRequest(
        asset="asset_example",
        asset_id="asset_id_example",
        client="client_example",
        date="date_example",
        service="service_example",
        snap_time="snap_time_example",
        sub_asset="sub_asset_example",
    ) # TitaniumCompleteDataUploadRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.data_service_complete_data_upload(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DataServiceApi->data_service_complete_data_upload: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumCompleteDataUploadRequest**](TitaniumCompleteDataUploadRequest.md)|  |

### Return type

[**TitaniumCompleteDataUploadResponse**](TitaniumCompleteDataUploadResponse.md)

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

# **data_service_export**
> TitaniumExportResponse data_service_export(body)

Export exports data according to the request.

### Example


```python
import time
import openapi_client
from openapi_client.api import data_service_api
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_export_response import TitaniumExportResponse
from openapi_client.model.titanium_export_request import TitaniumExportRequest
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_service_api.DataServiceApi(api_client)
    body = TitaniumExportRequest(
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
        filters=[
            TitaniumFilter(
                key="key_example",
                operator="operator_example",
                value={},
            ),
        ],
        include_header=True,
        order_by=TitaniumOrderBy(
            column="column_example",
            order="order_example",
        ),
        submission_date="submission_date_example",
        trace_name="trace_name_example",
    ) # TitaniumExportRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Export exports data according to the request.
        api_response = api_instance.data_service_export(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DataServiceApi->data_service_export: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumExportRequest**](TitaniumExportRequest.md)|  |

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

# **data_service_notify_upload**
> TitaniumMessageResponse data_service_notify_upload(body)

NotifyUpload returns message with notify that data was uploaded according to url in request.

### Example


```python
import time
import openapi_client
from openapi_client.api import data_service_api
from openapi_client.model.titanium_message_response import TitaniumMessageResponse
from openapi_client.model.titanium_upload_notify_request import TitaniumUploadNotifyRequest
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
    api_instance = data_service_api.DataServiceApi(api_client)
    body = TitaniumUploadNotifyRequest(
        current_path="current_path_example",
        target_path="target_path_example",
        uuid="uuid_example",
    ) # TitaniumUploadNotifyRequest | 

    # example passing only required values which don't have defaults set
    try:
        # NotifyUpload returns message with notify that data was uploaded according to url in request.
        api_response = api_instance.data_service_notify_upload(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DataServiceApi->data_service_notify_upload: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumUploadNotifyRequest**](TitaniumUploadNotifyRequest.md)|  |

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

# **data_service_submitted**
> TitaniumSubmittedResponse data_service_submitted(body)

Submitted returns submitted data based on the request made.

### Example


```python
import time
import openapi_client
from openapi_client.api import data_service_api
from openapi_client.model.titanium_submitted_response import TitaniumSubmittedResponse
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_submitted_request import TitaniumSubmittedRequest
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_service_api.DataServiceApi(api_client)
    body = TitaniumSubmittedRequest(
        asset_id="asset_id_example",
        collapse_table_config=TitaniumCollapseTableRequest(
            filters=[
                TitaniumFilter(
                    key="key_example",
                    operator="operator_example",
                    value={},
                ),
            ],
        ),
        consensus_run_timestamp="consensus_run_timestamp_example",
        data_type="data_type_example",
        submitted_date="submitted_date_example",
        table_config=TitaniumTableRequest(
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
            filters=[
                TitaniumFilter(
                    key="key_example",
                    operator="operator_example",
                    value={},
                ),
            ],
            order_by=TitaniumOrderBy(
                column="column_example",
                order="order_example",
            ),
            page=TitaniumPage(
                page_number=1,
                size=1,
                total_number_of_elements="total_number_of_elements_example",
            ),
        ),
        trace_name="trace_name_example",
    ) # TitaniumSubmittedRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Submitted returns submitted data based on the request made.
        api_response = api_instance.data_service_submitted(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DataServiceApi->data_service_submitted: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumSubmittedRequest**](TitaniumSubmittedRequest.md)|  |

### Return type

[**TitaniumSubmittedResponse**](TitaniumSubmittedResponse.md)

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

# **data_service_upload_data**
> TitaniumUploadDataResponse data_service_upload_data(body)



### Example


```python
import time
import openapi_client
from openapi_client.api import data_service_api
from openapi_client.model.titanium_upload_data_request import TitaniumUploadDataRequest
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_upload_data_response import TitaniumUploadDataResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_service_api.DataServiceApi(api_client)
    body = TitaniumUploadDataRequest(
        annotation={},
        asset=TitaniumAssetDetails(
            asset_id="asset_id_example",
            date="date_example",
            name="name_example",
            service="service_example",
            snap_time="snap_time_example",
            sub_asset="sub_asset_example",
        ),
        client="client_example",
        description="description_example",
        file_name="file_name_example",
        mode="mode_example",
        protocol="protocol_example",
    ) # TitaniumUploadDataRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.data_service_upload_data(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DataServiceApi->data_service_upload_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumUploadDataRequest**](TitaniumUploadDataRequest.md)|  |

### Return type

[**TitaniumUploadDataResponse**](TitaniumUploadDataResponse.md)

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

# **data_service_upload_url**
> TitaniumUploadURLResponse data_service_upload_url(body)

UploadURL returns a pre-signed S3 URL for uploading data.

### Example


```python
import time
import openapi_client
from openapi_client.api import data_service_api
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_upload_url_request import TitaniumUploadURLRequest
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
    api_instance = data_service_api.DataServiceApi(api_client)
    body = TitaniumUploadURLRequest(
        asset_id="asset_id_example",
        client="client_example",
        date="date_example",
        descriptor_name="descriptor_name_example",
        file_annotation=[
            TitaniumFileAnnotation(
                annotation={},
                asset=TitaniumAssetDetails(
                    asset_id="asset_id_example",
                    date="date_example",
                    name="name_example",
                    service="service_example",
                    snap_time="snap_time_example",
                    sub_asset="sub_asset_example",
                ),
                chunks=[
                    TitaniumChunk(
                        annotation={},
                        chunk_id="chunk_id_example",
                        description="description_example",
                        original_file_name="original_file_name_example",
                        rows_count=1,
                        start_row=1,
                        user="user_example",
                    ),
                ],
                client="client_example",
                file_name="file_name_example",
                mode="mode_example",
                upload_time="upload_time_example",
            ),
        ],
        file_name="file_name_example",
        trace_name="trace_name_example",
    ) # TitaniumUploadURLRequest | 

    # example passing only required values which don't have defaults set
    try:
        # UploadURL returns a pre-signed S3 URL for uploading data.
        api_response = api_instance.data_service_upload_url(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DataServiceApi->data_service_upload_url: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumUploadURLRequest**](TitaniumUploadURLRequest.md)|  |

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

