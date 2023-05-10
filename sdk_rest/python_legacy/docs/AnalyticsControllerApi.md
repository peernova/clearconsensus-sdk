# openapi_client.AnalyticsControllerApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analytics_controller_find_consensus_analytics**](AnalyticsControllerApi.md#analytics_controller_find_consensus_analytics) | **POST** /api/v1/analytics/consensus/find | FindConsensusAnalytics returns analytics related to specific consensus according to request.
[**analytics_controller_find_data_quality_errors**](AnalyticsControllerApi.md#analytics_controller_find_data_quality_errors) | **POST** /api/v1/analytics/data-quality-errors/find | FindDataQualityErrors returns data quality errors according to request.
[**analytics_controller_get_all_consensus_analytics**](AnalyticsControllerApi.md#analytics_controller_get_all_consensus_analytics) | **POST** /api/v1/analytics/consensus/get-all | GetAllConsensusAnalytics returns analytics related to all consensuses.
[**analytics_controller_get_all_data_quality_errors**](AnalyticsControllerApi.md#analytics_controller_get_all_data_quality_errors) | **POST** /api/v1/analytics/data-quality-errors/get-all | GetAllDataQualityErrors returns all existing data quality errors in the system.
[**analytics_controller_get_histogram**](AnalyticsControllerApi.md#analytics_controller_get_histogram) | **POST** /api/v1/analytics/histogram/get-all | GetHistogram returns analytics(submission and consensus) represented by histogram according to request.
[**analytics_controller_get_predefined_filter**](AnalyticsControllerApi.md#analytics_controller_get_predefined_filter) | **POST** /api/v1/analytics/predefined/filters | GetPredefinedFilter returns pre defined filters according to request.


# **analytics_controller_find_consensus_analytics**
> TitaniumGenericChartMetadataDataQualityResponse analytics_controller_find_consensus_analytics(body)

FindConsensusAnalytics returns analytics related to specific consensus according to request.

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
    api_instance = openapi_client.AnalyticsControllerApi(api_client)
    body = openapi_client.TitaniumGenericChartMetadataDataQuality() # TitaniumGenericChartMetadataDataQuality | 

    try:
        # FindConsensusAnalytics returns analytics related to specific consensus according to request.
        api_response = api_instance.analytics_controller_find_consensus_analytics(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AnalyticsControllerApi->analytics_controller_find_consensus_analytics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumGenericChartMetadataDataQuality**](TitaniumGenericChartMetadataDataQuality.md)|  | 

### Return type

[**TitaniumGenericChartMetadataDataQualityResponse**](TitaniumGenericChartMetadataDataQualityResponse.md)

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

# **analytics_controller_find_data_quality_errors**
> TitaniumGenericChartMetadataDataQualityResponse analytics_controller_find_data_quality_errors(body)

FindDataQualityErrors returns data quality errors according to request.

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
    api_instance = openapi_client.AnalyticsControllerApi(api_client)
    body = openapi_client.TitaniumGenericChartMetadataDataQuality() # TitaniumGenericChartMetadataDataQuality | 

    try:
        # FindDataQualityErrors returns data quality errors according to request.
        api_response = api_instance.analytics_controller_find_data_quality_errors(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AnalyticsControllerApi->analytics_controller_find_data_quality_errors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitaniumGenericChartMetadataDataQuality**](TitaniumGenericChartMetadataDataQuality.md)|  | 

### Return type

[**TitaniumGenericChartMetadataDataQualityResponse**](TitaniumGenericChartMetadataDataQualityResponse.md)

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

# **analytics_controller_get_all_consensus_analytics**
> TitaniumGenericChartMetadataDataQualityResponse analytics_controller_get_all_consensus_analytics()

GetAllConsensusAnalytics returns analytics related to all consensuses.

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
    api_instance = openapi_client.AnalyticsControllerApi(api_client)
    
    try:
        # GetAllConsensusAnalytics returns analytics related to all consensuses.
        api_response = api_instance.analytics_controller_get_all_consensus_analytics()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AnalyticsControllerApi->analytics_controller_get_all_consensus_analytics: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TitaniumGenericChartMetadataDataQualityResponse**](TitaniumGenericChartMetadataDataQualityResponse.md)

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

# **analytics_controller_get_all_data_quality_errors**
> TitaniumGenericChartMetadataDataQualityResponse analytics_controller_get_all_data_quality_errors()

GetAllDataQualityErrors returns all existing data quality errors in the system.

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
    api_instance = openapi_client.AnalyticsControllerApi(api_client)
    
    try:
        # GetAllDataQualityErrors returns all existing data quality errors in the system.
        api_response = api_instance.analytics_controller_get_all_data_quality_errors()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AnalyticsControllerApi->analytics_controller_get_all_data_quality_errors: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TitaniumGenericChartMetadataDataQualityResponse**](TitaniumGenericChartMetadataDataQualityResponse.md)

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

# **analytics_controller_get_histogram**
> TitaniumHistogramResponse analytics_controller_get_histogram()

GetHistogram returns analytics(submission and consensus) represented by histogram according to request.

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
    api_instance = openapi_client.AnalyticsControllerApi(api_client)
    
    try:
        # GetHistogram returns analytics(submission and consensus) represented by histogram according to request.
        api_response = api_instance.analytics_controller_get_histogram()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AnalyticsControllerApi->analytics_controller_get_histogram: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TitaniumHistogramResponse**](TitaniumHistogramResponse.md)

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

# **analytics_controller_get_predefined_filter**
> TitaniumGetPredefinedFiltersResponse analytics_controller_get_predefined_filter()

GetPredefinedFilter returns pre defined filters according to request.

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
    api_instance = openapi_client.AnalyticsControllerApi(api_client)
    
    try:
        # GetPredefinedFilter returns pre defined filters according to request.
        api_response = api_instance.analytics_controller_get_predefined_filter()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AnalyticsControllerApi->analytics_controller_get_predefined_filter: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TitaniumGetPredefinedFiltersResponse**](TitaniumGetPredefinedFiltersResponse.md)

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

