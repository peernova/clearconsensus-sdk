# openapi_client.ChallengeServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**challenge_service_challenge_create**](ChallengeServiceApi.md#challenge_service_challenge_create) | **POST** /api/v1/challenge/create | ChallengeCreate creates challenge in the system.(Initiate process by dealer) To create \&quot;challenger\&quot; needs to be authorised and challenge can be created only if one of their own submitted data points has been declared an outlier in the published Consensus. Need to specify asset and fill out evidence information. Returns response that contains ticket ID of the Challenge or the Error.
[**challenge_service_challenge_form_meta**](ChallengeServiceApi.md#challenge_service_challenge_form_meta) | **POST** /api/v1/challenge/form-meta | ChallengeFormMeta is used to request information(template) about the form fields required to submit a challenge for a specific asset and evidence type. Returns response with template with pre-filled data.
[**challenge_service_challenge_freeze_status**](ChallengeServiceApi.md#challenge_service_challenge_freeze_status) | **POST** /api/v1/challenge/freeze/status | ChallengeFreezeStatus returns StatusResponse that contains string that represents freeze status of challenges if the challenge process is stopped and nothing if the one is not. Challenge can be stopped by operator.Dealer can see the freeze status using this method. Need to specify consensus(where outliers exists) run timestamp.
[**challenge_service_get_challenge_attachment_upload_url**](ChallengeServiceApi.md#challenge_service_get_challenge_attachment_upload_url) | **POST** /api/v1/challenge/attachment_upload_urls | GetChallengeAttachmentUploadUrl returns string that represents s3 URL that can be used to upload attachment for the challenge. The file in attachment can be any file that provides additional information about the disputable outlier. Need to specify asset ID, submitted ID and file name.
[**challenge_service_get_challenge_details**](ChallengeServiceApi.md#challenge_service_get_challenge_details) | **POST** /api/v1/challenge-details | 


# **challenge_service_challenge_create**
> TitaniumChallengeCreateResponse challenge_service_challenge_create(body)

ChallengeCreate creates challenge in the system.(Initiate process by dealer) To create \"challenger\" needs to be authorised and challenge can be created only if one of their own submitted data points has been declared an outlier in the published Consensus. Need to specify asset and fill out evidence information. Returns response that contains ticket ID of the Challenge or the Error.

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
    api_instance = openapi_client.ChallengeServiceApi(api_client)
    body = openapi_client.TitaniumChallengeCreateRequest() # TitaniumChallengeCreateRequest | 

    try:
        # ChallengeCreate creates challenge in the system.(Initiate process by dealer) To create \"challenger\" needs to be authorised and challenge can be created only if one of their own submitted data points has been declared an outlier in the published Consensus. Need to specify asset and fill out evidence information. Returns response that contains ticket ID of the Challenge or the Error.
        api_response = api_instance.challenge_service_challenge_create(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChallengeServiceApi->challenge_service_challenge_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumChallengeCreateRequest**](TitaniumChallengeCreateRequest.md)|  | 

### Return type

[**TitaniumChallengeCreateResponse**](TitaniumChallengeCreateResponse.md)

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

# **challenge_service_challenge_form_meta**
> TitaniumChallengeFormMetaResponse challenge_service_challenge_form_meta(body)

ChallengeFormMeta is used to request information(template) about the form fields required to submit a challenge for a specific asset and evidence type. Returns response with template with pre-filled data.

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
    api_instance = openapi_client.ChallengeServiceApi(api_client)
    body = openapi_client.TitaniumChallengeFormMetaRequest() # TitaniumChallengeFormMetaRequest | 

    try:
        # ChallengeFormMeta is used to request information(template) about the form fields required to submit a challenge for a specific asset and evidence type. Returns response with template with pre-filled data.
        api_response = api_instance.challenge_service_challenge_form_meta(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChallengeServiceApi->challenge_service_challenge_form_meta: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumChallengeFormMetaRequest**](TitaniumChallengeFormMetaRequest.md)|  | 

### Return type

[**TitaniumChallengeFormMetaResponse**](TitaniumChallengeFormMetaResponse.md)

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

# **challenge_service_challenge_freeze_status**
> TitaniumStatusResponse challenge_service_challenge_freeze_status(body)

ChallengeFreezeStatus returns StatusResponse that contains string that represents freeze status of challenges if the challenge process is stopped and nothing if the one is not. Challenge can be stopped by operator.Dealer can see the freeze status using this method. Need to specify consensus(where outliers exists) run timestamp.

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
    api_instance = openapi_client.ChallengeServiceApi(api_client)
    body = openapi_client.TitaniumChallengeFreezeStatusRequest() # TitaniumChallengeFreezeStatusRequest | 

    try:
        # ChallengeFreezeStatus returns StatusResponse that contains string that represents freeze status of challenges if the challenge process is stopped and nothing if the one is not. Challenge can be stopped by operator.Dealer can see the freeze status using this method. Need to specify consensus(where outliers exists) run timestamp.
        api_response = api_instance.challenge_service_challenge_freeze_status(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChallengeServiceApi->challenge_service_challenge_freeze_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumChallengeFreezeStatusRequest**](TitaniumChallengeFreezeStatusRequest.md)|  | 

### Return type

[**TitaniumStatusResponse**](TitaniumStatusResponse.md)

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

# **challenge_service_get_challenge_attachment_upload_url**
> TitaniumGetAttachmentUploadUrlResponse challenge_service_get_challenge_attachment_upload_url(body)

GetChallengeAttachmentUploadUrl returns string that represents s3 URL that can be used to upload attachment for the challenge. The file in attachment can be any file that provides additional information about the disputable outlier. Need to specify asset ID, submitted ID and file name.

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
    api_instance = openapi_client.ChallengeServiceApi(api_client)
    body = openapi_client.TitaniumGetAttachmentUploadUrlRequest() # TitaniumGetAttachmentUploadUrlRequest | 

    try:
        # GetChallengeAttachmentUploadUrl returns string that represents s3 URL that can be used to upload attachment for the challenge. The file in attachment can be any file that provides additional information about the disputable outlier. Need to specify asset ID, submitted ID and file name.
        api_response = api_instance.challenge_service_get_challenge_attachment_upload_url(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChallengeServiceApi->challenge_service_get_challenge_attachment_upload_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumGetAttachmentUploadUrlRequest**](TitaniumGetAttachmentUploadUrlRequest.md)|  | 

### Return type

[**TitaniumGetAttachmentUploadUrlResponse**](TitaniumGetAttachmentUploadUrlResponse.md)

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

# **challenge_service_get_challenge_details**
> TitaniumGetChallengeDetailsResponse challenge_service_get_challenge_details(body)



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
    api_instance = openapi_client.ChallengeServiceApi(api_client)
    body = openapi_client.TitaniumGetChallengeDetailsRequest() # TitaniumGetChallengeDetailsRequest | 

    try:
        api_response = api_instance.challenge_service_get_challenge_details(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChallengeServiceApi->challenge_service_get_challenge_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumGetChallengeDetailsRequest**](TitaniumGetChallengeDetailsRequest.md)|  | 

### Return type

[**TitaniumGetChallengeDetailsResponse**](TitaniumGetChallengeDetailsResponse.md)

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

