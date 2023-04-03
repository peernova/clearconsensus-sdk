"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ..google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from ..common import assets_pb2 as common_dot_assets__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bpublic/assets_service.proto\x12\x08titanium\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x13common/assets.proto2\xab\x03\n\rAssetsService\x12n\n\x0cRecentAssets\x12\x1d.titanium.RecentAssetsRequest\x1a\x1e.titanium.RecentAssetsResponse"\x1f\x82\xd3\xe4\x93\x02\x19"\x14/api/v1/recentassets:\x01*\x12g\n\nAssetsList\x12\x1b.titanium.AssetsListRequest\x1a\x1c.titanium.AssetsListResponse"\x1e\x82\xd3\xe4\x93\x02\x18"\x13/api/v1/assets/list:\x01*\x12V\n\x06Assets\x12\x17.titanium.AssetsRequest\x1a\x18.titanium.AssetsResponse"\x19\x82\xd3\xe4\x93\x02\x13"\x0e/api/v1/assets:\x01*\x12i\n\x0fSupportedAssets\x12\x16.google.protobuf.Empty\x1a\x1c.titanium.AssetsListResponse" \x82\xd3\xe4\x93\x02\x1a\x12\x18/api/v1/supported/assetsBt\n com.peernova.titanium.interfacesB\x18AssetsServiceProtoPublicP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/publicb\x06proto3')
_ASSETSSERVICE = DESCRIPTOR.services_by_name['AssetsService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesB\x18AssetsServiceProtoPublicP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/public'
    _ASSETSSERVICE.methods_by_name['RecentAssets']._options = None
    _ASSETSSERVICE.methods_by_name['RecentAssets']._serialized_options = b'\x82\xd3\xe4\x93\x02\x19"\x14/api/v1/recentassets:\x01*'
    _ASSETSSERVICE.methods_by_name['AssetsList']._options = None
    _ASSETSSERVICE.methods_by_name['AssetsList']._serialized_options = b'\x82\xd3\xe4\x93\x02\x18"\x13/api/v1/assets/list:\x01*'
    _ASSETSSERVICE.methods_by_name['Assets']._options = None
    _ASSETSSERVICE.methods_by_name['Assets']._serialized_options = b'\x82\xd3\xe4\x93\x02\x13"\x0e/api/v1/assets:\x01*'
    _ASSETSSERVICE.methods_by_name['SupportedAssets']._options = None
    _ASSETSSERVICE.methods_by_name['SupportedAssets']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1a\x12\x18/api/v1/supported/assets'
    _ASSETSSERVICE._serialized_start = 122
    _ASSETSSERVICE._serialized_end = 549