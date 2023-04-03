"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ccommon/user_controller.proto\x12\x08titanium\x1a\x19common/gateway_base.proto"\x1f\n\x0eGetUserRequest\x12\r\n\x05email\x18\x01 \x01(\t"+\n\x0bUserRequest\x12\x1c\n\x04user\x18\x01 \x01(\x0b2\x0e.titanium.User"\\\n\x0cUserResponse\x12\x1e\n\x04user\x18\x01 \x01(\x0b2\x0e.titanium.UserH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"w\n\x04User\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05email\x18\x02 \x01(\t\x12\x14\n\x0corganization\x18\x03 \x01(\t\x12\x1f\n\x17notify_by_email_enabled\x18\x04 \x01(\x08\x12\x1d\n\x15notify_by_app_enabled\x18\x05 \x01(\x08",\n\x19GetUserPermissionsRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t"~\n\x17UserPermissionsResponse\x125\n\x10user_permissions\x18\x01 \x01(\x0b2\x19.titanium.UserPermissionsH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"D\n\x0fUserPermissions\x121\n\x0fuser_permission\x18\x01 \x03(\x0b2\x18.titanium.UserPermission"U\n\x0eUserPermission\x12\x10\n\x08asset_id\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x0f\n\x07enabled\x18\x03 \x01(\x08\x12\x12\n\ntrace_name\x18\x04 \x01(\t"-\n\x1aGetUserNotificationRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t"H\n"GetUserNotificationByMarketRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x11\n\tmarket_id\x18\x02 \x01(\t"\x84\x01\n\x19UserNotificationsResponse\x129\n\x12user_notifications\x18\x01 \x01(\x0b2\x1b.titanium.UserNotificationsH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"P\n\x17UserNotificationRequest\x125\n\x11user_notification\x18\x01 \x01(\x0b2\x1a.titanium.UserNotification"J\n\x11UserNotifications\x125\n\x11user_notification\x18\x01 \x03(\x0b2\x1a.titanium.UserNotification"\x9c\x01\n\x10UserNotification\x12\n\n\x02id\x18\x01 \x01(\t\x12\x1c\n\x04user\x18\x02 \x01(\x0b2\x0e.titanium.User\x12\x1f\n\x05asset\x18\x03 \x01(\x0b2\x10.titanium.AssetM\x12 \n\x06market\x18\x04 \x01(\x0b2\x10.titanium.Market\x12\x0c\n\x04type\x18\x05 \x01(\t\x12\r\n\x05value\x18\x06 \x01(\t"<\n\x06AssetM\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x18\n\x10instrument_types\x18\x02 \x03(\t\x12\n\n\x02id\x18\x03 \x01(\t"@\n\x06Market\x12\n\n\x02id\x18\x01 \x01(\t\x12\x1c\n\x04user\x18\x02 \x01(\x0b2\x0e.titanium.User\x12\x0c\n\x04name\x18\x03 \x01(\t"\x81\x01\n\x18UserNotificationResponse\x127\n\x11user_notification\x18\x01 \x01(\x0b2\x1a.titanium.UserNotificationH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08responseBu\n com.peernova.titanium.interfacesB\x19UserControllerProtoCommonP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/commonb\x06proto3')
_GETUSERREQUEST = DESCRIPTOR.message_types_by_name['GetUserRequest']
_USERREQUEST = DESCRIPTOR.message_types_by_name['UserRequest']
_USERRESPONSE = DESCRIPTOR.message_types_by_name['UserResponse']
_USER = DESCRIPTOR.message_types_by_name['User']
_GETUSERPERMISSIONSREQUEST = DESCRIPTOR.message_types_by_name['GetUserPermissionsRequest']
_USERPERMISSIONSRESPONSE = DESCRIPTOR.message_types_by_name['UserPermissionsResponse']
_USERPERMISSIONS = DESCRIPTOR.message_types_by_name['UserPermissions']
_USERPERMISSION = DESCRIPTOR.message_types_by_name['UserPermission']
_GETUSERNOTIFICATIONREQUEST = DESCRIPTOR.message_types_by_name['GetUserNotificationRequest']
_GETUSERNOTIFICATIONBYMARKETREQUEST = DESCRIPTOR.message_types_by_name['GetUserNotificationByMarketRequest']
_USERNOTIFICATIONSRESPONSE = DESCRIPTOR.message_types_by_name['UserNotificationsResponse']
_USERNOTIFICATIONREQUEST = DESCRIPTOR.message_types_by_name['UserNotificationRequest']
_USERNOTIFICATIONS = DESCRIPTOR.message_types_by_name['UserNotifications']
_USERNOTIFICATION = DESCRIPTOR.message_types_by_name['UserNotification']
_ASSETM = DESCRIPTOR.message_types_by_name['AssetM']
_MARKET = DESCRIPTOR.message_types_by_name['Market']
_USERNOTIFICATIONRESPONSE = DESCRIPTOR.message_types_by_name['UserNotificationResponse']
GetUserRequest = _reflection.GeneratedProtocolMessageType('GetUserRequest', (_message.Message,), {'DESCRIPTOR': _GETUSERREQUEST, '__module__': 'common.user_controller_pb2'})
_sym_db.RegisterMessage(GetUserRequest)
UserRequest = _reflection.GeneratedProtocolMessageType('UserRequest', (_message.Message,), {'DESCRIPTOR': _USERREQUEST, '__module__': 'common.user_controller_pb2'})
_sym_db.RegisterMessage(UserRequest)
UserResponse = _reflection.GeneratedProtocolMessageType('UserResponse', (_message.Message,), {'DESCRIPTOR': _USERRESPONSE, '__module__': 'common.user_controller_pb2'})
_sym_db.RegisterMessage(UserResponse)
User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {'DESCRIPTOR': _USER, '__module__': 'common.user_controller_pb2'})
_sym_db.RegisterMessage(User)
GetUserPermissionsRequest = _reflection.GeneratedProtocolMessageType('GetUserPermissionsRequest', (_message.Message,), {'DESCRIPTOR': _GETUSERPERMISSIONSREQUEST, '__module__': 'common.user_controller_pb2'})
_sym_db.RegisterMessage(GetUserPermissionsRequest)
UserPermissionsResponse = _reflection.GeneratedProtocolMessageType('UserPermissionsResponse', (_message.Message,), {'DESCRIPTOR': _USERPERMISSIONSRESPONSE, '__module__': 'common.user_controller_pb2'})
_sym_db.RegisterMessage(UserPermissionsResponse)
UserPermissions = _reflection.GeneratedProtocolMessageType('UserPermissions', (_message.Message,), {'DESCRIPTOR': _USERPERMISSIONS, '__module__': 'common.user_controller_pb2'})
_sym_db.RegisterMessage(UserPermissions)
UserPermission = _reflection.GeneratedProtocolMessageType('UserPermission', (_message.Message,), {'DESCRIPTOR': _USERPERMISSION, '__module__': 'common.user_controller_pb2'})
_sym_db.RegisterMessage(UserPermission)
GetUserNotificationRequest = _reflection.GeneratedProtocolMessageType('GetUserNotificationRequest', (_message.Message,), {'DESCRIPTOR': _GETUSERNOTIFICATIONREQUEST, '__module__': 'common.user_controller_pb2'})
_sym_db.RegisterMessage(GetUserNotificationRequest)
GetUserNotificationByMarketRequest = _reflection.GeneratedProtocolMessageType('GetUserNotificationByMarketRequest', (_message.Message,), {'DESCRIPTOR': _GETUSERNOTIFICATIONBYMARKETREQUEST, '__module__': 'common.user_controller_pb2'})
_sym_db.RegisterMessage(GetUserNotificationByMarketRequest)
UserNotificationsResponse = _reflection.GeneratedProtocolMessageType('UserNotificationsResponse', (_message.Message,), {'DESCRIPTOR': _USERNOTIFICATIONSRESPONSE, '__module__': 'common.user_controller_pb2'})
_sym_db.RegisterMessage(UserNotificationsResponse)
UserNotificationRequest = _reflection.GeneratedProtocolMessageType('UserNotificationRequest', (_message.Message,), {'DESCRIPTOR': _USERNOTIFICATIONREQUEST, '__module__': 'common.user_controller_pb2'})
_sym_db.RegisterMessage(UserNotificationRequest)
UserNotifications = _reflection.GeneratedProtocolMessageType('UserNotifications', (_message.Message,), {'DESCRIPTOR': _USERNOTIFICATIONS, '__module__': 'common.user_controller_pb2'})
_sym_db.RegisterMessage(UserNotifications)
UserNotification = _reflection.GeneratedProtocolMessageType('UserNotification', (_message.Message,), {'DESCRIPTOR': _USERNOTIFICATION, '__module__': 'common.user_controller_pb2'})
_sym_db.RegisterMessage(UserNotification)
AssetM = _reflection.GeneratedProtocolMessageType('AssetM', (_message.Message,), {'DESCRIPTOR': _ASSETM, '__module__': 'common.user_controller_pb2'})
_sym_db.RegisterMessage(AssetM)
Market = _reflection.GeneratedProtocolMessageType('Market', (_message.Message,), {'DESCRIPTOR': _MARKET, '__module__': 'common.user_controller_pb2'})
_sym_db.RegisterMessage(Market)
UserNotificationResponse = _reflection.GeneratedProtocolMessageType('UserNotificationResponse', (_message.Message,), {'DESCRIPTOR': _USERNOTIFICATIONRESPONSE, '__module__': 'common.user_controller_pb2'})
_sym_db.RegisterMessage(UserNotificationResponse)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesB\x19UserControllerProtoCommonP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/common'
    _GETUSERREQUEST._serialized_start = 69
    _GETUSERREQUEST._serialized_end = 100
    _USERREQUEST._serialized_start = 102
    _USERREQUEST._serialized_end = 145
    _USERRESPONSE._serialized_start = 147
    _USERRESPONSE._serialized_end = 239
    _USER._serialized_start = 241
    _USER._serialized_end = 360
    _GETUSERPERMISSIONSREQUEST._serialized_start = 362
    _GETUSERPERMISSIONSREQUEST._serialized_end = 406
    _USERPERMISSIONSRESPONSE._serialized_start = 408
    _USERPERMISSIONSRESPONSE._serialized_end = 534
    _USERPERMISSIONS._serialized_start = 536
    _USERPERMISSIONS._serialized_end = 604
    _USERPERMISSION._serialized_start = 606
    _USERPERMISSION._serialized_end = 691
    _GETUSERNOTIFICATIONREQUEST._serialized_start = 693
    _GETUSERNOTIFICATIONREQUEST._serialized_end = 738
    _GETUSERNOTIFICATIONBYMARKETREQUEST._serialized_start = 740
    _GETUSERNOTIFICATIONBYMARKETREQUEST._serialized_end = 812
    _USERNOTIFICATIONSRESPONSE._serialized_start = 815
    _USERNOTIFICATIONSRESPONSE._serialized_end = 947
    _USERNOTIFICATIONREQUEST._serialized_start = 949
    _USERNOTIFICATIONREQUEST._serialized_end = 1029
    _USERNOTIFICATIONS._serialized_start = 1031
    _USERNOTIFICATIONS._serialized_end = 1105
    _USERNOTIFICATION._serialized_start = 1108
    _USERNOTIFICATION._serialized_end = 1264
    _ASSETM._serialized_start = 1266
    _ASSETM._serialized_end = 1326
    _MARKET._serialized_start = 1328
    _MARKET._serialized_end = 1392
    _USERNOTIFICATIONRESPONSE._serialized_start = 1395
    _USERNOTIFICATIONRESPONSE._serialized_end = 1524