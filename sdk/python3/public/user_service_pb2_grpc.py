"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ..common import user_controller_pb2 as common_dot_user__controller__pb2

class UserServiceStub(object):
    """UserController is util service that helps to operate with user entity(permissions, notification and etc.).
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetUser = channel.unary_unary('/titanium.UserService/GetUser', request_serializer=common_dot_user__controller__pb2.GetUserRequest.SerializeToString, response_deserializer=common_dot_user__controller__pb2.UserResponse.FromString)
        self.GetUserPermissions = channel.unary_unary('/titanium.UserService/GetUserPermissions', request_serializer=common_dot_user__controller__pb2.GetUserPermissionsRequest.SerializeToString, response_deserializer=common_dot_user__controller__pb2.UserPermissionsResponse.FromString)
        self.GetUserNotifications = channel.unary_unary('/titanium.UserService/GetUserNotifications', request_serializer=common_dot_user__controller__pb2.GetUserNotificationRequest.SerializeToString, response_deserializer=common_dot_user__controller__pb2.UserNotificationsResponse.FromString)
        self.GetUserNotificationsByMarket = channel.unary_unary('/titanium.UserService/GetUserNotificationsByMarket', request_serializer=common_dot_user__controller__pb2.GetUserNotificationByMarketRequest.SerializeToString, response_deserializer=common_dot_user__controller__pb2.UserNotificationsResponse.FromString)
        self.UpdateUserNotification = channel.unary_unary('/titanium.UserService/UpdateUserNotification', request_serializer=common_dot_user__controller__pb2.UserNotificationRequest.SerializeToString, response_deserializer=common_dot_user__controller__pb2.UserNotificationResponse.FromString)
        self.AddUserNotification = channel.unary_unary('/titanium.UserService/AddUserNotification', request_serializer=common_dot_user__controller__pb2.UserNotificationRequest.SerializeToString, response_deserializer=common_dot_user__controller__pb2.UserNotificationResponse.FromString)
        self.DeleteUserNotification = channel.unary_unary('/titanium.UserService/DeleteUserNotification', request_serializer=common_dot_user__controller__pb2.UserNotificationRequest.SerializeToString, response_deserializer=common_dot_user__controller__pb2.UserNotificationResponse.FromString)

class UserServiceServicer(object):
    """UserController is util service that helps to operate with user entity(permissions, notification and etc.).
    """

    def GetUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUserPermissions(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUserNotifications(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUserNotificationsByMarket(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateUserNotification(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddUserNotification(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteUserNotification(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_UserServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'GetUser': grpc.unary_unary_rpc_method_handler(servicer.GetUser, request_deserializer=common_dot_user__controller__pb2.GetUserRequest.FromString, response_serializer=common_dot_user__controller__pb2.UserResponse.SerializeToString), 'GetUserPermissions': grpc.unary_unary_rpc_method_handler(servicer.GetUserPermissions, request_deserializer=common_dot_user__controller__pb2.GetUserPermissionsRequest.FromString, response_serializer=common_dot_user__controller__pb2.UserPermissionsResponse.SerializeToString), 'GetUserNotifications': grpc.unary_unary_rpc_method_handler(servicer.GetUserNotifications, request_deserializer=common_dot_user__controller__pb2.GetUserNotificationRequest.FromString, response_serializer=common_dot_user__controller__pb2.UserNotificationsResponse.SerializeToString), 'GetUserNotificationsByMarket': grpc.unary_unary_rpc_method_handler(servicer.GetUserNotificationsByMarket, request_deserializer=common_dot_user__controller__pb2.GetUserNotificationByMarketRequest.FromString, response_serializer=common_dot_user__controller__pb2.UserNotificationsResponse.SerializeToString), 'UpdateUserNotification': grpc.unary_unary_rpc_method_handler(servicer.UpdateUserNotification, request_deserializer=common_dot_user__controller__pb2.UserNotificationRequest.FromString, response_serializer=common_dot_user__controller__pb2.UserNotificationResponse.SerializeToString), 'AddUserNotification': grpc.unary_unary_rpc_method_handler(servicer.AddUserNotification, request_deserializer=common_dot_user__controller__pb2.UserNotificationRequest.FromString, response_serializer=common_dot_user__controller__pb2.UserNotificationResponse.SerializeToString), 'DeleteUserNotification': grpc.unary_unary_rpc_method_handler(servicer.DeleteUserNotification, request_deserializer=common_dot_user__controller__pb2.UserNotificationRequest.FromString, response_serializer=common_dot_user__controller__pb2.UserNotificationResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('titanium.UserService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class UserService(object):
    """UserController is util service that helps to operate with user entity(permissions, notification and etc.).
    """

    @staticmethod
    def GetUser(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.UserService/GetUser', common_dot_user__controller__pb2.GetUserRequest.SerializeToString, common_dot_user__controller__pb2.UserResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUserPermissions(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.UserService/GetUserPermissions', common_dot_user__controller__pb2.GetUserPermissionsRequest.SerializeToString, common_dot_user__controller__pb2.UserPermissionsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUserNotifications(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.UserService/GetUserNotifications', common_dot_user__controller__pb2.GetUserNotificationRequest.SerializeToString, common_dot_user__controller__pb2.UserNotificationsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUserNotificationsByMarket(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.UserService/GetUserNotificationsByMarket', common_dot_user__controller__pb2.GetUserNotificationByMarketRequest.SerializeToString, common_dot_user__controller__pb2.UserNotificationsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateUserNotification(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.UserService/UpdateUserNotification', common_dot_user__controller__pb2.UserNotificationRequest.SerializeToString, common_dot_user__controller__pb2.UserNotificationResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddUserNotification(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.UserService/AddUserNotification', common_dot_user__controller__pb2.UserNotificationRequest.SerializeToString, common_dot_user__controller__pb2.UserNotificationResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteUserNotification(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.UserService/DeleteUserNotification', common_dot_user__controller__pb2.UserNotificationRequest.SerializeToString, common_dot_user__controller__pb2.UserNotificationResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)