"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ..google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.private/supported_fields_private_service.proto\x12\x08titanium\x1a\x1cgoogle/api/annotations.proto\x1a\x19common/gateway_base.proto"\\\n\x15SupportedFieldsValues\x12\x10\n\x08asset_id\x18\x01 \x01(\t\x12\r\n\x05field\x18\x02 \x01(\t\x12\x0e\n\x06values\x18\x03 \x03(\t\x12\x12\n\ntrace_name\x18\x04 \x01(\t2\xad\x03\n\x1dSupportedFieldsPrivateService\x12\x84\x01\n\x15CreateSupportedFields\x12\x1f.titanium.SupportedFieldsValues\x1a\x19.titanium.MessageResponse"/\x82\xd3\xe4\x93\x02)"$/api/v1/operator/create/field-values:\x01*\x12~\n\x12AddSupportedFields\x12\x1f.titanium.SupportedFieldsValues\x1a\x19.titanium.MessageResponse",\x82\xd3\xe4\x93\x02&"!/api/v1/operator/add/field-values:\x01*\x12\x84\x01\n\x15DeleteSupportedFields\x12\x1f.titanium.SupportedFieldsValues\x1a\x19.titanium.MessageResponse"/\x82\xd3\xe4\x93\x02)"$/api/v1/operator/delete/field-values:\x01*B\x7f\n com.peernova.titanium.interfacesB"SupportedFieldsServiceProtoPrivateP\x01Z5github.com/peernova/clearconsensus-sdk/sdk/go/privateb\x06proto3')
_SUPPORTEDFIELDSVALUES = DESCRIPTOR.message_types_by_name['SupportedFieldsValues']
SupportedFieldsValues = _reflection.GeneratedProtocolMessageType('SupportedFieldsValues', (_message.Message,), {'DESCRIPTOR': _SUPPORTEDFIELDSVALUES, '__module__': 'private.supported_fields_private_service_pb2'})
_sym_db.RegisterMessage(SupportedFieldsValues)
_SUPPORTEDFIELDSPRIVATESERVICE = DESCRIPTOR.services_by_name['SupportedFieldsPrivateService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesB"SupportedFieldsServiceProtoPrivateP\x01Z5github.com/peernova/clearconsensus-sdk/sdk/go/private'
    _SUPPORTEDFIELDSPRIVATESERVICE.methods_by_name['CreateSupportedFields']._options = None
    _SUPPORTEDFIELDSPRIVATESERVICE.methods_by_name['CreateSupportedFields']._serialized_options = b'\x82\xd3\xe4\x93\x02)"$/api/v1/operator/create/field-values:\x01*'
    _SUPPORTEDFIELDSPRIVATESERVICE.methods_by_name['AddSupportedFields']._options = None
    _SUPPORTEDFIELDSPRIVATESERVICE.methods_by_name['AddSupportedFields']._serialized_options = b'\x82\xd3\xe4\x93\x02&"!/api/v1/operator/add/field-values:\x01*'
    _SUPPORTEDFIELDSPRIVATESERVICE.methods_by_name['DeleteSupportedFields']._options = None
    _SUPPORTEDFIELDSPRIVATESERVICE.methods_by_name['DeleteSupportedFields']._serialized_options = b'\x82\xd3\xe4\x93\x02)"$/api/v1/operator/delete/field-values:\x01*'
    _SUPPORTEDFIELDSVALUES._serialized_start = 117
    _SUPPORTEDFIELDSVALUES._serialized_end = 209
    _SUPPORTEDFIELDSPRIVATESERVICE._serialized_start = 212
    _SUPPORTEDFIELDSPRIVATESERVICE._serialized_end = 641