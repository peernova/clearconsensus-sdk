"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ..google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$public/metadata_entity_service.proto\x12\x08titanium\x1a\x1cgoogle/api/annotations.proto\x1a\x19common/gateway_base.proto2\xbe\x03\n\x15MetadataEntityService\x12e\n\tAddEntity\x12\x1a.titanium.EntityDefinition\x1a\x1d.titanium.AcknowledgeResponse"\x1d\x82\xd3\xe4\x93\x02\x17"\x12/api/v1/entity/add:\x01*\x12b\n\tGetEntity\x12\x1a.titanium.EntityIdentifier\x1a\x1a.titanium.EntityDefinition"\x1d\x82\xd3\xe4\x93\x02\x17"\x12/api/v1/entity/get:\x01*\x12k\n\x0cEnableEntity\x12\x1a.titanium.EntityIdentifier\x1a\x1d.titanium.AcknowledgeResponse" \x82\xd3\xe4\x93\x02\x1a"\x15/api/v1/entity/enable:\x01*\x12m\n\rDisableEntity\x12\x1a.titanium.EntityIdentifier\x1a\x1d.titanium.AcknowledgeResponse"!\x82\xd3\xe4\x93\x02\x1b"\x16/api/v1/entity/disable:\x01*B|\n com.peernova.titanium.interfacesB MetadataEntityServiceProtoPublicP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/publicb\x06proto3')
_METADATAENTITYSERVICE = DESCRIPTOR.services_by_name['MetadataEntityService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesB MetadataEntityServiceProtoPublicP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/public'
    _METADATAENTITYSERVICE.methods_by_name['AddEntity']._options = None
    _METADATAENTITYSERVICE.methods_by_name['AddEntity']._serialized_options = b'\x82\xd3\xe4\x93\x02\x17"\x12/api/v1/entity/add:\x01*'
    _METADATAENTITYSERVICE.methods_by_name['GetEntity']._options = None
    _METADATAENTITYSERVICE.methods_by_name['GetEntity']._serialized_options = b'\x82\xd3\xe4\x93\x02\x17"\x12/api/v1/entity/get:\x01*'
    _METADATAENTITYSERVICE.methods_by_name['EnableEntity']._options = None
    _METADATAENTITYSERVICE.methods_by_name['EnableEntity']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1a"\x15/api/v1/entity/enable:\x01*'
    _METADATAENTITYSERVICE.methods_by_name['DisableEntity']._options = None
    _METADATAENTITYSERVICE.methods_by_name['DisableEntity']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1b"\x16/api/v1/entity/disable:\x01*'
    _METADATAENTITYSERVICE._serialized_start = 108
    _METADATAENTITYSERVICE._serialized_end = 554