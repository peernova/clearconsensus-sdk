"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ..common import user_controller_pb2 as common_dot_user__controller__pb2

class UserPrivateServiceStub(object):
    """UserPrivateService is util service with private methods that help to operate with user entity(permissions, notification and etc.).
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddUser = channel.unary_unary('/titanium.UserPrivateService/AddUser', request_serializer=common_dot_user__controller__pb2.UserRequest.SerializeToString, response_deserializer=common_dot_user__controller__pb2.UserResponse.FromString)
        self.UpdateUser = channel.unary_unary('/titanium.UserPrivateService/UpdateUser', request_serializer=common_dot_user__controller__pb2.UserRequest.SerializeToString, response_deserializer=common_dot_user__controller__pb2.UserResponse.FromString)
        self.DeleteUser = channel.unary_unary('/titanium.UserPrivateService/DeleteUser', request_serializer=common_dot_user__controller__pb2.UserRequest.SerializeToString, response_deserializer=common_dot_user__controller__pb2.UserResponse.FromString)

class UserPrivateServiceServicer(object):
    """UserPrivateService is util service with private methods that help to operate with user entity(permissions, notification and etc.).
    """

    def AddUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_UserPrivateServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'AddUser': grpc.unary_unary_rpc_method_handler(servicer.AddUser, request_deserializer=common_dot_user__controller__pb2.UserRequest.FromString, response_serializer=common_dot_user__controller__pb2.UserResponse.SerializeToString), 'UpdateUser': grpc.unary_unary_rpc_method_handler(servicer.UpdateUser, request_deserializer=common_dot_user__controller__pb2.UserRequest.FromString, response_serializer=common_dot_user__controller__pb2.UserResponse.SerializeToString), 'DeleteUser': grpc.unary_unary_rpc_method_handler(servicer.DeleteUser, request_deserializer=common_dot_user__controller__pb2.UserRequest.FromString, response_serializer=common_dot_user__controller__pb2.UserResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('titanium.UserPrivateService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class UserPrivateService(object):
    """UserPrivateService is util service with private methods that help to operate with user entity(permissions, notification and etc.).
    """

    @staticmethod
    def AddUser(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.UserPrivateService/AddUser', common_dot_user__controller__pb2.UserRequest.SerializeToString, common_dot_user__controller__pb2.UserResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateUser(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.UserPrivateService/UpdateUser', common_dot_user__controller__pb2.UserRequest.SerializeToString, common_dot_user__controller__pb2.UserResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteUser(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.UserPrivateService/DeleteUser', common_dot_user__controller__pb2.UserRequest.SerializeToString, common_dot_user__controller__pb2.UserResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)