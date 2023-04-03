"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ..common import analytics_pb2 as common_dot_analytics__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2

class AnalyticsControllerStub(object):
    """AnalyticsController is service that can provide analytics related to consensuses, errors in data processing and etc..
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.FindDataQualityErrors = channel.unary_unary('/titanium.AnalyticsController/FindDataQualityErrors', request_serializer=common_dot_analytics__pb2.GenericChartMetadataDataQuality.SerializeToString, response_deserializer=common_dot_analytics__pb2.GenericChartMetadataDataQualityResponse.FromString)
        self.GetAllDataQualityErrors = channel.unary_unary('/titanium.AnalyticsController/GetAllDataQualityErrors', request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString, response_deserializer=common_dot_analytics__pb2.GenericChartMetadataDataQualityResponse.FromString)
        self.FindConsensusAnalytics = channel.unary_unary('/titanium.AnalyticsController/FindConsensusAnalytics', request_serializer=common_dot_analytics__pb2.GenericChartMetadataDataQuality.SerializeToString, response_deserializer=common_dot_analytics__pb2.GenericChartMetadataDataQualityResponse.FromString)
        self.GetAllConsensusAnalytics = channel.unary_unary('/titanium.AnalyticsController/GetAllConsensusAnalytics', request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString, response_deserializer=common_dot_analytics__pb2.GenericChartMetadataDataQualityResponse.FromString)
        self.GetPredefinedFilter = channel.unary_unary('/titanium.AnalyticsController/GetPredefinedFilter', request_serializer=common_dot_analytics__pb2.GetPredefinedFiltersRequest.SerializeToString, response_deserializer=common_dot_analytics__pb2.GetPredefinedFiltersResponse.FromString)
        self.GetHistogram = channel.unary_unary('/titanium.AnalyticsController/GetHistogram', request_serializer=common_dot_analytics__pb2.HistogramRequest.SerializeToString, response_deserializer=common_dot_analytics__pb2.HistogramResponse.FromString)

class AnalyticsControllerServicer(object):
    """AnalyticsController is service that can provide analytics related to consensuses, errors in data processing and etc..
    """

    def FindDataQualityErrors(self, request, context):
        """FindDataQualityErrors returns data quality errors according to request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAllDataQualityErrors(self, request, context):
        """GetAllDataQualityErrors returns all existing data quality errors in the system.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FindConsensusAnalytics(self, request, context):
        """FindConsensusAnalytics returns analytics related to specific consensus according to request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAllConsensusAnalytics(self, request, context):
        """GetAllConsensusAnalytics returns analytics related to all consensuses.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPredefinedFilter(self, request, context):
        """GetPredefinedFilter returns pre defined filters according to request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetHistogram(self, request, context):
        """GetHistogram returns analytics(submission and consensus) represented by histogram according to request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_AnalyticsControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {'FindDataQualityErrors': grpc.unary_unary_rpc_method_handler(servicer.FindDataQualityErrors, request_deserializer=common_dot_analytics__pb2.GenericChartMetadataDataQuality.FromString, response_serializer=common_dot_analytics__pb2.GenericChartMetadataDataQualityResponse.SerializeToString), 'GetAllDataQualityErrors': grpc.unary_unary_rpc_method_handler(servicer.GetAllDataQualityErrors, request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString, response_serializer=common_dot_analytics__pb2.GenericChartMetadataDataQualityResponse.SerializeToString), 'FindConsensusAnalytics': grpc.unary_unary_rpc_method_handler(servicer.FindConsensusAnalytics, request_deserializer=common_dot_analytics__pb2.GenericChartMetadataDataQuality.FromString, response_serializer=common_dot_analytics__pb2.GenericChartMetadataDataQualityResponse.SerializeToString), 'GetAllConsensusAnalytics': grpc.unary_unary_rpc_method_handler(servicer.GetAllConsensusAnalytics, request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString, response_serializer=common_dot_analytics__pb2.GenericChartMetadataDataQualityResponse.SerializeToString), 'GetPredefinedFilter': grpc.unary_unary_rpc_method_handler(servicer.GetPredefinedFilter, request_deserializer=common_dot_analytics__pb2.GetPredefinedFiltersRequest.FromString, response_serializer=common_dot_analytics__pb2.GetPredefinedFiltersResponse.SerializeToString), 'GetHistogram': grpc.unary_unary_rpc_method_handler(servicer.GetHistogram, request_deserializer=common_dot_analytics__pb2.HistogramRequest.FromString, response_serializer=common_dot_analytics__pb2.HistogramResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('titanium.AnalyticsController', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class AnalyticsController(object):
    """AnalyticsController is service that can provide analytics related to consensuses, errors in data processing and etc..
    """

    @staticmethod
    def FindDataQualityErrors(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.AnalyticsController/FindDataQualityErrors', common_dot_analytics__pb2.GenericChartMetadataDataQuality.SerializeToString, common_dot_analytics__pb2.GenericChartMetadataDataQualityResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAllDataQualityErrors(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.AnalyticsController/GetAllDataQualityErrors', google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString, common_dot_analytics__pb2.GenericChartMetadataDataQualityResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FindConsensusAnalytics(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.AnalyticsController/FindConsensusAnalytics', common_dot_analytics__pb2.GenericChartMetadataDataQuality.SerializeToString, common_dot_analytics__pb2.GenericChartMetadataDataQualityResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAllConsensusAnalytics(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.AnalyticsController/GetAllConsensusAnalytics', google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString, common_dot_analytics__pb2.GenericChartMetadataDataQualityResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPredefinedFilter(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.AnalyticsController/GetPredefinedFilter', common_dot_analytics__pb2.GetPredefinedFiltersRequest.SerializeToString, common_dot_analytics__pb2.GetPredefinedFiltersResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetHistogram(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.AnalyticsController/GetHistogram', common_dot_analytics__pb2.HistogramRequest.SerializeToString, common_dot_analytics__pb2.HistogramResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)