"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ..common import popup_pb2 as common_dot_popup__pb2

class PopUpServiceStub(object):
    """PopUpService is service that can be used for operating with popups.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.PopUpView = channel.unary_unary('/titanium.PopUpService/PopUpView', request_serializer=common_dot_popup__pb2.PopUpViewRequest.SerializeToString, response_deserializer=common_dot_popup__pb2.PopUpViewResponse.FromString)

class PopUpServiceServicer(object):
    """PopUpService is service that can be used for operating with popups.
    """

    def PopUpView(self, request, context):
        """PopUpView returns information according to request for the popup view.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_PopUpServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'PopUpView': grpc.unary_unary_rpc_method_handler(servicer.PopUpView, request_deserializer=common_dot_popup__pb2.PopUpViewRequest.FromString, response_serializer=common_dot_popup__pb2.PopUpViewResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('titanium.PopUpService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class PopUpService(object):
    """PopUpService is service that can be used for operating with popups.
    """

    @staticmethod
    def PopUpView(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.PopUpService/PopUpView', common_dot_popup__pb2.PopUpViewRequest.SerializeToString, common_dot_popup__pb2.PopUpViewResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)