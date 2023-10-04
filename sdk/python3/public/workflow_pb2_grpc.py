"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2
from ..common import workflow_pb2 as common_dot_workflow__pb2

class WorkflowServiceStub(object):
    """todo change URL path to file
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RunWorkflow = channel.unary_unary('/titanium.WorkflowService/RunWorkflow', request_serializer=common_dot_workflow__pb2.RunWorkflowRequest.SerializeToString, response_deserializer=common_dot_workflow__pb2.RunWorkflowResponse.FromString)
        self.ReprocessWorkflow = channel.unary_unary('/titanium.WorkflowService/ReprocessWorkflow', request_serializer=common_dot_workflow__pb2.ReprocessWorkflowRequest.SerializeToString, response_deserializer=common_dot_workflow__pb2.RunWorkflowResponse.FromString)
        self.AddWorkflow = channel.unary_unary('/titanium.WorkflowService/AddWorkflow', request_serializer=common_dot_workflow__pb2.AddWorkflowDefinitionRequest.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.AcknowledgeResponse.FromString)
        self.GetWorkflow = channel.unary_unary('/titanium.WorkflowService/GetWorkflow', request_serializer=common_dot_gateway__base__pb2.GetDefinition.SerializeToString, response_deserializer=common_dot_workflow__pb2.WorkflowDefinitionResponse.FromString)
        self.ListWorkflows = channel.unary_unary('/titanium.WorkflowService/ListWorkflows', request_serializer=common_dot_gateway__base__pb2.ListRequest.SerializeToString, response_deserializer=common_dot_workflow__pb2.WorkflowList.FromString)
        self.EnableWorkflow = channel.unary_unary('/titanium.WorkflowService/EnableWorkflow', request_serializer=common_dot_gateway__base__pb2.EnableDisableRequest.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.AcknowledgeResponse.FromString)
        self.DisableWorkflow = channel.unary_unary('/titanium.WorkflowService/DisableWorkflow', request_serializer=common_dot_gateway__base__pb2.EnableDisableRequest.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.AcknowledgeResponse.FromString)
        self.ListWorkflowActions = channel.unary_unary('/titanium.WorkflowService/ListWorkflowActions', request_serializer=common_dot_gateway__base__pb2.ListRequest.SerializeToString, response_deserializer=common_dot_workflow__pb2.WorkflowList.FromString)
        self.GetWorkflowAction = channel.unary_unary('/titanium.WorkflowService/GetWorkflowAction', request_serializer=common_dot_workflow__pb2.GetActionRequest.SerializeToString, response_deserializer=common_dot_workflow__pb2.GetWorkflowActionResponse.FromString)

class WorkflowServiceServicer(object):
    """todo change URL path to file
    """

    def RunWorkflow(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReprocessWorkflow(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddWorkflow(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetWorkflow(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListWorkflows(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EnableWorkflow(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DisableWorkflow(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListWorkflowActions(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetWorkflowAction(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_WorkflowServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'RunWorkflow': grpc.unary_unary_rpc_method_handler(servicer.RunWorkflow, request_deserializer=common_dot_workflow__pb2.RunWorkflowRequest.FromString, response_serializer=common_dot_workflow__pb2.RunWorkflowResponse.SerializeToString), 'ReprocessWorkflow': grpc.unary_unary_rpc_method_handler(servicer.ReprocessWorkflow, request_deserializer=common_dot_workflow__pb2.ReprocessWorkflowRequest.FromString, response_serializer=common_dot_workflow__pb2.RunWorkflowResponse.SerializeToString), 'AddWorkflow': grpc.unary_unary_rpc_method_handler(servicer.AddWorkflow, request_deserializer=common_dot_workflow__pb2.AddWorkflowDefinitionRequest.FromString, response_serializer=common_dot_gateway__base__pb2.AcknowledgeResponse.SerializeToString), 'GetWorkflow': grpc.unary_unary_rpc_method_handler(servicer.GetWorkflow, request_deserializer=common_dot_gateway__base__pb2.GetDefinition.FromString, response_serializer=common_dot_workflow__pb2.WorkflowDefinitionResponse.SerializeToString), 'ListWorkflows': grpc.unary_unary_rpc_method_handler(servicer.ListWorkflows, request_deserializer=common_dot_gateway__base__pb2.ListRequest.FromString, response_serializer=common_dot_workflow__pb2.WorkflowList.SerializeToString), 'EnableWorkflow': grpc.unary_unary_rpc_method_handler(servicer.EnableWorkflow, request_deserializer=common_dot_gateway__base__pb2.EnableDisableRequest.FromString, response_serializer=common_dot_gateway__base__pb2.AcknowledgeResponse.SerializeToString), 'DisableWorkflow': grpc.unary_unary_rpc_method_handler(servicer.DisableWorkflow, request_deserializer=common_dot_gateway__base__pb2.EnableDisableRequest.FromString, response_serializer=common_dot_gateway__base__pb2.AcknowledgeResponse.SerializeToString), 'ListWorkflowActions': grpc.unary_unary_rpc_method_handler(servicer.ListWorkflowActions, request_deserializer=common_dot_gateway__base__pb2.ListRequest.FromString, response_serializer=common_dot_workflow__pb2.WorkflowList.SerializeToString), 'GetWorkflowAction': grpc.unary_unary_rpc_method_handler(servicer.GetWorkflowAction, request_deserializer=common_dot_workflow__pb2.GetActionRequest.FromString, response_serializer=common_dot_workflow__pb2.GetWorkflowActionResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('titanium.WorkflowService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class WorkflowService(object):
    """todo change URL path to file
    """

    @staticmethod
    def RunWorkflow(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.WorkflowService/RunWorkflow', common_dot_workflow__pb2.RunWorkflowRequest.SerializeToString, common_dot_workflow__pb2.RunWorkflowResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReprocessWorkflow(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.WorkflowService/ReprocessWorkflow', common_dot_workflow__pb2.ReprocessWorkflowRequest.SerializeToString, common_dot_workflow__pb2.RunWorkflowResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddWorkflow(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.WorkflowService/AddWorkflow', common_dot_workflow__pb2.AddWorkflowDefinitionRequest.SerializeToString, common_dot_gateway__base__pb2.AcknowledgeResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetWorkflow(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.WorkflowService/GetWorkflow', common_dot_gateway__base__pb2.GetDefinition.SerializeToString, common_dot_workflow__pb2.WorkflowDefinitionResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListWorkflows(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.WorkflowService/ListWorkflows', common_dot_gateway__base__pb2.ListRequest.SerializeToString, common_dot_workflow__pb2.WorkflowList.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EnableWorkflow(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.WorkflowService/EnableWorkflow', common_dot_gateway__base__pb2.EnableDisableRequest.SerializeToString, common_dot_gateway__base__pb2.AcknowledgeResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DisableWorkflow(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.WorkflowService/DisableWorkflow', common_dot_gateway__base__pb2.EnableDisableRequest.SerializeToString, common_dot_gateway__base__pb2.AcknowledgeResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListWorkflowActions(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.WorkflowService/ListWorkflowActions', common_dot_gateway__base__pb2.ListRequest.SerializeToString, common_dot_workflow__pb2.WorkflowList.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetWorkflowAction(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.WorkflowService/GetWorkflowAction', common_dot_workflow__pb2.GetActionRequest.SerializeToString, common_dot_workflow__pb2.GetWorkflowActionResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)