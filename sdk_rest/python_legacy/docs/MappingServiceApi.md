# openapi_client.MappingServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mapping_service_add_mapping_rule**](MappingServiceApi.md#mapping_service_add_mapping_rule) | **POST** /api/v1/mapping/rule/add | AddMappingRule AddMappingRule is an API used to add a specific mapping rule to the system. The name provided for the mapping rule must match the asset class and descriptor names. If a mapping rule with the same name already exists, it will be updated. This API accepts a MappingRuleDefinition object as its parameter,which includes information about the mapping rule being added. The response from this API is a DescriptorPairBasedAcknowledgeResponse,which acknowledges the addition of the mapping rule.
[**mapping_service_disable_mapping_rule**](MappingServiceApi.md#mapping_service_disable_mapping_rule) | **POST** /api/v1/mapping/rule/disable | DisableMappingRule is used to disable a mapping rule for a given descriptor pair. It accepts a DescriptorPairBasedGetDefinition object as its parameter, which specifies the source and destination descriptors for the mapping rule. The response from this it is a DescriptorPairBasedAcknowledgeResponse, which acknowledges the disablement of the mapping rule.
[**mapping_service_enable_mapping_rule**](MappingServiceApi.md#mapping_service_enable_mapping_rule) | **POST** /api/v1/mapping/rule/enable | EnableMappingRule is used to enable a mapping rule for a given descriptor pair. It accepts a DescriptorPairBasedGetDefinition object as its parameter, which specifies the source and destination descriptors for the mapping rule. The response from this it is a DescriptorPairBasedAcknowledgeResponse, which acknowledges the enablement of the mapping rule.
[**mapping_service_get_mapping_rule**](MappingServiceApi.md#mapping_service_get_mapping_rule) | **POST** /api/v1/mapping/rule/get | GetMappingRule is used to retrieve a mapping rule for a given descriptor pair. It accepts a DescriptorPairBasedGetDefinition object as its parameter, which specifies the source and destination descriptors for the mapping rule. The response from this it is a MappingRuleResponse, which includes information about the retrieved mapping rule.
[**mapping_service_get_mapping_rule_version**](MappingServiceApi.md#mapping_service_get_mapping_rule_version) | **GET** /api/v1/mapping/rule/version/{scope}/{srcDescriptor}/{destDescriptor}/{versionId} | GetMappingRuleVersion is used to retrieve a specific version of a mapping rule for a given descriptor pair. It accepts a DescriptorPairBasedVersionRequest object as its parameter, which includes the scope, source descriptor, destination descriptor, and version ID for the mapping rule. The response from it is a MappingRuleResponse, which includes information about the retrieved version of the mapping rule.
[**mapping_service_list_mapping_rule_versions**](MappingServiceApi.md#mapping_service_list_mapping_rule_versions) | **POST** /api/v1/mapping/rule/versions | ListMappingRuleVersions is used to retrieve a list of all versions of a mapping rule for a given descriptor pair. It accepts a DescriptorPairBasedGetDefinition object as its parameter, which specifies the source and destination descriptors for the mapping rule. The response from this it is a ListVersionResponse, which includes information about all versions of the mapping rule.
[**mapping_service_list_mapping_rules**](MappingServiceApi.md#mapping_service_list_mapping_rules) | **POST** /api/v1/mapping/rule/list | ListMappingRules is used to retrieve a list of all mapping rules in the system. It accepts a ListRequest object as its parameter, which includes optional parameters for filtering the results. The response from this it is a MappingRuleList, which includes information about all mapping rules in the system that match the provided filter parameters.


# **mapping_service_add_mapping_rule**
> TitaniumDescriptorPairBasedAcknowledgeResponse mapping_service_add_mapping_rule(body)

AddMappingRule AddMappingRule is an API used to add a specific mapping rule to the system. The name provided for the mapping rule must match the asset class and descriptor names. If a mapping rule with the same name already exists, it will be updated. This API accepts a MappingRuleDefinition object as its parameter,which includes information about the mapping rule being added. The response from this API is a DescriptorPairBasedAcknowledgeResponse,which acknowledges the addition of the mapping rule.

Example of request for regular user : {   \"src_descriptor\":\"foreign_exchange-vanilla-forwards\",   \"dest_descriptor\":\"foreign_exchange-vanilla-forwards\",   \"transformations\":[      {         \"targetColumn\":\"submission_date\",         \"sourceColumn\":\"date\"      },      {         \"targetColumn\":\"submission_asset\",         \"rule\":\"{ \\\"$to_upper\\\": { \\\"$trim\\\" : \\\"fx_test_for_bank1.submission_asset\\\" }}\",         \"name\": \"upper case asset\",         \"description\": \"i am optional...\"      }   ] }  Example of request for Back Office : {   \"src_descriptor\":\"foreign_exchange-vanilla-forwards\",   \"dest_descriptor\":\"foreign_exchange-vanilla-forwards\",   \"scope\":\"global\",   \"transformations\":[      {         \"targetColumn\":\"submission_date\",         \"sourceColumn\":\"another_date\"      },      {         \"targetColumn\":\"submission_asset\",         \"rule\":\"{ \\\"$to_upper\\\": { \\\"$trim\\\" : \\\"fx_test_for_bank1.submission_asset\\\" }}\",         \"name\": \"upper case asset\",         \"description\": \"i am optional...\"      }   ] }  Example of response : {   \"data\":{      \"uid\":\"fc8b57b7-cc90-11ec-b784-8dfc726b351f\",      \"src_descriptor\":\"foreign_exchange-vanilla-forwards\",      \"dest_descriptor\":\"foreign_exchange-vanilla-forwards\"   } }  Example of error response : {   \"error\":{      \"code\":70,      \"message\":\"Missing argument: rule name.\"   } }

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
    api_instance = openapi_client.MappingServiceApi(api_client)
    body = openapi_client.TitaniumMappingRuleDefinition() # TitaniumMappingRuleDefinition | 

    try:
        # AddMappingRule AddMappingRule is an API used to add a specific mapping rule to the system. The name provided for the mapping rule must match the asset class and descriptor names. If a mapping rule with the same name already exists, it will be updated. This API accepts a MappingRuleDefinition object as its parameter,which includes information about the mapping rule being added. The response from this API is a DescriptorPairBasedAcknowledgeResponse,which acknowledges the addition of the mapping rule.
        api_response = api_instance.mapping_service_add_mapping_rule(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MappingServiceApi->mapping_service_add_mapping_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumMappingRuleDefinition**](TitaniumMappingRuleDefinition.md)|  | 

### Return type

[**TitaniumDescriptorPairBasedAcknowledgeResponse**](TitaniumDescriptorPairBasedAcknowledgeResponse.md)

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

# **mapping_service_disable_mapping_rule**
> TitaniumDescriptorPairBasedAcknowledgeResponse mapping_service_disable_mapping_rule(body)

DisableMappingRule is used to disable a mapping rule for a given descriptor pair. It accepts a DescriptorPairBasedGetDefinition object as its parameter, which specifies the source and destination descriptors for the mapping rule. The response from this it is a DescriptorPairBasedAcknowledgeResponse, which acknowledges the disablement of the mapping rule.

Request: {  \"src_descriptor\":\"foreign_exchange-vanilla-options\",  \"dest_descriptor\":\"foreign_exchange-vanilla-options\"  \"scope\": \"Zbank1\" }  Response: {    \"data\": {        \"uid\": \"\",        \"src_descriptor\":\"foreign_exchange-vanilla-options\",        \"dest_descriptor\":\"foreign_exchange-vanilla-options\"    } }

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
    api_instance = openapi_client.MappingServiceApi(api_client)
    body = openapi_client.TitaniumDescriptorPairBasedGetDefinition() # TitaniumDescriptorPairBasedGetDefinition | 

    try:
        # DisableMappingRule is used to disable a mapping rule for a given descriptor pair. It accepts a DescriptorPairBasedGetDefinition object as its parameter, which specifies the source and destination descriptors for the mapping rule. The response from this it is a DescriptorPairBasedAcknowledgeResponse, which acknowledges the disablement of the mapping rule.
        api_response = api_instance.mapping_service_disable_mapping_rule(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MappingServiceApi->mapping_service_disable_mapping_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumDescriptorPairBasedGetDefinition**](TitaniumDescriptorPairBasedGetDefinition.md)|  | 

### Return type

[**TitaniumDescriptorPairBasedAcknowledgeResponse**](TitaniumDescriptorPairBasedAcknowledgeResponse.md)

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

# **mapping_service_enable_mapping_rule**
> TitaniumDescriptorPairBasedAcknowledgeResponse mapping_service_enable_mapping_rule(body)

EnableMappingRule is used to enable a mapping rule for a given descriptor pair. It accepts a DescriptorPairBasedGetDefinition object as its parameter, which specifies the source and destination descriptors for the mapping rule. The response from this it is a DescriptorPairBasedAcknowledgeResponse, which acknowledges the enablement of the mapping rule.

Request: {  \"src_descriptor\":\"foreign_exchange-vanilla-options\",  \"dest_descriptor\":\"foreign_exchange-vanilla-options\"  \"scope\": \"Zbank1\" }  Response: {    \"data\": {        \"uid\": \"\",        \"src_descriptor\":\"foreign_exchange-vanilla-options\",        \"dest_descriptor\":\"foreign_exchange-vanilla-options\"    } }

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
    api_instance = openapi_client.MappingServiceApi(api_client)
    body = openapi_client.TitaniumDescriptorPairBasedGetDefinition() # TitaniumDescriptorPairBasedGetDefinition | 

    try:
        # EnableMappingRule is used to enable a mapping rule for a given descriptor pair. It accepts a DescriptorPairBasedGetDefinition object as its parameter, which specifies the source and destination descriptors for the mapping rule. The response from this it is a DescriptorPairBasedAcknowledgeResponse, which acknowledges the enablement of the mapping rule.
        api_response = api_instance.mapping_service_enable_mapping_rule(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MappingServiceApi->mapping_service_enable_mapping_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumDescriptorPairBasedGetDefinition**](TitaniumDescriptorPairBasedGetDefinition.md)|  | 

### Return type

[**TitaniumDescriptorPairBasedAcknowledgeResponse**](TitaniumDescriptorPairBasedAcknowledgeResponse.md)

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

# **mapping_service_get_mapping_rule**
> TitaniumMappingRuleResponse mapping_service_get_mapping_rule(body)

GetMappingRule is used to retrieve a mapping rule for a given descriptor pair. It accepts a DescriptorPairBasedGetDefinition object as its parameter, which specifies the source and destination descriptors for the mapping rule. The response from this it is a MappingRuleResponse, which includes information about the retrieved mapping rule.

Example of request for regular user : {   \"identifier\":{      \"uid\":\"fc8b57b7-cc90-11ec-b784-8dfc726b351f\"   } } Or : {      \"src_descriptor\":\"foreign_exchange-vanilla-forwards\",      \"dest_descriptor\":\"foreign_exchange-vanilla-forwards\" }  Example of request for Back Office : {   \"identifier\":{       \"uid\":\"fc8b57b7-cc90-11ec-b784-8dfc726b351f\"   },   \"scope\":\"bank1\" } Or : {   \"src_descriptor\":\"foreign_exchange-vanilla-forwards\",   \"dest_descriptor\":\"foreign_exchange-vanilla-forwards\",   \"scope\":\"bank1\" }  Example of response : { \"data\": {  \"uid\": \"\",  \"srcDescriptor\": \"foreign_exchange-vanilla-options\",  \"destDescriptor\": \"foreign_exchange-vanilla-options\",  \"transformations\": [   {    \"name\": \"\",    \"targetColumn\": \"snap_date\",    \"sourceColumn\": \"submission_date\",    \"rule\": \"\",    \"description\": \"\"   }  ],  \"scope\": \"\" } }  Example of error response : {   \"error\":{      \"code\":70,      \"message\":\"Can't get mapping rule: [[empty] of service [MAPPINGRULESET] does not exist in namespace [bank1]].\"   } }

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
    api_instance = openapi_client.MappingServiceApi(api_client)
    body = openapi_client.TitaniumDescriptorPairBasedGetDefinition() # TitaniumDescriptorPairBasedGetDefinition | 

    try:
        # GetMappingRule is used to retrieve a mapping rule for a given descriptor pair. It accepts a DescriptorPairBasedGetDefinition object as its parameter, which specifies the source and destination descriptors for the mapping rule. The response from this it is a MappingRuleResponse, which includes information about the retrieved mapping rule.
        api_response = api_instance.mapping_service_get_mapping_rule(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MappingServiceApi->mapping_service_get_mapping_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumDescriptorPairBasedGetDefinition**](TitaniumDescriptorPairBasedGetDefinition.md)|  | 

### Return type

[**TitaniumMappingRuleResponse**](TitaniumMappingRuleResponse.md)

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

# **mapping_service_get_mapping_rule_version**
> TitaniumMappingRuleResponse mapping_service_get_mapping_rule_version(scope, src_descriptor, dest_descriptor, version_id)

GetMappingRuleVersion is used to retrieve a specific version of a mapping rule for a given descriptor pair. It accepts a DescriptorPairBasedVersionRequest object as its parameter, which includes the scope, source descriptor, destination descriptor, and version ID for the mapping rule. The response from it is a MappingRuleResponse, which includes information about the retrieved version of the mapping rule.

Example of request : GET /api/v1/validation/rule/version/fx_fwd_1/fx_fwd_2/teTYb9Fs_lIOoPQJukM6dY3aJdiMqT-SdBPdvYfJAjk=  Example of response : {   \"definition\":\"{\\\"src_descriptor\\\":\\\"foreign_exchange-vanilla-forwards\\\",\\\"dest_descriptor\\\":\\\"foreign_exchange-vanilla-forwards\\\",\\\"transformations\\\":[{\\\"targetColumnName\\\":\\\"submission_date\\\",\\\"sourceColumnName\\\":\\\"another_date\\\"},{\\\"rule\\\":\\\"{ \\\\\\\"$to_upper\\\\\\\": { \\\\\\\"$trim\\\\\\\" : \\\\\\\"fx_test_for_bank1.submission_asset\\\\\\\" }}\\\",\\\"targetColumnName\\\":\\\"submission_asset\\\", \\\"name\\\": \\\"upper case asset\\\", \\\"description\\\": \\\"i am optional...\\\"}]}\" }

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
    api_instance = openapi_client.MappingServiceApi(api_client)
    scope = 'scope_example' # str | 
src_descriptor = 'src_descriptor_example' # str | 
dest_descriptor = 'dest_descriptor_example' # str | 
version_id = 'version_id_example' # str | 

    try:
        # GetMappingRuleVersion is used to retrieve a specific version of a mapping rule for a given descriptor pair. It accepts a DescriptorPairBasedVersionRequest object as its parameter, which includes the scope, source descriptor, destination descriptor, and version ID for the mapping rule. The response from it is a MappingRuleResponse, which includes information about the retrieved version of the mapping rule.
        api_response = api_instance.mapping_service_get_mapping_rule_version(scope, src_descriptor, dest_descriptor, version_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MappingServiceApi->mapping_service_get_mapping_rule_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**|  | 
 **src_descriptor** | **str**|  | 
 **dest_descriptor** | **str**|  | 
 **version_id** | **str**|  | 

### Return type

[**TitaniumMappingRuleResponse**](TitaniumMappingRuleResponse.md)

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

# **mapping_service_list_mapping_rule_versions**
> TitaniumListVersionResponse mapping_service_list_mapping_rule_versions(body)

ListMappingRuleVersions is used to retrieve a list of all versions of a mapping rule for a given descriptor pair. It accepts a DescriptorPairBasedGetDefinition object as its parameter, which specifies the source and destination descriptors for the mapping rule. The response from this it is a ListVersionResponse, which includes information about all versions of the mapping rule.

Example of request : {  \"scope\": \"global\",  \"src_descriptor\":\"foreign_exchange-vanilla-options\",  \"dest_descriptor\":\"foreign_exchange-vanilla-options\" }  Example of response : {   \"data\":{      \"versions\":[         {            \"versionId\":\"EKc9bpBGCbLJmBqOpP0FTqtNusxgZrgCheGXj_MTj7A=\",            \"createdAt\":\"2022-05-05 11:33:59.0\"         },         {            \"versionId\":\"JKLFLkhV3SC-fqO0L-WTswr5ttHLfnvF8rMlLnkafAc=\",            \"createdAt\":\"2022-05-05 11:32:42.0\"         }      ]   } }

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
    api_instance = openapi_client.MappingServiceApi(api_client)
    body = openapi_client.TitaniumDescriptorPairBasedGetDefinition() # TitaniumDescriptorPairBasedGetDefinition | 

    try:
        # ListMappingRuleVersions is used to retrieve a list of all versions of a mapping rule for a given descriptor pair. It accepts a DescriptorPairBasedGetDefinition object as its parameter, which specifies the source and destination descriptors for the mapping rule. The response from this it is a ListVersionResponse, which includes information about all versions of the mapping rule.
        api_response = api_instance.mapping_service_list_mapping_rule_versions(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MappingServiceApi->mapping_service_list_mapping_rule_versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumDescriptorPairBasedGetDefinition**](TitaniumDescriptorPairBasedGetDefinition.md)|  | 

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

# **mapping_service_list_mapping_rules**
> TitaniumMappingRuleList mapping_service_list_mapping_rules(body)

ListMappingRules is used to retrieve a list of all mapping rules in the system. It accepts a ListRequest object as its parameter, which includes optional parameters for filtering the results. The response from this it is a MappingRuleList, which includes information about all mapping rules in the system that match the provided filter parameters.

Example of request : {   \"scope\":\"global\" } Or optionally use filter: {   \"scope\":\"global\",   \"filter\": \".*vanilla.*__.*vanilla.*\" // all mapping rules from any vanilla to any vanilla }  Example of response : {    \"data\": {        \"results\": [            {                \"uid\": \"Djqreg7gTs7CV2rSyyucOWCFjK7ldgS9yQX0o0rEiV0=\",                \"src_descriptor\": \"foreign_exchange-vanilla-forwards\",                \"dest_descriptor\": \"foreign_exchange-vanilla-forwards\"             },            {                \"uid\": \"Djqreg7gTs7CV2rSyyucOWCFjK7ldgS9yQX0o0rEiV0=\",                \"src_descriptor\": \"foreign_exchange-vanilla-options\",                \"dest_descriptor\": \"foreign_exchange-vanilla-options\"            }        ]    } }

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
    api_instance = openapi_client.MappingServiceApi(api_client)
    body = openapi_client.TitaniumListRequest() # TitaniumListRequest | 

    try:
        # ListMappingRules is used to retrieve a list of all mapping rules in the system. It accepts a ListRequest object as its parameter, which includes optional parameters for filtering the results. The response from this it is a MappingRuleList, which includes information about all mapping rules in the system that match the provided filter parameters.
        api_response = api_instance.mapping_service_list_mapping_rules(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MappingServiceApi->mapping_service_list_mapping_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumListRequest**](TitaniumListRequest.md)|  | 

### Return type

[**TitaniumMappingRuleList**](TitaniumMappingRuleList.md)

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

