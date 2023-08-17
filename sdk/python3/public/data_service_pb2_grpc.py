"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ..common import data_pb2 as common_dot_data__pb2
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2

class DataServiceStub(object):
    """DataService is a utility service that provides operations on data.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Submitted = channel.unary_unary('/titanium.DataService/Submitted', request_serializer=common_dot_data__pb2.SubmittedRequest.SerializeToString, response_deserializer=common_dot_data__pb2.SubmittedResponse.FromString)
        self.Export = channel.unary_unary('/titanium.DataService/Export', request_serializer=common_dot_data__pb2.ExportRequest.SerializeToString, response_deserializer=common_dot_data__pb2.ExportResponse.FromString)
        self.UploadURL = channel.unary_unary('/titanium.DataService/UploadURL', request_serializer=common_dot_data__pb2.UploadURLRequest.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.UploadURLResponse.FromString)
        self.AuthorizeUpload = channel.unary_unary('/titanium.DataService/AuthorizeUpload', request_serializer=common_dot_data__pb2.UploadURLRequest.SerializeToString, response_deserializer=common_dot_data__pb2.UploadAuthorizationResponse.FromString)
        self.NotifyUpload = channel.unary_unary('/titanium.DataService/NotifyUpload', request_serializer=common_dot_data__pb2.UploadNotifyRequest.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.MessageResponse.FromString)
        self.UploadData = channel.unary_unary('/titanium.DataService/UploadData', request_serializer=common_dot_data__pb2.UploadDataRequest.SerializeToString, response_deserializer=common_dot_data__pb2.UploadDataResponse.FromString)
        self.CompleteDataUpload = channel.unary_unary('/titanium.DataService/CompleteDataUpload', request_serializer=common_dot_data__pb2.CompleteDataUploadRequest.SerializeToString, response_deserializer=common_dot_data__pb2.CompleteDataUploadResponse.FromString)

class DataServiceServicer(object):
    """DataService is a utility service that provides operations on data.
    """

    def Submitted(self, request, context):
        """Submitted returns submitted data based on the request made.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Export(self, request, context):
        """Export exports data according to the request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UploadURL(self, request, context):
        """UploadURL returns a pre-signed S3 URL for uploading data.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AuthorizeUpload(self, request, context):
        """AuthorizeUpload shows availability of uploading for user.
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

    def UploadData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CompleteDataUpload(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_DataServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'Submitted': grpc.unary_unary_rpc_method_handler(servicer.Submitted, request_deserializer=common_dot_data__pb2.SubmittedRequest.FromString, response_serializer=common_dot_data__pb2.SubmittedResponse.SerializeToString), 'Export': grpc.unary_unary_rpc_method_handler(servicer.Export, request_deserializer=common_dot_data__pb2.ExportRequest.FromString, response_serializer=common_dot_data__pb2.ExportResponse.SerializeToString), 'UploadURL': grpc.unary_unary_rpc_method_handler(servicer.UploadURL, request_deserializer=common_dot_data__pb2.UploadURLRequest.FromString, response_serializer=common_dot_gateway__base__pb2.UploadURLResponse.SerializeToString), 'AuthorizeUpload': grpc.unary_unary_rpc_method_handler(servicer.AuthorizeUpload, request_deserializer=common_dot_data__pb2.UploadURLRequest.FromString, response_serializer=common_dot_data__pb2.UploadAuthorizationResponse.SerializeToString), 'NotifyUpload': grpc.unary_unary_rpc_method_handler(servicer.NotifyUpload, request_deserializer=common_dot_data__pb2.UploadNotifyRequest.FromString, response_serializer=common_dot_gateway__base__pb2.MessageResponse.SerializeToString), 'UploadData': grpc.unary_unary_rpc_method_handler(servicer.UploadData, request_deserializer=common_dot_data__pb2.UploadDataRequest.FromString, response_serializer=common_dot_data__pb2.UploadDataResponse.SerializeToString), 'CompleteDataUpload': grpc.unary_unary_rpc_method_handler(servicer.CompleteDataUpload, request_deserializer=common_dot_data__pb2.CompleteDataUploadRequest.FromString, response_serializer=common_dot_data__pb2.CompleteDataUploadResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('titanium.DataService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class DataService(object):
    """DataService is a utility service that provides operations on data.
    """

    @staticmethod
    def Submitted(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.DataService/Submitted', common_dot_data__pb2.SubmittedRequest.SerializeToString, common_dot_data__pb2.SubmittedResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Export(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.DataService/Export', common_dot_data__pb2.ExportRequest.SerializeToString, common_dot_data__pb2.ExportResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UploadURL(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.DataService/UploadURL', common_dot_data__pb2.UploadURLRequest.SerializeToString, common_dot_gateway__base__pb2.UploadURLResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AuthorizeUpload(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.DataService/AuthorizeUpload', common_dot_data__pb2.UploadURLRequest.SerializeToString, common_dot_data__pb2.UploadAuthorizationResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NotifyUpload(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.DataService/NotifyUpload', common_dot_data__pb2.UploadNotifyRequest.SerializeToString, common_dot_gateway__base__pb2.MessageResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UploadData(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.DataService/UploadData', common_dot_data__pb2.UploadDataRequest.SerializeToString, common_dot_data__pb2.UploadDataResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CompleteDataUpload(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.DataService/CompleteDataUpload', common_dot_data__pb2.CompleteDataUploadRequest.SerializeToString, common_dot_data__pb2.CompleteDataUploadResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)