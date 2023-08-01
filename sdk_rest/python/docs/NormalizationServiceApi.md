# openapi_client.NormalizationServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**normalization_service_add_normalization_rule**](NormalizationServiceApi.md#normalization_service_add_normalization_rule) | **POST** /api/v1/normalization/rule/add | 
[**normalization_service_disable_normalization_rule**](NormalizationServiceApi.md#normalization_service_disable_normalization_rule) | **POST** /api/v1/normalization/rule/disable | 
[**normalization_service_enable_normalization_rule**](NormalizationServiceApi.md#normalization_service_enable_normalization_rule) | **POST** /api/v1/normalization/rule/enable | 
[**normalization_service_get_normalization_rule**](NormalizationServiceApi.md#normalization_service_get_normalization_rule) | **POST** /api/v1/normalization/rule/get | 
[**normalization_service_get_normalization_rule_version**](NormalizationServiceApi.md#normalization_service_get_normalization_rule_version) | **GET** /api/v1/normalization/rule/version/{descriptorName}/{versionId} | 
[**normalization_service_list_normalization_rule_versions**](NormalizationServiceApi.md#normalization_service_list_normalization_rule_versions) | **POST** /api/v1/normalization/rule/versions | 
[**normalization_service_list_normalization_rules**](NormalizationServiceApi.md#normalization_service_list_normalization_rules) | **POST** /api/v1/normalization/rule/list | 


# **normalization_service_add_normalization_rule**
> TitaniumAcknowledgeResponse normalization_service_add_normalization_rule(body)



### Example


```python
import time
import openapi_client
from openapi_client.api import normalization_service_api
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_normalization_rule_definition import TitaniumNormalizationRuleDefinition
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
    api_instance = normalization_service_api.NormalizationServiceApi(api_client)
    body = TitaniumNormalizationRuleDefinition(
        descriptor_name="descriptor_name_example",
        scope="scope_example",
        transformations=[
            TitaniumTransformation(
                description="description_example",
                lut=TitaniumDynamicLut(
                    filter="filter_example",
                    key=[
                        "key_example",
                    ],
                    type="type_example",
                    value={},
                ),
                name="name_example",
                rule="rule_example",
                source_column="source_column_example",
                target_column="target_column_example",
            ),
        ],
        uid="uid_example",
    ) # TitaniumNormalizationRuleDefinition | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.normalization_service_add_normalization_rule(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NormalizationServiceApi->normalization_service_add_normalization_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumNormalizationRuleDefinition**](TitaniumNormalizationRuleDefinition.md)|  |

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

# **normalization_service_disable_normalization_rule**
> TitaniumAcknowledgeResponse normalization_service_disable_normalization_rule(body)



### Example


```python
import time
import openapi_client
from openapi_client.api import normalization_service_api
from openapi_client.model.titanium_get_definition import TitaniumGetDefinition
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
    api_instance = normalization_service_api.NormalizationServiceApi(api_client)
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
        api_response = api_instance.normalization_service_disable_normalization_rule(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NormalizationServiceApi->normalization_service_disable_normalization_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumGetDefinition**](TitaniumGetDefinition.md)|  |

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

# **normalization_service_enable_normalization_rule**
> TitaniumAcknowledgeResponse normalization_service_enable_normalization_rule(body)



### Example


```python
import time
import openapi_client
from openapi_client.api import normalization_service_api
from openapi_client.model.titanium_get_definition import TitaniumGetDefinition
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
    api_instance = normalization_service_api.NormalizationServiceApi(api_client)
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
        api_response = api_instance.normalization_service_enable_normalization_rule(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NormalizationServiceApi->normalization_service_enable_normalization_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumGetDefinition**](TitaniumGetDefinition.md)|  |

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

# **normalization_service_get_normalization_rule**
> TitaniumNormalizationRuleResponse normalization_service_get_normalization_rule(body)



### Example


```python
import time
import openapi_client
from openapi_client.api import normalization_service_api
from openapi_client.model.titanium_get_definition import TitaniumGetDefinition
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_normalization_rule_response import TitaniumNormalizationRuleResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = normalization_service_api.NormalizationServiceApi(api_client)
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
        api_response = api_instance.normalization_service_get_normalization_rule(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NormalizationServiceApi->normalization_service_get_normalization_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumGetDefinition**](TitaniumGetDefinition.md)|  |

### Return type

[**TitaniumNormalizationRuleResponse**](TitaniumNormalizationRuleResponse.md)

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

# **normalization_service_get_normalization_rule_version**
> TitaniumNormalizationRuleResponse normalization_service_get_normalization_rule_version(descriptor_name, version_id)



### Example


```python
import time
import openapi_client
from openapi_client.api import normalization_service_api
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_normalization_rule_response import TitaniumNormalizationRuleResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = normalization_service_api.NormalizationServiceApi(api_client)
    descriptor_name = "descriptorName_example" # str | 
    version_id = "versionId_example" # str | 
    name = "name_example" # str |  (optional)
    scope = "scope_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.normalization_service_get_normalization_rule_version(descriptor_name, version_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NormalizationServiceApi->normalization_service_get_normalization_rule_version: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.normalization_service_get_normalization_rule_version(descriptor_name, version_id, name=name, scope=scope)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NormalizationServiceApi->normalization_service_get_normalization_rule_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **descriptor_name** | **str**|  |
 **version_id** | **str**|  |
 **name** | **str**|  | [optional]
 **scope** | **str**|  | [optional]

### Return type

[**TitaniumNormalizationRuleResponse**](TitaniumNormalizationRuleResponse.md)

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

# **normalization_service_list_normalization_rule_versions**
> TitaniumListVersionResponse normalization_service_list_normalization_rule_versions(body)



### Example


```python
import time
import openapi_client
from openapi_client.api import normalization_service_api
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
    api_instance = normalization_service_api.NormalizationServiceApi(api_client)
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
        api_response = api_instance.normalization_service_list_normalization_rule_versions(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NormalizationServiceApi->normalization_service_list_normalization_rule_versions: %s\n" % e)
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

# **normalization_service_list_normalization_rules**
> TitaniumListRuleResponse normalization_service_list_normalization_rules(body)



### Example


```python
import time
import openapi_client
from openapi_client.api import normalization_service_api
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_list_rule_response import TitaniumListRuleResponse
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
    api_instance = normalization_service_api.NormalizationServiceApi(api_client)
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
        api_response = api_instance.normalization_service_list_normalization_rules(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NormalizationServiceApi->normalization_service_list_normalization_rules: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumListRequest**](TitaniumListRequest.md)|  |

### Return type

[**TitaniumListRuleResponse**](TitaniumListRuleResponse.md)

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

