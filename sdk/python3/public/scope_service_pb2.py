"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ..google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2
from ..common import scope_pb2 as common_dot_scope__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1apublic/scope_service.proto\x12\x08titanium\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x19common/gateway_base.proto\x1a\x12common/scope.proto2\xba\x02\n\x0cScopeService\x12b\n\x08AddScope\x12\x19.titanium.ScopeIdentifier\x1a\x1d.titanium.AcknowledgeResponse"\x1c\x82\xd3\xe4\x93\x02\x16"\x11/api/v1/scope/add:\x01*\x12e\n\nExistScope\x12\x19.titanium.ScopeIdentifier\x1a\x1c.titanium.ScopeExistResponse"\x1e\x82\xd3\xe4\x93\x02\x18"\x13/api/v1/scope/exist:\x01*\x12_\n\tListScope\x12\x16.google.protobuf.Empty\x1a\x1b.titanium.ScopeListResponse"\x1d\x82\xd3\xe4\x93\x02\x17"\x12/api/v1/scope/list:\x01*Bs\n com.peernova.titanium.interfacesB\x17ScopeServiceProtoPublicP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/publicb\x06proto3')
_SCOPESERVICE = DESCRIPTOR.services_by_name['ScopeService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesB\x17ScopeServiceProtoPublicP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/public'
    _SCOPESERVICE.methods_by_name['AddScope']._options = None
    _SCOPESERVICE.methods_by_name['AddScope']._serialized_options = b'\x82\xd3\xe4\x93\x02\x16"\x11/api/v1/scope/add:\x01*'
    _SCOPESERVICE.methods_by_name['ExistScope']._options = None
    _SCOPESERVICE.methods_by_name['ExistScope']._serialized_options = b'\x82\xd3\xe4\x93\x02\x18"\x13/api/v1/scope/exist:\x01*'
    _SCOPESERVICE.methods_by_name['ListScope']._options = None
    _SCOPESERVICE.methods_by_name['ListScope']._serialized_options = b'\x82\xd3\xe4\x93\x02\x17"\x12/api/v1/scope/list:\x01*'
    _SCOPESERVICE._serialized_start = 147
    _SCOPESERVICE._serialized_end = 461