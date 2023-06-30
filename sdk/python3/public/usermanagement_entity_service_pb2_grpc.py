"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ..common import usermanagement_entity_pb2 as common_dot_usermanagement__entity__pb2
from ..common import usermanagement_fe_specific_pb2 as common_dot_usermanagement__fe__specific__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2

class EntityServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.create = channel.unary_unary('/com.peernova.titanium.casbin.management.grpc.service.EntityService/create', request_serializer=common_dot_usermanagement__entity__pb2.EntityDto.SerializeToString, response_deserializer=common_dot_usermanagement__fe__specific__pb2.ServiceResponse.FromString)
        self.update = channel.unary_unary('/com.peernova.titanium.casbin.management.grpc.service.EntityService/update', request_serializer=common_dot_usermanagement__entity__pb2.EntityDto.SerializeToString, response_deserializer=common_dot_usermanagement__fe__specific__pb2.ServiceResponse.FromString)
        self.getById = channel.unary_unary('/com.peernova.titanium.casbin.management.grpc.service.EntityService/getById', request_serializer=google_dot_protobuf_dot_wrappers__pb2.StringValue.SerializeToString, response_deserializer=common_dot_usermanagement__fe__specific__pb2.ServiceResponse.FromString)
        self.getAllEnabledOnly = channel.unary_unary('/com.peernova.titanium.casbin.management.grpc.service.EntityService/getAllEnabledOnly', request_serializer=google_dot_protobuf_dot_wrappers__pb2.BoolValue.SerializeToString, response_deserializer=common_dot_usermanagement__fe__specific__pb2.ServiceResponse.FromString)
        self.find = channel.unary_unary('/com.peernova.titanium.casbin.management.grpc.service.EntityService/find', request_serializer=common_dot_usermanagement__fe__specific__pb2.SearchCriteria.SerializeToString, response_deserializer=common_dot_usermanagement__fe__specific__pb2.ServiceResponse.FromString)

class EntityServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getAllEnabledOnly(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def find(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_EntityServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'create': grpc.unary_unary_rpc_method_handler(servicer.create, request_deserializer=common_dot_usermanagement__entity__pb2.EntityDto.FromString, response_serializer=common_dot_usermanagement__fe__specific__pb2.ServiceResponse.SerializeToString), 'update': grpc.unary_unary_rpc_method_handler(servicer.update, request_deserializer=common_dot_usermanagement__entity__pb2.EntityDto.FromString, response_serializer=common_dot_usermanagement__fe__specific__pb2.ServiceResponse.SerializeToString), 'getById': grpc.unary_unary_rpc_method_handler(servicer.getById, request_deserializer=google_dot_protobuf_dot_wrappers__pb2.StringValue.FromString, response_serializer=common_dot_usermanagement__fe__specific__pb2.ServiceResponse.SerializeToString), 'getAllEnabledOnly': grpc.unary_unary_rpc_method_handler(servicer.getAllEnabledOnly, request_deserializer=google_dot_protobuf_dot_wrappers__pb2.BoolValue.FromString, response_serializer=common_dot_usermanagement__fe__specific__pb2.ServiceResponse.SerializeToString), 'find': grpc.unary_unary_rpc_method_handler(servicer.find, request_deserializer=common_dot_usermanagement__fe__specific__pb2.SearchCriteria.FromString, response_serializer=common_dot_usermanagement__fe__specific__pb2.ServiceResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('com.peernova.titanium.casbin.management.grpc.service.EntityService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class EntityService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def create(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.peernova.titanium.casbin.management.grpc.service.EntityService/create', common_dot_usermanagement__entity__pb2.EntityDto.SerializeToString, common_dot_usermanagement__fe__specific__pb2.ServiceResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def update(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.peernova.titanium.casbin.management.grpc.service.EntityService/update', common_dot_usermanagement__entity__pb2.EntityDto.SerializeToString, common_dot_usermanagement__fe__specific__pb2.ServiceResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getById(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.peernova.titanium.casbin.management.grpc.service.EntityService/getById', google_dot_protobuf_dot_wrappers__pb2.StringValue.SerializeToString, common_dot_usermanagement__fe__specific__pb2.ServiceResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getAllEnabledOnly(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.peernova.titanium.casbin.management.grpc.service.EntityService/getAllEnabledOnly', google_dot_protobuf_dot_wrappers__pb2.BoolValue.SerializeToString, common_dot_usermanagement__fe__specific__pb2.ServiceResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def find(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.peernova.titanium.casbin.management.grpc.service.EntityService/find', common_dot_usermanagement__fe__specific__pb2.SearchCriteria.SerializeToString, common_dot_usermanagement__fe__specific__pb2.ServiceResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)