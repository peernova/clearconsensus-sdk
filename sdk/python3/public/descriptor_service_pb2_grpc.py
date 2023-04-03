"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ..common import descriptor_pb2 as common_dot_descriptor__pb2
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2

class DescriptorServiceStub(object):
    """DescriptorService is service used to operate with descriptor entity.
    Descriptor is used for describe different entities and requests in the system.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddDescriptor = channel.unary_unary('/titanium.DescriptorService/AddDescriptor', request_serializer=common_dot_gateway__base__pb2.DescriptorDefinition.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.AcknowledgeResponse.FromString)
        self.GetDescriptor = channel.unary_unary('/titanium.DescriptorService/GetDescriptor', request_serializer=common_dot_gateway__base__pb2.GetDefinition.SerializeToString, response_deserializer=common_dot_descriptor__pb2.DescriptorDefinitionResponse.FromString)
        self.EnableDescriptor = channel.unary_unary('/titanium.DescriptorService/EnableDescriptor', request_serializer=common_dot_gateway__base__pb2.EnableDisableRequest.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.AcknowledgeResponse.FromString)
        self.DisableDescriptor = channel.unary_unary('/titanium.DescriptorService/DisableDescriptor', request_serializer=common_dot_gateway__base__pb2.EnableDisableRequest.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.AcknowledgeResponse.FromString)
        self.ListDescriptors = channel.unary_unary('/titanium.DescriptorService/ListDescriptors', request_serializer=common_dot_gateway__base__pb2.ListRequest.SerializeToString, response_deserializer=common_dot_descriptor__pb2.DescriptorList.FromString)
        self.ListDescriptorVersions = channel.unary_unary('/titanium.DescriptorService/ListDescriptorVersions', request_serializer=common_dot_gateway__base__pb2.GetDefinition.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.ListVersionResponse.FromString)
        self.GetDescriptorVersion = channel.unary_unary('/titanium.DescriptorService/GetDescriptorVersion', request_serializer=common_dot_gateway__base__pb2.VersionRequest.SerializeToString, response_deserializer=common_dot_descriptor__pb2.DescriptorDefinitionResponse.FromString)

class DescriptorServiceServicer(object):
    """DescriptorService is service used to operate with descriptor entity.
    Descriptor is used for describe different entities and requests in the system.
    """

    def AddDescriptor(self, request, context):
        """AddDescriptor is used to add specific descriptor with specific definition to the system.
        Regular users can store a descriptor within their own scope, and any attempts to push it to a different scope will be declined.
        Back office users can store descriptors in any scope, provided that a scope key is provided.
        The name of the descriptor must match the name of the asset class to be mapped correctly.
        If a descriptor with the same name already exists, it will be updated.

        Example of request for regular user :
        {
        "name":"foreign_exchange-vanilla-forwards",
        "fields":[
        {
        [data]="typeEnumToDisplayName[cellData]"v        "name":"submission_date",
        "nullable":true,
        "type":"string"
        },
        {
        "name":"submission_asset",
        "nullable":true,
        "type":"string"
        }
        ]
        }

        Example of request for Back Office :
        {
        "name":"foreign_exchange-vanilla-forwards",
        "scope": "global",
        "fields":[
        {
        "name":"snap_date",
        "alias":"snap_date",
        "type":"date",
        "options":{
        "format":"MM/dd/yy"
        }
        },
        {
        "name":"asset",
        "alias":"asset",
        "type":"string"
        },
        {
        "name": "sub-asset",
        "alias": "sub-asset",
        "type": "string"
        }
        ]
        }

        Example of response :
        {
        "data":{
        "uid":"98fd0526-cc88-11ec-b784-0fe7a41b45e0",
        "name":"foreign_exchange-vanilla-forwards"
        }
        }

        Example of error response :
        {
        "error":{
        "code":70,
        "message":"Can't add descriptor: [com.peernova.api.searchmetadata.metadata.exceptions.MetaDataServiceException: Namespace [bank11] is not valid]."
        }
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDescriptor(self, request, context):
        """GetDescriptor is used to get specific descriptor definition based on get definition.
        Regular users can retrieve only their own descriptors and descriptors associated with asset classes.
        Back office users can retrieve any of the existing descriptors.

        Example of request :
        {
        "identifier":{
        "name":"foreign_exchange-vanilla-forwards"
        },
        "scope":"global"
        }

        Example of response :
        {
        "data": "{"name":"foreign_exchange-vanilla-forwards","fields":[{"name":"snap_date","type":"date","options":{"format":"MM/dd/yy"},"alias":"snap_date"},{"name":"asset","type":"string","alias":"asset"},{"name":"sub-asset","type":"string","alias":"sub-asset"},{"name":"service","type":"string","nullable":true,"alias":"service"},{"name":"snap_time","type":"string","alias":"snap_time"},{"name":"curr_1","type":"string","alias":"curr_1"},{"name":"curr_2","type":"string","alias":"curr_2"},{"name":"onshore_offshore_curr_1","type":"string","nullable":true,"alias":"onshore_offshore_curr_1"},{"name":"onshore_offshore_curr_2","type":"string","nullable":true,"alias":"onshore_offshore_curr_2"},{"name":"instrument_type","type":"string","alias":"instrument_type"},{"name":"tenor","type":"string","nullable":true,"alias":"tenor"},{"name":"value_source","type":"string","nullable":true,"alias":"value_source"},{"name":"fwrd_conversion_factor","type":"double","nullable":true,"alias":"fwrd_conversion_factor"},{"name":"mid_fwrd_outright","type":"double","nullable":true,"alias":"mid_fwrd_outright"},{"name":"value_source_ref_id","type":"string","nullable":true,"alias":"value_source_ref_id"},{"name":"client","type":"string","alias":"client"},{"name":"spot_reference_price","type":"double","nullable":true,"alias":"spot_reference_price"},{"name":"mid_fwrd_points","type":"double","alias":"mid_fwrd_points"}]}"
        }

        Example of error response :
        {
        "error": {
        "code": 70,
        "message": "Can't get descriptor: [[foreign_exchange-vanilla-forwards1] of service [DESCRIPTOR] does not exist in namespace [global]]."
        }
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EnableDescriptor(self, request, context):
        """EnableDescriptor is used to enable specific descriptor.

        Example of request :
        {
        "name" : "foreign_exchange-vanilla-forwards",
        "scope": "global"
        }

        Example of response :
        {
        "data": {
        "uid": "",
        "name": "foreign_exchange-vanilla-forwards"
        }
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DisableDescriptor(self, request, context):
        """DisableDescriptor is used to disable specific descriptor.
        Example of response :
        {
        "data": {
        "uid": "",
        "name": "foreign_exchange-vanilla-forwards"
        }
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListDescriptors(self, request, context):
        """ListDescriptors returns list of specific descriptors according to request.

        Example of request :
        {
        "scope":"global"
        }

        Example of response :
        {
        "data": {
        "results": [
        {
        "uid": "",
        "name": "foreign_exchange-vanilla-options"
        },
        {
        "uid": "",
        "name": "foreign_exchange-exotics-barriers_and_digitals"
        },
        {
        "uid": "",
        "name": "foreign_exchange-exotics-tarfs"
        }
        ]
        }
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListDescriptorVersions(self, request, context):
        """ListDescriptorVersions returns list of version of the specific descriptor versions.

        Example of request :
        {
        "scope":"global",
        "identifier":{
        "name":"foreign_exchange-vanilla-forwards"
        }
        }

        Example of response : {
        "data": {
        "versions": [
        {
        "versionId": "fM9AukEqTJXKOcbW_tQ7Sfr4Clp5qinKq_liXZYzyiI=",
        "createdAt": "2022-06-14 10:57:42.0"
        },
        {
        "versionId": "LmVlkPbnsUKFBw8qIbUHEzBsRrcnG_BSMnopA5Ptd7I=",
        "createdAt": "2022-06-14 10:20:48.0"
        }
        ]
        }
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDescriptorVersion(self, request, context):
        """GetDescriptorVersion returns current version of the specific descriptor.

        Example of response :
        {
        "data":"{"name":"fx_test_for_bank1","fields":[{"name":"submission_date","type":"date","options":{"format":"MM/dd/yyyy"},"alias":"date12"},{"name":"submission_asset","type":"string","nullable":true}],"options":{"DEDUPLICATION":{"GROUP_BY":["submission_date","submission_asset"]}}}"
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_DescriptorServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'AddDescriptor': grpc.unary_unary_rpc_method_handler(servicer.AddDescriptor, request_deserializer=common_dot_gateway__base__pb2.DescriptorDefinition.FromString, response_serializer=common_dot_gateway__base__pb2.AcknowledgeResponse.SerializeToString), 'GetDescriptor': grpc.unary_unary_rpc_method_handler(servicer.GetDescriptor, request_deserializer=common_dot_gateway__base__pb2.GetDefinition.FromString, response_serializer=common_dot_descriptor__pb2.DescriptorDefinitionResponse.SerializeToString), 'EnableDescriptor': grpc.unary_unary_rpc_method_handler(servicer.EnableDescriptor, request_deserializer=common_dot_gateway__base__pb2.EnableDisableRequest.FromString, response_serializer=common_dot_gateway__base__pb2.AcknowledgeResponse.SerializeToString), 'DisableDescriptor': grpc.unary_unary_rpc_method_handler(servicer.DisableDescriptor, request_deserializer=common_dot_gateway__base__pb2.EnableDisableRequest.FromString, response_serializer=common_dot_gateway__base__pb2.AcknowledgeResponse.SerializeToString), 'ListDescriptors': grpc.unary_unary_rpc_method_handler(servicer.ListDescriptors, request_deserializer=common_dot_gateway__base__pb2.ListRequest.FromString, response_serializer=common_dot_descriptor__pb2.DescriptorList.SerializeToString), 'ListDescriptorVersions': grpc.unary_unary_rpc_method_handler(servicer.ListDescriptorVersions, request_deserializer=common_dot_gateway__base__pb2.GetDefinition.FromString, response_serializer=common_dot_gateway__base__pb2.ListVersionResponse.SerializeToString), 'GetDescriptorVersion': grpc.unary_unary_rpc_method_handler(servicer.GetDescriptorVersion, request_deserializer=common_dot_gateway__base__pb2.VersionRequest.FromString, response_serializer=common_dot_descriptor__pb2.DescriptorDefinitionResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('titanium.DescriptorService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class DescriptorService(object):
    """DescriptorService is service used to operate with descriptor entity.
    Descriptor is used for describe different entities and requests in the system.
    """

    @staticmethod
    def AddDescriptor(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.DescriptorService/AddDescriptor', common_dot_gateway__base__pb2.DescriptorDefinition.SerializeToString, common_dot_gateway__base__pb2.AcknowledgeResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDescriptor(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.DescriptorService/GetDescriptor', common_dot_gateway__base__pb2.GetDefinition.SerializeToString, common_dot_descriptor__pb2.DescriptorDefinitionResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EnableDescriptor(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.DescriptorService/EnableDescriptor', common_dot_gateway__base__pb2.EnableDisableRequest.SerializeToString, common_dot_gateway__base__pb2.AcknowledgeResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DisableDescriptor(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.DescriptorService/DisableDescriptor', common_dot_gateway__base__pb2.EnableDisableRequest.SerializeToString, common_dot_gateway__base__pb2.AcknowledgeResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListDescriptors(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.DescriptorService/ListDescriptors', common_dot_gateway__base__pb2.ListRequest.SerializeToString, common_dot_descriptor__pb2.DescriptorList.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListDescriptorVersions(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.DescriptorService/ListDescriptorVersions', common_dot_gateway__base__pb2.GetDefinition.SerializeToString, common_dot_gateway__base__pb2.ListVersionResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDescriptorVersion(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.DescriptorService/GetDescriptorVersion', common_dot_gateway__base__pb2.VersionRequest.SerializeToString, common_dot_descriptor__pb2.DescriptorDefinitionResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

class DbDescriptorServiceStub(object):
    """DbDescriptorService is service used to operate with descriptor entity for database.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddDbDescriptor = channel.unary_unary('/titanium.DbDescriptorService/AddDbDescriptor', request_serializer=common_dot_gateway__base__pb2.DescriptorDefinition.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.AcknowledgeResponse.FromString)
        self.GetDbDescriptor = channel.unary_unary('/titanium.DbDescriptorService/GetDbDescriptor', request_serializer=common_dot_gateway__base__pb2.GetDefinition.SerializeToString, response_deserializer=common_dot_descriptor__pb2.DescriptorDefinitionResponse.FromString)
        self.EnableDbDescriptor = channel.unary_unary('/titanium.DbDescriptorService/EnableDbDescriptor', request_serializer=common_dot_gateway__base__pb2.EnableDisableRequest.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.AcknowledgeResponse.FromString)
        self.DisableDbDescriptor = channel.unary_unary('/titanium.DbDescriptorService/DisableDbDescriptor', request_serializer=common_dot_gateway__base__pb2.EnableDisableRequest.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.AcknowledgeResponse.FromString)
        self.ListDbDescriptors = channel.unary_unary('/titanium.DbDescriptorService/ListDbDescriptors', request_serializer=common_dot_gateway__base__pb2.ListRequest.SerializeToString, response_deserializer=common_dot_descriptor__pb2.DescriptorList.FromString)
        self.ListDbDescriptorVersions = channel.unary_unary('/titanium.DbDescriptorService/ListDbDescriptorVersions', request_serializer=common_dot_gateway__base__pb2.GetDefinition.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.ListVersionResponse.FromString)
        self.GetDbDescriptorVersion = channel.unary_unary('/titanium.DbDescriptorService/GetDbDescriptorVersion', request_serializer=common_dot_gateway__base__pb2.VersionRequest.SerializeToString, response_deserializer=common_dot_descriptor__pb2.DescriptorDefinitionResponse.FromString)

class DbDescriptorServiceServicer(object):
    """DbDescriptorService is service used to operate with descriptor entity for database.
    """

    def AddDbDescriptor(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDbDescriptor(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EnableDbDescriptor(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DisableDbDescriptor(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListDbDescriptors(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListDbDescriptorVersions(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDbDescriptorVersion(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_DbDescriptorServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'AddDbDescriptor': grpc.unary_unary_rpc_method_handler(servicer.AddDbDescriptor, request_deserializer=common_dot_gateway__base__pb2.DescriptorDefinition.FromString, response_serializer=common_dot_gateway__base__pb2.AcknowledgeResponse.SerializeToString), 'GetDbDescriptor': grpc.unary_unary_rpc_method_handler(servicer.GetDbDescriptor, request_deserializer=common_dot_gateway__base__pb2.GetDefinition.FromString, response_serializer=common_dot_descriptor__pb2.DescriptorDefinitionResponse.SerializeToString), 'EnableDbDescriptor': grpc.unary_unary_rpc_method_handler(servicer.EnableDbDescriptor, request_deserializer=common_dot_gateway__base__pb2.EnableDisableRequest.FromString, response_serializer=common_dot_gateway__base__pb2.AcknowledgeResponse.SerializeToString), 'DisableDbDescriptor': grpc.unary_unary_rpc_method_handler(servicer.DisableDbDescriptor, request_deserializer=common_dot_gateway__base__pb2.EnableDisableRequest.FromString, response_serializer=common_dot_gateway__base__pb2.AcknowledgeResponse.SerializeToString), 'ListDbDescriptors': grpc.unary_unary_rpc_method_handler(servicer.ListDbDescriptors, request_deserializer=common_dot_gateway__base__pb2.ListRequest.FromString, response_serializer=common_dot_descriptor__pb2.DescriptorList.SerializeToString), 'ListDbDescriptorVersions': grpc.unary_unary_rpc_method_handler(servicer.ListDbDescriptorVersions, request_deserializer=common_dot_gateway__base__pb2.GetDefinition.FromString, response_serializer=common_dot_gateway__base__pb2.ListVersionResponse.SerializeToString), 'GetDbDescriptorVersion': grpc.unary_unary_rpc_method_handler(servicer.GetDbDescriptorVersion, request_deserializer=common_dot_gateway__base__pb2.VersionRequest.FromString, response_serializer=common_dot_descriptor__pb2.DescriptorDefinitionResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('titanium.DbDescriptorService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class DbDescriptorService(object):
    """DbDescriptorService is service used to operate with descriptor entity for database.
    """

    @staticmethod
    def AddDbDescriptor(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.DbDescriptorService/AddDbDescriptor', common_dot_gateway__base__pb2.DescriptorDefinition.SerializeToString, common_dot_gateway__base__pb2.AcknowledgeResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDbDescriptor(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.DbDescriptorService/GetDbDescriptor', common_dot_gateway__base__pb2.GetDefinition.SerializeToString, common_dot_descriptor__pb2.DescriptorDefinitionResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EnableDbDescriptor(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.DbDescriptorService/EnableDbDescriptor', common_dot_gateway__base__pb2.EnableDisableRequest.SerializeToString, common_dot_gateway__base__pb2.AcknowledgeResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DisableDbDescriptor(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.DbDescriptorService/DisableDbDescriptor', common_dot_gateway__base__pb2.EnableDisableRequest.SerializeToString, common_dot_gateway__base__pb2.AcknowledgeResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListDbDescriptors(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.DbDescriptorService/ListDbDescriptors', common_dot_gateway__base__pb2.ListRequest.SerializeToString, common_dot_descriptor__pb2.DescriptorList.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListDbDescriptorVersions(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.DbDescriptorService/ListDbDescriptorVersions', common_dot_gateway__base__pb2.GetDefinition.SerializeToString, common_dot_gateway__base__pb2.ListVersionResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDbDescriptorVersion(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.DbDescriptorService/GetDbDescriptorVersion', common_dot_gateway__base__pb2.VersionRequest.SerializeToString, common_dot_descriptor__pb2.DescriptorDefinitionResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)