# ClearconsensusSdk.WorkflowServiceApi

All URIs are relative to *http://api-dev.clearconsensus.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workflowServiceAddWorkflow**](WorkflowServiceApi.md#workflowServiceAddWorkflow) | **POST** /api/v1/workflow/add | 
[**workflowServiceDisableWorkflow**](WorkflowServiceApi.md#workflowServiceDisableWorkflow) | **POST** /api/v1/workflow/disable | 
[**workflowServiceEnableWorkflow**](WorkflowServiceApi.md#workflowServiceEnableWorkflow) | **POST** /api/v1/workflow/enable | 
[**workflowServiceGetWorkflow**](WorkflowServiceApi.md#workflowServiceGetWorkflow) | **POST** /api/v1/workflow/get | 
[**workflowServiceGetWorkflowAction**](WorkflowServiceApi.md#workflowServiceGetWorkflowAction) | **GET** /api/v1/workflow/action/{name} | 
[**workflowServiceListWorkflowActions**](WorkflowServiceApi.md#workflowServiceListWorkflowActions) | **POST** /api/v1/workflow/action/list | 
[**workflowServiceListWorkflows**](WorkflowServiceApi.md#workflowServiceListWorkflows) | **POST** /api/v1/workflow/list | 
[**workflowServiceReprocessWorkflow**](WorkflowServiceApi.md#workflowServiceReprocessWorkflow) | **POST** /api/v1/workflow/reprocess | 
[**workflowServiceRunWorkflow**](WorkflowServiceApi.md#workflowServiceRunWorkflow) | **POST** /api/v1/workflow/run | 



## workflowServiceAddWorkflow

> TitaniumAcknowledgeResponse workflowServiceAddWorkflow(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.WorkflowServiceApi();
let body = new ClearconsensusSdk.TitaniumAddWorkflowDefinitionRequest(); // TitaniumAddWorkflowDefinitionRequest | 
apiInstance.workflowServiceAddWorkflow(body, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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


## workflowServiceDisableWorkflow

> TitaniumAcknowledgeResponse workflowServiceDisableWorkflow(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.WorkflowServiceApi();
let body = new ClearconsensusSdk.TitaniumEnableDisableRequest(); // TitaniumEnableDisableRequest | 
apiInstance.workflowServiceDisableWorkflow(body, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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


## workflowServiceEnableWorkflow

> TitaniumAcknowledgeResponse workflowServiceEnableWorkflow(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.WorkflowServiceApi();
let body = new ClearconsensusSdk.TitaniumEnableDisableRequest(); // TitaniumEnableDisableRequest | 
apiInstance.workflowServiceEnableWorkflow(body, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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


## workflowServiceGetWorkflow

> TitaniumWorkflowDefinitionResponse workflowServiceGetWorkflow(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.WorkflowServiceApi();
let body = new ClearconsensusSdk.TitaniumGetDefinition(); // TitaniumGetDefinition | 
apiInstance.workflowServiceGetWorkflow(body, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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


## workflowServiceGetWorkflowAction

> TitaniumGetWorkflowActionResponse workflowServiceGetWorkflowAction(name)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.WorkflowServiceApi();
let name = "name_example"; // String | 
apiInstance.workflowServiceGetWorkflowAction(name, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**|  | 

### Return type

[**TitaniumGetWorkflowActionResponse**](TitaniumGetWorkflowActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## workflowServiceListWorkflowActions

> TitaniumWorkflowList workflowServiceListWorkflowActions(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.WorkflowServiceApi();
let body = new ClearconsensusSdk.TitaniumListRequest(); // TitaniumListRequest | 
apiInstance.workflowServiceListWorkflowActions(body, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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


## workflowServiceListWorkflows

> TitaniumWorkflowList workflowServiceListWorkflows(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.WorkflowServiceApi();
let body = new ClearconsensusSdk.TitaniumListRequest(); // TitaniumListRequest | 
apiInstance.workflowServiceListWorkflows(body, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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


## workflowServiceReprocessWorkflow

> TitaniumRunWorkflowResponse workflowServiceReprocessWorkflow(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.WorkflowServiceApi();
let body = new ClearconsensusSdk.TitaniumReprocessWorkflowRequest(); // TitaniumReprocessWorkflowRequest | 
apiInstance.workflowServiceReprocessWorkflow(body, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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


## workflowServiceRunWorkflow

> TitaniumRunWorkflowResponse workflowServiceRunWorkflow(body)



### Example

```javascript
import ClearconsensusSdk from 'clearconsensus_sdk';

let apiInstance = new ClearconsensusSdk.WorkflowServiceApi();
let body = new ClearconsensusSdk.TitaniumRunWorkflowRequest(); // TitaniumRunWorkflowRequest | 
apiInstance.workflowServiceRunWorkflow(body, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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

