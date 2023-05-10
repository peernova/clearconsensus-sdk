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
    api_instance = openapi_client.NormalizationServiceApi(api_client)
    body = openapi_client.TitaniumNormalizationRuleDefinition() # TitaniumNormalizationRuleDefinition | 

    try:
        api_response = api_instance.normalization_service_add_normalization_rule(body)
        pprint(api_response)
    except ApiException as e:
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
    api_instance = openapi_client.NormalizationServiceApi(api_client)
    body = openapi_client.TitaniumGetDefinition() # TitaniumGetDefinition | 

    try:
        api_response = api_instance.normalization_service_disable_normalization_rule(body)
        pprint(api_response)
    except ApiException as e:
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
    api_instance = openapi_client.NormalizationServiceApi(api_client)
    body = openapi_client.TitaniumGetDefinition() # TitaniumGetDefinition | 

    try:
        api_response = api_instance.normalization_service_enable_normalization_rule(body)
        pprint(api_response)
    except ApiException as e:
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
    api_instance = openapi_client.NormalizationServiceApi(api_client)
    body = openapi_client.TitaniumGetDefinition() # TitaniumGetDefinition | 

    try:
        api_response = api_instance.normalization_service_get_normalization_rule(body)
        pprint(api_response)
    except ApiException as e:
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
> TitaniumNormalizationRuleResponse normalization_service_get_normalization_rule_version(descriptor_name, version_id, name=name, scope=scope)



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
    api_instance = openapi_client.NormalizationServiceApi(api_client)
    descriptor_name = 'descriptor_name_example' # str | 
version_id = 'version_id_example' # str | 
name = 'name_example' # str |  (optional)
scope = 'scope_example' # str |  (optional)

    try:
        api_response = api_instance.normalization_service_get_normalization_rule_version(descriptor_name, version_id, name=name, scope=scope)
        pprint(api_response)
    except ApiException as e:
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
    api_instance = openapi_client.NormalizationServiceApi(api_client)
    body = openapi_client.TitaniumGetDefinition() # TitaniumGetDefinition | 

    try:
        api_response = api_instance.normalization_service_list_normalization_rule_versions(body)
        pprint(api_response)
    except ApiException as e:
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
    api_instance = openapi_client.NormalizationServiceApi(api_client)
    body = openapi_client.TitaniumListRequest() # TitaniumListRequest | 

    try:
        api_response = api_instance.normalization_service_list_normalization_rules(body)
        pprint(api_response)
    except ApiException as e:
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

