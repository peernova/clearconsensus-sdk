"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2
from ..common import unique_key_pb2 as common_dot_unique__key__pb2

class UniqueKeyServiceStub(object):
    """UniqueKeyService is a service that is responsible for unique keys.
    The assets prices submission has a set of fields that uniquely identify a row and for deduplication purposes unique key entity exists. 
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddUniqueKey = channel.unary_unary('/titanium.UniqueKeyService/AddUniqueKey', request_serializer=common_dot_unique__key__pb2.UniqueKeyDefinition.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.AcknowledgeResponse.FromString)
        self.GetUniqueKey = channel.unary_unary('/titanium.UniqueKeyService/GetUniqueKey', request_serializer=common_dot_gateway__base__pb2.GetDefinition.SerializeToString, response_deserializer=common_dot_unique__key__pb2.UniqueKeyDefinitionResponse.FromString)
        self.ListUniqueKeys = channel.unary_unary('/titanium.UniqueKeyService/ListUniqueKeys', request_serializer=common_dot_gateway__base__pb2.ListRequest.SerializeToString, response_deserializer=common_dot_unique__key__pb2.ListUniqueKeysResponse.FromString)
        self.ListUniqueKeyVersions = channel.unary_unary('/titanium.UniqueKeyService/ListUniqueKeyVersions', request_serializer=common_dot_gateway__base__pb2.GetDefinition.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.ListVersionResponse.FromString)
        self.GetUniqueKeyVersion = channel.unary_unary('/titanium.UniqueKeyService/GetUniqueKeyVersion', request_serializer=common_dot_gateway__base__pb2.VersionRequest.SerializeToString, response_deserializer=common_dot_unique__key__pb2.UniqueKeyDefinitionResponse.FromString)
        self.EnableUniqueKey = channel.unary_unary('/titanium.UniqueKeyService/EnableUniqueKey', request_serializer=common_dot_gateway__base__pb2.EnableDisableRequest.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.AcknowledgeResponse.FromString)
        self.DisableUniqueKey = channel.unary_unary('/titanium.UniqueKeyService/DisableUniqueKey', request_serializer=common_dot_gateway__base__pb2.EnableDisableRequest.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.AcknowledgeResponse.FromString)

class UniqueKeyServiceServicer(object):
    """UniqueKeyService is a service that is responsible for unique keys.
    The assets prices submission has a set of fields that uniquely identify a row and for deduplication purposes unique key entity exists. 
    """

    def AddUniqueKey(self, request, context):
        """AddUniqueKey is used to add a new unique key definition to the system.

        Example of request :
        {
        "name":"foreign_exchange-vanilla-forwards",
        "scope":"global",
        "uniqueKey":[
        "snap_date",
        "asset",
        "service",
        "client",
        "service",
        "tenor",
        "snap_time",
        "instrument_type",
        "spot_reference_price",
        "mid_fwrd_outright",
        "mid_fwrd_points",
        "onshore_offshore_curr_1",
        "onshore_offshore_curr_2"
        ]
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUniqueKey(self, request, context):
        """GetUniqueKey is used to retrieve a unique key definition by its scope and name.
        Request:
        {
        "identifier":{
        "name":"foreign_exchange-vanilla-forwards"
        },
        "scope":"global"
        }

        Response:
        {
        "data": {
        "name": "foreign_exchange-vanilla-forwards",
        "scope": "global",
        "uniqueKey": [
        "snap_date",
        "asset",
        "service",
        "client",
        "service",
        "tenor",
        "snap_time",
        "instrument_type",
        "spot_reference_price",
        "mid_fwrd_outright",
        "mid_fwrd_points",
        "onshore_offshore_curr_1",
        "onshore_offshore_curr_2"
        ],
        "orderBy": [
        "__input_row_num"
        ],
        "order": "ASC"
        }
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListUniqueKeys(self, request, context):
        """ListUniqueKeys is used to retrieve a list of all unique key definitions in the system.
        Request:
        {
        "scope":"global"
        }

        Response:
        {
        "data": {
        "results": [
        {
        "name": "foreign_exchange-vanilla-forwards",
        "scope": "global",
        "uniqueKey": [
        "asset",
        "service",
        "sub-asset",
        "instrument_type",
        "tenor",
        "snap_date",
        "snap_time",
        "curr_1",
        "curr_2",
        "onshore_offshore_curr_1",
        "onshore_offshore_curr_2"
        ],
        "orderBy": [
        "__input_row_num"
        ],
        "order": "ASC"
        },
        {
        "name": "foreign_exchange-vanilla-options",
        "scope": "global",
        "uniqueKey": [
        "snap_date",
        "asset",
        "service",
        "snap_time",
        "instrument_type",
        "option_instrument_parameter",
        "exercise_style",
        "option_execution_cut_time",
        "curr_1",
        "curr_2",
        "tenor",
        "delta",
        "vol_format",
        "instrument_convention",
        "delta_convention",
        "premium_currency",
        "settlement_convention"
        ],
        "orderBy": [
        "__input_row_num"
        ],
        "order": "ASC"
        }
        ]
        }
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListUniqueKeyVersions(self, request, context):
        """ListUniqueKeyVersions is used to retrieve a list of all versions of a specific unique key definition by its scope and name.
        Request:
        {
        "scope":"global",
        "identifier": {
        "name": "foreign_exchange-vanilla-forwards"
        }
        }

        Response:
        {
        "data": {
        "versions": [
        {
        "versionId":"0bmhRR-7hISwkb_H2MvIqafpJCAoy3YgEySZjntZF9o=",
        "createdAt": "2022-08-22 15:23:44.0"
        }
        ]
        }
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUniqueKeyVersion(self, request, context):
        """GetUniqueKeyVersion is used to retrieve a specific version of a unique key definition by its scope, name, and version ID.
        Response:
        {
        "data": {
        "name": "foreign_exchange-vanilla-forwards",
        "scope": "global",
        "uniqueKey": [
        "asset",
        "service",
        "sub-asset",
        "instrument_type",
        "tenor",
        "snap_date",
        "snap_time",
        "curr_1",
        "curr_2",
        "onshore_offshore_curr_1",
        "onshore_offshore_curr_2"
        ],
        "orderBy": [
        "__input_row_num"
        ],
        "order": "ASC"
        }
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EnableUniqueKey(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DisableUniqueKey(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_UniqueKeyServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'AddUniqueKey': grpc.unary_unary_rpc_method_handler(servicer.AddUniqueKey, request_deserializer=common_dot_unique__key__pb2.UniqueKeyDefinition.FromString, response_serializer=common_dot_gateway__base__pb2.AcknowledgeResponse.SerializeToString), 'GetUniqueKey': grpc.unary_unary_rpc_method_handler(servicer.GetUniqueKey, request_deserializer=common_dot_gateway__base__pb2.GetDefinition.FromString, response_serializer=common_dot_unique__key__pb2.UniqueKeyDefinitionResponse.SerializeToString), 'ListUniqueKeys': grpc.unary_unary_rpc_method_handler(servicer.ListUniqueKeys, request_deserializer=common_dot_gateway__base__pb2.ListRequest.FromString, response_serializer=common_dot_unique__key__pb2.ListUniqueKeysResponse.SerializeToString), 'ListUniqueKeyVersions': grpc.unary_unary_rpc_method_handler(servicer.ListUniqueKeyVersions, request_deserializer=common_dot_gateway__base__pb2.GetDefinition.FromString, response_serializer=common_dot_gateway__base__pb2.ListVersionResponse.SerializeToString), 'GetUniqueKeyVersion': grpc.unary_unary_rpc_method_handler(servicer.GetUniqueKeyVersion, request_deserializer=common_dot_gateway__base__pb2.VersionRequest.FromString, response_serializer=common_dot_unique__key__pb2.UniqueKeyDefinitionResponse.SerializeToString), 'EnableUniqueKey': grpc.unary_unary_rpc_method_handler(servicer.EnableUniqueKey, request_deserializer=common_dot_gateway__base__pb2.EnableDisableRequest.FromString, response_serializer=common_dot_gateway__base__pb2.AcknowledgeResponse.SerializeToString), 'DisableUniqueKey': grpc.unary_unary_rpc_method_handler(servicer.DisableUniqueKey, request_deserializer=common_dot_gateway__base__pb2.EnableDisableRequest.FromString, response_serializer=common_dot_gateway__base__pb2.AcknowledgeResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('titanium.UniqueKeyService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class UniqueKeyService(object):
    """UniqueKeyService is a service that is responsible for unique keys.
    The assets prices submission has a set of fields that uniquely identify a row and for deduplication purposes unique key entity exists. 
    """

    @staticmethod
    def AddUniqueKey(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.UniqueKeyService/AddUniqueKey', common_dot_unique__key__pb2.UniqueKeyDefinition.SerializeToString, common_dot_gateway__base__pb2.AcknowledgeResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUniqueKey(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.UniqueKeyService/GetUniqueKey', common_dot_gateway__base__pb2.GetDefinition.SerializeToString, common_dot_unique__key__pb2.UniqueKeyDefinitionResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListUniqueKeys(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.UniqueKeyService/ListUniqueKeys', common_dot_gateway__base__pb2.ListRequest.SerializeToString, common_dot_unique__key__pb2.ListUniqueKeysResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListUniqueKeyVersions(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.UniqueKeyService/ListUniqueKeyVersions', common_dot_gateway__base__pb2.GetDefinition.SerializeToString, common_dot_gateway__base__pb2.ListVersionResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUniqueKeyVersion(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.UniqueKeyService/GetUniqueKeyVersion', common_dot_gateway__base__pb2.VersionRequest.SerializeToString, common_dot_unique__key__pb2.UniqueKeyDefinitionResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EnableUniqueKey(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.UniqueKeyService/EnableUniqueKey', common_dot_gateway__base__pb2.EnableDisableRequest.SerializeToString, common_dot_gateway__base__pb2.AcknowledgeResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DisableUniqueKey(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.UniqueKeyService/DisableUniqueKey', common_dot_gateway__base__pb2.EnableDisableRequest.SerializeToString, common_dot_gateway__base__pb2.AcknowledgeResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)