"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ..google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2
from ..common import mapper_pb2 as common_dot_mapper__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cpublic/mapping_service.proto\x12\x08titanium\x1a\x1cgoogle/api/annotations.proto\x1a\x19common/gateway_base.proto\x1a\x13common/mapper.proto2\x99\x08\n\x0eMappingService\x12\x88\x01\n\x0eAddMappingRule\x12\x1f.titanium.MappingRuleDefinition\x1a0.titanium.DescriptorPairBasedAcknowledgeResponse"#\x82\xd3\xe4\x93\x02\x1d"\x18/api/v1/mapping/rule/add:\x01*\x12\x80\x01\n\x0eGetMappingRule\x12*.titanium.DescriptorPairBasedGetDefinition\x1a\x1d.titanium.MappingRuleResponse"#\x82\xd3\xe4\x93\x02\x1d"\x18/api/v1/mapping/rule/get:\x01*\x12\x99\x01\n\x11EnableMappingRule\x12*.titanium.DescriptorPairBasedGetDefinition\x1a0.titanium.DescriptorPairBasedAcknowledgeResponse"&\x82\xd3\xe4\x93\x02 "\x1b/api/v1/mapping/rule/enable:\x01*\x12\x9b\x01\n\x12DisableMappingRule\x12*.titanium.DescriptorPairBasedGetDefinition\x1a0.titanium.DescriptorPairBasedAcknowledgeResponse"\'\x82\xd3\xe4\x93\x02!"\x1c/api/v1/mapping/rule/disable:\x01*\x12j\n\x10ListMappingRules\x12\x15.titanium.ListRequest\x1a\x19.titanium.MappingRuleList"$\x82\xd3\xe4\x93\x02\x1e"\x19/api/v1/mapping/rule/list:\x01*\x12\x8e\x01\n\x17ListMappingRuleVersions\x12*.titanium.DescriptorPairBasedGetDefinition\x1a\x1d.titanium.ListVersionResponse"(\x82\xd3\xe4\x93\x02""\x1d/api/v1/mapping/rule/versions:\x01*\x12\xc1\x01\n\x15GetMappingRuleVersion\x12+.titanium.DescriptorPairBasedVersionRequest\x1a\x1d.titanium.MappingRuleResponse"\\\x82\xd3\xe4\x93\x02V\x12T/api/v1/mapping/rule/version/{scope}/{src_descriptor}/{dest_descriptor}/{version_id}Bu\n com.peernova.titanium.interfacesB\x19MappingServiceProtoPublicP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/publicb\x06proto3')
_MAPPINGSERVICE = DESCRIPTOR.services_by_name['MappingService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesB\x19MappingServiceProtoPublicP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/public'
    _MAPPINGSERVICE.methods_by_name['AddMappingRule']._options = None
    _MAPPINGSERVICE.methods_by_name['AddMappingRule']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1d"\x18/api/v1/mapping/rule/add:\x01*'
    _MAPPINGSERVICE.methods_by_name['GetMappingRule']._options = None
    _MAPPINGSERVICE.methods_by_name['GetMappingRule']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1d"\x18/api/v1/mapping/rule/get:\x01*'
    _MAPPINGSERVICE.methods_by_name['EnableMappingRule']._options = None
    _MAPPINGSERVICE.methods_by_name['EnableMappingRule']._serialized_options = b'\x82\xd3\xe4\x93\x02 "\x1b/api/v1/mapping/rule/enable:\x01*'
    _MAPPINGSERVICE.methods_by_name['DisableMappingRule']._options = None
    _MAPPINGSERVICE.methods_by_name['DisableMappingRule']._serialized_options = b'\x82\xd3\xe4\x93\x02!"\x1c/api/v1/mapping/rule/disable:\x01*'
    _MAPPINGSERVICE.methods_by_name['ListMappingRules']._options = None
    _MAPPINGSERVICE.methods_by_name['ListMappingRules']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1e"\x19/api/v1/mapping/rule/list:\x01*'
    _MAPPINGSERVICE.methods_by_name['ListMappingRuleVersions']._options = None
    _MAPPINGSERVICE.methods_by_name['ListMappingRuleVersions']._serialized_options = b'\x82\xd3\xe4\x93\x02""\x1d/api/v1/mapping/rule/versions:\x01*'
    _MAPPINGSERVICE.methods_by_name['GetMappingRuleVersion']._options = None
    _MAPPINGSERVICE.methods_by_name['GetMappingRuleVersion']._serialized_options = b'\x82\xd3\xe4\x93\x02V\x12T/api/v1/mapping/rule/version/{scope}/{src_descriptor}/{dest_descriptor}/{version_id}'
    _MAPPINGSERVICE._serialized_start = 121
    _MAPPINGSERVICE._serialized_end = 1170