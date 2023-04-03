"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2
from ..private import supported_fields_private_service_pb2 as private_dot_supported__fields__private__service__pb2

class SupportedFieldsPrivateServiceStub(object):
    """todo remove /operator from URL paths

    SupportedFieldsPrivateService is service with private methods that responsible for supported fields.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateSupportedFields = channel.unary_unary('/titanium.SupportedFieldsPrivateService/CreateSupportedFields', request_serializer=private_dot_supported__fields__private__service__pb2.SupportedFieldsValues.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.MessageResponse.FromString)
        self.AddSupportedFields = channel.unary_unary('/titanium.SupportedFieldsPrivateService/AddSupportedFields', request_serializer=private_dot_supported__fields__private__service__pb2.SupportedFieldsValues.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.MessageResponse.FromString)
        self.DeleteSupportedFields = channel.unary_unary('/titanium.SupportedFieldsPrivateService/DeleteSupportedFields', request_serializer=private_dot_supported__fields__private__service__pb2.SupportedFieldsValues.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.MessageResponse.FromString)

class SupportedFieldsPrivateServiceServicer(object):
    """todo remove /operator from URL paths

    SupportedFieldsPrivateService is service with private methods that responsible for supported fields.
    """

    def CreateSupportedFields(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddSupportedFields(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteSupportedFields(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_SupportedFieldsPrivateServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'CreateSupportedFields': grpc.unary_unary_rpc_method_handler(servicer.CreateSupportedFields, request_deserializer=private_dot_supported__fields__private__service__pb2.SupportedFieldsValues.FromString, response_serializer=common_dot_gateway__base__pb2.MessageResponse.SerializeToString), 'AddSupportedFields': grpc.unary_unary_rpc_method_handler(servicer.AddSupportedFields, request_deserializer=private_dot_supported__fields__private__service__pb2.SupportedFieldsValues.FromString, response_serializer=common_dot_gateway__base__pb2.MessageResponse.SerializeToString), 'DeleteSupportedFields': grpc.unary_unary_rpc_method_handler(servicer.DeleteSupportedFields, request_deserializer=private_dot_supported__fields__private__service__pb2.SupportedFieldsValues.FromString, response_serializer=common_dot_gateway__base__pb2.MessageResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('titanium.SupportedFieldsPrivateService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class SupportedFieldsPrivateService(object):
    """todo remove /operator from URL paths

    SupportedFieldsPrivateService is service with private methods that responsible for supported fields.
    """

    @staticmethod
    def CreateSupportedFields(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.SupportedFieldsPrivateService/CreateSupportedFields', private_dot_supported__fields__private__service__pb2.SupportedFieldsValues.SerializeToString, common_dot_gateway__base__pb2.MessageResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddSupportedFields(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.SupportedFieldsPrivateService/AddSupportedFields', private_dot_supported__fields__private__service__pb2.SupportedFieldsValues.SerializeToString, common_dot_gateway__base__pb2.MessageResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteSupportedFields(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.SupportedFieldsPrivateService/DeleteSupportedFields', private_dot_supported__fields__private__service__pb2.SupportedFieldsValues.SerializeToString, common_dot_gateway__base__pb2.MessageResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)