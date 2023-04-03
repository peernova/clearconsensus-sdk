"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ..google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2
from ..common import unique_key_pb2 as common_dot_unique__key__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fpublic/unique_key_service.proto\x12\x08titanium\x1a\x1cgoogle/api/annotations.proto\x1a\x19common/gateway_base.proto\x1a\x17common/unique_key.proto2\xf2\x04\n\x10UniqueKeyService\x12n\n\x0cAddUniqueKey\x12\x1d.titanium.UniqueKeyDefinition\x1a\x1d.titanium.AcknowledgeResponse" \x82\xd3\xe4\x93\x02\x1a"\x15/api/v1/uniquekey/add:\x01*\x12p\n\x0cGetUniqueKey\x12\x17.titanium.GetDefinition\x1a%.titanium.UniqueKeyDefinitionResponse" \x82\xd3\xe4\x93\x02\x1a"\x15/api/v1/uniquekey/get:\x01*\x12l\n\x0eListUniqueKeys\x12\x15.titanium.ListRequest\x1a .titanium.ListUniqueKeysResponse"!\x82\xd3\xe4\x93\x02\x1b"\x16/api/v1/uniquekey/list:\x01*\x12v\n\x15ListUniqueKeyVersions\x12\x17.titanium.GetDefinition\x1a\x1d.titanium.ListVersionResponse"%\x82\xd3\xe4\x93\x02\x1f"\x1a/api/v1/uniquekey/versions:\x01*\x12\x95\x01\n\x13GetUniqueKeyVersion\x12\x18.titanium.VersionRequest\x1a%.titanium.UniqueKeyDefinitionResponse"=\x82\xd3\xe4\x93\x027\x125/api/v1/uniquekey/version/{scope}/{name}/{version_id}Bw\n com.peernova.titanium.interfacesB\x1bUniqueKeyServiceProtoPublicP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/publicb\x06proto3')
_UNIQUEKEYSERVICE = DESCRIPTOR.services_by_name['UniqueKeyService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesB\x1bUniqueKeyServiceProtoPublicP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/public'
    _UNIQUEKEYSERVICE.methods_by_name['AddUniqueKey']._options = None
    _UNIQUEKEYSERVICE.methods_by_name['AddUniqueKey']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1a"\x15/api/v1/uniquekey/add:\x01*'
    _UNIQUEKEYSERVICE.methods_by_name['GetUniqueKey']._options = None
    _UNIQUEKEYSERVICE.methods_by_name['GetUniqueKey']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1a"\x15/api/v1/uniquekey/get:\x01*'
    _UNIQUEKEYSERVICE.methods_by_name['ListUniqueKeys']._options = None
    _UNIQUEKEYSERVICE.methods_by_name['ListUniqueKeys']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1b"\x16/api/v1/uniquekey/list:\x01*'
    _UNIQUEKEYSERVICE.methods_by_name['ListUniqueKeyVersions']._options = None
    _UNIQUEKEYSERVICE.methods_by_name['ListUniqueKeyVersions']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1f"\x1a/api/v1/uniquekey/versions:\x01*'
    _UNIQUEKEYSERVICE.methods_by_name['GetUniqueKeyVersion']._options = None
    _UNIQUEKEYSERVICE.methods_by_name['GetUniqueKeyVersion']._serialized_options = b'\x82\xd3\xe4\x93\x027\x125/api/v1/uniquekey/version/{scope}/{name}/{version_id}'
    _UNIQUEKEYSERVICE._serialized_start = 128
    _UNIQUEKEYSERVICE._serialized_end = 754