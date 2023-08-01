"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ..common import usermanagement_error_pb2 as common_dot_usermanagement__error__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(common/usermanagement_group_policy.proto\x122com.peernova.titanium.casbin.management.grpc.proto\x1a!common/usermanagement_error.proto"?\n\x0eGroupPolicyDto\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\x12\r\n\x05group\x18\x03 \x01(\t"h\n\rGroupPolicies\x12W\n\x0bgroupPolicy\x18\x01 \x03(\x0b2B.com.peernova.titanium.casbin.management.grpc.proto.GroupPolicyDto"\xc2\x01\n\x15GroupPoliciesResponse\x12Q\n\x04data\x18\x01 \x01(\x0b2A.com.peernova.titanium.casbin.management.grpc.proto.GroupPoliciesH\x00\x12J\n\x05error\x18\x02 \x01(\x0b29.com.peernova.titanium.casbin.management.grpc.proto.ErrorH\x00B\n\n\x08responseBl\n2com.peernova.titanium.casbin.management.grpc.protoP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/commonb\x06proto3')
_GROUPPOLICYDTO = DESCRIPTOR.message_types_by_name['GroupPolicyDto']
_GROUPPOLICIES = DESCRIPTOR.message_types_by_name['GroupPolicies']
_GROUPPOLICIESRESPONSE = DESCRIPTOR.message_types_by_name['GroupPoliciesResponse']
GroupPolicyDto = _reflection.GeneratedProtocolMessageType('GroupPolicyDto', (_message.Message,), {'DESCRIPTOR': _GROUPPOLICYDTO, '__module__': 'common.usermanagement_group_policy_pb2'})
_sym_db.RegisterMessage(GroupPolicyDto)
GroupPolicies = _reflection.GeneratedProtocolMessageType('GroupPolicies', (_message.Message,), {'DESCRIPTOR': _GROUPPOLICIES, '__module__': 'common.usermanagement_group_policy_pb2'})
_sym_db.RegisterMessage(GroupPolicies)
GroupPoliciesResponse = _reflection.GeneratedProtocolMessageType('GroupPoliciesResponse', (_message.Message,), {'DESCRIPTOR': _GROUPPOLICIESRESPONSE, '__module__': 'common.usermanagement_group_policy_pb2'})
_sym_db.RegisterMessage(GroupPoliciesResponse)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n2com.peernova.titanium.casbin.management.grpc.protoP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/common'
    _GROUPPOLICYDTO._serialized_start = 131
    _GROUPPOLICYDTO._serialized_end = 194
    _GROUPPOLICIES._serialized_start = 196
    _GROUPPOLICIES._serialized_end = 300
    _GROUPPOLICIESRESPONSE._serialized_start = 303
    _GROUPPOLICIESRESPONSE._serialized_end = 497