"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ..common import dq_errors_pb2 as common_dot_dq__errors__pb2

class DataQualityServiceStub(object):
    """DataQualityService is used for operate with data quality errors for submission data.

    Data quality checks prior to submission of data
    Asset & Product & Instrument class check: check which product class & asset class file/stream belongs too field name check: check if field name matches submission template for each product class
    Format check: double, date/timestamp etc.

    Null check: check for empty spaces depending on field requirements (example: price = can be null, trade cannot be null,
    instrument cannot be null, version can be null)
    Provide Deadline for Asset Class &/or Product class based on timezone [london GMT; singapore etc] Auto submit file/stream options (optional)
    Submission only on Case: Pass & within Deadline
    Anonymized/masked data submission
    Data preview before submission, masked & unmasked

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetDataQualityErrors = channel.unary_unary('/titanium.DataQualityService/GetDataQualityErrors', request_serializer=common_dot_dq__errors__pb2.GetDataQualityErrorsRequest.SerializeToString, response_deserializer=common_dot_dq__errors__pb2.GetDataQualityErrorsResponse.FromString)
        self.DQErrors = channel.unary_unary('/titanium.DataQualityService/DQErrors', request_serializer=common_dot_dq__errors__pb2.DQErrorsRequest.SerializeToString, response_deserializer=common_dot_dq__errors__pb2.DQErrorsResponse.FromString)

class DataQualityServiceServicer(object):
    """DataQualityService is used for operate with data quality errors for submission data.

    Data quality checks prior to submission of data
    Asset & Product & Instrument class check: check which product class & asset class file/stream belongs too field name check: check if field name matches submission template for each product class
    Format check: double, date/timestamp etc.

    Null check: check for empty spaces depending on field requirements (example: price = can be null, trade cannot be null,
    instrument cannot be null, version can be null)
    Provide Deadline for Asset Class &/or Product class based on timezone [london GMT; singapore etc] Auto submit file/stream options (optional)
    Submission only on Case: Pass & within Deadline
    Anonymized/masked data submission
    Data preview before submission, masked & unmasked

    """

    def GetDataQualityErrors(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DQErrors(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_DataQualityServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'GetDataQualityErrors': grpc.unary_unary_rpc_method_handler(servicer.GetDataQualityErrors, request_deserializer=common_dot_dq__errors__pb2.GetDataQualityErrorsRequest.FromString, response_serializer=common_dot_dq__errors__pb2.GetDataQualityErrorsResponse.SerializeToString), 'DQErrors': grpc.unary_unary_rpc_method_handler(servicer.DQErrors, request_deserializer=common_dot_dq__errors__pb2.DQErrorsRequest.FromString, response_serializer=common_dot_dq__errors__pb2.DQErrorsResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('titanium.DataQualityService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class DataQualityService(object):
    """DataQualityService is used for operate with data quality errors for submission data.

    Data quality checks prior to submission of data
    Asset & Product & Instrument class check: check which product class & asset class file/stream belongs too field name check: check if field name matches submission template for each product class
    Format check: double, date/timestamp etc.

    Null check: check for empty spaces depending on field requirements (example: price = can be null, trade cannot be null,
    instrument cannot be null, version can be null)
    Provide Deadline for Asset Class &/or Product class based on timezone [london GMT; singapore etc] Auto submit file/stream options (optional)
    Submission only on Case: Pass & within Deadline
    Anonymized/masked data submission
    Data preview before submission, masked & unmasked

    """

    @staticmethod
    def GetDataQualityErrors(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.DataQualityService/GetDataQualityErrors', common_dot_dq__errors__pb2.GetDataQualityErrorsRequest.SerializeToString, common_dot_dq__errors__pb2.GetDataQualityErrorsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DQErrors(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.DataQualityService/DQErrors', common_dot_dq__errors__pb2.DQErrorsRequest.SerializeToString, common_dot_dq__errors__pb2.DQErrorsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)