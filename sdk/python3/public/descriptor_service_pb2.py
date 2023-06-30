"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ..google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2
from ..common import descriptor_pb2 as common_dot_descriptor__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fpublic/descriptor_service.proto\x12\x08titanium\x1a\x1cgoogle/api/annotations.proto\x1a\x19common/gateway_base.proto\x1a\x17common/descriptor.proto2\xf6\x07\n\x11DescriptorService\x12q\n\rAddDescriptor\x12\x1e.titanium.DescriptorDefinition\x1a\x1d.titanium.AcknowledgeResponse"!\x82\xd3\xe4\x93\x02\x1b"\x16/api/v1/descriptor/add:\x01*\x12s\n\rGetDescriptor\x12\x17.titanium.GetDefinition\x1a&.titanium.DescriptorDefinitionResponse"!\x82\xd3\xe4\x93\x02\x1b"\x16/api/v1/descriptor/get:\x01*\x12w\n\x10EnableDescriptor\x12\x1e.titanium.EnableDisableRequest\x1a\x1d.titanium.AcknowledgeResponse"$\x82\xd3\xe4\x93\x02\x1e"\x19/api/v1/descriptor/enable:\x01*\x12y\n\x11DisableDescriptor\x12\x1e.titanium.EnableDisableRequest\x1a\x1d.titanium.AcknowledgeResponse"%\x82\xd3\xe4\x93\x02\x1f"\x1a/api/v1/descriptor/disable:\x01*\x12f\n\x0fListDescriptors\x12\x15.titanium.ListRequest\x1a\x18.titanium.DescriptorList""\x82\xd3\xe4\x93\x02\x1c"\x17/api/v1/descriptor/list:\x01*\x12x\n\x16ListDescriptorVersions\x12\x17.titanium.GetDefinition\x1a\x1d.titanium.ListVersionResponse"&\x82\xd3\xe4\x93\x02 "\x1b/api/v1/descriptor/versions:\x01*\x12\x98\x01\n\x14GetDescriptorVersion\x12\x18.titanium.VersionRequest\x1a&.titanium.DescriptorDefinitionResponse">\x82\xd3\xe4\x93\x028\x126/api/v1/descriptor/version/{scope}/{name}/{version_id}\x12\x87\x01\n\x16DescriptorDependencies\x12\x17.titanium.GetDefinition\x1a(.titanium.DescriptorDependenciesResponse"*\x82\xd3\xe4\x93\x02$"\x1f/api/v1/descriptor/dependencies:\x01*2\x96\x08\n\x13DbDescriptorService\x12v\n\x0fAddDbDescriptor\x12\x1e.titanium.DescriptorDefinition\x1a\x1d.titanium.AcknowledgeResponse"$\x82\xd3\xe4\x93\x02\x1e"\x19/api/v1/db/descriptor/add:\x01*\x12x\n\x0fGetDbDescriptor\x12\x17.titanium.GetDefinition\x1a&.titanium.DescriptorDefinitionResponse"$\x82\xd3\xe4\x93\x02\x1e"\x19/api/v1/db/descriptor/get:\x01*\x12|\n\x12EnableDbDescriptor\x12\x1e.titanium.EnableDisableRequest\x1a\x1d.titanium.AcknowledgeResponse"\'\x82\xd3\xe4\x93\x02!"\x1c/api/v1/db/descriptor/enable:\x01*\x12~\n\x13DisableDbDescriptor\x12\x1e.titanium.EnableDisableRequest\x1a\x1d.titanium.AcknowledgeResponse"(\x82\xd3\xe4\x93\x02""\x1d/api/v1/db/descriptor/disable:\x01*\x12k\n\x11ListDbDescriptors\x12\x15.titanium.ListRequest\x1a\x18.titanium.DescriptorList"%\x82\xd3\xe4\x93\x02\x1f"\x1a/api/v1/db/descriptor/list:\x01*\x12}\n\x18ListDbDescriptorVersions\x12\x17.titanium.GetDefinition\x1a\x1d.titanium.ListVersionResponse")\x82\xd3\xe4\x93\x02#"\x1e/api/v1/db/descriptor/versions:\x01*\x12\x95\x01\n\x16GetDbDescriptorVersion\x12\x18.titanium.VersionRequest\x1a&.titanium.DescriptorDefinitionResponse"9\x82\xd3\xe4\x93\x023\x121/api/v1/db/descriptor/version/{name}/{version_id}\x12\x8a\x01\n\x16DescriptorDependencies\x12\x17.titanium.GetDefinition\x1a(.titanium.DescriptorDependenciesResponse"-\x82\xd3\xe4\x93\x02\'""/api/v1/db/descriptor/dependencies:\x01*Bq\n com.peernova.titanium.interfacesB\x15DescriptorProtoPublicP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/publicb\x06proto3')
_DESCRIPTORSERVICE = DESCRIPTOR.services_by_name['DescriptorService']
_DBDESCRIPTORSERVICE = DESCRIPTOR.services_by_name['DbDescriptorService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesB\x15DescriptorProtoPublicP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/public'
    _DESCRIPTORSERVICE.methods_by_name['AddDescriptor']._options = None
    _DESCRIPTORSERVICE.methods_by_name['AddDescriptor']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1b"\x16/api/v1/descriptor/add:\x01*'
    _DESCRIPTORSERVICE.methods_by_name['GetDescriptor']._options = None
    _DESCRIPTORSERVICE.methods_by_name['GetDescriptor']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1b"\x16/api/v1/descriptor/get:\x01*'
    _DESCRIPTORSERVICE.methods_by_name['EnableDescriptor']._options = None
    _DESCRIPTORSERVICE.methods_by_name['EnableDescriptor']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1e"\x19/api/v1/descriptor/enable:\x01*'
    _DESCRIPTORSERVICE.methods_by_name['DisableDescriptor']._options = None
    _DESCRIPTORSERVICE.methods_by_name['DisableDescriptor']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1f"\x1a/api/v1/descriptor/disable:\x01*'
    _DESCRIPTORSERVICE.methods_by_name['ListDescriptors']._options = None
    _DESCRIPTORSERVICE.methods_by_name['ListDescriptors']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1c"\x17/api/v1/descriptor/list:\x01*'
    _DESCRIPTORSERVICE.methods_by_name['ListDescriptorVersions']._options = None
    _DESCRIPTORSERVICE.methods_by_name['ListDescriptorVersions']._serialized_options = b'\x82\xd3\xe4\x93\x02 "\x1b/api/v1/descriptor/versions:\x01*'
    _DESCRIPTORSERVICE.methods_by_name['GetDescriptorVersion']._options = None
    _DESCRIPTORSERVICE.methods_by_name['GetDescriptorVersion']._serialized_options = b'\x82\xd3\xe4\x93\x028\x126/api/v1/descriptor/version/{scope}/{name}/{version_id}'
    _DESCRIPTORSERVICE.methods_by_name['DescriptorDependencies']._options = None
    _DESCRIPTORSERVICE.methods_by_name['DescriptorDependencies']._serialized_options = b'\x82\xd3\xe4\x93\x02$"\x1f/api/v1/descriptor/dependencies:\x01*'
    _DBDESCRIPTORSERVICE.methods_by_name['AddDbDescriptor']._options = None
    _DBDESCRIPTORSERVICE.methods_by_name['AddDbDescriptor']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1e"\x19/api/v1/db/descriptor/add:\x01*'
    _DBDESCRIPTORSERVICE.methods_by_name['GetDbDescriptor']._options = None
    _DBDESCRIPTORSERVICE.methods_by_name['GetDbDescriptor']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1e"\x19/api/v1/db/descriptor/get:\x01*'
    _DBDESCRIPTORSERVICE.methods_by_name['EnableDbDescriptor']._options = None
    _DBDESCRIPTORSERVICE.methods_by_name['EnableDbDescriptor']._serialized_options = b'\x82\xd3\xe4\x93\x02!"\x1c/api/v1/db/descriptor/enable:\x01*'
    _DBDESCRIPTORSERVICE.methods_by_name['DisableDbDescriptor']._options = None
    _DBDESCRIPTORSERVICE.methods_by_name['DisableDbDescriptor']._serialized_options = b'\x82\xd3\xe4\x93\x02""\x1d/api/v1/db/descriptor/disable:\x01*'
    _DBDESCRIPTORSERVICE.methods_by_name['ListDbDescriptors']._options = None
    _DBDESCRIPTORSERVICE.methods_by_name['ListDbDescriptors']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1f"\x1a/api/v1/db/descriptor/list:\x01*'
    _DBDESCRIPTORSERVICE.methods_by_name['ListDbDescriptorVersions']._options = None
    _DBDESCRIPTORSERVICE.methods_by_name['ListDbDescriptorVersions']._serialized_options = b'\x82\xd3\xe4\x93\x02#"\x1e/api/v1/db/descriptor/versions:\x01*'
    _DBDESCRIPTORSERVICE.methods_by_name['GetDbDescriptorVersion']._options = None
    _DBDESCRIPTORSERVICE.methods_by_name['GetDbDescriptorVersion']._serialized_options = b'\x82\xd3\xe4\x93\x023\x121/api/v1/db/descriptor/version/{name}/{version_id}'
    _DBDESCRIPTORSERVICE.methods_by_name['DescriptorDependencies']._options = None
    _DBDESCRIPTORSERVICE.methods_by_name['DescriptorDependencies']._serialized_options = b'\x82\xd3\xe4\x93\x02\'""/api/v1/db/descriptor/dependencies:\x01*'
    _DESCRIPTORSERVICE._serialized_start = 128
    _DESCRIPTORSERVICE._serialized_end = 1142
    _DBDESCRIPTORSERVICE._serialized_start = 1145
    _DBDESCRIPTORSERVICE._serialized_end = 2191