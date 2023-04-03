"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2
from ..common import validation_service_pb2 as common_dot_validation__service__pb2

class ValidatorServiceStub(object):
    """ValidatorService is a service that manages validation rules to ensure data quality.
    Validation Rules represent a specific and independent data quality condition or scenario to exercise.
    Validation rules evaluate as true or false and are applied only to the rows specific by their parent criteria element.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddValidationRule = channel.unary_unary('/titanium.ValidatorService/AddValidationRule', request_serializer=common_dot_validation__service__pb2.ValidationRuleDefinition.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.AcknowledgeResponse.FromString)
        self.GetValidationRule = channel.unary_unary('/titanium.ValidatorService/GetValidationRule', request_serializer=common_dot_gateway__base__pb2.GetDefinition.SerializeToString, response_deserializer=common_dot_validation__service__pb2.GetValidationRuleResponse.FromString)
        self.DisableValidationRule = channel.unary_unary('/titanium.ValidatorService/DisableValidationRule', request_serializer=common_dot_gateway__base__pb2.GetDefinition.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.AcknowledgeResponse.FromString)
        self.EnableValidationRule = channel.unary_unary('/titanium.ValidatorService/EnableValidationRule', request_serializer=common_dot_gateway__base__pb2.GetDefinition.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.AcknowledgeResponse.FromString)
        self.ListValidationRules = channel.unary_unary('/titanium.ValidatorService/ListValidationRules', request_serializer=common_dot_gateway__base__pb2.ListRequest.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.ListRuleResponse.FromString)
        self.ListValidationRuleVersions = channel.unary_unary('/titanium.ValidatorService/ListValidationRuleVersions', request_serializer=common_dot_gateway__base__pb2.GetDefinition.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.ListVersionResponse.FromString)
        self.GetValidationRuleVersion = channel.unary_unary('/titanium.ValidatorService/GetValidationRuleVersion', request_serializer=common_dot_gateway__base__pb2.VersionRequest.SerializeToString, response_deserializer=common_dot_validation__service__pb2.GetValidationRuleResponse.FromString)
        self.GetGeneratedValidationRule = channel.unary_unary('/titanium.ValidatorService/GetGeneratedValidationRule', request_serializer=common_dot_gateway__base__pb2.GetDefinition.SerializeToString, response_deserializer=common_dot_validation__service__pb2.GetGeneratedValidationRuleResponse.FromString)
        self.ListGeneratedValidationRuleVersions = channel.unary_unary('/titanium.ValidatorService/ListGeneratedValidationRuleVersions', request_serializer=common_dot_gateway__base__pb2.GetDefinition.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.ListVersionResponse.FromString)
        self.GetGeneratedValidationRuleVersion = channel.unary_unary('/titanium.ValidatorService/GetGeneratedValidationRuleVersion', request_serializer=common_dot_gateway__base__pb2.VersionRequest.SerializeToString, response_deserializer=common_dot_validation__service__pb2.GetGeneratedValidationRuleResponse.FromString)
        self.RdlCheck = channel.unary_unary('/titanium.ValidatorService/RdlCheck', request_serializer=common_dot_validation__service__pb2.RdlCheckRequest.SerializeToString, response_deserializer=common_dot_gateway__base__pb2.MessageResponse.FromString)

class ValidatorServiceServicer(object):
    """ValidatorService is a service that manages validation rules to ensure data quality.
    Validation Rules represent a specific and independent data quality condition or scenario to exercise.
    Validation rules evaluate as true or false and are applied only to the rows specific by their parent criteria element.
    """

    def AddValidationRule(self, request, context):
        """AddValidationRule is a method used to add a validation rule to the system.
        Backoffice users can create a new validation ruleset in the 'global' scope, for each asset class.
        Participant users can create a new validation ruleset in its own scope, for each asset class.
        Backoffice users can represent any participant and create a new validation ruleset in that participant's scope.
        The default scope is used if no scope is given in the request ('global' for the operator, participant scope for that participant user).
        The authorization will be fetched from the user's token. It will do an update if a validation rule with the same name already exists.

        Request for backoffice user:
        {
        "definition": {
        "descriptor_name":"foreign_exchange-vanilla-options",
        "criteria":[
        {
        "name":"FX-V-FXO: Option Instrument Parameter: Forward Points",
        "description":"This criteria element contains validation rules that will be applied to all fx-vanilla-options data submission rows where option_instrument_parameter equals "Forward Points".",
        "tags":[
        "forward points"
        ],
        "metadata":[

        ],
        "rule":"["foreign_exchange-vanilla-options.option_instrument_parameter","$eq_case_insensitive","Forward Points"]",
        "validations":[
        {
        "name":"FX-V-FXO: Forward Points: Forward Conversion Factor: Exiting Value Check",
        "severity":1,
        "rule_type":"input_data",
        "tags":[

        ],
        "description":"Compare the fwrd_conversion_factor for a given underlying against the expected values.",
        "rule":"[ { "$lut_name": "conversion_factor", "$get": [ "foreign_exchange-vanilla-options.underlying" ] }, "$eq", "foreign_exchange-vanilla-options.fwrd_conversion_factor" ]",
        "error":{
        "message":"[%s] is not a conversion factor used in consensus. Please update the conversion factor for this underlying -- [%s].",
        "message_args":[
        "foreign_exchange-vanilla-options.fwrd_conversion_factor",
        "foreign_exchange-vanilla-options.underlying"
        ]
        }
        }
        ]
        }
        ]
        },
        "scope": "global",
        "descriptor_name": "foreign_exchange-vanilla-options"
        }

        Response:
        {
        "data": {
        "uid": "ac49453d-cc9c-11ec-8bac-5314d58ea570",
        "descriptor_name": "fx_forward"
        }
        }

        Error response:

        Push to non ‘global’ scope :
        {
        "error": {
        "code": 70,
        "message": "Invalid argument: only support 'global' scope"
        }
        }

        Unauthorized user :
        {
        "error": {
        "code": 70,
        "message": "Invalid auth token - only operator is allowed to add validation rules"
        }
        }

        Missing argument :
        {
        "error": {
        "code": 70,
        "message": "Missing argument: descriptor_name"
        }
        }

        Invalid rule definition - rule col mismatch with descriptor :
        {
        "error": {
        "code": 70,
        "message": "Rule [fx_fwd] compile failed, details: Column [submission_clienttt] not found in schema [fx_forward]"
        }
        }

        Invalid rule definition - RDL syntax error :
        {
        "error": {
        "code": 70,
        "message": "Rule [fx_fwd] compile failed, details: line 1:14 no viable alternative at input '[{"$lower":"fx_forward.submission_service"'"
        }
        }

        Dependencies not found - dependencies could be: descriptor, named lut, custom function :
        {
        "error": {
        "code": 70,
        "message": "Rule [fx_fwd] compile failed, details: Invalid rule expression [ { "$lut_name" : "tenor", "$exist" : ["fx_forward.submission_tenor"] } ]
	err: com.peernova.api.searchmetadata.metadata.exceptions.MetadataNotFoundException: No Look Up Table by name [tenor] found in scope [global]"
        }
        }

        Ruleset with same name already exist :
        {
        "error": {
        "code": 70,
        "message": "Validation rule for descriptor [fx_fwd] already exist"
        }
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetValidationRule(self, request, context):
        """GetValidationRule method retrieves information about a validation rule.
        Both back office users and participant users can view validation rulesets.
        The default scope is used if no scope is given in the request. Authorization is fetched from the user's token.
        The rule can be retrieved by either descriptor name or UID.
        If multiple versions of the rule exist, this method returns the latest version.

        Example of Request:
        {
        "descriptor_name": "fx_fwd"
        }


        Or:
        {
        "uid": "ac49453d-cc9c-11ec-8bac-5314d58ea570"
        }



        Example of Response:
        {
        "data": {
        "uid": "",
        "definition": {
        "descriptorName": "foreign_exchange-vanilla-options",
        "criteria": [
        {
        "name": "FX-V-FXO: Option Instrument Parameter: Forward Points",
        "description": "This criteria element contains validation rules that will be applied to all fx-vanilla-options data submission rows where option_instrument_parameter equals "Forward Points".",
        "rule": "["foreign_exchange-vanilla-options.option_instrument_parameter","$eq_case_insensitive","Forward Points"]",
        "tags": [
        "forward points"
        ],
        "metadata": [],
        "validations": [
        {
        "name": "FX-V-FXO: Forward Points: Forward Conversion Factor: Exiting Value Check",
        "description": "Compare the fwrd_conversion_factor for a given underlying against the expected values.",
        "rule": "[ { "$lut_name": "conversion_factor", "$get": [ "foreign_exchange-vanilla-options.underlying" ] }, "$eq", "foreign_exchange-vanilla-options.fwrd_conversion_factor" ]",
        "ruleType": "INPUT_DATA",
        "severity": 1,
        "tags": [],
        "error": {
        "message": "[%s] is not a conversion factor used in consensus. Please update the conversion factor for this underlying -- [%s].",
        "messageArgs": [
        "foreign_exchange-vanilla-options.fwrd_conversion_factor",
        "foreign_exchange-vanilla-options.underlying"
        ]
        },
        "filter": ""
        }
        ]
        }
        ]
        },
        "scope": "global",
        "descriptorName": "foreign_exchange-vanilla-options"
        }
        }

        Example of Error response:

        Missing argument:
        {
        "error": {
        "code": 70,
        "message": "Missing argument: need either descriptor name or uid to get validation rule"
        }
        }

        Resource not found :
        {
        "error": {
        "code": 70,
        "message": "Rule [fx_fwd] not found, details: [fx_fwd] of service [VALIDATIONRULESET] does not exist in namespace [global]"
        }
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DisableValidationRule(self, request, context):
        """DisableValidationRule method disables a validation rule in the system.
        The request includes the descriptor name and scope of the rule.
        Example of Request:
        {
        "descriptor_name" : "foreign_exchange-vanilla-forwards",
        "scope": "global"
        }

        Example of Response:
        {
        "data": {
        "uid": "",
        "descriptor_name": "foreign_exchange-vanilla-forwards"
        }
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EnableValidationRule(self, request, context):
        """EnableValidationRule method enables a validation rule that has been previously disabled.
        The request includes the descriptor name and scope of the rule.
        Example of Request:
        {
        "descriptor_name" : "foreign_exchange-vanilla-forwards",
        "scope": "global"
        }

        Example of Response:
        {
        "data": {
        "uid": "",
        "descriptor_name": "foreign_exchange-vanilla-forwards"
        }
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListValidationRules(self, request, context):
        """ListValidationRules method is used to retrieve a list of validation rule names.
        Both back office users and participant users can retrieve validation rulesets, but the scope and authorization will depend on the user.
        The default scope is used if no scope is specified in the request.
        The request may include an optional filter and orderBy parameter to refine the search results.
        Pagination is also supported. The response will include a list of rule names matching the filter criteria.

        Example of Request:
        {
        "scope": "global",
        "filter": ".*exchange.*",
        "orderBy": {
        	"order": "DESC"
        }
        }

        Example of Response:
        {
        "data": {
        "results": [
        {
        "uid": "",
        "descriptor_name": "foreign_exchange-vanilla-options"
        },
        {
        "uid": "",
        "descriptor_name": "foreign_exchange-vanilla-forwards"
        },
        {
        "uid": "",
        "descriptor_name": "foreign_exchange-exotics-tarfs"
        }
        ]
        }
        }

        Example of Request with pagination:
        {
        "scope": "global",
        "filter": ".*exchange.*",
        "orderBy": {
        	"order": "DESC"
        },
        "limit": {
        	"value": 2
        },
        "offset": 1
        }

        Example of Response:
        {
        "data": {
        "results": [
        {
        "uid": "",
        "descriptor_name": "foreign_exchange-vanilla-forwards"
        },
        {
        "uid": "",
        "descriptor_name": "foreign_exchange-exotics-tarfs"
        }
        ]
        }
        }

        Example of Error response:
        not ‘global’ scope:
        {
        "error": {
        "code": 70,
        "message": "Invalid argument: only support 'global' scope"
        }
        }

        Invalid filter/regex:
        {
        "error": {
        "code": 70,
        "message": "Failed to list rules: Dangling meta character '*' near index 0
*May*
^"
        }
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListValidationRuleVersions(self, request, context):
        """ListValidationRuleVersions method is used to retrieve a list of versions for a given validation rule.
        Both back office users and participant users can retrieve versions of validation rulesets, but the scope will depend on the user.
        The request must specify the descriptor name for the validation rule.
        The response will include a list of versions and their created timestamp.
        If the requested rule is not found, an error response will be returned.

        Example of Request:
        {
        "descriptor_name": "fx_fwd"
        }

        Example of Response:
        {
        "data": {
        "versions": [
        {
        "versionId": "teTYb9Fs_lIOoPQJukM6dY3aJdiMqT-SdBPdvYfJAjk=",
        "createdAt": "2022-05-04 16:20:58.0"
        },
        {
        "versionId": "mwpGZcWNc2zFgweB5rcNmAbcxqekM_zUCdpVrl_V6BM=",
        "createdAt": "2022-05-04 16:17:19.0"
        },
        {
        "versionId": "6pfCXN2rFnIAMoDHy7VIFh6HmoyDu3njXkpwzeTp2nc=",
        "createdAt": "2022-05-04 15:02:00.0"
        }
        ]
        }
        }

        Example of Error response:
        Resource not found:
        {
        "error": {
        "code": 70,
        "message": "Failed to get rule [fx_fwd] versions, details: Rule [fx_fwd_validation] not found"
        }
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetValidationRuleVersion(self, request, context):
        """This is a method that allows both back office users and regular users to retrieve a specific version of a ruleset given the descriptor name and version ID.
        The ruleset is used for validation purposes and contains criteria and rules for validating data submissions.
        Back office users can retrieve a particular version of a ruleset from any scope, while participant users can only retrieve a version of a ruleset from either the global scope or their own scope.

        Example of Request:
        GET /api/v1/validation/rule/version/fx_fwd_May04/teTYb9Fs_lIOoPQJukM6dY3aJdiMqT-SdBPdvYfJAjk=

        Example of Response:
        {
        "data": {
        "uid": "",
        "definition": {
        "descriptorName": "foreign_exchange-vanilla-options",
        "criteria": [
        {
        "name": "FX-V-FXO: Option Instrument Parameter: Forward Points",
        "description": "This criteria element contains validation rules that will be applied to all fx-vanilla-options data submission rows where option_instrument_parameter equals "Forward Points".",
        "rule": "["foreign_exchange-vanilla-options.option_instrument_parameter","$eq_case_insensitive","Forward Points"]",
        "tags": [
        "forward points"
        ],
        "metadata": [],
        "validations": [
        {
        "name": "FX-V-FXO: Forward Points: Forward Conversion Factor: Exiting Value Check",
        "description": "Compare the fwrd_conversion_factor for a given underlying against the expected values.",
        "rule": "[ { "$lut_name": "conversion_factor", "$get": [ "foreign_exchange-vanilla-options.underlying" ] }, "$eq", "foreign_exchange-vanilla-options.fwrd_conversion_factor" ]",
        "ruleType": "INPUT_DATA",
        "severity": 1,
        "tags": [],
        "error": {
        "message": "[%s] is not a conversion factor used in consensus. Please update the conversion factor for this underlying -- [%s].",
        "messageArgs": [
        "foreign_exchange-vanilla-options.fwrd_conversion_factor",
        "foreign_exchange-vanilla-options.underlying"
        ]
        },
        "filter": ""
        }
        ]
        }
        ]
        },
        "scope": "global",
        "descriptorName": "foreign_exchange-vanilla-options"
        }
        }

        Example of Error response:
        Resource not found:
        {
        "error": {
        "code": 70,
        "message": "Failed to get rule [fx_fwd_May04], details: MetaData entity not found: name [fx_fwd_May04] version: [teTYb9Fs_lIOoPQJukM6dY3aJdiMqT-SdBPdvYfJAjk] in namespace: [global]"
        }
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetGeneratedValidationRule(self, request, context):
        """GetGeneratedValidationRule method allows back office users to view all generated validation rulesets, including Java rulesets.
        Participant users can only view global generated validation rulesets and rulesets within their own scope.
        If no scope is given in the request, the default scope is used ("global" for operators and participant scope for the participant user).
        Authorization is fetched from the user's token.
        This method returns the latest version of the generated ruleset if multiple versions exist.

        Example of Request:
        {
        "descriptor_name": "foreign_exchange-vanilla-forwards"
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListGeneratedValidationRuleVersions(self, request, context):
        """ListGeneratedValidationRuleVersions method returns a list of generated ruleset version IDs along with their creation timestamps.
        The request requires a descriptor name. If the requested ruleset is not found, an error response is returned.

        Example of Request:
        {
        "descriptor_name": "fx_fwd"
        }


        Example of Response:
        {
        "data": {
        "versions": [
        {
        "versionId": "teTYb9Fs_lIOoPQJukM6dY3aJdiMqT-SdBPdvYfJAjk=",
        "createdAt": "2022-05-04 16:20:58.0"
        },
        {
        "versionId": "mwpGZcWNc2zFgweB5rcNmAbcxqekM_zUCdpVrl_V6BM=",
        "createdAt": "2022-05-04 16:17:19.0"
        },
        {
        "versionId": "6pfCXN2rFnIAMoDHy7VIFh6HmoyDu3njXkpwzeTp2nc=",
        "createdAt": "2022-05-04 15:02:00.0"
        }
        ]
        }
        }

        Example of Error response:
        Resource not found:
        {
        "error": {
        "code": 70,
        "message": "Failed to get rule [fx_fwd] versions, details: Rule [fx_fwd] not found"
        }
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetGeneratedValidationRuleVersion(self, request, context):
        """GetGeneratedValidationRuleVersion method allows the user to view a particular version of a generated ruleset.
        The request requires a descriptor name and a version ID.
        If the requested ruleset version is not found, an error response is returned.

        Example of Request:
        GET /api/v1/validation/rule/generated/version/foreign_exchange-vanilla-forwards
        /QHF5uuOTjGprb3FRsI7ybBnU6-Ub32Xq8Q399PtQWeQ=
        {
        "scope": "global"
        }

        Example of Response:
        {
        "data": {
        "versions": [
        {
        "versionId": "teTYb9Fs_lIOoPQJukM6dY3aJdiMqT-SdBPdvYfJAjk=",
        "createdAt": "2022-05-04 16:20:58.0"
        },
        {
        "versionId": "mwpGZcWNc2zFgweB5rcNmAbcxqekM_zUCdpVrl_V6BM=",
        "createdAt": "2022-05-04 16:17:19.0"
        },
        {
        "versionId": "6pfCXN2rFnIAMoDHy7VIFh6HmoyDu3njXkpwzeTp2nc=",
        "createdAt": "2022-05-04 15:02:00.0"
        }
        ]
        }
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RdlCheck(self, request, context):
        """RdlCheck method checks the syntax of a given RDL (Rule Description Language) expression.
        It takes a RdlCheckRequest message as input and returns a MessageResponse message.

        Example of Request:
        {
        "rdl": "["a", "$eq", "b""
        }

        Example of Response:
        {
        "data": {
        "message": "success"
        }
        }

        Example of Error response:
        Resource not found:
        {
        "error": {
        "code": 69,
        "message": "rdl [["a", "$eq", "b"] cannot be parsed. Error: line 1:16 missing ']' at '<EOF>'"
        }
        }
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_ValidatorServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'AddValidationRule': grpc.unary_unary_rpc_method_handler(servicer.AddValidationRule, request_deserializer=common_dot_validation__service__pb2.ValidationRuleDefinition.FromString, response_serializer=common_dot_gateway__base__pb2.AcknowledgeResponse.SerializeToString), 'GetValidationRule': grpc.unary_unary_rpc_method_handler(servicer.GetValidationRule, request_deserializer=common_dot_gateway__base__pb2.GetDefinition.FromString, response_serializer=common_dot_validation__service__pb2.GetValidationRuleResponse.SerializeToString), 'DisableValidationRule': grpc.unary_unary_rpc_method_handler(servicer.DisableValidationRule, request_deserializer=common_dot_gateway__base__pb2.GetDefinition.FromString, response_serializer=common_dot_gateway__base__pb2.AcknowledgeResponse.SerializeToString), 'EnableValidationRule': grpc.unary_unary_rpc_method_handler(servicer.EnableValidationRule, request_deserializer=common_dot_gateway__base__pb2.GetDefinition.FromString, response_serializer=common_dot_gateway__base__pb2.AcknowledgeResponse.SerializeToString), 'ListValidationRules': grpc.unary_unary_rpc_method_handler(servicer.ListValidationRules, request_deserializer=common_dot_gateway__base__pb2.ListRequest.FromString, response_serializer=common_dot_gateway__base__pb2.ListRuleResponse.SerializeToString), 'ListValidationRuleVersions': grpc.unary_unary_rpc_method_handler(servicer.ListValidationRuleVersions, request_deserializer=common_dot_gateway__base__pb2.GetDefinition.FromString, response_serializer=common_dot_gateway__base__pb2.ListVersionResponse.SerializeToString), 'GetValidationRuleVersion': grpc.unary_unary_rpc_method_handler(servicer.GetValidationRuleVersion, request_deserializer=common_dot_gateway__base__pb2.VersionRequest.FromString, response_serializer=common_dot_validation__service__pb2.GetValidationRuleResponse.SerializeToString), 'GetGeneratedValidationRule': grpc.unary_unary_rpc_method_handler(servicer.GetGeneratedValidationRule, request_deserializer=common_dot_gateway__base__pb2.GetDefinition.FromString, response_serializer=common_dot_validation__service__pb2.GetGeneratedValidationRuleResponse.SerializeToString), 'ListGeneratedValidationRuleVersions': grpc.unary_unary_rpc_method_handler(servicer.ListGeneratedValidationRuleVersions, request_deserializer=common_dot_gateway__base__pb2.GetDefinition.FromString, response_serializer=common_dot_gateway__base__pb2.ListVersionResponse.SerializeToString), 'GetGeneratedValidationRuleVersion': grpc.unary_unary_rpc_method_handler(servicer.GetGeneratedValidationRuleVersion, request_deserializer=common_dot_gateway__base__pb2.VersionRequest.FromString, response_serializer=common_dot_validation__service__pb2.GetGeneratedValidationRuleResponse.SerializeToString), 'RdlCheck': grpc.unary_unary_rpc_method_handler(servicer.RdlCheck, request_deserializer=common_dot_validation__service__pb2.RdlCheckRequest.FromString, response_serializer=common_dot_gateway__base__pb2.MessageResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('titanium.ValidatorService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class ValidatorService(object):
    """ValidatorService is a service that manages validation rules to ensure data quality.
    Validation Rules represent a specific and independent data quality condition or scenario to exercise.
    Validation rules evaluate as true or false and are applied only to the rows specific by their parent criteria element.
    """

    @staticmethod
    def AddValidationRule(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.ValidatorService/AddValidationRule', common_dot_validation__service__pb2.ValidationRuleDefinition.SerializeToString, common_dot_gateway__base__pb2.AcknowledgeResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetValidationRule(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.ValidatorService/GetValidationRule', common_dot_gateway__base__pb2.GetDefinition.SerializeToString, common_dot_validation__service__pb2.GetValidationRuleResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DisableValidationRule(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.ValidatorService/DisableValidationRule', common_dot_gateway__base__pb2.GetDefinition.SerializeToString, common_dot_gateway__base__pb2.AcknowledgeResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EnableValidationRule(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.ValidatorService/EnableValidationRule', common_dot_gateway__base__pb2.GetDefinition.SerializeToString, common_dot_gateway__base__pb2.AcknowledgeResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListValidationRules(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.ValidatorService/ListValidationRules', common_dot_gateway__base__pb2.ListRequest.SerializeToString, common_dot_gateway__base__pb2.ListRuleResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListValidationRuleVersions(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.ValidatorService/ListValidationRuleVersions', common_dot_gateway__base__pb2.GetDefinition.SerializeToString, common_dot_gateway__base__pb2.ListVersionResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetValidationRuleVersion(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.ValidatorService/GetValidationRuleVersion', common_dot_gateway__base__pb2.VersionRequest.SerializeToString, common_dot_validation__service__pb2.GetValidationRuleResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetGeneratedValidationRule(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.ValidatorService/GetGeneratedValidationRule', common_dot_gateway__base__pb2.GetDefinition.SerializeToString, common_dot_validation__service__pb2.GetGeneratedValidationRuleResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListGeneratedValidationRuleVersions(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.ValidatorService/ListGeneratedValidationRuleVersions', common_dot_gateway__base__pb2.GetDefinition.SerializeToString, common_dot_gateway__base__pb2.ListVersionResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetGeneratedValidationRuleVersion(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.ValidatorService/GetGeneratedValidationRuleVersion', common_dot_gateway__base__pb2.VersionRequest.SerializeToString, common_dot_validation__service__pb2.GetGeneratedValidationRuleResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RdlCheck(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/titanium.ValidatorService/RdlCheck', common_dot_validation__service__pb2.RdlCheckRequest.SerializeToString, common_dot_gateway__base__pb2.MessageResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)