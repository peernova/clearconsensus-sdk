"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ..common import market_pb2 as common_dot_market__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2

class MarketServiceStub(object):
    """MarketService is used to operate with information related to current market status.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.MarketSnapTime = channel.unary_unary('/titanium.MarketService/MarketSnapTime', request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString, response_deserializer=common_dot_market__pb2.MarketSnapTimeResponse.FromString)

class MarketServiceServicer(object):
    """MarketService is used to operate with information related to current market status.
    """

    def MarketSnapTime(self, request, context):
        """MarketSnapTime returns time for which the prices(calculated in consensus) are valid.(Time of market closing)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_MarketServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'MarketSnapTime': grpc.unary_unary_rpc_method_handler(servicer.MarketSnapTime, request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString, response_serializer=common_dot_market__pb2.MarketSnapTimeResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('titanium.MarketService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class MarketService(object):
    """MarketService is used to operate with information related to current market status.
    """

    @staticmethod
    def MarketSnapTime(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.MarketService/MarketSnapTime', google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString, common_dot_market__pb2.MarketSnapTimeResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)