"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ..google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ..common import supported_fields_pb2 as common_dot_supported__fields__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%public/supported_fields_service.proto\x12\x08titanium\x1a\x1cgoogle/api/annotations.proto\x1a\x1dcommon/supported_fields.proto2\x91\x02\n\x16SupportedFieldsService\x12y\n\x13ListSupportedFields\x12\x1c.titanium.GetSupportedFields\x1a$.titanium.GetSupportedFieldsResponse"\x1e\x82\xd3\xe4\x93\x02\x18"\x13/api/v1/list/fields:\x01*\x12|\n\x18GetSupportedFieldsValues\x12\x18.titanium.SupportedField\x1a .titanium.GetFieldValuesResponse"$\x82\xd3\xe4\x93\x02\x1e"\x19/api/v1/list/field-values:\x01*B}\n com.peernova.titanium.interfacesB!SupportedFieldsServiceProtoPublicP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/publicb\x06proto3')
_SUPPORTEDFIELDSSERVICE = DESCRIPTOR.services_by_name['SupportedFieldsService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesB!SupportedFieldsServiceProtoPublicP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/public'
    _SUPPORTEDFIELDSSERVICE.methods_by_name['ListSupportedFields']._options = None
    _SUPPORTEDFIELDSSERVICE.methods_by_name['ListSupportedFields']._serialized_options = b'\x82\xd3\xe4\x93\x02\x18"\x13/api/v1/list/fields:\x01*'
    _SUPPORTEDFIELDSSERVICE.methods_by_name['GetSupportedFieldsValues']._options = None
    _SUPPORTEDFIELDSSERVICE.methods_by_name['GetSupportedFieldsValues']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1e"\x19/api/v1/list/field-values:\x01*'
    _SUPPORTEDFIELDSSERVICE._serialized_start = 113
    _SUPPORTEDFIELDSSERVICE._serialized_end = 386