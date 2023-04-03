"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17common/unique_key.proto\x12\x08titanium\x1a\x19common/gateway_base.proto"x\n\x13UniqueKeyDefinition\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05scope\x18\x02 \x01(\t\x12\x12\n\nunique_key\x18\x03 \x03(\t\x12\x10\n\x08order_by\x18\x04 \x03(\t\x12\x1e\n\x05order\x18\x05 \x01(\x0e2\x0f.titanium.Order"z\n\x1bUniqueKeyDefinitionResponse\x12-\n\x04data\x18\x01 \x01(\x0b2\x1d.titanium.UniqueKeyDefinitionH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"?\n\rUniqueKeyList\x12.\n\x07results\x18\x01 \x03(\x0b2\x1d.titanium.UniqueKeyDefinition"o\n\x16ListUniqueKeysResponse\x12\'\n\x04data\x18\x01 \x01(\x0b2\x17.titanium.UniqueKeyListH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08responseBw\n com.peernova.titanium.interfacesB\x1bUniqueKeyServiceProtoCommonP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/commonb\x06proto3')
_UNIQUEKEYDEFINITION = DESCRIPTOR.message_types_by_name['UniqueKeyDefinition']
_UNIQUEKEYDEFINITIONRESPONSE = DESCRIPTOR.message_types_by_name['UniqueKeyDefinitionResponse']
_UNIQUEKEYLIST = DESCRIPTOR.message_types_by_name['UniqueKeyList']
_LISTUNIQUEKEYSRESPONSE = DESCRIPTOR.message_types_by_name['ListUniqueKeysResponse']
UniqueKeyDefinition = _reflection.GeneratedProtocolMessageType('UniqueKeyDefinition', (_message.Message,), {'DESCRIPTOR': _UNIQUEKEYDEFINITION, '__module__': 'common.unique_key_pb2'})
_sym_db.RegisterMessage(UniqueKeyDefinition)
UniqueKeyDefinitionResponse = _reflection.GeneratedProtocolMessageType('UniqueKeyDefinitionResponse', (_message.Message,), {'DESCRIPTOR': _UNIQUEKEYDEFINITIONRESPONSE, '__module__': 'common.unique_key_pb2'})
_sym_db.RegisterMessage(UniqueKeyDefinitionResponse)
UniqueKeyList = _reflection.GeneratedProtocolMessageType('UniqueKeyList', (_message.Message,), {'DESCRIPTOR': _UNIQUEKEYLIST, '__module__': 'common.unique_key_pb2'})
_sym_db.RegisterMessage(UniqueKeyList)
ListUniqueKeysResponse = _reflection.GeneratedProtocolMessageType('ListUniqueKeysResponse', (_message.Message,), {'DESCRIPTOR': _LISTUNIQUEKEYSRESPONSE, '__module__': 'common.unique_key_pb2'})
_sym_db.RegisterMessage(ListUniqueKeysResponse)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesB\x1bUniqueKeyServiceProtoCommonP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/common'
    _UNIQUEKEYDEFINITION._serialized_start = 64
    _UNIQUEKEYDEFINITION._serialized_end = 184
    _UNIQUEKEYDEFINITIONRESPONSE._serialized_start = 186
    _UNIQUEKEYDEFINITIONRESPONSE._serialized_end = 308
    _UNIQUEKEYLIST._serialized_start = 310
    _UNIQUEKEYLIST._serialized_end = 373
    _LISTUNIQUEKEYSRESPONSE._serialized_start = 375
    _LISTUNIQUEKEYSRESPONSE._serialized_end = 486