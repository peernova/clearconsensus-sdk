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
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1epublic/challenge_service.proto\x12\x08titanium\x1a\x1cgoogle/api/annotations.proto\x1a\x19common/gateway_base.proto\x1a\x16common/challenge.proto2\xf5\n\n\x10ChallengeService\x12\x84\x01\n\x11ChallengeFormMeta\x12".titanium.ChallengeFormMetaRequest\x1a#.titanium.ChallengeFormMetaResponse"&\x82\xd3\xe4\x93\x02 "\x1b/api/v1/challenge/form-meta:\x01*\x12{\n\x0fChallengeCreate\x12 .titanium.ChallengeCreateRequest\x1a!.titanium.ChallengeCreateResponse"#\x82\xd3\xe4\x93\x02\x1d"\x18/api/v1/challenge/create:\x01*\x12\x85\x01\n\x15ChallengeFreezeStatus\x12&.titanium.ChallengeFreezeStatusRequest\x1a\x18.titanium.StatusResponse"*\x82\xd3\xe4\x93\x02$"\x1f/api/v1/challenge/freeze/status:\x01*\x12\x88\x01\n\x13GetChallengeDetails\x12$.titanium.GetChallengeDetailsRequest\x1a%.titanium.GetChallengeDetailsResponse"$\x82\xd3\xe4\x93\x02\x1e"\x19/api/v1/challenge-details:\x01*\x12\xa9\x01\n\x1fGetChallengeAttachmentUploadUrl\x12\'.titanium.GetAttachmentUploadUrlRequest\x1a(.titanium.GetAttachmentUploadUrlResponse"3\x82\xd3\xe4\x93\x02-"(/api/v1/challenge/attachment_upload_urls:\x01*\x12\x84\x01\n\x0fChallengeActive\x12 .titanium.ChallengeActiveRequest\x1a!.titanium.ChallengeActiveResponse",\x82\xd3\xe4\x93\x02&"!/api/v1/operator/challenge/active:\x01*\x12|\n\rChallengeList\x12\x1e.titanium.ChallengeListRequest\x1a\x1f.titanium.ChallengeListResponse"*\x82\xd3\xe4\x93\x02$"\x1f/api/v1/operator/challenge/list:\x01*\x12\x88\x01\n\x10ChallengeHistory\x12!.titanium.ChallengeHistoryRequest\x1a".titanium.ChallengeHistoryResponse"-\x82\xd3\xe4\x93\x02\'""/api/v1/operator/challenge/history:\x01*\x12\x82\x01\n\x11ChallengeDecision\x12".titanium.ChallengeDecisionRequest\x1a\x19.titanium.MessageResponse".\x82\xd3\xe4\x93\x02("#/api/v1/operator/challenge/decision:\x01*\x12\x88\x01\n\x15ChallengeFreezeAction\x12&.titanium.ChallengeFreezeActionRequest\x1a\x19.titanium.MessageResponse",\x82\xd3\xe4\x93\x02&"!/api/v1/operator/challenge/freeze:\x01*Bw\n com.peernova.titanium.interfacesB\x1bChallengeServiceProtoPublicP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/publicb\x06proto3')
_CHALLENGESERVICE = DESCRIPTOR.services_by_name['ChallengeService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesB\x1bChallengeServiceProtoPublicP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/public'
    _CHALLENGESERVICE.methods_by_name['ChallengeFormMeta']._options = None
    _CHALLENGESERVICE.methods_by_name['ChallengeFormMeta']._serialized_options = b'\x82\xd3\xe4\x93\x02 "\x1b/api/v1/challenge/form-meta:\x01*'
    _CHALLENGESERVICE.methods_by_name['ChallengeCreate']._options = None
    _CHALLENGESERVICE.methods_by_name['ChallengeCreate']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1d"\x18/api/v1/challenge/create:\x01*'
    _CHALLENGESERVICE.methods_by_name['ChallengeFreezeStatus']._options = None
    _CHALLENGESERVICE.methods_by_name['ChallengeFreezeStatus']._serialized_options = b'\x82\xd3\xe4\x93\x02$"\x1f/api/v1/challenge/freeze/status:\x01*'
    _CHALLENGESERVICE.methods_by_name['GetChallengeDetails']._options = None
    _CHALLENGESERVICE.methods_by_name['GetChallengeDetails']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1e"\x19/api/v1/challenge-details:\x01*'
    _CHALLENGESERVICE.methods_by_name['GetChallengeAttachmentUploadUrl']._options = None
    _CHALLENGESERVICE.methods_by_name['GetChallengeAttachmentUploadUrl']._serialized_options = b'\x82\xd3\xe4\x93\x02-"(/api/v1/challenge/attachment_upload_urls:\x01*'
    _CHALLENGESERVICE.methods_by_name['ChallengeActive']._options = None
    _CHALLENGESERVICE.methods_by_name['ChallengeActive']._serialized_options = b'\x82\xd3\xe4\x93\x02&"!/api/v1/operator/challenge/active:\x01*'
    _CHALLENGESERVICE.methods_by_name['ChallengeList']._options = None
    _CHALLENGESERVICE.methods_by_name['ChallengeList']._serialized_options = b'\x82\xd3\xe4\x93\x02$"\x1f/api/v1/operator/challenge/list:\x01*'
    _CHALLENGESERVICE.methods_by_name['ChallengeHistory']._options = None
    _CHALLENGESERVICE.methods_by_name['ChallengeHistory']._serialized_options = b'\x82\xd3\xe4\x93\x02\'""/api/v1/operator/challenge/history:\x01*'
    _CHALLENGESERVICE.methods_by_name['ChallengeDecision']._options = None
    _CHALLENGESERVICE.methods_by_name['ChallengeDecision']._serialized_options = b'\x82\xd3\xe4\x93\x02("#/api/v1/operator/challenge/decision:\x01*'
    _CHALLENGESERVICE.methods_by_name['ChallengeFreezeAction']._options = None
    _CHALLENGESERVICE.methods_by_name['ChallengeFreezeAction']._serialized_options = b'\x82\xd3\xe4\x93\x02&"!/api/v1/operator/challenge/freeze:\x01*'
    _CHALLENGESERVICE._serialized_start = 126
    _CHALLENGESERVICE._serialized_end = 1523