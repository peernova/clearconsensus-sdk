# openapi_client.OutliersServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**outliers_service_outliers**](OutliersServiceApi.md#outliers_service_outliers) | **POST** /api/v1/outliers | Outliers returns outliers according to request.


# **outliers_service_outliers**
> TitaniumOutliersResponse outliers_service_outliers(body)

Outliers returns outliers according to request.

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
    api_instance = openapi_client.OutliersServiceApi(api_client)
    body = openapi_client.TitaniumOutliersRequest() # TitaniumOutliersRequest | 

    try:
        # Outliers returns outliers according to request.
        api_response = api_instance.outliers_service_outliers(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OutliersServiceApi->outliers_service_outliers: %s\n" % e)
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

