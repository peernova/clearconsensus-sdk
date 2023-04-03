"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ..common import assets_pb2 as common_dot_assets__pb2
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2
from ..private import assets_private_service_pb2 as private_dot_assets__private__service__pb2

class AssetsPrivateServiceStub(object):
    """todo remove operator from URL paths

    AssetsServicePrivate is used to operate with assets.

    Asset is a resource with economic value.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddAsset = channel.unary_unary('/titanium.AssetsPrivateService/AddAsset', request_serializer=private_dot_assets__private__service__pb2.AddAssetRequest.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.MessageResponse.FromString)
        self.RecentAssets = channel.unary_unary('/titanium.AssetsPrivateService/RecentAssets', request_serializer=common_dot_assets__pb2.RecentAssetsRequest.SerializeToString, response_deserializer=common_dot_assets__pb2.RecentAssetsResponse.FromString)
        self.Assets = channel.unary_unary('/titanium.AssetsPrivateService/Assets', request_serializer=common_dot_assets__pb2.AssetsRequest.SerializeToString, response_deserializer=common_dot_assets__pb2.AssetsResponse.FromString)

class AssetsPrivateServiceServicer(object):
    """todo remove operator from URL paths

    AssetsServicePrivate is used to operate with assets.

    Asset is a resource with economic value.
    """

    def AddAsset(self, request, context):
        """AddAsset adds asset to the system.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RecentAssets(self, request, context):
        """todo delete and use the same method in public service
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Assets(self, request, context):
        """todo delete and use the same method in public service
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_AssetsPrivateServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'AddAsset': grpc.unary_unary_rpc_method_handler(servicer.AddAsset, request_deserializer=private_dot_assets__private__service__pb2.AddAssetRequest.FromString, response_serializer=common_dot_gateway__base__pb2.MessageResponse.SerializeToString), 'RecentAssets': grpc.unary_unary_rpc_method_handler(servicer.RecentAssets, request_deserializer=common_dot_assets__pb2.RecentAssetsRequest.FromString, response_serializer=common_dot_assets__pb2.RecentAssetsResponse.SerializeToString), 'Assets': grpc.unary_unary_rpc_method_handler(servicer.Assets, request_deserializer=common_dot_assets__pb2.AssetsRequest.FromString, response_serializer=common_dot_assets__pb2.AssetsResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('titanium.AssetsPrivateService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class AssetsPrivateService(object):
    """todo remove operator from URL paths

    AssetsServicePrivate is used to operate with assets.

    Asset is a resource with economic value.
    """

    @staticmethod
    def AddAsset(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.AssetsPrivateService/AddAsset', private_dot_assets__private__service__pb2.AddAssetRequest.SerializeToString, common_dot_gateway__base__pb2.MessageResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RecentAssets(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.AssetsPrivateService/RecentAssets', common_dot_assets__pb2.RecentAssetsRequest.SerializeToString, common_dot_assets__pb2.RecentAssetsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Assets(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.AssetsPrivateService/Assets', common_dot_assets__pb2.AssetsRequest.SerializeToString, common_dot_assets__pb2.AssetsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)