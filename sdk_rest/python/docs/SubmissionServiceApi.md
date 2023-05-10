# openapi_client.SubmissionServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**submission_service_get_files_view**](SubmissionServiceApi.md#submission_service_get_files_view) | **POST** /api/v1/submission/files-view | GetFilesView returns information about submitted to s3 storage files.


# **submission_service_get_files_view**
> TitaniumGetSubmissionFilesResponse submission_service_get_files_view(body)

GetFilesView returns information about submitted to s3 storage files.

### Example


```python
import time
import openapi_client
from openapi_client.api import submission_service_api
from openapi_client.model.titanium_get_submission_files_request import TitaniumGetSubmissionFilesRequest
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_get_submission_files_response import TitaniumGetSubmissionFilesResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = submission_service_api.SubmissionServiceApi(api_client)
    body = TitaniumGetSubmissionFilesRequest(
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
        snap_date_from="snap_date_from_example",
        snap_date_to="snap_date_to_example",
        trace_name="trace_name_example",
    ) # TitaniumGetSubmissionFilesRequest | 

    # example passing only required values which don't have defaults set
    try:
        # GetFilesView returns information about submitted to s3 storage files.
        api_response = api_instance.submission_service_get_files_view(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SubmissionServiceApi->submission_service_get_files_view: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumGetSubmissionFilesRequest**](TitaniumGetSubmissionFilesRequest.md)|  |

### Return type

[**TitaniumGetSubmissionFilesResponse**](TitaniumGetSubmissionFilesResponse.md)

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

