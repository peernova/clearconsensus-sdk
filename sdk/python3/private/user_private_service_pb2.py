"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ..google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ..common import user_controller_pb2 as common_dot_user__controller__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"private/user_private_service.proto\x12\x08titanium\x1a\x1cgoogle/api/annotations.proto\x1a\x1ccommon/user_controller.proto2\xa5\x02\n\x12UserPrivateService\x12U\n\x07AddUser\x12\x15.titanium.UserRequest\x1a\x16.titanium.UserResponse"\x1b\x82\xd3\xe4\x93\x02\x15"\x10/api/v1/user/add:\x01*\x12[\n\nUpdateUser\x12\x15.titanium.UserRequest\x1a\x16.titanium.UserResponse"\x1e\x82\xd3\xe4\x93\x02\x18"\x13/api/v1/user/update:\x01*\x12[\n\nDeleteUser\x12\x15.titanium.UserRequest\x1a\x16.titanium.UserResponse"\x1e\x82\xd3\xe4\x93\x02\x18"\x13/api/v1/user/delete:\x01*Bw\n com.peernova.titanium.interfacesB\x1aUserControllerProtoPrivateP\x01Z5github.com/peernova/clearconsensus-sdk/sdk/go/privateb\x06proto3')
_USERPRIVATESERVICE = DESCRIPTOR.services_by_name['UserPrivateService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesB\x1aUserControllerProtoPrivateP\x01Z5github.com/peernova/clearconsensus-sdk/sdk/go/private'
    _USERPRIVATESERVICE.methods_by_name['AddUser']._options = None
    _USERPRIVATESERVICE.methods_by_name['AddUser']._serialized_options = b'\x82\xd3\xe4\x93\x02\x15"\x10/api/v1/user/add:\x01*'
    _USERPRIVATESERVICE.methods_by_name['UpdateUser']._options = None
    _USERPRIVATESERVICE.methods_by_name['UpdateUser']._serialized_options = b'\x82\xd3\xe4\x93\x02\x18"\x13/api/v1/user/update:\x01*'
    _USERPRIVATESERVICE.methods_by_name['DeleteUser']._options = None
    _USERPRIVATESERVICE.methods_by_name['DeleteUser']._serialized_options = b'\x82\xd3\xe4\x93\x02\x18"\x13/api/v1/user/delete:\x01*'
    _USERPRIVATESERVICE._serialized_start = 109
    _USERPRIVATESERVICE._serialized_end = 402