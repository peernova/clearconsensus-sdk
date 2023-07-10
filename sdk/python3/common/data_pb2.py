"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11common/data.proto\x12\x08titanium\x1a\x1cgoogle/protobuf/struct.proto\x1a\x19common/gateway_base.proto"R\n\x1bUploadAuthorizationResponse\x12\x10\n\x08is_valid\x18\x01 \x01(\x08\x12\x0c\n\x04uuid\x18\x02 \x01(\t\x12\x13\n\x0btarget_path\x18\x03 \x01(\t"N\n\x13UploadNotifyRequest\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x14\n\x0ccurrent_path\x18\x02 \x01(\t\x12\x13\n\x0btarget_path\x18\x03 \x01(\t"\x91\x02\n\x10SubmittedRequest\x12\x10\n\x08asset_id\x18\x01 \x01(\t\x12\x16\n\x0esubmitted_date\x18\x02 \x01(\t\x12\x1f\n\x17consensus_run_timestamp\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12!\n\x07filters\x18\x05 \x03(\x0b2\x10.titanium.Filter\x12)\n\x0bfilter_pack\x18\x06 \x01(\x0b2\x14.titanium.FilterPack\x12"\n\x07orderBy\x18\x07 \x01(\x0b2\x11.titanium.OrderBy\x12\x12\n\ntrace_name\x18\x08 \x01(\t\x12\x1c\n\x04page\x18\t \x01(\x0b2\x0e.titanium.Page"r\n\x11SubmittedResponse\x12/\n\x04data\x18\x01 \x01(\x0b2\x1f.titanium.SubmittedResponseDataH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"\x82\x01\n\x15SubmittedResponseData\x12%\n\x07columns\x18\x01 \x03(\x0b2\x14.titanium.ColumnInfo\x12$\n\x04rows\x18\x02 \x03(\x0b2\x16.titanium.SubmittedRow\x12\x1c\n\x04page\x18\x03 \x01(\x0b2\x0e.titanium.Page"\x8c\x01\n\x0cSubmittedRow\x12&\n\x06values\x18\x01 \x03(\x0b2\x16.google.protobuf.Value\x12 \n\x16validation_error_count\x18\x02 \x01(\x05H\x00\x12\x11\n\x07outlier\x18\x03 \x01(\tH\x00\x12\x13\n\tbenchmark\x18\x04 \x01(\tH\x00B\n\n\x08metadata"\xf9\x01\n\rExportRequest\x12\x10\n\x08asset_id\x18\x01 \x01(\t\x12\x17\n\x0fsubmission_date\x18\x02 \x01(\t\x12\x1f\n\x17consensus_run_timestamp\x18\x03 \x01(\t\x12\x16\n\x0einclude_header\x18\x04 \x01(\x08\x12)\n\x0bfilter_pack\x18\x05 \x01(\x0b2\x14.titanium.FilterPack\x12!\n\x07filters\x18\x06 \x03(\x0b2\x10.titanium.Filter\x12"\n\x07orderBy\x18\x07 \x01(\x0b2\x11.titanium.OrderBy\x12\x12\n\ntrace_name\x18\x08 \x01(\t"\\\n\x13ExportReportRequest\x12\x10\n\x08asset_id\x18\x01 \x01(\t\x12\x1f\n\x17consensus_run_timestamp\x18\x02 \x01(\t\x12\x12\n\ntrace_name\x18\x03 \x01(\t"\x80\x01\n\x0eExportResponse\x12@\n\x04data\x18\x01 \x01(\x0b20.titanium.ExportPresignedUrlResponseResponseDataH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"g\n&ExportPresignedUrlResponseResponseData\x12\x15\n\rgetRequestUrl\x18\x01 \x01(\t\x12\x11\n\tfile_name\x18\x02 \x01(\t\x12\x13\n\x0bcompression\x18\x03 \x01(\t"G\n\x12ExportResponseData\x12\x0e\n\x06header\x18\x01 \x01(\t\x12\x13\n\x0bcompression\x18\x02 \x01(\t\x12\x0c\n\x04data\x18\x03 \x01(\t"\x82\x01\n\x10UploadURLRequest\x12\x0c\n\x04date\x18\x01 \x01(\t\x12\x10\n\x08asset_id\x18\x02 \x01(\t\x12\x11\n\tfile_name\x18\x03 \x01(\t\x12\x0e\n\x06client\x18\x04 \x01(\t\x12\x12\n\ntrace_name\x18\x05 \x01(\t\x12\x17\n\x0fdescriptor_name\x18\x06 \x01(\tBp\n com.peernova.titanium.interfacesB\x14DataUtilsProtoCommonP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/commonb\x06proto3')
_UPLOADAUTHORIZATIONRESPONSE = DESCRIPTOR.message_types_by_name['UploadAuthorizationResponse']
_UPLOADNOTIFYREQUEST = DESCRIPTOR.message_types_by_name['UploadNotifyRequest']
_SUBMITTEDREQUEST = DESCRIPTOR.message_types_by_name['SubmittedRequest']
_SUBMITTEDRESPONSE = DESCRIPTOR.message_types_by_name['SubmittedResponse']
_SUBMITTEDRESPONSEDATA = DESCRIPTOR.message_types_by_name['SubmittedResponseData']
_SUBMITTEDROW = DESCRIPTOR.message_types_by_name['SubmittedRow']
_EXPORTREQUEST = DESCRIPTOR.message_types_by_name['ExportRequest']
_EXPORTREPORTREQUEST = DESCRIPTOR.message_types_by_name['ExportReportRequest']
_EXPORTRESPONSE = DESCRIPTOR.message_types_by_name['ExportResponse']
_EXPORTPRESIGNEDURLRESPONSERESPONSEDATA = DESCRIPTOR.message_types_by_name['ExportPresignedUrlResponseResponseData']
_EXPORTRESPONSEDATA = DESCRIPTOR.message_types_by_name['ExportResponseData']
_UPLOADURLREQUEST = DESCRIPTOR.message_types_by_name['UploadURLRequest']
UploadAuthorizationResponse = _reflection.GeneratedProtocolMessageType('UploadAuthorizationResponse', (_message.Message,), {'DESCRIPTOR': _UPLOADAUTHORIZATIONRESPONSE, '__module__': 'common.data_pb2'})
_sym_db.RegisterMessage(UploadAuthorizationResponse)
UploadNotifyRequest = _reflection.GeneratedProtocolMessageType('UploadNotifyRequest', (_message.Message,), {'DESCRIPTOR': _UPLOADNOTIFYREQUEST, '__module__': 'common.data_pb2'})
_sym_db.RegisterMessage(UploadNotifyRequest)
SubmittedRequest = _reflection.GeneratedProtocolMessageType('SubmittedRequest', (_message.Message,), {'DESCRIPTOR': _SUBMITTEDREQUEST, '__module__': 'common.data_pb2'})
_sym_db.RegisterMessage(SubmittedRequest)
SubmittedResponse = _reflection.GeneratedProtocolMessageType('SubmittedResponse', (_message.Message,), {'DESCRIPTOR': _SUBMITTEDRESPONSE, '__module__': 'common.data_pb2'})
_sym_db.RegisterMessage(SubmittedResponse)
SubmittedResponseData = _reflection.GeneratedProtocolMessageType('SubmittedResponseData', (_message.Message,), {'DESCRIPTOR': _SUBMITTEDRESPONSEDATA, '__module__': 'common.data_pb2'})
_sym_db.RegisterMessage(SubmittedResponseData)
SubmittedRow = _reflection.GeneratedProtocolMessageType('SubmittedRow', (_message.Message,), {'DESCRIPTOR': _SUBMITTEDROW, '__module__': 'common.data_pb2'})
_sym_db.RegisterMessage(SubmittedRow)
ExportRequest = _reflection.GeneratedProtocolMessageType('ExportRequest', (_message.Message,), {'DESCRIPTOR': _EXPORTREQUEST, '__module__': 'common.data_pb2'})
_sym_db.RegisterMessage(ExportRequest)
ExportReportRequest = _reflection.GeneratedProtocolMessageType('ExportReportRequest', (_message.Message,), {'DESCRIPTOR': _EXPORTREPORTREQUEST, '__module__': 'common.data_pb2'})
_sym_db.RegisterMessage(ExportReportRequest)
ExportResponse = _reflection.GeneratedProtocolMessageType('ExportResponse', (_message.Message,), {'DESCRIPTOR': _EXPORTRESPONSE, '__module__': 'common.data_pb2'})
_sym_db.RegisterMessage(ExportResponse)
ExportPresignedUrlResponseResponseData = _reflection.GeneratedProtocolMessageType('ExportPresignedUrlResponseResponseData', (_message.Message,), {'DESCRIPTOR': _EXPORTPRESIGNEDURLRESPONSERESPONSEDATA, '__module__': 'common.data_pb2'})
_sym_db.RegisterMessage(ExportPresignedUrlResponseResponseData)
ExportResponseData = _reflection.GeneratedProtocolMessageType('ExportResponseData', (_message.Message,), {'DESCRIPTOR': _EXPORTRESPONSEDATA, '__module__': 'common.data_pb2'})
_sym_db.RegisterMessage(ExportResponseData)
UploadURLRequest = _reflection.GeneratedProtocolMessageType('UploadURLRequest', (_message.Message,), {'DESCRIPTOR': _UPLOADURLREQUEST, '__module__': 'common.data_pb2'})
_sym_db.RegisterMessage(UploadURLRequest)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesB\x14DataUtilsProtoCommonP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/common'
    _UPLOADAUTHORIZATIONRESPONSE._serialized_start = 88
    _UPLOADAUTHORIZATIONRESPONSE._serialized_end = 170
    _UPLOADNOTIFYREQUEST._serialized_start = 172
    _UPLOADNOTIFYREQUEST._serialized_end = 250
    _SUBMITTEDREQUEST._serialized_start = 253
    _SUBMITTEDREQUEST._serialized_end = 526
    _SUBMITTEDRESPONSE._serialized_start = 528
    _SUBMITTEDRESPONSE._serialized_end = 642
    _SUBMITTEDRESPONSEDATA._serialized_start = 645
    _SUBMITTEDRESPONSEDATA._serialized_end = 775
    _SUBMITTEDROW._serialized_start = 778
    _SUBMITTEDROW._serialized_end = 918
    _EXPORTREQUEST._serialized_start = 921
    _EXPORTREQUEST._serialized_end = 1170
    _EXPORTREPORTREQUEST._serialized_start = 1172
    _EXPORTREPORTREQUEST._serialized_end = 1264
    _EXPORTRESPONSE._serialized_start = 1267
    _EXPORTRESPONSE._serialized_end = 1395
    _EXPORTPRESIGNEDURLRESPONSERESPONSEDATA._serialized_start = 1397
    _EXPORTPRESIGNEDURLRESPONSERESPONSEDATA._serialized_end = 1500
    _EXPORTRESPONSEDATA._serialized_start = 1502
    _EXPORTRESPONSEDATA._serialized_end = 1573
    _UPLOADURLREQUEST._serialized_start = 1576
    _UPLOADURLREQUEST._serialized_end = 1706