"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17common/descriptor.proto\x12\x08titanium\x1a\x19common/gateway_base.proto"\\\n\x1cDescriptorDefinitionResponse\x12\x0e\n\x04data\x18\x01 \x01(\tH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"e\n\x0eDescriptorList\x12%\n\x04data\x18\x01 \x01(\x0b2\x15.titanium.ResultsListH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"\xdf\x01\n\x05Usage\x12\x12\n\nusage_name\x18\x01 \x01(\t\x12-\n\nusage_type\x18\x02 \x01(\x0e2\x19.titanium.Usage.UsageType"\x92\x01\n\tUsageType\x12\x13\n\x0fCRITERIA_FILTER\x10\x00\x12\x08\n\x04RULE\x10\x01\x12\x0f\n\x0bRULE_FILTER\x10\x02\x12\x11\n\rERROR_MESSAGE\x10\x03\x12\x13\n\x0fLOOKUPTABLE_KEY\x10\x04\x12\x15\n\x11LOOKUPTABLE_VALUE\x10\x05\x12\x16\n\x12LOOKUPTABLE_FILTER\x10\x06"\x9d\x01\n\nDependency\x12\r\n\x05scope\x18\x01 \x01(\t\x12)\n\x0bentity_type\x18\x02 \x01(\x0e2\x14.titanium.EntityType\x12\x13\n\x0bentity_name\x18\x03 \x01(\t\x12\x0e\n\x06entity\x18\x04 \x01(\t\x12\x0f\n\x07version\x18\x05 \x01(\t\x12\x1f\n\x06usages\x18\x06 \x03(\x0b2\x0f.titanium.Usage"F\n\rColDependency\x12\x0b\n\x03col\x18\x01 \x01(\t\x12(\n\ndependency\x18\x02 \x03(\x0b2\x14.titanium.Dependency"F\n\x15ColDependencyResponse\x12-\n\x0cdependencies\x18\x01 \x03(\x0b2\x17.titanium.ColDependency"\x87\x01\n\x1eDescriptorDependenciesResponse\x127\n\x0cdependencies\x18\x01 \x01(\x0b2\x1f.titanium.ColDependencyResponseH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08responseBq\n com.peernova.titanium.interfacesB\x15DescriptorProtoCommonP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/commonb\x06proto3')
_DESCRIPTORDEFINITIONRESPONSE = DESCRIPTOR.message_types_by_name['DescriptorDefinitionResponse']
_DESCRIPTORLIST = DESCRIPTOR.message_types_by_name['DescriptorList']
_USAGE = DESCRIPTOR.message_types_by_name['Usage']
_DEPENDENCY = DESCRIPTOR.message_types_by_name['Dependency']
_COLDEPENDENCY = DESCRIPTOR.message_types_by_name['ColDependency']
_COLDEPENDENCYRESPONSE = DESCRIPTOR.message_types_by_name['ColDependencyResponse']
_DESCRIPTORDEPENDENCIESRESPONSE = DESCRIPTOR.message_types_by_name['DescriptorDependenciesResponse']
_USAGE_USAGETYPE = _USAGE.enum_types_by_name['UsageType']
DescriptorDefinitionResponse = _reflection.GeneratedProtocolMessageType('DescriptorDefinitionResponse', (_message.Message,), {'DESCRIPTOR': _DESCRIPTORDEFINITIONRESPONSE, '__module__': 'common.descriptor_pb2'})
_sym_db.RegisterMessage(DescriptorDefinitionResponse)
DescriptorList = _reflection.GeneratedProtocolMessageType('DescriptorList', (_message.Message,), {'DESCRIPTOR': _DESCRIPTORLIST, '__module__': 'common.descriptor_pb2'})
_sym_db.RegisterMessage(DescriptorList)
Usage = _reflection.GeneratedProtocolMessageType('Usage', (_message.Message,), {'DESCRIPTOR': _USAGE, '__module__': 'common.descriptor_pb2'})
_sym_db.RegisterMessage(Usage)
Dependency = _reflection.GeneratedProtocolMessageType('Dependency', (_message.Message,), {'DESCRIPTOR': _DEPENDENCY, '__module__': 'common.descriptor_pb2'})
_sym_db.RegisterMessage(Dependency)
ColDependency = _reflection.GeneratedProtocolMessageType('ColDependency', (_message.Message,), {'DESCRIPTOR': _COLDEPENDENCY, '__module__': 'common.descriptor_pb2'})
_sym_db.RegisterMessage(ColDependency)
ColDependencyResponse = _reflection.GeneratedProtocolMessageType('ColDependencyResponse', (_message.Message,), {'DESCRIPTOR': _COLDEPENDENCYRESPONSE, '__module__': 'common.descriptor_pb2'})
_sym_db.RegisterMessage(ColDependencyResponse)
DescriptorDependenciesResponse = _reflection.GeneratedProtocolMessageType('DescriptorDependenciesResponse', (_message.Message,), {'DESCRIPTOR': _DESCRIPTORDEPENDENCIESRESPONSE, '__module__': 'common.descriptor_pb2'})
_sym_db.RegisterMessage(DescriptorDependenciesResponse)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesB\x15DescriptorProtoCommonP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/common'
    _DESCRIPTORDEFINITIONRESPONSE._serialized_start = 64
    _DESCRIPTORDEFINITIONRESPONSE._serialized_end = 156
    _DESCRIPTORLIST._serialized_start = 158
    _DESCRIPTORLIST._serialized_end = 259
    _USAGE._serialized_start = 262
    _USAGE._serialized_end = 485
    _USAGE_USAGETYPE._serialized_start = 339
    _USAGE_USAGETYPE._serialized_end = 485
    _DEPENDENCY._serialized_start = 488
    _DEPENDENCY._serialized_end = 645
    _COLDEPENDENCY._serialized_start = 647
    _COLDEPENDENCY._serialized_end = 717
    _COLDEPENDENCYRESPONSE._serialized_start = 719
    _COLDEPENDENCYRESPONSE._serialized_end = 789
    _DESCRIPTORDEPENDENCIESRESPONSE._serialized_start = 792
    _DESCRIPTORDEPENDENCIESRESPONSE._serialized_end = 927