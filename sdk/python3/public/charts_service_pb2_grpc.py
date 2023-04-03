"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ..common import charts_pb2 as common_dot_charts__pb2

class ChartsServiceStub(object):
    """ChartsService is used to operate with charts
    Charts is visual representation of the data.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Charts = channel.unary_unary('/titanium.ChartsService/Charts', request_serializer=common_dot_charts__pb2.ChartsRequest.SerializeToString, response_deserializer=common_dot_charts__pb2.ChartsResponse.FromString)
        self.ChartsCurrencies = channel.unary_unary('/titanium.ChartsService/ChartsCurrencies', request_serializer=common_dot_charts__pb2.ChartsCurrenciesRequest.SerializeToString, response_deserializer=common_dot_charts__pb2.ChartsCurrenciesResponse.FromString)

class ChartsServiceServicer(object):
    """ChartsService is used to operate with charts
    Charts is visual representation of the data.
    """

    def Charts(self, request, context):
        """Charts returns information about specific chart related to the specific asset.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ChartsCurrencies(self, request, context):
        """ChartsCurrencies returns information about the chart related to specific currency pair.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_ChartsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'Charts': grpc.unary_unary_rpc_method_handler(servicer.Charts, request_deserializer=common_dot_charts__pb2.ChartsRequest.FromString, response_serializer=common_dot_charts__pb2.ChartsResponse.SerializeToString), 'ChartsCurrencies': grpc.unary_unary_rpc_method_handler(servicer.ChartsCurrencies, request_deserializer=common_dot_charts__pb2.ChartsCurrenciesRequest.FromString, response_serializer=common_dot_charts__pb2.ChartsCurrenciesResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('titanium.ChartsService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class ChartsService(object):
    """ChartsService is used to operate with charts
    Charts is visual representation of the data.
    """

    @staticmethod
    def Charts(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.ChartsService/Charts', common_dot_charts__pb2.ChartsRequest.SerializeToString, common_dot_charts__pb2.ChartsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ChartsCurrencies(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.ChartsService/ChartsCurrencies', common_dot_charts__pb2.ChartsCurrenciesRequest.SerializeToString, common_dot_charts__pb2.ChartsCurrenciesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)