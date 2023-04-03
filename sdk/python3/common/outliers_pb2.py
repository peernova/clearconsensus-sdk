"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15common/outliers.proto\x12\x08titanium\x1a\x19common/gateway_base.proto"u\n\x0fOutliersRequest\x12\x1e\n\x05limit\x18\x01 \x01(\x0b2\x0f.titanium.Limit\x12\x0e\n\x06offset\x18\x02 \x01(\x05\x12"\n\x07orderBy\x18\x03 \x01(\x0b2\x11.titanium.OrderBy\x12\x0e\n\x06filter\x18\x04 \x01(\t"p\n\x10OutliersResponse\x12.\n\x04data\x18\x01 \x01(\x0b2\x1e.titanium.OutliersResponseDataH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"v\n\x14OutliersResponseData\x12%\n\x07columns\x18\x01 \x03(\x0b2\x14.titanium.ColumnInfo\x12#\n\x04rows\x18\x02 \x03(\x0b2\x15.titanium.OutliersRow\x12\x12\n\ntotal_rows\x18\x03 \x01(\x05"\x1d\n\x0bOutliersRow\x12\x0e\n\x06values\x18\x01 \x03(\tBv\n com.peernova.titanium.interfacesB\x1aOutliersServiceProtoCommonP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/commonb\x06proto3')
_OUTLIERSREQUEST = DESCRIPTOR.message_types_by_name['OutliersRequest']
_OUTLIERSRESPONSE = DESCRIPTOR.message_types_by_name['OutliersResponse']
_OUTLIERSRESPONSEDATA = DESCRIPTOR.message_types_by_name['OutliersResponseData']
_OUTLIERSROW = DESCRIPTOR.message_types_by_name['OutliersRow']
OutliersRequest = _reflection.GeneratedProtocolMessageType('OutliersRequest', (_message.Message,), {'DESCRIPTOR': _OUTLIERSREQUEST, '__module__': 'common.outliers_pb2'})
_sym_db.RegisterMessage(OutliersRequest)
OutliersResponse = _reflection.GeneratedProtocolMessageType('OutliersResponse', (_message.Message,), {'DESCRIPTOR': _OUTLIERSRESPONSE, '__module__': 'common.outliers_pb2'})
_sym_db.RegisterMessage(OutliersResponse)
OutliersResponseData = _reflection.GeneratedProtocolMessageType('OutliersResponseData', (_message.Message,), {'DESCRIPTOR': _OUTLIERSRESPONSEDATA, '__module__': 'common.outliers_pb2'})
_sym_db.RegisterMessage(OutliersResponseData)
OutliersRow = _reflection.GeneratedProtocolMessageType('OutliersRow', (_message.Message,), {'DESCRIPTOR': _OUTLIERSROW, '__module__': 'common.outliers_pb2'})
_sym_db.RegisterMessage(OutliersRow)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesB\x1aOutliersServiceProtoCommonP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/common'
    _OUTLIERSREQUEST._serialized_start = 62
    _OUTLIERSREQUEST._serialized_end = 179
    _OUTLIERSRESPONSE._serialized_start = 181
    _OUTLIERSRESPONSE._serialized_end = 293
    _OUTLIERSRESPONSEDATA._serialized_start = 295
    _OUTLIERSRESPONSEDATA._serialized_end = 413
    _OUTLIERSROW._serialized_start = 415
    _OUTLIERSROW._serialized_end = 444