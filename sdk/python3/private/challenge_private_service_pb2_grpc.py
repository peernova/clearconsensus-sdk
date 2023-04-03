"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ..common import challenge_pb2 as common_dot_challenge__pb2
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2

class ChallengePrivateServiceStub(object):
    """todo remove /operator from URL paths

    ChallengeServicePrivate is used to operate with challenge process.

    Challenge process is :
    After a Consensus has been published, the challenge process allows a dealer to “challenge”
    one of their own submitted data points that has been declared an outlier in the published Consensus.
    The dealer initiate a challenge and provide evidence to support their claim that the data point should be included in the Consensus.

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ChallengeActive = channel.unary_unary('/titanium.ChallengePrivateService/ChallengeActive', request_serializer=common_dot_challenge__pb2.ChallengeActiveRequest.SerializeToString, response_deserializer=common_dot_challenge__pb2.ChallengeActiveResponse.FromString)
        self.ChallengeList = channel.unary_unary('/titanium.ChallengePrivateService/ChallengeList', request_serializer=common_dot_challenge__pb2.ChallengeListRequest.SerializeToString, response_deserializer=common_dot_challenge__pb2.ChallengeListResponse.FromString)
        self.ChallengeHistory = channel.unary_unary('/titanium.ChallengePrivateService/ChallengeHistory', request_serializer=common_dot_challenge__pb2.ChallengeHistoryRequest.SerializeToString, response_deserializer=common_dot_challenge__pb2.ChallengeHistoryResponse.FromString)
        self.ChallengeDecision = channel.unary_unary('/titanium.ChallengePrivateService/ChallengeDecision', request_serializer=common_dot_challenge__pb2.ChallengeDecisionRequest.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.MessageResponse.FromString)
        self.ChallengeFreezeAction = channel.unary_unary('/titanium.ChallengePrivateService/ChallengeFreezeAction', request_serializer=common_dot_challenge__pb2.ChallengeFreezeActionRequest.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.MessageResponse.FromString)

class ChallengePrivateServiceServicer(object):
    """todo remove /operator from URL paths

    ChallengeServicePrivate is used to operate with challenge process.

    Challenge process is :
    After a Consensus has been published, the challenge process allows a dealer to “challenge”
    one of their own submitted data points that has been declared an outlier in the published Consensus.
    The dealer initiate a challenge and provide evidence to support their claim that the data point should be included in the Consensus.

    """

    def ChallengeActive(self, request, context):
        """ChallengeActive returns active challenges(according to request) in active status(challenge process is active).
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ChallengeList(self, request, context):
        """ChallengeList returns list of challenges according to request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ChallengeHistory(self, request, context):
        """ChallengeHistory return already closed challenges according to request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ChallengeDecision(self, request, context):
        """ChallengeDecision sets decision of the challenge according to request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ChallengeFreezeAction(self, request, context):
        """ChallengeFreezeAction makes challenge process stopped or not according to request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_ChallengePrivateServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'ChallengeActive': grpc.unary_unary_rpc_method_handler(servicer.ChallengeActive, request_deserializer=common_dot_challenge__pb2.ChallengeActiveRequest.FromString, response_serializer=common_dot_challenge__pb2.ChallengeActiveResponse.SerializeToString), 'ChallengeList': grpc.unary_unary_rpc_method_handler(servicer.ChallengeList, request_deserializer=common_dot_challenge__pb2.ChallengeListRequest.FromString, response_serializer=common_dot_challenge__pb2.ChallengeListResponse.SerializeToString), 'ChallengeHistory': grpc.unary_unary_rpc_method_handler(servicer.ChallengeHistory, request_deserializer=common_dot_challenge__pb2.ChallengeHistoryRequest.FromString, response_serializer=common_dot_challenge__pb2.ChallengeHistoryResponse.SerializeToString), 'ChallengeDecision': grpc.unary_unary_rpc_method_handler(servicer.ChallengeDecision, request_deserializer=common_dot_challenge__pb2.ChallengeDecisionRequest.FromString, response_serializer=common_dot_gateway__base__pb2.MessageResponse.SerializeToString), 'ChallengeFreezeAction': grpc.unary_unary_rpc_method_handler(servicer.ChallengeFreezeAction, request_deserializer=common_dot_challenge__pb2.ChallengeFreezeActionRequest.FromString, response_serializer=common_dot_gateway__base__pb2.MessageResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('titanium.ChallengePrivateService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class ChallengePrivateService(object):
    """todo remove /operator from URL paths

    ChallengeServicePrivate is used to operate with challenge process.

    Challenge process is :
    After a Consensus has been published, the challenge process allows a dealer to “challenge”
    one of their own submitted data points that has been declared an outlier in the published Consensus.
    The dealer initiate a challenge and provide evidence to support their claim that the data point should be included in the Consensus.

    """

    @staticmethod
    def ChallengeActive(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.ChallengePrivateService/ChallengeActive', common_dot_challenge__pb2.ChallengeActiveRequest.SerializeToString, common_dot_challenge__pb2.ChallengeActiveResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ChallengeList(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.ChallengePrivateService/ChallengeList', common_dot_challenge__pb2.ChallengeListRequest.SerializeToString, common_dot_challenge__pb2.ChallengeListResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ChallengeHistory(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.ChallengePrivateService/ChallengeHistory', common_dot_challenge__pb2.ChallengeHistoryRequest.SerializeToString, common_dot_challenge__pb2.ChallengeHistoryResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ChallengeDecision(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.ChallengePrivateService/ChallengeDecision', common_dot_challenge__pb2.ChallengeDecisionRequest.SerializeToString, common_dot_gateway__base__pb2.MessageResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ChallengeFreezeAction(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.ChallengePrivateService/ChallengeFreezeAction', common_dot_challenge__pb2.ChallengeFreezeActionRequest.SerializeToString, common_dot_gateway__base__pb2.MessageResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)