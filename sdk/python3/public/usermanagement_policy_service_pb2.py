"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ..common import usermanagement_policy_pb2 as common_dot_usermanagement__policy__pb2
from ..common import usermanagement_fe_specific_pb2 as common_dot_usermanagement__fe__specific__pb2
from ..google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*public/usermanagement_policy_service.proto\x124com.peernova.titanium.casbin.management.grpc.service\x1a"common/usermanagement_policy.proto\x1a\'common/usermanagement_fe_specific.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1egoogle/protobuf/wrappers.proto2\xc2\x0b\n\rPolicyService\x12\xbf\x01\n\x06create\x12<.com.peernova.titanium.casbin.management.grpc.proto.Policies\x1aC.com.peernova.titanium.casbin.management.grpc.proto.ServiceResponse"2\x82\xd3\xe4\x93\x02,"\'/api/v1/user-management/policies/create:\x01*\x12\xcb\x01\n\x0bgetPolicies\x12>.com.peernova.titanium.casbin.management.grpc.proto.PolicyType\x1aC.com.peernova.titanium.casbin.management.grpc.proto.ServiceResponse"7\x82\xd3\xe4\x93\x021",/api/v1/user-management/policies/getPolicies:\x01*\x12\xcc\x01\n\x0cremovePolicy\x12=.com.peernova.titanium.casbin.management.grpc.proto.PolicyDto\x1aC.com.peernova.titanium.casbin.management.grpc.proto.ServiceResponse"8\x82\xd3\xe4\x93\x022"-/api/v1/user-management/policies/removePolicy:\x01*\x12\xca\x01\n\x0bcheckPolicy\x12=.com.peernova.titanium.casbin.management.grpc.proto.PolicyDto\x1aC.com.peernova.titanium.casbin.management.grpc.proto.ServiceResponse"7\x82\xd3\xe4\x93\x021",/api/v1/user-management/policies/checkPolicy:\x01*\x12\xd6\x01\n\tgetAssets\x12M.com.peernova.titanium.casbin.management.grpc.proto.UsernamePermissionRequest\x1aC.com.peernova.titanium.casbin.management.grpc.proto.ServiceResponse"5\x82\xd3\xe4\x93\x02/"*/api/v1/user-management/policies/getAssets:\x01*\x12\xd2\x01\n\x07getApis\x12M.com.peernova.titanium.casbin.management.grpc.proto.UsernamePermissionRequest\x1aC.com.peernova.titanium.casbin.management.grpc.proto.ServiceResponse"3\x82\xd3\xe4\x93\x02-"(/api/v1/user-management/policies/getApis:\x01*\x12\xd6\x01\n\tgetAddons\x12M.com.peernova.titanium.casbin.management.grpc.proto.UsernamePermissionRequest\x1aC.com.peernova.titanium.casbin.management.grpc.proto.ServiceResponse"5\x82\xd3\xe4\x93\x02/"*/api/v1/user-management/policies/getAddons:\x01*Bn\n4com.peernova.titanium.casbin.management.grpc.serviceP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/publicb\x06proto3')
_POLICYSERVICE = DESCRIPTOR.services_by_name['PolicyService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n4com.peernova.titanium.casbin.management.grpc.serviceP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/public'
    _POLICYSERVICE.methods_by_name['create']._options = None
    _POLICYSERVICE.methods_by_name['create']._serialized_options = b'\x82\xd3\xe4\x93\x02,"\'/api/v1/user-management/policies/create:\x01*'
    _POLICYSERVICE.methods_by_name['getPolicies']._options = None
    _POLICYSERVICE.methods_by_name['getPolicies']._serialized_options = b'\x82\xd3\xe4\x93\x021",/api/v1/user-management/policies/getPolicies:\x01*'
    _POLICYSERVICE.methods_by_name['removePolicy']._options = None
    _POLICYSERVICE.methods_by_name['removePolicy']._serialized_options = b'\x82\xd3\xe4\x93\x022"-/api/v1/user-management/policies/removePolicy:\x01*'
    _POLICYSERVICE.methods_by_name['checkPolicy']._options = None
    _POLICYSERVICE.methods_by_name['checkPolicy']._serialized_options = b'\x82\xd3\xe4\x93\x021",/api/v1/user-management/policies/checkPolicy:\x01*'
    _POLICYSERVICE.methods_by_name['getAssets']._options = None
    _POLICYSERVICE.methods_by_name['getAssets']._serialized_options = b'\x82\xd3\xe4\x93\x02/"*/api/v1/user-management/policies/getAssets:\x01*'
    _POLICYSERVICE.methods_by_name['getApis']._options = None
    _POLICYSERVICE.methods_by_name['getApis']._serialized_options = b'\x82\xd3\xe4\x93\x02-"(/api/v1/user-management/policies/getApis:\x01*'
    _POLICYSERVICE.methods_by_name['getAddons']._options = None
    _POLICYSERVICE.methods_by_name['getAddons']._serialized_options = b'\x82\xd3\xe4\x93\x02/"*/api/v1/user-management/policies/getAddons:\x01*'
    _POLICYSERVICE._serialized_start = 240
    _POLICYSERVICE._serialized_end = 1714