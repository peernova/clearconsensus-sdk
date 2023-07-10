# openapi_client.DataServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**data_service_authorize_upload**](DataServiceApi.md#data_service_authorize_upload) | **POST** /api/v1/internal/upload/authorize | AuthorizeUpload shows availability of uploading for user.
[**data_service_export**](DataServiceApi.md#data_service_export) | **POST** /api/v1/export | Export exports data according to the request.
[**data_service_notify_upload**](DataServiceApi.md#data_service_notify_upload) | **POST** /api/v1/internal/upload/notify | NotifyUpload returns message with notify that data was uploaded according to url in request.
[**data_service_submitted**](DataServiceApi.md#data_service_submitted) | **POST** /api/v1/submitted | Submitted returns submitted data based on the request made.
[**data_service_upload_url**](DataServiceApi.md#data_service_upload_url) | **POST** /api/v1/upload/url | UploadURL returns a pre-signed S3 URL for uploading data.


# **data_service_authorize_upload**
> TitaniumUploadAuthorizationResponse data_service_authorize_upload(body)

AuthorizeUpload shows availability of uploading for user.

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
    api_instance = openapi_client.DataServiceApi(api_client)
    body = openapi_client.TitaniumUploadURLRequest() # TitaniumUploadURLRequest | 

    try:
        # AuthorizeUpload shows availability of uploading for user.
        api_response = api_instance.data_service_authorize_upload(body)
        pprint(api_response)
    except ApiException as e:
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

# **data_service_export**
> TitaniumExportResponse data_service_export(body)

Export exports data according to the request.

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
    api_instance = openapi_client.DataServiceApi(api_client)
    body = openapi_client.TitaniumExportRequest() # TitaniumExportRequest | 

    try:
        # Export exports data according to the request.
        api_response = api_instance.data_service_export(body)
        pprint(api_response)
    except ApiException as e:
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
    api_instance = openapi_client.DataServiceApi(api_client)
    body = openapi_client.TitaniumUploadNotifyRequest() # TitaniumUploadNotifyRequest | 

    try:
        # NotifyUpload returns message with notify that data was uploaded according to url in request.
        api_response = api_instance.data_service_notify_upload(body)
        pprint(api_response)
    except ApiException as e:
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
    api_instance = openapi_client.DataServiceApi(api_client)
    body = openapi_client.TitaniumSubmittedRequest() # TitaniumSubmittedRequest | 

    try:
        # Submitted returns submitted data based on the request made.
        api_response = api_instance.data_service_submitted(body)
        pprint(api_response)
    except ApiException as e:
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

# **data_service_upload_url**
> TitaniumUploadURLResponse data_service_upload_url(body)

UploadURL returns a pre-signed S3 URL for uploading data.

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
    api_instance = openapi_client.DataServiceApi(api_client)
    body = openapi_client.TitaniumUploadURLRequest() # TitaniumUploadURLRequest | 

    try:
        # UploadURL returns a pre-signed S3 URL for uploading data.
        api_response = api_instance.data_service_upload_url(body)
        pprint(api_response)
    except ApiException as e:
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

