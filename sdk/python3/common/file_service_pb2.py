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
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19common/file_service.proto\x12\x08titanium\x1a\x1cgoogle/protobuf/struct.proto\x1a\x19common/gateway_base.proto"L\n\x0eFileIdentifier\x12\x10\n\x08filename\x18\x01 \x01(\t\x12\x13\n\x0bupload_date\x18\x02 \x01(\t\x12\x13\n\x0bfile_status\x18\x03 \x01(\t"E\n\x14FileDelimiterSetting\x12\x11\n\tdelimiter\x18\x01 \x01(\t\x12\x1a\n\x12encapsulating_char\x18\x02 \x01(\t"\x87\x01\n\x17SetFileDelimiterRequest\x121\n\x0ffile_identifier\x18\x01 \x01(\x0b2\x18.titanium.FileIdentifier\x129\n\x11delimiter_setting\x18\x02 \x01(\x0b2\x1e.titanium.FileDelimiterSetting"\xae\x01\n\x0bFilePreview\x12%\n\x04rows\x18\x01 \x03(\x0b2\x17.google.protobuf.Struct\x129\n\x11delimiter_setting\x18\x02 \x01(\x0b2\x1e.titanium.FileDelimiterSetting\x12=\n\x15descriptor_definition\x18\x03 \x01(\x0b2\x1e.titanium.DescriptorDefinition"5\n\x08FileList\x12)\n\x07results\x18\x01 \x03(\x0b2\x18.titanium.FileIdentifier"0\n\x15FileDescriptorSetting\x12\x17\n\x0fdescriptor_name\x18\x01 \x01(\t"\x8a\x01\n\x18SetFileDescriptorRequest\x121\n\x0ffile_identifier\x18\x01 \x01(\x0b2\x18.titanium.FileIdentifier\x12;\n\x12descriptor_setting\x18\x02 \x01(\x0b2\x1f.titanium.FileDescriptorSetting"\x91\x01\n\x15FileSubmissionRequest\x12\x0c\n\x04date\x18\x01 \x01(\t\x12\x10\n\x08asset_id\x18\x02 \x01(\t\x12\x11\n\tfile_name\x18\x03 \x01(\t\x12\x0c\n\x04file\x18\x04 \x01(\t\x12\x0e\n\x06client\x18\x05 \x01(\t\x12\x13\n\x0bcompression\x18\x06 \x01(\t\x12\x12\n\ntrace_name\x18\x07 \x01(\t"\xc1\x01\n\x12FileHistoryRequest\x12\x10\n\x08asset_id\x18\x01 \x01(\t\x12\x11\n\tfile_date\x18\x02 \x01(\t\x12\x0e\n\x06filter\x18\x03 \x01(\t\x12\x0e\n\x06client\x18\x04 \x01(\t\x12"\n\x07orderBy\x18\x05 \x01(\x0b2\x11.titanium.OrderBy\x12\x1e\n\x05limit\x18\x06 \x01(\x0b2\x0f.titanium.Limit\x12\x0e\n\x06offset\x18\x07 \x01(\x05\x12\x12\n\ntrace_name\x18\x08 \x01(\t"v\n\x13FileHistoryResponse\x121\n\x04data\x18\x01 \x01(\x0b2!.titanium.FileHistoryResponseDataH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"\x86\x01\n\x17FileHistoryResponseData\x12%\n\x07columns\x18\x01 \x03(\x0b2\x14.titanium.ColumnInfo\x12&\n\x04rows\x18\x02 \x03(\x0b2\x18.titanium.FileHistoryRow\x12\x1c\n\x04page\x18\x03 \x01(\x0b2\x0e.titanium.Page"\x8b\x01\n\x0eFileHistoryRow\x12&\n\x06values\x18\x01 \x03(\x0b2\x16.google.protobuf.Value\x12\x1f\n\x17latest_consensus_member\x18\x02 \x01(\x08\x120\n\x0cconsensusRun\x18\x03 \x03(\x0b2\x1a.titanium.ConsensusRunInfo"r\n\x17GetFileExportUrlRequest\x12\x14\n\x0csubmitted_id\x18\x01 \x01(\t\x12\x16\n\x0esubmitted_date\x18\x02 \x01(\t\x12)\n\x0bexport_type\x18\x03 \x01(\x0e2\x14.titanium.ExportType"\xab\x01\n\x18GetFileExportUrlResponse\x12@\n\x04data\x18\x01 \x01(\x0b20.titanium.GetFileExportUrlResponse.FileExportUrlH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00\x1a\x1f\n\rFileExportUrl\x12\x0e\n\x06s3_url\x18\x01 \x01(\tB\n\n\x08response*y\n\nExportType\x12\x1b\n\x17EXPORT_TYPE_UNSPECIFIED\x10\x00\x12)\n%EXPORT_TYPE_ORIGINALLY_SUBMITTED_FILE\x10\x01\x12#\n\x1fEXPORT_TYPE_PARSING_ERRORS_FILE\x10\x02Br\n com.peernova.titanium.interfacesB\x16FileServiceProtoCommonP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/commonb\x06proto3')
_EXPORTTYPE = DESCRIPTOR.enum_types_by_name['ExportType']
ExportType = enum_type_wrapper.EnumTypeWrapper(_EXPORTTYPE)
EXPORT_TYPE_UNSPECIFIED = 0
EXPORT_TYPE_ORIGINALLY_SUBMITTED_FILE = 1
EXPORT_TYPE_PARSING_ERRORS_FILE = 2
_FILEIDENTIFIER = DESCRIPTOR.message_types_by_name['FileIdentifier']
_FILEDELIMITERSETTING = DESCRIPTOR.message_types_by_name['FileDelimiterSetting']
_SETFILEDELIMITERREQUEST = DESCRIPTOR.message_types_by_name['SetFileDelimiterRequest']
_FILEPREVIEW = DESCRIPTOR.message_types_by_name['FilePreview']
_FILELIST = DESCRIPTOR.message_types_by_name['FileList']
_FILEDESCRIPTORSETTING = DESCRIPTOR.message_types_by_name['FileDescriptorSetting']
_SETFILEDESCRIPTORREQUEST = DESCRIPTOR.message_types_by_name['SetFileDescriptorRequest']
_FILESUBMISSIONREQUEST = DESCRIPTOR.message_types_by_name['FileSubmissionRequest']
_FILEHISTORYREQUEST = DESCRIPTOR.message_types_by_name['FileHistoryRequest']
_FILEHISTORYRESPONSE = DESCRIPTOR.message_types_by_name['FileHistoryResponse']
_FILEHISTORYRESPONSEDATA = DESCRIPTOR.message_types_by_name['FileHistoryResponseData']
_FILEHISTORYROW = DESCRIPTOR.message_types_by_name['FileHistoryRow']
_GETFILEEXPORTURLREQUEST = DESCRIPTOR.message_types_by_name['GetFileExportUrlRequest']
_GETFILEEXPORTURLRESPONSE = DESCRIPTOR.message_types_by_name['GetFileExportUrlResponse']
_GETFILEEXPORTURLRESPONSE_FILEEXPORTURL = _GETFILEEXPORTURLRESPONSE.nested_types_by_name['FileExportUrl']
FileIdentifier = _reflection.GeneratedProtocolMessageType('FileIdentifier', (_message.Message,), {'DESCRIPTOR': _FILEIDENTIFIER, '__module__': 'common.file_service_pb2'})
_sym_db.RegisterMessage(FileIdentifier)
FileDelimiterSetting = _reflection.GeneratedProtocolMessageType('FileDelimiterSetting', (_message.Message,), {'DESCRIPTOR': _FILEDELIMITERSETTING, '__module__': 'common.file_service_pb2'})
_sym_db.RegisterMessage(FileDelimiterSetting)
SetFileDelimiterRequest = _reflection.GeneratedProtocolMessageType('SetFileDelimiterRequest', (_message.Message,), {'DESCRIPTOR': _SETFILEDELIMITERREQUEST, '__module__': 'common.file_service_pb2'})
_sym_db.RegisterMessage(SetFileDelimiterRequest)
FilePreview = _reflection.GeneratedProtocolMessageType('FilePreview', (_message.Message,), {'DESCRIPTOR': _FILEPREVIEW, '__module__': 'common.file_service_pb2'})
_sym_db.RegisterMessage(FilePreview)
FileList = _reflection.GeneratedProtocolMessageType('FileList', (_message.Message,), {'DESCRIPTOR': _FILELIST, '__module__': 'common.file_service_pb2'})
_sym_db.RegisterMessage(FileList)
FileDescriptorSetting = _reflection.GeneratedProtocolMessageType('FileDescriptorSetting', (_message.Message,), {'DESCRIPTOR': _FILEDESCRIPTORSETTING, '__module__': 'common.file_service_pb2'})
_sym_db.RegisterMessage(FileDescriptorSetting)
SetFileDescriptorRequest = _reflection.GeneratedProtocolMessageType('SetFileDescriptorRequest', (_message.Message,), {'DESCRIPTOR': _SETFILEDESCRIPTORREQUEST, '__module__': 'common.file_service_pb2'})
_sym_db.RegisterMessage(SetFileDescriptorRequest)
FileSubmissionRequest = _reflection.GeneratedProtocolMessageType('FileSubmissionRequest', (_message.Message,), {'DESCRIPTOR': _FILESUBMISSIONREQUEST, '__module__': 'common.file_service_pb2'})
_sym_db.RegisterMessage(FileSubmissionRequest)
FileHistoryRequest = _reflection.GeneratedProtocolMessageType('FileHistoryRequest', (_message.Message,), {'DESCRIPTOR': _FILEHISTORYREQUEST, '__module__': 'common.file_service_pb2'})
_sym_db.RegisterMessage(FileHistoryRequest)
FileHistoryResponse = _reflection.GeneratedProtocolMessageType('FileHistoryResponse', (_message.Message,), {'DESCRIPTOR': _FILEHISTORYRESPONSE, '__module__': 'common.file_service_pb2'})
_sym_db.RegisterMessage(FileHistoryResponse)
FileHistoryResponseData = _reflection.GeneratedProtocolMessageType('FileHistoryResponseData', (_message.Message,), {'DESCRIPTOR': _FILEHISTORYRESPONSEDATA, '__module__': 'common.file_service_pb2'})
_sym_db.RegisterMessage(FileHistoryResponseData)
FileHistoryRow = _reflection.GeneratedProtocolMessageType('FileHistoryRow', (_message.Message,), {'DESCRIPTOR': _FILEHISTORYROW, '__module__': 'common.file_service_pb2'})
_sym_db.RegisterMessage(FileHistoryRow)
GetFileExportUrlRequest = _reflection.GeneratedProtocolMessageType('GetFileExportUrlRequest', (_message.Message,), {'DESCRIPTOR': _GETFILEEXPORTURLREQUEST, '__module__': 'common.file_service_pb2'})
_sym_db.RegisterMessage(GetFileExportUrlRequest)
GetFileExportUrlResponse = _reflection.GeneratedProtocolMessageType('GetFileExportUrlResponse', (_message.Message,), {'FileExportUrl': _reflection.GeneratedProtocolMessageType('FileExportUrl', (_message.Message,), {'DESCRIPTOR': _GETFILEEXPORTURLRESPONSE_FILEEXPORTURL, '__module__': 'common.file_service_pb2'}), 'DESCRIPTOR': _GETFILEEXPORTURLRESPONSE, '__module__': 'common.file_service_pb2'})
_sym_db.RegisterMessage(GetFileExportUrlResponse)
_sym_db.RegisterMessage(GetFileExportUrlResponse.FileExportUrl)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesB\x16FileServiceProtoCommonP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/common'
    _EXPORTTYPE._serialized_start = 1839
    _EXPORTTYPE._serialized_end = 1960
    _FILEIDENTIFIER._serialized_start = 96
    _FILEIDENTIFIER._serialized_end = 172
    _FILEDELIMITERSETTING._serialized_start = 174
    _FILEDELIMITERSETTING._serialized_end = 243
    _SETFILEDELIMITERREQUEST._serialized_start = 246
    _SETFILEDELIMITERREQUEST._serialized_end = 381
    _FILEPREVIEW._serialized_start = 384
    _FILEPREVIEW._serialized_end = 558
    _FILELIST._serialized_start = 560
    _FILELIST._serialized_end = 613
    _FILEDESCRIPTORSETTING._serialized_start = 615
    _FILEDESCRIPTORSETTING._serialized_end = 663
    _SETFILEDESCRIPTORREQUEST._serialized_start = 666
    _SETFILEDESCRIPTORREQUEST._serialized_end = 804
    _FILESUBMISSIONREQUEST._serialized_start = 807
    _FILESUBMISSIONREQUEST._serialized_end = 952
    _FILEHISTORYREQUEST._serialized_start = 955
    _FILEHISTORYREQUEST._serialized_end = 1148
    _FILEHISTORYRESPONSE._serialized_start = 1150
    _FILEHISTORYRESPONSE._serialized_end = 1268
    _FILEHISTORYRESPONSEDATA._serialized_start = 1271
    _FILEHISTORYRESPONSEDATA._serialized_end = 1405
    _FILEHISTORYROW._serialized_start = 1408
    _FILEHISTORYROW._serialized_end = 1547
    _GETFILEEXPORTURLREQUEST._serialized_start = 1549
    _GETFILEEXPORTURLREQUEST._serialized_end = 1663
    _GETFILEEXPORTURLRESPONSE._serialized_start = 1666
    _GETFILEEXPORTURLRESPONSE._serialized_end = 1837
    _GETFILEEXPORTURLRESPONSE_FILEEXPORTURL._serialized_start = 1794
    _GETFILEEXPORTURLRESPONSE_FILEEXPORTURL._serialized_end = 1825