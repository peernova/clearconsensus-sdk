"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ..google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ..common import outliers_pb2 as common_dot_outliers__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dpublic/outliers_service.proto\x12\x08titanium\x1a\x1cgoogle/api/annotations.proto\x1a\x15common/outliers.proto2q\n\x0fOutliersService\x12^\n\x08Outliers\x12\x19.titanium.OutliersRequest\x1a\x1a.titanium.OutliersResponse"\x1b\x82\xd3\xe4\x93\x02\x15"\x10/api/v1/outliers:\x01*Bv\n com.peernova.titanium.interfacesB\x1aOutliersServiceProtoPublicP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/publicb\x06proto3')
_OUTLIERSSERVICE = DESCRIPTOR.services_by_name['OutliersService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesB\x1aOutliersServiceProtoPublicP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/public'
    _OUTLIERSSERVICE.methods_by_name['Outliers']._options = None
    _OUTLIERSSERVICE.methods_by_name['Outliers']._serialized_options = b'\x82\xd3\xe4\x93\x02\x15"\x10/api/v1/outliers:\x01*'
    _OUTLIERSSERVICE._serialized_start = 96
    _OUTLIERSSERVICE._serialized_end = 209