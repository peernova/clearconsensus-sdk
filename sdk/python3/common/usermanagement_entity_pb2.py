"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ..common import usermanagement_error_pb2 as common_dot_usermanagement__error__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"common/usermanagement_entity.proto\x122com.peernova.titanium.casbin.management.grpc.proto\x1a!common/usermanagement_error.proto"J\n\tEntityDto\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\nexternalId\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0f\n\x07enabled\x18\x04 \x01(\x08"\x16\n\x08EntityId\x12\n\n\x02id\x18\x01 \x01(\t"\xb7\x01\n\x0eEntityResponse\x12M\n\x04data\x18\x01 \x01(\x0b2=.com.peernova.titanium.casbin.management.grpc.proto.EntityDtoH\x00\x12J\n\x05error\x18\x02 \x01(\x0b29.com.peernova.titanium.casbin.management.grpc.proto.ErrorH\x00B\n\n\x08response"^\n\x0bEntitiesDto\x12O\n\x08entities\x18\x01 \x03(\x0b2=.com.peernova.titanium.casbin.management.grpc.proto.EntityDto"\xbb\x01\n\x10EntitiesResponse\x12O\n\x04data\x18\x01 \x01(\x0b2?.com.peernova.titanium.casbin.management.grpc.proto.EntitiesDtoH\x00\x12J\n\x05error\x18\x02 \x01(\x0b29.com.peernova.titanium.casbin.management.grpc.proto.ErrorH\x00B\n\n\x08responseBl\n2com.peernova.titanium.casbin.management.grpc.protoP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/commonb\x06proto3')
_ENTITYDTO = DESCRIPTOR.message_types_by_name['EntityDto']
_ENTITYID = DESCRIPTOR.message_types_by_name['EntityId']
_ENTITYRESPONSE = DESCRIPTOR.message_types_by_name['EntityResponse']
_ENTITIESDTO = DESCRIPTOR.message_types_by_name['EntitiesDto']
_ENTITIESRESPONSE = DESCRIPTOR.message_types_by_name['EntitiesResponse']
EntityDto = _reflection.GeneratedProtocolMessageType('EntityDto', (_message.Message,), {'DESCRIPTOR': _ENTITYDTO, '__module__': 'common.usermanagement_entity_pb2'})
_sym_db.RegisterMessage(EntityDto)
EntityId = _reflection.GeneratedProtocolMessageType('EntityId', (_message.Message,), {'DESCRIPTOR': _ENTITYID, '__module__': 'common.usermanagement_entity_pb2'})
_sym_db.RegisterMessage(EntityId)
EntityResponse = _reflection.GeneratedProtocolMessageType('EntityResponse', (_message.Message,), {'DESCRIPTOR': _ENTITYRESPONSE, '__module__': 'common.usermanagement_entity_pb2'})
_sym_db.RegisterMessage(EntityResponse)
EntitiesDto = _reflection.GeneratedProtocolMessageType('EntitiesDto', (_message.Message,), {'DESCRIPTOR': _ENTITIESDTO, '__module__': 'common.usermanagement_entity_pb2'})
_sym_db.RegisterMessage(EntitiesDto)
EntitiesResponse = _reflection.GeneratedProtocolMessageType('EntitiesResponse', (_message.Message,), {'DESCRIPTOR': _ENTITIESRESPONSE, '__module__': 'common.usermanagement_entity_pb2'})
_sym_db.RegisterMessage(EntitiesResponse)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n2com.peernova.titanium.casbin.management.grpc.protoP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/common'
    _ENTITYDTO._serialized_start = 125
    _ENTITYDTO._serialized_end = 199
    _ENTITYID._serialized_start = 201
    _ENTITYID._serialized_end = 223
    _ENTITYRESPONSE._serialized_start = 226
    _ENTITYRESPONSE._serialized_end = 409
    _ENTITIESDTO._serialized_start = 411
    _ENTITIESDTO._serialized_end = 505
    _ENTITIESRESPONSE._serialized_start = 508
    _ENTITIESRESPONSE._serialized_end = 695