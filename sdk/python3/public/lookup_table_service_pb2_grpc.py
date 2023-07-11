"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2
from ..common import lookup_table_pb2 as common_dot_lookup__table__pb2

class LookupTableServiceStub(object):
    """LookupTableService is service that responsible for lookup tables.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddLookupTable = channel.unary_unary('/titanium.LookupTableService/AddLookupTable', request_serializer=common_dot_lookup__table__pb2.AddLookupTableRequest.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.AcknowledgeResponse.FromString)
        self.GetLookupTable = channel.unary_unary('/titanium.LookupTableService/GetLookupTable', request_serializer=common_dot_gateway__base__pb2.GetDefinition.SerializeToString, response_deserializer=common_dot_lookup__table__pb2.GetLookupTableResponse.FromString)
        self.ListLookupTables = channel.unary_unary('/titanium.LookupTableService/ListLookupTables', request_serializer=common_dot_gateway__base__pb2.ListRequest.SerializeToString, response_deserializer=common_dot_lookup__table__pb2.ListLookupTableResponse.FromString)
        self.ListLookupTableVersions = channel.unary_unary('/titanium.LookupTableService/ListLookupTableVersions', request_serializer=common_dot_gateway__base__pb2.GetDefinition.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.ListVersionResponse.FromString)
        self.EnableLookupTable = channel.unary_unary('/titanium.LookupTableService/EnableLookupTable', request_serializer=common_dot_gateway__base__pb2.EnableDisableRequest.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.AcknowledgeResponse.FromString)
        self.DisableLookupTable = channel.unary_unary('/titanium.LookupTableService/DisableLookupTable', request_serializer=common_dot_gateway__base__pb2.EnableDisableRequest.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.AcknowledgeResponse.FromString)

class LookupTableServiceServicer(object):
    """LookupTableService is service that responsible for lookup tables.
    """

    def AddLookupTable(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLookupTable(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListLookupTables(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListLookupTableVersions(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EnableLookupTable(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DisableLookupTable(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_LookupTableServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'AddLookupTable': grpc.unary_unary_rpc_method_handler(servicer.AddLookupTable, request_deserializer=common_dot_lookup__table__pb2.AddLookupTableRequest.FromString, response_serializer=common_dot_gateway__base__pb2.AcknowledgeResponse.SerializeToString), 'GetLookupTable': grpc.unary_unary_rpc_method_handler(servicer.GetLookupTable, request_deserializer=common_dot_gateway__base__pb2.GetDefinition.FromString, response_serializer=common_dot_lookup__table__pb2.GetLookupTableResponse.SerializeToString), 'ListLookupTables': grpc.unary_unary_rpc_method_handler(servicer.ListLookupTables, request_deserializer=common_dot_gateway__base__pb2.ListRequest.FromString, response_serializer=common_dot_lookup__table__pb2.ListLookupTableResponse.SerializeToString), 'ListLookupTableVersions': grpc.unary_unary_rpc_method_handler(servicer.ListLookupTableVersions, request_deserializer=common_dot_gateway__base__pb2.GetDefinition.FromString, response_serializer=common_dot_gateway__base__pb2.ListVersionResponse.SerializeToString), 'EnableLookupTable': grpc.unary_unary_rpc_method_handler(servicer.EnableLookupTable, request_deserializer=common_dot_gateway__base__pb2.EnableDisableRequest.FromString, response_serializer=common_dot_gateway__base__pb2.AcknowledgeResponse.SerializeToString), 'DisableLookupTable': grpc.unary_unary_rpc_method_handler(servicer.DisableLookupTable, request_deserializer=common_dot_gateway__base__pb2.EnableDisableRequest.FromString, response_serializer=common_dot_gateway__base__pb2.AcknowledgeResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('titanium.LookupTableService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class LookupTableService(object):
    """LookupTableService is service that responsible for lookup tables.
    """

    @staticmethod
    def AddLookupTable(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.LookupTableService/AddLookupTable', common_dot_lookup__table__pb2.AddLookupTableRequest.SerializeToString, common_dot_gateway__base__pb2.AcknowledgeResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetLookupTable(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.LookupTableService/GetLookupTable', common_dot_gateway__base__pb2.GetDefinition.SerializeToString, common_dot_lookup__table__pb2.GetLookupTableResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListLookupTables(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.LookupTableService/ListLookupTables', common_dot_gateway__base__pb2.ListRequest.SerializeToString, common_dot_lookup__table__pb2.ListLookupTableResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListLookupTableVersions(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.LookupTableService/ListLookupTableVersions', common_dot_gateway__base__pb2.GetDefinition.SerializeToString, common_dot_gateway__base__pb2.ListVersionResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EnableLookupTable(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.LookupTableService/EnableLookupTable', common_dot_gateway__base__pb2.EnableDisableRequest.SerializeToString, common_dot_gateway__base__pb2.AcknowledgeResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DisableLookupTable(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.LookupTableService/DisableLookupTable', common_dot_gateway__base__pb2.EnableDisableRequest.SerializeToString, common_dot_gateway__base__pb2.AcknowledgeResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)