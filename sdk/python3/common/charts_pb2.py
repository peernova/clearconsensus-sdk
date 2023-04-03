"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13common/charts.proto\x12\x08titanium\x1a\x19common/gateway_base.proto"q\n\rChartsRequest\x12\x10\n\x08asset_id\x18\x01 \x01(\t\x12\x12\n\nunderlying\x18\x02 \x01(\t\x12\x16\n\x0esubmitted_date\x18\x03 \x01(\t\x12\x0e\n\x06client\x18\x04 \x01(\t\x12\x12\n\ntrace_name\x18\x05 \x01(\t"l\n\x0eChartsResponse\x12,\n\x04data\x18\x01 \x01(\x0b2\x1c.titanium.ChartsResponseDataH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"\xae\x01\n\x12ChartsResponseData\x12+\n\x08outliers\x18\x01 \x03(\x0b2\x19.titanium.OutlierMetadata\x12.\n\tbenchmark\x18\x02 \x03(\x0b2\x1b.titanium.BenchmarkMetadata\x12+\n\x0cchartSources\x18\x03 \x03(\x0b2\x15.titanium.ChartSource\x12\x0e\n\x06tenors\x18\x04 \x03(\t"<\n\x0bChartSource\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1f\n\x06charts\x18\x02 \x03(\x0b2\x0f.titanium.Chart";\n\x05Chart\x12\x0c\n\x04name\x18\x01 \x01(\t\x12$\n\x06points\x18\x02 \x03(\x0b2\x14.titanium.ChartPoint"*\n\nChartPoint\x12\r\n\x05tenor\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01"W\n\x17ChartsCurrenciesRequest\x12\x10\n\x08asset_id\x18\x01 \x01(\t\x12\x16\n\x0esubmitted_date\x18\x02 \x01(\t\x12\x12\n\ntrace_name\x18\x03 \x01(\t"\x80\x01\n\x18ChartsCurrenciesResponse\x126\n\x04data\x18\x01 \x01(\x0b2&.titanium.ChartsCurrenciesResponseDataH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"5\n\x1cChartsCurrenciesResponseData\x12\x15\n\rcurrencyPairs\x18\x01 \x03(\tBt\n com.peernova.titanium.interfacesB\x18ChartsServiceProtoCommonP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/commonb\x06proto3')
_CHARTSREQUEST = DESCRIPTOR.message_types_by_name['ChartsRequest']
_CHARTSRESPONSE = DESCRIPTOR.message_types_by_name['ChartsResponse']
_CHARTSRESPONSEDATA = DESCRIPTOR.message_types_by_name['ChartsResponseData']
_CHARTSOURCE = DESCRIPTOR.message_types_by_name['ChartSource']
_CHART = DESCRIPTOR.message_types_by_name['Chart']
_CHARTPOINT = DESCRIPTOR.message_types_by_name['ChartPoint']
_CHARTSCURRENCIESREQUEST = DESCRIPTOR.message_types_by_name['ChartsCurrenciesRequest']
_CHARTSCURRENCIESRESPONSE = DESCRIPTOR.message_types_by_name['ChartsCurrenciesResponse']
_CHARTSCURRENCIESRESPONSEDATA = DESCRIPTOR.message_types_by_name['ChartsCurrenciesResponseData']
ChartsRequest = _reflection.GeneratedProtocolMessageType('ChartsRequest', (_message.Message,), {'DESCRIPTOR': _CHARTSREQUEST, '__module__': 'common.charts_pb2'})
_sym_db.RegisterMessage(ChartsRequest)
ChartsResponse = _reflection.GeneratedProtocolMessageType('ChartsResponse', (_message.Message,), {'DESCRIPTOR': _CHARTSRESPONSE, '__module__': 'common.charts_pb2'})
_sym_db.RegisterMessage(ChartsResponse)
ChartsResponseData = _reflection.GeneratedProtocolMessageType('ChartsResponseData', (_message.Message,), {'DESCRIPTOR': _CHARTSRESPONSEDATA, '__module__': 'common.charts_pb2'})
_sym_db.RegisterMessage(ChartsResponseData)
ChartSource = _reflection.GeneratedProtocolMessageType('ChartSource', (_message.Message,), {'DESCRIPTOR': _CHARTSOURCE, '__module__': 'common.charts_pb2'})
_sym_db.RegisterMessage(ChartSource)
Chart = _reflection.GeneratedProtocolMessageType('Chart', (_message.Message,), {'DESCRIPTOR': _CHART, '__module__': 'common.charts_pb2'})
_sym_db.RegisterMessage(Chart)
ChartPoint = _reflection.GeneratedProtocolMessageType('ChartPoint', (_message.Message,), {'DESCRIPTOR': _CHARTPOINT, '__module__': 'common.charts_pb2'})
_sym_db.RegisterMessage(ChartPoint)
ChartsCurrenciesRequest = _reflection.GeneratedProtocolMessageType('ChartsCurrenciesRequest', (_message.Message,), {'DESCRIPTOR': _CHARTSCURRENCIESREQUEST, '__module__': 'common.charts_pb2'})
_sym_db.RegisterMessage(ChartsCurrenciesRequest)
ChartsCurrenciesResponse = _reflection.GeneratedProtocolMessageType('ChartsCurrenciesResponse', (_message.Message,), {'DESCRIPTOR': _CHARTSCURRENCIESRESPONSE, '__module__': 'common.charts_pb2'})
_sym_db.RegisterMessage(ChartsCurrenciesResponse)
ChartsCurrenciesResponseData = _reflection.GeneratedProtocolMessageType('ChartsCurrenciesResponseData', (_message.Message,), {'DESCRIPTOR': _CHARTSCURRENCIESRESPONSEDATA, '__module__': 'common.charts_pb2'})
_sym_db.RegisterMessage(ChartsCurrenciesResponseData)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesB\x18ChartsServiceProtoCommonP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/common'
    _CHARTSREQUEST._serialized_start = 60
    _CHARTSREQUEST._serialized_end = 173
    _CHARTSRESPONSE._serialized_start = 175
    _CHARTSRESPONSE._serialized_end = 283
    _CHARTSRESPONSEDATA._serialized_start = 286
    _CHARTSRESPONSEDATA._serialized_end = 460
    _CHARTSOURCE._serialized_start = 462
    _CHARTSOURCE._serialized_end = 522
    _CHART._serialized_start = 524
    _CHART._serialized_end = 583
    _CHARTPOINT._serialized_start = 585
    _CHARTPOINT._serialized_end = 627
    _CHARTSCURRENCIESREQUEST._serialized_start = 629
    _CHARTSCURRENCIESREQUEST._serialized_end = 716
    _CHARTSCURRENCIESRESPONSE._serialized_start = 719
    _CHARTSCURRENCIESRESPONSE._serialized_end = 847
    _CHARTSCURRENCIESRESPONSEDATA._serialized_start = 849
    _CHARTSCURRENCIESRESPONSEDATA._serialized_end = 902