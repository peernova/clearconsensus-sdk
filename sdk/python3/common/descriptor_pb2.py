"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17common/descriptor.proto\x12\x08titanium\x1a\x19common/gateway_base.proto"\\\n\x1cDescriptorDefinitionResponse\x12\x0e\n\x04data\x18\x01 \x01(\tH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"e\n\x0eDescriptorList\x12%\n\x04data\x18\x01 \x01(\x0b2\x15.titanium.ResultsListH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08responseBq\n com.peernova.titanium.interfacesB\x15DescriptorProtoCommonP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/commonb\x06proto3')
_DESCRIPTORDEFINITIONRESPONSE = DESCRIPTOR.message_types_by_name['DescriptorDefinitionResponse']
_DESCRIPTORLIST = DESCRIPTOR.message_types_by_name['DescriptorList']
DescriptorDefinitionResponse = _reflection.GeneratedProtocolMessageType('DescriptorDefinitionResponse', (_message.Message,), {'DESCRIPTOR': _DESCRIPTORDEFINITIONRESPONSE, '__module__': 'common.descriptor_pb2'})
_sym_db.RegisterMessage(DescriptorDefinitionResponse)
DescriptorList = _reflection.GeneratedProtocolMessageType('DescriptorList', (_message.Message,), {'DESCRIPTOR': _DESCRIPTORLIST, '__module__': 'common.descriptor_pb2'})
_sym_db.RegisterMessage(DescriptorList)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesB\x15DescriptorProtoCommonP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/common'
    _DESCRIPTORDEFINITIONRESPONSE._serialized_start = 64
    _DESCRIPTORDEFINITIONRESPONSE._serialized_end = 156
    _DESCRIPTORLIST._serialized_start = 158
    _DESCRIPTORLIST._serialized_end = 259