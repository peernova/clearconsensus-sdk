"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ..google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2
from ..common import custom_function_pb2 as common_dot_custom__function__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$public/custom_function_service.proto\x12\x08titanium\x1a\x1cgoogle/api/annotations.proto\x1a\x19common/gateway_base.proto\x1a\x1ccommon/custom_function.proto2\xaa\x04\n\x15CustomFunctionService\x12s\n\x11AddCustomFunction\x12\x18.titanium.CustomFunction\x1a\x1d.titanium.AcknowledgeResponse"%\x82\xd3\xe4\x93\x02\x1f"\x1a/api/v1/customfunction/add:\x01*\x12\x8d\x01\n\x11GetCustomFunction\x12%.titanium.CustomFunctionGetDefinition\x1a*.titanium.CustomFunctionDefinitionResponse"%\x82\xd3\xe4\x93\x02\x1f"\x1a/api/v1/customfunction/get:\x01*\x12\x88\x01\n\x13ListCustomFunctions\x12#.titanium.ListCustomFunctionRequest\x1a$.titanium.ListCustomFunctionResponse"&\x82\xd3\xe4\x93\x02 "\x1b/api/v1/customfunction/list:\x01*\x12\x80\x01\n\x1aListCustomFunctionVersions\x12\x17.titanium.GetDefinition\x1a\x1d.titanium.ListVersionResponse"*\x82\xd3\xe4\x93\x02$"\x1f/api/v1/customfunction/versions:\x01*B|\n com.peernova.titanium.interfacesB CustomFunctionServiceProtoPublicP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/publicb\x06proto3')
_CUSTOMFUNCTIONSERVICE = DESCRIPTOR.services_by_name['CustomFunctionService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesB CustomFunctionServiceProtoPublicP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/public'
    _CUSTOMFUNCTIONSERVICE.methods_by_name['AddCustomFunction']._options = None
    _CUSTOMFUNCTIONSERVICE.methods_by_name['AddCustomFunction']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1f"\x1a/api/v1/customfunction/add:\x01*'
    _CUSTOMFUNCTIONSERVICE.methods_by_name['GetCustomFunction']._options = None
    _CUSTOMFUNCTIONSERVICE.methods_by_name['GetCustomFunction']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1f"\x1a/api/v1/customfunction/get:\x01*'
    _CUSTOMFUNCTIONSERVICE.methods_by_name['ListCustomFunctions']._options = None
    _CUSTOMFUNCTIONSERVICE.methods_by_name['ListCustomFunctions']._serialized_options = b'\x82\xd3\xe4\x93\x02 "\x1b/api/v1/customfunction/list:\x01*'
    _CUSTOMFUNCTIONSERVICE.methods_by_name['ListCustomFunctionVersions']._options = None
    _CUSTOMFUNCTIONSERVICE.methods_by_name['ListCustomFunctionVersions']._serialized_options = b'\x82\xd3\xe4\x93\x02$"\x1f/api/v1/customfunction/versions:\x01*'
    _CUSTOMFUNCTIONSERVICE._serialized_start = 138
    _CUSTOMFUNCTIONSERVICE._serialized_end = 692