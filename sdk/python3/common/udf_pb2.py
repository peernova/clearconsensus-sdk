"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ..google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10common/udf.proto\x12\x08titanium\x1a\x1cgoogle/api/annotations.proto\x1a\x19common/gateway_base.proto"T\n\x07UdfItem\x12\x0c\n\x04name\x18\x01 \x01(\t\x12$\n\x04type\x18\x02 \x01(\x0e2\x16.titanium.UdfFieldType\x12\x15\n\rlast_modified\x18\x03 \x01(\t"-\n\x07UdfList\x12"\n\x07results\x18\x01 \x03(\x0b2\x11.titanium.UdfItem"b\n\x0fListUdfResponse\x12!\n\x04data\x18\x01 \x01(\x0b2\x11.titanium.UdfListH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"-\n\x0eUdfNameRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05scope\x18\x02 \x01(\t"\x97\x01\n\x0bUdfMetadata\x12\x0c\n\x04name\x18\x01 \x01(\t\x12&\n\x06output\x18\x02 \x01(\x0e2\x16.titanium.UdfFieldType\x12$\n\x04args\x18\x03 \x03(\x0e2\x16.titanium.UdfFieldType\x12,\n\x0ccolumn_types\x18\x04 \x03(\x0e2\x16.titanium.UdfFieldType"e\n\x0eGetUdfResponse\x12%\n\x04data\x18\x01 \x01(\x0b2\x15.titanium.UdfMetadataH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response*\xb7\x01\n\x0cUdfFieldType\x12\x0e\n\nUDF_STRING\x10\x00\x12\x0f\n\x0bUDF_BOOLEAN\x10\x01\x12\x0e\n\nBIGDECIMAL\x10\x02\x12\x11\n\rUDF_TIMESTAMP\x10\x03\x12\x08\n\x04LONG\x10\x04\x12\x08\n\x04LIST\x10\x05\x12\t\n\x05FLOAT\x10\x06\x12\n\n\x06DOUBLE\x10\x07\x12\x0b\n\x07INTEGER\x10\x08\x12\x0f\n\x0bLOOKUPTABLE\x10\t\x12\r\n\tRULEERROR\x10\n\x12\x0b\n\x07DATASET\x10\x0bBd\n com.peernova.titanium.interfacesB\x08UdfProtoP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/commonb\x06proto3')
_UDFFIELDTYPE = DESCRIPTOR.enum_types_by_name['UdfFieldType']
UdfFieldType = enum_type_wrapper.EnumTypeWrapper(_UDFFIELDTYPE)
UDF_STRING = 0
UDF_BOOLEAN = 1
BIGDECIMAL = 2
UDF_TIMESTAMP = 3
LONG = 4
LIST = 5
FLOAT = 6
DOUBLE = 7
INTEGER = 8
LOOKUPTABLE = 9
RULEERROR = 10
DATASET = 11
_UDFITEM = DESCRIPTOR.message_types_by_name['UdfItem']
_UDFLIST = DESCRIPTOR.message_types_by_name['UdfList']
_LISTUDFRESPONSE = DESCRIPTOR.message_types_by_name['ListUdfResponse']
_UDFNAMEREQUEST = DESCRIPTOR.message_types_by_name['UdfNameRequest']
_UDFMETADATA = DESCRIPTOR.message_types_by_name['UdfMetadata']
_GETUDFRESPONSE = DESCRIPTOR.message_types_by_name['GetUdfResponse']
UdfItem = _reflection.GeneratedProtocolMessageType('UdfItem', (_message.Message,), {'DESCRIPTOR': _UDFITEM, '__module__': 'common.udf_pb2'})
_sym_db.RegisterMessage(UdfItem)
UdfList = _reflection.GeneratedProtocolMessageType('UdfList', (_message.Message,), {'DESCRIPTOR': _UDFLIST, '__module__': 'common.udf_pb2'})
_sym_db.RegisterMessage(UdfList)
ListUdfResponse = _reflection.GeneratedProtocolMessageType('ListUdfResponse', (_message.Message,), {'DESCRIPTOR': _LISTUDFRESPONSE, '__module__': 'common.udf_pb2'})
_sym_db.RegisterMessage(ListUdfResponse)
UdfNameRequest = _reflection.GeneratedProtocolMessageType('UdfNameRequest', (_message.Message,), {'DESCRIPTOR': _UDFNAMEREQUEST, '__module__': 'common.udf_pb2'})
_sym_db.RegisterMessage(UdfNameRequest)
UdfMetadata = _reflection.GeneratedProtocolMessageType('UdfMetadata', (_message.Message,), {'DESCRIPTOR': _UDFMETADATA, '__module__': 'common.udf_pb2'})
_sym_db.RegisterMessage(UdfMetadata)
GetUdfResponse = _reflection.GeneratedProtocolMessageType('GetUdfResponse', (_message.Message,), {'DESCRIPTOR': _GETUDFRESPONSE, '__module__': 'common.udf_pb2'})
_sym_db.RegisterMessage(GetUdfResponse)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesB\x08UdfProtoP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/common'
    _UDFFIELDTYPE._serialized_start = 625
    _UDFFIELDTYPE._serialized_end = 808
    _UDFITEM._serialized_start = 87
    _UDFITEM._serialized_end = 171
    _UDFLIST._serialized_start = 173
    _UDFLIST._serialized_end = 218
    _LISTUDFRESPONSE._serialized_start = 220
    _LISTUDFRESPONSE._serialized_end = 318
    _UDFNAMEREQUEST._serialized_start = 320
    _UDFNAMEREQUEST._serialized_end = 365
    _UDFMETADATA._serialized_start = 368
    _UDFMETADATA._serialized_end = 519
    _GETUDFRESPONSE._serialized_start = 521
    _GETUDFRESPONSE._serialized_end = 622