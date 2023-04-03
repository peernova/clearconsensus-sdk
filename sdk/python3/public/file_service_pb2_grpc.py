"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ..common import file_service_pb2 as common_dot_file__service__pb2
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2

class FileServiceStub(object):
    """todo change URL path to file

    FileService is a utility service that helps with file operations.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetFilePreview = channel.unary_unary('/titanium.FileService/GetFilePreview', request_serializer=common_dot_file__service__pb2.FileIdentifier.SerializeToString, response_deserializer=common_dot_file__service__pb2.FilePreview.FromString)
        self.ListFiles = channel.unary_unary('/titanium.FileService/ListFiles', request_serializer=common_dot_gateway__base__pb2.ListRequest.SerializeToString, response_deserializer=common_dot_file__service__pb2.FileList.FromString)
        self.SetFileDelimiter = channel.unary_unary('/titanium.FileService/SetFileDelimiter', request_serializer=common_dot_file__service__pb2.SetFileDelimiterRequest.SerializeToString, response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString)
        self.GetFileDelimiter = channel.unary_unary('/titanium.FileService/GetFileDelimiter', request_serializer=common_dot_file__service__pb2.FileIdentifier.SerializeToString, response_deserializer=common_dot_file__service__pb2.FileDelimiterSetting.FromString)
        self.SetFileDescriptor = channel.unary_unary('/titanium.FileService/SetFileDescriptor', request_serializer=common_dot_file__service__pb2.SetFileDescriptorRequest.SerializeToString, response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString)
        self.GetFileDescriptor = channel.unary_unary('/titanium.FileService/GetFileDescriptor', request_serializer=common_dot_file__service__pb2.FileIdentifier.SerializeToString, response_deserializer=common_dot_file__service__pb2.FileDescriptorSetting.FromString)
        self.FileSubmission = channel.unary_unary('/titanium.FileService/FileSubmission', request_serializer=common_dot_file__service__pb2.FileSubmissionRequest.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.MessageResponse.FromString)
        self.FileHistory = channel.unary_unary('/titanium.FileService/FileHistory', request_serializer=common_dot_file__service__pb2.FileHistoryRequest.SerializeToString, response_deserializer=common_dot_file__service__pb2.FileHistoryResponse.FromString)
        self.GetFileExportUrl = channel.unary_unary('/titanium.FileService/GetFileExportUrl', request_serializer=common_dot_file__service__pb2.GetFileExportUrlRequest.SerializeToString, response_deserializer=common_dot_file__service__pb2.GetFileExportUrlResponse.FromString)

class FileServiceServicer(object):
    """todo change URL path to file

    FileService is a utility service that helps with file operations.
    """

    def GetFilePreview(self, request, context):
        """GetFilePreview retrieves a preview of a specified file.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListFiles(self, request, context):
        """ListFiles retrieves a list of files.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetFileDelimiter(self, request, context):
        """SetFileDelimiter sets the delimiter for a specified file.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFileDelimiter(self, request, context):
        """GetFileDelimiter retrieves the delimiter for a specified file.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetFileDescriptor(self, request, context):
        """SetFileDescriptor sets the descriptor for a specified file.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFileDescriptor(self, request, context):
        """GetFileDescriptor retrieves the descriptor for a specified file.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FileSubmission(self, request, context):
        """FileSubmission submits a file for processing.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FileHistory(self, request, context):
        """FileHistory retrieves the history for a specified file.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFileExportUrl(self, request, context):
        """GetFileExportUrl retrieves the export URL for a specified file.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_FileServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'GetFilePreview': grpc.unary_unary_rpc_method_handler(servicer.GetFilePreview, request_deserializer=common_dot_file__service__pb2.FileIdentifier.FromString, response_serializer=common_dot_file__service__pb2.FilePreview.SerializeToString), 'ListFiles': grpc.unary_unary_rpc_method_handler(servicer.ListFiles, request_deserializer=common_dot_gateway__base__pb2.ListRequest.FromString, response_serializer=common_dot_file__service__pb2.FileList.SerializeToString), 'SetFileDelimiter': grpc.unary_unary_rpc_method_handler(servicer.SetFileDelimiter, request_deserializer=common_dot_file__service__pb2.SetFileDelimiterRequest.FromString, response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString), 'GetFileDelimiter': grpc.unary_unary_rpc_method_handler(servicer.GetFileDelimiter, request_deserializer=common_dot_file__service__pb2.FileIdentifier.FromString, response_serializer=common_dot_file__service__pb2.FileDelimiterSetting.SerializeToString), 'SetFileDescriptor': grpc.unary_unary_rpc_method_handler(servicer.SetFileDescriptor, request_deserializer=common_dot_file__service__pb2.SetFileDescriptorRequest.FromString, response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString), 'GetFileDescriptor': grpc.unary_unary_rpc_method_handler(servicer.GetFileDescriptor, request_deserializer=common_dot_file__service__pb2.FileIdentifier.FromString, response_serializer=common_dot_file__service__pb2.FileDescriptorSetting.SerializeToString), 'FileSubmission': grpc.unary_unary_rpc_method_handler(servicer.FileSubmission, request_deserializer=common_dot_file__service__pb2.FileSubmissionRequest.FromString, response_serializer=common_dot_gateway__base__pb2.MessageResponse.SerializeToString), 'FileHistory': grpc.unary_unary_rpc_method_handler(servicer.FileHistory, request_deserializer=common_dot_file__service__pb2.FileHistoryRequest.FromString, response_serializer=common_dot_file__service__pb2.FileHistoryResponse.SerializeToString), 'GetFileExportUrl': grpc.unary_unary_rpc_method_handler(servicer.GetFileExportUrl, request_deserializer=common_dot_file__service__pb2.GetFileExportUrlRequest.FromString, response_serializer=common_dot_file__service__pb2.GetFileExportUrlResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('titanium.FileService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class FileService(object):
    """todo change URL path to file

    FileService is a utility service that helps with file operations.
    """

    @staticmethod
    def GetFilePreview(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.FileService/GetFilePreview', common_dot_file__service__pb2.FileIdentifier.SerializeToString, common_dot_file__service__pb2.FilePreview.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListFiles(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.FileService/ListFiles', common_dot_gateway__base__pb2.ListRequest.SerializeToString, common_dot_file__service__pb2.FileList.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetFileDelimiter(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.FileService/SetFileDelimiter', common_dot_file__service__pb2.SetFileDelimiterRequest.SerializeToString, google_dot_protobuf_dot_empty__pb2.Empty.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetFileDelimiter(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.FileService/GetFileDelimiter', common_dot_file__service__pb2.FileIdentifier.SerializeToString, common_dot_file__service__pb2.FileDelimiterSetting.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetFileDescriptor(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.FileService/SetFileDescriptor', common_dot_file__service__pb2.SetFileDescriptorRequest.SerializeToString, google_dot_protobuf_dot_empty__pb2.Empty.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetFileDescriptor(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.FileService/GetFileDescriptor', common_dot_file__service__pb2.FileIdentifier.SerializeToString, common_dot_file__service__pb2.FileDescriptorSetting.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FileSubmission(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.FileService/FileSubmission', common_dot_file__service__pb2.FileSubmissionRequest.SerializeToString, common_dot_gateway__base__pb2.MessageResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FileHistory(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.FileService/FileHistory', common_dot_file__service__pb2.FileHistoryRequest.SerializeToString, common_dot_file__service__pb2.FileHistoryResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetFileExportUrl(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.FileService/GetFileExportUrl', common_dot_file__service__pb2.GetFileExportUrlRequest.SerializeToString, common_dot_file__service__pb2.GetFileExportUrlResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)