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
from ..common import assets_pb2 as common_dot_assets__pb2
from ..common import data_pb2 as common_dot_data__pb2
from ..common import outliers_pb2 as common_dot_outliers__pb2
from ..common import supported_fields_pb2 as common_dot_supported__fields__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dpublic/operator_service.proto\x12\x08titanium\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x19common/gateway_base.proto\x1a\x13common/assets.proto\x1a\x11common/data.proto\x1a\x15common/outliers.proto\x1a\x1dcommon/supported_fields.proto"J\n\x0fAddAssetRequest\x12\r\n\x05asset\x18\x01 \x01(\t\x12\x17\n\x0finstrument_type\x18\x02 \x01(\t\x12\x0f\n\x07service\x18\x03 \x01(\t"\\\n\x15SupportedFieldsValues\x12\x10\n\x08asset_id\x18\x01 \x01(\t\x12\r\n\x05field\x18\x02 \x01(\t\x12\x0e\n\x06values\x18\x03 \x03(\t\x12\x12\n\ntrace_name\x18\x04 \x01(\t"\x8b\x01\n\x17OperatorOutliersRequest\x12\x0c\n\x04date\x18\x01 \x01(\t\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12"\n\x07orderBy\x18\x03 \x01(\x0b2\x11.titanium.OrderBy\x12\x1e\n\x05limit\x18\x04 \x01(\x0b2\x0f.titanium.Limit\x12\x0e\n\x06offset\x18\x05 \x01(\x05"\x80\x01\n\x18OperatorOutliersResponse\x126\n\x04data\x18\x01 \x01(\x0b2&.titanium.OperatorOutliersResponseDataH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"|\n\x1cOperatorOutliersResponseData\x12%\n\x07columns\x18\x01 \x03(\x0b2\x14.titanium.ColumnInfo\x12!\n\x04rows\x18\x02 \x03(\x0b2\x13.titanium.ValuesRow\x12\x12\n\ntotal_rows\x18\x03 \x01(\x05"0\n\nClientName\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t"v\n\x13ListClientsResponse\x121\n\x04data\x18\x01 \x01(\x0b2!.titanium.ListClientsResponseDataH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"@\n\x17ListClientsResponseData\x12%\n\x07clients\x18\x01 \x03(\x0b2\x14.titanium.ClientName"J\n\x12EvpStatusesRequest\x124\n\x10sliceRequestData\x18\x01 \x01(\x0b2\x1a.titanium.SliceRequestData"1\n\x10SliceRequestData\x12\x0e\n\x06offset\x18\x01 \x01(\x05\x12\r\n\x05limit\x18\x02 \x01(\x05"v\n\x13EvpStatusesResponse\x121\n\x04data\x18\x01 \x01(\x0b2!.titanium.EvpStatusesResponseDataH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"e\n\x17EvpStatusesResponseData\x12*\n\x0bevpStatuses\x18\x01 \x01(\x0b2\x15.titanium.EvpStatuses\x12\x1e\n\x05slice\x18\x02 \x01(\x0b2\x0f.titanium.Slice"7\n\x0bEvpStatuses\x12(\n\x0bevpStatuses\x18\x01 \x03(\x0b2\x13.titanium.EvpStatus"\x16\n\x05Slice\x12\r\n\x05total\x18\x01 \x01(\x03"\xb6\x01\n\tEvpStatus\x12\r\n\x05asset\x18\x01 \x01(\t\x12\x16\n\x0einstrumentType\x18\x02 \x01(\t\x12\x0c\n\x04date\x18\x03 \x01(\t\x12\x10\n\x08snapTime\x18\x04 \x01(\t\x12\x0e\n\x06status\x18\x05 \x01(\t\x12\x0e\n\x06dealer\x18\x06 \x01(\t\x12\x12\n\nuser_email\x18\x07 \x01(\t\x12\r\n\x05added\x18\x08 \x01(\t\x12\x0e\n\x06s3path\x18\t \x01(\t\x12\x0f\n\x07logPath\x18\n \x01(\t"Y\n\x10UploadEVPRequest\x12\x10\n\x08asset_id\x18\x01 \x01(\t\x12\x0c\n\x04date\x18\x02 \x01(\t\x12\x11\n\tfile_name\x18\x03 \x01(\t\x12\x12\n\ntrace_name\x18\x04 \x01(\t"Z\n\x11UploadDTCCRequest\x12\x10\n\x08asset_id\x18\x01 \x01(\t\x12\x0c\n\x04date\x18\x02 \x01(\t\x12\x11\n\tfile_name\x18\x03 \x01(\t\x12\x12\n\ntrace_name\x18\x04 \x01(\t2\xf9\x0c\n\x16OperatorServicePrivate\x12d\n\tAddClient\x12\x14.titanium.ClientName\x1a\x19.titanium.MessageResponse"&\x82\xd3\xe4\x93\x02 "\x1b/api/v1/operator/client/add:\x01*\x12j\n\x0bListClients\x12\x16.google.protobuf.Empty\x1a\x1d.titanium.ListClientsResponse"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/api/v1/operator/client/list\x12~\n\x0bEvpStatuses\x12\x1c.titanium.EvpStatusesRequest\x1a\x1d.titanium.EvpStatusesResponse"2\x82\xd3\xe4\x93\x02,"\'/api/v1/operator/evaluated-prices/slice:\x01*\x12l\n\tUploadEVP\x12\x1a.titanium.UploadEVPRequest\x1a\x1b.titanium.UploadURLResponse"&\x82\xd3\xe4\x93\x02 "\x1b/api/v1/operator/evp/upload:\x01*\x12v\n\nUploadDTCC\x12\x1b.titanium.UploadDTCCRequest\x1a\x1b.titanium.UploadURLResponse".\x82\xd3\xe4\x93\x02("#/api/v1/operator/dtcc-trades/upload:\x01*\x12\x7f\n\x10OperatorOutliers\x12!.titanium.OperatorOutliersRequest\x1a".titanium.OperatorOutliersResponse"$\x82\xd3\xe4\x93\x02\x1e"\x19/api/v1/operator-outliers:\x01*\x12g\n\x08Outliers\x12\x19.titanium.OutliersRequest\x1a\x1a.titanium.OutliersResponse"$\x82\xd3\xe4\x93\x02\x1e"\x19/api/v1/operator/outliers:\x01*\x12\x84\x01\n\x15CreateSupportedFields\x12\x1f.titanium.SupportedFieldsValues\x1a\x19.titanium.MessageResponse"/\x82\xd3\xe4\x93\x02)"$/api/v1/operator/create/field-values:\x01*\x12~\n\x12AddSupportedFields\x12\x1f.titanium.SupportedFieldsValues\x1a\x19.titanium.MessageResponse",\x82\xd3\xe4\x93\x02&"!/api/v1/operator/add/field-values:\x01*\x12\x84\x01\n\x15DeleteSupportedFields\x12\x1f.titanium.SupportedFieldsValues\x1a\x19.titanium.MessageResponse"/\x82\xd3\xe4\x93\x02)"$/api/v1/operator/delete/field-values:\x01*\x12k\n\x0cExportReport\x12\x1d.titanium.ExportReportRequest\x1a\x18.titanium.ExportResponse""\x82\xd3\xe4\x93\x02\x1c"\x17/api/v1/operator/report:\x01*\x12h\n\x08AddAsset\x12\x19.titanium.AddAssetRequest\x1a\x19.titanium.MessageResponse"&\x82\xd3\xe4\x93\x02 "\x1b/api/v1/operator/assets/add:\x01*\x12w\n\x0cRecentAssets\x12\x1d.titanium.RecentAssetsRequest\x1a\x1e.titanium.RecentAssetsResponse"(\x82\xd3\xe4\x93\x02""\x1d/api/v1/operator/recentassets:\x01*\x12_\n\x06Assets\x12\x17.titanium.AssetsRequest\x1a\x18.titanium.AssetsResponse""\x82\xd3\xe4\x93\x02\x1c"\x17/api/v1/operator/assets:\x01*Bw\n com.peernova.titanium.interfacesB\x1bOperatorServiceProtoPrivateP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/publicb\x06proto3')
_ADDASSETREQUEST = DESCRIPTOR.message_types_by_name['AddAssetRequest']
_SUPPORTEDFIELDSVALUES = DESCRIPTOR.message_types_by_name['SupportedFieldsValues']
_OPERATOROUTLIERSREQUEST = DESCRIPTOR.message_types_by_name['OperatorOutliersRequest']
_OPERATOROUTLIERSRESPONSE = DESCRIPTOR.message_types_by_name['OperatorOutliersResponse']
_OPERATOROUTLIERSRESPONSEDATA = DESCRIPTOR.message_types_by_name['OperatorOutliersResponseData']
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
_UPLOADDTCCREQUEST = DESCRIPTOR.message_types_by_name['UploadDTCCRequest']
AddAssetRequest = _reflection.GeneratedProtocolMessageType('AddAssetRequest', (_message.Message,), {'DESCRIPTOR': _ADDASSETREQUEST, '__module__': 'public.operator_service_pb2'})
_sym_db.RegisterMessage(AddAssetRequest)
SupportedFieldsValues = _reflection.GeneratedProtocolMessageType('SupportedFieldsValues', (_message.Message,), {'DESCRIPTOR': _SUPPORTEDFIELDSVALUES, '__module__': 'public.operator_service_pb2'})
_sym_db.RegisterMessage(SupportedFieldsValues)
OperatorOutliersRequest = _reflection.GeneratedProtocolMessageType('OperatorOutliersRequest', (_message.Message,), {'DESCRIPTOR': _OPERATOROUTLIERSREQUEST, '__module__': 'public.operator_service_pb2'})
_sym_db.RegisterMessage(OperatorOutliersRequest)
OperatorOutliersResponse = _reflection.GeneratedProtocolMessageType('OperatorOutliersResponse', (_message.Message,), {'DESCRIPTOR': _OPERATOROUTLIERSRESPONSE, '__module__': 'public.operator_service_pb2'})
_sym_db.RegisterMessage(OperatorOutliersResponse)
OperatorOutliersResponseData = _reflection.GeneratedProtocolMessageType('OperatorOutliersResponseData', (_message.Message,), {'DESCRIPTOR': _OPERATOROUTLIERSRESPONSEDATA, '__module__': 'public.operator_service_pb2'})
_sym_db.RegisterMessage(OperatorOutliersResponseData)
ClientName = _reflection.GeneratedProtocolMessageType('ClientName', (_message.Message,), {'DESCRIPTOR': _CLIENTNAME, '__module__': 'public.operator_service_pb2'})
_sym_db.RegisterMessage(ClientName)
ListClientsResponse = _reflection.GeneratedProtocolMessageType('ListClientsResponse', (_message.Message,), {'DESCRIPTOR': _LISTCLIENTSRESPONSE, '__module__': 'public.operator_service_pb2'})
_sym_db.RegisterMessage(ListClientsResponse)
ListClientsResponseData = _reflection.GeneratedProtocolMessageType('ListClientsResponseData', (_message.Message,), {'DESCRIPTOR': _LISTCLIENTSRESPONSEDATA, '__module__': 'public.operator_service_pb2'})
_sym_db.RegisterMessage(ListClientsResponseData)
EvpStatusesRequest = _reflection.GeneratedProtocolMessageType('EvpStatusesRequest', (_message.Message,), {'DESCRIPTOR': _EVPSTATUSESREQUEST, '__module__': 'public.operator_service_pb2'})
_sym_db.RegisterMessage(EvpStatusesRequest)
SliceRequestData = _reflection.GeneratedProtocolMessageType('SliceRequestData', (_message.Message,), {'DESCRIPTOR': _SLICEREQUESTDATA, '__module__': 'public.operator_service_pb2'})
_sym_db.RegisterMessage(SliceRequestData)
EvpStatusesResponse = _reflection.GeneratedProtocolMessageType('EvpStatusesResponse', (_message.Message,), {'DESCRIPTOR': _EVPSTATUSESRESPONSE, '__module__': 'public.operator_service_pb2'})
_sym_db.RegisterMessage(EvpStatusesResponse)
EvpStatusesResponseData = _reflection.GeneratedProtocolMessageType('EvpStatusesResponseData', (_message.Message,), {'DESCRIPTOR': _EVPSTATUSESRESPONSEDATA, '__module__': 'public.operator_service_pb2'})
_sym_db.RegisterMessage(EvpStatusesResponseData)
EvpStatuses = _reflection.GeneratedProtocolMessageType('EvpStatuses', (_message.Message,), {'DESCRIPTOR': _EVPSTATUSES, '__module__': 'public.operator_service_pb2'})
_sym_db.RegisterMessage(EvpStatuses)
Slice = _reflection.GeneratedProtocolMessageType('Slice', (_message.Message,), {'DESCRIPTOR': _SLICE, '__module__': 'public.operator_service_pb2'})
_sym_db.RegisterMessage(Slice)
EvpStatus = _reflection.GeneratedProtocolMessageType('EvpStatus', (_message.Message,), {'DESCRIPTOR': _EVPSTATUS, '__module__': 'public.operator_service_pb2'})
_sym_db.RegisterMessage(EvpStatus)
UploadEVPRequest = _reflection.GeneratedProtocolMessageType('UploadEVPRequest', (_message.Message,), {'DESCRIPTOR': _UPLOADEVPREQUEST, '__module__': 'public.operator_service_pb2'})
_sym_db.RegisterMessage(UploadEVPRequest)
UploadDTCCRequest = _reflection.GeneratedProtocolMessageType('UploadDTCCRequest', (_message.Message,), {'DESCRIPTOR': _UPLOADDTCCREQUEST, '__module__': 'public.operator_service_pb2'})
_sym_db.RegisterMessage(UploadDTCCRequest)
_OPERATORSERVICEPRIVATE = DESCRIPTOR.services_by_name['OperatorServicePrivate']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesB\x1bOperatorServiceProtoPrivateP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/public'
    _OPERATORSERVICEPRIVATE.methods_by_name['AddClient']._options = None
    _OPERATORSERVICEPRIVATE.methods_by_name['AddClient']._serialized_options = b'\x82\xd3\xe4\x93\x02 "\x1b/api/v1/operator/client/add:\x01*'
    _OPERATORSERVICEPRIVATE.methods_by_name['ListClients']._options = None
    _OPERATORSERVICEPRIVATE.methods_by_name['ListClients']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1e\x12\x1c/api/v1/operator/client/list'
    _OPERATORSERVICEPRIVATE.methods_by_name['EvpStatuses']._options = None
    _OPERATORSERVICEPRIVATE.methods_by_name['EvpStatuses']._serialized_options = b'\x82\xd3\xe4\x93\x02,"\'/api/v1/operator/evaluated-prices/slice:\x01*'
    _OPERATORSERVICEPRIVATE.methods_by_name['UploadEVP']._options = None
    _OPERATORSERVICEPRIVATE.methods_by_name['UploadEVP']._serialized_options = b'\x82\xd3\xe4\x93\x02 "\x1b/api/v1/operator/evp/upload:\x01*'
    _OPERATORSERVICEPRIVATE.methods_by_name['UploadDTCC']._options = None
    _OPERATORSERVICEPRIVATE.methods_by_name['UploadDTCC']._serialized_options = b'\x82\xd3\xe4\x93\x02("#/api/v1/operator/dtcc-trades/upload:\x01*'
    _OPERATORSERVICEPRIVATE.methods_by_name['OperatorOutliers']._options = None
    _OPERATORSERVICEPRIVATE.methods_by_name['OperatorOutliers']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1e"\x19/api/v1/operator-outliers:\x01*'
    _OPERATORSERVICEPRIVATE.methods_by_name['Outliers']._options = None
    _OPERATORSERVICEPRIVATE.methods_by_name['Outliers']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1e"\x19/api/v1/operator/outliers:\x01*'
    _OPERATORSERVICEPRIVATE.methods_by_name['CreateSupportedFields']._options = None
    _OPERATORSERVICEPRIVATE.methods_by_name['CreateSupportedFields']._serialized_options = b'\x82\xd3\xe4\x93\x02)"$/api/v1/operator/create/field-values:\x01*'
    _OPERATORSERVICEPRIVATE.methods_by_name['AddSupportedFields']._options = None
    _OPERATORSERVICEPRIVATE.methods_by_name['AddSupportedFields']._serialized_options = b'\x82\xd3\xe4\x93\x02&"!/api/v1/operator/add/field-values:\x01*'
    _OPERATORSERVICEPRIVATE.methods_by_name['DeleteSupportedFields']._options = None
    _OPERATORSERVICEPRIVATE.methods_by_name['DeleteSupportedFields']._serialized_options = b'\x82\xd3\xe4\x93\x02)"$/api/v1/operator/delete/field-values:\x01*'
    _OPERATORSERVICEPRIVATE.methods_by_name['ExportReport']._options = None
    _OPERATORSERVICEPRIVATE.methods_by_name['ExportReport']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1c"\x17/api/v1/operator/report:\x01*'
    _OPERATORSERVICEPRIVATE.methods_by_name['AddAsset']._options = None
    _OPERATORSERVICEPRIVATE.methods_by_name['AddAsset']._serialized_options = b'\x82\xd3\xe4\x93\x02 "\x1b/api/v1/operator/assets/add:\x01*'
    _OPERATORSERVICEPRIVATE.methods_by_name['RecentAssets']._options = None
    _OPERATORSERVICEPRIVATE.methods_by_name['RecentAssets']._serialized_options = b'\x82\xd3\xe4\x93\x02""\x1d/api/v1/operator/recentassets:\x01*'
    _OPERATORSERVICEPRIVATE.methods_by_name['Assets']._options = None
    _OPERATORSERVICEPRIVATE.methods_by_name['Assets']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1c"\x17/api/v1/operator/assets:\x01*'
    _ADDASSETREQUEST._serialized_start = 223
    _ADDASSETREQUEST._serialized_end = 297
    _SUPPORTEDFIELDSVALUES._serialized_start = 299
    _SUPPORTEDFIELDSVALUES._serialized_end = 391
    _OPERATOROUTLIERSREQUEST._serialized_start = 394
    _OPERATOROUTLIERSREQUEST._serialized_end = 533
    _OPERATOROUTLIERSRESPONSE._serialized_start = 536
    _OPERATOROUTLIERSRESPONSE._serialized_end = 664
    _OPERATOROUTLIERSRESPONSEDATA._serialized_start = 666
    _OPERATOROUTLIERSRESPONSEDATA._serialized_end = 790
    _CLIENTNAME._serialized_start = 792
    _CLIENTNAME._serialized_end = 840
    _LISTCLIENTSRESPONSE._serialized_start = 842
    _LISTCLIENTSRESPONSE._serialized_end = 960
    _LISTCLIENTSRESPONSEDATA._serialized_start = 962
    _LISTCLIENTSRESPONSEDATA._serialized_end = 1026
    _EVPSTATUSESREQUEST._serialized_start = 1028
    _EVPSTATUSESREQUEST._serialized_end = 1102
    _SLICEREQUESTDATA._serialized_start = 1104
    _SLICEREQUESTDATA._serialized_end = 1153
    _EVPSTATUSESRESPONSE._serialized_start = 1155
    _EVPSTATUSESRESPONSE._serialized_end = 1273
    _EVPSTATUSESRESPONSEDATA._serialized_start = 1275
    _EVPSTATUSESRESPONSEDATA._serialized_end = 1376
    _EVPSTATUSES._serialized_start = 1378
    _EVPSTATUSES._serialized_end = 1433
    _SLICE._serialized_start = 1435
    _SLICE._serialized_end = 1457
    _EVPSTATUS._serialized_start = 1460
    _EVPSTATUS._serialized_end = 1642
    _UPLOADEVPREQUEST._serialized_start = 1644
    _UPLOADEVPREQUEST._serialized_end = 1733
    _UPLOADDTCCREQUEST._serialized_start = 1735
    _UPLOADDTCCREQUEST._serialized_end = 1825
    _OPERATORSERVICEPRIVATE._serialized_start = 1828
    _OPERATORSERVICEPRIVATE._serialized_end = 3485