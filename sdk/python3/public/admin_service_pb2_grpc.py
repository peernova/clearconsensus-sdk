"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2
from ..public import admin_service_pb2 as public_dot_admin__service__pb2

class AdminServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.OnBoard = channel.unary_unary('/titanium.AdminService/OnBoard', request_serializer=public_dot_admin__service__pb2.OnBoardRequest.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.MessageResponse.FromString)
        self.RunCalculator = channel.unary_unary('/titanium.AdminService/RunCalculator', request_serializer=public_dot_admin__service__pb2.RunCalculatorRequest.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.MessageResponse.FromString)
        self.UploadEvaluatedPrice = channel.unary_unary('/titanium.AdminService/UploadEvaluatedPrice', request_serializer=public_dot_admin__service__pb2.UploadEvaluatedPriceRequest.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.MessageResponse.FromString)
        self.RunConsensus = channel.unary_unary('/titanium.AdminService/RunConsensus', request_serializer=public_dot_admin__service__pb2.RunConsensusRequest.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.MessageResponse.FromString)

class AdminServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def OnBoard(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RunCalculator(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UploadEvaluatedPrice(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RunConsensus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_AdminServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'OnBoard': grpc.unary_unary_rpc_method_handler(servicer.OnBoard, request_deserializer=public_dot_admin__service__pb2.OnBoardRequest.FromString, response_serializer=common_dot_gateway__base__pb2.MessageResponse.SerializeToString), 'RunCalculator': grpc.unary_unary_rpc_method_handler(servicer.RunCalculator, request_deserializer=public_dot_admin__service__pb2.RunCalculatorRequest.FromString, response_serializer=common_dot_gateway__base__pb2.MessageResponse.SerializeToString), 'UploadEvaluatedPrice': grpc.unary_unary_rpc_method_handler(servicer.UploadEvaluatedPrice, request_deserializer=public_dot_admin__service__pb2.UploadEvaluatedPriceRequest.FromString, response_serializer=common_dot_gateway__base__pb2.MessageResponse.SerializeToString), 'RunConsensus': grpc.unary_unary_rpc_method_handler(servicer.RunConsensus, request_deserializer=public_dot_admin__service__pb2.RunConsensusRequest.FromString, response_serializer=common_dot_gateway__base__pb2.MessageResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('titanium.AdminService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class AdminService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def OnBoard(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.AdminService/OnBoard', public_dot_admin__service__pb2.OnBoardRequest.SerializeToString, common_dot_gateway__base__pb2.MessageResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RunCalculator(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.AdminService/RunCalculator', public_dot_admin__service__pb2.RunCalculatorRequest.SerializeToString, common_dot_gateway__base__pb2.MessageResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UploadEvaluatedPrice(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.AdminService/UploadEvaluatedPrice', public_dot_admin__service__pb2.UploadEvaluatedPriceRequest.SerializeToString, common_dot_gateway__base__pb2.MessageResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RunConsensus(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.AdminService/RunConsensus', public_dot_admin__service__pb2.RunConsensusRequest.SerializeToString, common_dot_gateway__base__pb2.MessageResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)