"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ..common import outliers_pb2 as common_dot_outliers__pb2

class OutliersServiceStub(object):
    """todo change URL to outliers/...

    OutliersService is service that can be used to operate with outliers.

    An outlier is an instrument price that falls outside the standard deviation limit for a particular instrument.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Outliers = channel.unary_unary('/titanium.OutliersService/Outliers', request_serializer=common_dot_outliers__pb2.OutliersRequest.SerializeToString, response_deserializer=common_dot_outliers__pb2.OutliersResponse.FromString)

class OutliersServiceServicer(object):
    """todo change URL to outliers/...

    OutliersService is service that can be used to operate with outliers.

    An outlier is an instrument price that falls outside the standard deviation limit for a particular instrument.
    """

    def Outliers(self, request, context):
        """Outliers returns outliers according to request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_OutliersServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'Outliers': grpc.unary_unary_rpc_method_handler(servicer.Outliers, request_deserializer=common_dot_outliers__pb2.OutliersRequest.FromString, response_serializer=common_dot_outliers__pb2.OutliersResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('titanium.OutliersService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class OutliersService(object):
    """todo change URL to outliers/...

    OutliersService is service that can be used to operate with outliers.

    An outlier is an instrument price that falls outside the standard deviation limit for a particular instrument.
    """

    @staticmethod
    def Outliers(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.OutliersService/Outliers', common_dot_outliers__pb2.OutliersRequest.SerializeToString, common_dot_outliers__pb2.OutliersResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)