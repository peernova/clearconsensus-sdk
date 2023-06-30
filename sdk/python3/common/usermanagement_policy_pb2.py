"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"common/usermanagement_policy.proto\x122com.peernova.titanium.casbin.management.grpc.proto\x1a google/protobuf/descriptor.proto"\x86\x01\n\tPolicyDto\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\x12\r\n\x05asset\x18\x03 \x01(\t\x12\x17\n\x0fassetPermission\x18\x04 \x01(\t\x12\x0b\n\x03api\x18\x05 \x01(\t\x12\x15\n\rapiPermission\x18\x06 \x01(\t\x12\r\n\x05addon\x18\x07 \x01(\t"\\\n\x08Policies\x12P\n\tpolicyDto\x18\x01 \x03(\x0b2=.com.peernova.titanium.casbin.management.grpc.proto.PolicyDto"A\n\x19UsernamePermissionRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x12\n\npermission\x18\x02 \x01(\t"$\n\x10PoliciesResponse\x12\x10\n\x08policies\x18\x01 \x03(\t*H\n\x08TypeEnum\x12\x0e\n\nASSET_TYPE\x10\x00\x12\x0c\n\x08API_TYPE\x10\x01\x12\x0e\n\nADDON_TYPE\x10\x02\x12\x0e\n\nGROUP_TYPE\x10\x03Bl\n2com.peernova.titanium.casbin.management.grpc.protoP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/commonb\x06proto3')
_TYPEENUM = DESCRIPTOR.enum_types_by_name['TypeEnum']
TypeEnum = enum_type_wrapper.EnumTypeWrapper(_TYPEENUM)
ASSET_TYPE = 0
API_TYPE = 1
ADDON_TYPE = 2
GROUP_TYPE = 3
_POLICYDTO = DESCRIPTOR.message_types_by_name['PolicyDto']
_POLICIES = DESCRIPTOR.message_types_by_name['Policies']
_USERNAMEPERMISSIONREQUEST = DESCRIPTOR.message_types_by_name['UsernamePermissionRequest']
_POLICIESRESPONSE = DESCRIPTOR.message_types_by_name['PoliciesResponse']
PolicyDto = _reflection.GeneratedProtocolMessageType('PolicyDto', (_message.Message,), {'DESCRIPTOR': _POLICYDTO, '__module__': 'common.usermanagement_policy_pb2'})
_sym_db.RegisterMessage(PolicyDto)
Policies = _reflection.GeneratedProtocolMessageType('Policies', (_message.Message,), {'DESCRIPTOR': _POLICIES, '__module__': 'common.usermanagement_policy_pb2'})
_sym_db.RegisterMessage(Policies)
UsernamePermissionRequest = _reflection.GeneratedProtocolMessageType('UsernamePermissionRequest', (_message.Message,), {'DESCRIPTOR': _USERNAMEPERMISSIONREQUEST, '__module__': 'common.usermanagement_policy_pb2'})
_sym_db.RegisterMessage(UsernamePermissionRequest)
PoliciesResponse = _reflection.GeneratedProtocolMessageType('PoliciesResponse', (_message.Message,), {'DESCRIPTOR': _POLICIESRESPONSE, '__module__': 'common.usermanagement_policy_pb2'})
_sym_db.RegisterMessage(PoliciesResponse)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n2com.peernova.titanium.casbin.management.grpc.protoP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/common'
    _TYPEENUM._serialized_start = 460
    _TYPEENUM._serialized_end = 532
    _POLICYDTO._serialized_start = 125
    _POLICYDTO._serialized_end = 259
    _POLICIES._serialized_start = 261
    _POLICIES._serialized_end = 353
    _USERNAMEPERMISSIONREQUEST._serialized_start = 355
    _USERNAMEPERMISSIONREQUEST._serialized_end = 420
    _POLICIESRESPONSE._serialized_start = 422
    _POLICIESRESPONSE._serialized_end = 458