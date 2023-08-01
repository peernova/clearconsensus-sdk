"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2
from ..common import usermanagement_error_pb2 as common_dot_usermanagement__error__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"common/usermanagement_policy.proto\x122com.peernova.titanium.casbin.management.grpc.proto\x1a google/protobuf/descriptor.proto\x1a!common/usermanagement_error.proto"\x86\x01\n\tPolicyDto\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\x12\r\n\x05asset\x18\x03 \x01(\t\x12\x17\n\x0fassetPermission\x18\x04 \x01(\t\x12\x0b\n\x03api\x18\x05 \x01(\t\x12\x15\n\rapiPermission\x18\x06 \x01(\t\x12\r\n\x05addon\x18\x07 \x01(\t"\\\n\x08Policies\x12P\n\tpolicyDto\x18\x01 \x03(\x0b2=.com.peernova.titanium.casbin.management.grpc.proto.PolicyDto"\xb8\x01\n\x10PoliciesResponse\x12L\n\x04data\x18\x01 \x01(\x0b2<.com.peernova.titanium.casbin.management.grpc.proto.PoliciesH\x00\x12J\n\x05error\x18\x02 \x01(\x0b29.com.peernova.titanium.casbin.management.grpc.proto.ErrorH\x00B\n\n\x08response"\x1a\n\nPolicyType\x12\x0c\n\x04type\x18\x01 \x01(\t"A\n\x19UsernamePermissionRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x12\n\npermission\x18\x02 \x01(\t" \n\x0cPoliciesList\x12\x10\n\x08policies\x18\x01 \x03(\t"\xc0\x01\n\x14PoliciesListResponse\x12P\n\x04data\x18\x01 \x01(\x0b2@.com.peernova.titanium.casbin.management.grpc.proto.PoliciesListH\x00\x12J\n\x05error\x18\x02 \x01(\x0b29.com.peernova.titanium.casbin.management.grpc.proto.ErrorH\x00B\n\n\x08responseBl\n2com.peernova.titanium.casbin.management.grpc.protoP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/commonb\x06proto3')
_POLICYDTO = DESCRIPTOR.message_types_by_name['PolicyDto']
_POLICIES = DESCRIPTOR.message_types_by_name['Policies']
_POLICIESRESPONSE = DESCRIPTOR.message_types_by_name['PoliciesResponse']
_POLICYTYPE = DESCRIPTOR.message_types_by_name['PolicyType']
_USERNAMEPERMISSIONREQUEST = DESCRIPTOR.message_types_by_name['UsernamePermissionRequest']
_POLICIESLIST = DESCRIPTOR.message_types_by_name['PoliciesList']
_POLICIESLISTRESPONSE = DESCRIPTOR.message_types_by_name['PoliciesListResponse']
PolicyDto = _reflection.GeneratedProtocolMessageType('PolicyDto', (_message.Message,), {'DESCRIPTOR': _POLICYDTO, '__module__': 'common.usermanagement_policy_pb2'})
_sym_db.RegisterMessage(PolicyDto)
Policies = _reflection.GeneratedProtocolMessageType('Policies', (_message.Message,), {'DESCRIPTOR': _POLICIES, '__module__': 'common.usermanagement_policy_pb2'})
_sym_db.RegisterMessage(Policies)
PoliciesResponse = _reflection.GeneratedProtocolMessageType('PoliciesResponse', (_message.Message,), {'DESCRIPTOR': _POLICIESRESPONSE, '__module__': 'common.usermanagement_policy_pb2'})
_sym_db.RegisterMessage(PoliciesResponse)
PolicyType = _reflection.GeneratedProtocolMessageType('PolicyType', (_message.Message,), {'DESCRIPTOR': _POLICYTYPE, '__module__': 'common.usermanagement_policy_pb2'})
_sym_db.RegisterMessage(PolicyType)
UsernamePermissionRequest = _reflection.GeneratedProtocolMessageType('UsernamePermissionRequest', (_message.Message,), {'DESCRIPTOR': _USERNAMEPERMISSIONREQUEST, '__module__': 'common.usermanagement_policy_pb2'})
_sym_db.RegisterMessage(UsernamePermissionRequest)
PoliciesList = _reflection.GeneratedProtocolMessageType('PoliciesList', (_message.Message,), {'DESCRIPTOR': _POLICIESLIST, '__module__': 'common.usermanagement_policy_pb2'})
_sym_db.RegisterMessage(PoliciesList)
PoliciesListResponse = _reflection.GeneratedProtocolMessageType('PoliciesListResponse', (_message.Message,), {'DESCRIPTOR': _POLICIESLISTRESPONSE, '__module__': 'common.usermanagement_policy_pb2'})
_sym_db.RegisterMessage(PoliciesListResponse)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n2com.peernova.titanium.casbin.management.grpc.protoP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/common'
    _POLICYDTO._serialized_start = 160
    _POLICYDTO._serialized_end = 294
    _POLICIES._serialized_start = 296
    _POLICIES._serialized_end = 388
    _POLICIESRESPONSE._serialized_start = 391
    _POLICIESRESPONSE._serialized_end = 575
    _POLICYTYPE._serialized_start = 577
    _POLICYTYPE._serialized_end = 603
    _USERNAMEPERMISSIONREQUEST._serialized_start = 605
    _USERNAMEPERMISSIONREQUEST._serialized_end = 670
    _POLICIESLIST._serialized_start = 672
    _POLICIESLIST._serialized_end = 704
    _POLICIESLISTRESPONSE._serialized_start = 707
    _POLICIESLISTRESPONSE._serialized_end = 899