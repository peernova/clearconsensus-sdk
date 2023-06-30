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
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bprivate/admin_service.proto\x12\x08titanium\x1a\x1cgoogle/api/annotations.proto\x1a\x19common/gateway_base.proto\x1a\x13common/assets.proto"p\n\x13RunConsensusRequest\x12\x10\n\x08asset_id\x18\x01 \x01(\t\x12\x0f\n\x07clients\x18\x02 \x03(\t\x12\r\n\x05dates\x18\x03 \x03(\t\x12\x13\n\x0bdescription\x18\x05 \x01(\t\x12\x12\n\ntrace_name\x18\x06 \x01(\t"\x82\x01\n\x0eOnBoardRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\x0e\n\x06client\x18\x03 \x01(\t\x12\x12\n\npublic_key\x18\x04 \x01(\t\x12(\n\nauthorized\x18\x05 \x01(\x0b2\x14.titanium.AssetsList"\x8f\x01\n\x14RunCalculatorRequest\x12\x10\n\x08asset_id\x18\x01 \x01(\t\x12\x0f\n\x07clients\x18\x02 \x03(\t\x12\r\n\x05dates\x18\x03 \x03(\t\x12\x1c\n\x14consensus_run_reason\x18\x04 \x01(\t\x12\x13\n\x0bdescription\x18\x05 \x01(\t\x12\x12\n\ntrace_name\x18\x06 \x01(\t"r\n\x1bUploadEvaluatedPriceRequest\x12\x10\n\x08asset_id\x18\x01 \x01(\t\x12\x0c\n\x04date\x18\x02 \x01(\t\x12\x11\n\tfile_name\x18\x03 \x01(\t\x12\x0c\n\x04file\x18\x04 \x01(\t\x12\x12\n\ntrace_name\x18\x05 \x01(\t2\xcb\x03\n\x0cAdminService\x12Z\n\x07OnBoard\x12\x18.titanium.OnBoardRequest\x1a\x19.titanium.MessageResponse"\x1a\x82\xd3\xe4\x93\x02\x14"\x0f/api/v1/onboard:\x01*\x12m\n\rRunCalculator\x12\x1e.titanium.RunCalculatorRequest\x1a\x19.titanium.MessageResponse"!\x82\xd3\xe4\x93\x02\x1b"\x16/api/v1/calculator/run:\x01*\x12\x83\x01\n\x14UploadEvaluatedPrice\x12%.titanium.UploadEvaluatedPriceRequest\x1a\x19.titanium.MessageResponse")\x82\xd3\xe4\x93\x02#"\x1e/api/v1/upload/evaluated-price:\x01*\x12j\n\x0cRunConsensus\x12\x1d.titanium.RunConsensusRequest\x1a\x19.titanium.MessageResponse" \x82\xd3\xe4\x93\x02\x1a"\x15/api/v1/consensus/run:\x01*Bu\n com.peernova.titanium.interfacesB\x18AdminServiceProtoPrivateP\x01Z5github.com/peernova/clearconsensus-sdk/sdk/go/privateb\x06proto3')
_RUNCONSENSUSREQUEST = DESCRIPTOR.message_types_by_name['RunConsensusRequest']
_ONBOARDREQUEST = DESCRIPTOR.message_types_by_name['OnBoardRequest']
_RUNCALCULATORREQUEST = DESCRIPTOR.message_types_by_name['RunCalculatorRequest']
_UPLOADEVALUATEDPRICEREQUEST = DESCRIPTOR.message_types_by_name['UploadEvaluatedPriceRequest']
RunConsensusRequest = _reflection.GeneratedProtocolMessageType('RunConsensusRequest', (_message.Message,), {'DESCRIPTOR': _RUNCONSENSUSREQUEST, '__module__': 'private.admin_service_pb2'})
_sym_db.RegisterMessage(RunConsensusRequest)
OnBoardRequest = _reflection.GeneratedProtocolMessageType('OnBoardRequest', (_message.Message,), {'DESCRIPTOR': _ONBOARDREQUEST, '__module__': 'private.admin_service_pb2'})
_sym_db.RegisterMessage(OnBoardRequest)
RunCalculatorRequest = _reflection.GeneratedProtocolMessageType('RunCalculatorRequest', (_message.Message,), {'DESCRIPTOR': _RUNCALCULATORREQUEST, '__module__': 'private.admin_service_pb2'})
_sym_db.RegisterMessage(RunCalculatorRequest)
UploadEvaluatedPriceRequest = _reflection.GeneratedProtocolMessageType('UploadEvaluatedPriceRequest', (_message.Message,), {'DESCRIPTOR': _UPLOADEVALUATEDPRICEREQUEST, '__module__': 'private.admin_service_pb2'})
_sym_db.RegisterMessage(UploadEvaluatedPriceRequest)
_ADMINSERVICE = DESCRIPTOR.services_by_name['AdminService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesB\x18AdminServiceProtoPrivateP\x01Z5github.com/peernova/clearconsensus-sdk/sdk/go/private'
    _ADMINSERVICE.methods_by_name['OnBoard']._options = None
    _ADMINSERVICE.methods_by_name['OnBoard']._serialized_options = b'\x82\xd3\xe4\x93\x02\x14"\x0f/api/v1/onboard:\x01*'
    _ADMINSERVICE.methods_by_name['RunCalculator']._options = None
    _ADMINSERVICE.methods_by_name['RunCalculator']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1b"\x16/api/v1/calculator/run:\x01*'
    _ADMINSERVICE.methods_by_name['UploadEvaluatedPrice']._options = None
    _ADMINSERVICE.methods_by_name['UploadEvaluatedPrice']._serialized_options = b'\x82\xd3\xe4\x93\x02#"\x1e/api/v1/upload/evaluated-price:\x01*'
    _ADMINSERVICE.methods_by_name['RunConsensus']._options = None
    _ADMINSERVICE.methods_by_name['RunConsensus']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1a"\x15/api/v1/consensus/run:\x01*'
    _RUNCONSENSUSREQUEST._serialized_start = 119
    _RUNCONSENSUSREQUEST._serialized_end = 231
    _ONBOARDREQUEST._serialized_start = 234
    _ONBOARDREQUEST._serialized_end = 364
    _RUNCALCULATORREQUEST._serialized_start = 367
    _RUNCALCULATORREQUEST._serialized_end = 510
    _UPLOADEVALUATEDPRICEREQUEST._serialized_start = 512
    _UPLOADEVALUATEDPRICEREQUEST._serialized_end = 626
    _ADMINSERVICE._serialized_start = 629
    _ADMINSERVICE._serialized_end = 1088