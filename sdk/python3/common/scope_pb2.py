"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12common/scope.proto\x12\x08titanium\x1a\x19common/gateway_base.proto" \n\x0fScopeIdentifier\x12\r\n\x05scope\x18\x01 \x01(\t"A\n\x11ScopeListResponse\x12\x0c\n\x04data\x18\x01 \x03(\t\x12\x1e\n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.Error"C\n\x12ScopeExistResponse\x12\r\n\x05exist\x18\x01 \x01(\x08\x12\x1e\n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorBs\n com.peernova.titanium.interfacesB\x17ScopeServiceProtoCommonP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/commonb\x06proto3')
_SCOPEIDENTIFIER = DESCRIPTOR.message_types_by_name['ScopeIdentifier']
_SCOPELISTRESPONSE = DESCRIPTOR.message_types_by_name['ScopeListResponse']
_SCOPEEXISTRESPONSE = DESCRIPTOR.message_types_by_name['ScopeExistResponse']
ScopeIdentifier = _reflection.GeneratedProtocolMessageType('ScopeIdentifier', (_message.Message,), {'DESCRIPTOR': _SCOPEIDENTIFIER, '__module__': 'common.scope_pb2'})
_sym_db.RegisterMessage(ScopeIdentifier)
ScopeListResponse = _reflection.GeneratedProtocolMessageType('ScopeListResponse', (_message.Message,), {'DESCRIPTOR': _SCOPELISTRESPONSE, '__module__': 'common.scope_pb2'})
_sym_db.RegisterMessage(ScopeListResponse)
ScopeExistResponse = _reflection.GeneratedProtocolMessageType('ScopeExistResponse', (_message.Message,), {'DESCRIPTOR': _SCOPEEXISTRESPONSE, '__module__': 'common.scope_pb2'})
_sym_db.RegisterMessage(ScopeExistResponse)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesB\x17ScopeServiceProtoCommonP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/common'
    _SCOPEIDENTIFIER._serialized_start = 59
    _SCOPEIDENTIFIER._serialized_end = 91
    _SCOPELISTRESPONSE._serialized_start = 93
    _SCOPELISTRESPONSE._serialized_end = 158
    _SCOPEEXISTRESPONSE._serialized_start = 160
    _SCOPEEXISTRESPONSE._serialized_end = 227