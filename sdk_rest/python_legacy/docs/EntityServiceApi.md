# openapi_client.EntityServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**entity_service_create**](EntityServiceApi.md#entity_service_create) | **POST** /api/v1/user-management/entities/create | 
[**entity_service_find**](EntityServiceApi.md#entity_service_find) | **POST** /api/v1/user-management/entities | 
[**entity_service_get_all_enabled_only**](EntityServiceApi.md#entity_service_get_all_enabled_only) | **GET** /api/v1/user-management/entities | 
[**entity_service_get_by_id**](EntityServiceApi.md#entity_service_get_by_id) | **GET** /api/v1/user-management/entities/{id} | 
[**entity_service_update**](EntityServiceApi.md#entity_service_update) | **PUT** /api/v1/user-management/entities/{id} | 


# **entity_service_create**
> ProtoEntityResponse entity_service_create(body)



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
    api_instance = openapi_client.EntityServiceApi(api_client)
    body = openapi_client.ProtoEntityDto() # ProtoEntityDto | 

    try:
        api_response = api_instance.entity_service_create(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EntityServiceApi->entity_service_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProtoEntityDto**](ProtoEntityDto.md)|  | 

### Return type

[**ProtoEntityResponse**](ProtoEntityResponse.md)

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

# **entity_service_find**
> ProtoTableResponse entity_service_find(body)



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
    api_instance = openapi_client.EntityServiceApi(api_client)
    body = openapi_client.ProtoSearchCriteria() # ProtoSearchCriteria | 

    try:
        api_response = api_instance.entity_service_find(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EntityServiceApi->entity_service_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProtoSearchCriteria**](ProtoSearchCriteria.md)|  | 

### Return type

[**ProtoTableResponse**](ProtoTableResponse.md)

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

# **entity_service_get_all_enabled_only**
> ProtoEntitiesResponse entity_service_get_all_enabled_only()



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
    api_instance = openapi_client.EntityServiceApi(api_client)
    
    try:
        api_response = api_instance.entity_service_get_all_enabled_only()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EntityServiceApi->entity_service_get_all_enabled_only: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ProtoEntitiesResponse**](ProtoEntitiesResponse.md)

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

# **entity_service_get_by_id**
> ProtoEntityResponse entity_service_get_by_id(id)



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
    api_instance = openapi_client.EntityServiceApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.entity_service_get_by_id(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EntityServiceApi->entity_service_get_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ProtoEntityResponse**](ProtoEntityResponse.md)

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

# **entity_service_update**
> ProtoEntityResponse entity_service_update(id, body)



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
    api_instance = openapi_client.EntityServiceApi(api_client)
    id = 'id_example' # str | 
body = openapi_client.EntityServiceUpdateRequest() # EntityServiceUpdateRequest | 

    try:
        api_response = api_instance.entity_service_update(id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EntityServiceApi->entity_service_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**EntityServiceUpdateRequest**](EntityServiceUpdateRequest.md)|  | 

### Return type

[**ProtoEntityResponse**](ProtoEntityResponse.md)

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

