"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2
from ..common import mapper_pb2 as common_dot_mapper__pb2

class MappingServiceStub(object):
    """MappingService is service that responsible for rules that related to
    transformation of submission data into system definition for further calculation and analysis 
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddMappingRule = channel.unary_unary('/titanium.MappingService/AddMappingRule', request_serializer=common_dot_mapper__pb2.MappingRuleDefinition.SerializeToString, response_deserializer=common_dot_mapper__pb2.DescriptorPairBasedAcknowledgeResponse.FromString)
        self.GetMappingRule = channel.unary_unary('/titanium.MappingService/GetMappingRule', request_serializer=common_dot_mapper__pb2.DescriptorPairBasedGetDefinition.SerializeToString, response_deserializer=common_dot_mapper__pb2.MappingRuleResponse.FromString)
        self.EnableMappingRule = channel.unary_unary('/titanium.MappingService/EnableMappingRule', request_serializer=common_dot_mapper__pb2.DescriptorPairBasedGetDefinition.SerializeToString, response_deserializer=common_dot_mapper__pb2.DescriptorPairBasedAcknowledgeResponse.FromString)
        self.DisableMappingRule = channel.unary_unary('/titanium.MappingService/DisableMappingRule', request_serializer=common_dot_mapper__pb2.DescriptorPairBasedGetDefinition.SerializeToString, response_deserializer=common_dot_mapper__pb2.DescriptorPairBasedAcknowledgeResponse.FromString)
        self.ListMappingRules = channel.unary_unary('/titanium.MappingService/ListMappingRules', request_serializer=common_dot_gateway__base__pb2.ListRequest.SerializeToString, response_deserializer=common_dot_mapper__pb2.MappingRuleList.FromString)
        self.ListMappingRuleVersions = channel.unary_unary('/titanium.MappingService/ListMappingRuleVersions', request_serializer=common_dot_mapper__pb2.DescriptorPairBasedGetDefinition.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.ListVersionResponse.FromString)
        self.GetMappingRuleVersion = channel.unary_unary('/titanium.MappingService/GetMappingRuleVersion', request_serializer=common_dot_mapper__pb2.DescriptorPairBasedVersionRequest.SerializeToString, response_deserializer=common_dot_mapper__pb2.MappingRuleResponse.FromString)

class MappingServiceServicer(object):
    """MappingService is service that responsible for rules that related to
    transformation of submission data into system definition for further calculation and analysis 
    """

    def AddMappingRule(self, request, context):
        """AddMappingRule AddMappingRule is an API used to add a specific mapping rule to the system.
        The name provided for the mapping rule must match the asset class and descriptor names.
        If a mapping rule with the same name already exists, it will be updated.
        This API accepts a MappingRuleDefinition object as its parameter,which includes information about the mapping rule being added.
        The response from this API is a DescriptorPairBasedAcknowledgeResponse,which acknowledges the addition of the mapping rule.

        Example of request for regular user :
        {
        "src_descriptor":"foreign_exchange-vanilla-forwards",
        "dest_descriptor":"foreign_exchange-vanilla-forwards",
        "transformations":[
        {
        "targetColumn":"submission_date",
        "sourceColumn":"date"
        },
        {
        "targetColumn":"submission_asset",
        "rule":"{ "$to_upper": { "$trim" : "fx_test_for_bank1.submission_asset" }}",
        "name": "upper case asset",
        "description": "i am optional..."
        }
        ]
        }

        Example of request for Back Office :
        {
        "src_descriptor":"foreign_exchange-vanilla-forwards",
        "dest_descriptor":"foreign_exchange-vanilla-forwards",
        "scope":"global",
        "transformations":[
        {
        "targetColumn":"submission_date",
        "sourceColumn":"another_date"
        },
        {
        "targetColumn":"submission_asset",
        "rule":"{ "$to_upper": { "$trim" : "fx_test_for_bank1.submission_asset" }}",
        "name": "upper case asset",
        "description": "i am optional..."
        }
        ]
        }

        Example of response :
        {
        "data":{
        "uid":"fc8b57b7-cc90-11ec-b784-8dfc726b351f",
        "src_descriptor":"foreign_exchange-vanilla-forwards",
        "dest_descriptor":"foreign_exchange-vanilla-forwards"
        }
        }

        Example of error response :
        {
        "error":{
        "code":70,
        "message":"Missing argument: rule name."
        }
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMappingRule(self, request, context):
        """GetMappingRule is used to retrieve a mapping rule for a given descriptor pair.
        It accepts a DescriptorPairBasedGetDefinition object as its parameter, which specifies the source and destination descriptors for the mapping rule.
        The response from this it is a MappingRuleResponse, which includes information about the retrieved mapping rule.

        Example of request for regular user :
        {
        "identifier":{
        "uid":"fc8b57b7-cc90-11ec-b784-8dfc726b351f"
        }
        }
        Or :
        {
        "src_descriptor":"foreign_exchange-vanilla-forwards",
        "dest_descriptor":"foreign_exchange-vanilla-forwards"
        }

        Example of request for Back Office :
        {
        "identifier":{
        "uid":"fc8b57b7-cc90-11ec-b784-8dfc726b351f"
        },
        "scope":"bank1"
        }
        Or :
        {
        "src_descriptor":"foreign_exchange-vanilla-forwards",
        "dest_descriptor":"foreign_exchange-vanilla-forwards",
        "scope":"bank1"
        }

        Example of response :
        {
        "data": {
        "uid": "",
        "srcDescriptor": "foreign_exchange-vanilla-options",
        "destDescriptor": "foreign_exchange-vanilla-options",
        "transformations": [
        {
        "name": "",
        "targetColumn": "snap_date",
        "sourceColumn": "submission_date",
        "rule": "",
        "description": ""
        }
        ],
        "scope": ""
        }
        }

        Example of error response :
        {
        "error":{
        "code":70,
        "message":"Can't get mapping rule: [[empty] of service [MAPPINGRULESET] does not exist in namespace [bank1]]."
        }
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EnableMappingRule(self, request, context):
        """EnableMappingRule is used to enable a mapping rule for a given descriptor pair.
        It accepts a DescriptorPairBasedGetDefinition object as its parameter, which specifies the source and destination descriptors for the mapping rule.
        The response from this it is a DescriptorPairBasedAcknowledgeResponse, which acknowledges the enablement of the mapping rule.

        Request:
        {
        "src_descriptor":"foreign_exchange-vanilla-options",
        "dest_descriptor":"foreign_exchange-vanilla-options"
        "scope": "Zbank1"
        }

        Response:
        {
        "data": {
        "uid": "",
        "src_descriptor":"foreign_exchange-vanilla-options",
        "dest_descriptor":"foreign_exchange-vanilla-options"
        }
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DisableMappingRule(self, request, context):
        """DisableMappingRule is used to disable a mapping rule for a given descriptor pair.
        It accepts a DescriptorPairBasedGetDefinition object as its parameter, which specifies the source and destination descriptors for the mapping rule.
        The response from this it is a DescriptorPairBasedAcknowledgeResponse, which acknowledges the disablement of the mapping rule.

        Request:
        {
        "src_descriptor":"foreign_exchange-vanilla-options",
        "dest_descriptor":"foreign_exchange-vanilla-options"
        "scope": "Zbank1"
        }

        Response:
        {
        "data": {
        "uid": "",
        "src_descriptor":"foreign_exchange-vanilla-options",
        "dest_descriptor":"foreign_exchange-vanilla-options"
        }
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListMappingRules(self, request, context):
        """ListMappingRules is used to retrieve a list of all mapping rules in the system.
        It accepts a ListRequest object as its parameter, which includes optional parameters for filtering the results.
        The response from this it is a MappingRuleList, which includes information about all mapping rules in the system that match the provided filter parameters.

        Example of request :
        {
        "scope":"global"
        }
        Or optionally use filter:
        {
        "scope":"global",
        "filter": ".*vanilla.*__.*vanilla.*" // all mapping rules from any vanilla to any vanilla
        }

        Example of response :
        {
        "data": {
        "results": [
        {
        "uid": "Djqreg7gTs7CV2rSyyucOWCFjK7ldgS9yQX0o0rEiV0=",
        "src_descriptor": "foreign_exchange-vanilla-forwards",
        "dest_descriptor": "foreign_exchange-vanilla-forwards"

        },
        {
        "uid": "Djqreg7gTs7CV2rSyyucOWCFjK7ldgS9yQX0o0rEiV0=",
        "src_descriptor": "foreign_exchange-vanilla-options",
        "dest_descriptor": "foreign_exchange-vanilla-options"
        }
        ]
        }
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListMappingRuleVersions(self, request, context):
        """ListMappingRuleVersions is used to retrieve a list of all versions of a mapping rule for a given descriptor pair.
        It accepts a DescriptorPairBasedGetDefinition object as its parameter, which specifies the source and destination descriptors for the mapping rule.
        The response from this it is a ListVersionResponse, which includes information about all versions of the mapping rule.

        Example of request :
        {
        "scope": "global",
        "src_descriptor":"foreign_exchange-vanilla-options",
        "dest_descriptor":"foreign_exchange-vanilla-options"
        }

        Example of response :
        {
        "data":{
        "versions":[
        {
        "versionId":"EKc9bpBGCbLJmBqOpP0FTqtNusxgZrgCheGXj_MTj7A=",
        "createdAt":"2022-05-05 11:33:59.0"
        },
        {
        "versionId":"JKLFLkhV3SC-fqO0L-WTswr5ttHLfnvF8rMlLnkafAc=",
        "createdAt":"2022-05-05 11:32:42.0"
        }
        ]
        }
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMappingRuleVersion(self, request, context):
        """GetMappingRuleVersion is used to retrieve a specific version of a mapping rule for a given descriptor pair.
        It accepts a DescriptorPairBasedVersionRequest object as its parameter, which includes the scope, source descriptor, destination descriptor, and version ID for the mapping rule.
        The response from it is a MappingRuleResponse, which includes information about the retrieved version of the mapping rule.

        Example of request : GET /api/v1/validation/rule/version/fx_fwd_1/fx_fwd_2/teTYb9Fs_lIOoPQJukM6dY3aJdiMqT-SdBPdvYfJAjk=

        Example of response :
        {
        "definition":"{"src_descriptor":"foreign_exchange-vanilla-forwards","dest_descriptor":"foreign_exchange-vanilla-forwards","transformations":[{"targetColumnName":"submission_date","sourceColumnName":"another_date"},{"rule":"{ \\"$to_upper\\": { \\"$trim\\" : \\"fx_test_for_bank1.submission_asset\\" }}","targetColumnName":"submission_asset", "name": "upper case asset", "description": "i am optional..."}]}"
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_MappingServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'AddMappingRule': grpc.unary_unary_rpc_method_handler(servicer.AddMappingRule, request_deserializer=common_dot_mapper__pb2.MappingRuleDefinition.FromString, response_serializer=common_dot_mapper__pb2.DescriptorPairBasedAcknowledgeResponse.SerializeToString), 'GetMappingRule': grpc.unary_unary_rpc_method_handler(servicer.GetMappingRule, request_deserializer=common_dot_mapper__pb2.DescriptorPairBasedGetDefinition.FromString, response_serializer=common_dot_mapper__pb2.MappingRuleResponse.SerializeToString), 'EnableMappingRule': grpc.unary_unary_rpc_method_handler(servicer.EnableMappingRule, request_deserializer=common_dot_mapper__pb2.DescriptorPairBasedGetDefinition.FromString, response_serializer=common_dot_mapper__pb2.DescriptorPairBasedAcknowledgeResponse.SerializeToString), 'DisableMappingRule': grpc.unary_unary_rpc_method_handler(servicer.DisableMappingRule, request_deserializer=common_dot_mapper__pb2.DescriptorPairBasedGetDefinition.FromString, response_serializer=common_dot_mapper__pb2.DescriptorPairBasedAcknowledgeResponse.SerializeToString), 'ListMappingRules': grpc.unary_unary_rpc_method_handler(servicer.ListMappingRules, request_deserializer=common_dot_gateway__base__pb2.ListRequest.FromString, response_serializer=common_dot_mapper__pb2.MappingRuleList.SerializeToString), 'ListMappingRuleVersions': grpc.unary_unary_rpc_method_handler(servicer.ListMappingRuleVersions, request_deserializer=common_dot_mapper__pb2.DescriptorPairBasedGetDefinition.FromString, response_serializer=common_dot_gateway__base__pb2.ListVersionResponse.SerializeToString), 'GetMappingRuleVersion': grpc.unary_unary_rpc_method_handler(servicer.GetMappingRuleVersion, request_deserializer=common_dot_mapper__pb2.DescriptorPairBasedVersionRequest.FromString, response_serializer=common_dot_mapper__pb2.MappingRuleResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('titanium.MappingService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class MappingService(object):
    """MappingService is service that responsible for rules that related to
    transformation of submission data into system definition for further calculation and analysis 
    """

    @staticmethod
    def AddMappingRule(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.MappingService/AddMappingRule', common_dot_mapper__pb2.MappingRuleDefinition.SerializeToString, common_dot_mapper__pb2.DescriptorPairBasedAcknowledgeResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetMappingRule(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.MappingService/GetMappingRule', common_dot_mapper__pb2.DescriptorPairBasedGetDefinition.SerializeToString, common_dot_mapper__pb2.MappingRuleResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EnableMappingRule(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.MappingService/EnableMappingRule', common_dot_mapper__pb2.DescriptorPairBasedGetDefinition.SerializeToString, common_dot_mapper__pb2.DescriptorPairBasedAcknowledgeResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DisableMappingRule(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.MappingService/DisableMappingRule', common_dot_mapper__pb2.DescriptorPairBasedGetDefinition.SerializeToString, common_dot_mapper__pb2.DescriptorPairBasedAcknowledgeResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListMappingRules(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.MappingService/ListMappingRules', common_dot_gateway__base__pb2.ListRequest.SerializeToString, common_dot_mapper__pb2.MappingRuleList.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListMappingRuleVersions(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.MappingService/ListMappingRuleVersions', common_dot_mapper__pb2.DescriptorPairBasedGetDefinition.SerializeToString, common_dot_gateway__base__pb2.ListVersionResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetMappingRuleVersion(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.MappingService/GetMappingRuleVersion', common_dot_mapper__pb2.DescriptorPairBasedVersionRequest.SerializeToString, common_dot_mapper__pb2.MappingRuleResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)