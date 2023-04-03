"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dcommon/supported_fields.proto\x12\x08titanium\x1a\x19common/gateway_base.proto"j\n\x12GetSupportedFields\x12\x10\n\x08asset_id\x18\x01 \x01(\t\x12\x1e\n\x05limit\x18\x02 \x01(\x0b2\x0f.titanium.Limit\x12\x0e\n\x06offset\x18\x03 \x01(\x05\x12\x12\n\ntrace_name\x18\x04 \x01(\t"l\n\x1aGetSupportedFieldsResponse\x12 \n\x04data\x18\x01 \x01(\x0b2\x10.titanium.FieldsH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"\xed\x01\n\x0eSupportedField\x12\r\n\x05asset\x18\x01 \x01(\t\x12\x17\n\x0finstrument_type\x18\x02 \x01(\t\x12\x0f\n\x07service\x18\x03 \x01(\t\x12\x16\n\x0esubmitted_date\x18\x04 \x01(\t\x12\r\n\x05field\x18\x05 \x01(\t\x12\x15\n\rmatch_pattern\x18\x06 \x01(\t\x12\x0e\n\x06filter\x18\x07 \x01(\t\x12\x1e\n\x05limit\x18\x08 \x01(\x0b2\x0f.titanium.Limit\x12\x0e\n\x06offset\x18\t \x01(\x05\x12\x10\n\x08asset_id\x18\n \x01(\t\x12\x12\n\ntrace_name\x18\x0b \x01(\t"h\n\x16GetFieldValuesResponse\x12 \n\x04data\x18\x01 \x01(\x0b2\x10.titanium.ValuesH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08responseB}\n com.peernova.titanium.interfacesB!SupportedFieldsServiceProtoCommonP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/commonb\x06proto3')
_GETSUPPORTEDFIELDS = DESCRIPTOR.message_types_by_name['GetSupportedFields']
_GETSUPPORTEDFIELDSRESPONSE = DESCRIPTOR.message_types_by_name['GetSupportedFieldsResponse']
_SUPPORTEDFIELD = DESCRIPTOR.message_types_by_name['SupportedField']
_GETFIELDVALUESRESPONSE = DESCRIPTOR.message_types_by_name['GetFieldValuesResponse']
GetSupportedFields = _reflection.GeneratedProtocolMessageType('GetSupportedFields', (_message.Message,), {'DESCRIPTOR': _GETSUPPORTEDFIELDS, '__module__': 'common.supported_fields_pb2'})
_sym_db.RegisterMessage(GetSupportedFields)
GetSupportedFieldsResponse = _reflection.GeneratedProtocolMessageType('GetSupportedFieldsResponse', (_message.Message,), {'DESCRIPTOR': _GETSUPPORTEDFIELDSRESPONSE, '__module__': 'common.supported_fields_pb2'})
_sym_db.RegisterMessage(GetSupportedFieldsResponse)
SupportedField = _reflection.GeneratedProtocolMessageType('SupportedField', (_message.Message,), {'DESCRIPTOR': _SUPPORTEDFIELD, '__module__': 'common.supported_fields_pb2'})
_sym_db.RegisterMessage(SupportedField)
GetFieldValuesResponse = _reflection.GeneratedProtocolMessageType('GetFieldValuesResponse', (_message.Message,), {'DESCRIPTOR': _GETFIELDVALUESRESPONSE, '__module__': 'common.supported_fields_pb2'})
_sym_db.RegisterMessage(GetFieldValuesResponse)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesB!SupportedFieldsServiceProtoCommonP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/common'
    _GETSUPPORTEDFIELDS._serialized_start = 70
    _GETSUPPORTEDFIELDS._serialized_end = 176
    _GETSUPPORTEDFIELDSRESPONSE._serialized_start = 178
    _GETSUPPORTEDFIELDSRESPONSE._serialized_end = 286
    _SUPPORTEDFIELD._serialized_start = 289
    _SUPPORTEDFIELD._serialized_end = 526
    _GETFIELDVALUESRESPONSE._serialized_start = 528
    _GETFIELDVALUESRESPONSE._serialized_end = 632