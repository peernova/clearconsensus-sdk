"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!common/usermanagement_error.proto\x122com.peernova.titanium.casbin.management.grpc.proto"\xd8\x01\n\x05Error\x12\x0c\n\x04code\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\x12o\n\x16validationErrorDetails\x18\x03 \x03(\x0b2O.com.peernova.titanium.casbin.management.grpc.proto.Error.ValidationErrorDetail\x1a?\n\x15ValidationErrorDetail\x12\x11\n\tfieldName\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\tBl\n2com.peernova.titanium.casbin.management.grpc.protoP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/commonb\x06proto3')
_ERROR = DESCRIPTOR.message_types_by_name['Error']
_ERROR_VALIDATIONERRORDETAIL = _ERROR.nested_types_by_name['ValidationErrorDetail']
Error = _reflection.GeneratedProtocolMessageType('Error', (_message.Message,), {'ValidationErrorDetail': _reflection.GeneratedProtocolMessageType('ValidationErrorDetail', (_message.Message,), {'DESCRIPTOR': _ERROR_VALIDATIONERRORDETAIL, '__module__': 'common.usermanagement_error_pb2'}), 'DESCRIPTOR': _ERROR, '__module__': 'common.usermanagement_error_pb2'})
_sym_db.RegisterMessage(Error)
_sym_db.RegisterMessage(Error.ValidationErrorDetail)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n2com.peernova.titanium.casbin.management.grpc.protoP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/common'
    _ERROR._serialized_start = 90
    _ERROR._serialized_end = 306
    _ERROR_VALIDATIONERRORDETAIL._serialized_start = 243
    _ERROR_VALIDATIONERRORDETAIL._serialized_end = 306