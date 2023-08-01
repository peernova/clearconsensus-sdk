"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ..common import usermanagement_fe_specific_pb2 as common_dot_usermanagement__fe__specific__pb2
from ..common import usermanagement_policy_pb2 as common_dot_usermanagement__policy__pb2

class PolicyServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.create = channel.unary_unary('/com.peernova.titanium.casbin.management.grpc.service.PolicyService/create', request_serializer=common_dot_usermanagement__policy__pb2.Policies.SerializeToString, response_deserializer=common_dot_usermanagement__fe__specific__pb2.OperationSuccess.FromString)
        self.getPolicies = channel.unary_unary('/com.peernova.titanium.casbin.management.grpc.service.PolicyService/getPolicies', request_serializer=common_dot_usermanagement__policy__pb2.PolicyType.SerializeToString, response_deserializer=common_dot_usermanagement__policy__pb2.PoliciesResponse.FromString)
        self.removePolicy = channel.unary_unary('/com.peernova.titanium.casbin.management.grpc.service.PolicyService/removePolicy', request_serializer=common_dot_usermanagement__policy__pb2.PolicyDto.SerializeToString, response_deserializer=common_dot_usermanagement__fe__specific__pb2.OperationSuccess.FromString)
        self.checkPolicy = channel.unary_unary('/com.peernova.titanium.casbin.management.grpc.service.PolicyService/checkPolicy', request_serializer=common_dot_usermanagement__policy__pb2.PolicyDto.SerializeToString, response_deserializer=common_dot_usermanagement__fe__specific__pb2.OperationSuccess.FromString)
        self.getAssets = channel.unary_unary('/com.peernova.titanium.casbin.management.grpc.service.PolicyService/getAssets', request_serializer=common_dot_usermanagement__policy__pb2.UsernamePermissionRequest.SerializeToString, response_deserializer=common_dot_usermanagement__policy__pb2.PoliciesListResponse.FromString)
        self.getApis = channel.unary_unary('/com.peernova.titanium.casbin.management.grpc.service.PolicyService/getApis', request_serializer=common_dot_usermanagement__policy__pb2.UsernamePermissionRequest.SerializeToString, response_deserializer=common_dot_usermanagement__policy__pb2.PoliciesListResponse.FromString)
        self.getAddons = channel.unary_unary('/com.peernova.titanium.casbin.management.grpc.service.PolicyService/getAddons', request_serializer=common_dot_usermanagement__policy__pb2.UsernamePermissionRequest.SerializeToString, response_deserializer=common_dot_usermanagement__policy__pb2.PoliciesListResponse.FromString)

class PolicyServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getPolicies(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def removePolicy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def checkPolicy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getAssets(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getApis(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getAddons(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_PolicyServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'create': grpc.unary_unary_rpc_method_handler(servicer.create, request_deserializer=common_dot_usermanagement__policy__pb2.Policies.FromString, response_serializer=common_dot_usermanagement__fe__specific__pb2.OperationSuccess.SerializeToString), 'getPolicies': grpc.unary_unary_rpc_method_handler(servicer.getPolicies, request_deserializer=common_dot_usermanagement__policy__pb2.PolicyType.FromString, response_serializer=common_dot_usermanagement__policy__pb2.PoliciesResponse.SerializeToString), 'removePolicy': grpc.unary_unary_rpc_method_handler(servicer.removePolicy, request_deserializer=common_dot_usermanagement__policy__pb2.PolicyDto.FromString, response_serializer=common_dot_usermanagement__fe__specific__pb2.OperationSuccess.SerializeToString), 'checkPolicy': grpc.unary_unary_rpc_method_handler(servicer.checkPolicy, request_deserializer=common_dot_usermanagement__policy__pb2.PolicyDto.FromString, response_serializer=common_dot_usermanagement__fe__specific__pb2.OperationSuccess.SerializeToString), 'getAssets': grpc.unary_unary_rpc_method_handler(servicer.getAssets, request_deserializer=common_dot_usermanagement__policy__pb2.UsernamePermissionRequest.FromString, response_serializer=common_dot_usermanagement__policy__pb2.PoliciesListResponse.SerializeToString), 'getApis': grpc.unary_unary_rpc_method_handler(servicer.getApis, request_deserializer=common_dot_usermanagement__policy__pb2.UsernamePermissionRequest.FromString, response_serializer=common_dot_usermanagement__policy__pb2.PoliciesListResponse.SerializeToString), 'getAddons': grpc.unary_unary_rpc_method_handler(servicer.getAddons, request_deserializer=common_dot_usermanagement__policy__pb2.UsernamePermissionRequest.FromString, response_serializer=common_dot_usermanagement__policy__pb2.PoliciesListResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('com.peernova.titanium.casbin.management.grpc.service.PolicyService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class PolicyService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def create(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.peernova.titanium.casbin.management.grpc.service.PolicyService/create', common_dot_usermanagement__policy__pb2.Policies.SerializeToString, common_dot_usermanagement__fe__specific__pb2.OperationSuccess.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getPolicies(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.peernova.titanium.casbin.management.grpc.service.PolicyService/getPolicies', common_dot_usermanagement__policy__pb2.PolicyType.SerializeToString, common_dot_usermanagement__policy__pb2.PoliciesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def removePolicy(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.peernova.titanium.casbin.management.grpc.service.PolicyService/removePolicy', common_dot_usermanagement__policy__pb2.PolicyDto.SerializeToString, common_dot_usermanagement__fe__specific__pb2.OperationSuccess.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def checkPolicy(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.peernova.titanium.casbin.management.grpc.service.PolicyService/checkPolicy', common_dot_usermanagement__policy__pb2.PolicyDto.SerializeToString, common_dot_usermanagement__fe__specific__pb2.OperationSuccess.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getAssets(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.peernova.titanium.casbin.management.grpc.service.PolicyService/getAssets', common_dot_usermanagement__policy__pb2.UsernamePermissionRequest.SerializeToString, common_dot_usermanagement__policy__pb2.PoliciesListResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getApis(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.peernova.titanium.casbin.management.grpc.service.PolicyService/getApis', common_dot_usermanagement__policy__pb2.UsernamePermissionRequest.SerializeToString, common_dot_usermanagement__policy__pb2.PoliciesListResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getAddons(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.peernova.titanium.casbin.management.grpc.service.PolicyService/getAddons', common_dot_usermanagement__policy__pb2.UsernamePermissionRequest.SerializeToString, common_dot_usermanagement__policy__pb2.PoliciesListResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)