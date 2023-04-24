"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2

class MetadataEntityServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddEntity = channel.unary_unary('/titanium.MetadataEntityService/AddEntity', request_serializer=common_dot_gateway__base__pb2.EntityDefinition.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.AcknowledgeResponse.FromString)
        self.GetEntity = channel.unary_unary('/titanium.MetadataEntityService/GetEntity', request_serializer=common_dot_gateway__base__pb2.EntityIdentifier.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.EntityDefinition.FromString)
        self.EnableEntity = channel.unary_unary('/titanium.MetadataEntityService/EnableEntity', request_serializer=common_dot_gateway__base__pb2.EntityIdentifier.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.AcknowledgeResponse.FromString)
        self.DisableEntity = channel.unary_unary('/titanium.MetadataEntityService/DisableEntity', request_serializer=common_dot_gateway__base__pb2.EntityIdentifier.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.AcknowledgeResponse.FromString)

class MetadataEntityServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AddEntity(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetEntity(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EnableEntity(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DisableEntity(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_MetadataEntityServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'AddEntity': grpc.unary_unary_rpc_method_handler(servicer.AddEntity, request_deserializer=common_dot_gateway__base__pb2.EntityDefinition.FromString, response_serializer=common_dot_gateway__base__pb2.AcknowledgeResponse.SerializeToString), 'GetEntity': grpc.unary_unary_rpc_method_handler(servicer.GetEntity, request_deserializer=common_dot_gateway__base__pb2.EntityIdentifier.FromString, response_serializer=common_dot_gateway__base__pb2.EntityDefinition.SerializeToString), 'EnableEntity': grpc.unary_unary_rpc_method_handler(servicer.EnableEntity, request_deserializer=common_dot_gateway__base__pb2.EntityIdentifier.FromString, response_serializer=common_dot_gateway__base__pb2.AcknowledgeResponse.SerializeToString), 'DisableEntity': grpc.unary_unary_rpc_method_handler(servicer.DisableEntity, request_deserializer=common_dot_gateway__base__pb2.EntityIdentifier.FromString, response_serializer=common_dot_gateway__base__pb2.AcknowledgeResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('titanium.MetadataEntityService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class MetadataEntityService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AddEntity(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.MetadataEntityService/AddEntity', common_dot_gateway__base__pb2.EntityDefinition.SerializeToString, common_dot_gateway__base__pb2.AcknowledgeResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetEntity(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.MetadataEntityService/GetEntity', common_dot_gateway__base__pb2.EntityIdentifier.SerializeToString, common_dot_gateway__base__pb2.EntityDefinition.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EnableEntity(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.MetadataEntityService/EnableEntity', common_dot_gateway__base__pb2.EntityIdentifier.SerializeToString, common_dot_gateway__base__pb2.AcknowledgeResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DisableEntity(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.MetadataEntityService/DisableEntity', common_dot_gateway__base__pb2.EntityIdentifier.SerializeToString, common_dot_gateway__base__pb2.AcknowledgeResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)