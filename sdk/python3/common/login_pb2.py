"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12common/login.proto\x12\x08titanium\x1a\x19common/gateway_base.proto" \n\x0cLoginRequest\x12\x10\n\x08username\x18\x01 \x01(\t"j\n\rLoginResponse\x12+\n\x04data\x18\x01 \x01(\x0b2\x1b.titanium.LoginResponseDataH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response""\n\x11LoginResponseData\x12\r\n\x05token\x18\x01 \x01(\tBs\n com.peernova.titanium.interfacesB\x17LoginServiceProtoCommonP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/commonb\x06proto3')
_LOGINREQUEST = DESCRIPTOR.message_types_by_name['LoginRequest']
_LOGINRESPONSE = DESCRIPTOR.message_types_by_name['LoginResponse']
_LOGINRESPONSEDATA = DESCRIPTOR.message_types_by_name['LoginResponseData']
LoginRequest = _reflection.GeneratedProtocolMessageType('LoginRequest', (_message.Message,), {'DESCRIPTOR': _LOGINREQUEST, '__module__': 'common.login_pb2'})
_sym_db.RegisterMessage(LoginRequest)
LoginResponse = _reflection.GeneratedProtocolMessageType('LoginResponse', (_message.Message,), {'DESCRIPTOR': _LOGINRESPONSE, '__module__': 'common.login_pb2'})
_sym_db.RegisterMessage(LoginResponse)
LoginResponseData = _reflection.GeneratedProtocolMessageType('LoginResponseData', (_message.Message,), {'DESCRIPTOR': _LOGINRESPONSEDATA, '__module__': 'common.login_pb2'})
_sym_db.RegisterMessage(LoginResponseData)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesB\x17LoginServiceProtoCommonP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/common'
    _LOGINREQUEST._serialized_start = 59
    _LOGINREQUEST._serialized_end = 91
    _LOGINRESPONSE._serialized_start = 93
    _LOGINRESPONSE._serialized_end = 199
    _LOGINRESPONSEDATA._serialized_start = 201
    _LOGINRESPONSEDATA._serialized_end = 235