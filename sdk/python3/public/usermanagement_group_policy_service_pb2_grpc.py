"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ..common import usermanagement_fe_specific_pb2 as common_dot_usermanagement__fe__specific__pb2
from ..common import usermanagement_group_policy_pb2 as common_dot_usermanagement__group__policy__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2

class GroupPolicyServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.create = channel.unary_unary('/com.peernova.titanium.casbin.management.grpc.service.GroupPolicyService/create', request_serializer=common_dot_usermanagement__group__policy__pb2.GroupPolicies.SerializeToString, response_deserializer=common_dot_usermanagement__fe__specific__pb2.ServiceResponse.FromString)
        self.getPolicies = channel.unary_unary('/com.peernova.titanium.casbin.management.grpc.service.GroupPolicyService/getPolicies', request_serializer=google_dot_protobuf_dot_wrappers__pb2.StringValue.SerializeToString, response_deserializer=common_dot_usermanagement__fe__specific__pb2.ServiceResponse.FromString)

class GroupPolicyServiceServicer(object):
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

def add_GroupPolicyServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'create': grpc.unary_unary_rpc_method_handler(servicer.create, request_deserializer=common_dot_usermanagement__group__policy__pb2.GroupPolicies.FromString, response_serializer=common_dot_usermanagement__fe__specific__pb2.ServiceResponse.SerializeToString), 'getPolicies': grpc.unary_unary_rpc_method_handler(servicer.getPolicies, request_deserializer=google_dot_protobuf_dot_wrappers__pb2.StringValue.FromString, response_serializer=common_dot_usermanagement__fe__specific__pb2.ServiceResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('com.peernova.titanium.casbin.management.grpc.service.GroupPolicyService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class GroupPolicyService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def create(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.peernova.titanium.casbin.management.grpc.service.GroupPolicyService/create', common_dot_usermanagement__group__policy__pb2.GroupPolicies.SerializeToString, common_dot_usermanagement__fe__specific__pb2.ServiceResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getPolicies(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.peernova.titanium.casbin.management.grpc.service.GroupPolicyService/getPolicies', google_dot_protobuf_dot_wrappers__pb2.StringValue.SerializeToString, common_dot_usermanagement__fe__specific__pb2.ServiceResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)