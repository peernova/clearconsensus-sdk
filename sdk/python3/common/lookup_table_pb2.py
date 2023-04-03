"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19common/lookup_table.proto\x12\x08titanium\x1a\x1cgoogle/protobuf/struct.proto\x1a\x19common/gateway_base.proto"\\\n\x15AddLookupTableRequest\x12\r\n\x05scope\x18\x01 \x01(\t\x124\n\x0blookuptable\x18\x02 \x01(\x0b2\x1f.titanium.LookupTableDefinition"w\n\x16GetLookupTableResponse\x12/\n\x04data\x18\x01 \x01(\x0b2\x1f.titanium.LookupTableDefinitionH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"u\n\x13LookupTableListItem\x12(\n\nidentifier\x18\x01 \x01(\x0b2\x14.titanium.Identifier\x12\x1f\n\x04type\x18\x02 \x01(\x0e2\x11.titanium.LutType\x12\x13\n\x0bvalue_field\x18\x03 \x01(\t"W\n\x0fLookupTableList\x12.\n\x07results\x18\x01 \x03(\x0b2\x1d.titanium.LookupTableListItem\x12\x14\n\x0ctotalRecords\x18\x02 \x01(\x05"r\n\x17ListLookupTableResponse\x12)\n\x04data\x18\x01 \x01(\x0b2\x19.titanium.LookupTableListH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"\xa2\x01\n\x15LookupTableDefinition\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1f\n\x04type\x18\x02 \x01(\x0e2\x11.titanium.LutType\x12"\n\x06fields\x18\x03 \x03(\x0b2\x12.titanium.LutField\x12 \n\x04rows\x18\x04 \x03(\x0b2\x12.titanium.LutEntry\x12\x14\n\x0ctotalRecords\x18\x05 \x01(\x05"F\n\x08LutField\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1f\n\x04type\x18\x02 \x01(\x0e2\x11.titanium.LutType\x12\x0b\n\x03key\x18\x03 \x01(\x08"6\n\x08LutEntry\x12*\n\x06values\x18\x01 \x01(\x0b2\x1a.google.protobuf.ListValue*>\n\x07LutType\x12\x0b\n\x07BOOLEAN\x10\x00\x12\n\n\x06STRING\x10\x01\x12\x0b\n\x07NUMERIC\x10\x02\x12\r\n\tTIMESTAMP\x10\x03Bt\n com.peernova.titanium.interfacesB\x18LookupServiceProtoCommonP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/commonb\x06proto3')
_LUTTYPE = DESCRIPTOR.enum_types_by_name['LutType']
LutType = enum_type_wrapper.EnumTypeWrapper(_LUTTYPE)
BOOLEAN = 0
STRING = 1
NUMERIC = 2
TIMESTAMP = 3
_ADDLOOKUPTABLEREQUEST = DESCRIPTOR.message_types_by_name['AddLookupTableRequest']
_GETLOOKUPTABLERESPONSE = DESCRIPTOR.message_types_by_name['GetLookupTableResponse']
_LOOKUPTABLELISTITEM = DESCRIPTOR.message_types_by_name['LookupTableListItem']
_LOOKUPTABLELIST = DESCRIPTOR.message_types_by_name['LookupTableList']
_LISTLOOKUPTABLERESPONSE = DESCRIPTOR.message_types_by_name['ListLookupTableResponse']
_LOOKUPTABLEDEFINITION = DESCRIPTOR.message_types_by_name['LookupTableDefinition']
_LUTFIELD = DESCRIPTOR.message_types_by_name['LutField']
_LUTENTRY = DESCRIPTOR.message_types_by_name['LutEntry']
AddLookupTableRequest = _reflection.GeneratedProtocolMessageType('AddLookupTableRequest', (_message.Message,), {'DESCRIPTOR': _ADDLOOKUPTABLEREQUEST, '__module__': 'common.lookup_table_pb2'})
_sym_db.RegisterMessage(AddLookupTableRequest)
GetLookupTableResponse = _reflection.GeneratedProtocolMessageType('GetLookupTableResponse', (_message.Message,), {'DESCRIPTOR': _GETLOOKUPTABLERESPONSE, '__module__': 'common.lookup_table_pb2'})
_sym_db.RegisterMessage(GetLookupTableResponse)
LookupTableListItem = _reflection.GeneratedProtocolMessageType('LookupTableListItem', (_message.Message,), {'DESCRIPTOR': _LOOKUPTABLELISTITEM, '__module__': 'common.lookup_table_pb2'})
_sym_db.RegisterMessage(LookupTableListItem)
LookupTableList = _reflection.GeneratedProtocolMessageType('LookupTableList', (_message.Message,), {'DESCRIPTOR': _LOOKUPTABLELIST, '__module__': 'common.lookup_table_pb2'})
_sym_db.RegisterMessage(LookupTableList)
ListLookupTableResponse = _reflection.GeneratedProtocolMessageType('ListLookupTableResponse', (_message.Message,), {'DESCRIPTOR': _LISTLOOKUPTABLERESPONSE, '__module__': 'common.lookup_table_pb2'})
_sym_db.RegisterMessage(ListLookupTableResponse)
LookupTableDefinition = _reflection.GeneratedProtocolMessageType('LookupTableDefinition', (_message.Message,), {'DESCRIPTOR': _LOOKUPTABLEDEFINITION, '__module__': 'common.lookup_table_pb2'})
_sym_db.RegisterMessage(LookupTableDefinition)
LutField = _reflection.GeneratedProtocolMessageType('LutField', (_message.Message,), {'DESCRIPTOR': _LUTFIELD, '__module__': 'common.lookup_table_pb2'})
_sym_db.RegisterMessage(LutField)
LutEntry = _reflection.GeneratedProtocolMessageType('LutEntry', (_message.Message,), {'DESCRIPTOR': _LUTENTRY, '__module__': 'common.lookup_table_pb2'})
_sym_db.RegisterMessage(LutEntry)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesB\x18LookupServiceProtoCommonP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/common'
    _LUTTYPE._serialized_start = 928
    _LUTTYPE._serialized_end = 990
    _ADDLOOKUPTABLEREQUEST._serialized_start = 96
    _ADDLOOKUPTABLEREQUEST._serialized_end = 188
    _GETLOOKUPTABLERESPONSE._serialized_start = 190
    _GETLOOKUPTABLERESPONSE._serialized_end = 309
    _LOOKUPTABLELISTITEM._serialized_start = 311
    _LOOKUPTABLELISTITEM._serialized_end = 428
    _LOOKUPTABLELIST._serialized_start = 430
    _LOOKUPTABLELIST._serialized_end = 517
    _LISTLOOKUPTABLERESPONSE._serialized_start = 519
    _LISTLOOKUPTABLERESPONSE._serialized_end = 633
    _LOOKUPTABLEDEFINITION._serialized_start = 636
    _LOOKUPTABLEDEFINITION._serialized_end = 798
    _LUTFIELD._serialized_start = 800
    _LUTFIELD._serialized_end = 870
    _LUTENTRY._serialized_start = 872
    _LUTENTRY._serialized_end = 926