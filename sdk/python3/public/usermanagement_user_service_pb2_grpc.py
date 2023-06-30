"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ..common import usermanagement_fe_specific_pb2 as common_dot_usermanagement__fe__specific__pb2
from ..common import usermanagement_user_pb2 as common_dot_usermanagement__user__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2

class UserServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.create = channel.unary_unary('/com.peernova.titanium.casbin.management.grpc.service.UserService/create', request_serializer=common_dot_usermanagement__user__pb2.UserDto.SerializeToString, response_deserializer=common_dot_usermanagement__fe__specific__pb2.ServiceResponse.FromString)
        self.update = channel.unary_unary('/com.peernova.titanium.casbin.management.grpc.service.UserService/update', request_serializer=common_dot_usermanagement__user__pb2.UserDto.SerializeToString, response_deserializer=common_dot_usermanagement__fe__specific__pb2.ServiceResponse.FromString)
        self.getById = channel.unary_unary('/com.peernova.titanium.casbin.management.grpc.service.UserService/getById', request_serializer=google_dot_protobuf_dot_wrappers__pb2.StringValue.SerializeToString, response_deserializer=common_dot_usermanagement__fe__specific__pb2.ServiceResponse.FromString)
        self.getAll = channel.unary_unary('/com.peernova.titanium.casbin.management.grpc.service.UserService/getAll', request_serializer=google_dot_protobuf_dot_wrappers__pb2.BoolValue.SerializeToString, response_deserializer=common_dot_usermanagement__fe__specific__pb2.ServiceResponse.FromString)

class UserServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getAll(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_UserServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'create': grpc.unary_unary_rpc_method_handler(servicer.create, request_deserializer=common_dot_usermanagement__user__pb2.UserDto.FromString, response_serializer=common_dot_usermanagement__fe__specific__pb2.ServiceResponse.SerializeToString), 'update': grpc.unary_unary_rpc_method_handler(servicer.update, request_deserializer=common_dot_usermanagement__user__pb2.UserDto.FromString, response_serializer=common_dot_usermanagement__fe__specific__pb2.ServiceResponse.SerializeToString), 'getById': grpc.unary_unary_rpc_method_handler(servicer.getById, request_deserializer=google_dot_protobuf_dot_wrappers__pb2.StringValue.FromString, response_serializer=common_dot_usermanagement__fe__specific__pb2.ServiceResponse.SerializeToString), 'getAll': grpc.unary_unary_rpc_method_handler(servicer.getAll, request_deserializer=google_dot_protobuf_dot_wrappers__pb2.BoolValue.FromString, response_serializer=common_dot_usermanagement__fe__specific__pb2.ServiceResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('com.peernova.titanium.casbin.management.grpc.service.UserService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class UserService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def create(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.peernova.titanium.casbin.management.grpc.service.UserService/create', common_dot_usermanagement__user__pb2.UserDto.SerializeToString, common_dot_usermanagement__fe__specific__pb2.ServiceResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def update(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.peernova.titanium.casbin.management.grpc.service.UserService/update', common_dot_usermanagement__user__pb2.UserDto.SerializeToString, common_dot_usermanagement__fe__specific__pb2.ServiceResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getById(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.peernova.titanium.casbin.management.grpc.service.UserService/getById', google_dot_protobuf_dot_wrappers__pb2.StringValue.SerializeToString, common_dot_usermanagement__fe__specific__pb2.ServiceResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getAll(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.peernova.titanium.casbin.management.grpc.service.UserService/getAll', google_dot_protobuf_dot_wrappers__pb2.BoolValue.SerializeToString, common_dot_usermanagement__fe__specific__pb2.ServiceResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)