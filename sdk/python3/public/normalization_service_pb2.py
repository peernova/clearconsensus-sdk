"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ..google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2
from ..common import normalization_pb2 as common_dot_normalization__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"public/normalization_service.proto\x12\x08titanium\x1a\x1cgoogle/api/annotations.proto\x1a\x19common/gateway_base.proto\x1a\x1acommon/normalization.proto2\xd3\x07\n\x14NormalizationService\x12\x87\x01\n\x14AddNormalizationRule\x12%.titanium.NormalizationRuleDefinition\x1a\x1d.titanium.AcknowledgeResponse")\x82\xd3\xe4\x93\x02#"\x1e/api/v1/normalization/rule/add:\x01*\x12\x7f\n\x14GetNormalizationRule\x12\x17.titanium.GetDefinition\x1a#.titanium.NormalizationRuleResponse")\x82\xd3\xe4\x93\x02#"\x1e/api/v1/normalization/rule/get:\x01*\x12\x7f\n\x17EnableNormalizationRule\x12\x17.titanium.GetDefinition\x1a\x1d.titanium.AcknowledgeResponse",\x82\xd3\xe4\x93\x02&"!/api/v1/normalization/rule/enable:\x01*\x12\x81\x01\n\x18DisableNormalizationRule\x12\x17.titanium.GetDefinition\x1a\x1d.titanium.AcknowledgeResponse"-\x82\xd3\xe4\x93\x02\'""/api/v1/normalization/rule/disable:\x01*\x12w\n\x16ListNormalizationRules\x12\x15.titanium.ListRequest\x1a\x1a.titanium.ListRuleResponse"*\x82\xd3\xe4\x93\x02$"\x1f/api/v1/normalization/rule/list:\x01*\x12\x87\x01\n\x1dListNormalizationRuleVersions\x12\x17.titanium.GetDefinition\x1a\x1d.titanium.ListVersionResponse".\x82\xd3\xe4\x93\x02("#/api/v1/normalization/rule/versions:\x01*\x12\xa7\x01\n\x1bGetNormalizationRuleVersion\x12\x18.titanium.VersionRequest\x1a#.titanium.NormalizationRuleResponse"I\x82\xd3\xe4\x93\x02C\x12A/api/v1/normalization/rule/version/{descriptor_name}/{version_id}B{\n com.peernova.titanium.interfacesB\x1fNormalizationServiceProtoPublicP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/publicb\x06proto3')
_NORMALIZATIONSERVICE = DESCRIPTOR.services_by_name['NormalizationService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesB\x1fNormalizationServiceProtoPublicP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/public'
    _NORMALIZATIONSERVICE.methods_by_name['AddNormalizationRule']._options = None
    _NORMALIZATIONSERVICE.methods_by_name['AddNormalizationRule']._serialized_options = b'\x82\xd3\xe4\x93\x02#"\x1e/api/v1/normalization/rule/add:\x01*'
    _NORMALIZATIONSERVICE.methods_by_name['GetNormalizationRule']._options = None
    _NORMALIZATIONSERVICE.methods_by_name['GetNormalizationRule']._serialized_options = b'\x82\xd3\xe4\x93\x02#"\x1e/api/v1/normalization/rule/get:\x01*'
    _NORMALIZATIONSERVICE.methods_by_name['EnableNormalizationRule']._options = None
    _NORMALIZATIONSERVICE.methods_by_name['EnableNormalizationRule']._serialized_options = b'\x82\xd3\xe4\x93\x02&"!/api/v1/normalization/rule/enable:\x01*'
    _NORMALIZATIONSERVICE.methods_by_name['DisableNormalizationRule']._options = None
    _NORMALIZATIONSERVICE.methods_by_name['DisableNormalizationRule']._serialized_options = b'\x82\xd3\xe4\x93\x02\'""/api/v1/normalization/rule/disable:\x01*'
    _NORMALIZATIONSERVICE.methods_by_name['ListNormalizationRules']._options = None
    _NORMALIZATIONSERVICE.methods_by_name['ListNormalizationRules']._serialized_options = b'\x82\xd3\xe4\x93\x02$"\x1f/api/v1/normalization/rule/list:\x01*'
    _NORMALIZATIONSERVICE.methods_by_name['ListNormalizationRuleVersions']._options = None
    _NORMALIZATIONSERVICE.methods_by_name['ListNormalizationRuleVersions']._serialized_options = b'\x82\xd3\xe4\x93\x02("#/api/v1/normalization/rule/versions:\x01*'
    _NORMALIZATIONSERVICE.methods_by_name['GetNormalizationRuleVersion']._options = None
    _NORMALIZATIONSERVICE.methods_by_name['GetNormalizationRuleVersion']._serialized_options = b'\x82\xd3\xe4\x93\x02C\x12A/api/v1/normalization/rule/version/{descriptor_name}/{version_id}'
    _NORMALIZATIONSERVICE._serialized_start = 134
    _NORMALIZATIONSERVICE._serialized_end = 1113