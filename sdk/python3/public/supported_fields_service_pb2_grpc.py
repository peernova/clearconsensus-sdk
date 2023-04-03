"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ..common import supported_fields_pb2 as common_dot_supported__fields__pb2

class SupportedFieldsServiceStub(object):
    """SupportedFieldsService is service that responsible for supported fields.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListSupportedFields = channel.unary_unary('/titanium.SupportedFieldsService/ListSupportedFields', request_serializer=common_dot_supported__fields__pb2.GetSupportedFields.SerializeToString, response_deserializer=common_dot_supported__fields__pb2.GetSupportedFieldsResponse.FromString)
        self.GetSupportedFieldsValues = channel.unary_unary('/titanium.SupportedFieldsService/GetSupportedFieldsValues', request_serializer=common_dot_supported__fields__pb2.SupportedField.SerializeToString, response_deserializer=common_dot_supported__fields__pb2.GetFieldValuesResponse.FromString)

class SupportedFieldsServiceServicer(object):
    """SupportedFieldsService is service that responsible for supported fields.
    """

    def ListSupportedFields(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSupportedFieldsValues(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_SupportedFieldsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'ListSupportedFields': grpc.unary_unary_rpc_method_handler(servicer.ListSupportedFields, request_deserializer=common_dot_supported__fields__pb2.GetSupportedFields.FromString, response_serializer=common_dot_supported__fields__pb2.GetSupportedFieldsResponse.SerializeToString), 'GetSupportedFieldsValues': grpc.unary_unary_rpc_method_handler(servicer.GetSupportedFieldsValues, request_deserializer=common_dot_supported__fields__pb2.SupportedField.FromString, response_serializer=common_dot_supported__fields__pb2.GetFieldValuesResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('titanium.SupportedFieldsService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class SupportedFieldsService(object):
    """SupportedFieldsService is service that responsible for supported fields.
    """

    @staticmethod
    def ListSupportedFields(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.SupportedFieldsService/ListSupportedFields', common_dot_supported__fields__pb2.GetSupportedFields.SerializeToString, common_dot_supported__fields__pb2.GetSupportedFieldsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetSupportedFieldsValues(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.SupportedFieldsService/GetSupportedFieldsValues', common_dot_supported__fields__pb2.SupportedField.SerializeToString, common_dot_supported__fields__pb2.GetFieldValuesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)