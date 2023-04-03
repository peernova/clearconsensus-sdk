"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ..google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ..common import dq_errors_pb2 as common_dot_dq__errors__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1epublic/dq_errors_service.proto\x12\x08titanium\x1a\x1cgoogle/api/annotations.proto\x1a\x16common/dq_errors.proto2\x84\x02\n\x12DataQualityService\x12\x8d\x01\n\x14GetDataQualityErrors\x12%.titanium.GetDataQualityErrorsRequest\x1a&.titanium.GetDataQualityErrorsResponse"&\x82\xd3\xe4\x93\x02 "\x1b/api/v1/data-quality-errors:\x01*\x12^\n\x08DQErrors\x12\x19.titanium.DQErrorsRequest\x1a\x1a.titanium.DQErrorsResponse"\x1b\x82\xd3\xe4\x93\x02\x15"\x10/api/v1/dqerrors:\x01*By\n com.peernova.titanium.interfacesB\x1dDataQualityServiceProtoPublicP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/publicb\x06proto3')
_DATAQUALITYSERVICE = DESCRIPTOR.services_by_name['DataQualityService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesB\x1dDataQualityServiceProtoPublicP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/public'
    _DATAQUALITYSERVICE.methods_by_name['GetDataQualityErrors']._options = None
    _DATAQUALITYSERVICE.methods_by_name['GetDataQualityErrors']._serialized_options = b'\x82\xd3\xe4\x93\x02 "\x1b/api/v1/data-quality-errors:\x01*'
    _DATAQUALITYSERVICE.methods_by_name['DQErrors']._options = None
    _DATAQUALITYSERVICE.methods_by_name['DQErrors']._serialized_options = b'\x82\xd3\xe4\x93\x02\x15"\x10/api/v1/dqerrors:\x01*'
    _DATAQUALITYSERVICE._serialized_start = 99
    _DATAQUALITYSERVICE._serialized_end = 359