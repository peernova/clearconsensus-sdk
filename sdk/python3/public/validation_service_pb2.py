"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ..google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2
from ..common import validation_pb2 as common_dot_validation__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fpublic/validation_service.proto\x12\x08titanium\x1a\x1cgoogle/api/annotations.proto\x1a\x19common/gateway_base.proto\x1a\x17common/validation.proto2\xf7\x0b\n\x10ValidatorService\x12~\n\x11AddValidationRule\x12".titanium.ValidationRuleDefinition\x1a\x1d.titanium.AcknowledgeResponse"&\x82\xd3\xe4\x93\x02 "\x1b/api/v1/validation/rule/add:\x01*\x12y\n\x11GetValidationRule\x12\x17.titanium.GetDefinition\x1a#.titanium.GetValidationRuleResponse"&\x82\xd3\xe4\x93\x02 "\x1b/api/v1/validation/rule/get:\x01*\x12{\n\x15DisableValidationRule\x12\x17.titanium.GetDefinition\x1a\x1d.titanium.AcknowledgeResponse"*\x82\xd3\xe4\x93\x02$"\x1f/api/v1/validation/rule/disable:\x01*\x12y\n\x14EnableValidationRule\x12\x17.titanium.GetDefinition\x1a\x1d.titanium.AcknowledgeResponse")\x82\xd3\xe4\x93\x02#"\x1e/api/v1/validation/rule/enable:\x01*\x12q\n\x13ListValidationRules\x12\x15.titanium.ListRequest\x1a\x1a.titanium.ListRuleResponse"\'\x82\xd3\xe4\x93\x02!"\x1c/api/v1/validation/rule/list:\x01*\x12\x81\x01\n\x1aListValidationRuleVersions\x12\x17.titanium.GetDefinition\x1a\x1d.titanium.ListVersionResponse"+\x82\xd3\xe4\x93\x02%" /api/v1/validation/rule/versions:\x01*\x12\xa1\x01\n\x18GetValidationRuleVersion\x12\x18.titanium.VersionRequest\x1a#.titanium.GetValidationRuleResponse"F\x82\xd3\xe4\x93\x02@\x12>/api/v1/validation/rule/version/{descriptor_name}/{version_id}\x12\x91\x01\n\x1aGetGeneratedValidationRule\x12\x17.titanium.GetDefinition\x1a,.titanium.GetGeneratedValidationRuleResponse",\x82\xd3\xe4\x93\x02&"!/api/v1/validation/rule/generated:\x01*\x12\x94\x01\n#ListGeneratedValidationRuleVersions\x12\x17.titanium.GetDefinition\x1a\x1d.titanium.ListVersionResponse"5\x82\xd3\xe4\x93\x02/"*/api/v1/validation/rule/generated/versions:\x01*\x12\xbd\x01\n!GetGeneratedValidationRuleVersion\x12\x18.titanium.VersionRequest\x1a,.titanium.GetGeneratedValidationRuleResponse"P\x82\xd3\xe4\x93\x02J\x12H/api/v1/validation/rule/generated/version/{descriptor_name}/{version_id}\x12j\n\x08RdlCheck\x12\x19.titanium.RdlCheckRequest\x1a\x19.titanium.MessageResponse"(\x82\xd3\xe4\x93\x02""\x1d/api/v1/validation/rule/check:\x01*Bx\n com.peernova.titanium.interfacesB\x1cValidationServiceProtoPublicP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/publicb\x06proto3')
_VALIDATORSERVICE = DESCRIPTOR.services_by_name['ValidatorService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesB\x1cValidationServiceProtoPublicP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/public'
    _VALIDATORSERVICE.methods_by_name['AddValidationRule']._options = None
    _VALIDATORSERVICE.methods_by_name['AddValidationRule']._serialized_options = b'\x82\xd3\xe4\x93\x02 "\x1b/api/v1/validation/rule/add:\x01*'
    _VALIDATORSERVICE.methods_by_name['GetValidationRule']._options = None
    _VALIDATORSERVICE.methods_by_name['GetValidationRule']._serialized_options = b'\x82\xd3\xe4\x93\x02 "\x1b/api/v1/validation/rule/get:\x01*'
    _VALIDATORSERVICE.methods_by_name['DisableValidationRule']._options = None
    _VALIDATORSERVICE.methods_by_name['DisableValidationRule']._serialized_options = b'\x82\xd3\xe4\x93\x02$"\x1f/api/v1/validation/rule/disable:\x01*'
    _VALIDATORSERVICE.methods_by_name['EnableValidationRule']._options = None
    _VALIDATORSERVICE.methods_by_name['EnableValidationRule']._serialized_options = b'\x82\xd3\xe4\x93\x02#"\x1e/api/v1/validation/rule/enable:\x01*'
    _VALIDATORSERVICE.methods_by_name['ListValidationRules']._options = None
    _VALIDATORSERVICE.methods_by_name['ListValidationRules']._serialized_options = b'\x82\xd3\xe4\x93\x02!"\x1c/api/v1/validation/rule/list:\x01*'
    _VALIDATORSERVICE.methods_by_name['ListValidationRuleVersions']._options = None
    _VALIDATORSERVICE.methods_by_name['ListValidationRuleVersions']._serialized_options = b'\x82\xd3\xe4\x93\x02%" /api/v1/validation/rule/versions:\x01*'
    _VALIDATORSERVICE.methods_by_name['GetValidationRuleVersion']._options = None
    _VALIDATORSERVICE.methods_by_name['GetValidationRuleVersion']._serialized_options = b'\x82\xd3\xe4\x93\x02@\x12>/api/v1/validation/rule/version/{descriptor_name}/{version_id}'
    _VALIDATORSERVICE.methods_by_name['GetGeneratedValidationRule']._options = None
    _VALIDATORSERVICE.methods_by_name['GetGeneratedValidationRule']._serialized_options = b'\x82\xd3\xe4\x93\x02&"!/api/v1/validation/rule/generated:\x01*'
    _VALIDATORSERVICE.methods_by_name['ListGeneratedValidationRuleVersions']._options = None
    _VALIDATORSERVICE.methods_by_name['ListGeneratedValidationRuleVersions']._serialized_options = b'\x82\xd3\xe4\x93\x02/"*/api/v1/validation/rule/generated/versions:\x01*'
    _VALIDATORSERVICE.methods_by_name['GetGeneratedValidationRuleVersion']._options = None
    _VALIDATORSERVICE.methods_by_name['GetGeneratedValidationRuleVersion']._serialized_options = b'\x82\xd3\xe4\x93\x02J\x12H/api/v1/validation/rule/generated/version/{descriptor_name}/{version_id}'
    _VALIDATORSERVICE.methods_by_name['RdlCheck']._options = None
    _VALIDATORSERVICE.methods_by_name['RdlCheck']._serialized_options = b'\x82\xd3\xe4\x93\x02""\x1d/api/v1/validation/rule/check:\x01*'
    _VALIDATORSERVICE._serialized_start = 128
    _VALIDATORSERVICE._serialized_end = 1655