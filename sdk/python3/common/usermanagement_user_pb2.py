"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ..common import usermanagement_fe_specific_pb2 as common_dot_usermanagement__fe__specific__pb2
from ..common import usermanagement_entity_pb2 as common_dot_usermanagement__entity__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n common/usermanagement_user.proto\x122com.peernova.titanium.casbin.management.grpc.proto\x1a\'common/usermanagement_fe_specific.proto\x1a"common/usermanagement_entity.proto"\xa9\x01\n\x07UserDto\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05email\x18\x02 \x01(\t\x12\x11\n\tfirstName\x18\x03 \x01(\t\x12\x10\n\x08lastName\x18\x04 \x01(\t\x12\x0f\n\x07enabled\x18\x05 \x01(\x08\x12M\n\x06entity\x18\x06 \x01(\x0b2=.com.peernova.titanium.casbin.management.grpc.proto.EntityDto"U\n\x08UsersDto\x12I\n\x04user\x18\x01 \x03(\x0b2;.com.peernova.titanium.casbin.management.grpc.proto.UserDtoBl\n2com.peernova.titanium.casbin.management.grpc.protoP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/commonb\x06proto3')
_USERDTO = DESCRIPTOR.message_types_by_name['UserDto']
_USERSDTO = DESCRIPTOR.message_types_by_name['UsersDto']
UserDto = _reflection.GeneratedProtocolMessageType('UserDto', (_message.Message,), {'DESCRIPTOR': _USERDTO, '__module__': 'common.usermanagement_user_pb2'})
_sym_db.RegisterMessage(UserDto)
UsersDto = _reflection.GeneratedProtocolMessageType('UsersDto', (_message.Message,), {'DESCRIPTOR': _USERSDTO, '__module__': 'common.usermanagement_user_pb2'})
_sym_db.RegisterMessage(UsersDto)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n2com.peernova.titanium.casbin.management.grpc.protoP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/common'
    _USERDTO._serialized_start = 166
    _USERDTO._serialized_end = 335
    _USERSDTO._serialized_start = 337
    _USERSDTO._serialized_end = 422