"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13common/assets.proto\x12\x08titanium\x1a\x19common/gateway_base.proto"y\n\x13RecentAssetsRequest\x12\x1e\n\x05limit\x18\x01 \x01(\x0b2\x0f.titanium.Limit\x12\x0e\n\x06offset\x18\x02 \x01(\x05\x12"\n\x07orderBy\x18\x03 \x01(\x0b2\x11.titanium.OrderBy\x12\x0e\n\x06filter\x18\x04 \x01(\t"x\n\x14RecentAssetsResponse\x122\n\x04data\x18\x01 \x01(\x0b2".titanium.RecentAssetsResponseDataH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"~\n\x18RecentAssetsResponseData\x12%\n\x07columns\x18\x01 \x03(\x0b2\x14.titanium.ColumnInfo\x12\'\n\x04rows\x18\x02 \x03(\x0b2\x19.titanium.RecentAssetsRow\x12\x12\n\ntotal_rows\x18\x03 \x01(\x05"!\n\x0fRecentAssetsRow\x12\x0e\n\x06values\x18\x01 \x03(\t"&\n\x11AssetsListRequest\x12\x11\n\tsnap_time\x18\x01 \x01(\t"h\n\x12AssetsListResponse\x12$\n\x04data\x18\x01 \x01(\x0b2\x14.titanium.AssetsListH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"-\n\nAssetsList\x12\x1f\n\x06assets\x18\x01 \x03(\x0b2\x0f.titanium.Asset":\n\x05Asset\x12\x0c\n\x04name\x18\x01 \x01(\t\x12#\n\x08services\x18\x02 \x03(\x0b2\x11.titanium.Service"?\n\x07Service\x12\x0c\n\x04name\x18\x01 \x01(\t\x12&\n\nsub_assets\x18\x02 \x03(\x0b2\x12.titanium.SubAsset"8\n\x08SubAsset\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x12\n\ntrace_name\x18\x03 \x01(\t"\x99\x01\n\rAssetsRequest\x12\x10\n\x08asset_id\x18\x01 \x01(\t\x12"\n\x07orderBy\x18\x02 \x01(\x0b2\x11.titanium.OrderBy\x12\x1e\n\x05limit\x18\x03 \x01(\x0b2\x0f.titanium.Limit\x12\x0e\n\x06offset\x18\x04 \x01(\x05\x12\x0e\n\x06filter\x18\x05 \x01(\t\x12\x12\n\ntrace_name\x18\x06 \x01(\t"f\n\x0eAssetsResponse\x12&\n\x04data\x18\x01 \x01(\x0b2\x16.titanium.ResponseDataH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"r\n\x12AssetsResponseData\x12%\n\x07columns\x18\x01 \x03(\x0b2\x14.titanium.ColumnInfo\x12!\n\x04rows\x18\x02 \x03(\x0b2\x13.titanium.AssetsRow\x12\x12\n\ntotal_rows\x18\x03 \x01(\x05"\x1b\n\tAssetsRow\x12\x0e\n\x06values\x18\x01 \x03(\tBt\n com.peernova.titanium.interfacesB\x18AssetsServiceProtoCommonP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/commonb\x06proto3')
_RECENTASSETSREQUEST = DESCRIPTOR.message_types_by_name['RecentAssetsRequest']
_RECENTASSETSRESPONSE = DESCRIPTOR.message_types_by_name['RecentAssetsResponse']
_RECENTASSETSRESPONSEDATA = DESCRIPTOR.message_types_by_name['RecentAssetsResponseData']
_RECENTASSETSROW = DESCRIPTOR.message_types_by_name['RecentAssetsRow']
_ASSETSLISTREQUEST = DESCRIPTOR.message_types_by_name['AssetsListRequest']
_ASSETSLISTRESPONSE = DESCRIPTOR.message_types_by_name['AssetsListResponse']
_ASSETSLIST = DESCRIPTOR.message_types_by_name['AssetsList']
_ASSET = DESCRIPTOR.message_types_by_name['Asset']
_SERVICE = DESCRIPTOR.message_types_by_name['Service']
_SUBASSET = DESCRIPTOR.message_types_by_name['SubAsset']
_ASSETSREQUEST = DESCRIPTOR.message_types_by_name['AssetsRequest']
_ASSETSRESPONSE = DESCRIPTOR.message_types_by_name['AssetsResponse']
_ASSETSRESPONSEDATA = DESCRIPTOR.message_types_by_name['AssetsResponseData']
_ASSETSROW = DESCRIPTOR.message_types_by_name['AssetsRow']
RecentAssetsRequest = _reflection.GeneratedProtocolMessageType('RecentAssetsRequest', (_message.Message,), {'DESCRIPTOR': _RECENTASSETSREQUEST, '__module__': 'common.assets_pb2'})
_sym_db.RegisterMessage(RecentAssetsRequest)
RecentAssetsResponse = _reflection.GeneratedProtocolMessageType('RecentAssetsResponse', (_message.Message,), {'DESCRIPTOR': _RECENTASSETSRESPONSE, '__module__': 'common.assets_pb2'})
_sym_db.RegisterMessage(RecentAssetsResponse)
RecentAssetsResponseData = _reflection.GeneratedProtocolMessageType('RecentAssetsResponseData', (_message.Message,), {'DESCRIPTOR': _RECENTASSETSRESPONSEDATA, '__module__': 'common.assets_pb2'})
_sym_db.RegisterMessage(RecentAssetsResponseData)
RecentAssetsRow = _reflection.GeneratedProtocolMessageType('RecentAssetsRow', (_message.Message,), {'DESCRIPTOR': _RECENTASSETSROW, '__module__': 'common.assets_pb2'})
_sym_db.RegisterMessage(RecentAssetsRow)
AssetsListRequest = _reflection.GeneratedProtocolMessageType('AssetsListRequest', (_message.Message,), {'DESCRIPTOR': _ASSETSLISTREQUEST, '__module__': 'common.assets_pb2'})
_sym_db.RegisterMessage(AssetsListRequest)
AssetsListResponse = _reflection.GeneratedProtocolMessageType('AssetsListResponse', (_message.Message,), {'DESCRIPTOR': _ASSETSLISTRESPONSE, '__module__': 'common.assets_pb2'})
_sym_db.RegisterMessage(AssetsListResponse)
AssetsList = _reflection.GeneratedProtocolMessageType('AssetsList', (_message.Message,), {'DESCRIPTOR': _ASSETSLIST, '__module__': 'common.assets_pb2'})
_sym_db.RegisterMessage(AssetsList)
Asset = _reflection.GeneratedProtocolMessageType('Asset', (_message.Message,), {'DESCRIPTOR': _ASSET, '__module__': 'common.assets_pb2'})
_sym_db.RegisterMessage(Asset)
Service = _reflection.GeneratedProtocolMessageType('Service', (_message.Message,), {'DESCRIPTOR': _SERVICE, '__module__': 'common.assets_pb2'})
_sym_db.RegisterMessage(Service)
SubAsset = _reflection.GeneratedProtocolMessageType('SubAsset', (_message.Message,), {'DESCRIPTOR': _SUBASSET, '__module__': 'common.assets_pb2'})
_sym_db.RegisterMessage(SubAsset)
AssetsRequest = _reflection.GeneratedProtocolMessageType('AssetsRequest', (_message.Message,), {'DESCRIPTOR': _ASSETSREQUEST, '__module__': 'common.assets_pb2'})
_sym_db.RegisterMessage(AssetsRequest)
AssetsResponse = _reflection.GeneratedProtocolMessageType('AssetsResponse', (_message.Message,), {'DESCRIPTOR': _ASSETSRESPONSE, '__module__': 'common.assets_pb2'})
_sym_db.RegisterMessage(AssetsResponse)
AssetsResponseData = _reflection.GeneratedProtocolMessageType('AssetsResponseData', (_message.Message,), {'DESCRIPTOR': _ASSETSRESPONSEDATA, '__module__': 'common.assets_pb2'})
_sym_db.RegisterMessage(AssetsResponseData)
AssetsRow = _reflection.GeneratedProtocolMessageType('AssetsRow', (_message.Message,), {'DESCRIPTOR': _ASSETSROW, '__module__': 'common.assets_pb2'})
_sym_db.RegisterMessage(AssetsRow)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesB\x18AssetsServiceProtoCommonP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/common'
    _RECENTASSETSREQUEST._serialized_start = 60
    _RECENTASSETSREQUEST._serialized_end = 181
    _RECENTASSETSRESPONSE._serialized_start = 183
    _RECENTASSETSRESPONSE._serialized_end = 303
    _RECENTASSETSRESPONSEDATA._serialized_start = 305
    _RECENTASSETSRESPONSEDATA._serialized_end = 431
    _RECENTASSETSROW._serialized_start = 433
    _RECENTASSETSROW._serialized_end = 466
    _ASSETSLISTREQUEST._serialized_start = 468
    _ASSETSLISTREQUEST._serialized_end = 506
    _ASSETSLISTRESPONSE._serialized_start = 508
    _ASSETSLISTRESPONSE._serialized_end = 612
    _ASSETSLIST._serialized_start = 614
    _ASSETSLIST._serialized_end = 659
    _ASSET._serialized_start = 661
    _ASSET._serialized_end = 719
    _SERVICE._serialized_start = 721
    _SERVICE._serialized_end = 784
    _SUBASSET._serialized_start = 786
    _SUBASSET._serialized_end = 842
    _ASSETSREQUEST._serialized_start = 845
    _ASSETSREQUEST._serialized_end = 998
    _ASSETSRESPONSE._serialized_start = 1000
    _ASSETSRESPONSE._serialized_end = 1102
    _ASSETSRESPONSEDATA._serialized_start = 1104
    _ASSETSRESPONSEDATA._serialized_end = 1218
    _ASSETSROW._serialized_start = 1220
    _ASSETSROW._serialized_end = 1247