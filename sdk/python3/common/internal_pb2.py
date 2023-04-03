"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15common/internal.proto\x12\x08titanium"}\n\x19UploadNotificationRequest\x12\x17\n\x0finternalHeaders\x18\x01 \x03(\t\x12\x0f\n\x07assetId\x18\x02 \x01(\t\x12\x0c\n\x04date\x18\x03 \x01(\t\x12\x16\n\x0eoperatorClient\x18\x04 \x01(\t\x12\x10\n\x08fileName\x18\x05 \x01(\t"\x1c\n\x1aUploadNotificationResponseB^\n\x15com.peernova.titaniumB\rInternalProtoP\x00Z4github.com/peernova/clearconsensus-sdk/sdk/go/commonb\x06proto3')
_UPLOADNOTIFICATIONREQUEST = DESCRIPTOR.message_types_by_name['UploadNotificationRequest']
_UPLOADNOTIFICATIONRESPONSE = DESCRIPTOR.message_types_by_name['UploadNotificationResponse']
UploadNotificationRequest = _reflection.GeneratedProtocolMessageType('UploadNotificationRequest', (_message.Message,), {'DESCRIPTOR': _UPLOADNOTIFICATIONREQUEST, '__module__': 'common.internal_pb2'})
_sym_db.RegisterMessage(UploadNotificationRequest)
UploadNotificationResponse = _reflection.GeneratedProtocolMessageType('UploadNotificationResponse', (_message.Message,), {'DESCRIPTOR': _UPLOADNOTIFICATIONRESPONSE, '__module__': 'common.internal_pb2'})
_sym_db.RegisterMessage(UploadNotificationResponse)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\x15com.peernova.titaniumB\rInternalProtoP\x00Z4github.com/peernova/clearconsensus-sdk/sdk/go/common'
    _UPLOADNOTIFICATIONREQUEST._serialized_start = 35
    _UPLOADNOTIFICATIONREQUEST._serialized_end = 160
    _UPLOADNOTIFICATIONRESPONSE._serialized_start = 162
    _UPLOADNOTIFICATIONRESPONSE._serialized_end = 190