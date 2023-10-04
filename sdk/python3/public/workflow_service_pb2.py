"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ..google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2
from ..common import workflow_pb2 as common_dot_workflow__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dpublic/workflow_service.proto\x12\x08titanium\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x19common/gateway_base.proto\x1a\x15common/workflow.proto2\x9e\x08\n\x0fWorkflowService\x12k\n\x0bRunWorkflow\x12\x1c.titanium.RunWorkflowRequest\x1a\x1d.titanium.RunWorkflowResponse"\x1f\x82\xd3\xe4\x93\x02\x19"\x14/api/v1/workflow/run:\x01*\x12}\n\x11ReprocessWorkflow\x12".titanium.ReprocessWorkflowRequest\x1a\x1d.titanium.RunWorkflowResponse"%\x82\xd3\xe4\x93\x02\x1f"\x1a/api/v1/workflow/reprocess:\x01*\x12u\n\x0bAddWorkflow\x12&.titanium.AddWorkflowDefinitionRequest\x1a\x1d.titanium.AcknowledgeResponse"\x1f\x82\xd3\xe4\x93\x02\x19"\x14/api/v1/workflow/add:\x01*\x12m\n\x0bGetWorkflow\x12\x17.titanium.GetDefinition\x1a$.titanium.WorkflowDefinitionResponse"\x1f\x82\xd3\xe4\x93\x02\x19"\x14/api/v1/workflow/get:\x01*\x12`\n\rListWorkflows\x12\x15.titanium.ListRequest\x1a\x16.titanium.WorkflowList" \x82\xd3\xe4\x93\x02\x1a"\x15/api/v1/workflow/list:\x01*\x12s\n\x0eEnableWorkflow\x12\x1e.titanium.EnableDisableRequest\x1a\x1d.titanium.AcknowledgeResponse""\x82\xd3\xe4\x93\x02\x1c"\x17/api/v1/workflow/enable:\x01*\x12u\n\x0fDisableWorkflow\x12\x1e.titanium.EnableDisableRequest\x1a\x1d.titanium.AcknowledgeResponse"#\x82\xd3\xe4\x93\x02\x1d"\x18/api/v1/workflow/disable:\x01*\x12m\n\x13ListWorkflowActions\x12\x15.titanium.ListRequest\x1a\x16.titanium.WorkflowList"\'\x82\xd3\xe4\x93\x02!"\x1c/api/v1/workflow/action/list:\x01*\x12|\n\x11GetWorkflowAction\x12\x1a.titanium.GetActionRequest\x1a#.titanium.GetWorkflowActionResponse"&\x82\xd3\xe4\x93\x02 \x12\x1e/api/v1/workflow/action/{name}Bo\n com.peernova.titanium.interfacesB\x13WorkflowProtoPublicP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/publicb\x06proto3')
_WORKFLOWSERVICE = DESCRIPTOR.services_by_name['WorkflowService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesB\x13WorkflowProtoPublicP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/public'
    _WORKFLOWSERVICE.methods_by_name['RunWorkflow']._options = None
    _WORKFLOWSERVICE.methods_by_name['RunWorkflow']._serialized_options = b'\x82\xd3\xe4\x93\x02\x19"\x14/api/v1/workflow/run:\x01*'
    _WORKFLOWSERVICE.methods_by_name['ReprocessWorkflow']._options = None
    _WORKFLOWSERVICE.methods_by_name['ReprocessWorkflow']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1f"\x1a/api/v1/workflow/reprocess:\x01*'
    _WORKFLOWSERVICE.methods_by_name['AddWorkflow']._options = None
    _WORKFLOWSERVICE.methods_by_name['AddWorkflow']._serialized_options = b'\x82\xd3\xe4\x93\x02\x19"\x14/api/v1/workflow/add:\x01*'
    _WORKFLOWSERVICE.methods_by_name['GetWorkflow']._options = None
    _WORKFLOWSERVICE.methods_by_name['GetWorkflow']._serialized_options = b'\x82\xd3\xe4\x93\x02\x19"\x14/api/v1/workflow/get:\x01*'
    _WORKFLOWSERVICE.methods_by_name['ListWorkflows']._options = None
    _WORKFLOWSERVICE.methods_by_name['ListWorkflows']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1a"\x15/api/v1/workflow/list:\x01*'
    _WORKFLOWSERVICE.methods_by_name['EnableWorkflow']._options = None
    _WORKFLOWSERVICE.methods_by_name['EnableWorkflow']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1c"\x17/api/v1/workflow/enable:\x01*'
    _WORKFLOWSERVICE.methods_by_name['DisableWorkflow']._options = None
    _WORKFLOWSERVICE.methods_by_name['DisableWorkflow']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1d"\x18/api/v1/workflow/disable:\x01*'
    _WORKFLOWSERVICE.methods_by_name['ListWorkflowActions']._options = None
    _WORKFLOWSERVICE.methods_by_name['ListWorkflowActions']._serialized_options = b'\x82\xd3\xe4\x93\x02!"\x1c/api/v1/workflow/action/list:\x01*'
    _WORKFLOWSERVICE.methods_by_name['GetWorkflowAction']._options = None
    _WORKFLOWSERVICE.methods_by_name['GetWorkflowAction']._serialized_options = b'\x82\xd3\xe4\x93\x02 \x12\x1e/api/v1/workflow/action/{name}'
    _WORKFLOWSERVICE._serialized_start = 153
    _WORKFLOWSERVICE._serialized_end = 1207