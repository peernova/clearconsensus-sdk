"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ..google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ..common import submission_pb2 as common_dot_submission__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fpublic/submission_service.proto\x12\x08titanium\x1a\x1cgoogle/api/annotations.proto\x1a\x17common/submission.proto2\x99\x01\n\x11SubmissionService\x12\x83\x01\n\x0cGetFilesView\x12#.titanium.GetSubmissionFilesRequest\x1a$.titanium.GetSubmissionFilesResponse"(\x82\xd3\xe4\x93\x02""\x1d/api/v1/submission/files-view:\x01*Bx\n com.peernova.titanium.interfacesB\x1cSubmissionServiceProtoPublicP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/publicb\x06proto3')
_SUBMISSIONSERVICE = DESCRIPTOR.services_by_name['SubmissionService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesB\x1cSubmissionServiceProtoPublicP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/public'
    _SUBMISSIONSERVICE.methods_by_name['GetFilesView']._options = None
    _SUBMISSIONSERVICE.methods_by_name['GetFilesView']._serialized_options = b'\x82\xd3\xe4\x93\x02""\x1d/api/v1/submission/files-view:\x01*'
    _SUBMISSIONSERVICE._serialized_start = 101
    _SUBMISSIONSERVICE._serialized_end = 254