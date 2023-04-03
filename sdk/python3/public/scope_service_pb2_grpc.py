"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2
from ..common import scope_pb2 as common_dot_scope__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2

class ScopeServiceStub(object):
    """ScopeService is service that can be used to operate with scopes.

    Scope defines visibility or application area of function, rules and etc.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddScope = channel.unary_unary('/titanium.ScopeService/AddScope', request_serializer=common_dot_scope__pb2.ScopeIdentifier.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.AcknowledgeResponse.FromString)
        self.ExistScope = channel.unary_unary('/titanium.ScopeService/ExistScope', request_serializer=common_dot_scope__pb2.ScopeIdentifier.SerializeToString, response_deserializer=common_dot_scope__pb2.ScopeExistResponse.FromString)
        self.ListScope = channel.unary_unary('/titanium.ScopeService/ListScope', request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString, response_deserializer=common_dot_scope__pb2.ScopeListResponse.FromString)

class ScopeServiceServicer(object):
    """ScopeService is service that can be used to operate with scopes.

    Scope defines visibility or application area of function, rules and etc.
    """

    def AddScope(self, request, context):
        """AddScope creates scope in the system.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExistScope(self, request, context):
        """ExistScope return boolean value about existence of scope according to request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListScope(self, request, context):
        """ListScope returns list of all existing scopes.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_ScopeServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'AddScope': grpc.unary_unary_rpc_method_handler(servicer.AddScope, request_deserializer=common_dot_scope__pb2.ScopeIdentifier.FromString, response_serializer=common_dot_gateway__base__pb2.AcknowledgeResponse.SerializeToString), 'ExistScope': grpc.unary_unary_rpc_method_handler(servicer.ExistScope, request_deserializer=common_dot_scope__pb2.ScopeIdentifier.FromString, response_serializer=common_dot_scope__pb2.ScopeExistResponse.SerializeToString), 'ListScope': grpc.unary_unary_rpc_method_handler(servicer.ListScope, request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString, response_serializer=common_dot_scope__pb2.ScopeListResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('titanium.ScopeService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class ScopeService(object):
    """ScopeService is service that can be used to operate with scopes.

    Scope defines visibility or application area of function, rules and etc.
    """

    @staticmethod
    def AddScope(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.ScopeService/AddScope', common_dot_scope__pb2.ScopeIdentifier.SerializeToString, common_dot_gateway__base__pb2.AcknowledgeResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ExistScope(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.ScopeService/ExistScope', common_dot_scope__pb2.ScopeIdentifier.SerializeToString, common_dot_scope__pb2.ScopeExistResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListScope(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.ScopeService/ListScope', google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString, common_dot_scope__pb2.ScopeListResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)