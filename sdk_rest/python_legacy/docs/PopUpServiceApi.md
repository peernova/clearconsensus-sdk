# openapi_client.PopUpServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pop_up_service_pop_up_view**](PopUpServiceApi.md#pop_up_service_pop_up_view) | **POST** /api/v1/popup-view | PopUpView returns information according to request for the popup view.


# **pop_up_service_pop_up_view**
> TitaniumPopUpViewResponse pop_up_service_pop_up_view(body)

PopUpView returns information according to request for the popup view.

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
    api_instance = openapi_client.PopUpServiceApi(api_client)
    body = openapi_client.TitaniumPopUpViewRequest() # TitaniumPopUpViewRequest | 

    try:
        # PopUpView returns information according to request for the popup view.
        api_response = api_instance.pop_up_service_pop_up_view(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PopUpServiceApi->pop_up_service_pop_up_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumPopUpViewRequest**](TitaniumPopUpViewRequest.md)|  | 

### Return type

[**TitaniumPopUpViewResponse**](TitaniumPopUpViewResponse.md)

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

