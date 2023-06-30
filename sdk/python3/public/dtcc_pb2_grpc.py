"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ..public import dtcc_pb2 as public_dot_dtcc__pb2

class DtccServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetDtccTable = channel.unary_unary('/titanium.DtccService/GetDtccTable', request_serializer=public_dot_dtcc__pb2.DtccTabRequest.SerializeToString, response_deserializer=public_dot_dtcc__pb2.DtccTabResponse.FromString)

class DtccServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetDtccTable(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_DtccServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'GetDtccTable': grpc.unary_unary_rpc_method_handler(servicer.GetDtccTable, request_deserializer=public_dot_dtcc__pb2.DtccTabRequest.FromString, response_serializer=public_dot_dtcc__pb2.DtccTabResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('titanium.DtccService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class DtccService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetDtccTable(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.DtccService/GetDtccTable', public_dot_dtcc__pb2.DtccTabRequest.SerializeToString, public_dot_dtcc__pb2.DtccTabResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)