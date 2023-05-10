# openapi_client.UniqueKeyServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**unique_key_service_add_unique_key**](UniqueKeyServiceApi.md#unique_key_service_add_unique_key) | **POST** /api/v1/uniquekey/add | AddUniqueKey is used to add a new unique key definition to the system.
[**unique_key_service_get_unique_key**](UniqueKeyServiceApi.md#unique_key_service_get_unique_key) | **POST** /api/v1/uniquekey/get | GetUniqueKey is used to retrieve a unique key definition by its scope and name. Request: {   \&quot;identifier\&quot;:{      \&quot;name\&quot;:\&quot;foreign_exchange-vanilla-forwards\&quot;   },   \&quot;scope\&quot;:\&quot;global\&quot; }
[**unique_key_service_get_unique_key_version**](UniqueKeyServiceApi.md#unique_key_service_get_unique_key_version) | **GET** /api/v1/uniquekey/version/{scope}/{name}/{versionId} | GetUniqueKeyVersion is used to retrieve a specific version of a unique key definition by its scope, name, and version ID. Response: {    \&quot;data\&quot;: {        \&quot;name\&quot;: \&quot;foreign_exchange-vanilla-forwards\&quot;,        \&quot;scope\&quot;: \&quot;global\&quot;,        \&quot;uniqueKey\&quot;: [            \&quot;asset\&quot;,            \&quot;service\&quot;,            \&quot;sub-asset\&quot;,            \&quot;instrument_type\&quot;,            \&quot;tenor\&quot;,            \&quot;snap_date\&quot;,            \&quot;snap_time\&quot;,            \&quot;curr_1\&quot;,            \&quot;curr_2\&quot;,            \&quot;onshore_offshore_curr_1\&quot;,            \&quot;onshore_offshore_curr_2\&quot;        ],        \&quot;orderBy\&quot;: [            \&quot;__input_row_num\&quot;        ],        \&quot;order\&quot;: \&quot;ASC\&quot;    } }
[**unique_key_service_list_unique_key_versions**](UniqueKeyServiceApi.md#unique_key_service_list_unique_key_versions) | **POST** /api/v1/uniquekey/versions | ListUniqueKeyVersions is used to retrieve a list of all versions of a specific unique key definition by its scope and name. Request: {   \&quot;scope\&quot;:\&quot;global\&quot;,   \&quot;identifier\&quot;: {        \&quot;name\&quot;: \&quot;foreign_exchange-vanilla-forwards\&quot;    } }
[**unique_key_service_list_unique_keys**](UniqueKeyServiceApi.md#unique_key_service_list_unique_keys) | **POST** /api/v1/uniquekey/list | ListUniqueKeys is used to retrieve a list of all unique key definitions in the system. Request: {   \&quot;scope\&quot;:\&quot;global\&quot; }


# **unique_key_service_add_unique_key**
> TitaniumAcknowledgeResponse unique_key_service_add_unique_key(body)

AddUniqueKey is used to add a new unique key definition to the system.

Example of request : {   \"name\":\"foreign_exchange-vanilla-forwards\",   \"scope\":\"global\",   \"uniqueKey\":[      \"snap_date\",      \"asset\",      \"service\",      \"client\",      \"service\",      \"tenor\",      \"snap_time\",      \"instrument_type\",      \"spot_reference_price\",      \"mid_fwrd_outright\",      \"mid_fwrd_points\",      \"onshore_offshore_curr_1\",      \"onshore_offshore_curr_2\"   ] }

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
    api_instance = openapi_client.UniqueKeyServiceApi(api_client)
    body = openapi_client.TitaniumUniqueKeyDefinition() # TitaniumUniqueKeyDefinition | 

    try:
        # AddUniqueKey is used to add a new unique key definition to the system.
        api_response = api_instance.unique_key_service_add_unique_key(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UniqueKeyServiceApi->unique_key_service_add_unique_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumUniqueKeyDefinition**](TitaniumUniqueKeyDefinition.md)|  | 

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

# **unique_key_service_get_unique_key**
> TitaniumUniqueKeyDefinitionResponse unique_key_service_get_unique_key(body)

GetUniqueKey is used to retrieve a unique key definition by its scope and name. Request: {   \"identifier\":{      \"name\":\"foreign_exchange-vanilla-forwards\"   },   \"scope\":\"global\" }

Response: {    \"data\": {        \"name\": \"foreign_exchange-vanilla-forwards\",        \"scope\": \"global\",        \"uniqueKey\": [            \"snap_date\",            \"asset\",            \"service\",            \"client\",            \"service\",            \"tenor\",            \"snap_time\",            \"instrument_type\",            \"spot_reference_price\",            \"mid_fwrd_outright\",            \"mid_fwrd_points\",            \"onshore_offshore_curr_1\",            \"onshore_offshore_curr_2\"        ],        \"orderBy\": [            \"__input_row_num\"        ],        \"order\": \"ASC\"    } }

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
    api_instance = openapi_client.UniqueKeyServiceApi(api_client)
    body = openapi_client.TitaniumGetDefinition() # TitaniumGetDefinition | 

    try:
        # GetUniqueKey is used to retrieve a unique key definition by its scope and name. Request: {   \"identifier\":{      \"name\":\"foreign_exchange-vanilla-forwards\"   },   \"scope\":\"global\" }
        api_response = api_instance.unique_key_service_get_unique_key(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UniqueKeyServiceApi->unique_key_service_get_unique_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumGetDefinition**](TitaniumGetDefinition.md)|  | 

### Return type

[**TitaniumUniqueKeyDefinitionResponse**](TitaniumUniqueKeyDefinitionResponse.md)

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

# **unique_key_service_get_unique_key_version**
> TitaniumUniqueKeyDefinitionResponse unique_key_service_get_unique_key_version(scope, name, version_id, descriptor_name=descriptor_name)

GetUniqueKeyVersion is used to retrieve a specific version of a unique key definition by its scope, name, and version ID. Response: {    \"data\": {        \"name\": \"foreign_exchange-vanilla-forwards\",        \"scope\": \"global\",        \"uniqueKey\": [            \"asset\",            \"service\",            \"sub-asset\",            \"instrument_type\",            \"tenor\",            \"snap_date\",            \"snap_time\",            \"curr_1\",            \"curr_2\",            \"onshore_offshore_curr_1\",            \"onshore_offshore_curr_2\"        ],        \"orderBy\": [            \"__input_row_num\"        ],        \"order\": \"ASC\"    } }

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
    api_instance = openapi_client.UniqueKeyServiceApi(api_client)
    scope = 'scope_example' # str | 
name = 'name_example' # str | 
version_id = 'version_id_example' # str | 
descriptor_name = 'descriptor_name_example' # str |  (optional)

    try:
        # GetUniqueKeyVersion is used to retrieve a specific version of a unique key definition by its scope, name, and version ID. Response: {    \"data\": {        \"name\": \"foreign_exchange-vanilla-forwards\",        \"scope\": \"global\",        \"uniqueKey\": [            \"asset\",            \"service\",            \"sub-asset\",            \"instrument_type\",            \"tenor\",            \"snap_date\",            \"snap_time\",            \"curr_1\",            \"curr_2\",            \"onshore_offshore_curr_1\",            \"onshore_offshore_curr_2\"        ],        \"orderBy\": [            \"__input_row_num\"        ],        \"order\": \"ASC\"    } }
        api_response = api_instance.unique_key_service_get_unique_key_version(scope, name, version_id, descriptor_name=descriptor_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UniqueKeyServiceApi->unique_key_service_get_unique_key_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**|  | 
 **name** | **str**|  | 
 **version_id** | **str**|  | 
 **descriptor_name** | **str**|  | [optional] 

### Return type

[**TitaniumUniqueKeyDefinitionResponse**](TitaniumUniqueKeyDefinitionResponse.md)

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

# **unique_key_service_list_unique_key_versions**
> TitaniumListVersionResponse unique_key_service_list_unique_key_versions(body)

ListUniqueKeyVersions is used to retrieve a list of all versions of a specific unique key definition by its scope and name. Request: {   \"scope\":\"global\",   \"identifier\": {        \"name\": \"foreign_exchange-vanilla-forwards\"    } }

Response: {    \"data\": {        \"versions\": [            {                \"versionId\":\"0bmhRR-7hISwkb_H2MvIqafpJCAoy3YgEySZjntZF9o=\",                \"createdAt\": \"2022-08-22 15:23:44.0\"            }        ]    } }

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
    api_instance = openapi_client.UniqueKeyServiceApi(api_client)
    body = openapi_client.TitaniumGetDefinition() # TitaniumGetDefinition | 

    try:
        # ListUniqueKeyVersions is used to retrieve a list of all versions of a specific unique key definition by its scope and name. Request: {   \"scope\":\"global\",   \"identifier\": {        \"name\": \"foreign_exchange-vanilla-forwards\"    } }
        api_response = api_instance.unique_key_service_list_unique_key_versions(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UniqueKeyServiceApi->unique_key_service_list_unique_key_versions: %s\n" % e)
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

# **unique_key_service_list_unique_keys**
> TitaniumListUniqueKeysResponse unique_key_service_list_unique_keys(body)

ListUniqueKeys is used to retrieve a list of all unique key definitions in the system. Request: {   \"scope\":\"global\" }

Response: {    \"data\": {        \"results\": [            {                \"name\": \"foreign_exchange-vanilla-forwards\",                \"scope\": \"global\",                \"uniqueKey\": [                    \"asset\",                    \"service\",                    \"sub-asset\",                    \"instrument_type\",                    \"tenor\",                    \"snap_date\",                    \"snap_time\",                    \"curr_1\",                    \"curr_2\",                    \"onshore_offshore_curr_1\",                    \"onshore_offshore_curr_2\"                ],                \"orderBy\": [                    \"__input_row_num\"                ],                \"order\": \"ASC\"            },            {                \"name\": \"foreign_exchange-vanilla-options\",                \"scope\": \"global\",                \"uniqueKey\": [                    \"snap_date\",                    \"asset\",                    \"service\",                    \"snap_time\",                    \"instrument_type\",                    \"option_instrument_parameter\",                    \"exercise_style\",                    \"option_execution_cut_time\",                    \"curr_1\",                    \"curr_2\",                    \"tenor\",                    \"delta\",                    \"vol_format\",                    \"instrument_convention\",                    \"delta_convention\",                    \"premium_currency\",                    \"settlement_convention\"                ],                \"orderBy\": [                    \"__input_row_num\"                ],                \"order\": \"ASC\"            }        ]    } }

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
    api_instance = openapi_client.UniqueKeyServiceApi(api_client)
    body = openapi_client.TitaniumListRequest() # TitaniumListRequest | 

    try:
        # ListUniqueKeys is used to retrieve a list of all unique key definitions in the system. Request: {   \"scope\":\"global\" }
        api_response = api_instance.unique_key_service_list_unique_keys(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UniqueKeyServiceApi->unique_key_service_list_unique_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumListRequest**](TitaniumListRequest.md)|  | 

### Return type

[**TitaniumListUniqueKeysResponse**](TitaniumListUniqueKeysResponse.md)

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

