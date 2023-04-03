"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ..google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2
from ..common import assets_pb2 as common_dot_assets__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$private/assets_private_service.proto\x12\x08titanium\x1a\x1cgoogle/api/annotations.proto\x1a\x19common/gateway_base.proto\x1a\x13common/assets.proto"J\n\x0fAddAssetRequest\x12\r\n\x05asset\x18\x01 \x01(\t\x12\x17\n\x0finstrument_type\x18\x02 \x01(\t\x12\x0f\n\x07service\x18\x03 \x01(\t2\xda\x02\n\x14AssetsPrivateService\x12h\n\x08AddAsset\x12\x19.titanium.AddAssetRequest\x1a\x19.titanium.MessageResponse"&\x82\xd3\xe4\x93\x02 "\x1b/api/v1/operator/assets/add:\x01*\x12w\n\x0cRecentAssets\x12\x1d.titanium.RecentAssetsRequest\x1a\x1e.titanium.RecentAssetsResponse"(\x82\xd3\xe4\x93\x02""\x1d/api/v1/operator/recentassets:\x01*\x12_\n\x06Assets\x12\x17.titanium.AssetsRequest\x1a\x18.titanium.AssetsResponse""\x82\xd3\xe4\x93\x02\x1c"\x17/api/v1/operator/assets:\x01*Bv\n com.peernova.titanium.interfacesB\x19AssetsServiceProtoPrivateP\x01Z5github.com/peernova/clearconsensus-sdk/sdk/go/privateb\x06proto3')
_ADDASSETREQUEST = DESCRIPTOR.message_types_by_name['AddAssetRequest']
AddAssetRequest = _reflection.GeneratedProtocolMessageType('AddAssetRequest', (_message.Message,), {'DESCRIPTOR': _ADDASSETREQUEST, '__module__': 'private.assets_private_service_pb2'})
_sym_db.RegisterMessage(AddAssetRequest)
_ASSETSPRIVATESERVICE = DESCRIPTOR.services_by_name['AssetsPrivateService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesB\x19AssetsServiceProtoPrivateP\x01Z5github.com/peernova/clearconsensus-sdk/sdk/go/private'
    _ASSETSPRIVATESERVICE.methods_by_name['AddAsset']._options = None
    _ASSETSPRIVATESERVICE.methods_by_name['AddAsset']._serialized_options = b'\x82\xd3\xe4\x93\x02 "\x1b/api/v1/operator/assets/add:\x01*'
    _ASSETSPRIVATESERVICE.methods_by_name['RecentAssets']._options = None
    _ASSETSPRIVATESERVICE.methods_by_name['RecentAssets']._serialized_options = b'\x82\xd3\xe4\x93\x02""\x1d/api/v1/operator/recentassets:\x01*'
    _ASSETSPRIVATESERVICE.methods_by_name['Assets']._options = None
    _ASSETSPRIVATESERVICE.methods_by_name['Assets']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1c"\x17/api/v1/operator/assets:\x01*'
    _ADDASSETREQUEST._serialized_start = 128
    _ADDASSETREQUEST._serialized_end = 202
    _ASSETSPRIVATESERVICE._serialized_start = 205
    _ASSETSPRIVATESERVICE._serialized_end = 551