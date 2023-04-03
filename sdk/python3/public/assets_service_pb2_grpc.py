"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ..common import assets_pb2 as common_dot_assets__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2

class AssetsServiceStub(object):
    """AssetsService is used to operate with assets.
    Asset is a resource with economic value.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RecentAssets = channel.unary_unary('/titanium.AssetsService/RecentAssets', request_serializer=common_dot_assets__pb2.RecentAssetsRequest.SerializeToString, response_deserializer=common_dot_assets__pb2.RecentAssetsResponse.FromString)
        self.AssetsList = channel.unary_unary('/titanium.AssetsService/AssetsList', request_serializer=common_dot_assets__pb2.AssetsListRequest.SerializeToString, response_deserializer=common_dot_assets__pb2.AssetsListResponse.FromString)
        self.Assets = channel.unary_unary('/titanium.AssetsService/Assets', request_serializer=common_dot_assets__pb2.AssetsRequest.SerializeToString, response_deserializer=common_dot_assets__pb2.AssetsResponse.FromString)
        self.SupportedAssets = channel.unary_unary('/titanium.AssetsService/SupportedAssets', request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString, response_deserializer=common_dot_assets__pb2.AssetsListResponse.FromString)

class AssetsServiceServicer(object):
    """AssetsService is used to operate with assets.
    Asset is a resource with economic value.
    """

    def RecentAssets(self, request, context):
        """RecentAssets returns recent added assets according to request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AssetsList(self, request, context):
        """AssetsList return list of assets according to request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Assets(self, request, context):
        """Assets returns asset from the system according to request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SupportedAssets(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_AssetsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'RecentAssets': grpc.unary_unary_rpc_method_handler(servicer.RecentAssets, request_deserializer=common_dot_assets__pb2.RecentAssetsRequest.FromString, response_serializer=common_dot_assets__pb2.RecentAssetsResponse.SerializeToString), 'AssetsList': grpc.unary_unary_rpc_method_handler(servicer.AssetsList, request_deserializer=common_dot_assets__pb2.AssetsListRequest.FromString, response_serializer=common_dot_assets__pb2.AssetsListResponse.SerializeToString), 'Assets': grpc.unary_unary_rpc_method_handler(servicer.Assets, request_deserializer=common_dot_assets__pb2.AssetsRequest.FromString, response_serializer=common_dot_assets__pb2.AssetsResponse.SerializeToString), 'SupportedAssets': grpc.unary_unary_rpc_method_handler(servicer.SupportedAssets, request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString, response_serializer=common_dot_assets__pb2.AssetsListResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('titanium.AssetsService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class AssetsService(object):
    """AssetsService is used to operate with assets.
    Asset is a resource with economic value.
    """

    @staticmethod
    def RecentAssets(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.AssetsService/RecentAssets', common_dot_assets__pb2.RecentAssetsRequest.SerializeToString, common_dot_assets__pb2.RecentAssetsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AssetsList(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.AssetsService/AssetsList', common_dot_assets__pb2.AssetsListRequest.SerializeToString, common_dot_assets__pb2.AssetsListResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Assets(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.AssetsService/Assets', common_dot_assets__pb2.AssetsRequest.SerializeToString, common_dot_assets__pb2.AssetsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SupportedAssets(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.AssetsService/SupportedAssets', google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString, common_dot_assets__pb2.AssetsListResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)