"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ..google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from ..common import analytics_pb2 as common_dot_analytics__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1epublic/analytics_service.proto\x12\x08titanium\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x16common/analytics.proto2\xa8\x07\n\x13AnalyticsController\x12\xac\x01\n\x15FindDataQualityErrors\x12).titanium.GenericChartMetadataDataQuality\x1a1.titanium.GenericChartMetadataDataQualityResponse"5\x82\xd3\xe4\x93\x02/"*/api/v1/analytics/data-quality-errors/find:\x01*\x12\x9b\x01\n\x17GetAllDataQualityErrors\x12\x16.google.protobuf.Empty\x1a1.titanium.GenericChartMetadataDataQualityResponse"5\x82\xd3\xe4\x93\x02/"-/api/v1/analytics/data-quality-errors/get-all\x12\xa3\x01\n\x16FindConsensusAnalytics\x12).titanium.GenericChartMetadataDataQuality\x1a1.titanium.GenericChartMetadataDataQualityResponse"+\x82\xd3\xe4\x93\x02%" /api/v1/analytics/consensus/find:\x01*\x12\x92\x01\n\x18GetAllConsensusAnalytics\x12\x16.google.protobuf.Empty\x1a1.titanium.GenericChartMetadataDataQualityResponse"+\x82\xd3\xe4\x93\x02%"#/api/v1/analytics/consensus/get-all\x12\x92\x01\n\x13GetPredefinedFilter\x12%.titanium.GetPredefinedFiltersRequest\x1a&.titanium.GetPredefinedFiltersResponse",\x82\xd3\xe4\x93\x02&"$/api/v1/analytics/predefined/filters\x12t\n\x0cGetHistogram\x12\x1a.titanium.HistogramRequest\x1a\x1b.titanium.HistogramResponse"+\x82\xd3\xe4\x93\x02%"#/api/v1/analytics/histogram/get-allBz\n com.peernova.titanium.interfacesB\x1eAnalyticsControllerProtoPublicP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/publicb\x06proto3')
_ANALYTICSCONTROLLER = DESCRIPTOR.services_by_name['AnalyticsController']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesB\x1eAnalyticsControllerProtoPublicP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/public'
    _ANALYTICSCONTROLLER.methods_by_name['FindDataQualityErrors']._options = None
    _ANALYTICSCONTROLLER.methods_by_name['FindDataQualityErrors']._serialized_options = b'\x82\xd3\xe4\x93\x02/"*/api/v1/analytics/data-quality-errors/find:\x01*'
    _ANALYTICSCONTROLLER.methods_by_name['GetAllDataQualityErrors']._options = None
    _ANALYTICSCONTROLLER.methods_by_name['GetAllDataQualityErrors']._serialized_options = b'\x82\xd3\xe4\x93\x02/"-/api/v1/analytics/data-quality-errors/get-all'
    _ANALYTICSCONTROLLER.methods_by_name['FindConsensusAnalytics']._options = None
    _ANALYTICSCONTROLLER.methods_by_name['FindConsensusAnalytics']._serialized_options = b'\x82\xd3\xe4\x93\x02%" /api/v1/analytics/consensus/find:\x01*'
    _ANALYTICSCONTROLLER.methods_by_name['GetAllConsensusAnalytics']._options = None
    _ANALYTICSCONTROLLER.methods_by_name['GetAllConsensusAnalytics']._serialized_options = b'\x82\xd3\xe4\x93\x02%"#/api/v1/analytics/consensus/get-all'
    _ANALYTICSCONTROLLER.methods_by_name['GetPredefinedFilter']._options = None
    _ANALYTICSCONTROLLER.methods_by_name['GetPredefinedFilter']._serialized_options = b'\x82\xd3\xe4\x93\x02&"$/api/v1/analytics/predefined/filters'
    _ANALYTICSCONTROLLER.methods_by_name['GetHistogram']._options = None
    _ANALYTICSCONTROLLER.methods_by_name['GetHistogram']._serialized_options = b'\x82\xd3\xe4\x93\x02%"#/api/v1/analytics/histogram/get-all'
    _ANALYTICSCONTROLLER._serialized_start = 128
    _ANALYTICSCONTROLLER._serialized_end = 1064