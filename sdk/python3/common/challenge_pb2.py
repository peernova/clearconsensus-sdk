"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16common/challenge.proto\x12\x08titanium\x1a\x1cgoogle/protobuf/struct.proto\x1a\x19common/gateway_base.proto"\x86\x01\n\x18ChallengeFormMetaRequest\x12\x10\n\x08asset_id\x18\x01 \x01(\t\x12-\n\revidence_type\x18\x02 \x01(\x0e2\x16.titanium.EvidenceType\x12\x15\n\rsubmission_id\x18\x03 \x01(\t\x12\x12\n\ntrace_name\x18\x04 \x01(\t"\x82\x01\n\x19ChallengeFormMetaResponse\x127\n\x04data\x18\x01 \x01(\x0b2\'.titanium.ChallengeFormMetaResponseDataH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"\x8b\x01\n\x1dChallengeFormMetaResponseData\x12/\n\x04rows\x18\x01 \x03(\x0b2!.titanium.ChallengeFormGeneralRow\x129\n\rone_of_fields\x18\x02 \x03(\x0b2".titanium.ChallengeFormOneOfFields")\n\x18ChallengeFormOneOfFields\x12\r\n\x05names\x18\x01 \x03(\t"\xa2\x03\n\x17ChallengeFormGeneralRow\x12\r\n\x05field\x18\x01 \x01(\t\x12\x0f\n\x07tooltip\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12=\n\tprecision\x18\x04 \x01(\x0b2*.titanium.ChallengeFormGeneralRowPrecision\x121\n\x03max\x18\x05 \x01(\x0b2$.titanium.ChallengeFormGeneralRowMax\x121\n\x03min\x18\x06 \x01(\x0b2$.titanium.ChallengeFormGeneralRowMin\x12\r\n\x05regex\x18\x07 \x01(\t\x12>\n\nmax_length\x18\x08 \x01(\x0b2*.titanium.ChallengeFormGeneralRowMaxLength\x12>\n\nmin_length\x18\t \x01(\x0b2*.titanium.ChallengeFormGeneralRowMinLength\x12%\n\x05value\x18\n \x01(\x0b2\x16.google.protobuf.Value"1\n ChallengeFormGeneralRowPrecision\x12\r\n\x05value\x18\x01 \x01(\x05"+\n\x1aChallengeFormGeneralRowMax\x12\r\n\x05value\x18\x01 \x01(\x01"+\n\x1aChallengeFormGeneralRowMin\x12\r\n\x05value\x18\x01 \x01(\x01"1\n ChallengeFormGeneralRowMaxLength\x12\r\n\x05value\x18\x01 \x01(\x05"1\n ChallengeFormGeneralRowMinLength\x12\r\n\x05value\x18\x01 \x01(\x05"\x9f\x02\n\x16ChallengeCreateRequest\x12\x10\n\x08asset_id\x18\x01 \x01(\t\x12-\n\revidence_type\x18\x02 \x01(\x0e2\x16.titanium.EvidenceType\x12\x16\n\x0esubmitted_date\x18\x03 \x01(\t\x12\x14\n\x0csubmitted_id\x18\x04 \x01(\t\x12\x15\n\rsubmitted_url\x18\x05 \x01(\t\x12\x0c\n\x04date\x18\x06 \x01(\t\x12\x0c\n\x04time\x18\x07 \x01(\t\x12\x16\n\x0egeneral_fields\x18\x08 \x03(\t\x12\x0c\n\x04note\x18\t \x01(\t\x12)\n\x0battachments\x18\n \x03(\x0b2\x14.titanium.Attachment\x12\x12\n\ntrace_name\x18\x0b \x01(\t"~\n\x17ChallengeCreateResponse\x125\n\x04data\x18\x01 \x01(\x0b2%.titanium.ChallengeCreateResponseDataH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"0\n\x1bChallengeCreateResponseData\x12\x11\n\tticket_id\x18\x01 \x01(\t"8\n\x1cChallengeFreezeStatusRequest\x12\x18\n\x10consensus_run_id\x18\x01 \x01(\t"i\n\x1cChallengeFreezeActionRequest\x12\x18\n\x10consensus_run_id\x18\x01 \x01(\t\x12/\n\x06action\x18\x02 \x01(\x0e2\x1f.titanium.ChallengeFreezeAction"\xa2\x01\n\x16ChallengeActiveRequest\x12\x10\n\x08asset_id\x18\x01 \x01(\t\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12"\n\x07orderBy\x18\x03 \x01(\x0b2\x11.titanium.OrderBy\x12\x1e\n\x05limit\x18\x04 \x01(\x0b2\x0f.titanium.Limit\x12\x0e\n\x06offset\x18\x05 \x01(\x05\x12\x12\n\ntrace_name\x18\x06 \x01(\t"~\n\x17ChallengeActiveResponse\x125\n\x04data\x18\x01 \x01(\x0b2%.titanium.ChallengeActiveResponseDataH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"\x8c\x01\n\x1bChallengeActiveResponseData\x12%\n\x07columns\x18\x01 \x03(\x0b2\x14.titanium.ColumnInfo\x122\n\x04rows\x18\x02 \x03(\x0b2$.titanium.ChallengeConsensusMetadata\x12\x12\n\ntotal_rows\x18\x03 \x01(\x05"E\n\x1aChallengeConsensusMetadata\x12\'\n\nchallenges\x18\x03 \x03(\x0b2\x13.titanium.ValuesRow"\x80\x01\n\x18ChallengeHistoryResponse\x126\n\x04data\x18\x01 \x01(\x0b2&.titanium.ChallengeHistoryResponseDataH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"|\n\x1cChallengeHistoryResponseData\x12%\n\x07columns\x18\x01 \x03(\x0b2\x14.titanium.ColumnInfo\x12!\n\x04rows\x18\x02 \x03(\x0b2\x13.titanium.ValuesRow\x12\x12\n\ntotal_rows\x18\x03 \x01(\x05"h\n\x18ChallengeDecisionRequest\x12\x10\n\x08asset_id\x18\x01 \x01(\t\x12\x14\n\x0cchallenge_id\x18\x02 \x01(\t\x12$\n\x08decision\x18\x03 \x01(\x0e2\x12.titanium.Decision"\xa3\x01\n\x17ChallengeHistoryRequest\x12\x10\n\x08asset_id\x18\x01 \x01(\t\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12"\n\x07orderBy\x18\x03 \x01(\x0b2\x11.titanium.OrderBy\x12\x1e\n\x05limit\x18\x04 \x01(\x0b2\x0f.titanium.Limit\x12\x0e\n\x06offset\x18\x05 \x01(\x05\x12\x12\n\ntrace_name\x18\x06 \x01(\t"\xe2\x01\n\x14ChallengeListRequest\x12\x10\n\x08asset_id\x18\x01 \x01(\t\x12\x1f\n\x17consensus_run_timestamp\x18\x02 \x01(\t\x12\x11\n\tsnap_time\x18\x03 \x01(\t\x12\x0c\n\x04date\x18\x04 \x01(\t\x12\x0e\n\x06filter\x18\x05 \x01(\t\x12"\n\x07orderBy\x18\x06 \x01(\x0b2\x11.titanium.OrderBy\x12\x1e\n\x05limit\x18\x07 \x01(\x0b2\x0f.titanium.Limit\x12\x0e\n\x06offset\x18\x08 \x01(\x05\x12\x12\n\ntrace_name\x18\t \x01(\t"z\n\x15ChallengeListResponse\x123\n\x04data\x18\x01 \x01(\x0b2#.titanium.ChallengeListResponseDataH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"\x8b\x01\n\x19ChallengeListResponseData\x12%\n\x07columns\x18\x01 \x03(\x0b2\x14.titanium.ColumnInfo\x123\n\nchallenges\x18\x02 \x03(\x0b2\x1f.titanium.ChallengeListMetadata\x12\x12\n\ntotal_rows\x18\x03 \x01(\x05"?\n\x15ChallengeListMetadata\x12&\n\x06values\x18\x01 \x03(\x0b2\x16.google.protobuf.Value"Z\n\x1dGetAttachmentUploadUrlRequest\x12\x10\n\x08asset_id\x18\x01 \x01(\t\x12\x14\n\x0csubmitted_id\x18\x02 \x01(\t\x12\x11\n\tfile_name\x18\x03 \x01(\t"\xf1\x01\n\x1eGetAttachmentUploadUrlResponse\x12L\n\x04data\x18\x01 \x01(\x0b2<.titanium.GetAttachmentUploadUrlResponse.AttachmentUploadUrlH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00\x1aS\n\x13AttachmentUploadUrl\x12\x12\n\nupload_url\x18\x01 \x01(\t\x12\x15\n\rattachment_id\x18\x02 \x01(\t\x12\x11\n\tfile_name\x18\x03 \x01(\tB\n\n\x08response">\n\nAttachment\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\rattachment_id\x18\x02 \x01(\t\x12\x0b\n\x03url\x18\x03 \x01(\t"\x8b\x01\n\x1aGetChallengeDetailsRequest\x12\x10\n\x08asset_id\x18\x01 \x01(\t\x12\x16\n\x0esubmitted_date\x18\x02 \x01(\t\x12\x15\n\rsubmission_id\x18\x03 \x01(\t\x12\x12\n\ntrace_name\x18\x04 \x01(\t\x12\x18\n\x10consensus_run_id\x18\x05 \x01(\t"\xfa\x04\n\x1bGetChallengeDetailsResponse\x12<\n\x04data\x18\x01 \x01(\x0b2,.titanium.GetChallengeDetailsResponse.ResultH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00\x1a\xa4\x03\n\x06Result\x12W\n\x0echallenge_data\x18\x01 \x03(\x0b2?.titanium.GetChallengeDetailsResponse.Result.ChallengeDataEntry\x12X\n\x15common_challenge_data\x18\x02 \x01(\x0b29.titanium.GetChallengeDetailsResponse.CommonChallengeData\x12)\n\x0battachments\x18\x03 \x03(\x0b2\x14.titanium.Attachment\x12R\n\x0btotalNumber\x18\x04 \x03(\x0b2=.titanium.GetChallengeDetailsResponse.Result.TotalNumberEntry\x1a4\n\x12ChallengeDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a2\n\x10TotalNumberEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x028\x01\x1aH\n\x13CommonChallengeData\x12\x0c\n\x04date\x18\x01 \x01(\t\x12\x0c\n\x04time\x18\x02 \x01(\t\x12\x15\n\revidence_type\x18\x03 \x01(\tB\n\n\x08response*\x89\x01\n\x15ChallengeFreezeAction\x12\'\n#CHALLENGE_FREEZE_ACTION_UNSPECIFIED\x10\x00\x12"\n\x1eCHALLENGE_FREEZE_ACTION_ENABLE\x10\x01\x12#\n\x1fCHALLENGE_FREEZE_ACTION_DISABLE\x10\x02*C\n\x0cEvidenceType\x12\x1d\n\x19EVIDENCE_TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05TRADE\x10\x01\x12\t\n\x05ORDER\x10\x02Bw\n com.peernova.titanium.interfacesB\x1bChallengeServiceProtoCommonP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/commonb\x06proto3')
_CHALLENGEFREEZEACTION = DESCRIPTOR.enum_types_by_name['ChallengeFreezeAction']
ChallengeFreezeAction = enum_type_wrapper.EnumTypeWrapper(_CHALLENGEFREEZEACTION)
_EVIDENCETYPE = DESCRIPTOR.enum_types_by_name['EvidenceType']
EvidenceType = enum_type_wrapper.EnumTypeWrapper(_EVIDENCETYPE)
CHALLENGE_FREEZE_ACTION_UNSPECIFIED = 0
CHALLENGE_FREEZE_ACTION_ENABLE = 1
CHALLENGE_FREEZE_ACTION_DISABLE = 2
EVIDENCE_TYPE_UNSPECIFIED = 0
TRADE = 1
ORDER = 2
_CHALLENGEFORMMETAREQUEST = DESCRIPTOR.message_types_by_name['ChallengeFormMetaRequest']
_CHALLENGEFORMMETARESPONSE = DESCRIPTOR.message_types_by_name['ChallengeFormMetaResponse']
_CHALLENGEFORMMETARESPONSEDATA = DESCRIPTOR.message_types_by_name['ChallengeFormMetaResponseData']
_CHALLENGEFORMONEOFFIELDS = DESCRIPTOR.message_types_by_name['ChallengeFormOneOfFields']
_CHALLENGEFORMGENERALROW = DESCRIPTOR.message_types_by_name['ChallengeFormGeneralRow']
_CHALLENGEFORMGENERALROWPRECISION = DESCRIPTOR.message_types_by_name['ChallengeFormGeneralRowPrecision']
_CHALLENGEFORMGENERALROWMAX = DESCRIPTOR.message_types_by_name['ChallengeFormGeneralRowMax']
_CHALLENGEFORMGENERALROWMIN = DESCRIPTOR.message_types_by_name['ChallengeFormGeneralRowMin']
_CHALLENGEFORMGENERALROWMAXLENGTH = DESCRIPTOR.message_types_by_name['ChallengeFormGeneralRowMaxLength']
_CHALLENGEFORMGENERALROWMINLENGTH = DESCRIPTOR.message_types_by_name['ChallengeFormGeneralRowMinLength']
_CHALLENGECREATEREQUEST = DESCRIPTOR.message_types_by_name['ChallengeCreateRequest']
_CHALLENGECREATERESPONSE = DESCRIPTOR.message_types_by_name['ChallengeCreateResponse']
_CHALLENGECREATERESPONSEDATA = DESCRIPTOR.message_types_by_name['ChallengeCreateResponseData']
_CHALLENGEFREEZESTATUSREQUEST = DESCRIPTOR.message_types_by_name['ChallengeFreezeStatusRequest']
_CHALLENGEFREEZEACTIONREQUEST = DESCRIPTOR.message_types_by_name['ChallengeFreezeActionRequest']
_CHALLENGEACTIVEREQUEST = DESCRIPTOR.message_types_by_name['ChallengeActiveRequest']
_CHALLENGEACTIVERESPONSE = DESCRIPTOR.message_types_by_name['ChallengeActiveResponse']
_CHALLENGEACTIVERESPONSEDATA = DESCRIPTOR.message_types_by_name['ChallengeActiveResponseData']
_CHALLENGECONSENSUSMETADATA = DESCRIPTOR.message_types_by_name['ChallengeConsensusMetadata']
_CHALLENGEHISTORYRESPONSE = DESCRIPTOR.message_types_by_name['ChallengeHistoryResponse']
_CHALLENGEHISTORYRESPONSEDATA = DESCRIPTOR.message_types_by_name['ChallengeHistoryResponseData']
_CHALLENGEDECISIONREQUEST = DESCRIPTOR.message_types_by_name['ChallengeDecisionRequest']
_CHALLENGEHISTORYREQUEST = DESCRIPTOR.message_types_by_name['ChallengeHistoryRequest']
_CHALLENGELISTREQUEST = DESCRIPTOR.message_types_by_name['ChallengeListRequest']
_CHALLENGELISTRESPONSE = DESCRIPTOR.message_types_by_name['ChallengeListResponse']
_CHALLENGELISTRESPONSEDATA = DESCRIPTOR.message_types_by_name['ChallengeListResponseData']
_CHALLENGELISTMETADATA = DESCRIPTOR.message_types_by_name['ChallengeListMetadata']
_GETATTACHMENTUPLOADURLREQUEST = DESCRIPTOR.message_types_by_name['GetAttachmentUploadUrlRequest']
_GETATTACHMENTUPLOADURLRESPONSE = DESCRIPTOR.message_types_by_name['GetAttachmentUploadUrlResponse']
_GETATTACHMENTUPLOADURLRESPONSE_ATTACHMENTUPLOADURL = _GETATTACHMENTUPLOADURLRESPONSE.nested_types_by_name['AttachmentUploadUrl']
_ATTACHMENT = DESCRIPTOR.message_types_by_name['Attachment']
_GETCHALLENGEDETAILSREQUEST = DESCRIPTOR.message_types_by_name['GetChallengeDetailsRequest']
_GETCHALLENGEDETAILSRESPONSE = DESCRIPTOR.message_types_by_name['GetChallengeDetailsResponse']
_GETCHALLENGEDETAILSRESPONSE_RESULT = _GETCHALLENGEDETAILSRESPONSE.nested_types_by_name['Result']
_GETCHALLENGEDETAILSRESPONSE_RESULT_CHALLENGEDATAENTRY = _GETCHALLENGEDETAILSRESPONSE_RESULT.nested_types_by_name['ChallengeDataEntry']
_GETCHALLENGEDETAILSRESPONSE_RESULT_TOTALNUMBERENTRY = _GETCHALLENGEDETAILSRESPONSE_RESULT.nested_types_by_name['TotalNumberEntry']
_GETCHALLENGEDETAILSRESPONSE_COMMONCHALLENGEDATA = _GETCHALLENGEDETAILSRESPONSE.nested_types_by_name['CommonChallengeData']
ChallengeFormMetaRequest = _reflection.GeneratedProtocolMessageType('ChallengeFormMetaRequest', (_message.Message,), {'DESCRIPTOR': _CHALLENGEFORMMETAREQUEST, '__module__': 'common.challenge_pb2'})
_sym_db.RegisterMessage(ChallengeFormMetaRequest)
ChallengeFormMetaResponse = _reflection.GeneratedProtocolMessageType('ChallengeFormMetaResponse', (_message.Message,), {'DESCRIPTOR': _CHALLENGEFORMMETARESPONSE, '__module__': 'common.challenge_pb2'})
_sym_db.RegisterMessage(ChallengeFormMetaResponse)
ChallengeFormMetaResponseData = _reflection.GeneratedProtocolMessageType('ChallengeFormMetaResponseData', (_message.Message,), {'DESCRIPTOR': _CHALLENGEFORMMETARESPONSEDATA, '__module__': 'common.challenge_pb2'})
_sym_db.RegisterMessage(ChallengeFormMetaResponseData)
ChallengeFormOneOfFields = _reflection.GeneratedProtocolMessageType('ChallengeFormOneOfFields', (_message.Message,), {'DESCRIPTOR': _CHALLENGEFORMONEOFFIELDS, '__module__': 'common.challenge_pb2'})
_sym_db.RegisterMessage(ChallengeFormOneOfFields)
ChallengeFormGeneralRow = _reflection.GeneratedProtocolMessageType('ChallengeFormGeneralRow', (_message.Message,), {'DESCRIPTOR': _CHALLENGEFORMGENERALROW, '__module__': 'common.challenge_pb2'})
_sym_db.RegisterMessage(ChallengeFormGeneralRow)
ChallengeFormGeneralRowPrecision = _reflection.GeneratedProtocolMessageType('ChallengeFormGeneralRowPrecision', (_message.Message,), {'DESCRIPTOR': _CHALLENGEFORMGENERALROWPRECISION, '__module__': 'common.challenge_pb2'})
_sym_db.RegisterMessage(ChallengeFormGeneralRowPrecision)
ChallengeFormGeneralRowMax = _reflection.GeneratedProtocolMessageType('ChallengeFormGeneralRowMax', (_message.Message,), {'DESCRIPTOR': _CHALLENGEFORMGENERALROWMAX, '__module__': 'common.challenge_pb2'})
_sym_db.RegisterMessage(ChallengeFormGeneralRowMax)
ChallengeFormGeneralRowMin = _reflection.GeneratedProtocolMessageType('ChallengeFormGeneralRowMin', (_message.Message,), {'DESCRIPTOR': _CHALLENGEFORMGENERALROWMIN, '__module__': 'common.challenge_pb2'})
_sym_db.RegisterMessage(ChallengeFormGeneralRowMin)
ChallengeFormGeneralRowMaxLength = _reflection.GeneratedProtocolMessageType('ChallengeFormGeneralRowMaxLength', (_message.Message,), {'DESCRIPTOR': _CHALLENGEFORMGENERALROWMAXLENGTH, '__module__': 'common.challenge_pb2'})
_sym_db.RegisterMessage(ChallengeFormGeneralRowMaxLength)
ChallengeFormGeneralRowMinLength = _reflection.GeneratedProtocolMessageType('ChallengeFormGeneralRowMinLength', (_message.Message,), {'DESCRIPTOR': _CHALLENGEFORMGENERALROWMINLENGTH, '__module__': 'common.challenge_pb2'})
_sym_db.RegisterMessage(ChallengeFormGeneralRowMinLength)
ChallengeCreateRequest = _reflection.GeneratedProtocolMessageType('ChallengeCreateRequest', (_message.Message,), {'DESCRIPTOR': _CHALLENGECREATEREQUEST, '__module__': 'common.challenge_pb2'})
_sym_db.RegisterMessage(ChallengeCreateRequest)
ChallengeCreateResponse = _reflection.GeneratedProtocolMessageType('ChallengeCreateResponse', (_message.Message,), {'DESCRIPTOR': _CHALLENGECREATERESPONSE, '__module__': 'common.challenge_pb2'})
_sym_db.RegisterMessage(ChallengeCreateResponse)
ChallengeCreateResponseData = _reflection.GeneratedProtocolMessageType('ChallengeCreateResponseData', (_message.Message,), {'DESCRIPTOR': _CHALLENGECREATERESPONSEDATA, '__module__': 'common.challenge_pb2'})
_sym_db.RegisterMessage(ChallengeCreateResponseData)
ChallengeFreezeStatusRequest = _reflection.GeneratedProtocolMessageType('ChallengeFreezeStatusRequest', (_message.Message,), {'DESCRIPTOR': _CHALLENGEFREEZESTATUSREQUEST, '__module__': 'common.challenge_pb2'})
_sym_db.RegisterMessage(ChallengeFreezeStatusRequest)
ChallengeFreezeActionRequest = _reflection.GeneratedProtocolMessageType('ChallengeFreezeActionRequest', (_message.Message,), {'DESCRIPTOR': _CHALLENGEFREEZEACTIONREQUEST, '__module__': 'common.challenge_pb2'})
_sym_db.RegisterMessage(ChallengeFreezeActionRequest)
ChallengeActiveRequest = _reflection.GeneratedProtocolMessageType('ChallengeActiveRequest', (_message.Message,), {'DESCRIPTOR': _CHALLENGEACTIVEREQUEST, '__module__': 'common.challenge_pb2'})
_sym_db.RegisterMessage(ChallengeActiveRequest)
ChallengeActiveResponse = _reflection.GeneratedProtocolMessageType('ChallengeActiveResponse', (_message.Message,), {'DESCRIPTOR': _CHALLENGEACTIVERESPONSE, '__module__': 'common.challenge_pb2'})
_sym_db.RegisterMessage(ChallengeActiveResponse)
ChallengeActiveResponseData = _reflection.GeneratedProtocolMessageType('ChallengeActiveResponseData', (_message.Message,), {'DESCRIPTOR': _CHALLENGEACTIVERESPONSEDATA, '__module__': 'common.challenge_pb2'})
_sym_db.RegisterMessage(ChallengeActiveResponseData)
ChallengeConsensusMetadata = _reflection.GeneratedProtocolMessageType('ChallengeConsensusMetadata', (_message.Message,), {'DESCRIPTOR': _CHALLENGECONSENSUSMETADATA, '__module__': 'common.challenge_pb2'})
_sym_db.RegisterMessage(ChallengeConsensusMetadata)
ChallengeHistoryResponse = _reflection.GeneratedProtocolMessageType('ChallengeHistoryResponse', (_message.Message,), {'DESCRIPTOR': _CHALLENGEHISTORYRESPONSE, '__module__': 'common.challenge_pb2'})
_sym_db.RegisterMessage(ChallengeHistoryResponse)
ChallengeHistoryResponseData = _reflection.GeneratedProtocolMessageType('ChallengeHistoryResponseData', (_message.Message,), {'DESCRIPTOR': _CHALLENGEHISTORYRESPONSEDATA, '__module__': 'common.challenge_pb2'})
_sym_db.RegisterMessage(ChallengeHistoryResponseData)
ChallengeDecisionRequest = _reflection.GeneratedProtocolMessageType('ChallengeDecisionRequest', (_message.Message,), {'DESCRIPTOR': _CHALLENGEDECISIONREQUEST, '__module__': 'common.challenge_pb2'})
_sym_db.RegisterMessage(ChallengeDecisionRequest)
ChallengeHistoryRequest = _reflection.GeneratedProtocolMessageType('ChallengeHistoryRequest', (_message.Message,), {'DESCRIPTOR': _CHALLENGEHISTORYREQUEST, '__module__': 'common.challenge_pb2'})
_sym_db.RegisterMessage(ChallengeHistoryRequest)
ChallengeListRequest = _reflection.GeneratedProtocolMessageType('ChallengeListRequest', (_message.Message,), {'DESCRIPTOR': _CHALLENGELISTREQUEST, '__module__': 'common.challenge_pb2'})
_sym_db.RegisterMessage(ChallengeListRequest)
ChallengeListResponse = _reflection.GeneratedProtocolMessageType('ChallengeListResponse', (_message.Message,), {'DESCRIPTOR': _CHALLENGELISTRESPONSE, '__module__': 'common.challenge_pb2'})
_sym_db.RegisterMessage(ChallengeListResponse)
ChallengeListResponseData = _reflection.GeneratedProtocolMessageType('ChallengeListResponseData', (_message.Message,), {'DESCRIPTOR': _CHALLENGELISTRESPONSEDATA, '__module__': 'common.challenge_pb2'})
_sym_db.RegisterMessage(ChallengeListResponseData)
ChallengeListMetadata = _reflection.GeneratedProtocolMessageType('ChallengeListMetadata', (_message.Message,), {'DESCRIPTOR': _CHALLENGELISTMETADATA, '__module__': 'common.challenge_pb2'})
_sym_db.RegisterMessage(ChallengeListMetadata)
GetAttachmentUploadUrlRequest = _reflection.GeneratedProtocolMessageType('GetAttachmentUploadUrlRequest', (_message.Message,), {'DESCRIPTOR': _GETATTACHMENTUPLOADURLREQUEST, '__module__': 'common.challenge_pb2'})
_sym_db.RegisterMessage(GetAttachmentUploadUrlRequest)
GetAttachmentUploadUrlResponse = _reflection.GeneratedProtocolMessageType('GetAttachmentUploadUrlResponse', (_message.Message,), {'AttachmentUploadUrl': _reflection.GeneratedProtocolMessageType('AttachmentUploadUrl', (_message.Message,), {'DESCRIPTOR': _GETATTACHMENTUPLOADURLRESPONSE_ATTACHMENTUPLOADURL, '__module__': 'common.challenge_pb2'}), 'DESCRIPTOR': _GETATTACHMENTUPLOADURLRESPONSE, '__module__': 'common.challenge_pb2'})
_sym_db.RegisterMessage(GetAttachmentUploadUrlResponse)
_sym_db.RegisterMessage(GetAttachmentUploadUrlResponse.AttachmentUploadUrl)
Attachment = _reflection.GeneratedProtocolMessageType('Attachment', (_message.Message,), {'DESCRIPTOR': _ATTACHMENT, '__module__': 'common.challenge_pb2'})
_sym_db.RegisterMessage(Attachment)
GetChallengeDetailsRequest = _reflection.GeneratedProtocolMessageType('GetChallengeDetailsRequest', (_message.Message,), {'DESCRIPTOR': _GETCHALLENGEDETAILSREQUEST, '__module__': 'common.challenge_pb2'})
_sym_db.RegisterMessage(GetChallengeDetailsRequest)
GetChallengeDetailsResponse = _reflection.GeneratedProtocolMessageType('GetChallengeDetailsResponse', (_message.Message,), {'Result': _reflection.GeneratedProtocolMessageType('Result', (_message.Message,), {'ChallengeDataEntry': _reflection.GeneratedProtocolMessageType('ChallengeDataEntry', (_message.Message,), {'DESCRIPTOR': _GETCHALLENGEDETAILSRESPONSE_RESULT_CHALLENGEDATAENTRY, '__module__': 'common.challenge_pb2'}), 'TotalNumberEntry': _reflection.GeneratedProtocolMessageType('TotalNumberEntry', (_message.Message,), {'DESCRIPTOR': _GETCHALLENGEDETAILSRESPONSE_RESULT_TOTALNUMBERENTRY, '__module__': 'common.challenge_pb2'}), 'DESCRIPTOR': _GETCHALLENGEDETAILSRESPONSE_RESULT, '__module__': 'common.challenge_pb2'}), 'CommonChallengeData': _reflection.GeneratedProtocolMessageType('CommonChallengeData', (_message.Message,), {'DESCRIPTOR': _GETCHALLENGEDETAILSRESPONSE_COMMONCHALLENGEDATA, '__module__': 'common.challenge_pb2'}), 'DESCRIPTOR': _GETCHALLENGEDETAILSRESPONSE, '__module__': 'common.challenge_pb2'})
_sym_db.RegisterMessage(GetChallengeDetailsResponse)
_sym_db.RegisterMessage(GetChallengeDetailsResponse.Result)
_sym_db.RegisterMessage(GetChallengeDetailsResponse.Result.ChallengeDataEntry)
_sym_db.RegisterMessage(GetChallengeDetailsResponse.Result.TotalNumberEntry)
_sym_db.RegisterMessage(GetChallengeDetailsResponse.CommonChallengeData)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesB\x1bChallengeServiceProtoCommonP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/common'
    _GETCHALLENGEDETAILSRESPONSE_RESULT_CHALLENGEDATAENTRY._options = None
    _GETCHALLENGEDETAILSRESPONSE_RESULT_CHALLENGEDATAENTRY._serialized_options = b'8\x01'
    _GETCHALLENGEDETAILSRESPONSE_RESULT_TOTALNUMBERENTRY._options = None
    _GETCHALLENGEDETAILSRESPONSE_RESULT_TOTALNUMBERENTRY._serialized_options = b'8\x01'
    _CHALLENGEFREEZEACTION._serialized_start = 4621
    _CHALLENGEFREEZEACTION._serialized_end = 4758
    _EVIDENCETYPE._serialized_start = 4760
    _EVIDENCETYPE._serialized_end = 4827
    _CHALLENGEFORMMETAREQUEST._serialized_start = 94
    _CHALLENGEFORMMETAREQUEST._serialized_end = 228
    _CHALLENGEFORMMETARESPONSE._serialized_start = 231
    _CHALLENGEFORMMETARESPONSE._serialized_end = 361
    _CHALLENGEFORMMETARESPONSEDATA._serialized_start = 364
    _CHALLENGEFORMMETARESPONSEDATA._serialized_end = 503
    _CHALLENGEFORMONEOFFIELDS._serialized_start = 505
    _CHALLENGEFORMONEOFFIELDS._serialized_end = 546
    _CHALLENGEFORMGENERALROW._serialized_start = 549
    _CHALLENGEFORMGENERALROW._serialized_end = 967
    _CHALLENGEFORMGENERALROWPRECISION._serialized_start = 969
    _CHALLENGEFORMGENERALROWPRECISION._serialized_end = 1018
    _CHALLENGEFORMGENERALROWMAX._serialized_start = 1020
    _CHALLENGEFORMGENERALROWMAX._serialized_end = 1063
    _CHALLENGEFORMGENERALROWMIN._serialized_start = 1065
    _CHALLENGEFORMGENERALROWMIN._serialized_end = 1108
    _CHALLENGEFORMGENERALROWMAXLENGTH._serialized_start = 1110
    _CHALLENGEFORMGENERALROWMAXLENGTH._serialized_end = 1159
    _CHALLENGEFORMGENERALROWMINLENGTH._serialized_start = 1161
    _CHALLENGEFORMGENERALROWMINLENGTH._serialized_end = 1210
    _CHALLENGECREATEREQUEST._serialized_start = 1213
    _CHALLENGECREATEREQUEST._serialized_end = 1500
    _CHALLENGECREATERESPONSE._serialized_start = 1502
    _CHALLENGECREATERESPONSE._serialized_end = 1628
    _CHALLENGECREATERESPONSEDATA._serialized_start = 1630
    _CHALLENGECREATERESPONSEDATA._serialized_end = 1678
    _CHALLENGEFREEZESTATUSREQUEST._serialized_start = 1680
    _CHALLENGEFREEZESTATUSREQUEST._serialized_end = 1736
    _CHALLENGEFREEZEACTIONREQUEST._serialized_start = 1738
    _CHALLENGEFREEZEACTIONREQUEST._serialized_end = 1843
    _CHALLENGEACTIVEREQUEST._serialized_start = 1846
    _CHALLENGEACTIVEREQUEST._serialized_end = 2008
    _CHALLENGEACTIVERESPONSE._serialized_start = 2010
    _CHALLENGEACTIVERESPONSE._serialized_end = 2136
    _CHALLENGEACTIVERESPONSEDATA._serialized_start = 2139
    _CHALLENGEACTIVERESPONSEDATA._serialized_end = 2279
    _CHALLENGECONSENSUSMETADATA._serialized_start = 2281
    _CHALLENGECONSENSUSMETADATA._serialized_end = 2350
    _CHALLENGEHISTORYRESPONSE._serialized_start = 2353
    _CHALLENGEHISTORYRESPONSE._serialized_end = 2481
    _CHALLENGEHISTORYRESPONSEDATA._serialized_start = 2483
    _CHALLENGEHISTORYRESPONSEDATA._serialized_end = 2607
    _CHALLENGEDECISIONREQUEST._serialized_start = 2609
    _CHALLENGEDECISIONREQUEST._serialized_end = 2713
    _CHALLENGEHISTORYREQUEST._serialized_start = 2716
    _CHALLENGEHISTORYREQUEST._serialized_end = 2879
    _CHALLENGELISTREQUEST._serialized_start = 2882
    _CHALLENGELISTREQUEST._serialized_end = 3108
    _CHALLENGELISTRESPONSE._serialized_start = 3110
    _CHALLENGELISTRESPONSE._serialized_end = 3232
    _CHALLENGELISTRESPONSEDATA._serialized_start = 3235
    _CHALLENGELISTRESPONSEDATA._serialized_end = 3374
    _CHALLENGELISTMETADATA._serialized_start = 3376
    _CHALLENGELISTMETADATA._serialized_end = 3439
    _GETATTACHMENTUPLOADURLREQUEST._serialized_start = 3441
    _GETATTACHMENTUPLOADURLREQUEST._serialized_end = 3531
    _GETATTACHMENTUPLOADURLRESPONSE._serialized_start = 3534
    _GETATTACHMENTUPLOADURLRESPONSE._serialized_end = 3775
    _GETATTACHMENTUPLOADURLRESPONSE_ATTACHMENTUPLOADURL._serialized_start = 3680
    _GETATTACHMENTUPLOADURLRESPONSE_ATTACHMENTUPLOADURL._serialized_end = 3763
    _ATTACHMENT._serialized_start = 3777
    _ATTACHMENT._serialized_end = 3839
    _GETCHALLENGEDETAILSREQUEST._serialized_start = 3842
    _GETCHALLENGEDETAILSREQUEST._serialized_end = 3981
    _GETCHALLENGEDETAILSRESPONSE._serialized_start = 3984
    _GETCHALLENGEDETAILSRESPONSE._serialized_end = 4618
    _GETCHALLENGEDETAILSRESPONSE_RESULT._serialized_start = 4112
    _GETCHALLENGEDETAILSRESPONSE_RESULT._serialized_end = 4532
    _GETCHALLENGEDETAILSRESPONSE_RESULT_CHALLENGEDATAENTRY._serialized_start = 4428
    _GETCHALLENGEDETAILSRESPONSE_RESULT_CHALLENGEDATAENTRY._serialized_end = 4480
    _GETCHALLENGEDETAILSRESPONSE_RESULT_TOTALNUMBERENTRY._serialized_start = 4482
    _GETCHALLENGEDETAILSRESPONSE_RESULT_TOTALNUMBERENTRY._serialized_end = 4532
    _GETCHALLENGEDETAILSRESPONSE_COMMONCHALLENGEDATA._serialized_start = 4534
    _GETCHALLENGEDETAILSRESPONSE_COMMONCHALLENGEDATA._serialized_end = 4606