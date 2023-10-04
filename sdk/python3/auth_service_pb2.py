"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from .google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .common import gateway_base_pb2 as common_dot_gateway__base__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12auth_service.proto\x12\x1ecom.peernova.titanium.security\x1a\x1cgoogle/api/annotations.proto\x1a\x19common/gateway_base.proto"\xec\x05\n\x0bAuthRequest\x12R\n\x0eauthentication\x18\x01 \x01(\x0b2:.com.peernova.titanium.security.AuthRequest.Authentication\x12P\n\rauthorization\x18\x02 \x01(\x0b29.com.peernova.titanium.security.AuthRequest.Authorization\x1a,\n\x0eAuthentication\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05token\x18\x02 \x01(\t\x1a\x88\x04\n\rAuthorization\x12P\n\x06method\x18\x01 \x01(\x0e2@.com.peernova.titanium.security.AuthRequest.Authorization.Method\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\r\n\x05asset\x18\x03 \x01(\t\x12Q\n\x04time\x18\x04 \x01(\x0b2C.com.peernova.titanium.security.AuthRequest.Authorization.TimeStamp\x1a\xbf\x01\n\tTimeStamp\x12\x12\n\x08epoch_ms\x18\x01 \x01(\x03H\x00\x12Z\n\x05range\x18\x02 \x01(\x0b2I.com.peernova.titanium.security.AuthRequest.Authorization.TimeStamp.RangeH\x00\x1a5\n\x05Range\x12\x16\n\x0estart_epoch_ms\x18\x01 \x01(\x03\x12\x14\n\x0cend_epoch_ms\x18\x02 \x01(\x03B\x0b\n\ttime_kind"s\n\x06Method\x12\x07\n\x03RPC\x10\x00\x12\x07\n\x03GET\x10\x01\x12\x08\n\x04HEAD\x10\x02\x12\x08\n\x04POST\x10\x03\x12\x07\n\x03PUT\x10\x04\x12\n\n\x06DELETE\x10\x05\x12\x0b\n\x07CONNECT\x10\x06\x12\x0b\n\x07OPTIONS\x10\x07\x12\t\n\x05TRACE\x10\x08\x12\t\n\x05PATCH\x10\t"\xa1\x06\n\x0cAuthResponse\x12\x0f\n\x07allowed\x18\x01 \x01(\x08\x12N\n\x04data\x18\x02 \x01(\x0b2>.com.peernova.titanium.security.AuthResponse.AuthorizationDataH\x00\x12 \n\x05error\x18\x03 \x01(\x0b2\x0f.titanium.ErrorH\x00\x1a\x81\x05\n\x11AuthorizationData\x12\x15\n\rauthenticated\x18\x01 \x01(\x08\x12h\n\trequester\x18\x02 \x01(\x0b2S.com.peernova.titanium.security.AuthResponse.AuthorizationData.RequesterInformationH\x00\x12/\n\x14authentication_error\x18\x03 \x01(\x0b2\x0f.titanium.ErrorH\x00\x12\x12\n\nauthorized\x18\x04 \x01(\x08\x12,\n\x13authorization_error\x18\x05 \x01(\x0b2\x0f.titanium.Error\x1a\xe5\x02\n\x14RequesterInformation\x12\n\n\x02id\x18\x01 \x01(\t\x12t\n\x0bparticipant\x18\x02 \x01(\x0b2_.com.peernova.titanium.security.AuthResponse.AuthorizationData.RequesterInformation.Participant\x12f\n\x04user\x18\x03 \x01(\x0b2X.com.peernova.titanium.security.AuthResponse.AuthorizationData.RequesterInformation.User\x1a:\n\x04User\x12\r\n\x05email\x18\x01 \x01(\t\x12\x11\n\tfirstName\x18\x02 \x01(\t\x12\x10\n\x08lastName\x18\x03 \x01(\t\x1a\'\n\x0bParticipant\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\tB\x10\n\x0eauthenticationB\n\n\x08response2\x9a\x01\n\x0bAuthService\x12\x8a\x01\n\x05Check\x12+.com.peernova.titanium.security.AuthRequest\x1a,.com.peernova.titanium.security.AuthResponse"&\x82\xd3\xe4\x93\x02 "\x1e/api/v1/internal/security/authB1P\x01Z-github.com/peernova/clearconsensus-sdk/sdk/gob\x06proto3')
_AUTHREQUEST = DESCRIPTOR.message_types_by_name['AuthRequest']
_AUTHREQUEST_AUTHENTICATION = _AUTHREQUEST.nested_types_by_name['Authentication']
_AUTHREQUEST_AUTHORIZATION = _AUTHREQUEST.nested_types_by_name['Authorization']
_AUTHREQUEST_AUTHORIZATION_TIMESTAMP = _AUTHREQUEST_AUTHORIZATION.nested_types_by_name['TimeStamp']
_AUTHREQUEST_AUTHORIZATION_TIMESTAMP_RANGE = _AUTHREQUEST_AUTHORIZATION_TIMESTAMP.nested_types_by_name['Range']
_AUTHRESPONSE = DESCRIPTOR.message_types_by_name['AuthResponse']
_AUTHRESPONSE_AUTHORIZATIONDATA = _AUTHRESPONSE.nested_types_by_name['AuthorizationData']
_AUTHRESPONSE_AUTHORIZATIONDATA_REQUESTERINFORMATION = _AUTHRESPONSE_AUTHORIZATIONDATA.nested_types_by_name['RequesterInformation']
_AUTHRESPONSE_AUTHORIZATIONDATA_REQUESTERINFORMATION_USER = _AUTHRESPONSE_AUTHORIZATIONDATA_REQUESTERINFORMATION.nested_types_by_name['User']
_AUTHRESPONSE_AUTHORIZATIONDATA_REQUESTERINFORMATION_PARTICIPANT = _AUTHRESPONSE_AUTHORIZATIONDATA_REQUESTERINFORMATION.nested_types_by_name['Participant']
_AUTHREQUEST_AUTHORIZATION_METHOD = _AUTHREQUEST_AUTHORIZATION.enum_types_by_name['Method']
AuthRequest = _reflection.GeneratedProtocolMessageType('AuthRequest', (_message.Message,), {'Authentication': _reflection.GeneratedProtocolMessageType('Authentication', (_message.Message,), {'DESCRIPTOR': _AUTHREQUEST_AUTHENTICATION, '__module__': 'auth_service_pb2'}), 'Authorization': _reflection.GeneratedProtocolMessageType('Authorization', (_message.Message,), {'TimeStamp': _reflection.GeneratedProtocolMessageType('TimeStamp', (_message.Message,), {'Range': _reflection.GeneratedProtocolMessageType('Range', (_message.Message,), {'DESCRIPTOR': _AUTHREQUEST_AUTHORIZATION_TIMESTAMP_RANGE, '__module__': 'auth_service_pb2'}), 'DESCRIPTOR': _AUTHREQUEST_AUTHORIZATION_TIMESTAMP, '__module__': 'auth_service_pb2'}), 'DESCRIPTOR': _AUTHREQUEST_AUTHORIZATION, '__module__': 'auth_service_pb2'}), 'DESCRIPTOR': _AUTHREQUEST, '__module__': 'auth_service_pb2'})
_sym_db.RegisterMessage(AuthRequest)
_sym_db.RegisterMessage(AuthRequest.Authentication)
_sym_db.RegisterMessage(AuthRequest.Authorization)
_sym_db.RegisterMessage(AuthRequest.Authorization.TimeStamp)
_sym_db.RegisterMessage(AuthRequest.Authorization.TimeStamp.Range)
AuthResponse = _reflection.GeneratedProtocolMessageType('AuthResponse', (_message.Message,), {'AuthorizationData': _reflection.GeneratedProtocolMessageType('AuthorizationData', (_message.Message,), {'RequesterInformation': _reflection.GeneratedProtocolMessageType('RequesterInformation', (_message.Message,), {'User': _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {'DESCRIPTOR': _AUTHRESPONSE_AUTHORIZATIONDATA_REQUESTERINFORMATION_USER, '__module__': 'auth_service_pb2'}), 'Participant': _reflection.GeneratedProtocolMessageType('Participant', (_message.Message,), {'DESCRIPTOR': _AUTHRESPONSE_AUTHORIZATIONDATA_REQUESTERINFORMATION_PARTICIPANT, '__module__': 'auth_service_pb2'}), 'DESCRIPTOR': _AUTHRESPONSE_AUTHORIZATIONDATA_REQUESTERINFORMATION, '__module__': 'auth_service_pb2'}), 'DESCRIPTOR': _AUTHRESPONSE_AUTHORIZATIONDATA, '__module__': 'auth_service_pb2'}), 'DESCRIPTOR': _AUTHRESPONSE, '__module__': 'auth_service_pb2'})
_sym_db.RegisterMessage(AuthResponse)
_sym_db.RegisterMessage(AuthResponse.AuthorizationData)
_sym_db.RegisterMessage(AuthResponse.AuthorizationData.RequesterInformation)
_sym_db.RegisterMessage(AuthResponse.AuthorizationData.RequesterInformation.User)
_sym_db.RegisterMessage(AuthResponse.AuthorizationData.RequesterInformation.Participant)
_AUTHSERVICE = DESCRIPTOR.services_by_name['AuthService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'P\x01Z-github.com/peernova/clearconsensus-sdk/sdk/go'
    _AUTHSERVICE.methods_by_name['Check']._options = None
    _AUTHSERVICE.methods_by_name['Check']._serialized_options = b'\x82\xd3\xe4\x93\x02 "\x1e/api/v1/internal/security/auth'
    _AUTHREQUEST._serialized_start = 112
    _AUTHREQUEST._serialized_end = 860
    _AUTHREQUEST_AUTHENTICATION._serialized_start = 293
    _AUTHREQUEST_AUTHENTICATION._serialized_end = 337
    _AUTHREQUEST_AUTHORIZATION._serialized_start = 340
    _AUTHREQUEST_AUTHORIZATION._serialized_end = 860
    _AUTHREQUEST_AUTHORIZATION_TIMESTAMP._serialized_start = 552
    _AUTHREQUEST_AUTHORIZATION_TIMESTAMP._serialized_end = 743
    _AUTHREQUEST_AUTHORIZATION_TIMESTAMP_RANGE._serialized_start = 677
    _AUTHREQUEST_AUTHORIZATION_TIMESTAMP_RANGE._serialized_end = 730
    _AUTHREQUEST_AUTHORIZATION_METHOD._serialized_start = 745
    _AUTHREQUEST_AUTHORIZATION_METHOD._serialized_end = 860
    _AUTHRESPONSE._serialized_start = 863
    _AUTHRESPONSE._serialized_end = 1664
    _AUTHRESPONSE_AUTHORIZATIONDATA._serialized_start = 1011
    _AUTHRESPONSE_AUTHORIZATIONDATA._serialized_end = 1652
    _AUTHRESPONSE_AUTHORIZATIONDATA_REQUESTERINFORMATION._serialized_start = 1277
    _AUTHRESPONSE_AUTHORIZATIONDATA_REQUESTERINFORMATION._serialized_end = 1634
    _AUTHRESPONSE_AUTHORIZATIONDATA_REQUESTERINFORMATION_USER._serialized_start = 1535
    _AUTHRESPONSE_AUTHORIZATIONDATA_REQUESTERINFORMATION_USER._serialized_end = 1593
    _AUTHRESPONSE_AUTHORIZATIONDATA_REQUESTERINFORMATION_PARTICIPANT._serialized_start = 1595
    _AUTHRESPONSE_AUTHORIZATIONDATA_REQUESTERINFORMATION_PARTICIPANT._serialized_end = 1634
    _AUTHSERVICE._serialized_start = 1667
    _AUTHSERVICE._serialized_end = 1821