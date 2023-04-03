"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ..google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ..common import data_proccesing_app_pb2 as common_dot_data__proccesing__app__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(public/data_proccesing_app_service.proto\x12\x08titanium\x1a\x1cgoogle/api/annotations.proto\x1a common/data_proccesing_app.proto2\xac\x01\n\x18DataProcessingAppService\x12\x8f\x01\n\x14RunDataProcessingApp\x12%.titanium.RunDataProcessingAppRequest\x1a&.titanium.RunDataProcessingAppResponse"(\x82\xd3\xe4\x93\x02""\x1d/api/v1/dataprocessingapp/run:\x01*B\x7f\n com.peernova.titanium.interfacesB#DataProcessingAppServiceProtoPublicP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/publicb\x06proto3')
_DATAPROCESSINGAPPSERVICE = DESCRIPTOR.services_by_name['DataProcessingAppService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesB#DataProcessingAppServiceProtoPublicP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/public'
    _DATAPROCESSINGAPPSERVICE.methods_by_name['RunDataProcessingApp']._options = None
    _DATAPROCESSINGAPPSERVICE.methods_by_name['RunDataProcessingApp']._serialized_options = b'\x82\xd3\xe4\x93\x02""\x1d/api/v1/dataprocessingapp/run:\x01*'
    _DATAPROCESSINGAPPSERVICE._serialized_start = 119
    _DATAPROCESSINGAPPSERVICE._serialized_end = 291