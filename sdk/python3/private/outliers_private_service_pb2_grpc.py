"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ..common import outliers_pb2 as common_dot_outliers__pb2
from ..private import outliers_private_service_pb2 as private_dot_outliers__private__service__pb2

class OutliersPrivateServiceStub(object):
    """todo remove '/operator' from URL paths make it - '/outliers/...'

    OutliersPrivateService is service with private methods that can be used to operate with outliers.

    An outlier is an instrument price that falls outside the standard deviation limit for a particular instrument.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.OperatorOutliers = channel.unary_unary('/titanium.OutliersPrivateService/OperatorOutliers', request_serializer=private_dot_outliers__private__service__pb2.OperatorOutliersRequest.SerializeToString, response_deserializer=private_dot_outliers__private__service__pb2.OperatorOutliersResponse.FromString)
        self.Outliers = channel.unary_unary('/titanium.OutliersPrivateService/Outliers', request_serializer=common_dot_outliers__pb2.OutliersRequest.SerializeToString, response_deserializer=common_dot_outliers__pb2.OutliersResponse.FromString)

class OutliersPrivateServiceServicer(object):
    """todo remove '/operator' from URL paths make it - '/outliers/...'

    OutliersPrivateService is service with private methods that can be used to operate with outliers.

    An outlier is an instrument price that falls outside the standard deviation limit for a particular instrument.
    """

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

def add_OutliersPrivateServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'OperatorOutliers': grpc.unary_unary_rpc_method_handler(servicer.OperatorOutliers, request_deserializer=private_dot_outliers__private__service__pb2.OperatorOutliersRequest.FromString, response_serializer=private_dot_outliers__private__service__pb2.OperatorOutliersResponse.SerializeToString), 'Outliers': grpc.unary_unary_rpc_method_handler(servicer.Outliers, request_deserializer=common_dot_outliers__pb2.OutliersRequest.FromString, response_serializer=common_dot_outliers__pb2.OutliersResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('titanium.OutliersPrivateService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class OutliersPrivateService(object):
    """todo remove '/operator' from URL paths make it - '/outliers/...'

    OutliersPrivateService is service with private methods that can be used to operate with outliers.

    An outlier is an instrument price that falls outside the standard deviation limit for a particular instrument.
    """

    @staticmethod
    def OperatorOutliers(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.OutliersPrivateService/OperatorOutliers', private_dot_outliers__private__service__pb2.OperatorOutliersRequest.SerializeToString, private_dot_outliers__private__service__pb2.OperatorOutliersResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Outliers(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.OutliersPrivateService/Outliers', common_dot_outliers__pb2.OutliersRequest.SerializeToString, common_dot_outliers__pb2.OutliersResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)