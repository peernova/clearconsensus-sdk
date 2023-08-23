"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ..google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ..common import user_pb2 as common_dot_user__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19public/user_service.proto\x12\x08titanium\x1a\x1cgoogle/api/annotations.proto\x1a\x11common/user.proto2\xcf\t\n\x0bUserService\x12T\n\x07GetUser\x12\x18.titanium.GetUserRequest\x1a\x16.titanium.UserResponse"\x17\x82\xd3\xe4\x93\x02\x11"\x0c/api/v1/user:\x01*\x12\x81\x01\n\x12GetUserPermissions\x12#.titanium.GetUserPermissionsRequest\x1a!.titanium.UserPermissionsResponse"#\x82\xd3\xe4\x93\x02\x1d"\x18/api/v1/user/permissions:\x01*\x12\x88\x01\n\x14GetUserNotifications\x12$.titanium.GetUserNotificationRequest\x1a#.titanium.UserNotificationsResponse"%\x82\xd3\xe4\x93\x02\x1f"\x1a/api/v1/user/notifications:\x01*\x12\x9f\x01\n\x1cGetUserNotificationsByMarket\x12,.titanium.GetUserNotificationByMarketRequest\x1a#.titanium.UserNotificationsResponse",\x82\xd3\xe4\x93\x02&"!/api/v1/user/notifications/market:\x01*\x12\x8d\x01\n\x16UpdateUserNotification\x12!.titanium.UserNotificationRequest\x1a".titanium.UserNotificationResponse",\x82\xd3\xe4\x93\x02&"!/api/v1/user/notifications/update:\x01*\x12\x87\x01\n\x13AddUserNotification\x12!.titanium.UserNotificationRequest\x1a".titanium.UserNotificationResponse")\x82\xd3\xe4\x93\x02#"\x1e/api/v1/user/notifications/add:\x01*\x12\x8d\x01\n\x16DeleteUserNotification\x12!.titanium.UserNotificationRequest\x1a".titanium.UserNotificationResponse",\x82\xd3\xe4\x93\x02&"!/api/v1/user/notifications/delete:\x01*\x12U\n\x07AddUser\x12\x15.titanium.UserRequest\x1a\x16.titanium.UserResponse"\x1b\x82\xd3\xe4\x93\x02\x15"\x10/api/v1/user/add:\x01*\x12[\n\nUpdateUser\x12\x15.titanium.UserRequest\x1a\x16.titanium.UserResponse"\x1e\x82\xd3\xe4\x93\x02\x18"\x13/api/v1/user/update:\x01*\x12[\n\nDeleteUser\x12\x15.titanium.UserRequest\x1a\x16.titanium.UserResponse"\x1e\x82\xd3\xe4\x93\x02\x18"\x13/api/v1/user/delete:\x01*Bu\n com.peernova.titanium.interfacesB\x19UserControllerProtoPublicP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/publicb\x06proto3')
_USERSERVICE = DESCRIPTOR.services_by_name['UserService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesB\x19UserControllerProtoPublicP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/public'
    _USERSERVICE.methods_by_name['GetUser']._options = None
    _USERSERVICE.methods_by_name['GetUser']._serialized_options = b'\x82\xd3\xe4\x93\x02\x11"\x0c/api/v1/user:\x01*'
    _USERSERVICE.methods_by_name['GetUserPermissions']._options = None
    _USERSERVICE.methods_by_name['GetUserPermissions']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1d"\x18/api/v1/user/permissions:\x01*'
    _USERSERVICE.methods_by_name['GetUserNotifications']._options = None
    _USERSERVICE.methods_by_name['GetUserNotifications']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1f"\x1a/api/v1/user/notifications:\x01*'
    _USERSERVICE.methods_by_name['GetUserNotificationsByMarket']._options = None
    _USERSERVICE.methods_by_name['GetUserNotificationsByMarket']._serialized_options = b'\x82\xd3\xe4\x93\x02&"!/api/v1/user/notifications/market:\x01*'
    _USERSERVICE.methods_by_name['UpdateUserNotification']._options = None
    _USERSERVICE.methods_by_name['UpdateUserNotification']._serialized_options = b'\x82\xd3\xe4\x93\x02&"!/api/v1/user/notifications/update:\x01*'
    _USERSERVICE.methods_by_name['AddUserNotification']._options = None
    _USERSERVICE.methods_by_name['AddUserNotification']._serialized_options = b'\x82\xd3\xe4\x93\x02#"\x1e/api/v1/user/notifications/add:\x01*'
    _USERSERVICE.methods_by_name['DeleteUserNotification']._options = None
    _USERSERVICE.methods_by_name['DeleteUserNotification']._serialized_options = b'\x82\xd3\xe4\x93\x02&"!/api/v1/user/notifications/delete:\x01*'
    _USERSERVICE.methods_by_name['AddUser']._options = None
    _USERSERVICE.methods_by_name['AddUser']._serialized_options = b'\x82\xd3\xe4\x93\x02\x15"\x10/api/v1/user/add:\x01*'
    _USERSERVICE.methods_by_name['UpdateUser']._options = None
    _USERSERVICE.methods_by_name['UpdateUser']._serialized_options = b'\x82\xd3\xe4\x93\x02\x18"\x13/api/v1/user/update:\x01*'
    _USERSERVICE.methods_by_name['DeleteUser']._options = None
    _USERSERVICE.methods_by_name['DeleteUser']._serialized_options = b'\x82\xd3\xe4\x93\x02\x18"\x13/api/v1/user/delete:\x01*'
    _USERSERVICE._serialized_start = 89
    _USERSERVICE._serialized_end = 1320