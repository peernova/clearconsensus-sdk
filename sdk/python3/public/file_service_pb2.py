"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ..google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2
from ..common import file_pb2 as common_dot_file__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19public/file_service.proto\x12\x08titanium\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x19common/gateway_base.proto\x1a\x11common/file.proto2\xc7\x08\n\x0bFileService\x12g\n\x0eGetFilePreview\x12\x18.titanium.FileIdentifier\x1a\x15.titanium.FilePreview"$\x82\xd3\xe4\x93\x02\x1e"\x19/api/v1/import/{filename}:\x01*\x12V\n\tListFiles\x12\x15.titanium.ListRequest\x1a\x12.titanium.FileList"\x1e\x82\xd3\xe4\x93\x02\x18"\x13/api/v1/import/list:\x01*\x12\x8d\x01\n\x10SetFileDelimiter\x12!.titanium.SetFileDelimiterRequest\x1a\x16.google.protobuf.Empty">\x82\xd3\xe4\x93\x028"3/api/v1/import/{file_identifier.filename}/delimiter:\x01*\x12|\n\x10GetFileDelimiter\x12\x18.titanium.FileIdentifier\x1a\x1e.titanium.FileDelimiterSetting".\x82\xd3\xe4\x93\x02("#/api/v1/import/{filename}/delimiter:\x01*\x12\x90\x01\n\x11SetFileDescriptor\x12".titanium.SetFileDescriptorRequest\x1a\x16.google.protobuf.Empty"?\x82\xd3\xe4\x93\x029"4/api/v1/import/{file_identifier.filename}/descriptor:\x01*\x12\x7f\n\x11GetFileDescriptor\x12\x18.titanium.FileIdentifier\x1a\x1f.titanium.FileDescriptorSetting"/\x82\xd3\xe4\x93\x02)"$/api/v1/import/{filename}/descriptor:\x01*\x12p\n\x0eFileSubmission\x12\x1f.titanium.FileSubmissionRequest\x1a\x19.titanium.MessageResponse""\x82\xd3\xe4\x93\x02\x1c"\x17/api/v1/file-submission:\x01*\x12k\n\x0bFileHistory\x12\x1c.titanium.FileHistoryRequest\x1a\x1d.titanium.FileHistoryResponse"\x1f\x82\xd3\xe4\x93\x02\x19"\x14/api/v1/file-history:\x01*\x12v\n\x10GetFileExportUrl\x12!.titanium.GetFileExportUrlRequest\x1a".titanium.GetFileExportUrlResponse"\x1b\x82\xd3\xe4\x93\x02\x15"\x10/api/v1/raw-file:\x01*Br\n com.peernova.titanium.interfacesB\x16FileServiceProtoPublicP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/publicb\x06proto3')
_FILESERVICE = DESCRIPTOR.services_by_name['FileService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesB\x16FileServiceProtoPublicP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/public'
    _FILESERVICE.methods_by_name['GetFilePreview']._options = None
    _FILESERVICE.methods_by_name['GetFilePreview']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1e"\x19/api/v1/import/{filename}:\x01*'
    _FILESERVICE.methods_by_name['ListFiles']._options = None
    _FILESERVICE.methods_by_name['ListFiles']._serialized_options = b'\x82\xd3\xe4\x93\x02\x18"\x13/api/v1/import/list:\x01*'
    _FILESERVICE.methods_by_name['SetFileDelimiter']._options = None
    _FILESERVICE.methods_by_name['SetFileDelimiter']._serialized_options = b'\x82\xd3\xe4\x93\x028"3/api/v1/import/{file_identifier.filename}/delimiter:\x01*'
    _FILESERVICE.methods_by_name['GetFileDelimiter']._options = None
    _FILESERVICE.methods_by_name['GetFileDelimiter']._serialized_options = b'\x82\xd3\xe4\x93\x02("#/api/v1/import/{filename}/delimiter:\x01*'
    _FILESERVICE.methods_by_name['SetFileDescriptor']._options = None
    _FILESERVICE.methods_by_name['SetFileDescriptor']._serialized_options = b'\x82\xd3\xe4\x93\x029"4/api/v1/import/{file_identifier.filename}/descriptor:\x01*'
    _FILESERVICE.methods_by_name['GetFileDescriptor']._options = None
    _FILESERVICE.methods_by_name['GetFileDescriptor']._serialized_options = b'\x82\xd3\xe4\x93\x02)"$/api/v1/import/{filename}/descriptor:\x01*'
    _FILESERVICE.methods_by_name['FileSubmission']._options = None
    _FILESERVICE.methods_by_name['FileSubmission']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1c"\x17/api/v1/file-submission:\x01*'
    _FILESERVICE.methods_by_name['FileHistory']._options = None
    _FILESERVICE.methods_by_name['FileHistory']._serialized_options = b'\x82\xd3\xe4\x93\x02\x19"\x14/api/v1/file-history:\x01*'
    _FILESERVICE.methods_by_name['GetFileExportUrl']._options = None
    _FILESERVICE.methods_by_name['GetFileExportUrl']._serialized_options = b'\x82\xd3\xe4\x93\x02\x15"\x10/api/v1/raw-file:\x01*'
    _FILESERVICE._serialized_start = 145
    _FILESERVICE._serialized_end = 1240