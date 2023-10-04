# openapi_client.WorkflowServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workflow_service_add_workflow**](WorkflowServiceApi.md#workflow_service_add_workflow) | **POST** /api/v1/workflow/add | 
[**workflow_service_disable_workflow**](WorkflowServiceApi.md#workflow_service_disable_workflow) | **POST** /api/v1/workflow/disable | 
[**workflow_service_enable_workflow**](WorkflowServiceApi.md#workflow_service_enable_workflow) | **POST** /api/v1/workflow/enable | 
[**workflow_service_get_workflow**](WorkflowServiceApi.md#workflow_service_get_workflow) | **POST** /api/v1/workflow/get | 
[**workflow_service_get_workflow_action**](WorkflowServiceApi.md#workflow_service_get_workflow_action) | **GET** /api/v1/workflow/action/{name} | 
[**workflow_service_list_workflow_actions**](WorkflowServiceApi.md#workflow_service_list_workflow_actions) | **POST** /api/v1/workflow/action/list | 
[**workflow_service_list_workflows**](WorkflowServiceApi.md#workflow_service_list_workflows) | **POST** /api/v1/workflow/list | 
[**workflow_service_reprocess_workflow**](WorkflowServiceApi.md#workflow_service_reprocess_workflow) | **POST** /api/v1/workflow/reprocess | 
[**workflow_service_run_workflow**](WorkflowServiceApi.md#workflow_service_run_workflow) | **POST** /api/v1/workflow/run | 


# **workflow_service_add_workflow**
> TitaniumAcknowledgeResponse workflow_service_add_workflow(body)



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
    api_instance = openapi_client.WorkflowServiceApi(api_client)
    body = openapi_client.TitaniumAddWorkflowDefinitionRequest() # TitaniumAddWorkflowDefinitionRequest | 

    try:
        api_response = api_instance.workflow_service_add_workflow(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->workflow_service_add_workflow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumAddWorkflowDefinitionRequest**](TitaniumAddWorkflowDefinitionRequest.md)|  | 

### Return type

[**TitaniumAcknowledgeResponse**](TitaniumAcknowledgeResponse.md)

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

# **workflow_service_disable_workflow**
> TitaniumAcknowledgeResponse workflow_service_disable_workflow(body)



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
    api_instance = openapi_client.WorkflowServiceApi(api_client)
    body = openapi_client.TitaniumEnableDisableRequest() # TitaniumEnableDisableRequest | 

    try:
        api_response = api_instance.workflow_service_disable_workflow(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->workflow_service_disable_workflow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumEnableDisableRequest**](TitaniumEnableDisableRequest.md)|  | 

### Return type

[**TitaniumAcknowledgeResponse**](TitaniumAcknowledgeResponse.md)

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

# **workflow_service_enable_workflow**
> TitaniumAcknowledgeResponse workflow_service_enable_workflow(body)



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
    api_instance = openapi_client.WorkflowServiceApi(api_client)
    body = openapi_client.TitaniumEnableDisableRequest() # TitaniumEnableDisableRequest | 

    try:
        api_response = api_instance.workflow_service_enable_workflow(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->workflow_service_enable_workflow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumEnableDisableRequest**](TitaniumEnableDisableRequest.md)|  | 

### Return type

[**TitaniumAcknowledgeResponse**](TitaniumAcknowledgeResponse.md)

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

# **workflow_service_get_workflow**
> TitaniumWorkflowDefinitionResponse workflow_service_get_workflow(body)



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
    api_instance = openapi_client.WorkflowServiceApi(api_client)
    body = openapi_client.TitaniumGetDefinition() # TitaniumGetDefinition | 

    try:
        api_response = api_instance.workflow_service_get_workflow(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->workflow_service_get_workflow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumGetDefinition**](TitaniumGetDefinition.md)|  | 

### Return type

[**TitaniumWorkflowDefinitionResponse**](TitaniumWorkflowDefinitionResponse.md)

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

# **workflow_service_get_workflow_action**
> TitaniumGetWorkflowActionResponse workflow_service_get_workflow_action(name)



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
    api_instance = openapi_client.WorkflowServiceApi(api_client)
    name = 'name_example' # str | 

    try:
        api_response = api_instance.workflow_service_get_workflow_action(name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->workflow_service_get_workflow_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**TitaniumGetWorkflowActionResponse**](TitaniumGetWorkflowActionResponse.md)

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

# **workflow_service_list_workflow_actions**
> TitaniumWorkflowList workflow_service_list_workflow_actions(body)



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
    api_instance = openapi_client.WorkflowServiceApi(api_client)
    body = openapi_client.TitaniumListRequest() # TitaniumListRequest | 

    try:
        api_response = api_instance.workflow_service_list_workflow_actions(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->workflow_service_list_workflow_actions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumListRequest**](TitaniumListRequest.md)|  | 

### Return type

[**TitaniumWorkflowList**](TitaniumWorkflowList.md)

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

# **workflow_service_list_workflows**
> TitaniumWorkflowList workflow_service_list_workflows(body)



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
    api_instance = openapi_client.WorkflowServiceApi(api_client)
    body = openapi_client.TitaniumListRequest() # TitaniumListRequest | 

    try:
        api_response = api_instance.workflow_service_list_workflows(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->workflow_service_list_workflows: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumListRequest**](TitaniumListRequest.md)|  | 

### Return type

[**TitaniumWorkflowList**](TitaniumWorkflowList.md)

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

# **workflow_service_reprocess_workflow**
> TitaniumRunWorkflowResponse workflow_service_reprocess_workflow(body)



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
    api_instance = openapi_client.WorkflowServiceApi(api_client)
    body = openapi_client.TitaniumReprocessWorkflowRequest() # TitaniumReprocessWorkflowRequest | 

    try:
        api_response = api_instance.workflow_service_reprocess_workflow(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->workflow_service_reprocess_workflow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumReprocessWorkflowRequest**](TitaniumReprocessWorkflowRequest.md)|  | 

### Return type

[**TitaniumRunWorkflowResponse**](TitaniumRunWorkflowResponse.md)

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

# **workflow_service_run_workflow**
> TitaniumRunWorkflowResponse workflow_service_run_workflow(body)



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
    api_instance = openapi_client.WorkflowServiceApi(api_client)
    body = openapi_client.TitaniumRunWorkflowRequest() # TitaniumRunWorkflowRequest | 

    try:
        api_response = api_instance.workflow_service_run_workflow(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->workflow_service_run_workflow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumRunWorkflowRequest**](TitaniumRunWorkflowRequest.md)|  | 

### Return type

[**TitaniumRunWorkflowResponse**](TitaniumRunWorkflowResponse.md)

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

