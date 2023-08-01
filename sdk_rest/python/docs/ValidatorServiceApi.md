# openapi_client.ValidatorServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**validator_service_add_validation_rule**](ValidatorServiceApi.md#validator_service_add_validation_rule) | **POST** /api/v1/validation/rule/add | AddValidationRule is a method used to add a validation rule to the system. Backoffice users can create a new validation ruleset in the &#39;global&#39; scope, for each asset class. Participant users can create a new validation ruleset in its own scope, for each asset class. Backoffice users can represent any participant and create a new validation ruleset in that participant&#39;s scope. The default scope is used if no scope is given in the request (&#39;global&#39; for the operator, participant scope for that participant user). The authorization will be fetched from the user&#39;s token. It will do an update if a validation rule with the same name already exists.
[**validator_service_disable_validation_rule**](ValidatorServiceApi.md#validator_service_disable_validation_rule) | **POST** /api/v1/validation/rule/disable | DisableValidationRule method disables a validation rule in the system. The request includes the descriptor name and scope of the rule. Example of Request: { \&quot;descriptor_name\&quot; : \&quot;foreign_exchange-vanilla-forwards\&quot;, \&quot;scope\&quot;: \&quot;global\&quot; }
[**validator_service_enable_validation_rule**](ValidatorServiceApi.md#validator_service_enable_validation_rule) | **POST** /api/v1/validation/rule/enable | EnableValidationRule method enables a validation rule that has been previously disabled. The request includes the descriptor name and scope of the rule. Example of Request: { \&quot;descriptor_name\&quot; : \&quot;foreign_exchange-vanilla-forwards\&quot;, \&quot;scope\&quot;: \&quot;global\&quot; }
[**validator_service_get_generated_validation_rule**](ValidatorServiceApi.md#validator_service_get_generated_validation_rule) | **POST** /api/v1/validation/rule/generated | GetGeneratedValidationRule method allows back office users to view all generated validation rulesets, including Java rulesets. Participant users can only view global generated validation rulesets and rulesets within their own scope. If no scope is given in the request, the default scope is used (\&quot;global\&quot; for operators and participant scope for the participant user). Authorization is fetched from the user&#39;s token. This method returns the latest version of the generated ruleset if multiple versions exist.
[**validator_service_get_generated_validation_rule_version**](ValidatorServiceApi.md#validator_service_get_generated_validation_rule_version) | **GET** /api/v1/validation/rule/generated/version/{descriptorName}/{versionId} | GetGeneratedValidationRuleVersion method allows the user to view a particular version of a generated ruleset. The request requires a descriptor name and a version ID. If the requested ruleset version is not found, an error response is returned.
[**validator_service_get_validation_rule**](ValidatorServiceApi.md#validator_service_get_validation_rule) | **POST** /api/v1/validation/rule/get | GetValidationRule method retrieves information about a validation rule. Both back office users and participant users can view validation rulesets. The default scope is used if no scope is given in the request. Authorization is fetched from the user&#39;s token. The rule can be retrieved by either descriptor name or UID. If multiple versions of the rule exist, this method returns the latest version.
[**validator_service_get_validation_rule_version**](ValidatorServiceApi.md#validator_service_get_validation_rule_version) | **GET** /api/v1/validation/rule/version/{descriptorName}/{versionId} | This is a method that allows both back office users and regular users to retrieve a specific version of a ruleset given the descriptor name and version ID. The ruleset is used for validation purposes and contains criteria and rules for validating data submissions. Back office users can retrieve a particular version of a ruleset from any scope, while participant users can only retrieve a version of a ruleset from either the global scope or their own scope.
[**validator_service_list_generated_validation_rule_versions**](ValidatorServiceApi.md#validator_service_list_generated_validation_rule_versions) | **POST** /api/v1/validation/rule/generated/versions | ListGeneratedValidationRuleVersions method returns a list of generated ruleset version IDs along with their creation timestamps. The request requires a descriptor name. If the requested ruleset is not found, an error response is returned.
[**validator_service_list_validation_rule_versions**](ValidatorServiceApi.md#validator_service_list_validation_rule_versions) | **POST** /api/v1/validation/rule/versions | ListValidationRuleVersions method is used to retrieve a list of versions for a given validation rule. Both back office users and participant users can retrieve versions of validation rulesets, but the scope will depend on the user. The request must specify the descriptor name for the validation rule. The response will include a list of versions and their created timestamp. If the requested rule is not found, an error response will be returned.
[**validator_service_list_validation_rules**](ValidatorServiceApi.md#validator_service_list_validation_rules) | **POST** /api/v1/validation/rule/list | ListValidationRules method is used to retrieve a list of validation rule names. Both back office users and participant users can retrieve validation rulesets, but the scope and authorization will depend on the user. The default scope is used if no scope is specified in the request. The request may include an optional filter and orderBy parameter to refine the search results. Pagination is also supported. The response will include a list of rule names matching the filter criteria.
[**validator_service_rdl_check**](ValidatorServiceApi.md#validator_service_rdl_check) | **POST** /api/v1/validation/rule/check | RdlCheck method checks the syntax of a given RDL (Rule Description Language) expression. It takes a RdlCheckRequest message as input and returns a MessageResponse message.


# **validator_service_add_validation_rule**
> TitaniumAcknowledgeResponse validator_service_add_validation_rule(body)

AddValidationRule is a method used to add a validation rule to the system. Backoffice users can create a new validation ruleset in the 'global' scope, for each asset class. Participant users can create a new validation ruleset in its own scope, for each asset class. Backoffice users can represent any participant and create a new validation ruleset in that participant's scope. The default scope is used if no scope is given in the request ('global' for the operator, participant scope for that participant user). The authorization will be fetched from the user's token. It will do an update if a validation rule with the same name already exists.

Request for backoffice user: { \"definition\": {   \"descriptor_name\":\"foreign_exchange-vanilla-options\",   \"criteria\":[     {       \"name\":\"FX-V-FXO: Option Instrument Parameter: Forward Points\",       \"description\":\"This criteria element contains validation rules that will be applied to all fx-vanilla-options data submission rows where option_instrument_parameter equals \\\"Forward Points\\\".\",       \"tags\":[         \"forward points\"       ],       \"metadata\":[        ],       \"rule\":\"[\\\"foreign_exchange-vanilla-options.option_instrument_parameter\\\",\\\"$eq_case_insensitive\\\",\\\"Forward Points\\\"]\",       \"validations\":[         {           \"name\":\"FX-V-FXO: Forward Points: Forward Conversion Factor: Exiting Value Check\",           \"severity\":1,           \"rule_type\":\"input_data\",           \"tags\":[            ],           \"description\":\"Compare the fwrd_conversion_factor for a given underlying against the expected values.\",           \"rule\":\"[ { \\\"$lut_name\\\": \\\"conversion_factor\\\", \\\"$get\\\": [ \\\"foreign_exchange-vanilla-options.underlying\\\" ] }, \\\"$eq\\\", \\\"foreign_exchange-vanilla-options.fwrd_conversion_factor\\\" ]\",           \"error\":{             \"message\":\"[%s] is not a conversion factor used in consensus. Please update the conversion factor for this underlying -- [%s].\",             \"message_args\":[               \"foreign_exchange-vanilla-options.fwrd_conversion_factor\",               \"foreign_exchange-vanilla-options.underlying\"             ]           }         }       ]     }   ] }, \"scope\": \"global\", \"descriptor_name\": \"foreign_exchange-vanilla-options\" }  Response: {    \"data\": {        \"uid\": \"ac49453d-cc9c-11ec-8bac-5314d58ea570\",        \"descriptor_name\": \"fx_forward\"    } }  Error response:  Push to non ‘global’ scope : {    \"error\": {        \"code\": 70,        \"message\": \"Invalid argument: only support 'global' scope\"    } }  Unauthorized user : {    \"error\": {        \"code\": 70,        \"message\": \"Invalid auth token - only operator is allowed to add validation rules\"    } }  Missing argument : {    \"error\": {        \"code\": 70,        \"message\": \"Missing argument: descriptor_name\"    } }  Invalid rule definition - rule col mismatch with descriptor : {    \"error\": {        \"code\": 70,        \"message\": \"Rule [fx_fwd] compile failed, details: Column [submission_clienttt] not found in schema [fx_forward]\"    } }  Invalid rule definition - RDL syntax error : {    \"error\": {        \"code\": 70,        \"message\": \"Rule [fx_fwd] compile failed, details: line 1:14 no viable alternative at input '[{\\\"$lower\\\":\\\"fx_forward.submission_service\\\"'\"    } }  Dependencies not found - dependencies could be: descriptor, named lut, custom function : {    \"error\": {        \"code\": 70,        \"message\": \"Rule [fx_fwd] compile failed, details: Invalid rule expression [ { \\\"$lut_name\\\" : \\\"tenor\\\", \\\"$exist\\\" : [\\\"fx_forward.submission_tenor\\\"] } ]\\n\\terr: com.peernova.api.searchmetadata.metadata.exceptions.MetadataNotFoundException: No Look Up Table by name [tenor] found in scope [global]\"    } }  Ruleset with same name already exist : {    \"error\": {        \"code\": 70,        \"message\": \"Validation rule for descriptor [fx_fwd] already exist\"    } }

### Example


```python
import time
import openapi_client
from openapi_client.api import validator_service_api
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_acknowledge_response import TitaniumAcknowledgeResponse
from openapi_client.model.titanium_validation_rule_definition import TitaniumValidationRuleDefinition
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = validator_service_api.ValidatorServiceApi(api_client)
    body = TitaniumValidationRuleDefinition(
        definition=TitaniumRulesetDefinition(
            criteria=[
                TitaniumCriteriaDefinition(
                    description="description_example",
                    metadata=[
                        "metadata_example",
                    ],
                    name="name_example",
                    rule="rule_example",
                    tags=[
                        "tags_example",
                    ],
                    validations=[
                        TitaniumRuleDefinition(
                            description="description_example",
                            error=TitaniumErrorDefinition(
                                message="message_example",
                                message_args=[
                                    "message_args_example",
                                ],
                            ),
                            filter="filter_example",
                            lookuptable=TitaniumDynamicLut(
                                filter="filter_example",
                                key=[
                                    "key_example",
                                ],
                                type="type_example",
                                value={},
                            ),
                            name="name_example",
                            rule="rule_example",
                            rule_type="rule_type_example",
                            severity=1,
                            tags=[
                                "tags_example",
                            ],
                        ),
                    ],
                ),
            ],
            descriptor_name="descriptor_name_example",
        ),
        descriptor_name="descriptor_name_example",
        scope="scope_example",
        uid="uid_example",
    ) # TitaniumValidationRuleDefinition | 

    # example passing only required values which don't have defaults set
    try:
        # AddValidationRule is a method used to add a validation rule to the system. Backoffice users can create a new validation ruleset in the 'global' scope, for each asset class. Participant users can create a new validation ruleset in its own scope, for each asset class. Backoffice users can represent any participant and create a new validation ruleset in that participant's scope. The default scope is used if no scope is given in the request ('global' for the operator, participant scope for that participant user). The authorization will be fetched from the user's token. It will do an update if a validation rule with the same name already exists.
        api_response = api_instance.validator_service_add_validation_rule(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ValidatorServiceApi->validator_service_add_validation_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumValidationRuleDefinition**](TitaniumValidationRuleDefinition.md)|  |

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

# **validator_service_disable_validation_rule**
> TitaniumAcknowledgeResponse validator_service_disable_validation_rule(body)

DisableValidationRule method disables a validation rule in the system. The request includes the descriptor name and scope of the rule. Example of Request: { \"descriptor_name\" : \"foreign_exchange-vanilla-forwards\", \"scope\": \"global\" }

Example of Response: {    \"data\": {        \"uid\": \"\",        \"descriptor_name\": \"foreign_exchange-vanilla-forwards\"    } }

### Example


```python
import time
import openapi_client
from openapi_client.api import validator_service_api
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
    api_instance = validator_service_api.ValidatorServiceApi(api_client)
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
        # DisableValidationRule method disables a validation rule in the system. The request includes the descriptor name and scope of the rule. Example of Request: { \"descriptor_name\" : \"foreign_exchange-vanilla-forwards\", \"scope\": \"global\" }
        api_response = api_instance.validator_service_disable_validation_rule(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ValidatorServiceApi->validator_service_disable_validation_rule: %s\n" % e)
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

# **validator_service_enable_validation_rule**
> TitaniumAcknowledgeResponse validator_service_enable_validation_rule(body)

EnableValidationRule method enables a validation rule that has been previously disabled. The request includes the descriptor name and scope of the rule. Example of Request: { \"descriptor_name\" : \"foreign_exchange-vanilla-forwards\", \"scope\": \"global\" }

Example of Response: {    \"data\": {        \"uid\": \"\",        \"descriptor_name\": \"foreign_exchange-vanilla-forwards\"    } }

### Example


```python
import time
import openapi_client
from openapi_client.api import validator_service_api
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
    api_instance = validator_service_api.ValidatorServiceApi(api_client)
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
        # EnableValidationRule method enables a validation rule that has been previously disabled. The request includes the descriptor name and scope of the rule. Example of Request: { \"descriptor_name\" : \"foreign_exchange-vanilla-forwards\", \"scope\": \"global\" }
        api_response = api_instance.validator_service_enable_validation_rule(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ValidatorServiceApi->validator_service_enable_validation_rule: %s\n" % e)
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

# **validator_service_get_generated_validation_rule**
> TitaniumGetGeneratedValidationRuleResponse validator_service_get_generated_validation_rule(body)

GetGeneratedValidationRule method allows back office users to view all generated validation rulesets, including Java rulesets. Participant users can only view global generated validation rulesets and rulesets within their own scope. If no scope is given in the request, the default scope is used (\"global\" for operators and participant scope for the participant user). Authorization is fetched from the user's token. This method returns the latest version of the generated ruleset if multiple versions exist.

Example of Request: {  \"descriptor_name\": \"foreign_exchange-vanilla-forwards\" }

### Example


```python
import time
import openapi_client
from openapi_client.api import validator_service_api
from openapi_client.model.titanium_get_definition import TitaniumGetDefinition
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_get_generated_validation_rule_response import TitaniumGetGeneratedValidationRuleResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = validator_service_api.ValidatorServiceApi(api_client)
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
        # GetGeneratedValidationRule method allows back office users to view all generated validation rulesets, including Java rulesets. Participant users can only view global generated validation rulesets and rulesets within their own scope. If no scope is given in the request, the default scope is used (\"global\" for operators and participant scope for the participant user). Authorization is fetched from the user's token. This method returns the latest version of the generated ruleset if multiple versions exist.
        api_response = api_instance.validator_service_get_generated_validation_rule(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ValidatorServiceApi->validator_service_get_generated_validation_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumGetDefinition**](TitaniumGetDefinition.md)|  |

### Return type

[**TitaniumGetGeneratedValidationRuleResponse**](TitaniumGetGeneratedValidationRuleResponse.md)

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

# **validator_service_get_generated_validation_rule_version**
> TitaniumGetGeneratedValidationRuleResponse validator_service_get_generated_validation_rule_version(descriptor_name, version_id)

GetGeneratedValidationRuleVersion method allows the user to view a particular version of a generated ruleset. The request requires a descriptor name and a version ID. If the requested ruleset version is not found, an error response is returned.

Example of Request: GET /api/v1/validation/rule/generated/version/foreign_exchange-vanilla-forwards /QHF5uuOTjGprb3FRsI7ybBnU6-Ub32Xq8Q399PtQWeQ= {  \"scope\": \"global\" }  Example of Response: {     \"data\": {          \"versions\": [              {                 \"versionId\": \"teTYb9Fs_lIOoPQJukM6dY3aJdiMqT-SdBPdvYfJAjk=\",                 \"createdAt\": \"2022-05-04 16:20:58.0\"              },              {                  \"versionId\": \"mwpGZcWNc2zFgweB5rcNmAbcxqekM_zUCdpVrl_V6BM=\",                  \"createdAt\": \"2022-05-04 16:17:19.0\"              },              {                  \"versionId\": \"6pfCXN2rFnIAMoDHy7VIFh6HmoyDu3njXkpwzeTp2nc=\",                  \"createdAt\": \"2022-05-04 15:02:00.0\"              }          ]      }  }

### Example


```python
import time
import openapi_client
from openapi_client.api import validator_service_api
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_get_generated_validation_rule_response import TitaniumGetGeneratedValidationRuleResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = validator_service_api.ValidatorServiceApi(api_client)
    descriptor_name = "descriptorName_example" # str | 
    version_id = "versionId_example" # str | 
    name = "name_example" # str |  (optional)
    scope = "scope_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # GetGeneratedValidationRuleVersion method allows the user to view a particular version of a generated ruleset. The request requires a descriptor name and a version ID. If the requested ruleset version is not found, an error response is returned.
        api_response = api_instance.validator_service_get_generated_validation_rule_version(descriptor_name, version_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ValidatorServiceApi->validator_service_get_generated_validation_rule_version: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # GetGeneratedValidationRuleVersion method allows the user to view a particular version of a generated ruleset. The request requires a descriptor name and a version ID. If the requested ruleset version is not found, an error response is returned.
        api_response = api_instance.validator_service_get_generated_validation_rule_version(descriptor_name, version_id, name=name, scope=scope)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ValidatorServiceApi->validator_service_get_generated_validation_rule_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **descriptor_name** | **str**|  |
 **version_id** | **str**|  |
 **name** | **str**|  | [optional]
 **scope** | **str**|  | [optional]

### Return type

[**TitaniumGetGeneratedValidationRuleResponse**](TitaniumGetGeneratedValidationRuleResponse.md)

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

# **validator_service_get_validation_rule**
> TitaniumGetValidationRuleResponse validator_service_get_validation_rule(body)

GetValidationRule method retrieves information about a validation rule. Both back office users and participant users can view validation rulesets. The default scope is used if no scope is given in the request. Authorization is fetched from the user's token. The rule can be retrieved by either descriptor name or UID. If multiple versions of the rule exist, this method returns the latest version.

Example of Request: {  \"descriptor_name\": \"fx_fwd\" }   Or: {  \"uid\": \"ac49453d-cc9c-11ec-8bac-5314d58ea570\" }    Example of Response: {    \"data\": {        \"uid\": \"\",        \"definition\": {            \"descriptorName\": \"foreign_exchange-vanilla-options\",            \"criteria\": [                {                    \"name\": \"FX-V-FXO: Option Instrument Parameter: Forward Points\",                    \"description\": \"This criteria element contains validation rules that will be applied to all fx-vanilla-options data submission rows where option_instrument_parameter equals \\\"Forward Points\\\".\",                    \"rule\": \"[\\\"foreign_exchange-vanilla-options.option_instrument_parameter\\\",\\\"$eq_case_insensitive\\\",\\\"Forward Points\\\"]\",                    \"tags\": [                        \"forward points\"                    ],                    \"metadata\": [],                    \"validations\": [                        {                            \"name\": \"FX-V-FXO: Forward Points: Forward Conversion Factor: Exiting Value Check\",                            \"description\": \"Compare the fwrd_conversion_factor for a given underlying against the expected values.\",                            \"rule\": \"[ { \\\"$lut_name\\\": \\\"conversion_factor\\\", \\\"$get\\\": [ \\\"foreign_exchange-vanilla-options.underlying\\\" ] }, \\\"$eq\\\", \\\"foreign_exchange-vanilla-options.fwrd_conversion_factor\\\" ]\",                            \"ruleType\": \"INPUT_DATA\",                            \"severity\": 1,                            \"tags\": [],                            \"error\": {                                \"message\": \"[%s] is not a conversion factor used in consensus. Please update the conversion factor for this underlying -- [%s].\",                                \"messageArgs\": [                                    \"foreign_exchange-vanilla-options.fwrd_conversion_factor\",                                    \"foreign_exchange-vanilla-options.underlying\"                                ]                            },                            \"filter\": \"\"                        }                    ]                }            ]        },        \"scope\": \"global\",        \"descriptorName\": \"foreign_exchange-vanilla-options\"    } }  Example of Error response:  Missing argument: {    \"error\": {        \"code\": 70,        \"message\": \"Missing argument: need either descriptor name or uid to get validation rule\"    } }  Resource not found : {    \"error\": {        \"code\": 70,        \"message\": \"Rule [fx_fwd] not found, details: [fx_fwd] of service [VALIDATIONRULESET] does not exist in namespace [global]\"    } }

### Example


```python
import time
import openapi_client
from openapi_client.api import validator_service_api
from openapi_client.model.titanium_get_validation_rule_response import TitaniumGetValidationRuleResponse
from openapi_client.model.titanium_get_definition import TitaniumGetDefinition
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
    api_instance = validator_service_api.ValidatorServiceApi(api_client)
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
        # GetValidationRule method retrieves information about a validation rule. Both back office users and participant users can view validation rulesets. The default scope is used if no scope is given in the request. Authorization is fetched from the user's token. The rule can be retrieved by either descriptor name or UID. If multiple versions of the rule exist, this method returns the latest version.
        api_response = api_instance.validator_service_get_validation_rule(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ValidatorServiceApi->validator_service_get_validation_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumGetDefinition**](TitaniumGetDefinition.md)|  |

### Return type

[**TitaniumGetValidationRuleResponse**](TitaniumGetValidationRuleResponse.md)

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

# **validator_service_get_validation_rule_version**
> TitaniumGetValidationRuleResponse validator_service_get_validation_rule_version(descriptor_name, version_id)

This is a method that allows both back office users and regular users to retrieve a specific version of a ruleset given the descriptor name and version ID. The ruleset is used for validation purposes and contains criteria and rules for validating data submissions. Back office users can retrieve a particular version of a ruleset from any scope, while participant users can only retrieve a version of a ruleset from either the global scope or their own scope.

Example of Request: GET /api/v1/validation/rule/version/fx_fwd_May04/teTYb9Fs_lIOoPQJukM6dY3aJdiMqT-SdBPdvYfJAjk=  Example of Response: {    \"data\": {        \"uid\": \"\",        \"definition\": {            \"descriptorName\": \"foreign_exchange-vanilla-options\",            \"criteria\": [                {                    \"name\": \"FX-V-FXO: Option Instrument Parameter: Forward Points\",                    \"description\": \"This criteria element contains validation rules that will be applied to all fx-vanilla-options data submission rows where option_instrument_parameter equals \\\"Forward Points\\\".\",                    \"rule\": \"[\\\"foreign_exchange-vanilla-options.option_instrument_parameter\\\",\\\"$eq_case_insensitive\\\",\\\"Forward Points\\\"]\",                    \"tags\": [                        \"forward points\"                    ],                    \"metadata\": [],                    \"validations\": [                        {                            \"name\": \"FX-V-FXO: Forward Points: Forward Conversion Factor: Exiting Value Check\",                            \"description\": \"Compare the fwrd_conversion_factor for a given underlying against the expected values.\",                            \"rule\": \"[ { \\\"$lut_name\\\": \\\"conversion_factor\\\", \\\"$get\\\": [ \\\"foreign_exchange-vanilla-options.underlying\\\" ] }, \\\"$eq\\\", \\\"foreign_exchange-vanilla-options.fwrd_conversion_factor\\\" ]\",                            \"ruleType\": \"INPUT_DATA\",                            \"severity\": 1,                            \"tags\": [],                            \"error\": {                                \"message\": \"[%s] is not a conversion factor used in consensus. Please update the conversion factor for this underlying -- [%s].\",                                \"messageArgs\": [                                    \"foreign_exchange-vanilla-options.fwrd_conversion_factor\",                                    \"foreign_exchange-vanilla-options.underlying\"                                ]                            },                            \"filter\": \"\"                        }                    ]                }            ]        },        \"scope\": \"global\",        \"descriptorName\": \"foreign_exchange-vanilla-options\"    } }  Example of Error response: Resource not found: {    \"error\": {        \"code\": 70,        \"message\": \"Failed to get rule [fx_fwd_May04], details: MetaData entity not found: name [fx_fwd_May04] version: [teTYb9Fs_lIOoPQJukM6dY3aJdiMqT-SdBPdvYfJAjk] in namespace: [global]\"    } }

### Example


```python
import time
import openapi_client
from openapi_client.api import validator_service_api
from openapi_client.model.titanium_get_validation_rule_response import TitaniumGetValidationRuleResponse
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
    api_instance = validator_service_api.ValidatorServiceApi(api_client)
    descriptor_name = "descriptorName_example" # str | 
    version_id = "versionId_example" # str | 
    name = "name_example" # str |  (optional)
    scope = "scope_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # This is a method that allows both back office users and regular users to retrieve a specific version of a ruleset given the descriptor name and version ID. The ruleset is used for validation purposes and contains criteria and rules for validating data submissions. Back office users can retrieve a particular version of a ruleset from any scope, while participant users can only retrieve a version of a ruleset from either the global scope or their own scope.
        api_response = api_instance.validator_service_get_validation_rule_version(descriptor_name, version_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ValidatorServiceApi->validator_service_get_validation_rule_version: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # This is a method that allows both back office users and regular users to retrieve a specific version of a ruleset given the descriptor name and version ID. The ruleset is used for validation purposes and contains criteria and rules for validating data submissions. Back office users can retrieve a particular version of a ruleset from any scope, while participant users can only retrieve a version of a ruleset from either the global scope or their own scope.
        api_response = api_instance.validator_service_get_validation_rule_version(descriptor_name, version_id, name=name, scope=scope)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ValidatorServiceApi->validator_service_get_validation_rule_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **descriptor_name** | **str**|  |
 **version_id** | **str**|  |
 **name** | **str**|  | [optional]
 **scope** | **str**|  | [optional]

### Return type

[**TitaniumGetValidationRuleResponse**](TitaniumGetValidationRuleResponse.md)

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

# **validator_service_list_generated_validation_rule_versions**
> TitaniumListVersionResponse validator_service_list_generated_validation_rule_versions(body)

ListGeneratedValidationRuleVersions method returns a list of generated ruleset version IDs along with their creation timestamps. The request requires a descriptor name. If the requested ruleset is not found, an error response is returned.

Example of Request: {  \"descriptor_name\": \"fx_fwd\" }   Example of Response: {    \"data\": {        \"versions\": [            {                \"versionId\": \"teTYb9Fs_lIOoPQJukM6dY3aJdiMqT-SdBPdvYfJAjk=\",                \"createdAt\": \"2022-05-04 16:20:58.0\"            },            {                \"versionId\": \"mwpGZcWNc2zFgweB5rcNmAbcxqekM_zUCdpVrl_V6BM=\",                \"createdAt\": \"2022-05-04 16:17:19.0\"            },            {                \"versionId\": \"6pfCXN2rFnIAMoDHy7VIFh6HmoyDu3njXkpwzeTp2nc=\",                \"createdAt\": \"2022-05-04 15:02:00.0\"            }        ]    } }  Example of Error response: Resource not found: {    \"error\": {        \"code\": 70,        \"message\": \"Failed to get rule [fx_fwd] versions, details: Rule [fx_fwd] not found\"    } }

### Example


```python
import time
import openapi_client
from openapi_client.api import validator_service_api
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
    api_instance = validator_service_api.ValidatorServiceApi(api_client)
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
        # ListGeneratedValidationRuleVersions method returns a list of generated ruleset version IDs along with their creation timestamps. The request requires a descriptor name. If the requested ruleset is not found, an error response is returned.
        api_response = api_instance.validator_service_list_generated_validation_rule_versions(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ValidatorServiceApi->validator_service_list_generated_validation_rule_versions: %s\n" % e)
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

# **validator_service_list_validation_rule_versions**
> TitaniumListVersionResponse validator_service_list_validation_rule_versions(body)

ListValidationRuleVersions method is used to retrieve a list of versions for a given validation rule. Both back office users and participant users can retrieve versions of validation rulesets, but the scope will depend on the user. The request must specify the descriptor name for the validation rule. The response will include a list of versions and their created timestamp. If the requested rule is not found, an error response will be returned.

Example of Request: {  \"descriptor_name\": \"fx_fwd\" }  Example of Response: {    \"data\": {        \"versions\": [            {                \"versionId\": \"teTYb9Fs_lIOoPQJukM6dY3aJdiMqT-SdBPdvYfJAjk=\",                \"createdAt\": \"2022-05-04 16:20:58.0\"            },            {                \"versionId\": \"mwpGZcWNc2zFgweB5rcNmAbcxqekM_zUCdpVrl_V6BM=\",                \"createdAt\": \"2022-05-04 16:17:19.0\"            },            {                \"versionId\": \"6pfCXN2rFnIAMoDHy7VIFh6HmoyDu3njXkpwzeTp2nc=\",                \"createdAt\": \"2022-05-04 15:02:00.0\"            }        ]    } }  Example of Error response: Resource not found: {    \"error\": {        \"code\": 70,        \"message\": \"Failed to get rule [fx_fwd] versions, details: Rule [fx_fwd_validation] not found\"    } }

### Example


```python
import time
import openapi_client
from openapi_client.api import validator_service_api
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
    api_instance = validator_service_api.ValidatorServiceApi(api_client)
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
        # ListValidationRuleVersions method is used to retrieve a list of versions for a given validation rule. Both back office users and participant users can retrieve versions of validation rulesets, but the scope will depend on the user. The request must specify the descriptor name for the validation rule. The response will include a list of versions and their created timestamp. If the requested rule is not found, an error response will be returned.
        api_response = api_instance.validator_service_list_validation_rule_versions(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ValidatorServiceApi->validator_service_list_validation_rule_versions: %s\n" % e)
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

# **validator_service_list_validation_rules**
> TitaniumListRuleResponse validator_service_list_validation_rules(body)

ListValidationRules method is used to retrieve a list of validation rule names. Both back office users and participant users can retrieve validation rulesets, but the scope and authorization will depend on the user. The default scope is used if no scope is specified in the request. The request may include an optional filter and orderBy parameter to refine the search results. Pagination is also supported. The response will include a list of rule names matching the filter criteria.

Example of Request: {  \"scope\": \"global\",  \"filter\": \".*exchange.*\",  \"orderBy\": {   \"order\": \"DESC\"  } }  Example of Response: {    \"data\": {        \"results\": [            {                \"uid\": \"\",                \"descriptor_name\": \"foreign_exchange-vanilla-options\"            },            {                \"uid\": \"\",                \"descriptor_name\": \"foreign_exchange-vanilla-forwards\"            },            {                \"uid\": \"\",                \"descriptor_name\": \"foreign_exchange-exotics-tarfs\"            }        ]    } }  Example of Request with pagination: {  \"scope\": \"global\",  \"filter\": \".*exchange.*\",  \"orderBy\": {   \"order\": \"DESC\"  },  \"limit\": {   \"value\": 2  },  \"offset\": 1 }  Example of Response: {    \"data\": {        \"results\": [            {                \"uid\": \"\",                \"descriptor_name\": \"foreign_exchange-vanilla-forwards\"            },            {                \"uid\": \"\",                \"descriptor_name\": \"foreign_exchange-exotics-tarfs\"            }        ]    } }  Example of Error response: not ‘global’ scope: {    \"error\": {        \"code\": 70,        \"message\": \"Invalid argument: only support 'global' scope\"    } }  Invalid filter/regex: {    \"error\": {        \"code\": 70,        \"message\": \"Failed to list rules: Dangling meta character '*' near index 0\\n*May*\\n^\"    } }

### Example


```python
import time
import openapi_client
from openapi_client.api import validator_service_api
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
    api_instance = validator_service_api.ValidatorServiceApi(api_client)
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
        # ListValidationRules method is used to retrieve a list of validation rule names. Both back office users and participant users can retrieve validation rulesets, but the scope and authorization will depend on the user. The default scope is used if no scope is specified in the request. The request may include an optional filter and orderBy parameter to refine the search results. Pagination is also supported. The response will include a list of rule names matching the filter criteria.
        api_response = api_instance.validator_service_list_validation_rules(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ValidatorServiceApi->validator_service_list_validation_rules: %s\n" % e)
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

# **validator_service_rdl_check**
> TitaniumMessageResponse validator_service_rdl_check(body)

RdlCheck method checks the syntax of a given RDL (Rule Description Language) expression. It takes a RdlCheckRequest message as input and returns a MessageResponse message.

Example of Request: {  \"rdl\": \"[\\\"a\\\", \\\"$eq\\\", \\\"b\\\"\" }  Example of Response: {    \"data\": {        \"message\": \"success\"    } }  Example of Error response: Resource not found: {    \"error\": {        \"code\": 69,        \"message\": \"rdl [[\\\"a\\\", \\\"$eq\\\", \\\"b\\\"] cannot be parsed. Error: line 1:16 missing ']' at '<EOF>'\"    } }

### Example


```python
import time
import openapi_client
from openapi_client.api import validator_service_api
from openapi_client.model.titanium_message_response import TitaniumMessageResponse
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.titanium_rdl_check_request import TitaniumRdlCheckRequest
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = validator_service_api.ValidatorServiceApi(api_client)
    body = TitaniumRdlCheckRequest(
        rdl="rdl_example",
    ) # TitaniumRdlCheckRequest | 

    # example passing only required values which don't have defaults set
    try:
        # RdlCheck method checks the syntax of a given RDL (Rule Description Language) expression. It takes a RdlCheckRequest message as input and returns a MessageResponse message.
        api_response = api_instance.validator_service_rdl_check(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ValidatorServiceApi->validator_service_rdl_check: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumRdlCheckRequest**](TitaniumRdlCheckRequest.md)|  |

### Return type

[**TitaniumMessageResponse**](TitaniumMessageResponse.md)

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

