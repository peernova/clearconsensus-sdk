"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13common/market.proto\x12\x08titanium\x1a\x19common/gateway_base.proto"k\n\x16MarketSnapTimeResponse\x12#\n\x04data\x18\x01 \x01(\x0b2\x13.titanium.SnapTimesH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"\x1f\n\tSnapTimes\x12\x12\n\nsnap_times\x18\x01 \x03(\tBt\n com.peernova.titanium.interfacesB\x18MarketServiceProtoCommonP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/commonb\x06proto3')
_MARKETSNAPTIMERESPONSE = DESCRIPTOR.message_types_by_name['MarketSnapTimeResponse']
_SNAPTIMES = DESCRIPTOR.message_types_by_name['SnapTimes']
MarketSnapTimeResponse = _reflection.GeneratedProtocolMessageType('MarketSnapTimeResponse', (_message.Message,), {'DESCRIPTOR': _MARKETSNAPTIMERESPONSE, '__module__': 'common.market_pb2'})
_sym_db.RegisterMessage(MarketSnapTimeResponse)
SnapTimes = _reflection.GeneratedProtocolMessageType('SnapTimes', (_message.Message,), {'DESCRIPTOR': _SNAPTIMES, '__module__': 'common.market_pb2'})
_sym_db.RegisterMessage(SnapTimes)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesB\x18MarketServiceProtoCommonP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/common'
    _MARKETSNAPTIMERESPONSE._serialized_start = 60
    _MARKETSNAPTIMERESPONSE._serialized_end = 167
    _SNAPTIMES._serialized_start = 169
    _SNAPTIMES._serialized_end = 200