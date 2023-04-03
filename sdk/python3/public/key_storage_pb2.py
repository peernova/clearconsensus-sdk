"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ..google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18public/key_storage.proto\x12\x08titanium\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x19common/gateway_base.proto"\x83\x01\n\x07KVAsset\x12\x0b\n\x03key\x18\x01 \x01(\t\x12&\n\x05value\x18\x02 \x01(\x0b2\x17.google.protobuf.Struct\x12\x0b\n\x03ttl\x18\x03 \x01(\t\x12$\n\x08ttl_from\x18\x04 \x01(\x0e2\x12.titanium.TTLTypes\x12\x10\n\x08ttl_date\x18\x05 \x01(\t"\x18\n\tKVRequest\x12\x0b\n\x03key\x18\x01 \x01(\t"V\n\x13KVOperationResponse\x12\x11\n\x07message\x18\x01 \x01(\tH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"`\n\rGetKVResponse\x12!\n\x04data\x18\x01 \x01(\x0b2\x11.titanium.KVAssetH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"\x1f\n\rListKVRequest\x12\x0e\n\x06filter\x18\x01 \x01(\t",\n\x0bKVListAsset\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x10\n\x08ttl_date\x18\x02 \x01(\t"0\n\x06KVList\x12&\n\x07results\x18\x01 \x03(\x0b2\x15.titanium.KVListAsset"`\n\x0eListKVResponse\x12 \n\x04data\x18\x01 \x01(\x0b2\x10.titanium.KVListH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response*)\n\x08TTLTypes\x12\x08\n\x04NONE\x10\x00\x12\x08\n\x04READ\x10\x01\x12\t\n\x05WRITE\x10\x022\xcc\x03\n\tKVService\x12U\n\x06AddKey\x12\x11.titanium.KVAsset\x1a\x1d.titanium.KVOperationResponse"\x19\x82\xd3\xe4\x93\x02\x13"\x0e/api/v1/kv/add:\x01*\x12[\n\tUpdateKey\x12\x11.titanium.KVAsset\x1a\x1d.titanium.KVOperationResponse"\x1c\x82\xd3\xe4\x93\x02\x16"\x11/api/v1/kv/update:\x01*\x12Q\n\x06GetKey\x12\x13.titanium.KVRequest\x1a\x17.titanium.GetKVResponse"\x19\x82\xd3\xe4\x93\x02\x13"\x0e/api/v1/kv/get:\x01*\x12]\n\tDeleteKey\x12\x13.titanium.KVRequest\x1a\x1d.titanium.KVOperationResponse"\x1c\x82\xd3\xe4\x93\x02\x16"\x11/api/v1/kv/delete:\x01*\x12Y\n\x08ListKeys\x12\x17.titanium.ListKVRequest\x1a\x18.titanium.ListKVResponse"\x1a\x82\xd3\xe4\x93\x02\x14"\x0f/api/v1/kv/list:\x01*Bc\n com.peernova.titanium.interfacesB\x07KVProtoP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/publicb\x06proto3')
_TTLTYPES = DESCRIPTOR.enum_types_by_name['TTLTypes']
TTLTypes = enum_type_wrapper.EnumTypeWrapper(_TTLTYPES)
NONE = 0
READ = 1
WRITE = 2
_KVASSET = DESCRIPTOR.message_types_by_name['KVAsset']
_KVREQUEST = DESCRIPTOR.message_types_by_name['KVRequest']
_KVOPERATIONRESPONSE = DESCRIPTOR.message_types_by_name['KVOperationResponse']
_GETKVRESPONSE = DESCRIPTOR.message_types_by_name['GetKVResponse']
_LISTKVREQUEST = DESCRIPTOR.message_types_by_name['ListKVRequest']
_KVLISTASSET = DESCRIPTOR.message_types_by_name['KVListAsset']
_KVLIST = DESCRIPTOR.message_types_by_name['KVList']
_LISTKVRESPONSE = DESCRIPTOR.message_types_by_name['ListKVResponse']
KVAsset = _reflection.GeneratedProtocolMessageType('KVAsset', (_message.Message,), {'DESCRIPTOR': _KVASSET, '__module__': 'public.key_storage_pb2'})
_sym_db.RegisterMessage(KVAsset)
KVRequest = _reflection.GeneratedProtocolMessageType('KVRequest', (_message.Message,), {'DESCRIPTOR': _KVREQUEST, '__module__': 'public.key_storage_pb2'})
_sym_db.RegisterMessage(KVRequest)
KVOperationResponse = _reflection.GeneratedProtocolMessageType('KVOperationResponse', (_message.Message,), {'DESCRIPTOR': _KVOPERATIONRESPONSE, '__module__': 'public.key_storage_pb2'})
_sym_db.RegisterMessage(KVOperationResponse)
GetKVResponse = _reflection.GeneratedProtocolMessageType('GetKVResponse', (_message.Message,), {'DESCRIPTOR': _GETKVRESPONSE, '__module__': 'public.key_storage_pb2'})
_sym_db.RegisterMessage(GetKVResponse)
ListKVRequest = _reflection.GeneratedProtocolMessageType('ListKVRequest', (_message.Message,), {'DESCRIPTOR': _LISTKVREQUEST, '__module__': 'public.key_storage_pb2'})
_sym_db.RegisterMessage(ListKVRequest)
KVListAsset = _reflection.GeneratedProtocolMessageType('KVListAsset', (_message.Message,), {'DESCRIPTOR': _KVLISTASSET, '__module__': 'public.key_storage_pb2'})
_sym_db.RegisterMessage(KVListAsset)
KVList = _reflection.GeneratedProtocolMessageType('KVList', (_message.Message,), {'DESCRIPTOR': _KVLIST, '__module__': 'public.key_storage_pb2'})
_sym_db.RegisterMessage(KVList)
ListKVResponse = _reflection.GeneratedProtocolMessageType('ListKVResponse', (_message.Message,), {'DESCRIPTOR': _LISTKVRESPONSE, '__module__': 'public.key_storage_pb2'})
_sym_db.RegisterMessage(ListKVResponse)
_KVSERVICE = DESCRIPTOR.services_by_name['KVService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesB\x07KVProtoP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/public'
    _KVSERVICE.methods_by_name['AddKey']._options = None
    _KVSERVICE.methods_by_name['AddKey']._serialized_options = b'\x82\xd3\xe4\x93\x02\x13"\x0e/api/v1/kv/add:\x01*'
    _KVSERVICE.methods_by_name['UpdateKey']._options = None
    _KVSERVICE.methods_by_name['UpdateKey']._serialized_options = b'\x82\xd3\xe4\x93\x02\x16"\x11/api/v1/kv/update:\x01*'
    _KVSERVICE.methods_by_name['GetKey']._options = None
    _KVSERVICE.methods_by_name['GetKey']._serialized_options = b'\x82\xd3\xe4\x93\x02\x13"\x0e/api/v1/kv/get:\x01*'
    _KVSERVICE.methods_by_name['DeleteKey']._options = None
    _KVSERVICE.methods_by_name['DeleteKey']._serialized_options = b'\x82\xd3\xe4\x93\x02\x16"\x11/api/v1/kv/delete:\x01*'
    _KVSERVICE.methods_by_name['ListKeys']._options = None
    _KVSERVICE.methods_by_name['ListKeys']._serialized_options = b'\x82\xd3\xe4\x93\x02\x14"\x0f/api/v1/kv/list:\x01*'
    _TTLTYPES._serialized_start = 698
    _TTLTYPES._serialized_end = 739
    _KVASSET._serialized_start = 126
    _KVASSET._serialized_end = 257
    _KVREQUEST._serialized_start = 259
    _KVREQUEST._serialized_end = 283
    _KVOPERATIONRESPONSE._serialized_start = 285
    _KVOPERATIONRESPONSE._serialized_end = 371
    _GETKVRESPONSE._serialized_start = 373
    _GETKVRESPONSE._serialized_end = 469
    _LISTKVREQUEST._serialized_start = 471
    _LISTKVREQUEST._serialized_end = 502
    _KVLISTASSET._serialized_start = 504
    _KVLISTASSET._serialized_end = 548
    _KVLIST._serialized_start = 550
    _KVLIST._serialized_end = 598
    _LISTKVRESPONSE._serialized_start = 600
    _LISTKVRESPONSE._serialized_end = 696
    _KVSERVICE._serialized_start = 742
    _KVSERVICE._serialized_end = 1202