"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ..google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ..common import charts_pb2 as common_dot_charts__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bpublic/charts_service.proto\x12\x08titanium\x1a\x1cgoogle/api/annotations.proto\x1a\x13common/charts.proto2\xe8\x01\n\rChartsService\x12V\n\x06Charts\x12\x17.titanium.ChartsRequest\x1a\x18.titanium.ChartsResponse"\x19\x82\xd3\xe4\x93\x02\x13"\x0e/api/v1/charts:\x01*\x12\x7f\n\x10ChartsCurrencies\x12!.titanium.ChartsCurrenciesRequest\x1a".titanium.ChartsCurrenciesResponse"$\x82\xd3\xe4\x93\x02\x1e"\x19/api/v1/charts/currencies:\x01*Bt\n com.peernova.titanium.interfacesB\x18ChartsServiceProtoPublicP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/publicb\x06proto3')
_CHARTSSERVICE = DESCRIPTOR.services_by_name['ChartsService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesB\x18ChartsServiceProtoPublicP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/public'
    _CHARTSSERVICE.methods_by_name['Charts']._options = None
    _CHARTSSERVICE.methods_by_name['Charts']._serialized_options = b'\x82\xd3\xe4\x93\x02\x13"\x0e/api/v1/charts:\x01*'
    _CHARTSSERVICE.methods_by_name['ChartsCurrencies']._options = None
    _CHARTSSERVICE.methods_by_name['ChartsCurrencies']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1e"\x19/api/v1/charts/currencies:\x01*'
    _CHARTSSERVICE._serialized_start = 93
    _CHARTSSERVICE._serialized_end = 325