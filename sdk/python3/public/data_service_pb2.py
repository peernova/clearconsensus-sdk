"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ..google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2
from ..common import data_pb2 as common_dot_data__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19public/data_service.proto\x12\x08titanium\x1a\x1cgoogle/api/annotations.proto\x1a\x19common/gateway_base.proto\x1a\x11common/data.proto2\xa8\x04\n\x0bDataService\x12b\n\tSubmitted\x12\x1a.titanium.SubmittedRequest\x1a\x1b.titanium.SubmittedResponse"\x1c\x82\xd3\xe4\x93\x02\x16"\x11/api/v1/submitted:\x01*\x12V\n\x06Export\x12\x17.titanium.ExportRequest\x1a\x18.titanium.ExportResponse"\x19\x82\xd3\xe4\x93\x02\x13"\x0e/api/v1/export:\x01*\x12c\n\tUploadURL\x12\x1a.titanium.UploadURLRequest\x1a\x1b.titanium.UploadURLResponse"\x1d\x82\xd3\xe4\x93\x02\x17"\x12/api/v1/upload/url:\x01*\x12\x82\x01\n\x0fAuthorizeUpload\x12\x1a.titanium.UploadURLRequest\x1a%.titanium.UploadAuthorizationResponse",\x82\xd3\xe4\x93\x02&"!/api/v1/internal/upload/authorize:\x01*\x12s\n\x0cNotifyUpload\x12\x1d.titanium.UploadNotifyRequest\x1a\x19.titanium.MessageResponse")\x82\xd3\xe4\x93\x02#"\x1e/api/v1/internal/upload/notify:\x01*Bp\n com.peernova.titanium.interfacesB\x14DataUtilsProtoPublicP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/publicb\x06proto3')
_DATASERVICE = DESCRIPTOR.services_by_name['DataService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesB\x14DataUtilsProtoPublicP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/public'
    _DATASERVICE.methods_by_name['Submitted']._options = None
    _DATASERVICE.methods_by_name['Submitted']._serialized_options = b'\x82\xd3\xe4\x93\x02\x16"\x11/api/v1/submitted:\x01*'
    _DATASERVICE.methods_by_name['Export']._options = None
    _DATASERVICE.methods_by_name['Export']._serialized_options = b'\x82\xd3\xe4\x93\x02\x13"\x0e/api/v1/export:\x01*'
    _DATASERVICE.methods_by_name['UploadURL']._options = None
    _DATASERVICE.methods_by_name['UploadURL']._serialized_options = b'\x82\xd3\xe4\x93\x02\x17"\x12/api/v1/upload/url:\x01*'
    _DATASERVICE.methods_by_name['AuthorizeUpload']._options = None
    _DATASERVICE.methods_by_name['AuthorizeUpload']._serialized_options = b'\x82\xd3\xe4\x93\x02&"!/api/v1/internal/upload/authorize:\x01*'
    _DATASERVICE.methods_by_name['NotifyUpload']._options = None
    _DATASERVICE.methods_by_name['NotifyUpload']._serialized_options = b'\x82\xd3\xe4\x93\x02#"\x1e/api/v1/internal/upload/notify:\x01*'
    _DATASERVICE._serialized_start = 116
    _DATASERVICE._serialized_end = 668