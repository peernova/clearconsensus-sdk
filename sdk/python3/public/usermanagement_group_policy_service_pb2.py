"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ..common import usermanagement_group_policy_pb2 as common_dot_usermanagement__group__policy__pb2
from ..common import usermanagement_fe_specific_pb2 as common_dot_usermanagement__fe__specific__pb2
from ..common import usermanagement_policy_pb2 as common_dot_usermanagement__policy__pb2
from ..google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0public/usermanagement_group_policy_service.proto\x124com.peernova.titanium.casbin.management.grpc.service\x1a(common/usermanagement_group_policy.proto\x1a\'common/usermanagement_fe_specific.proto\x1a"common/usermanagement_policy.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1egoogle/protobuf/wrappers.proto2\xb5\x03\n\x12GroupPolicyService\x12\xca\x01\n\x06create\x12A.com.peernova.titanium.casbin.management.grpc.proto.GroupPolicies\x1aC.com.peernova.titanium.casbin.management.grpc.proto.ServiceResponse"8\x82\xd3\xe4\x93\x022"-/api/v1/user-management/group-policies/create:\x01*\x12\xd1\x01\n\x0bgetPolicies\x12>.com.peernova.titanium.casbin.management.grpc.proto.PolicyType\x1aC.com.peernova.titanium.casbin.management.grpc.proto.ServiceResponse"=\x82\xd3\xe4\x93\x027"2/api/v1/user-management/group-policies/getPolicies:\x01*Bn\n4com.peernova.titanium.casbin.management.grpc.serviceP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/publicb\x06proto3')
_GROUPPOLICYSERVICE = DESCRIPTOR.services_by_name['GroupPolicyService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n4com.peernova.titanium.casbin.management.grpc.serviceP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/public'
    _GROUPPOLICYSERVICE.methods_by_name['create']._options = None
    _GROUPPOLICYSERVICE.methods_by_name['create']._serialized_options = b'\x82\xd3\xe4\x93\x022"-/api/v1/user-management/group-policies/create:\x01*'
    _GROUPPOLICYSERVICE.methods_by_name['getPolicies']._options = None
    _GROUPPOLICYSERVICE.methods_by_name['getPolicies']._serialized_options = b'\x82\xd3\xe4\x93\x027"2/api/v1/user-management/group-policies/getPolicies:\x01*'
    _GROUPPOLICYSERVICE._serialized_start = 288
    _GROUPPOLICYSERVICE._serialized_end = 725