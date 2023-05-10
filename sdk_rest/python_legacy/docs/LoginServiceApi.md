# openapi_client.LoginServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login_service_login**](LoginServiceApi.md#login_service_login) | **POST** /api/v1/login | 


# **login_service_login**
> TitaniumLoginResponse login_service_login(body)



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
    api_instance = openapi_client.LoginServiceApi(api_client)
    body = openapi_client.TitaniumLoginRequest() # TitaniumLoginRequest | 

    try:
        api_response = api_instance.login_service_login(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LoginServiceApi->login_service_login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumLoginRequest**](TitaniumLoginRequest.md)|  | 

### Return type

[**TitaniumLoginResponse**](TitaniumLoginResponse.md)

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

