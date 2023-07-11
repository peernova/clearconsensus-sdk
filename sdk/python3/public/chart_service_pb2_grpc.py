"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ..public import chart_service_pb2 as public_dot_chart__service__pb2

class ChartServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.getChartData = channel.unary_unary('/titanium.ChartService/getChartData', request_serializer=public_dot_chart__service__pb2.GetChartDataRequest.SerializeToString, response_deserializer=public_dot_chart__service__pb2.GetChartDataResponse.FromString)
        self.getTableData = channel.unary_unary('/titanium.ChartService/getTableData', request_serializer=public_dot_chart__service__pb2.GetChartDataRequest.SerializeToString, response_deserializer=public_dot_chart__service__pb2.GetTableResponse.FromString)

class ChartServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def getChartData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getTableData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_ChartServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'getChartData': grpc.unary_unary_rpc_method_handler(servicer.getChartData, request_deserializer=public_dot_chart__service__pb2.GetChartDataRequest.FromString, response_serializer=public_dot_chart__service__pb2.GetChartDataResponse.SerializeToString), 'getTableData': grpc.unary_unary_rpc_method_handler(servicer.getTableData, request_deserializer=public_dot_chart__service__pb2.GetChartDataRequest.FromString, response_serializer=public_dot_chart__service__pb2.GetTableResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('titanium.ChartService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class ChartService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def getChartData(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.ChartService/getChartData', public_dot_chart__service__pb2.GetChartDataRequest.SerializeToString, public_dot_chart__service__pb2.GetChartDataResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getTableData(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.ChartService/getTableData', public_dot_chart__service__pb2.GetChartDataRequest.SerializeToString, public_dot_chart__service__pb2.GetTableResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)