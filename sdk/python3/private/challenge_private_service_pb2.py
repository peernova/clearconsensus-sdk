"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ..google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2
from ..common import challenge_pb2 as common_dot_challenge__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'private/challenge_private_service.proto\x12\x08titanium\x1a\x1cgoogle/api/annotations.proto\x1a\x19common/gateway_base.proto\x1a\x16common/challenge.proto2\xb9\x05\n\x17ChallengePrivateService\x12\x84\x01\n\x0fChallengeActive\x12 .titanium.ChallengeActiveRequest\x1a!.titanium.ChallengeActiveResponse",\x82\xd3\xe4\x93\x02&"!/api/v1/operator/challenge/active:\x01*\x12|\n\rChallengeList\x12\x1e.titanium.ChallengeListRequest\x1a\x1f.titanium.ChallengeListResponse"*\x82\xd3\xe4\x93\x02$"\x1f/api/v1/operator/challenge/list:\x01*\x12\x88\x01\n\x10ChallengeHistory\x12!.titanium.ChallengeHistoryRequest\x1a".titanium.ChallengeHistoryResponse"-\x82\xd3\xe4\x93\x02\'""/api/v1/operator/challenge/history:\x01*\x12\x82\x01\n\x11ChallengeDecision\x12".titanium.ChallengeDecisionRequest\x1a\x19.titanium.MessageResponse".\x82\xd3\xe4\x93\x02("#/api/v1/operator/challenge/decision:\x01*\x12\x88\x01\n\x15ChallengeFreezeAction\x12&.titanium.ChallengeFreezeActionRequest\x1a\x19.titanium.MessageResponse",\x82\xd3\xe4\x93\x02&"!/api/v1/operator/challenge/freeze:\x01*By\n com.peernova.titanium.interfacesB\x1cChallengeServiceProtoPrivateP\x01Z5github.com/peernova/clearconsensus-sdk/sdk/go/privateb\x06proto3')
_CHALLENGEPRIVATESERVICE = DESCRIPTOR.services_by_name['ChallengePrivateService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesB\x1cChallengeServiceProtoPrivateP\x01Z5github.com/peernova/clearconsensus-sdk/sdk/go/private'
    _CHALLENGEPRIVATESERVICE.methods_by_name['ChallengeActive']._options = None
    _CHALLENGEPRIVATESERVICE.methods_by_name['ChallengeActive']._serialized_options = b'\x82\xd3\xe4\x93\x02&"!/api/v1/operator/challenge/active:\x01*'
    _CHALLENGEPRIVATESERVICE.methods_by_name['ChallengeList']._options = None
    _CHALLENGEPRIVATESERVICE.methods_by_name['ChallengeList']._serialized_options = b'\x82\xd3\xe4\x93\x02$"\x1f/api/v1/operator/challenge/list:\x01*'
    _CHALLENGEPRIVATESERVICE.methods_by_name['ChallengeHistory']._options = None
    _CHALLENGEPRIVATESERVICE.methods_by_name['ChallengeHistory']._serialized_options = b'\x82\xd3\xe4\x93\x02\'""/api/v1/operator/challenge/history:\x01*'
    _CHALLENGEPRIVATESERVICE.methods_by_name['ChallengeDecision']._options = None
    _CHALLENGEPRIVATESERVICE.methods_by_name['ChallengeDecision']._serialized_options = b'\x82\xd3\xe4\x93\x02("#/api/v1/operator/challenge/decision:\x01*'
    _CHALLENGEPRIVATESERVICE.methods_by_name['ChallengeFreezeAction']._options = None
    _CHALLENGEPRIVATESERVICE.methods_by_name['ChallengeFreezeAction']._serialized_options = b'\x82\xd3\xe4\x93\x02&"!/api/v1/operator/challenge/freeze:\x01*'
    _CHALLENGEPRIVATESERVICE._serialized_start = 135
    _CHALLENGEPRIVATESERVICE._serialized_end = 832