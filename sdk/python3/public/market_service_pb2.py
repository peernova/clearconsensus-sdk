"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ..google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from ..common import market_pb2 as common_dot_market__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bpublic/market_service.proto\x12\x08titanium\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x13common/market.proto2}\n\rMarketService\x12l\n\x0eMarketSnapTime\x12\x16.google.protobuf.Empty\x1a .titanium.MarketSnapTimeResponse" \x82\xd3\xe4\x93\x02\x1a\x12\x18/api/v1/market/snap-timeBt\n com.peernova.titanium.interfacesB\x18MarketServiceProtoPublicP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/publicb\x06proto3')
_MARKETSERVICE = DESCRIPTOR.services_by_name['MarketService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesB\x18MarketServiceProtoPublicP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/public'
    _MARKETSERVICE.methods_by_name['MarketSnapTime']._options = None
    _MARKETSERVICE.methods_by_name['MarketSnapTime']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1a\x12\x18/api/v1/market/snap-time'
    _MARKETSERVICE._serialized_start = 121
    _MARKETSERVICE._serialized_end = 246