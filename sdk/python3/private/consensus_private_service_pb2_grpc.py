"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2
from ..public import consensus_service_pb2 as public_dot_consensus__service__pb2

class ConsensusServicePrivateStub(object):
    """todo remove /operator from URL paths

    ConsensusServicePrivate is service whit private methods that can be used to operate with consensus entity.

    Consensus price is either the valuation price of an instrument provided by combining the submissions for an
    instrument. For a consensus to be reached for a tenor 3 points of data are requirement at minimum.
    It can be the average price, average volatility or other agreed upon methods for a particular instrument.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ConsensusActive = channel.unary_unary('/titanium.ConsensusServicePrivate/ConsensusActive', request_serializer=public_dot_consensus__service__pb2.ConsensusActiveRequest.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.ConsensusActiveResponse.FromString)
        self.ConsensusToPublish = channel.unary_unary('/titanium.ConsensusServicePrivate/ConsensusToPublish', request_serializer=public_dot_consensus__service__pb2.ConsensusToPublishRequest.SerializeToString, response_deserializer=public_dot_consensus__service__pb2.ConsensusToPublishResponse.FromString)
        self.ConsensusPublish = channel.unary_unary('/titanium.ConsensusServicePrivate/ConsensusPublish', request_serializer=public_dot_consensus__service__pb2.ConsensusPublishRequest.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.MessageResponse.FromString)
        self.ConsensusHistory = channel.unary_unary('/titanium.ConsensusServicePrivate/ConsensusHistory', request_serializer=public_dot_consensus__service__pb2.ConsensusHistoryRequest.SerializeToString, response_deserializer=public_dot_consensus__service__pb2.ConsensusHistoryResponse.FromString)
        self.ConsensusDecision = channel.unary_unary('/titanium.ConsensusServicePrivate/ConsensusDecision', request_serializer=public_dot_consensus__service__pb2.ConsensusDecisionRequest.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.MessageResponse.FromString)

class ConsensusServicePrivateServicer(object):
    """todo remove /operator from URL paths

    ConsensusServicePrivate is service whit private methods that can be used to operate with consensus entity.

    Consensus price is either the valuation price of an instrument provided by combining the submissions for an
    instrument. For a consensus to be reached for a tenor 3 points of data are requirement at minimum.
    It can be the average price, average volatility or other agreed upon methods for a particular instrument.
    """

    def ConsensusActive(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConsensusToPublish(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConsensusPublish(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConsensusHistory(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConsensusDecision(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_ConsensusServicePrivateServicer_to_server(servicer, server):
    rpc_method_handlers = {'ConsensusActive': grpc.unary_unary_rpc_method_handler(servicer.ConsensusActive, request_deserializer=public_dot_consensus__service__pb2.ConsensusActiveRequest.FromString, response_serializer=common_dot_gateway__base__pb2.ConsensusActiveResponse.SerializeToString), 'ConsensusToPublish': grpc.unary_unary_rpc_method_handler(servicer.ConsensusToPublish, request_deserializer=public_dot_consensus__service__pb2.ConsensusToPublishRequest.FromString, response_serializer=public_dot_consensus__service__pb2.ConsensusToPublishResponse.SerializeToString), 'ConsensusPublish': grpc.unary_unary_rpc_method_handler(servicer.ConsensusPublish, request_deserializer=public_dot_consensus__service__pb2.ConsensusPublishRequest.FromString, response_serializer=common_dot_gateway__base__pb2.MessageResponse.SerializeToString), 'ConsensusHistory': grpc.unary_unary_rpc_method_handler(servicer.ConsensusHistory, request_deserializer=public_dot_consensus__service__pb2.ConsensusHistoryRequest.FromString, response_serializer=public_dot_consensus__service__pb2.ConsensusHistoryResponse.SerializeToString), 'ConsensusDecision': grpc.unary_unary_rpc_method_handler(servicer.ConsensusDecision, request_deserializer=public_dot_consensus__service__pb2.ConsensusDecisionRequest.FromString, response_serializer=common_dot_gateway__base__pb2.MessageResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('titanium.ConsensusServicePrivate', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class ConsensusServicePrivate(object):
    """todo remove /operator from URL paths

    ConsensusServicePrivate is service whit private methods that can be used to operate with consensus entity.

    Consensus price is either the valuation price of an instrument provided by combining the submissions for an
    instrument. For a consensus to be reached for a tenor 3 points of data are requirement at minimum.
    It can be the average price, average volatility or other agreed upon methods for a particular instrument.
    """

    @staticmethod
    def ConsensusActive(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.ConsensusServicePrivate/ConsensusActive', public_dot_consensus__service__pb2.ConsensusActiveRequest.SerializeToString, common_dot_gateway__base__pb2.ConsensusActiveResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConsensusToPublish(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.ConsensusServicePrivate/ConsensusToPublish', public_dot_consensus__service__pb2.ConsensusToPublishRequest.SerializeToString, public_dot_consensus__service__pb2.ConsensusToPublishResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConsensusPublish(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.ConsensusServicePrivate/ConsensusPublish', public_dot_consensus__service__pb2.ConsensusPublishRequest.SerializeToString, common_dot_gateway__base__pb2.MessageResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConsensusHistory(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.ConsensusServicePrivate/ConsensusHistory', public_dot_consensus__service__pb2.ConsensusHistoryRequest.SerializeToString, public_dot_consensus__service__pb2.ConsensusHistoryResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConsensusDecision(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.ConsensusServicePrivate/ConsensusDecision', public_dot_consensus__service__pb2.ConsensusDecisionRequest.SerializeToString, common_dot_gateway__base__pb2.MessageResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)