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
import time
import openapi_client
from openapi_client.api import unique_key_service_api
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_unique_key_definition import TitaniumUniqueKeyDefinition
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
    api_instance = unique_key_service_api.UniqueKeyServiceApi(api_client)
    body = TitaniumUniqueKeyDefinition(
        name="name_example",
        order="order_example",
        order_by=[
            "order_by_example",
        ],
        scope="scope_example",
        unique_key=[
            "unique_key_example",
        ],
    ) # TitaniumUniqueKeyDefinition | 

    # example passing only required values which don't have defaults set
    try:
        # AddUniqueKey is used to add a new unique key definition to the system.
        api_response = api_instance.unique_key_service_add_unique_key(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
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
import time
import openapi_client
from openapi_client.api import unique_key_service_api
from openapi_client.model.titanium_get_definition import TitaniumGetDefinition
from openapi_client.model.titanium_unique_key_definition_response import TitaniumUniqueKeyDefinitionResponse
from openapi_client.model.rpc_status import RpcStatus
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = unique_key_service_api.UniqueKeyServiceApi(api_client)
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
        # GetUniqueKey is used to retrieve a unique key definition by its scope and name. Request: {   \"identifier\":{      \"name\":\"foreign_exchange-vanilla-forwards\"   },   \"scope\":\"global\" }
        api_response = api_instance.unique_key_service_get_unique_key(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
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
> TitaniumUniqueKeyDefinitionResponse unique_key_service_get_unique_key_version(scope, name, version_id)

GetUniqueKeyVersion is used to retrieve a specific version of a unique key definition by its scope, name, and version ID. Response: {    \"data\": {        \"name\": \"foreign_exchange-vanilla-forwards\",        \"scope\": \"global\",        \"uniqueKey\": [            \"asset\",            \"service\",            \"sub-asset\",            \"instrument_type\",            \"tenor\",            \"snap_date\",            \"snap_time\",            \"curr_1\",            \"curr_2\",            \"onshore_offshore_curr_1\",            \"onshore_offshore_curr_2\"        ],        \"orderBy\": [            \"__input_row_num\"        ],        \"order\": \"ASC\"    } }

### Example


```python
import time
import openapi_client
from openapi_client.api import unique_key_service_api
from openapi_client.model.titanium_unique_key_definition_response import TitaniumUniqueKeyDefinitionResponse
from openapi_client.model.rpc_status import RpcStatus
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = unique_key_service_api.UniqueKeyServiceApi(api_client)
    scope = "scope_example" # str | 
    name = "name_example" # str | 
    version_id = "versionId_example" # str | 
    descriptor_name = "descriptorName_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # GetUniqueKeyVersion is used to retrieve a specific version of a unique key definition by its scope, name, and version ID. Response: {    \"data\": {        \"name\": \"foreign_exchange-vanilla-forwards\",        \"scope\": \"global\",        \"uniqueKey\": [            \"asset\",            \"service\",            \"sub-asset\",            \"instrument_type\",            \"tenor\",            \"snap_date\",            \"snap_time\",            \"curr_1\",            \"curr_2\",            \"onshore_offshore_curr_1\",            \"onshore_offshore_curr_2\"        ],        \"orderBy\": [            \"__input_row_num\"        ],        \"order\": \"ASC\"    } }
        api_response = api_instance.unique_key_service_get_unique_key_version(scope, name, version_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UniqueKeyServiceApi->unique_key_service_get_unique_key_version: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # GetUniqueKeyVersion is used to retrieve a specific version of a unique key definition by its scope, name, and version ID. Response: {    \"data\": {        \"name\": \"foreign_exchange-vanilla-forwards\",        \"scope\": \"global\",        \"uniqueKey\": [            \"asset\",            \"service\",            \"sub-asset\",            \"instrument_type\",            \"tenor\",            \"snap_date\",            \"snap_time\",            \"curr_1\",            \"curr_2\",            \"onshore_offshore_curr_1\",            \"onshore_offshore_curr_2\"        ],        \"orderBy\": [            \"__input_row_num\"        ],        \"order\": \"ASC\"    } }
        api_response = api_instance.unique_key_service_get_unique_key_version(scope, name, version_id, descriptor_name=descriptor_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
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
import time
import openapi_client
from openapi_client.api import unique_key_service_api
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
    api_instance = unique_key_service_api.UniqueKeyServiceApi(api_client)
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
        # ListUniqueKeyVersions is used to retrieve a list of all versions of a specific unique key definition by its scope and name. Request: {   \"scope\":\"global\",   \"identifier\": {        \"name\": \"foreign_exchange-vanilla-forwards\"    } }
        api_response = api_instance.unique_key_service_list_unique_key_versions(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
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
import time
import openapi_client
from openapi_client.api import unique_key_service_api
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_list_unique_keys_response import TitaniumListUniqueKeysResponse
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
    api_instance = unique_key_service_api.UniqueKeyServiceApi(api_client)
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
        # ListUniqueKeys is used to retrieve a list of all unique key definitions in the system. Request: {   \"scope\":\"global\" }
        api_response = api_instance.unique_key_service_list_unique_keys(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
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

