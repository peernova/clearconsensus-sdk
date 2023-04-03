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
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"private/data_private_service.proto\x12\x08titanium\x1a\x1cgoogle/api/annotations.proto\x1a\x19common/gateway_base.proto\x1a\x11common/data.proto"R\n\x1bUploadAuthorizationResponse\x12\x10\n\x08is_valid\x18\x01 \x01(\x08\x12\x0c\n\x04uuid\x18\x02 \x01(\t\x12\x13\n\x0btarget_path\x18\x03 \x01(\t"N\n\x13UploadNotifyRequest\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x14\n\x0ccurrent_path\x18\x02 \x01(\t\x12\x13\n\x0btarget_path\x18\x03 \x01(\t2\xfb\x02\n\x12DataServicePrivate\x12k\n\x0cExportReport\x12\x1d.titanium.ExportReportRequest\x1a\x18.titanium.ExportResponse""\x82\xd3\xe4\x93\x02\x1c"\x17/api/v1/operator/report:\x01*\x12\x82\x01\n\x0fAuthorizeUpload\x12\x1a.titanium.UploadURLRequest\x1a%.titanium.UploadAuthorizationResponse",\x82\xd3\xe4\x93\x02&"!/api/v1/internal/upload/authorize:\x01*\x12s\n\x0cNotifyUpload\x12\x1d.titanium.UploadNotifyRequest\x1a\x19.titanium.MessageResponse")\x82\xd3\xe4\x93\x02#"\x1e/api/v1/internal/upload/notify:\x01*Br\n com.peernova.titanium.interfacesB\x15DataUtilsProtoPrivateP\x01Z5github.com/peernova/clearconsensus-sdk/sdk/go/privateb\x06proto3')
_UPLOADAUTHORIZATIONRESPONSE = DESCRIPTOR.message_types_by_name['UploadAuthorizationResponse']
_UPLOADNOTIFYREQUEST = DESCRIPTOR.message_types_by_name['UploadNotifyRequest']
UploadAuthorizationResponse = _reflection.GeneratedProtocolMessageType('UploadAuthorizationResponse', (_message.Message,), {'DESCRIPTOR': _UPLOADAUTHORIZATIONRESPONSE, '__module__': 'private.data_private_service_pb2'})
_sym_db.RegisterMessage(UploadAuthorizationResponse)
UploadNotifyRequest = _reflection.GeneratedProtocolMessageType('UploadNotifyRequest', (_message.Message,), {'DESCRIPTOR': _UPLOADNOTIFYREQUEST, '__module__': 'private.data_private_service_pb2'})
_sym_db.RegisterMessage(UploadNotifyRequest)
_DATASERVICEPRIVATE = DESCRIPTOR.services_by_name['DataServicePrivate']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesB\x15DataUtilsProtoPrivateP\x01Z5github.com/peernova/clearconsensus-sdk/sdk/go/private'
    _DATASERVICEPRIVATE.methods_by_name['ExportReport']._options = None
    _DATASERVICEPRIVATE.methods_by_name['ExportReport']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1c"\x17/api/v1/operator/report:\x01*'
    _DATASERVICEPRIVATE.methods_by_name['AuthorizeUpload']._options = None
    _DATASERVICEPRIVATE.methods_by_name['AuthorizeUpload']._serialized_options = b'\x82\xd3\xe4\x93\x02&"!/api/v1/internal/upload/authorize:\x01*'
    _DATASERVICEPRIVATE.methods_by_name['NotifyUpload']._options = None
    _DATASERVICEPRIVATE.methods_by_name['NotifyUpload']._serialized_options = b'\x82\xd3\xe4\x93\x02#"\x1e/api/v1/internal/upload/notify:\x01*'
    _UPLOADAUTHORIZATIONRESPONSE._serialized_start = 124
    _UPLOADAUTHORIZATIONRESPONSE._serialized_end = 206
    _UPLOADNOTIFYREQUEST._serialized_start = 208
    _UPLOADNOTIFYREQUEST._serialized_end = 286
    _DATASERVICEPRIVATE._serialized_start = 289
    _DATASERVICEPRIVATE._serialized_end = 668