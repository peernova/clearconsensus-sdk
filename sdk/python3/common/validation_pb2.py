"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17common/validation.proto\x12\x08titanium\x1a\x19common/gateway_base.proto"\x86\x01\n\x18ValidationRuleDefinition\x12\x0b\n\x03uid\x18\x01 \x01(\t\x12/\n\ndefinition\x18\x03 \x01(\x0b2\x1b.titanium.RulesetDefinition\x12\r\n\x05scope\x18\x04 \x01(\t\x12\x17\n\x0fdescriptor_name\x18\x05 \x01(\tJ\x04\x08\x02\x10\x03"}\n\x19GetValidationRuleResponse\x122\n\x04data\x18\x01 \x01(\x0b2".titanium.ValidationRuleDefinitionH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"b\n"GetGeneratedValidationRuleResponse\x12\x0e\n\x04data\x18\x01 \x01(\tH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"\x1e\n\x0fRdlCheckRequest\x12\x0b\n\x03rdl\x18\x01 \x01(\tBx\n com.peernova.titanium.interfacesB\x1cValidationServiceProtoCommonP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/commonb\x06proto3')
_VALIDATIONRULEDEFINITION = DESCRIPTOR.message_types_by_name['ValidationRuleDefinition']
_GETVALIDATIONRULERESPONSE = DESCRIPTOR.message_types_by_name['GetValidationRuleResponse']
_GETGENERATEDVALIDATIONRULERESPONSE = DESCRIPTOR.message_types_by_name['GetGeneratedValidationRuleResponse']
_RDLCHECKREQUEST = DESCRIPTOR.message_types_by_name['RdlCheckRequest']
ValidationRuleDefinition = _reflection.GeneratedProtocolMessageType('ValidationRuleDefinition', (_message.Message,), {'DESCRIPTOR': _VALIDATIONRULEDEFINITION, '__module__': 'common.validation_pb2'})
_sym_db.RegisterMessage(ValidationRuleDefinition)
GetValidationRuleResponse = _reflection.GeneratedProtocolMessageType('GetValidationRuleResponse', (_message.Message,), {'DESCRIPTOR': _GETVALIDATIONRULERESPONSE, '__module__': 'common.validation_pb2'})
_sym_db.RegisterMessage(GetValidationRuleResponse)
GetGeneratedValidationRuleResponse = _reflection.GeneratedProtocolMessageType('GetGeneratedValidationRuleResponse', (_message.Message,), {'DESCRIPTOR': _GETGENERATEDVALIDATIONRULERESPONSE, '__module__': 'common.validation_pb2'})
_sym_db.RegisterMessage(GetGeneratedValidationRuleResponse)
RdlCheckRequest = _reflection.GeneratedProtocolMessageType('RdlCheckRequest', (_message.Message,), {'DESCRIPTOR': _RDLCHECKREQUEST, '__module__': 'common.validation_pb2'})
_sym_db.RegisterMessage(RdlCheckRequest)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesB\x1cValidationServiceProtoCommonP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/common'
    _VALIDATIONRULEDEFINITION._serialized_start = 65
    _VALIDATIONRULEDEFINITION._serialized_end = 199
    _GETVALIDATIONRULERESPONSE._serialized_start = 201
    _GETVALIDATIONRULERESPONSE._serialized_end = 326
    _GETGENERATEDVALIDATIONRULERESPONSE._serialized_start = 328
    _GETGENERATEDVALIDATIONRULERESPONSE._serialized_end = 426
    _RDLCHECKREQUEST._serialized_start = 428
    _RDLCHECKREQUEST._serialized_end = 458