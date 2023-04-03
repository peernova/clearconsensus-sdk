"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12common/popup.proto\x12\x08titanium\x1a\x1cgoogle/protobuf/struct.proto\x1a\x19common/gateway_base.proto"\xc5\x01\n\x10PopUpViewRequest\x12\x10\n\x08asset_id\x18\x01 \x01(\t\x12\x16\n\x0esubmitted_date\x18\x02 \x01(\t\x12\x1f\n\x17consensus_run_timestamp\x18\x03 \x01(\t\x12\x16\n\x0csubmitted_id\x18\x04 \x01(\tH\x00\x12\x16\n\x0cconsensus_id\x18\x05 \x01(\tH\x00\x12\x1c\n\x12evaluated_price_id\x18\x06 \x01(\tH\x00\x12\x12\n\ntrace_name\x18\x07 \x01(\tB\x04\n\x02id"r\n\x11PopUpViewResponse\x12/\n\x04data\x18\x01 \x01(\x0b2\x1f.titanium.PopUpViewResponseDataH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"\x91\x03\n\x15PopUpViewResponseData\x12%\n\nsubmission\x18\x01 \x01(\x0b2\x11.titanium.ViewRow\x12$\n\tconsensus\x18\x02 \x01(\x0b2\x11.titanium.ViewRow\x12)\n\x0eevaluatedPrice\x18\x03 \x01(\x0b2\x11.titanium.ViewRow\x12\x1a\n\x10validationErrors\x18\x04 \x01(\tH\x00\x12\x11\n\x07outlier\x18\x05 \x01(\tH\x00\x12\x13\n\tbenchmark\x18\x06 \x01(\tH\x00\x123\n\x10consensusDetails\x18\x07 \x01(\x0b2\x19.titanium.ConsensusDetail\x12\x14\n\x0cranges_chart\x18\x08 \x01(\t\x126\n\x11dataQualityErrors\x18\t \x01(\x0b2\x1b.titanium.DataQualityErrors\x12-\n\rgrouping_keys\x18\n \x03(\x0b2\x16.titanium.StringKeyValB\n\n\x08metadata"X\n\x07ViewRow\x12%\n\x07columns\x18\x01 \x03(\x0b2\x14.titanium.ColumnInfo\x12&\n\x06values\x18\x02 \x03(\x0b2\x16.google.protobuf.ValueBs\n com.peernova.titanium.interfacesB\x17PopUpServiceProtoCommonP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/commonb\x06proto3')
_POPUPVIEWREQUEST = DESCRIPTOR.message_types_by_name['PopUpViewRequest']
_POPUPVIEWRESPONSE = DESCRIPTOR.message_types_by_name['PopUpViewResponse']
_POPUPVIEWRESPONSEDATA = DESCRIPTOR.message_types_by_name['PopUpViewResponseData']
_VIEWROW = DESCRIPTOR.message_types_by_name['ViewRow']
PopUpViewRequest = _reflection.GeneratedProtocolMessageType('PopUpViewRequest', (_message.Message,), {'DESCRIPTOR': _POPUPVIEWREQUEST, '__module__': 'common.popup_pb2'})
_sym_db.RegisterMessage(PopUpViewRequest)
PopUpViewResponse = _reflection.GeneratedProtocolMessageType('PopUpViewResponse', (_message.Message,), {'DESCRIPTOR': _POPUPVIEWRESPONSE, '__module__': 'common.popup_pb2'})
_sym_db.RegisterMessage(PopUpViewResponse)
PopUpViewResponseData = _reflection.GeneratedProtocolMessageType('PopUpViewResponseData', (_message.Message,), {'DESCRIPTOR': _POPUPVIEWRESPONSEDATA, '__module__': 'common.popup_pb2'})
_sym_db.RegisterMessage(PopUpViewResponseData)
ViewRow = _reflection.GeneratedProtocolMessageType('ViewRow', (_message.Message,), {'DESCRIPTOR': _VIEWROW, '__module__': 'common.popup_pb2'})
_sym_db.RegisterMessage(ViewRow)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesB\x17PopUpServiceProtoCommonP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/common'
    _POPUPVIEWREQUEST._serialized_start = 90
    _POPUPVIEWREQUEST._serialized_end = 287
    _POPUPVIEWRESPONSE._serialized_start = 289
    _POPUPVIEWRESPONSE._serialized_end = 403
    _POPUPVIEWRESPONSEDATA._serialized_start = 406
    _POPUPVIEWRESPONSEDATA._serialized_end = 807
    _VIEWROW._serialized_start = 809
    _VIEWROW._serialized_end = 897