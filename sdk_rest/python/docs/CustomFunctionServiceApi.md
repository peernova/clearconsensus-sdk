# openapi_client.CustomFunctionServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**custom_function_service_add_custom_function**](CustomFunctionServiceApi.md#custom_function_service_add_custom_function) | **POST** /api/v1/customfunction/add | AddCustomFunction allows the user to create a new custom function by sending a CustomFunction message. It returns an AcknowledgeResponse indicating whether the custom function was successfully added or not.
[**custom_function_service_get_custom_function**](CustomFunctionServiceApi.md#custom_function_service_get_custom_function) | **POST** /api/v1/customfunction/get | GetCustomFunction retrieves the definition of a specific custom function. The custom function is specified in the CustomFunctionGetDefinition message, which includes its ID and scope. The method returns a CustomFunctionDefinitionResponse that contains either the custom function definition or an error.
[**custom_function_service_list_custom_function_versions**](CustomFunctionServiceApi.md#custom_function_service_list_custom_function_versions) | **POST** /api/v1/customfunction/versions | ListCustomFunctionVersions lists all the versions of a specific custom function. The custom function is specified in the GetDefinition message, which includes its ID and scope. The method returns a ListVersionResponse that contains either a list of versions or an error.
[**custom_function_service_list_custom_functions**](CustomFunctionServiceApi.md#custom_function_service_list_custom_functions) | **POST** /api/v1/customfunction/list | ListCustomFunctions lists all the custom functions that match the specified criteria. The criteria are defined in the ListCustomFunctionRequest message, which includes the descriptor name and the type of the custom function descriptor. The method returns a ListCustomFunctionResponse that contains either a list of custom functions or an error.


# **custom_function_service_add_custom_function**
> TitaniumAcknowledgeResponse custom_function_service_add_custom_function(body)

AddCustomFunction allows the user to create a new custom function by sending a CustomFunction message. It returns an AcknowledgeResponse indicating whether the custom function was successfully added or not.

### Example


```python
import time
import openapi_client
from openapi_client.api import custom_function_service_api
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_custom_function import TitaniumCustomFunction
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
    api_instance = custom_function_service_api.CustomFunctionServiceApi(api_client)
    body = TitaniumCustomFunction(
        category="category_example",
        definition="definition_example",
        descriptor_name="descriptor_name_example",
        descriptor_type="descriptor_type_example",
        name="name_example",
        output_type="output_type_example",
        scope="scope_example",
        uid="uid_example",
        usages=[
            TitaniumCustomFunctionUsage(
                identifier=TitaniumIdentifier(
                    name="name_example",
                    uid="uid_example",
                ),
                type="type_example",
            ),
        ],
    ) # TitaniumCustomFunction | 

    # example passing only required values which don't have defaults set
    try:
        # AddCustomFunction allows the user to create a new custom function by sending a CustomFunction message. It returns an AcknowledgeResponse indicating whether the custom function was successfully added or not.
        api_response = api_instance.custom_function_service_add_custom_function(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CustomFunctionServiceApi->custom_function_service_add_custom_function: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumCustomFunction**](TitaniumCustomFunction.md)|  |

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

# **custom_function_service_get_custom_function**
> TitaniumCustomFunctionDefinitionResponse custom_function_service_get_custom_function(body)

GetCustomFunction retrieves the definition of a specific custom function. The custom function is specified in the CustomFunctionGetDefinition message, which includes its ID and scope. The method returns a CustomFunctionDefinitionResponse that contains either the custom function definition or an error.

### Example


```python
import time
import openapi_client
from openapi_client.api import custom_function_service_api
from openapi_client.model.titanium_custom_function_get_definition import TitaniumCustomFunctionGetDefinition
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_custom_function_definition_response import TitaniumCustomFunctionDefinitionResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = custom_function_service_api.CustomFunctionServiceApi(api_client)
    body = TitaniumCustomFunctionGetDefinition(
        descriptor_type="descriptor_type_example",
        id_scope=TitaniumGetDefinition(
            descriptor_name="descriptor_name_example",
            identifier=TitaniumIdentifier(
                name="name_example",
                uid="uid_example",
            ),
            scope="scope_example",
        ),
    ) # TitaniumCustomFunctionGetDefinition | 

    # example passing only required values which don't have defaults set
    try:
        # GetCustomFunction retrieves the definition of a specific custom function. The custom function is specified in the CustomFunctionGetDefinition message, which includes its ID and scope. The method returns a CustomFunctionDefinitionResponse that contains either the custom function definition or an error.
        api_response = api_instance.custom_function_service_get_custom_function(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CustomFunctionServiceApi->custom_function_service_get_custom_function: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumCustomFunctionGetDefinition**](TitaniumCustomFunctionGetDefinition.md)|  |

### Return type

[**TitaniumCustomFunctionDefinitionResponse**](TitaniumCustomFunctionDefinitionResponse.md)

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

# **custom_function_service_list_custom_function_versions**
> TitaniumListVersionResponse custom_function_service_list_custom_function_versions(body)

ListCustomFunctionVersions lists all the versions of a specific custom function. The custom function is specified in the GetDefinition message, which includes its ID and scope. The method returns a ListVersionResponse that contains either a list of versions or an error.

### Example


```python
import time
import openapi_client
from openapi_client.api import custom_function_service_api
from openapi_client.model.titanium_get_definition import TitaniumGetDefinition
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_list_version_response import TitaniumListVersionResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = custom_function_service_api.CustomFunctionServiceApi(api_client)
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
        # ListCustomFunctionVersions lists all the versions of a specific custom function. The custom function is specified in the GetDefinition message, which includes its ID and scope. The method returns a ListVersionResponse that contains either a list of versions or an error.
        api_response = api_instance.custom_function_service_list_custom_function_versions(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CustomFunctionServiceApi->custom_function_service_list_custom_function_versions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumGetDefinition**](TitaniumGetDefinition.md)|  |

### Return type

[**TitaniumListVersionResponse**](TitaniumListVersionResponse.md)

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

# **custom_function_service_list_custom_functions**
> TitaniumListCustomFunctionResponse custom_function_service_list_custom_functions(body)

ListCustomFunctions lists all the custom functions that match the specified criteria. The criteria are defined in the ListCustomFunctionRequest message, which includes the descriptor name and the type of the custom function descriptor. The method returns a ListCustomFunctionResponse that contains either a list of custom functions or an error.

### Example


```python
import time
import openapi_client
from openapi_client.api import custom_function_service_api
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_list_custom_function_response import TitaniumListCustomFunctionResponse
from openapi_client.model.titanium_list_custom_function_request import TitaniumListCustomFunctionRequest
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = custom_function_service_api.CustomFunctionServiceApi(api_client)
    body = TitaniumListCustomFunctionRequest(
        descriptor_name="descriptor_name_example",
        descriptor_type="descriptor_type_example",
        request=TitaniumListRequest(
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
        ),
    ) # TitaniumListCustomFunctionRequest | 

    # example passing only required values which don't have defaults set
    try:
        # ListCustomFunctions lists all the custom functions that match the specified criteria. The criteria are defined in the ListCustomFunctionRequest message, which includes the descriptor name and the type of the custom function descriptor. The method returns a ListCustomFunctionResponse that contains either a list of custom functions or an error.
        api_response = api_instance.custom_function_service_list_custom_functions(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CustomFunctionServiceApi->custom_function_service_list_custom_functions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumListCustomFunctionRequest**](TitaniumListCustomFunctionRequest.md)|  |

### Return type

[**TitaniumListCustomFunctionResponse**](TitaniumListCustomFunctionResponse.md)

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

