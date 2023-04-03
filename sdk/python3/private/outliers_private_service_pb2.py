"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ..google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2
from ..common import outliers_pb2 as common_dot_outliers__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&private/outliers_private_service.proto\x12\x08titanium\x1a\x1cgoogle/api/annotations.proto\x1a\x19common/gateway_base.proto\x1a\x15common/outliers.proto"\x8b\x01\n\x17OperatorOutliersRequest\x12\x0c\n\x04date\x18\x01 \x01(\t\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12"\n\x07orderBy\x18\x03 \x01(\x0b2\x11.titanium.OrderBy\x12\x1e\n\x05limit\x18\x04 \x01(\x0b2\x0f.titanium.Limit\x12\x0e\n\x06offset\x18\x05 \x01(\x05"\x80\x01\n\x18OperatorOutliersResponse\x126\n\x04data\x18\x01 \x01(\x0b2&.titanium.OperatorOutliersResponseDataH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"|\n\x1cOperatorOutliersResponseData\x12%\n\x07columns\x18\x01 \x03(\x0b2\x14.titanium.ColumnInfo\x12!\n\x04rows\x18\x02 \x03(\x0b2\x13.titanium.ValuesRow\x12\x12\n\ntotal_rows\x18\x03 \x01(\x052\x82\x02\n\x16OutliersPrivateService\x12\x7f\n\x10OperatorOutliers\x12!.titanium.OperatorOutliersRequest\x1a".titanium.OperatorOutliersResponse"$\x82\xd3\xe4\x93\x02\x1e"\x19/api/v1/operator-outliers:\x01*\x12g\n\x08Outliers\x12\x19.titanium.OutliersRequest\x1a\x1a.titanium.OutliersResponse"$\x82\xd3\xe4\x93\x02\x1e"\x19/api/v1/operator/outliers:\x01*Bx\n com.peernova.titanium.interfacesB\x1bOutliersServiceProtoPrivateP\x01Z5github.com/peernova/clearconsensus-sdk/sdk/go/privateb\x06proto3')
_OPERATOROUTLIERSREQUEST = DESCRIPTOR.message_types_by_name['OperatorOutliersRequest']
_OPERATOROUTLIERSRESPONSE = DESCRIPTOR.message_types_by_name['OperatorOutliersResponse']
_OPERATOROUTLIERSRESPONSEDATA = DESCRIPTOR.message_types_by_name['OperatorOutliersResponseData']
OperatorOutliersRequest = _reflection.GeneratedProtocolMessageType('OperatorOutliersRequest', (_message.Message,), {'DESCRIPTOR': _OPERATOROUTLIERSREQUEST, '__module__': 'private.outliers_private_service_pb2'})
_sym_db.RegisterMessage(OperatorOutliersRequest)
OperatorOutliersResponse = _reflection.GeneratedProtocolMessageType('OperatorOutliersResponse', (_message.Message,), {'DESCRIPTOR': _OPERATOROUTLIERSRESPONSE, '__module__': 'private.outliers_private_service_pb2'})
_sym_db.RegisterMessage(OperatorOutliersResponse)
OperatorOutliersResponseData = _reflection.GeneratedProtocolMessageType('OperatorOutliersResponseData', (_message.Message,), {'DESCRIPTOR': _OPERATOROUTLIERSRESPONSEDATA, '__module__': 'private.outliers_private_service_pb2'})
_sym_db.RegisterMessage(OperatorOutliersResponseData)
_OUTLIERSPRIVATESERVICE = DESCRIPTOR.services_by_name['OutliersPrivateService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesB\x1bOutliersServiceProtoPrivateP\x01Z5github.com/peernova/clearconsensus-sdk/sdk/go/private'
    _OUTLIERSPRIVATESERVICE.methods_by_name['OperatorOutliers']._options = None
    _OUTLIERSPRIVATESERVICE.methods_by_name['OperatorOutliers']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1e"\x19/api/v1/operator-outliers:\x01*'
    _OUTLIERSPRIVATESERVICE.methods_by_name['Outliers']._options = None
    _OUTLIERSPRIVATESERVICE.methods_by_name['Outliers']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1e"\x19/api/v1/operator/outliers:\x01*'
    _OPERATOROUTLIERSREQUEST._serialized_start = 133
    _OPERATOROUTLIERSREQUEST._serialized_end = 272
    _OPERATOROUTLIERSRESPONSE._serialized_start = 275
    _OPERATOROUTLIERSRESPONSE._serialized_end = 403
    _OPERATOROUTLIERSRESPONSEDATA._serialized_start = 405
    _OPERATOROUTLIERSRESPONSEDATA._serialized_end = 529
    _OUTLIERSPRIVATESERVICE._serialized_start = 532
    _OUTLIERSPRIVATESERVICE._serialized_end = 790