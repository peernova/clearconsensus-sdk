"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"common/usermanagement_entity.proto\x122com.peernova.titanium.casbin.management.grpc.proto"J\n\tEntityDto\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\nexternalId\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0f\n\x07enabled\x18\x04 \x01(\x08"^\n\x0bEntitiesDto\x12O\n\x08entities\x18\x01 \x03(\x0b2=.com.peernova.titanium.casbin.management.grpc.proto.EntityDtoBl\n2com.peernova.titanium.casbin.management.grpc.protoP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/commonb\x06proto3')
_ENTITYDTO = DESCRIPTOR.message_types_by_name['EntityDto']
_ENTITIESDTO = DESCRIPTOR.message_types_by_name['EntitiesDto']
EntityDto = _reflection.GeneratedProtocolMessageType('EntityDto', (_message.Message,), {'DESCRIPTOR': _ENTITYDTO, '__module__': 'common.usermanagement_entity_pb2'})
_sym_db.RegisterMessage(EntityDto)
EntitiesDto = _reflection.GeneratedProtocolMessageType('EntitiesDto', (_message.Message,), {'DESCRIPTOR': _ENTITIESDTO, '__module__': 'common.usermanagement_entity_pb2'})
_sym_db.RegisterMessage(EntitiesDto)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n2com.peernova.titanium.casbin.management.grpc.protoP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/common'
    _ENTITYDTO._serialized_start = 90
    _ENTITYDTO._serialized_end = 164
    _ENTITIESDTO._serialized_start = 166
    _ENTITIESDTO._serialized_end = 260