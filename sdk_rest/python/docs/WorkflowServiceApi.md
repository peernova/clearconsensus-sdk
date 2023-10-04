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
import time
import openapi_client
from openapi_client.api import workflow_service_api
from openapi_client.model.titanium_add_workflow_definition_request import TitaniumAddWorkflowDefinitionRequest
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_acknowledge_response import TitaniumAcknowledgeResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = workflow_service_api.WorkflowServiceApi(api_client)
    body = TitaniumAddWorkflowDefinitionRequest(
        definition=TitaniumWorkflowDefinition(
            action_list=[
                TitaniumActionDefinition(
                    action_type="action_type_example",
                    depends_on=[
                        "depends_on_example",
                    ],
                    do_not_run_if="do_not_run_if_example",
                    id="id_example",
                    ignore_failure=True,
                    input_arguments=[
                        TitaniumArgument(
                            definition="definition_example",
                            name="name_example",
                            value={},
                            variable="variable_example",
                        ),
                    ],
                    output_argument="output_argument_example",
                    queue="queue_example",
                    retries=1,
                    run_if="run_if_example",
                    timeout_seconds=1,
                ),
            ],
            max_attempts=1,
            predefined_arguments={},
            runtime_arguments=[
                "runtime_arguments_example",
            ],
            schedule="schedule_example",
            timeout="timeout_example",
            workflow_name="workflow_name_example",
            workflow_queue="workflow_queue_example",
        ),
        scope="scope_example",
    ) # TitaniumAddWorkflowDefinitionRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.workflow_service_add_workflow(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
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
import time
import openapi_client
from openapi_client.api import workflow_service_api
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_enable_disable_request import TitaniumEnableDisableRequest
from openapi_client.model.titanium_acknowledge_response import TitaniumAcknowledgeResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = workflow_service_api.WorkflowServiceApi(api_client)
    body = TitaniumEnableDisableRequest(
        name="name_example",
        scope="scope_example",
    ) # TitaniumEnableDisableRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.workflow_service_disable_workflow(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
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
import time
import openapi_client
from openapi_client.api import workflow_service_api
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_enable_disable_request import TitaniumEnableDisableRequest
from openapi_client.model.titanium_acknowledge_response import TitaniumAcknowledgeResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = workflow_service_api.WorkflowServiceApi(api_client)
    body = TitaniumEnableDisableRequest(
        name="name_example",
        scope="scope_example",
    ) # TitaniumEnableDisableRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.workflow_service_enable_workflow(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
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
import time
import openapi_client
from openapi_client.api import workflow_service_api
from openapi_client.model.titanium_get_definition import TitaniumGetDefinition
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_workflow_definition_response import TitaniumWorkflowDefinitionResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = workflow_service_api.WorkflowServiceApi(api_client)
    body = TitaniumGetDefinition(
        descriptor_name="descriptor_name_example",
        identifier=TitaniumIdentifier(
            name="name_example",
            uid="uid_example",
        ),
        scope="scope_example",
    ) # TitaniumGetDefinition | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.workflow_service_get_workflow(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
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
import time
import openapi_client
from openapi_client.api import workflow_service_api
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_get_workflow_action_response import TitaniumGetWorkflowActionResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = workflow_service_api.WorkflowServiceApi(api_client)
    name = "name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.workflow_service_get_workflow_action(name)
        pprint(api_response)
    except openapi_client.ApiException as e:
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
import time
import openapi_client
from openapi_client.api import workflow_service_api
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_workflow_list import TitaniumWorkflowList
from openapi_client.model.titanium_list_request import TitaniumListRequest
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = workflow_service_api.WorkflowServiceApi(api_client)
    body = TitaniumListRequest(
        filter="filter_example",
        limit=TitaniumLimit(
            value=1,
        ),
        offset=1,
        order_by=TitaniumOrderBy(
            column="column_example",
            order="order_example",
        ),
        scope="scope_example",
    ) # TitaniumListRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.workflow_service_list_workflow_actions(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
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
import time
import openapi_client
from openapi_client.api import workflow_service_api
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_workflow_list import TitaniumWorkflowList
from openapi_client.model.titanium_list_request import TitaniumListRequest
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = workflow_service_api.WorkflowServiceApi(api_client)
    body = TitaniumListRequest(
        filter="filter_example",
        limit=TitaniumLimit(
            value=1,
        ),
        offset=1,
        order_by=TitaniumOrderBy(
            column="column_example",
            order="order_example",
        ),
        scope="scope_example",
    ) # TitaniumListRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.workflow_service_list_workflows(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
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
import time
import openapi_client
from openapi_client.api import workflow_service_api
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_run_workflow_response import TitaniumRunWorkflowResponse
from openapi_client.model.titanium_reprocess_workflow_request import TitaniumReprocessWorkflowRequest
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = workflow_service_api.WorkflowServiceApi(api_client)
    body = TitaniumReprocessWorkflowRequest(
        run_id="run_id_example",
        workflow_id="workflow_id_example",
    ) # TitaniumReprocessWorkflowRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.workflow_service_reprocess_workflow(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
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
import time
import openapi_client
from openapi_client.api import workflow_service_api
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_run_workflow_response import TitaniumRunWorkflowResponse
from openapi_client.model.titanium_run_workflow_request import TitaniumRunWorkflowRequest
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = workflow_service_api.WorkflowServiceApi(api_client)
    body = TitaniumRunWorkflowRequest(
        args={},
        name="name_example",
        scope="scope_example",
    ) # TitaniumRunWorkflowRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.workflow_service_run_workflow(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
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

