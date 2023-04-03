"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2
from ..common import normalization_pb2 as common_dot_normalization__pb2

class NormalizationServiceStub(object):
    """NormalizationService is service that can be used to operate with rules for normalization of the data.

    Process of normalization is updating submission in case of submission issues it happens before validation
    and simplifies communication with our clients since we can skip minor defects like redundant spaces.

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddNormalizationRule = channel.unary_unary('/titanium.NormalizationService/AddNormalizationRule', request_serializer=common_dot_normalization__pb2.NormalizationRuleDefinition.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.AcknowledgeResponse.FromString)
        self.GetNormalizationRule = channel.unary_unary('/titanium.NormalizationService/GetNormalizationRule', request_serializer=common_dot_gateway__base__pb2.GetDefinition.SerializeToString, response_deserializer=common_dot_normalization__pb2.NormalizationRuleResponse.FromString)
        self.EnableNormalizationRule = channel.unary_unary('/titanium.NormalizationService/EnableNormalizationRule', request_serializer=common_dot_gateway__base__pb2.GetDefinition.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.AcknowledgeResponse.FromString)
        self.DisableNormalizationRule = channel.unary_unary('/titanium.NormalizationService/DisableNormalizationRule', request_serializer=common_dot_gateway__base__pb2.GetDefinition.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.AcknowledgeResponse.FromString)
        self.ListNormalizationRules = channel.unary_unary('/titanium.NormalizationService/ListNormalizationRules', request_serializer=common_dot_gateway__base__pb2.ListRequest.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.ListRuleResponse.FromString)
        self.ListNormalizationRuleVersions = channel.unary_unary('/titanium.NormalizationService/ListNormalizationRuleVersions', request_serializer=common_dot_gateway__base__pb2.GetDefinition.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.ListVersionResponse.FromString)
        self.GetNormalizationRuleVersion = channel.unary_unary('/titanium.NormalizationService/GetNormalizationRuleVersion', request_serializer=common_dot_gateway__base__pb2.VersionRequest.SerializeToString, response_deserializer=common_dot_normalization__pb2.NormalizationRuleResponse.FromString)

class NormalizationServiceServicer(object):
    """NormalizationService is service that can be used to operate with rules for normalization of the data.

    Process of normalization is updating submission in case of submission issues it happens before validation
    and simplifies communication with our clients since we can skip minor defects like redundant spaces.

    """

    def AddNormalizationRule(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetNormalizationRule(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EnableNormalizationRule(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DisableNormalizationRule(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListNormalizationRules(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListNormalizationRuleVersions(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetNormalizationRuleVersion(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_NormalizationServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'AddNormalizationRule': grpc.unary_unary_rpc_method_handler(servicer.AddNormalizationRule, request_deserializer=common_dot_normalization__pb2.NormalizationRuleDefinition.FromString, response_serializer=common_dot_gateway__base__pb2.AcknowledgeResponse.SerializeToString), 'GetNormalizationRule': grpc.unary_unary_rpc_method_handler(servicer.GetNormalizationRule, request_deserializer=common_dot_gateway__base__pb2.GetDefinition.FromString, response_serializer=common_dot_normalization__pb2.NormalizationRuleResponse.SerializeToString), 'EnableNormalizationRule': grpc.unary_unary_rpc_method_handler(servicer.EnableNormalizationRule, request_deserializer=common_dot_gateway__base__pb2.GetDefinition.FromString, response_serializer=common_dot_gateway__base__pb2.AcknowledgeResponse.SerializeToString), 'DisableNormalizationRule': grpc.unary_unary_rpc_method_handler(servicer.DisableNormalizationRule, request_deserializer=common_dot_gateway__base__pb2.GetDefinition.FromString, response_serializer=common_dot_gateway__base__pb2.AcknowledgeResponse.SerializeToString), 'ListNormalizationRules': grpc.unary_unary_rpc_method_handler(servicer.ListNormalizationRules, request_deserializer=common_dot_gateway__base__pb2.ListRequest.FromString, response_serializer=common_dot_gateway__base__pb2.ListRuleResponse.SerializeToString), 'ListNormalizationRuleVersions': grpc.unary_unary_rpc_method_handler(servicer.ListNormalizationRuleVersions, request_deserializer=common_dot_gateway__base__pb2.GetDefinition.FromString, response_serializer=common_dot_gateway__base__pb2.ListVersionResponse.SerializeToString), 'GetNormalizationRuleVersion': grpc.unary_unary_rpc_method_handler(servicer.GetNormalizationRuleVersion, request_deserializer=common_dot_gateway__base__pb2.VersionRequest.FromString, response_serializer=common_dot_normalization__pb2.NormalizationRuleResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('titanium.NormalizationService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class NormalizationService(object):
    """NormalizationService is service that can be used to operate with rules for normalization of the data.

    Process of normalization is updating submission in case of submission issues it happens before validation
    and simplifies communication with our clients since we can skip minor defects like redundant spaces.

    """

    @staticmethod
    def AddNormalizationRule(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.NormalizationService/AddNormalizationRule', common_dot_normalization__pb2.NormalizationRuleDefinition.SerializeToString, common_dot_gateway__base__pb2.AcknowledgeResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetNormalizationRule(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.NormalizationService/GetNormalizationRule', common_dot_gateway__base__pb2.GetDefinition.SerializeToString, common_dot_normalization__pb2.NormalizationRuleResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EnableNormalizationRule(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.NormalizationService/EnableNormalizationRule', common_dot_gateway__base__pb2.GetDefinition.SerializeToString, common_dot_gateway__base__pb2.AcknowledgeResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DisableNormalizationRule(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.NormalizationService/DisableNormalizationRule', common_dot_gateway__base__pb2.GetDefinition.SerializeToString, common_dot_gateway__base__pb2.AcknowledgeResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListNormalizationRules(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.NormalizationService/ListNormalizationRules', common_dot_gateway__base__pb2.ListRequest.SerializeToString, common_dot_gateway__base__pb2.ListRuleResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListNormalizationRuleVersions(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.NormalizationService/ListNormalizationRuleVersions', common_dot_gateway__base__pb2.GetDefinition.SerializeToString, common_dot_gateway__base__pb2.ListVersionResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetNormalizationRuleVersion(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.NormalizationService/GetNormalizationRuleVersion', common_dot_gateway__base__pb2.VersionRequest.SerializeToString, common_dot_normalization__pb2.NormalizationRuleResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)