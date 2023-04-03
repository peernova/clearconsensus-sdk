"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ..google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2
from ..common import consensus_pb2 as common_dot_consensus__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'private/consensus_private_service.proto\x12\x08titanium\x1a\x1cgoogle/api/annotations.proto\x1a\x19common/gateway_base.proto\x1a\x16common/consensus.proto2\xc5\x05\n\x17ConsensusServicePrivate\x12\x84\x01\n\x0fConsensusActive\x12 .titanium.ConsensusActiveRequest\x1a!.titanium.ConsensusActiveResponse",\x82\xd3\xe4\x93\x02&"!/api/v1/operator/consensus/active:\x01*\x12\x91\x01\n\x12ConsensusToPublish\x12#.titanium.ConsensusToPublishRequest\x1a$.titanium.ConsensusToPublishResponse"0\x82\xd3\xe4\x93\x02*"%/api/v1/operator/consensus/to-publish:\x01*\x12\x7f\n\x10ConsensusPublish\x12!.titanium.ConsensusPublishRequest\x1a\x19.titanium.MessageResponse"-\x82\xd3\xe4\x93\x02\'""/api/v1/operator/consensus/publish:\x01*\x12\x88\x01\n\x10ConsensusHistory\x12!.titanium.ConsensusHistoryRequest\x1a".titanium.ConsensusHistoryResponse"-\x82\xd3\xe4\x93\x02\'""/api/v1/operator/consensus/history:\x01*\x12\x82\x01\n\x11ConsensusDecision\x12".titanium.ConsensusDecisionRequest\x1a\x19.titanium.MessageResponse".\x82\xd3\xe4\x93\x02("#/api/v1/operator/consensus/decision:\x01*B\x80\x01\n com.peernova.titanium.interfacesB#ConsensusServiceServiceProtoPrivateP\x01Z5github.com/peernova/clearconsensus-sdk/sdk/go/privateb\x06proto3')
_CONSENSUSSERVICEPRIVATE = DESCRIPTOR.services_by_name['ConsensusServicePrivate']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesB#ConsensusServiceServiceProtoPrivateP\x01Z5github.com/peernova/clearconsensus-sdk/sdk/go/private'
    _CONSENSUSSERVICEPRIVATE.methods_by_name['ConsensusActive']._options = None
    _CONSENSUSSERVICEPRIVATE.methods_by_name['ConsensusActive']._serialized_options = b'\x82\xd3\xe4\x93\x02&"!/api/v1/operator/consensus/active:\x01*'
    _CONSENSUSSERVICEPRIVATE.methods_by_name['ConsensusToPublish']._options = None
    _CONSENSUSSERVICEPRIVATE.methods_by_name['ConsensusToPublish']._serialized_options = b'\x82\xd3\xe4\x93\x02*"%/api/v1/operator/consensus/to-publish:\x01*'
    _CONSENSUSSERVICEPRIVATE.methods_by_name['ConsensusPublish']._options = None
    _CONSENSUSSERVICEPRIVATE.methods_by_name['ConsensusPublish']._serialized_options = b'\x82\xd3\xe4\x93\x02\'""/api/v1/operator/consensus/publish:\x01*'
    _CONSENSUSSERVICEPRIVATE.methods_by_name['ConsensusHistory']._options = None
    _CONSENSUSSERVICEPRIVATE.methods_by_name['ConsensusHistory']._serialized_options = b'\x82\xd3\xe4\x93\x02\'""/api/v1/operator/consensus/history:\x01*'
    _CONSENSUSSERVICEPRIVATE.methods_by_name['ConsensusDecision']._options = None
    _CONSENSUSSERVICEPRIVATE.methods_by_name['ConsensusDecision']._serialized_options = b'\x82\xd3\xe4\x93\x02("#/api/v1/operator/consensus/decision:\x01*'
    _CONSENSUSSERVICEPRIVATE._serialized_start = 135
    _CONSENSUSSERVICEPRIVATE._serialized_end = 844