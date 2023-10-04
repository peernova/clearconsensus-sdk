"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ..google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15common/workflow.proto\x12\x08titanium\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x19google/protobuf/any.proto\x1a\x19common/gateway_base.proto"X\n\x12RunWorkflowRequest\x12\r\n\x05scope\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12%\n\x04args\x18\x03 \x01(\x0b2\x17.google.protobuf.Struct"?\n\x18ReprocessWorkflowRequest\x12\x13\n\x0bworkflow_id\x18\x01 \x01(\t\x12\x0e\n\x06run_id\x18\x02 \x01(\t" \n\x10GetActionRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"8\n\x13RunWorkflowResponse\x12\x12\n\nworkflowId\x18\x01 \x01(\t\x12\r\n\x05runId\x18\x02 \x01(\t"_\n\x1cAddWorkflowDefinitionRequest\x12\r\n\x05scope\x18\x01 \x01(\t\x120\n\ndefinition\x18\x02 \x01(\x0b2\x1c.titanium.WorkflowDefinition"`\n\x1aWorkflowDefinitionResponse\x12\x14\n\ndefinition\x18\x01 \x01(\tH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"\xff\x01\n\x12WorkflowDefinition\x12\x15\n\rworkflow_name\x18\x01 \x01(\t\x12\x16\n\x0eworkflow_queue\x18\x02 \x01(\t\x12\x0f\n\x07timeout\x18\x03 \x01(\x03\x12\x10\n\x08schedule\x18\x04 \x01(\t\x12\x14\n\x0cmax_attempts\x18\x05 \x01(\x05\x12/\n\x0baction_list\x18\x06 \x03(\x0b2\x1a.titanium.ActionDefinition\x125\n\x14predefined_arguments\x18\x07 \x01(\x0b2\x17.google.protobuf.Struct\x12\x19\n\x11runtime_arguments\x18\x08 \x03(\t"\x85\x02\n\x10ActionDefinition\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\ndepends_on\x18\x02 \x03(\t\x12\x13\n\x0baction_type\x18\x03 \x01(\t\x12\r\n\x05queue\x18\x04 \x01(\t\x12\x17\n\x0ftimeout_seconds\x18\x05 \x01(\x05\x12\x0f\n\x07retries\x18\x06 \x01(\x05\x12\x16\n\x0eignore_failure\x18\x07 \x01(\x08\x12\x0e\n\x06run_if\x18\x08 \x01(\t\x12\x15\n\rdo_not_run_if\x18\t \x01(\t\x12+\n\x0finput_arguments\x18\n \x03(\x0b2\x12.titanium.Argument\x12\x17\n\x0foutput_argument\x18\x0b \x01(\t"e\n\x08Argument\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08variable\x18\x02 \x01(\t\x12%\n\x05value\x18\x03 \x01(\x0b2\x16.google.protobuf.Value\x12\x12\n\ndefinition\x18\x04 \x01(\t"b\n\x19GetWorkflowActionResponse\x12\x13\n\x0bdescription\x18\x01 \x01(\t\x12\x17\n\x0finput_arguments\x18\x02 \x03(\t\x12\x17\n\x0foutput_argument\x18\x03 \x01(\t"c\n\x0cWorkflowList\x12%\n\x04data\x18\x01 \x01(\x0b2\x15.titanium.ResultsListH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"G\n\x16WorkflowDefinitionList\x12-\n\x07results\x18\x01 \x03(\x0b2\x1c.titanium.WorkflowDefinitionBo\n com.peernova.titanium.interfacesB\x13WorkflowProtoCommonP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/commonb\x06proto3')
_RUNWORKFLOWREQUEST = DESCRIPTOR.message_types_by_name['RunWorkflowRequest']
_REPROCESSWORKFLOWREQUEST = DESCRIPTOR.message_types_by_name['ReprocessWorkflowRequest']
_GETACTIONREQUEST = DESCRIPTOR.message_types_by_name['GetActionRequest']
_RUNWORKFLOWRESPONSE = DESCRIPTOR.message_types_by_name['RunWorkflowResponse']
_ADDWORKFLOWDEFINITIONREQUEST = DESCRIPTOR.message_types_by_name['AddWorkflowDefinitionRequest']
_WORKFLOWDEFINITIONRESPONSE = DESCRIPTOR.message_types_by_name['WorkflowDefinitionResponse']
_WORKFLOWDEFINITION = DESCRIPTOR.message_types_by_name['WorkflowDefinition']
_ACTIONDEFINITION = DESCRIPTOR.message_types_by_name['ActionDefinition']
_ARGUMENT = DESCRIPTOR.message_types_by_name['Argument']
_GETWORKFLOWACTIONRESPONSE = DESCRIPTOR.message_types_by_name['GetWorkflowActionResponse']
_WORKFLOWLIST = DESCRIPTOR.message_types_by_name['WorkflowList']
_WORKFLOWDEFINITIONLIST = DESCRIPTOR.message_types_by_name['WorkflowDefinitionList']
RunWorkflowRequest = _reflection.GeneratedProtocolMessageType('RunWorkflowRequest', (_message.Message,), {'DESCRIPTOR': _RUNWORKFLOWREQUEST, '__module__': 'common.workflow_pb2'})
_sym_db.RegisterMessage(RunWorkflowRequest)
ReprocessWorkflowRequest = _reflection.GeneratedProtocolMessageType('ReprocessWorkflowRequest', (_message.Message,), {'DESCRIPTOR': _REPROCESSWORKFLOWREQUEST, '__module__': 'common.workflow_pb2'})
_sym_db.RegisterMessage(ReprocessWorkflowRequest)
GetActionRequest = _reflection.GeneratedProtocolMessageType('GetActionRequest', (_message.Message,), {'DESCRIPTOR': _GETACTIONREQUEST, '__module__': 'common.workflow_pb2'})
_sym_db.RegisterMessage(GetActionRequest)
RunWorkflowResponse = _reflection.GeneratedProtocolMessageType('RunWorkflowResponse', (_message.Message,), {'DESCRIPTOR': _RUNWORKFLOWRESPONSE, '__module__': 'common.workflow_pb2'})
_sym_db.RegisterMessage(RunWorkflowResponse)
AddWorkflowDefinitionRequest = _reflection.GeneratedProtocolMessageType('AddWorkflowDefinitionRequest', (_message.Message,), {'DESCRIPTOR': _ADDWORKFLOWDEFINITIONREQUEST, '__module__': 'common.workflow_pb2'})
_sym_db.RegisterMessage(AddWorkflowDefinitionRequest)
WorkflowDefinitionResponse = _reflection.GeneratedProtocolMessageType('WorkflowDefinitionResponse', (_message.Message,), {'DESCRIPTOR': _WORKFLOWDEFINITIONRESPONSE, '__module__': 'common.workflow_pb2'})
_sym_db.RegisterMessage(WorkflowDefinitionResponse)
WorkflowDefinition = _reflection.GeneratedProtocolMessageType('WorkflowDefinition', (_message.Message,), {'DESCRIPTOR': _WORKFLOWDEFINITION, '__module__': 'common.workflow_pb2'})
_sym_db.RegisterMessage(WorkflowDefinition)
ActionDefinition = _reflection.GeneratedProtocolMessageType('ActionDefinition', (_message.Message,), {'DESCRIPTOR': _ACTIONDEFINITION, '__module__': 'common.workflow_pb2'})
_sym_db.RegisterMessage(ActionDefinition)
Argument = _reflection.GeneratedProtocolMessageType('Argument', (_message.Message,), {'DESCRIPTOR': _ARGUMENT, '__module__': 'common.workflow_pb2'})
_sym_db.RegisterMessage(Argument)
GetWorkflowActionResponse = _reflection.GeneratedProtocolMessageType('GetWorkflowActionResponse', (_message.Message,), {'DESCRIPTOR': _GETWORKFLOWACTIONRESPONSE, '__module__': 'common.workflow_pb2'})
_sym_db.RegisterMessage(GetWorkflowActionResponse)
WorkflowList = _reflection.GeneratedProtocolMessageType('WorkflowList', (_message.Message,), {'DESCRIPTOR': _WORKFLOWLIST, '__module__': 'common.workflow_pb2'})
_sym_db.RegisterMessage(WorkflowList)
WorkflowDefinitionList = _reflection.GeneratedProtocolMessageType('WorkflowDefinitionList', (_message.Message,), {'DESCRIPTOR': _WORKFLOWDEFINITIONLIST, '__module__': 'common.workflow_pb2'})
_sym_db.RegisterMessage(WorkflowDefinitionList)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesB\x13WorkflowProtoCommonP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/common'
    _RUNWORKFLOWREQUEST._serialized_start = 149
    _RUNWORKFLOWREQUEST._serialized_end = 237
    _REPROCESSWORKFLOWREQUEST._serialized_start = 239
    _REPROCESSWORKFLOWREQUEST._serialized_end = 302
    _GETACTIONREQUEST._serialized_start = 304
    _GETACTIONREQUEST._serialized_end = 336
    _RUNWORKFLOWRESPONSE._serialized_start = 338
    _RUNWORKFLOWRESPONSE._serialized_end = 394
    _ADDWORKFLOWDEFINITIONREQUEST._serialized_start = 396
    _ADDWORKFLOWDEFINITIONREQUEST._serialized_end = 491
    _WORKFLOWDEFINITIONRESPONSE._serialized_start = 493
    _WORKFLOWDEFINITIONRESPONSE._serialized_end = 589
    _WORKFLOWDEFINITION._serialized_start = 592
    _WORKFLOWDEFINITION._serialized_end = 847
    _ACTIONDEFINITION._serialized_start = 850
    _ACTIONDEFINITION._serialized_end = 1111
    _ARGUMENT._serialized_start = 1113
    _ARGUMENT._serialized_end = 1214
    _GETWORKFLOWACTIONRESPONSE._serialized_start = 1216
    _GETWORKFLOWACTIONRESPONSE._serialized_end = 1314
    _WORKFLOWLIST._serialized_start = 1316
    _WORKFLOWLIST._serialized_end = 1415
    _WORKFLOWDEFINITIONLIST._serialized_start = 1417
    _WORKFLOWDEFINITIONLIST._serialized_end = 1488