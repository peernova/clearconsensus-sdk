"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ..public import key_storage_pb2 as public_dot_key__storage__pb2

class KVServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddKey = channel.unary_unary('/titanium.KVService/AddKey', request_serializer=public_dot_key__storage__pb2.KVAsset.SerializeToString, response_deserializer=public_dot_key__storage__pb2.KVOperationResponse.FromString)
        self.UpdateKey = channel.unary_unary('/titanium.KVService/UpdateKey', request_serializer=public_dot_key__storage__pb2.KVAsset.SerializeToString, response_deserializer=public_dot_key__storage__pb2.KVOperationResponse.FromString)
        self.GetKey = channel.unary_unary('/titanium.KVService/GetKey', request_serializer=public_dot_key__storage__pb2.KVRequest.SerializeToString, response_deserializer=public_dot_key__storage__pb2.GetKVResponse.FromString)
        self.DeleteKey = channel.unary_unary('/titanium.KVService/DeleteKey', request_serializer=public_dot_key__storage__pb2.KVRequest.SerializeToString, response_deserializer=public_dot_key__storage__pb2.KVOperationResponse.FromString)
        self.ListKeys = channel.unary_unary('/titanium.KVService/ListKeys', request_serializer=public_dot_key__storage__pb2.ListKVRequest.SerializeToString, response_deserializer=public_dot_key__storage__pb2.ListKVResponse.FromString)

class KVServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AddKey(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateKey(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetKey(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteKey(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListKeys(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_KVServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'AddKey': grpc.unary_unary_rpc_method_handler(servicer.AddKey, request_deserializer=public_dot_key__storage__pb2.KVAsset.FromString, response_serializer=public_dot_key__storage__pb2.KVOperationResponse.SerializeToString), 'UpdateKey': grpc.unary_unary_rpc_method_handler(servicer.UpdateKey, request_deserializer=public_dot_key__storage__pb2.KVAsset.FromString, response_serializer=public_dot_key__storage__pb2.KVOperationResponse.SerializeToString), 'GetKey': grpc.unary_unary_rpc_method_handler(servicer.GetKey, request_deserializer=public_dot_key__storage__pb2.KVRequest.FromString, response_serializer=public_dot_key__storage__pb2.GetKVResponse.SerializeToString), 'DeleteKey': grpc.unary_unary_rpc_method_handler(servicer.DeleteKey, request_deserializer=public_dot_key__storage__pb2.KVRequest.FromString, response_serializer=public_dot_key__storage__pb2.KVOperationResponse.SerializeToString), 'ListKeys': grpc.unary_unary_rpc_method_handler(servicer.ListKeys, request_deserializer=public_dot_key__storage__pb2.ListKVRequest.FromString, response_serializer=public_dot_key__storage__pb2.ListKVResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('titanium.KVService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class KVService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AddKey(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.KVService/AddKey', public_dot_key__storage__pb2.KVAsset.SerializeToString, public_dot_key__storage__pb2.KVOperationResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateKey(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.KVService/UpdateKey', public_dot_key__storage__pb2.KVAsset.SerializeToString, public_dot_key__storage__pb2.KVOperationResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetKey(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.KVService/GetKey', public_dot_key__storage__pb2.KVRequest.SerializeToString, public_dot_key__storage__pb2.GetKVResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteKey(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.KVService/DeleteKey', public_dot_key__storage__pb2.KVRequest.SerializeToString, public_dot_key__storage__pb2.KVOperationResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListKeys(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.KVService/ListKeys', public_dot_key__storage__pb2.ListKVRequest.SerializeToString, public_dot_key__storage__pb2.ListKVResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)