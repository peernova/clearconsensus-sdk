"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ..common import challenge_pb2 as common_dot_challenge__pb2
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2

class ChallengeServiceStub(object):
    """
    ChallengeService is used to operate with challenge process.

    Challenge process is :
    1.A Consensus has been published, the challenge process allows a dealer to “challenge”.
    ("Challenge can be created only for  one of dealer own submitted data points that has benn declared an outlier in the published Consensus.")

    2."Challenger"(dealer) creates challenge with the evidence to support their claim(Using ChallengeCreate method and ChallengeCreateRequest that has evidence)
    "Challenger" can attach any file for additional information about the disputable outlier.(Using pre-signed S3 URL that can be fetched with method GetChallengeAttachmentUploadUrl)
    Note: Challenger gets template with pre-filled data(Using ChallengeFormMeta)  to fill out it in his own way.

    3.The operator considers the evidence and allows it if there is a valid transaction ID filled in.

    4.The operator set decision on the Challenge (Accept or deny)
    Note : Challenge points need to have been accepted as valid by Operator 1 and approved for inclusion in the revised Consensus run by Operator 2 (not the same operator)

    5.After all the challenge points have been reviewed and marked, the "Review Complete" flag is set. A second operator (not the same person who marked the challenge points)
    can now accept all challenges and prepare for the consensus to be run again.

    Note : Operator can also freeze challenge.(Stop process of challenging). Dealer can see current freeze status of the Challenge.(Using ChallengeFreezeStatus method)
    Dealer and Operator can also just view information about the Challenge (Using GetChallenge method)

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ChallengeFormMeta = channel.unary_unary('/titanium.ChallengeService/ChallengeFormMeta', request_serializer=common_dot_challenge__pb2.ChallengeFormMetaRequest.SerializeToString, response_deserializer=common_dot_challenge__pb2.ChallengeFormMetaResponse.FromString)
        self.ChallengeCreate = channel.unary_unary('/titanium.ChallengeService/ChallengeCreate', request_serializer=common_dot_challenge__pb2.ChallengeCreateRequest.SerializeToString, response_deserializer=common_dot_challenge__pb2.ChallengeCreateResponse.FromString)
        self.ChallengeFreezeStatus = channel.unary_unary('/titanium.ChallengeService/ChallengeFreezeStatus', request_serializer=common_dot_challenge__pb2.ChallengeFreezeStatusRequest.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.StatusResponse.FromString)
        self.GetChallengeDetails = channel.unary_unary('/titanium.ChallengeService/GetChallengeDetails', request_serializer=common_dot_challenge__pb2.GetChallengeDetailsRequest.SerializeToString, response_deserializer=common_dot_challenge__pb2.GetChallengeDetailsResponse.FromString)
        self.GetChallengeAttachmentUploadUrl = channel.unary_unary('/titanium.ChallengeService/GetChallengeAttachmentUploadUrl', request_serializer=common_dot_challenge__pb2.GetAttachmentUploadUrlRequest.SerializeToString, response_deserializer=common_dot_challenge__pb2.GetAttachmentUploadUrlResponse.FromString)
        self.ChallengeActive = channel.unary_unary('/titanium.ChallengeService/ChallengeActive', request_serializer=common_dot_challenge__pb2.ChallengeActiveRequest.SerializeToString, response_deserializer=common_dot_challenge__pb2.ChallengeActiveResponse.FromString)
        self.ChallengeList = channel.unary_unary('/titanium.ChallengeService/ChallengeList', request_serializer=common_dot_challenge__pb2.ChallengeListRequest.SerializeToString, response_deserializer=common_dot_challenge__pb2.ChallengeListResponse.FromString)
        self.ChallengeHistory = channel.unary_unary('/titanium.ChallengeService/ChallengeHistory', request_serializer=common_dot_challenge__pb2.ChallengeHistoryRequest.SerializeToString, response_deserializer=common_dot_challenge__pb2.ChallengeHistoryResponse.FromString)
        self.ChallengeDecision = channel.unary_unary('/titanium.ChallengeService/ChallengeDecision', request_serializer=common_dot_challenge__pb2.ChallengeDecisionRequest.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.MessageResponse.FromString)
        self.ChallengeFreezeAction = channel.unary_unary('/titanium.ChallengeService/ChallengeFreezeAction', request_serializer=common_dot_challenge__pb2.ChallengeFreezeActionRequest.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.MessageResponse.FromString)

class ChallengeServiceServicer(object):
    """
    ChallengeService is used to operate with challenge process.

    Challenge process is :
    1.A Consensus has been published, the challenge process allows a dealer to “challenge”.
    ("Challenge can be created only for  one of dealer own submitted data points that has benn declared an outlier in the published Consensus.")

    2."Challenger"(dealer) creates challenge with the evidence to support their claim(Using ChallengeCreate method and ChallengeCreateRequest that has evidence)
    "Challenger" can attach any file for additional information about the disputable outlier.(Using pre-signed S3 URL that can be fetched with method GetChallengeAttachmentUploadUrl)
    Note: Challenger gets template with pre-filled data(Using ChallengeFormMeta)  to fill out it in his own way.

    3.The operator considers the evidence and allows it if there is a valid transaction ID filled in.

    4.The operator set decision on the Challenge (Accept or deny)
    Note : Challenge points need to have been accepted as valid by Operator 1 and approved for inclusion in the revised Consensus run by Operator 2 (not the same operator)

    5.After all the challenge points have been reviewed and marked, the "Review Complete" flag is set. A second operator (not the same person who marked the challenge points)
    can now accept all challenges and prepare for the consensus to be run again.

    Note : Operator can also freeze challenge.(Stop process of challenging). Dealer can see current freeze status of the Challenge.(Using ChallengeFreezeStatus method)
    Dealer and Operator can also just view information about the Challenge (Using GetChallenge method)

    """

    def ChallengeFormMeta(self, request, context):
        """ChallengeFormMeta is used to request information(template) about the form fields required to submit a challenge for a specific asset and evidence type.
        Returns response with template with pre-filled data.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ChallengeCreate(self, request, context):
        """ChallengeCreate creates challenge in the system.(Initiate process by dealer)
        To create "challenger" needs to be authorised and challenge can be created only if one of their own submitted data points has been declared an outlier in the published Consensus.
        Need to specify asset and fill out evidence information.
        Returns response that contains ticket ID of the Challenge or the Error.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ChallengeFreezeStatus(self, request, context):
        """ChallengeFreezeStatus returns StatusResponse that contains string that represents freeze status of challenges if the challenge process is stopped and nothing if the one is not.
        Challenge can be stopped by operator.Dealer can see the freeze status using this method.
        Need to specify consensus(where outliers exists) run timestamp.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetChallengeDetails(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetChallengeAttachmentUploadUrl(self, request, context):
        """GetChallengeAttachmentUploadUrl returns string that represents s3 URL that can be used to upload attachment for the challenge.
        The file in attachment can be any file that provides additional information about the disputable outlier.
        Need to specify asset ID, submitted ID and file name.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

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

def add_ChallengeServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'ChallengeFormMeta': grpc.unary_unary_rpc_method_handler(servicer.ChallengeFormMeta, request_deserializer=common_dot_challenge__pb2.ChallengeFormMetaRequest.FromString, response_serializer=common_dot_challenge__pb2.ChallengeFormMetaResponse.SerializeToString), 'ChallengeCreate': grpc.unary_unary_rpc_method_handler(servicer.ChallengeCreate, request_deserializer=common_dot_challenge__pb2.ChallengeCreateRequest.FromString, response_serializer=common_dot_challenge__pb2.ChallengeCreateResponse.SerializeToString), 'ChallengeFreezeStatus': grpc.unary_unary_rpc_method_handler(servicer.ChallengeFreezeStatus, request_deserializer=common_dot_challenge__pb2.ChallengeFreezeStatusRequest.FromString, response_serializer=common_dot_gateway__base__pb2.StatusResponse.SerializeToString), 'GetChallengeDetails': grpc.unary_unary_rpc_method_handler(servicer.GetChallengeDetails, request_deserializer=common_dot_challenge__pb2.GetChallengeDetailsRequest.FromString, response_serializer=common_dot_challenge__pb2.GetChallengeDetailsResponse.SerializeToString), 'GetChallengeAttachmentUploadUrl': grpc.unary_unary_rpc_method_handler(servicer.GetChallengeAttachmentUploadUrl, request_deserializer=common_dot_challenge__pb2.GetAttachmentUploadUrlRequest.FromString, response_serializer=common_dot_challenge__pb2.GetAttachmentUploadUrlResponse.SerializeToString), 'ChallengeActive': grpc.unary_unary_rpc_method_handler(servicer.ChallengeActive, request_deserializer=common_dot_challenge__pb2.ChallengeActiveRequest.FromString, response_serializer=common_dot_challenge__pb2.ChallengeActiveResponse.SerializeToString), 'ChallengeList': grpc.unary_unary_rpc_method_handler(servicer.ChallengeList, request_deserializer=common_dot_challenge__pb2.ChallengeListRequest.FromString, response_serializer=common_dot_challenge__pb2.ChallengeListResponse.SerializeToString), 'ChallengeHistory': grpc.unary_unary_rpc_method_handler(servicer.ChallengeHistory, request_deserializer=common_dot_challenge__pb2.ChallengeHistoryRequest.FromString, response_serializer=common_dot_challenge__pb2.ChallengeHistoryResponse.SerializeToString), 'ChallengeDecision': grpc.unary_unary_rpc_method_handler(servicer.ChallengeDecision, request_deserializer=common_dot_challenge__pb2.ChallengeDecisionRequest.FromString, response_serializer=common_dot_gateway__base__pb2.MessageResponse.SerializeToString), 'ChallengeFreezeAction': grpc.unary_unary_rpc_method_handler(servicer.ChallengeFreezeAction, request_deserializer=common_dot_challenge__pb2.ChallengeFreezeActionRequest.FromString, response_serializer=common_dot_gateway__base__pb2.MessageResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('titanium.ChallengeService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class ChallengeService(object):
    """
    ChallengeService is used to operate with challenge process.

    Challenge process is :
    1.A Consensus has been published, the challenge process allows a dealer to “challenge”.
    ("Challenge can be created only for  one of dealer own submitted data points that has benn declared an outlier in the published Consensus.")

    2."Challenger"(dealer) creates challenge with the evidence to support their claim(Using ChallengeCreate method and ChallengeCreateRequest that has evidence)
    "Challenger" can attach any file for additional information about the disputable outlier.(Using pre-signed S3 URL that can be fetched with method GetChallengeAttachmentUploadUrl)
    Note: Challenger gets template with pre-filled data(Using ChallengeFormMeta)  to fill out it in his own way.

    3.The operator considers the evidence and allows it if there is a valid transaction ID filled in.

    4.The operator set decision on the Challenge (Accept or deny)
    Note : Challenge points need to have been accepted as valid by Operator 1 and approved for inclusion in the revised Consensus run by Operator 2 (not the same operator)

    5.After all the challenge points have been reviewed and marked, the "Review Complete" flag is set. A second operator (not the same person who marked the challenge points)
    can now accept all challenges and prepare for the consensus to be run again.

    Note : Operator can also freeze challenge.(Stop process of challenging). Dealer can see current freeze status of the Challenge.(Using ChallengeFreezeStatus method)
    Dealer and Operator can also just view information about the Challenge (Using GetChallenge method)

    """

    @staticmethod
    def ChallengeFormMeta(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.ChallengeService/ChallengeFormMeta', common_dot_challenge__pb2.ChallengeFormMetaRequest.SerializeToString, common_dot_challenge__pb2.ChallengeFormMetaResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ChallengeCreate(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.ChallengeService/ChallengeCreate', common_dot_challenge__pb2.ChallengeCreateRequest.SerializeToString, common_dot_challenge__pb2.ChallengeCreateResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ChallengeFreezeStatus(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.ChallengeService/ChallengeFreezeStatus', common_dot_challenge__pb2.ChallengeFreezeStatusRequest.SerializeToString, common_dot_gateway__base__pb2.StatusResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetChallengeDetails(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.ChallengeService/GetChallengeDetails', common_dot_challenge__pb2.GetChallengeDetailsRequest.SerializeToString, common_dot_challenge__pb2.GetChallengeDetailsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetChallengeAttachmentUploadUrl(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.ChallengeService/GetChallengeAttachmentUploadUrl', common_dot_challenge__pb2.GetAttachmentUploadUrlRequest.SerializeToString, common_dot_challenge__pb2.GetAttachmentUploadUrlResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ChallengeActive(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.ChallengeService/ChallengeActive', common_dot_challenge__pb2.ChallengeActiveRequest.SerializeToString, common_dot_challenge__pb2.ChallengeActiveResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ChallengeList(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.ChallengeService/ChallengeList', common_dot_challenge__pb2.ChallengeListRequest.SerializeToString, common_dot_challenge__pb2.ChallengeListResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ChallengeHistory(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.ChallengeService/ChallengeHistory', common_dot_challenge__pb2.ChallengeHistoryRequest.SerializeToString, common_dot_challenge__pb2.ChallengeHistoryResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ChallengeDecision(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.ChallengeService/ChallengeDecision', common_dot_challenge__pb2.ChallengeDecisionRequest.SerializeToString, common_dot_gateway__base__pb2.MessageResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ChallengeFreezeAction(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.ChallengeService/ChallengeFreezeAction', common_dot_challenge__pb2.ChallengeFreezeActionRequest.SerializeToString, common_dot_gateway__base__pb2.MessageResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)