# openapi_client.FileServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**file_service_file_history**](FileServiceApi.md#file_service_file_history) | **POST** /api/v1/file-history | FileHistory retrieves the history for a specified file.
[**file_service_file_submission**](FileServiceApi.md#file_service_file_submission) | **POST** /api/v1/file-submission | FileSubmission submits a file for processing.
[**file_service_get_file_delimiter**](FileServiceApi.md#file_service_get_file_delimiter) | **POST** /api/v1/import/{filename}/delimiter | GetFileDelimiter retrieves the delimiter for a specified file.
[**file_service_get_file_descriptor**](FileServiceApi.md#file_service_get_file_descriptor) | **POST** /api/v1/import/{filename}/descriptor | GetFileDescriptor retrieves the descriptor for a specified file.
[**file_service_get_file_export_url**](FileServiceApi.md#file_service_get_file_export_url) | **POST** /api/v1/raw-file | GetFileExportUrl retrieves the export URL for a specified file.
[**file_service_get_file_preview**](FileServiceApi.md#file_service_get_file_preview) | **POST** /api/v1/import/{filename} | GetFilePreview retrieves a preview of a specified file.
[**file_service_list_files**](FileServiceApi.md#file_service_list_files) | **POST** /api/v1/import/list | ListFiles retrieves a list of files.
[**file_service_set_file_delimiter**](FileServiceApi.md#file_service_set_file_delimiter) | **POST** /api/v1/import/{fileIdentifier.filename}/delimiter | SetFileDelimiter sets the delimiter for a specified file.
[**file_service_set_file_descriptor**](FileServiceApi.md#file_service_set_file_descriptor) | **POST** /api/v1/import/{fileIdentifier.filename}/descriptor | SetFileDescriptor sets the descriptor for a specified file.


# **file_service_file_history**
> TitaniumFileHistoryResponse file_service_file_history(body)

FileHistory retrieves the history for a specified file.

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
    api_instance = openapi_client.FileServiceApi(api_client)
    body = openapi_client.TitaniumFileHistoryRequest() # TitaniumFileHistoryRequest | 

    try:
        # FileHistory retrieves the history for a specified file.
        api_response = api_instance.file_service_file_history(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FileServiceApi->file_service_file_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumFileHistoryRequest**](TitaniumFileHistoryRequest.md)|  | 

### Return type

[**TitaniumFileHistoryResponse**](TitaniumFileHistoryResponse.md)

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

# **file_service_file_submission**
> TitaniumMessageResponse file_service_file_submission(body)

FileSubmission submits a file for processing.

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
    api_instance = openapi_client.FileServiceApi(api_client)
    body = openapi_client.TitaniumFileSubmissionRequest() # TitaniumFileSubmissionRequest | 

    try:
        # FileSubmission submits a file for processing.
        api_response = api_instance.file_service_file_submission(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FileServiceApi->file_service_file_submission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumFileSubmissionRequest**](TitaniumFileSubmissionRequest.md)|  | 

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

# **file_service_get_file_delimiter**
> TitaniumFileDelimiterSetting file_service_get_file_delimiter(filename, body)

GetFileDelimiter retrieves the delimiter for a specified file.

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
    api_instance = openapi_client.FileServiceApi(api_client)
    filename = 'filename_example' # str | 
body = openapi_client.FileServiceGetFilePreviewRequest() # FileServiceGetFilePreviewRequest | 

    try:
        # GetFileDelimiter retrieves the delimiter for a specified file.
        api_response = api_instance.file_service_get_file_delimiter(filename, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FileServiceApi->file_service_get_file_delimiter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filename** | **str**|  | 
 **body** | [**FileServiceGetFilePreviewRequest**](FileServiceGetFilePreviewRequest.md)|  | 

### Return type

[**TitaniumFileDelimiterSetting**](TitaniumFileDelimiterSetting.md)

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

# **file_service_get_file_descriptor**
> TitaniumFileDescriptorSetting file_service_get_file_descriptor(filename, body)

GetFileDescriptor retrieves the descriptor for a specified file.

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
    api_instance = openapi_client.FileServiceApi(api_client)
    filename = 'filename_example' # str | 
body = openapi_client.FileServiceGetFilePreviewRequest() # FileServiceGetFilePreviewRequest | 

    try:
        # GetFileDescriptor retrieves the descriptor for a specified file.
        api_response = api_instance.file_service_get_file_descriptor(filename, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FileServiceApi->file_service_get_file_descriptor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filename** | **str**|  | 
 **body** | [**FileServiceGetFilePreviewRequest**](FileServiceGetFilePreviewRequest.md)|  | 

### Return type

[**TitaniumFileDescriptorSetting**](TitaniumFileDescriptorSetting.md)

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

# **file_service_get_file_export_url**
> TitaniumGetFileExportUrlResponse file_service_get_file_export_url(body)

GetFileExportUrl retrieves the export URL for a specified file.

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
    api_instance = openapi_client.FileServiceApi(api_client)
    body = openapi_client.TitaniumGetFileExportUrlRequest() # TitaniumGetFileExportUrlRequest | 

    try:
        # GetFileExportUrl retrieves the export URL for a specified file.
        api_response = api_instance.file_service_get_file_export_url(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FileServiceApi->file_service_get_file_export_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumGetFileExportUrlRequest**](TitaniumGetFileExportUrlRequest.md)|  | 

### Return type

[**TitaniumGetFileExportUrlResponse**](TitaniumGetFileExportUrlResponse.md)

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

# **file_service_get_file_preview**
> TitaniumFilePreview file_service_get_file_preview(filename, body)

GetFilePreview retrieves a preview of a specified file.

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
    api_instance = openapi_client.FileServiceApi(api_client)
    filename = 'filename_example' # str | 
body = openapi_client.FileServiceGetFilePreviewRequest() # FileServiceGetFilePreviewRequest | 

    try:
        # GetFilePreview retrieves a preview of a specified file.
        api_response = api_instance.file_service_get_file_preview(filename, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FileServiceApi->file_service_get_file_preview: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filename** | **str**|  | 
 **body** | [**FileServiceGetFilePreviewRequest**](FileServiceGetFilePreviewRequest.md)|  | 

### Return type

[**TitaniumFilePreview**](TitaniumFilePreview.md)

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

# **file_service_list_files**
> TitaniumFileList file_service_list_files(body)

ListFiles retrieves a list of files.

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
    api_instance = openapi_client.FileServiceApi(api_client)
    body = openapi_client.TitaniumListRequest() # TitaniumListRequest | 

    try:
        # ListFiles retrieves a list of files.
        api_response = api_instance.file_service_list_files(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FileServiceApi->file_service_list_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumListRequest**](TitaniumListRequest.md)|  | 

### Return type

[**TitaniumFileList**](TitaniumFileList.md)

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

# **file_service_set_file_delimiter**
> object file_service_set_file_delimiter(file_identifier_filename, body)

SetFileDelimiter sets the delimiter for a specified file.

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
    api_instance = openapi_client.FileServiceApi(api_client)
    file_identifier_filename = 'file_identifier_filename_example' # str | 
body = openapi_client.TitaniumSetFileDelimiterRequest() # TitaniumSetFileDelimiterRequest | 

    try:
        # SetFileDelimiter sets the delimiter for a specified file.
        api_response = api_instance.file_service_set_file_delimiter(file_identifier_filename, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FileServiceApi->file_service_set_file_delimiter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_identifier_filename** | **str**|  | 
 **body** | [**TitaniumSetFileDelimiterRequest**](TitaniumSetFileDelimiterRequest.md)|  | 

### Return type

**object**

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

# **file_service_set_file_descriptor**
> object file_service_set_file_descriptor(file_identifier_filename, body)

SetFileDescriptor sets the descriptor for a specified file.

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
    api_instance = openapi_client.FileServiceApi(api_client)
    file_identifier_filename = 'file_identifier_filename_example' # str | 
body = openapi_client.TitaniumSetFileDescriptorRequest() # TitaniumSetFileDescriptorRequest | 

    try:
        # SetFileDescriptor sets the descriptor for a specified file.
        api_response = api_instance.file_service_set_file_descriptor(file_identifier_filename, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FileServiceApi->file_service_set_file_descriptor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_identifier_filename** | **str**|  | 
 **body** | [**TitaniumSetFileDescriptorRequest**](TitaniumSetFileDescriptorRequest.md)|  | 

### Return type

**object**

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

