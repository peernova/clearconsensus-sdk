# openapi_client.GroupPolicyServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**group_policy_service_create**](GroupPolicyServiceApi.md#group_policy_service_create) | **POST** /api/v1/user-management/group-policies/create | 
[**group_policy_service_get_policies**](GroupPolicyServiceApi.md#group_policy_service_get_policies) | **POST** /api/v1/user-management/group-policies/getPolicies | 


# **group_policy_service_create**
> ProtoOperationSuccess group_policy_service_create(body)



### Example


```python
import time
import openapi_client
from openapi_client.api import group_policy_service_api
from openapi_client.model.proto_group_policies import ProtoGroupPolicies
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.proto_operation_success import ProtoOperationSuccess
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = group_policy_service_api.GroupPolicyServiceApi(api_client)
    body = ProtoGroupPolicies(
        group_policy=[
            ProtoGroupPolicyDto(
                group="group_example",
                type="type_example",
                username="username_example",
            ),
        ],
    ) # ProtoGroupPolicies | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.group_policy_service_create(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GroupPolicyServiceApi->group_policy_service_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProtoGroupPolicies**](ProtoGroupPolicies.md)|  |

### Return type

[**ProtoOperationSuccess**](ProtoOperationSuccess.md)

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

# **group_policy_service_get_policies**
> ProtoGroupPoliciesResponse group_policy_service_get_policies(body)



### Example


```python
import time
import openapi_client
from openapi_client.api import group_policy_service_api
from openapi_client.model.proto_policy_type import ProtoPolicyType
from openapi_client.model.rpc_status import RpcStatus
from openapi_client.model.proto_group_policies_response import ProtoGroupPoliciesResponse
from pprint import pprint
# Defining the host is optional and defaults to http://api-dev.clearconsensus.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api-dev.clearconsensus.io"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = group_policy_service_api.GroupPolicyServiceApi(api_client)
    body = ProtoPolicyType(
        type="type_example",
    ) # ProtoPolicyType | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.group_policy_service_get_policies(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GroupPolicyServiceApi->group_policy_service_get_policies: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProtoPolicyType**](ProtoPolicyType.md)|  |

### Return type

[**ProtoGroupPoliciesResponse**](ProtoGroupPoliciesResponse.md)

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

