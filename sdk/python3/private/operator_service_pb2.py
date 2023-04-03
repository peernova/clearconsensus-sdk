"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ..google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eprivate/operator_service.proto\x12\x08titanium\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x19common/gateway_base.proto"0\n\nClientName\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t"v\n\x13ListClientsResponse\x121\n\x04data\x18\x01 \x01(\x0b2!.titanium.ListClientsResponseDataH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"@\n\x17ListClientsResponseData\x12%\n\x07clients\x18\x01 \x03(\x0b2\x14.titanium.ClientName"J\n\x12EvpStatusesRequest\x124\n\x10sliceRequestData\x18\x01 \x01(\x0b2\x1a.titanium.SliceRequestData"1\n\x10SliceRequestData\x12\x0e\n\x06offset\x18\x01 \x01(\x05\x12\r\n\x05limit\x18\x02 \x01(\x05"v\n\x13EvpStatusesResponse\x121\n\x04data\x18\x01 \x01(\x0b2!.titanium.EvpStatusesResponseDataH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"e\n\x17EvpStatusesResponseData\x12*\n\x0bevpStatuses\x18\x01 \x01(\x0b2\x15.titanium.EvpStatuses\x12\x1e\n\x05slice\x18\x02 \x01(\x0b2\x0f.titanium.Slice"7\n\x0bEvpStatuses\x12(\n\x0bevpStatuses\x18\x01 \x03(\x0b2\x13.titanium.EvpStatus"\x16\n\x05Slice\x12\r\n\x05total\x18\x01 \x01(\x03"\xb6\x01\n\tEvpStatus\x12\r\n\x05asset\x18\x01 \x01(\t\x12\x16\n\x0einstrumentType\x18\x02 \x01(\t\x12\x0c\n\x04date\x18\x03 \x01(\t\x12\x10\n\x08snapTime\x18\x04 \x01(\t\x12\x0e\n\x06status\x18\x05 \x01(\t\x12\x0e\n\x06dealer\x18\x06 \x01(\t\x12\x12\n\nuser_email\x18\x07 \x01(\t\x12\r\n\x05added\x18\x08 \x01(\t\x12\x0e\n\x06s3path\x18\t \x01(\t\x12\x0f\n\x07logPath\x18\n \x01(\t"Y\n\x10UploadEVPRequest\x12\x10\n\x08asset_id\x18\x01 \x01(\t\x12\x0c\n\x04date\x18\x02 \x01(\t\x12\x11\n\tfile_name\x18\x03 \x01(\t\x12\x12\n\ntrace_name\x18\x04 \x01(\t2\xd8\x03\n\x16OperatorServicePrivate\x12d\n\tAddClient\x12\x14.titanium.ClientName\x1a\x19.titanium.MessageResponse"&\x82\xd3\xe4\x93\x02 "\x1b/api/v1/operator/client/add:\x01*\x12j\n\x0bListClients\x12\x16.google.protobuf.Empty\x1a\x1d.titanium.ListClientsResponse"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/api/v1/operator/client/list\x12~\n\x0bEvpStatuses\x12\x1c.titanium.EvpStatusesRequest\x1a\x1d.titanium.EvpStatusesResponse"2\x82\xd3\xe4\x93\x02,"\'/api/v1/operator/evaluated-prices/slice:\x01*\x12l\n\tUploadEVP\x12\x1a.titanium.UploadEVPRequest\x1a\x1b.titanium.UploadURLResponse"&\x82\xd3\xe4\x93\x02 "\x1b/api/v1/operator/evp/upload:\x01*Bx\n com.peernova.titanium.interfacesB\x1bOperatorServiceProtoPrivateP\x01Z5github.com/peernova/clearconsensus-sdk/sdk/go/privateb\x06proto3')
_CLIENTNAME = DESCRIPTOR.message_types_by_name['ClientName']
_LISTCLIENTSRESPONSE = DESCRIPTOR.message_types_by_name['ListClientsResponse']
_LISTCLIENTSRESPONSEDATA = DESCRIPTOR.message_types_by_name['ListClientsResponseData']
_EVPSTATUSESREQUEST = DESCRIPTOR.message_types_by_name['EvpStatusesRequest']
_SLICEREQUESTDATA = DESCRIPTOR.message_types_by_name['SliceRequestData']
_EVPSTATUSESRESPONSE = DESCRIPTOR.message_types_by_name['EvpStatusesResponse']
_EVPSTATUSESRESPONSEDATA = DESCRIPTOR.message_types_by_name['EvpStatusesResponseData']
_EVPSTATUSES = DESCRIPTOR.message_types_by_name['EvpStatuses']
_SLICE = DESCRIPTOR.message_types_by_name['Slice']
_EVPSTATUS = DESCRIPTOR.message_types_by_name['EvpStatus']
_UPLOADEVPREQUEST = DESCRIPTOR.message_types_by_name['UploadEVPRequest']
ClientName = _reflection.GeneratedProtocolMessageType('ClientName', (_message.Message,), {'DESCRIPTOR': _CLIENTNAME, '__module__': 'private.operator_service_pb2'})
_sym_db.RegisterMessage(ClientName)
ListClientsResponse = _reflection.GeneratedProtocolMessageType('ListClientsResponse', (_message.Message,), {'DESCRIPTOR': _LISTCLIENTSRESPONSE, '__module__': 'private.operator_service_pb2'})
_sym_db.RegisterMessage(ListClientsResponse)
ListClientsResponseData = _reflection.GeneratedProtocolMessageType('ListClientsResponseData', (_message.Message,), {'DESCRIPTOR': _LISTCLIENTSRESPONSEDATA, '__module__': 'private.operator_service_pb2'})
_sym_db.RegisterMessage(ListClientsResponseData)
EvpStatusesRequest = _reflection.GeneratedProtocolMessageType('EvpStatusesRequest', (_message.Message,), {'DESCRIPTOR': _EVPSTATUSESREQUEST, '__module__': 'private.operator_service_pb2'})
_sym_db.RegisterMessage(EvpStatusesRequest)
SliceRequestData = _reflection.GeneratedProtocolMessageType('SliceRequestData', (_message.Message,), {'DESCRIPTOR': _SLICEREQUESTDATA, '__module__': 'private.operator_service_pb2'})
_sym_db.RegisterMessage(SliceRequestData)
EvpStatusesResponse = _reflection.GeneratedProtocolMessageType('EvpStatusesResponse', (_message.Message,), {'DESCRIPTOR': _EVPSTATUSESRESPONSE, '__module__': 'private.operator_service_pb2'})
_sym_db.RegisterMessage(EvpStatusesResponse)
EvpStatusesResponseData = _reflection.GeneratedProtocolMessageType('EvpStatusesResponseData', (_message.Message,), {'DESCRIPTOR': _EVPSTATUSESRESPONSEDATA, '__module__': 'private.operator_service_pb2'})
_sym_db.RegisterMessage(EvpStatusesResponseData)
EvpStatuses = _reflection.GeneratedProtocolMessageType('EvpStatuses', (_message.Message,), {'DESCRIPTOR': _EVPSTATUSES, '__module__': 'private.operator_service_pb2'})
_sym_db.RegisterMessage(EvpStatuses)
Slice = _reflection.GeneratedProtocolMessageType('Slice', (_message.Message,), {'DESCRIPTOR': _SLICE, '__module__': 'private.operator_service_pb2'})
_sym_db.RegisterMessage(Slice)
EvpStatus = _reflection.GeneratedProtocolMessageType('EvpStatus', (_message.Message,), {'DESCRIPTOR': _EVPSTATUS, '__module__': 'private.operator_service_pb2'})
_sym_db.RegisterMessage(EvpStatus)
UploadEVPRequest = _reflection.GeneratedProtocolMessageType('UploadEVPRequest', (_message.Message,), {'DESCRIPTOR': _UPLOADEVPREQUEST, '__module__': 'private.operator_service_pb2'})
_sym_db.RegisterMessage(UploadEVPRequest)
_OPERATORSERVICEPRIVATE = DESCRIPTOR.services_by_name['OperatorServicePrivate']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesB\x1bOperatorServiceProtoPrivateP\x01Z5github.com/peernova/clearconsensus-sdk/sdk/go/private'
    _OPERATORSERVICEPRIVATE.methods_by_name['AddClient']._options = None
    _OPERATORSERVICEPRIVATE.methods_by_name['AddClient']._serialized_options = b'\x82\xd3\xe4\x93\x02 "\x1b/api/v1/operator/client/add:\x01*'
    _OPERATORSERVICEPRIVATE.methods_by_name['ListClients']._options = None
    _OPERATORSERVICEPRIVATE.methods_by_name['ListClients']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1e\x12\x1c/api/v1/operator/client/list'
    _OPERATORSERVICEPRIVATE.methods_by_name['EvpStatuses']._options = None
    _OPERATORSERVICEPRIVATE.methods_by_name['EvpStatuses']._serialized_options = b'\x82\xd3\xe4\x93\x02,"\'/api/v1/operator/evaluated-prices/slice:\x01*'
    _OPERATORSERVICEPRIVATE.methods_by_name['UploadEVP']._options = None
    _OPERATORSERVICEPRIVATE.methods_by_name['UploadEVP']._serialized_options = b'\x82\xd3\xe4\x93\x02 "\x1b/api/v1/operator/evp/upload:\x01*'
    _CLIENTNAME._serialized_start = 130
    _CLIENTNAME._serialized_end = 178
    _LISTCLIENTSRESPONSE._serialized_start = 180
    _LISTCLIENTSRESPONSE._serialized_end = 298
    _LISTCLIENTSRESPONSEDATA._serialized_start = 300
    _LISTCLIENTSRESPONSEDATA._serialized_end = 364
    _EVPSTATUSESREQUEST._serialized_start = 366
    _EVPSTATUSESREQUEST._serialized_end = 440
    _SLICEREQUESTDATA._serialized_start = 442
    _SLICEREQUESTDATA._serialized_end = 491
    _EVPSTATUSESRESPONSE._serialized_start = 493
    _EVPSTATUSESRESPONSE._serialized_end = 611
    _EVPSTATUSESRESPONSEDATA._serialized_start = 613
    _EVPSTATUSESRESPONSEDATA._serialized_end = 714
    _EVPSTATUSES._serialized_start = 716
    _EVPSTATUSES._serialized_end = 771
    _SLICE._serialized_start = 773
    _SLICE._serialized_end = 795
    _EVPSTATUS._serialized_start = 798
    _EVPSTATUS._serialized_end = 980
    _UPLOADEVPREQUEST._serialized_start = 982
    _UPLOADEVPREQUEST._serialized_end = 1071
    _OPERATORSERVICEPRIVATE._serialized_start = 1074
    _OPERATORSERVICEPRIVATE._serialized_end = 1546