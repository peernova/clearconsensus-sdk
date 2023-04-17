"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ..common import submission_pb2 as common_dot_submission__pb2

class SubmissionServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetFilesView = channel.unary_unary('/titanium.SubmissionService/GetFilesView', request_serializer=common_dot_submission__pb2.GetSubmissionFilesRequest.SerializeToString, response_deserializer=common_dot_submission__pb2.GetSubmissionFilesResponse.FromString)

class SubmissionServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetFilesView(self, request, context):
        """GetFilesView returns information about submitted to s3 storage files.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_SubmissionServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'GetFilesView': grpc.unary_unary_rpc_method_handler(servicer.GetFilesView, request_deserializer=common_dot_submission__pb2.GetSubmissionFilesRequest.FromString, response_serializer=common_dot_submission__pb2.GetSubmissionFilesResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('titanium.SubmissionService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class SubmissionService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetFilesView(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.SubmissionService/GetFilesView', common_dot_submission__pb2.GetSubmissionFilesRequest.SerializeToString, common_dot_submission__pb2.GetSubmissionFilesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)