"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17common/submission.proto\x12\x08titanium\x1a\x19common/gateway_base.proto"\xdd\x01\n\x19GetSubmissionFilesRequest\x12\x10\n\x08asset_id\x18\x01 \x01(\t\x12\x12\n\ntrace_name\x18\x02 \x01(\t\x12\x16\n\x0esnap_date_from\x18\x03 \x01(\t\x12\x14\n\x0csnap_date_to\x18\x04 \x01(\t\x12#\n\x08order_by\x18\x05 \x01(\x0b2\x11.titanium.OrderBy\x12)\n\x0bfilter_pack\x18\x06 \x01(\x0b2\x14.titanium.FilterPack\x12\x1c\n\x04page\x18\x07 \x01(\x0b2\x0e.titanium.Page"|\n\x1aGetSubmissionFilesResponse\x12 \n\x05error\x18\x01 \x01(\x0b2\x0f.titanium.ErrorH\x00\x120\n\x04data\x18\x02 \x01(\x0b2 .titanium.GetSubmissionFilesDataH\x00B\n\n\x08response"\x80\x01\n\x16GetSubmissionFilesData\x12%\n\x07columns\x18\x01 \x03(\x0b2\x14.titanium.ColumnInfo\x12!\n\x04rows\x18\x02 \x03(\x0b2\x13.titanium.ValuesRow\x12\x1c\n\x04page\x18\x03 \x01(\x0b2\x0e.titanium.PageBx\n com.peernova.titanium.interfacesB\x1cSubmissionServiceProtoCommonP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/commonb\x06proto3')
_GETSUBMISSIONFILESREQUEST = DESCRIPTOR.message_types_by_name['GetSubmissionFilesRequest']
_GETSUBMISSIONFILESRESPONSE = DESCRIPTOR.message_types_by_name['GetSubmissionFilesResponse']
_GETSUBMISSIONFILESDATA = DESCRIPTOR.message_types_by_name['GetSubmissionFilesData']
GetSubmissionFilesRequest = _reflection.GeneratedProtocolMessageType('GetSubmissionFilesRequest', (_message.Message,), {'DESCRIPTOR': _GETSUBMISSIONFILESREQUEST, '__module__': 'common.submission_pb2'})
_sym_db.RegisterMessage(GetSubmissionFilesRequest)
GetSubmissionFilesResponse = _reflection.GeneratedProtocolMessageType('GetSubmissionFilesResponse', (_message.Message,), {'DESCRIPTOR': _GETSUBMISSIONFILESRESPONSE, '__module__': 'common.submission_pb2'})
_sym_db.RegisterMessage(GetSubmissionFilesResponse)
GetSubmissionFilesData = _reflection.GeneratedProtocolMessageType('GetSubmissionFilesData', (_message.Message,), {'DESCRIPTOR': _GETSUBMISSIONFILESDATA, '__module__': 'common.submission_pb2'})
_sym_db.RegisterMessage(GetSubmissionFilesData)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesB\x1cSubmissionServiceProtoCommonP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/common'
    _GETSUBMISSIONFILESREQUEST._serialized_start = 65
    _GETSUBMISSIONFILESREQUEST._serialized_end = 286
    _GETSUBMISSIONFILESRESPONSE._serialized_start = 288
    _GETSUBMISSIONFILESRESPONSE._serialized_end = 412
    _GETSUBMISSIONFILESDATA._serialized_start = 415
    _GETSUBMISSIONFILESDATA._serialized_end = 543