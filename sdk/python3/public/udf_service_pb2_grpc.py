"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2
from ..common import udf_pb2 as common_dot_udf__pb2

class UdfServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListUdfs = channel.unary_unary('/titanium.UdfService/ListUdfs', request_serializer=common_dot_gateway__base__pb2.ListRequest.SerializeToString, response_deserializer=common_dot_udf__pb2.ListUdfResponse.FromString)
        self.GetUdfDefinition = channel.unary_unary('/titanium.UdfService/GetUdfDefinition', request_serializer=common_dot_udf__pb2.UdfNameRequest.SerializeToString, response_deserializer=common_dot_udf__pb2.GetUdfResponse.FromString)
        self.DisableUdf = channel.unary_unary('/titanium.UdfService/DisableUdf', request_serializer=common_dot_udf__pb2.UdfNameRequest.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.MessageResponse.FromString)

class UdfServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ListUdfs(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUdfDefinition(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DisableUdf(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_UdfServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'ListUdfs': grpc.unary_unary_rpc_method_handler(servicer.ListUdfs, request_deserializer=common_dot_gateway__base__pb2.ListRequest.FromString, response_serializer=common_dot_udf__pb2.ListUdfResponse.SerializeToString), 'GetUdfDefinition': grpc.unary_unary_rpc_method_handler(servicer.GetUdfDefinition, request_deserializer=common_dot_udf__pb2.UdfNameRequest.FromString, response_serializer=common_dot_udf__pb2.GetUdfResponse.SerializeToString), 'DisableUdf': grpc.unary_unary_rpc_method_handler(servicer.DisableUdf, request_deserializer=common_dot_udf__pb2.UdfNameRequest.FromString, response_serializer=common_dot_gateway__base__pb2.MessageResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('titanium.UdfService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class UdfService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ListUdfs(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.UdfService/ListUdfs', common_dot_gateway__base__pb2.ListRequest.SerializeToString, common_dot_udf__pb2.ListUdfResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUdfDefinition(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.UdfService/GetUdfDefinition', common_dot_udf__pb2.UdfNameRequest.SerializeToString, common_dot_udf__pb2.GetUdfResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DisableUdf(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.UdfService/DisableUdf', common_dot_udf__pb2.UdfNameRequest.SerializeToString, common_dot_gateway__base__pb2.MessageResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)