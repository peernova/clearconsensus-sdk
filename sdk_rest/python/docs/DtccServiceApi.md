# openapi_client.DtccServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dtcc_service_get_dtcc_table**](DtccServiceApi.md#dtcc_service_get_dtcc_table) | **POST** /api/v1/dtcc/tab | 


# **dtcc_service_get_dtcc_table**
> TitaniumDtccTabResponse dtcc_service_get_dtcc_table(body)



### Example


```python
import time
import openapi_client
from openapi_client.api import dtcc_service_api
from openapi_client.model.titanium_dtcc_tab_request import TitaniumDtccTabRequest
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_dtcc_tab_response import TitaniumDtccTabResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = dtcc_service_api.DtccServiceApi(api_client)
    body = TitaniumDtccTabRequest(
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
        group_keys=TitaniumListOfKeys(
            list=[
                TitaniumKeyAndValue(
                    key="key_example",
                    value={},
                ),
            ],
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
        snap_date="snap_date_example",
        submission_id="submission_id_example",
        trace_name="trace_name_example",
    ) # TitaniumDtccTabRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.dtcc_service_get_dtcc_table(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DtccServiceApi->dtcc_service_get_dtcc_table: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumDtccTabRequest**](TitaniumDtccTabRequest.md)|  |

### Return type

[**TitaniumDtccTabResponse**](TitaniumDtccTabResponse.md)

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

