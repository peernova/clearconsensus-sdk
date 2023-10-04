"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from . import auth_service_pb2 as auth__service__pb2

class AuthServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Check = channel.unary_unary('/com.peernova.titanium.security.AuthService/Check', request_serializer=auth__service__pb2.AuthRequest.SerializeToString, response_deserializer=auth__service__pb2.AuthResponse.FromString)

class AuthServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Check(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_AuthServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'Check': grpc.unary_unary_rpc_method_handler(servicer.Check, request_deserializer=auth__service__pb2.AuthRequest.FromString, response_serializer=auth__service__pb2.AuthResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('com.peernova.titanium.security.AuthService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class AuthService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Check(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.peernova.titanium.security.AuthService/Check', auth__service__pb2.AuthRequest.SerializeToString, auth__service__pb2.AuthResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)