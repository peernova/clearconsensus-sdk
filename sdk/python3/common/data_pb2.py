"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11common/data.proto\x12\x08titanium\x1a\x1cgoogle/protobuf/struct.proto\x1a\x19common/gateway_base.proto"R\n\x1bUploadAuthorizationResponse\x12\x10\n\x08is_valid\x18\x01 \x01(\x08\x12\x0c\n\x04uuid\x18\x02 \x01(\t\x12\x13\n\x0btarget_path\x18\x03 \x01(\t"N\n\x13UploadNotifyRequest\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x14\n\x0ccurrent_path\x18\x02 \x01(\t\x12\x13\n\x0btarget_path\x18\x03 \x01(\t"\xa4\x02\n\x10SubmittedRequest\x12\x10\n\x08asset_id\x18\x01 \x01(\t\x12\x12\n\ntrace_name\x18\x02 \x01(\t\x12\x16\n\x0esubmitted_date\x18\x03 \x01(\t\x12\x1f\n\x17consensus_run_timestamp\x18\x04 \x01(\t\x12(\n\tdata_type\x18\x05 \x01(\x0e2\x15.titanium.TabDataType\x12.\n\x0ctable_config\x18\x06 \x01(\x0b2\x16.titanium.TableRequestH\x00\x12?\n\x15collapse_table_config\x18\x07 \x01(\x0b2\x1e.titanium.CollapseTableRequestH\x00B\x16\n\x14search_configuration"\x9e\x01\n\x0cTableRequest\x12!\n\x07filters\x18\x06 \x03(\x0b2\x10.titanium.Filter\x12)\n\x0bfilter_pack\x18\x07 \x01(\x0b2\x14.titanium.FilterPack\x12"\n\x07orderBy\x18\x08 \x01(\x0b2\x11.titanium.OrderBy\x12\x1c\n\x04page\x18\t \x01(\x0b2\x0e.titanium.Page"9\n\x14CollapseTableRequest\x12!\n\x07filters\x18\x06 \x03(\x0b2\x10.titanium.Filter"r\n\x11SubmittedResponse\x12/\n\x04data\x18\x01 \x01(\x0b2\x1f.titanium.SubmittedResponseDataH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"\x82\x01\n\x15SubmittedResponseData\x12%\n\x07columns\x18\x01 \x03(\x0b2\x14.titanium.ColumnInfo\x12$\n\x04rows\x18\x02 \x03(\x0b2\x16.titanium.SubmittedRow\x12\x1c\n\x04page\x18\x03 \x01(\x0b2\x0e.titanium.Page"\x8c\x01\n\x0cSubmittedRow\x12&\n\x06values\x18\x01 \x03(\x0b2\x16.google.protobuf.Value\x12 \n\x16validation_error_count\x18\x02 \x01(\x05H\x00\x12\x11\n\x07outlier\x18\x03 \x01(\tH\x00\x12\x13\n\tbenchmark\x18\x04 \x01(\tH\x00B\n\n\x08metadata"\xf9\x01\n\rExportRequest\x12\x10\n\x08asset_id\x18\x01 \x01(\t\x12\x17\n\x0fsubmission_date\x18\x02 \x01(\t\x12\x1f\n\x17consensus_run_timestamp\x18\x03 \x01(\t\x12\x16\n\x0einclude_header\x18\x04 \x01(\x08\x12)\n\x0bfilter_pack\x18\x05 \x01(\x0b2\x14.titanium.FilterPack\x12!\n\x07filters\x18\x06 \x03(\x0b2\x10.titanium.Filter\x12"\n\x07orderBy\x18\x07 \x01(\x0b2\x11.titanium.OrderBy\x12\x12\n\ntrace_name\x18\x08 \x01(\t"\\\n\x13ExportReportRequest\x12\x10\n\x08asset_id\x18\x01 \x01(\t\x12\x1f\n\x17consensus_run_timestamp\x18\x02 \x01(\t\x12\x12\n\ntrace_name\x18\x03 \x01(\t"\x80\x01\n\x0eExportResponse\x12@\n\x04data\x18\x01 \x01(\x0b20.titanium.ExportPresignedUrlResponseResponseDataH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"g\n&ExportPresignedUrlResponseResponseData\x12\x15\n\rgetRequestUrl\x18\x01 \x01(\t\x12\x11\n\tfile_name\x18\x02 \x01(\t\x12\x13\n\x0bcompression\x18\x03 \x01(\t"G\n\x12ExportResponseData\x12\x0e\n\x06header\x18\x01 \x01(\t\x12\x13\n\x0bcompression\x18\x02 \x01(\t\x12\x0c\n\x04data\x18\x03 \x01(\t"\x82\x01\n\x10UploadURLRequest\x12\x0c\n\x04date\x18\x01 \x01(\t\x12\x10\n\x08asset_id\x18\x02 \x01(\t\x12\x11\n\tfile_name\x18\x03 \x01(\t\x12\x0e\n\x06client\x18\x04 \x01(\t\x12\x12\n\ntrace_name\x18\x05 \x01(\t\x12\x17\n\x0fdescriptor_name\x18\x06 \x01(\t"k\n\x12UploadDataResponse\x12\x10\n\x06s3_url\x18\x01 \x01(\tH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00\x12\x15\n\x0btus_payload\x18\x03 \x01(\tH\x00B\n\n\x08response"\x91\x01\n\x19CompleteDataUploadRequest\x12\x0e\n\x06client\x18\x01 \x01(\t\x12\x10\n\x08asset_id\x18\x02 \x01(\t\x12\r\n\x05asset\x18\x03 \x01(\t\x12\x11\n\tsub_asset\x18\x04 \x01(\t\x12\x0f\n\x07service\x18\x05 \x01(\t\x12\x11\n\tsnap_time\x18\x06 \x01(\t\x12\x0c\n\x04date\x18\x07 \x01(\t"]\n\x1aCompleteDataUploadResponse\x12\x11\n\x07success\x18\x01 \x01(\x08H\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"\x86\x01\n\x11UploadDataRequest\x12\x0e\n\x06client\x18\x01 \x01(\t\x12\x11\n\tfile_name\x18\x02 \x01(\t\x12(\n\nannotation\x18\x03 \x01(\x0b2\x14.titanium.Annotation\x12$\n\x08protocol\x18\x04 \x01(\x0e2\x12.titanium.Protocol"\xd9\x01\n\nAnnotation\x12"\n\x04mode\x18\x01 \x01(\x0e2\x14.titanium.UploadMode\x12\x10\n\x08asset_id\x18\x02 \x01(\t\x12\r\n\x05asset\x18\x03 \x01(\t\x12\x11\n\tsub_asset\x18\x04 \x01(\t\x12\x0f\n\x07service\x18\x05 \x01(\t\x12\x11\n\tsnap_time\x18\x06 \x01(\t\x12\x0c\n\x04date\x18\x07 \x01(\t\x12\x13\n\x0bdescription\x18\x08 \x01(\t\x12,\n\x0bannotations\x18\t \x01(\x0b2\x17.google.protobuf.Struct*,\n\x0bTabDataType\x12\t\n\x05TABLE\x10\x00\x12\x12\n\x0eCOLLAPSE_TABLE\x10\x01*\x82\x01\n\nUploadMode\x12\x0e\n\nSUBMISSION\x10\x00\x12\x0b\n\x07PARTIAL\x10\x01\x12\n\n\x06CUSTOM\x10\x02\x12\x0e\n\nCORRECTION\x10\x03\x12\x0e\n\nsubmission\x10\x00\x12\x0b\n\x07partial\x10\x01\x12\n\n\x06custom\x10\x02\x12\x0e\n\ncorrection\x10\x03\x1a\x02\x10\x01*0\n\x08Protocol\x12\x06\n\x02S3\x10\x00\x12\x07\n\x03TUS\x10\x01\x12\x06\n\x02s3\x10\x00\x12\x07\n\x03tus\x10\x01\x1a\x02\x10\x01Bp\n com.peernova.titanium.interfacesB\x14DataUtilsProtoCommonP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/commonb\x06proto3')
_TABDATATYPE = DESCRIPTOR.enum_types_by_name['TabDataType']
TabDataType = enum_type_wrapper.EnumTypeWrapper(_TABDATATYPE)
_UPLOADMODE = DESCRIPTOR.enum_types_by_name['UploadMode']
UploadMode = enum_type_wrapper.EnumTypeWrapper(_UPLOADMODE)
_PROTOCOL = DESCRIPTOR.enum_types_by_name['Protocol']
Protocol = enum_type_wrapper.EnumTypeWrapper(_PROTOCOL)
TABLE = 0
COLLAPSE_TABLE = 1
SUBMISSION = 0
PARTIAL = 1
CUSTOM = 2
CORRECTION = 3
submission = 0
partial = 1
custom = 2
correction = 3
S3 = 0
TUS = 1
s3 = 0
tus = 1
_UPLOADAUTHORIZATIONRESPONSE = DESCRIPTOR.message_types_by_name['UploadAuthorizationResponse']
_UPLOADNOTIFYREQUEST = DESCRIPTOR.message_types_by_name['UploadNotifyRequest']
_SUBMITTEDREQUEST = DESCRIPTOR.message_types_by_name['SubmittedRequest']
_TABLEREQUEST = DESCRIPTOR.message_types_by_name['TableRequest']
_COLLAPSETABLEREQUEST = DESCRIPTOR.message_types_by_name['CollapseTableRequest']
_SUBMITTEDRESPONSE = DESCRIPTOR.message_types_by_name['SubmittedResponse']
_SUBMITTEDRESPONSEDATA = DESCRIPTOR.message_types_by_name['SubmittedResponseData']
_SUBMITTEDROW = DESCRIPTOR.message_types_by_name['SubmittedRow']
_EXPORTREQUEST = DESCRIPTOR.message_types_by_name['ExportRequest']
_EXPORTREPORTREQUEST = DESCRIPTOR.message_types_by_name['ExportReportRequest']
_EXPORTRESPONSE = DESCRIPTOR.message_types_by_name['ExportResponse']
_EXPORTPRESIGNEDURLRESPONSERESPONSEDATA = DESCRIPTOR.message_types_by_name['ExportPresignedUrlResponseResponseData']
_EXPORTRESPONSEDATA = DESCRIPTOR.message_types_by_name['ExportResponseData']
_UPLOADURLREQUEST = DESCRIPTOR.message_types_by_name['UploadURLRequest']
_UPLOADDATARESPONSE = DESCRIPTOR.message_types_by_name['UploadDataResponse']
_COMPLETEDATAUPLOADREQUEST = DESCRIPTOR.message_types_by_name['CompleteDataUploadRequest']
_COMPLETEDATAUPLOADRESPONSE = DESCRIPTOR.message_types_by_name['CompleteDataUploadResponse']
_UPLOADDATAREQUEST = DESCRIPTOR.message_types_by_name['UploadDataRequest']
_ANNOTATION = DESCRIPTOR.message_types_by_name['Annotation']
UploadAuthorizationResponse = _reflection.GeneratedProtocolMessageType('UploadAuthorizationResponse', (_message.Message,), {'DESCRIPTOR': _UPLOADAUTHORIZATIONRESPONSE, '__module__': 'common.data_pb2'})
_sym_db.RegisterMessage(UploadAuthorizationResponse)
UploadNotifyRequest = _reflection.GeneratedProtocolMessageType('UploadNotifyRequest', (_message.Message,), {'DESCRIPTOR': _UPLOADNOTIFYREQUEST, '__module__': 'common.data_pb2'})
_sym_db.RegisterMessage(UploadNotifyRequest)
SubmittedRequest = _reflection.GeneratedProtocolMessageType('SubmittedRequest', (_message.Message,), {'DESCRIPTOR': _SUBMITTEDREQUEST, '__module__': 'common.data_pb2'})
_sym_db.RegisterMessage(SubmittedRequest)
TableRequest = _reflection.GeneratedProtocolMessageType('TableRequest', (_message.Message,), {'DESCRIPTOR': _TABLEREQUEST, '__module__': 'common.data_pb2'})
_sym_db.RegisterMessage(TableRequest)
CollapseTableRequest = _reflection.GeneratedProtocolMessageType('CollapseTableRequest', (_message.Message,), {'DESCRIPTOR': _COLLAPSETABLEREQUEST, '__module__': 'common.data_pb2'})
_sym_db.RegisterMessage(CollapseTableRequest)
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
UploadDataResponse = _reflection.GeneratedProtocolMessageType('UploadDataResponse', (_message.Message,), {'DESCRIPTOR': _UPLOADDATARESPONSE, '__module__': 'common.data_pb2'})
_sym_db.RegisterMessage(UploadDataResponse)
CompleteDataUploadRequest = _reflection.GeneratedProtocolMessageType('CompleteDataUploadRequest', (_message.Message,), {'DESCRIPTOR': _COMPLETEDATAUPLOADREQUEST, '__module__': 'common.data_pb2'})
_sym_db.RegisterMessage(CompleteDataUploadRequest)
CompleteDataUploadResponse = _reflection.GeneratedProtocolMessageType('CompleteDataUploadResponse', (_message.Message,), {'DESCRIPTOR': _COMPLETEDATAUPLOADRESPONSE, '__module__': 'common.data_pb2'})
_sym_db.RegisterMessage(CompleteDataUploadResponse)
UploadDataRequest = _reflection.GeneratedProtocolMessageType('UploadDataRequest', (_message.Message,), {'DESCRIPTOR': _UPLOADDATAREQUEST, '__module__': 'common.data_pb2'})
_sym_db.RegisterMessage(UploadDataRequest)
Annotation = _reflection.GeneratedProtocolMessageType('Annotation', (_message.Message,), {'DESCRIPTOR': _ANNOTATION, '__module__': 'common.data_pb2'})
_sym_db.RegisterMessage(Annotation)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesB\x14DataUtilsProtoCommonP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/common'
    _UPLOADMODE._options = None
    _UPLOADMODE._serialized_options = b'\x10\x01'
    _PROTOCOL._options = None
    _PROTOCOL._serialized_options = b'\x10\x01'
    _TABDATATYPE._serialized_start = 2656
    _TABDATATYPE._serialized_end = 2700
    _UPLOADMODE._serialized_start = 2703
    _UPLOADMODE._serialized_end = 2833
    _PROTOCOL._serialized_start = 2835
    _PROTOCOL._serialized_end = 2883
    _UPLOADAUTHORIZATIONRESPONSE._serialized_start = 88
    _UPLOADAUTHORIZATIONRESPONSE._serialized_end = 170
    _UPLOADNOTIFYREQUEST._serialized_start = 172
    _UPLOADNOTIFYREQUEST._serialized_end = 250
    _SUBMITTEDREQUEST._serialized_start = 253
    _SUBMITTEDREQUEST._serialized_end = 545
    _TABLEREQUEST._serialized_start = 548
    _TABLEREQUEST._serialized_end = 706
    _COLLAPSETABLEREQUEST._serialized_start = 708
    _COLLAPSETABLEREQUEST._serialized_end = 765
    _SUBMITTEDRESPONSE._serialized_start = 767
    _SUBMITTEDRESPONSE._serialized_end = 881
    _SUBMITTEDRESPONSEDATA._serialized_start = 884
    _SUBMITTEDRESPONSEDATA._serialized_end = 1014
    _SUBMITTEDROW._serialized_start = 1017
    _SUBMITTEDROW._serialized_end = 1157
    _EXPORTREQUEST._serialized_start = 1160
    _EXPORTREQUEST._serialized_end = 1409
    _EXPORTREPORTREQUEST._serialized_start = 1411
    _EXPORTREPORTREQUEST._serialized_end = 1503
    _EXPORTRESPONSE._serialized_start = 1506
    _EXPORTRESPONSE._serialized_end = 1634
    _EXPORTPRESIGNEDURLRESPONSERESPONSEDATA._serialized_start = 1636
    _EXPORTPRESIGNEDURLRESPONSERESPONSEDATA._serialized_end = 1739
    _EXPORTRESPONSEDATA._serialized_start = 1741
    _EXPORTRESPONSEDATA._serialized_end = 1812
    _UPLOADURLREQUEST._serialized_start = 1815
    _UPLOADURLREQUEST._serialized_end = 1945
    _UPLOADDATARESPONSE._serialized_start = 1947
    _UPLOADDATARESPONSE._serialized_end = 2054
    _COMPLETEDATAUPLOADREQUEST._serialized_start = 2057
    _COMPLETEDATAUPLOADREQUEST._serialized_end = 2202
    _COMPLETEDATAUPLOADRESPONSE._serialized_start = 2204
    _COMPLETEDATAUPLOADRESPONSE._serialized_end = 2297
    _UPLOADDATAREQUEST._serialized_start = 2300
    _UPLOADDATAREQUEST._serialized_end = 2434
    _ANNOTATION._serialized_start = 2437
    _ANNOTATION._serialized_end = 2654