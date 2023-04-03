"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1acommon/normalization.proto\x12\x08titanium\x1a\x19common/gateway_base.proto"\x85\x01\n\x1bNormalizationRuleDefinition\x12\x0b\n\x03uid\x18\x01 \x01(\t\x12\x17\n\x0fdescriptor_name\x18\x02 \x01(\t\x121\n\x0ftransformations\x18\x04 \x03(\x0b2\x18.titanium.Transformation\x12\r\n\x05scope\x18\x05 \x01(\t"\x80\x01\n\x19NormalizationRuleResponse\x125\n\x04data\x18\x01 \x01(\x0b2%.titanium.NormalizationRuleDefinitionH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08responseB{\n com.peernova.titanium.interfacesB\x1fNormalizationServiceProtoCommonP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/commonb\x06proto3')
_NORMALIZATIONRULEDEFINITION = DESCRIPTOR.message_types_by_name['NormalizationRuleDefinition']
_NORMALIZATIONRULERESPONSE = DESCRIPTOR.message_types_by_name['NormalizationRuleResponse']
NormalizationRuleDefinition = _reflection.GeneratedProtocolMessageType('NormalizationRuleDefinition', (_message.Message,), {'DESCRIPTOR': _NORMALIZATIONRULEDEFINITION, '__module__': 'common.normalization_pb2'})
_sym_db.RegisterMessage(NormalizationRuleDefinition)
NormalizationRuleResponse = _reflection.GeneratedProtocolMessageType('NormalizationRuleResponse', (_message.Message,), {'DESCRIPTOR': _NORMALIZATIONRULERESPONSE, '__module__': 'common.normalization_pb2'})
_sym_db.RegisterMessage(NormalizationRuleResponse)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesB\x1fNormalizationServiceProtoCommonP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/common'
    _NORMALIZATIONRULEDEFINITION._serialized_start = 68
    _NORMALIZATIONRULEDEFINITION._serialized_end = 201
    _NORMALIZATIONRULERESPONSE._serialized_start = 204
    _NORMALIZATIONRULERESPONSE._serialized_end = 332