"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ..common import assets_pb2 as common_dot_assets__pb2
from ..common import data_pb2 as common_dot_data__pb2
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2
from ..common import outliers_pb2 as common_dot_outliers__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from ..public import operator_service_pb2 as public_dot_operator__service__pb2

class OperatorServicePrivateStub(object):
    """OperatorServicePrivate is service with private methods that can be used only by operator.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddClient = channel.unary_unary('/titanium.OperatorServicePrivate/AddClient', request_serializer=public_dot_operator__service__pb2.ClientName.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.MessageResponse.FromString)
        self.ListClients = channel.unary_unary('/titanium.OperatorServicePrivate/ListClients', request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString, response_deserializer=public_dot_operator__service__pb2.ListClientsResponse.FromString)
        self.EvpStatuses = channel.unary_unary('/titanium.OperatorServicePrivate/EvpStatuses', request_serializer=public_dot_operator__service__pb2.EvpStatusesRequest.SerializeToString, response_deserializer=public_dot_operator__service__pb2.EvpStatusesResponse.FromString)
        self.UploadEVP = channel.unary_unary('/titanium.OperatorServicePrivate/UploadEVP', request_serializer=public_dot_operator__service__pb2.UploadEVPRequest.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.UploadURLResponse.FromString)
        self.UploadDTCC = channel.unary_unary('/titanium.OperatorServicePrivate/UploadDTCC', request_serializer=public_dot_operator__service__pb2.UploadDTCCRequest.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.UploadURLResponse.FromString)
        self.OperatorOutliers = channel.unary_unary('/titanium.OperatorServicePrivate/OperatorOutliers', request_serializer=public_dot_operator__service__pb2.OperatorOutliersRequest.SerializeToString, response_deserializer=public_dot_operator__service__pb2.OperatorOutliersResponse.FromString)
        self.Outliers = channel.unary_unary('/titanium.OperatorServicePrivate/Outliers', request_serializer=common_dot_outliers__pb2.OutliersRequest.SerializeToString, response_deserializer=common_dot_outliers__pb2.OutliersResponse.FromString)
        self.CreateSupportedFields = channel.unary_unary('/titanium.OperatorServicePrivate/CreateSupportedFields', request_serializer=public_dot_operator__service__pb2.SupportedFieldsValues.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.MessageResponse.FromString)
        self.AddSupportedFields = channel.unary_unary('/titanium.OperatorServicePrivate/AddSupportedFields', request_serializer=public_dot_operator__service__pb2.SupportedFieldsValues.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.MessageResponse.FromString)
        self.DeleteSupportedFields = channel.unary_unary('/titanium.OperatorServicePrivate/DeleteSupportedFields', request_serializer=public_dot_operator__service__pb2.SupportedFieldsValues.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.MessageResponse.FromString)
        self.ExportReport = channel.unary_unary('/titanium.OperatorServicePrivate/ExportReport', request_serializer=common_dot_data__pb2.ExportReportRequest.SerializeToString, response_deserializer=common_dot_data__pb2.ExportResponse.FromString)
        self.AddAsset = channel.unary_unary('/titanium.OperatorServicePrivate/AddAsset', request_serializer=public_dot_operator__service__pb2.AddAssetRequest.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.MessageResponse.FromString)
        self.RecentAssets = channel.unary_unary('/titanium.OperatorServicePrivate/RecentAssets', request_serializer=common_dot_assets__pb2.RecentAssetsRequest.SerializeToString, response_deserializer=common_dot_assets__pb2.RecentAssetsResponse.FromString)
        self.Assets = channel.unary_unary('/titanium.OperatorServicePrivate/Assets', request_serializer=common_dot_assets__pb2.AssetsRequest.SerializeToString, response_deserializer=common_dot_assets__pb2.AssetsResponse.FromString)

class OperatorServicePrivateServicer(object):
    """OperatorServicePrivate is service with private methods that can be used only by operator.
    """

    def AddClient(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListClients(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EvpStatuses(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UploadEVP(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UploadDTCC(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def OperatorOutliers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Outliers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

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

    def ExportReport(self, request, context):
        """ExportReport returns pre signed s3 urls which can be used for export report(and compression type)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddAsset(self, request, context):
        """AddAsset adds asset to the system.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RecentAssets(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Assets(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_OperatorServicePrivateServicer_to_server(servicer, server):
    rpc_method_handlers = {'AddClient': grpc.unary_unary_rpc_method_handler(servicer.AddClient, request_deserializer=public_dot_operator__service__pb2.ClientName.FromString, response_serializer=common_dot_gateway__base__pb2.MessageResponse.SerializeToString), 'ListClients': grpc.unary_unary_rpc_method_handler(servicer.ListClients, request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString, response_serializer=public_dot_operator__service__pb2.ListClientsResponse.SerializeToString), 'EvpStatuses': grpc.unary_unary_rpc_method_handler(servicer.EvpStatuses, request_deserializer=public_dot_operator__service__pb2.EvpStatusesRequest.FromString, response_serializer=public_dot_operator__service__pb2.EvpStatusesResponse.SerializeToString), 'UploadEVP': grpc.unary_unary_rpc_method_handler(servicer.UploadEVP, request_deserializer=public_dot_operator__service__pb2.UploadEVPRequest.FromString, response_serializer=common_dot_gateway__base__pb2.UploadURLResponse.SerializeToString), 'UploadDTCC': grpc.unary_unary_rpc_method_handler(servicer.UploadDTCC, request_deserializer=public_dot_operator__service__pb2.UploadDTCCRequest.FromString, response_serializer=common_dot_gateway__base__pb2.UploadURLResponse.SerializeToString), 'OperatorOutliers': grpc.unary_unary_rpc_method_handler(servicer.OperatorOutliers, request_deserializer=public_dot_operator__service__pb2.OperatorOutliersRequest.FromString, response_serializer=public_dot_operator__service__pb2.OperatorOutliersResponse.SerializeToString), 'Outliers': grpc.unary_unary_rpc_method_handler(servicer.Outliers, request_deserializer=common_dot_outliers__pb2.OutliersRequest.FromString, response_serializer=common_dot_outliers__pb2.OutliersResponse.SerializeToString), 'CreateSupportedFields': grpc.unary_unary_rpc_method_handler(servicer.CreateSupportedFields, request_deserializer=public_dot_operator__service__pb2.SupportedFieldsValues.FromString, response_serializer=common_dot_gateway__base__pb2.MessageResponse.SerializeToString), 'AddSupportedFields': grpc.unary_unary_rpc_method_handler(servicer.AddSupportedFields, request_deserializer=public_dot_operator__service__pb2.SupportedFieldsValues.FromString, response_serializer=common_dot_gateway__base__pb2.MessageResponse.SerializeToString), 'DeleteSupportedFields': grpc.unary_unary_rpc_method_handler(servicer.DeleteSupportedFields, request_deserializer=public_dot_operator__service__pb2.SupportedFieldsValues.FromString, response_serializer=common_dot_gateway__base__pb2.MessageResponse.SerializeToString), 'ExportReport': grpc.unary_unary_rpc_method_handler(servicer.ExportReport, request_deserializer=common_dot_data__pb2.ExportReportRequest.FromString, response_serializer=common_dot_data__pb2.ExportResponse.SerializeToString), 'AddAsset': grpc.unary_unary_rpc_method_handler(servicer.AddAsset, request_deserializer=public_dot_operator__service__pb2.AddAssetRequest.FromString, response_serializer=common_dot_gateway__base__pb2.MessageResponse.SerializeToString), 'RecentAssets': grpc.unary_unary_rpc_method_handler(servicer.RecentAssets, request_deserializer=common_dot_assets__pb2.RecentAssetsRequest.FromString, response_serializer=common_dot_assets__pb2.RecentAssetsResponse.SerializeToString), 'Assets': grpc.unary_unary_rpc_method_handler(servicer.Assets, request_deserializer=common_dot_assets__pb2.AssetsRequest.FromString, response_serializer=common_dot_assets__pb2.AssetsResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('titanium.OperatorServicePrivate', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class OperatorServicePrivate(object):
    """OperatorServicePrivate is service with private methods that can be used only by operator.
    """

    @staticmethod
    def AddClient(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.OperatorServicePrivate/AddClient', public_dot_operator__service__pb2.ClientName.SerializeToString, common_dot_gateway__base__pb2.MessageResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListClients(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.OperatorServicePrivate/ListClients', google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString, public_dot_operator__service__pb2.ListClientsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EvpStatuses(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.OperatorServicePrivate/EvpStatuses', public_dot_operator__service__pb2.EvpStatusesRequest.SerializeToString, public_dot_operator__service__pb2.EvpStatusesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UploadEVP(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.OperatorServicePrivate/UploadEVP', public_dot_operator__service__pb2.UploadEVPRequest.SerializeToString, common_dot_gateway__base__pb2.UploadURLResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UploadDTCC(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.OperatorServicePrivate/UploadDTCC', public_dot_operator__service__pb2.UploadDTCCRequest.SerializeToString, common_dot_gateway__base__pb2.UploadURLResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def OperatorOutliers(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.OperatorServicePrivate/OperatorOutliers', public_dot_operator__service__pb2.OperatorOutliersRequest.SerializeToString, public_dot_operator__service__pb2.OperatorOutliersResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Outliers(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.OperatorServicePrivate/Outliers', common_dot_outliers__pb2.OutliersRequest.SerializeToString, common_dot_outliers__pb2.OutliersResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateSupportedFields(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.OperatorServicePrivate/CreateSupportedFields', public_dot_operator__service__pb2.SupportedFieldsValues.SerializeToString, common_dot_gateway__base__pb2.MessageResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddSupportedFields(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.OperatorServicePrivate/AddSupportedFields', public_dot_operator__service__pb2.SupportedFieldsValues.SerializeToString, common_dot_gateway__base__pb2.MessageResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteSupportedFields(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.OperatorServicePrivate/DeleteSupportedFields', public_dot_operator__service__pb2.SupportedFieldsValues.SerializeToString, common_dot_gateway__base__pb2.MessageResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ExportReport(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.OperatorServicePrivate/ExportReport', common_dot_data__pb2.ExportReportRequest.SerializeToString, common_dot_data__pb2.ExportResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddAsset(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.OperatorServicePrivate/AddAsset', public_dot_operator__service__pb2.AddAssetRequest.SerializeToString, common_dot_gateway__base__pb2.MessageResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RecentAssets(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.OperatorServicePrivate/RecentAssets', common_dot_assets__pb2.RecentAssetsRequest.SerializeToString, common_dot_assets__pb2.RecentAssetsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Assets(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.OperatorServicePrivate/Assets', common_dot_assets__pb2.AssetsRequest.SerializeToString, common_dot_assets__pb2.AssetsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)