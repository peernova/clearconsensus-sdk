"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13common/mapper.proto\x12\x08titanium\x1a\x19common/gateway_base.proto"\x8c\x01\n DescriptorPairBasedGetDefinition\x12(\n\nidentifier\x18\x01 \x01(\x0b2\x14.titanium.Identifier\x12\r\n\x05scope\x18\x02 \x01(\t\x12\x16\n\x0esrc_descriptor\x18\x03 \x01(\t\x12\x17\n\x0fdest_descriptor\x18\x04 \x01(\t"\x8f\x01\n&DescriptorPairBasedAcknowledgeResponse\x127\n\x04data\x18\x01 \x01(\x0b2\'.titanium.DescriptorPairBasedIdentifierH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"\x97\x01\n\x15MappingRuleDefinition\x12\x0b\n\x03uid\x18\x01 \x01(\t\x12\x16\n\x0esrc_descriptor\x18\x02 \x01(\t\x12\x17\n\x0fdest_descriptor\x18\x03 \x01(\t\x121\n\x0ftransformations\x18\x04 \x03(\x0b2\x18.titanium.Transformation\x12\r\n\x05scope\x18\x05 \x01(\t"t\n\x13MappingRuleResponse\x12/\n\x04data\x18\x01 \x01(\x0b2\x1f.titanium.MappingRuleDefinitionH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"]\n\x1dDescriptorPairBasedIdentifier\x12\x0b\n\x03uid\x18\x01 \x01(\t\x12\x16\n\x0esrc_descriptor\x18\x02 \x01(\t\x12\x17\n\x0fdest_descriptor\x18\x03 \x01(\t"Z\n\x1eDescriptorPairBasedResultsList\x128\n\x07results\x18\x01 \x03(\x0b2\'.titanium.DescriptorPairBasedIdentifier"y\n\x0fMappingRuleList\x128\n\x04data\x18\x01 \x01(\x0b2(.titanium.DescriptorPairBasedResultsListH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"w\n!DescriptorPairBasedVersionRequest\x12\x16\n\x0esrc_descriptor\x18\x01 \x01(\t\x12\x17\n\x0fdest_descriptor\x18\x02 \x01(\t\x12\x12\n\nversion_id\x18\x03 \x01(\t\x12\r\n\x05scope\x18\x04 \x01(\tBu\n com.peernova.titanium.interfacesB\x19MappingServiceProtoCommonP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/commonb\x06proto3')
_DESCRIPTORPAIRBASEDGETDEFINITION = DESCRIPTOR.message_types_by_name['DescriptorPairBasedGetDefinition']
_DESCRIPTORPAIRBASEDACKNOWLEDGERESPONSE = DESCRIPTOR.message_types_by_name['DescriptorPairBasedAcknowledgeResponse']
_MAPPINGRULEDEFINITION = DESCRIPTOR.message_types_by_name['MappingRuleDefinition']
_MAPPINGRULERESPONSE = DESCRIPTOR.message_types_by_name['MappingRuleResponse']
_DESCRIPTORPAIRBASEDIDENTIFIER = DESCRIPTOR.message_types_by_name['DescriptorPairBasedIdentifier']
_DESCRIPTORPAIRBASEDRESULTSLIST = DESCRIPTOR.message_types_by_name['DescriptorPairBasedResultsList']
_MAPPINGRULELIST = DESCRIPTOR.message_types_by_name['MappingRuleList']
_DESCRIPTORPAIRBASEDVERSIONREQUEST = DESCRIPTOR.message_types_by_name['DescriptorPairBasedVersionRequest']
DescriptorPairBasedGetDefinition = _reflection.GeneratedProtocolMessageType('DescriptorPairBasedGetDefinition', (_message.Message,), {'DESCRIPTOR': _DESCRIPTORPAIRBASEDGETDEFINITION, '__module__': 'common.mapper_pb2'})
_sym_db.RegisterMessage(DescriptorPairBasedGetDefinition)
DescriptorPairBasedAcknowledgeResponse = _reflection.GeneratedProtocolMessageType('DescriptorPairBasedAcknowledgeResponse', (_message.Message,), {'DESCRIPTOR': _DESCRIPTORPAIRBASEDACKNOWLEDGERESPONSE, '__module__': 'common.mapper_pb2'})
_sym_db.RegisterMessage(DescriptorPairBasedAcknowledgeResponse)
MappingRuleDefinition = _reflection.GeneratedProtocolMessageType('MappingRuleDefinition', (_message.Message,), {'DESCRIPTOR': _MAPPINGRULEDEFINITION, '__module__': 'common.mapper_pb2'})
_sym_db.RegisterMessage(MappingRuleDefinition)
MappingRuleResponse = _reflection.GeneratedProtocolMessageType('MappingRuleResponse', (_message.Message,), {'DESCRIPTOR': _MAPPINGRULERESPONSE, '__module__': 'common.mapper_pb2'})
_sym_db.RegisterMessage(MappingRuleResponse)
DescriptorPairBasedIdentifier = _reflection.GeneratedProtocolMessageType('DescriptorPairBasedIdentifier', (_message.Message,), {'DESCRIPTOR': _DESCRIPTORPAIRBASEDIDENTIFIER, '__module__': 'common.mapper_pb2'})
_sym_db.RegisterMessage(DescriptorPairBasedIdentifier)
DescriptorPairBasedResultsList = _reflection.GeneratedProtocolMessageType('DescriptorPairBasedResultsList', (_message.Message,), {'DESCRIPTOR': _DESCRIPTORPAIRBASEDRESULTSLIST, '__module__': 'common.mapper_pb2'})
_sym_db.RegisterMessage(DescriptorPairBasedResultsList)
MappingRuleList = _reflection.GeneratedProtocolMessageType('MappingRuleList', (_message.Message,), {'DESCRIPTOR': _MAPPINGRULELIST, '__module__': 'common.mapper_pb2'})
_sym_db.RegisterMessage(MappingRuleList)
DescriptorPairBasedVersionRequest = _reflection.GeneratedProtocolMessageType('DescriptorPairBasedVersionRequest', (_message.Message,), {'DESCRIPTOR': _DESCRIPTORPAIRBASEDVERSIONREQUEST, '__module__': 'common.mapper_pb2'})
_sym_db.RegisterMessage(DescriptorPairBasedVersionRequest)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesB\x19MappingServiceProtoCommonP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/common'
    _DESCRIPTORPAIRBASEDGETDEFINITION._serialized_start = 61
    _DESCRIPTORPAIRBASEDGETDEFINITION._serialized_end = 201
    _DESCRIPTORPAIRBASEDACKNOWLEDGERESPONSE._serialized_start = 204
    _DESCRIPTORPAIRBASEDACKNOWLEDGERESPONSE._serialized_end = 347
    _MAPPINGRULEDEFINITION._serialized_start = 350
    _MAPPINGRULEDEFINITION._serialized_end = 501
    _MAPPINGRULERESPONSE._serialized_start = 503
    _MAPPINGRULERESPONSE._serialized_end = 619
    _DESCRIPTORPAIRBASEDIDENTIFIER._serialized_start = 621
    _DESCRIPTORPAIRBASEDIDENTIFIER._serialized_end = 714
    _DESCRIPTORPAIRBASEDRESULTSLIST._serialized_start = 716
    _DESCRIPTORPAIRBASEDRESULTSLIST._serialized_end = 806
    _MAPPINGRULELIST._serialized_start = 808
    _MAPPINGRULELIST._serialized_end = 929
    _DESCRIPTORPAIRBASEDVERSIONREQUEST._serialized_start = 931
    _DESCRIPTORPAIRBASEDVERSIONREQUEST._serialized_end = 1050