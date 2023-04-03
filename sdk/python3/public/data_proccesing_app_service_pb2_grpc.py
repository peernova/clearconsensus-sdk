"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ..common import data_proccesing_app_pb2 as common_dot_data__proccesing__app__pb2

class DataProcessingAppServiceStub(object):
    """DataProcessingAppService is service that start processing of data uploaded by a dealer.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RunDataProcessingApp = channel.unary_unary('/titanium.DataProcessingAppService/RunDataProcessingApp', request_serializer=common_dot_data__proccesing__app__pb2.RunDataProcessingAppRequest.SerializeToString, response_deserializer=common_dot_data__proccesing__app__pb2.RunDataProcessingAppResponse.FromString)

class DataProcessingAppServiceServicer(object):
    """DataProcessingAppService is service that start processing of data uploaded by a dealer.
    """

    def RunDataProcessingApp(self, request, context):
        """RunDataProcessingApp triggers jobs that are responsible to processing of received data.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_DataProcessingAppServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'RunDataProcessingApp': grpc.unary_unary_rpc_method_handler(servicer.RunDataProcessingApp, request_deserializer=common_dot_data__proccesing__app__pb2.RunDataProcessingAppRequest.FromString, response_serializer=common_dot_data__proccesing__app__pb2.RunDataProcessingAppResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('titanium.DataProcessingAppService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class DataProcessingAppService(object):
    """DataProcessingAppService is service that start processing of data uploaded by a dealer.
    """

    @staticmethod
    def RunDataProcessingApp(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.DataProcessingAppService/RunDataProcessingApp', common_dot_data__proccesing__app__pb2.RunDataProcessingAppRequest.SerializeToString, common_dot_data__proccesing__app__pb2.RunDataProcessingAppResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)