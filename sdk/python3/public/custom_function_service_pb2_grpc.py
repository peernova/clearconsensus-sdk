"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ..common import custom_function_pb2 as common_dot_custom__function__pb2
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2

class CustomFunctionServiceStub(object):
    """CustomFunctionService is service that can be used to operate with custom function entity.

    Custom function can be created by user for customizing processes (validation, normalization, mapping)
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddCustomFunction = channel.unary_unary('/titanium.CustomFunctionService/AddCustomFunction', request_serializer=common_dot_custom__function__pb2.CustomFunction.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.AcknowledgeResponse.FromString)
        self.GetCustomFunction = channel.unary_unary('/titanium.CustomFunctionService/GetCustomFunction', request_serializer=common_dot_custom__function__pb2.CustomFunctionGetDefinition.SerializeToString, response_deserializer=common_dot_custom__function__pb2.CustomFunctionDefinitionResponse.FromString)
        self.ListCustomFunctions = channel.unary_unary('/titanium.CustomFunctionService/ListCustomFunctions', request_serializer=common_dot_custom__function__pb2.ListCustomFunctionRequest.SerializeToString, response_deserializer=common_dot_custom__function__pb2.ListCustomFunctionResponse.FromString)
        self.ListCustomFunctionVersions = channel.unary_unary('/titanium.CustomFunctionService/ListCustomFunctionVersions', request_serializer=common_dot_gateway__base__pb2.GetDefinition.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.ListVersionResponse.FromString)

class CustomFunctionServiceServicer(object):
    """CustomFunctionService is service that can be used to operate with custom function entity.

    Custom function can be created by user for customizing processes (validation, normalization, mapping)
    """

    def AddCustomFunction(self, request, context):
        """AddCustomFunction allows the user to create a new custom function by sending a CustomFunction message. It returns an AcknowledgeResponse indicating whether the custom function was successfully added or not.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCustomFunction(self, request, context):
        """GetCustomFunction retrieves the definition of a specific custom function. The custom function is specified in the CustomFunctionGetDefinition message, which includes its ID and scope. The method returns a CustomFunctionDefinitionResponse that contains either the custom function definition or an error.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListCustomFunctions(self, request, context):
        """ListCustomFunctions lists all the custom functions that match the specified criteria. The criteria are defined in the ListCustomFunctionRequest message, which includes the descriptor name and the type of the custom function descriptor. The method returns a ListCustomFunctionResponse that contains either a list of custom functions or an error.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListCustomFunctionVersions(self, request, context):
        """ListCustomFunctionVersions lists all the versions of a specific custom function. The custom function is specified in the GetDefinition message, which includes its ID and scope. The method returns a ListVersionResponse that contains either a list of versions or an error.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_CustomFunctionServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'AddCustomFunction': grpc.unary_unary_rpc_method_handler(servicer.AddCustomFunction, request_deserializer=common_dot_custom__function__pb2.CustomFunction.FromString, response_serializer=common_dot_gateway__base__pb2.AcknowledgeResponse.SerializeToString), 'GetCustomFunction': grpc.unary_unary_rpc_method_handler(servicer.GetCustomFunction, request_deserializer=common_dot_custom__function__pb2.CustomFunctionGetDefinition.FromString, response_serializer=common_dot_custom__function__pb2.CustomFunctionDefinitionResponse.SerializeToString), 'ListCustomFunctions': grpc.unary_unary_rpc_method_handler(servicer.ListCustomFunctions, request_deserializer=common_dot_custom__function__pb2.ListCustomFunctionRequest.FromString, response_serializer=common_dot_custom__function__pb2.ListCustomFunctionResponse.SerializeToString), 'ListCustomFunctionVersions': grpc.unary_unary_rpc_method_handler(servicer.ListCustomFunctionVersions, request_deserializer=common_dot_gateway__base__pb2.GetDefinition.FromString, response_serializer=common_dot_gateway__base__pb2.ListVersionResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('titanium.CustomFunctionService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class CustomFunctionService(object):
    """CustomFunctionService is service that can be used to operate with custom function entity.

    Custom function can be created by user for customizing processes (validation, normalization, mapping)
    """

    @staticmethod
    def AddCustomFunction(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.CustomFunctionService/AddCustomFunction', common_dot_custom__function__pb2.CustomFunction.SerializeToString, common_dot_gateway__base__pb2.AcknowledgeResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetCustomFunction(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.CustomFunctionService/GetCustomFunction', common_dot_custom__function__pb2.CustomFunctionGetDefinition.SerializeToString, common_dot_custom__function__pb2.CustomFunctionDefinitionResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListCustomFunctions(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.CustomFunctionService/ListCustomFunctions', common_dot_custom__function__pb2.ListCustomFunctionRequest.SerializeToString, common_dot_custom__function__pb2.ListCustomFunctionResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListCustomFunctionVersions(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.CustomFunctionService/ListCustomFunctionVersions', common_dot_gateway__base__pb2.GetDefinition.SerializeToString, common_dot_gateway__base__pb2.ListVersionResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)