"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ..common import data_pb2 as common_dot_data__pb2
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2
from ..private import data_private_service_pb2 as private_dot_data__private__service__pb2

class DataServicePrivateStub(object):
    """DataUtilsPrivate is util service with private methods that help operate with data.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ExportReport = channel.unary_unary('/titanium.DataServicePrivate/ExportReport', request_serializer=common_dot_data__pb2.ExportReportRequest.SerializeToString, response_deserializer=common_dot_data__pb2.ExportResponse.FromString)
        self.AuthorizeUpload = channel.unary_unary('/titanium.DataServicePrivate/AuthorizeUpload', request_serializer=common_dot_data__pb2.UploadURLRequest.SerializeToString, response_deserializer=private_dot_data__private__service__pb2.UploadAuthorizationResponse.FromString)
        self.NotifyUpload = channel.unary_unary('/titanium.DataServicePrivate/NotifyUpload', request_serializer=private_dot_data__private__service__pb2.UploadNotifyRequest.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.MessageResponse.FromString)

class DataServicePrivateServicer(object):
    """DataUtilsPrivate is util service with private methods that help operate with data.
    """

    def ExportReport(self, request, context):
        """todo remove /operator from URL paths
        ExportReport returns pre signed s3 urls which can be used for export report(and compression type)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AuthorizeUpload(self, request, context):
        """todo remove /operator from URL paths
        AuthorizeUpload shows availability of uploading for user.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NotifyUpload(self, request, context):
        """NotifyUpload returns message with notify that data was uploaded according to url in request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_DataServicePrivateServicer_to_server(servicer, server):
    rpc_method_handlers = {'ExportReport': grpc.unary_unary_rpc_method_handler(servicer.ExportReport, request_deserializer=common_dot_data__pb2.ExportReportRequest.FromString, response_serializer=common_dot_data__pb2.ExportResponse.SerializeToString), 'AuthorizeUpload': grpc.unary_unary_rpc_method_handler(servicer.AuthorizeUpload, request_deserializer=common_dot_data__pb2.UploadURLRequest.FromString, response_serializer=private_dot_data__private__service__pb2.UploadAuthorizationResponse.SerializeToString), 'NotifyUpload': grpc.unary_unary_rpc_method_handler(servicer.NotifyUpload, request_deserializer=private_dot_data__private__service__pb2.UploadNotifyRequest.FromString, response_serializer=common_dot_gateway__base__pb2.MessageResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('titanium.DataServicePrivate', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class DataServicePrivate(object):
    """DataUtilsPrivate is util service with private methods that help operate with data.
    """

    @staticmethod
    def ExportReport(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.DataServicePrivate/ExportReport', common_dot_data__pb2.ExportReportRequest.SerializeToString, common_dot_data__pb2.ExportResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AuthorizeUpload(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.DataServicePrivate/AuthorizeUpload', common_dot_data__pb2.UploadURLRequest.SerializeToString, private_dot_data__private__service__pb2.UploadAuthorizationResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NotifyUpload(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.DataServicePrivate/NotifyUpload', private_dot_data__private__service__pb2.UploadNotifyRequest.SerializeToString, common_dot_gateway__base__pb2.MessageResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)