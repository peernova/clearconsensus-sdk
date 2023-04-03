"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n common/data_proccesing_app.proto\x12\x08titanium\x1a\x19common/gateway_base.proto"\xe0\x01\n\x1bRunDataProcessingAppRequest\x12\r\n\x05asset\x18\x01 \x01(\t\x12\x17\n\x0finstrument_type\x18\x02 \x01(\t\x12\x0f\n\x07service\x18\x03 \x01(\t\x12\x0c\n\x04date\x18\x04 \x01(\t\x12\x11\n\tsnap_time\x18\x05 \x01(\t\x12\x11\n\tfile_name\x18\x06 \x01(\t\x12\x13\n\x0bmapper_rule\x18\x07 \x01(\t\x12\x17\n\x0fvalidation_rule\x18\x08 \x01(\t\x12\x17\n\x0fdescriptor_name\x18\t \x01(\t\x12\r\n\x05input\x18\n \x01(\t"\\\n\x1cRunDataProcessingAppResponse\x12\x0e\n\x04data\x18\x01 \x01(\tH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08responseB\x7f\n com.peernova.titanium.interfacesB#DataProcessingAppServiceProtoCommonP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/commonb\x06proto3')
_RUNDATAPROCESSINGAPPREQUEST = DESCRIPTOR.message_types_by_name['RunDataProcessingAppRequest']
_RUNDATAPROCESSINGAPPRESPONSE = DESCRIPTOR.message_types_by_name['RunDataProcessingAppResponse']
RunDataProcessingAppRequest = _reflection.GeneratedProtocolMessageType('RunDataProcessingAppRequest', (_message.Message,), {'DESCRIPTOR': _RUNDATAPROCESSINGAPPREQUEST, '__module__': 'common.data_proccesing_app_pb2'})
_sym_db.RegisterMessage(RunDataProcessingAppRequest)
RunDataProcessingAppResponse = _reflection.GeneratedProtocolMessageType('RunDataProcessingAppResponse', (_message.Message,), {'DESCRIPTOR': _RUNDATAPROCESSINGAPPRESPONSE, '__module__': 'common.data_proccesing_app_pb2'})
_sym_db.RegisterMessage(RunDataProcessingAppResponse)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesB#DataProcessingAppServiceProtoCommonP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/common'
    _RUNDATAPROCESSINGAPPREQUEST._serialized_start = 74
    _RUNDATAPROCESSINGAPPREQUEST._serialized_end = 298
    _RUNDATAPROCESSINGAPPRESPONSE._serialized_start = 300
    _RUNDATAPROCESSINGAPPRESPONSE._serialized_end = 392