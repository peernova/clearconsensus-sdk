"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ..common import usermanagement_user_pb2 as common_dot_usermanagement__user__pb2
from ..common import usermanagement_fe_specific_pb2 as common_dot_usermanagement__fe__specific__pb2
from ..google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(public/usermanagement_user_service.proto\x124com.peernova.titanium.casbin.management.grpc.service\x1a common/usermanagement_user.proto\x1a\'common/usermanagement_fe_specific.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1egoogle/protobuf/wrappers.proto2\xc7\x05\n\x0bUserService\x12\xbb\x01\n\x06create\x12;.com.peernova.titanium.casbin.management.grpc.proto.UserDto\x1aC.com.peernova.titanium.casbin.management.grpc.proto.ServiceResponse"/\x82\xd3\xe4\x93\x02)"$/api/v1/user-management/users/create:\x01*\x12\xbb\x01\n\x06update\x12;.com.peernova.titanium.casbin.management.grpc.proto.UserDto\x1aC.com.peernova.titanium.casbin.management.grpc.proto.ServiceResponse"/\x82\xd3\xe4\x93\x02)"$/api/v1/user-management/users/update:\x01*\x12\x9e\x01\n\x07getById\x12\x1c.google.protobuf.StringValue\x1aC.com.peernova.titanium.casbin.management.grpc.proto.ServiceResponse"0\x82\xd3\xe4\x93\x02*"%/api/v1/user-management/users/getById:\x01*\x12\x9a\x01\n\x06getAll\x12\x1a.google.protobuf.BoolValue\x1aC.com.peernova.titanium.casbin.management.grpc.proto.ServiceResponse"/\x82\xd3\xe4\x93\x02)"$/api/v1/user-management/users/getAll:\x01*Bn\n4com.peernova.titanium.casbin.management.grpc.serviceP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/publicb\x06proto3')
_USERSERVICE = DESCRIPTOR.services_by_name['UserService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n4com.peernova.titanium.casbin.management.grpc.serviceP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/public'
    _USERSERVICE.methods_by_name['create']._options = None
    _USERSERVICE.methods_by_name['create']._serialized_options = b'\x82\xd3\xe4\x93\x02)"$/api/v1/user-management/users/create:\x01*'
    _USERSERVICE.methods_by_name['update']._options = None
    _USERSERVICE.methods_by_name['update']._serialized_options = b'\x82\xd3\xe4\x93\x02)"$/api/v1/user-management/users/update:\x01*'
    _USERSERVICE.methods_by_name['getById']._options = None
    _USERSERVICE.methods_by_name['getById']._serialized_options = b'\x82\xd3\xe4\x93\x02*"%/api/v1/user-management/users/getById:\x01*'
    _USERSERVICE.methods_by_name['getAll']._options = None
    _USERSERVICE.methods_by_name['getAll']._serialized_options = b'\x82\xd3\xe4\x93\x02)"$/api/v1/user-management/users/getAll:\x01*'
    _USERSERVICE._serialized_start = 236
    _USERSERVICE._serialized_end = 947