"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ..google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11public/dtcc.proto\x12\x08titanium\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x19common/gateway_base.proto"\x92\x02\n\x0eDtccTabRequest\x12\x10\n\x08asset_id\x18\x01 \x01(\t\x12\x12\n\ntrace_name\x18\x02 \x01(\t\x12\x11\n\tsnap_date\x18\x03 \x01(\t\x12)\n\x0bfilter_pack\x18\x04 \x01(\x0b2\x14.titanium.FilterPack\x12"\n\x07orderBy\x18\x05 \x01(\x0b2\x11.titanium.OrderBy\x12\x1c\n\x04page\x18\x06 \x01(\x0b2\x0e.titanium.Page\x12\x17\n\rsubmission_id\x18\x07 \x01(\tH\x00\x12;\n\x14sub_group_key_search\x18\x08 \x01(\x0b2\x1b.titanium.SubGroupKeySearchH\x00B\x04\n\x02id"Y\n\x11SubGroupKeySearch\x12\x1a\n\x12sub_submitted_date\x18\x01 \x01(\t\x12(\n\ngroup_keys\x18\x02 \x01(\x0b2\x14.titanium.FilterPack"n\n\x0fDtccTabResponse\x12-\n\x04data\x18\x01 \x01(\x0b2\x1d.titanium.DtccTabResponseDataH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"}\n\x13DtccTabResponseData\x12%\n\x07columns\x18\x01 \x03(\x0b2\x14.titanium.ColumnInfo\x12!\n\x04rows\x18\x02 \x03(\x0b2\x13.titanium.ValuesRow\x12\x1c\n\x04page\x18\x03 \x01(\x0b2\x0e.titanium.Page2o\n\x0bDtccService\x12`\n\x0cGetDtccTable\x12\x18.titanium.DtccTabRequest\x1a\x19.titanium.DtccTabResponse"\x1b\x82\xd3\xe4\x93\x02\x15"\x10/api/v1/dtcc/tab:\x01*BZ\n com.peernova.titanium.interfacesP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/publicb\x06proto3')
_DTCCTABREQUEST = DESCRIPTOR.message_types_by_name['DtccTabRequest']
_SUBGROUPKEYSEARCH = DESCRIPTOR.message_types_by_name['SubGroupKeySearch']
_DTCCTABRESPONSE = DESCRIPTOR.message_types_by_name['DtccTabResponse']
_DTCCTABRESPONSEDATA = DESCRIPTOR.message_types_by_name['DtccTabResponseData']
DtccTabRequest = _reflection.GeneratedProtocolMessageType('DtccTabRequest', (_message.Message,), {'DESCRIPTOR': _DTCCTABREQUEST, '__module__': 'public.dtcc_pb2'})
_sym_db.RegisterMessage(DtccTabRequest)
SubGroupKeySearch = _reflection.GeneratedProtocolMessageType('SubGroupKeySearch', (_message.Message,), {'DESCRIPTOR': _SUBGROUPKEYSEARCH, '__module__': 'public.dtcc_pb2'})
_sym_db.RegisterMessage(SubGroupKeySearch)
DtccTabResponse = _reflection.GeneratedProtocolMessageType('DtccTabResponse', (_message.Message,), {'DESCRIPTOR': _DTCCTABRESPONSE, '__module__': 'public.dtcc_pb2'})
_sym_db.RegisterMessage(DtccTabResponse)
DtccTabResponseData = _reflection.GeneratedProtocolMessageType('DtccTabResponseData', (_message.Message,), {'DESCRIPTOR': _DTCCTABRESPONSEDATA, '__module__': 'public.dtcc_pb2'})
_sym_db.RegisterMessage(DtccTabResponseData)
_DTCCSERVICE = DESCRIPTOR.services_by_name['DtccService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/public'
    _DTCCSERVICE.methods_by_name['GetDtccTable']._options = None
    _DTCCSERVICE.methods_by_name['GetDtccTable']._serialized_options = b'\x82\xd3\xe4\x93\x02\x15"\x10/api/v1/dtcc/tab:\x01*'
    _DTCCTABREQUEST._serialized_start = 119
    _DTCCTABREQUEST._serialized_end = 393
    _SUBGROUPKEYSEARCH._serialized_start = 395
    _SUBGROUPKEYSEARCH._serialized_end = 484
    _DTCCTABRESPONSE._serialized_start = 486
    _DTCCTABRESPONSE._serialized_end = 596
    _DTCCTABRESPONSEDATA._serialized_start = 598
    _DTCCTABRESPONSEDATA._serialized_end = 723
    _DTCCSERVICE._serialized_start = 725
    _DTCCSERVICE._serialized_end = 836