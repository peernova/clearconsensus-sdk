"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from ..private import operator_service_pb2 as private_dot_operator__service__pb2

class OperatorServicePrivateStub(object):
    """OperatorServicePrivate is service with private methods that can be used only by operator.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddClient = channel.unary_unary('/titanium.OperatorServicePrivate/AddClient', request_serializer=private_dot_operator__service__pb2.ClientName.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.MessageResponse.FromString)
        self.ListClients = channel.unary_unary('/titanium.OperatorServicePrivate/ListClients', request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString, response_deserializer=private_dot_operator__service__pb2.ListClientsResponse.FromString)
        self.EvpStatuses = channel.unary_unary('/titanium.OperatorServicePrivate/EvpStatuses', request_serializer=private_dot_operator__service__pb2.EvpStatusesRequest.SerializeToString, response_deserializer=private_dot_operator__service__pb2.EvpStatusesResponse.FromString)
        self.UploadEVP = channel.unary_unary('/titanium.OperatorServicePrivate/UploadEVP', request_serializer=private_dot_operator__service__pb2.UploadEVPRequest.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.UploadURLResponse.FromString)

class OperatorServicePrivateServicer(object):
    """OperatorServicePrivate is service with private methods that can be used only by operator.
    """

    def AddClient(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListClients(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EvpStatuses(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UploadEVP(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_OperatorServicePrivateServicer_to_server(servicer, server):
    rpc_method_handlers = {'AddClient': grpc.unary_unary_rpc_method_handler(servicer.AddClient, request_deserializer=private_dot_operator__service__pb2.ClientName.FromString, response_serializer=common_dot_gateway__base__pb2.MessageResponse.SerializeToString), 'ListClients': grpc.unary_unary_rpc_method_handler(servicer.ListClients, request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString, response_serializer=private_dot_operator__service__pb2.ListClientsResponse.SerializeToString), 'EvpStatuses': grpc.unary_unary_rpc_method_handler(servicer.EvpStatuses, request_deserializer=private_dot_operator__service__pb2.EvpStatusesRequest.FromString, response_serializer=private_dot_operator__service__pb2.EvpStatusesResponse.SerializeToString), 'UploadEVP': grpc.unary_unary_rpc_method_handler(servicer.UploadEVP, request_deserializer=private_dot_operator__service__pb2.UploadEVPRequest.FromString, response_serializer=common_dot_gateway__base__pb2.UploadURLResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('titanium.OperatorServicePrivate', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class OperatorServicePrivate(object):
    """OperatorServicePrivate is service with private methods that can be used only by operator.
    """

    @staticmethod
    def AddClient(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.OperatorServicePrivate/AddClient', private_dot_operator__service__pb2.ClientName.SerializeToString, common_dot_gateway__base__pb2.MessageResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListClients(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.OperatorServicePrivate/ListClients', google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString, private_dot_operator__service__pb2.ListClientsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EvpStatuses(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.OperatorServicePrivate/EvpStatuses', private_dot_operator__service__pb2.EvpStatusesRequest.SerializeToString, private_dot_operator__service__pb2.EvpStatusesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UploadEVP(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.OperatorServicePrivate/UploadEVP', private_dot_operator__service__pb2.UploadEVPRequest.SerializeToString, common_dot_gateway__base__pb2.UploadURLResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)