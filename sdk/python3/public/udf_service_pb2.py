"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ..google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2
from ..common import udf_pb2 as common_dot_udf__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18public/udf_service.proto\x12\x08titanium\x1a\x1cgoogle/api/annotations.proto\x1a\x19common/gateway_base.proto\x1a\x10common/udf.proto2\xae\x02\n\nUdfService\x12Y\n\x08ListUdfs\x12\x15.titanium.ListRequest\x1a\x19.titanium.ListUdfResponse"\x1b\x82\xd3\xe4\x93\x02\x15"\x10/api/v1/udf/list:\x01*\x12b\n\x10GetUdfDefinition\x12\x18.titanium.UdfNameRequest\x1a\x18.titanium.GetUdfResponse"\x1a\x82\xd3\xe4\x93\x02\x14\x12\x12/api/v1/udf/{name}\x12a\n\nDisableUdf\x12\x18.titanium.UdfNameRequest\x1a\x19.titanium.MessageResponse"\x1e\x82\xd3\xe4\x93\x02\x18"\x13/api/v1/udf/disable:\x01*Bi\n com.peernova.titanium.interfacesB\x0fUdfServiceProtoZ4github.com/peernova/clearconsensus-sdk/sdk/go/publicb\x06proto3')
_UDFSERVICE = DESCRIPTOR.services_by_name['UdfService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesB\x0fUdfServiceProtoZ4github.com/peernova/clearconsensus-sdk/sdk/go/public'
    _UDFSERVICE.methods_by_name['ListUdfs']._options = None
    _UDFSERVICE.methods_by_name['ListUdfs']._serialized_options = b'\x82\xd3\xe4\x93\x02\x15"\x10/api/v1/udf/list:\x01*'
    _UDFSERVICE.methods_by_name['GetUdfDefinition']._options = None
    _UDFSERVICE.methods_by_name['GetUdfDefinition']._serialized_options = b'\x82\xd3\xe4\x93\x02\x14\x12\x12/api/v1/udf/{name}'
    _UDFSERVICE.methods_by_name['DisableUdf']._options = None
    _UDFSERVICE.methods_by_name['DisableUdf']._serialized_options = b'\x82\xd3\xe4\x93\x02\x18"\x13/api/v1/udf/disable:\x01*'
    _UDFSERVICE._serialized_start = 114
    _UDFSERVICE._serialized_end = 416