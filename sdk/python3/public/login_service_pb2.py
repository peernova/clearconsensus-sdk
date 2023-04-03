"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ..google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ..common import login_pb2 as common_dot_login__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1apublic/login_service.proto\x12\x08titanium\x1a\x1cgoogle/api/annotations.proto\x1a\x12common/login.proto2b\n\x0cLoginService\x12R\n\x05Login\x12\x16.titanium.LoginRequest\x1a\x17.titanium.LoginResponse"\x18\x82\xd3\xe4\x93\x02\x12"\r/api/v1/login:\x01*Bs\n com.peernova.titanium.interfacesB\x17LoginServiceProtoPublicP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/publicb\x06proto3')
_LOGINSERVICE = DESCRIPTOR.services_by_name['LoginService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesB\x17LoginServiceProtoPublicP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/public'
    _LOGINSERVICE.methods_by_name['Login']._options = None
    _LOGINSERVICE.methods_by_name['Login']._serialized_options = b'\x82\xd3\xe4\x93\x02\x12"\r/api/v1/login:\x01*'
    _LOGINSERVICE._serialized_start = 90
    _LOGINSERVICE._serialized_end = 188