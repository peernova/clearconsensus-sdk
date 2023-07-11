"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ..google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2
from ..common import lookup_table_pb2 as common_dot_lookup__table__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!public/lookup_table_service.proto\x12\x08titanium\x1a\x1cgoogle/api/annotations.proto\x1a\x19common/gateway_base.proto\x1a\x19common/lookup_table.proto2\xe2\x05\n\x12LookupTableService\x12t\n\x0eAddLookupTable\x12\x1f.titanium.AddLookupTableRequest\x1a\x1d.titanium.AcknowledgeResponse""\x82\xd3\xe4\x93\x02\x1c"\x17/api/v1/lookuptable/add:\x01*\x12o\n\x0eGetLookupTable\x12\x17.titanium.GetDefinition\x1a .titanium.GetLookupTableResponse""\x82\xd3\xe4\x93\x02\x1c"\x17/api/v1/lookuptable/get:\x01*\x12q\n\x10ListLookupTables\x12\x15.titanium.ListRequest\x1a!.titanium.ListLookupTableResponse"#\x82\xd3\xe4\x93\x02\x1d"\x18/api/v1/lookuptable/list:\x01*\x12z\n\x17ListLookupTableVersions\x12\x17.titanium.GetDefinition\x1a\x1d.titanium.ListVersionResponse"\'\x82\xd3\xe4\x93\x02!"\x1c/api/v1/lookuptable/versions:\x01*\x12y\n\x11EnableLookupTable\x12\x1e.titanium.EnableDisableRequest\x1a\x1d.titanium.AcknowledgeResponse"%\x82\xd3\xe4\x93\x02\x1f"\x1a/api/v1/lookuptable/enable:\x01*\x12{\n\x12DisableLookupTable\x12\x1e.titanium.EnableDisableRequest\x1a\x1d.titanium.AcknowledgeResponse"&\x82\xd3\xe4\x93\x02 "\x1b/api/v1/lookuptable/disable:\x01*Bt\n com.peernova.titanium.interfacesB\x18LookupServiceProtoPublicP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/publicb\x06proto3')
_LOOKUPTABLESERVICE = DESCRIPTOR.services_by_name['LookupTableService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesB\x18LookupServiceProtoPublicP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/public'
    _LOOKUPTABLESERVICE.methods_by_name['AddLookupTable']._options = None
    _LOOKUPTABLESERVICE.methods_by_name['AddLookupTable']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1c"\x17/api/v1/lookuptable/add:\x01*'
    _LOOKUPTABLESERVICE.methods_by_name['GetLookupTable']._options = None
    _LOOKUPTABLESERVICE.methods_by_name['GetLookupTable']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1c"\x17/api/v1/lookuptable/get:\x01*'
    _LOOKUPTABLESERVICE.methods_by_name['ListLookupTables']._options = None
    _LOOKUPTABLESERVICE.methods_by_name['ListLookupTables']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1d"\x18/api/v1/lookuptable/list:\x01*'
    _LOOKUPTABLESERVICE.methods_by_name['ListLookupTableVersions']._options = None
    _LOOKUPTABLESERVICE.methods_by_name['ListLookupTableVersions']._serialized_options = b'\x82\xd3\xe4\x93\x02!"\x1c/api/v1/lookuptable/versions:\x01*'
    _LOOKUPTABLESERVICE.methods_by_name['EnableLookupTable']._options = None
    _LOOKUPTABLESERVICE.methods_by_name['EnableLookupTable']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1f"\x1a/api/v1/lookuptable/enable:\x01*'
    _LOOKUPTABLESERVICE.methods_by_name['DisableLookupTable']._options = None
    _LOOKUPTABLESERVICE.methods_by_name['DisableLookupTable']._serialized_options = b'\x82\xd3\xe4\x93\x02 "\x1b/api/v1/lookuptable/disable:\x01*'
    _LOOKUPTABLESERVICE._serialized_start = 132
    _LOOKUPTABLESERVICE._serialized_end = 870