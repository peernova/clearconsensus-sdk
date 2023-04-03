"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16common/consensus.proto\x12\x08titanium\x1a\x19common/gateway_base.proto"|\n\x16ConsensusActiveRequest\x12\x0e\n\x06filter\x18\x01 \x01(\t\x12"\n\x07orderBy\x18\x02 \x01(\x0b2\x11.titanium.OrderBy\x12\x1e\n\x05limit\x18\x03 \x01(\x0b2\x0f.titanium.Limit\x12\x0e\n\x06offset\x18\x04 \x01(\x05"\x7f\n\x19ConsensusToPublishRequest\x12\x0e\n\x06filter\x18\x01 \x01(\t\x12"\n\x07orderBy\x18\x02 \x01(\x0b2\x11.titanium.OrderBy\x12\x1e\n\x05limit\x18\x03 \x01(\x0b2\x0f.titanium.Limit\x12\x0e\n\x06offset\x18\x04 \x01(\x05"\x84\x01\n\x1aConsensusToPublishResponse\x128\n\x04data\x18\x01 \x01(\x0b2(.titanium.ConsensusToPublishResponseDataH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"~\n\x1eConsensusToPublishResponseData\x12%\n\x07columns\x18\x01 \x03(\x0b2\x14.titanium.ColumnInfo\x12!\n\x04rows\x18\x02 \x03(\x0b2\x13.titanium.ValuesRow\x12\x12\n\ntotal_rows\x18\x03 \x01(\x05"^\n\x17ConsensusPublishRequest\x12\x1d\n\x15consensus_tracking_id\x18\x01 \x01(\t\x12\x10\n\x08asset_id\x18\x02 \x01(\t\x12\x12\n\ntrace_name\x18\x03 \x01(\t"}\n\x17ConsensusHistoryRequest\x12\x0e\n\x06filter\x18\x01 \x01(\t\x12"\n\x07orderBy\x18\x02 \x01(\x0b2\x11.titanium.OrderBy\x12\x1e\n\x05limit\x18\x03 \x01(\x0b2\x0f.titanium.Limit\x12\x0e\n\x06offset\x18\x04 \x01(\x05"\x80\x01\n\x18ConsensusHistoryResponse\x126\n\x04data\x18\x01 \x01(\x0b2&.titanium.ConsensusHistoryResponseDataH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"|\n\x1cConsensusHistoryResponseData\x12%\n\x07columns\x18\x01 \x03(\x0b2\x14.titanium.ColumnInfo\x12!\n\x04rows\x18\x02 \x03(\x0b2\x13.titanium.ValuesRow\x12\x12\n\ntotal_rows\x18\x03 \x01(\x05"_\n\x18ConsensusDecisionRequest\x12\x1d\n\x15consensus_tracking_id\x18\x01 \x01(\t\x12$\n\x08decision\x18\x02 \x01(\x0e2\x12.titanium.Decision"B\n\x1aConsensusTimestampsRequest\x12\x10\n\x08asset_id\x18\x01 \x01(\t\x12\x12\n\ntrace_name\x18\x02 \x01(\t"\x86\x01\n\x1bConsensusTimestampsResponse\x129\n\x04data\x18\x01 \x01(\x0b2).titanium.ConsensusTimestampsResponseDataH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"W\n\x1fConsensusTimestampsResponseData\x124\n\ntimestamps\x18\x01 \x03(\x0b2 .titanium.ConsensusTimestampMeta"R\n\x16ConsensusTimestampMeta\x12\x1f\n\x17consensus_run_timestamp\x18\x01 \x01(\t\x12\x17\n\x0fsubmitted_dates\x18\x02 \x03(\t"\xd5\x01\n\x10ConsensusRequest\x12\x10\n\x08asset_id\x18\x01 \x01(\t\x12\x16\n\x0esubmitted_date\x18\x02 \x01(\t\x12\x1f\n\x17consensus_run_timestamp\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12"\n\x07orderBy\x18\x05 \x01(\x0b2\x11.titanium.OrderBy\x12\x1e\n\x05limit\x18\x06 \x01(\x0b2\x0f.titanium.Limit\x12\x0e\n\x06offset\x18\x07 \x01(\x05\x12\x12\n\ntrace_name\x18\x08 \x01(\t"r\n\x11ConsensusResponse\x12/\n\x04data\x18\x01 \x01(\x0b2\x1f.titanium.ConsensusResponseDataH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"u\n\x15ConsensusResponseData\x12%\n\x07columns\x18\x01 \x03(\x0b2\x14.titanium.ColumnInfo\x12!\n\x04rows\x18\x02 \x03(\x0b2\x13.titanium.ValuesRow\x12\x12\n\ntotal_rows\x18\x03 \x01(\x05"\xe2\x01\n\x17GetConsensusRunsRequest\x12\x10\n\x08asset_id\x18\x01 \x01(\t\x12\x12\n\ntrace_name\x18\x02 \x01(\t\x12\x16\n\x0esnap_date_from\x18\x03 \x01(\t\x12\x14\n\x0csnap_date_to\x18\x04 \x01(\t\x12\x13\n\x0bparticipant\x18\x05 \x01(\t\x12\x15\n\rshow_archived\x18\x06 \x01(\x08\x12)\n\x0bfilter_pack\x18\x07 \x01(\x0b2\x14.titanium.FilterPack\x12\x1c\n\x04page\x18\x08 \x01(\x0b2\x0e.titanium.Page"x\n\x18GetConsensusRunsResponse\x12 \n\x05error\x18\x01 \x01(\x0b2\x0f.titanium.ErrorH\x00\x12.\n\x04data\x18\x02 \x01(\x0b2\x1e.titanium.GetConsensusRunsDataH\x00B\n\n\x08response"~\n\x14GetConsensusRunsData\x12%\n\x07columns\x18\x01 \x03(\x0b2\x14.titanium.ColumnInfo\x12!\n\x04rows\x18\x02 \x03(\x0b2\x13.titanium.ValuesRow\x12\x1c\n\x04page\x18\x03 \x01(\x0b2\x0e.titanium.Page"\xef\x02\n\x12ConsensusResultSet\x12\x18\n\x10consensus_run_id\x18\x01 \x01(\t\x12\x1f\n\x17consensus_result_set_id\x18\x02 \x01(\t\x12\x1c\n\x14submission_timestamp\x18\x03 \x01(\t\x12\x1c\n\x14consensus_run_status\x18\x04 \x01(\t\x12\x13\n\x0bcohort_name\x18\x05 \x01(\t\x12\x14\n\x0cdata_content\x18\x06 \x01(\t\x12\x1f\n\x17consensus_run_timestamp\x18\x07 \x01(\t\x12\x14\n\x0cparticipants\x18\x08 \x03(\t\x12\x13\n\x0bparticipant\x18\t \x01(\t\x12\x0e\n\x06status\x18\n \x01(\t\x12\x17\n\x0fconsensus_notes\x18\x0b \x01(\t\x12"\n\x1aconsensus_result_set_label\x18\x0c \x01(\t\x12\x0e\n\x06run_by\x18\r \x01(\t\x12\x0e\n\x06job_id\x18\x0e \x01(\t"\xc4\x02\n\x1fConsensusResultSetValuesRequest\x12\x10\n\x08asset_id\x18\x01 \x01(\t\x12\x12\n\ntrace_name\x18\x02 \x01(\t\x12\x14\n\x0csubmitted_id\x18\x03 \x01(\t\x12\x16\n\x0esubmitted_date\x18\x04 \x01(\t\x12\x1f\n\x17consensus_result_set_id\x18\x05 \x01(\t\x12\x1f\n\x17consensus_run_timestamp\x18\x06 \x01(\t\x12\x0e\n\x06client\x18\x07 \x01(\t\x12\x0e\n\x06filter\x18\x08 \x01(\t\x12)\n\x0bfilter_pack\x18\t \x01(\x0b2\x14.titanium.FilterPack\x12"\n\x07orderBy\x18\n \x01(\x0b2\x11.titanium.OrderBy\x12\x1c\n\x04page\x18\x0b \x01(\x0b2\x0e.titanium.Page"\x84\x01\n ConsensusResultSetValuesResponse\x122\n\x04data\x18\x01 \x01(\x0b2".titanium.ConsensusResultSetValuesH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"\x82\x01\n\x18ConsensusResultSetValues\x12%\n\x07columns\x18\x01 \x03(\x0b2\x14.titanium.ColumnInfo\x12!\n\x04rows\x18\x02 \x03(\x0b2\x13.titanium.ValuesRow\x12\x1c\n\x04page\x18\x03 \x01(\x0b2\x0e.titanium.PageBw\n com.peernova.titanium.interfacesB\x1bConsensusServiceProtoCommonP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/commonb\x06proto3')
_CONSENSUSACTIVEREQUEST = DESCRIPTOR.message_types_by_name['ConsensusActiveRequest']
_CONSENSUSTOPUBLISHREQUEST = DESCRIPTOR.message_types_by_name['ConsensusToPublishRequest']
_CONSENSUSTOPUBLISHRESPONSE = DESCRIPTOR.message_types_by_name['ConsensusToPublishResponse']
_CONSENSUSTOPUBLISHRESPONSEDATA = DESCRIPTOR.message_types_by_name['ConsensusToPublishResponseData']
_CONSENSUSPUBLISHREQUEST = DESCRIPTOR.message_types_by_name['ConsensusPublishRequest']
_CONSENSUSHISTORYREQUEST = DESCRIPTOR.message_types_by_name['ConsensusHistoryRequest']
_CONSENSUSHISTORYRESPONSE = DESCRIPTOR.message_types_by_name['ConsensusHistoryResponse']
_CONSENSUSHISTORYRESPONSEDATA = DESCRIPTOR.message_types_by_name['ConsensusHistoryResponseData']
_CONSENSUSDECISIONREQUEST = DESCRIPTOR.message_types_by_name['ConsensusDecisionRequest']
_CONSENSUSTIMESTAMPSREQUEST = DESCRIPTOR.message_types_by_name['ConsensusTimestampsRequest']
_CONSENSUSTIMESTAMPSRESPONSE = DESCRIPTOR.message_types_by_name['ConsensusTimestampsResponse']
_CONSENSUSTIMESTAMPSRESPONSEDATA = DESCRIPTOR.message_types_by_name['ConsensusTimestampsResponseData']
_CONSENSUSTIMESTAMPMETA = DESCRIPTOR.message_types_by_name['ConsensusTimestampMeta']
_CONSENSUSREQUEST = DESCRIPTOR.message_types_by_name['ConsensusRequest']
_CONSENSUSRESPONSE = DESCRIPTOR.message_types_by_name['ConsensusResponse']
_CONSENSUSRESPONSEDATA = DESCRIPTOR.message_types_by_name['ConsensusResponseData']
_GETCONSENSUSRUNSREQUEST = DESCRIPTOR.message_types_by_name['GetConsensusRunsRequest']
_GETCONSENSUSRUNSRESPONSE = DESCRIPTOR.message_types_by_name['GetConsensusRunsResponse']
_GETCONSENSUSRUNSDATA = DESCRIPTOR.message_types_by_name['GetConsensusRunsData']
_CONSENSUSRESULTSET = DESCRIPTOR.message_types_by_name['ConsensusResultSet']
_CONSENSUSRESULTSETVALUESREQUEST = DESCRIPTOR.message_types_by_name['ConsensusResultSetValuesRequest']
_CONSENSUSRESULTSETVALUESRESPONSE = DESCRIPTOR.message_types_by_name['ConsensusResultSetValuesResponse']
_CONSENSUSRESULTSETVALUES = DESCRIPTOR.message_types_by_name['ConsensusResultSetValues']
ConsensusActiveRequest = _reflection.GeneratedProtocolMessageType('ConsensusActiveRequest', (_message.Message,), {'DESCRIPTOR': _CONSENSUSACTIVEREQUEST, '__module__': 'common.consensus_pb2'})
_sym_db.RegisterMessage(ConsensusActiveRequest)
ConsensusToPublishRequest = _reflection.GeneratedProtocolMessageType('ConsensusToPublishRequest', (_message.Message,), {'DESCRIPTOR': _CONSENSUSTOPUBLISHREQUEST, '__module__': 'common.consensus_pb2'})
_sym_db.RegisterMessage(ConsensusToPublishRequest)
ConsensusToPublishResponse = _reflection.GeneratedProtocolMessageType('ConsensusToPublishResponse', (_message.Message,), {'DESCRIPTOR': _CONSENSUSTOPUBLISHRESPONSE, '__module__': 'common.consensus_pb2'})
_sym_db.RegisterMessage(ConsensusToPublishResponse)
ConsensusToPublishResponseData = _reflection.GeneratedProtocolMessageType('ConsensusToPublishResponseData', (_message.Message,), {'DESCRIPTOR': _CONSENSUSTOPUBLISHRESPONSEDATA, '__module__': 'common.consensus_pb2'})
_sym_db.RegisterMessage(ConsensusToPublishResponseData)
ConsensusPublishRequest = _reflection.GeneratedProtocolMessageType('ConsensusPublishRequest', (_message.Message,), {'DESCRIPTOR': _CONSENSUSPUBLISHREQUEST, '__module__': 'common.consensus_pb2'})
_sym_db.RegisterMessage(ConsensusPublishRequest)
ConsensusHistoryRequest = _reflection.GeneratedProtocolMessageType('ConsensusHistoryRequest', (_message.Message,), {'DESCRIPTOR': _CONSENSUSHISTORYREQUEST, '__module__': 'common.consensus_pb2'})
_sym_db.RegisterMessage(ConsensusHistoryRequest)
ConsensusHistoryResponse = _reflection.GeneratedProtocolMessageType('ConsensusHistoryResponse', (_message.Message,), {'DESCRIPTOR': _CONSENSUSHISTORYRESPONSE, '__module__': 'common.consensus_pb2'})
_sym_db.RegisterMessage(ConsensusHistoryResponse)
ConsensusHistoryResponseData = _reflection.GeneratedProtocolMessageType('ConsensusHistoryResponseData', (_message.Message,), {'DESCRIPTOR': _CONSENSUSHISTORYRESPONSEDATA, '__module__': 'common.consensus_pb2'})
_sym_db.RegisterMessage(ConsensusHistoryResponseData)
ConsensusDecisionRequest = _reflection.GeneratedProtocolMessageType('ConsensusDecisionRequest', (_message.Message,), {'DESCRIPTOR': _CONSENSUSDECISIONREQUEST, '__module__': 'common.consensus_pb2'})
_sym_db.RegisterMessage(ConsensusDecisionRequest)
ConsensusTimestampsRequest = _reflection.GeneratedProtocolMessageType('ConsensusTimestampsRequest', (_message.Message,), {'DESCRIPTOR': _CONSENSUSTIMESTAMPSREQUEST, '__module__': 'common.consensus_pb2'})
_sym_db.RegisterMessage(ConsensusTimestampsRequest)
ConsensusTimestampsResponse = _reflection.GeneratedProtocolMessageType('ConsensusTimestampsResponse', (_message.Message,), {'DESCRIPTOR': _CONSENSUSTIMESTAMPSRESPONSE, '__module__': 'common.consensus_pb2'})
_sym_db.RegisterMessage(ConsensusTimestampsResponse)
ConsensusTimestampsResponseData = _reflection.GeneratedProtocolMessageType('ConsensusTimestampsResponseData', (_message.Message,), {'DESCRIPTOR': _CONSENSUSTIMESTAMPSRESPONSEDATA, '__module__': 'common.consensus_pb2'})
_sym_db.RegisterMessage(ConsensusTimestampsResponseData)
ConsensusTimestampMeta = _reflection.GeneratedProtocolMessageType('ConsensusTimestampMeta', (_message.Message,), {'DESCRIPTOR': _CONSENSUSTIMESTAMPMETA, '__module__': 'common.consensus_pb2'})
_sym_db.RegisterMessage(ConsensusTimestampMeta)
ConsensusRequest = _reflection.GeneratedProtocolMessageType('ConsensusRequest', (_message.Message,), {'DESCRIPTOR': _CONSENSUSREQUEST, '__module__': 'common.consensus_pb2'})
_sym_db.RegisterMessage(ConsensusRequest)
ConsensusResponse = _reflection.GeneratedProtocolMessageType('ConsensusResponse', (_message.Message,), {'DESCRIPTOR': _CONSENSUSRESPONSE, '__module__': 'common.consensus_pb2'})
_sym_db.RegisterMessage(ConsensusResponse)
ConsensusResponseData = _reflection.GeneratedProtocolMessageType('ConsensusResponseData', (_message.Message,), {'DESCRIPTOR': _CONSENSUSRESPONSEDATA, '__module__': 'common.consensus_pb2'})
_sym_db.RegisterMessage(ConsensusResponseData)
GetConsensusRunsRequest = _reflection.GeneratedProtocolMessageType('GetConsensusRunsRequest', (_message.Message,), {'DESCRIPTOR': _GETCONSENSUSRUNSREQUEST, '__module__': 'common.consensus_pb2'})
_sym_db.RegisterMessage(GetConsensusRunsRequest)
GetConsensusRunsResponse = _reflection.GeneratedProtocolMessageType('GetConsensusRunsResponse', (_message.Message,), {'DESCRIPTOR': _GETCONSENSUSRUNSRESPONSE, '__module__': 'common.consensus_pb2'})
_sym_db.RegisterMessage(GetConsensusRunsResponse)
GetConsensusRunsData = _reflection.GeneratedProtocolMessageType('GetConsensusRunsData', (_message.Message,), {'DESCRIPTOR': _GETCONSENSUSRUNSDATA, '__module__': 'common.consensus_pb2'})
_sym_db.RegisterMessage(GetConsensusRunsData)
ConsensusResultSet = _reflection.GeneratedProtocolMessageType('ConsensusResultSet', (_message.Message,), {'DESCRIPTOR': _CONSENSUSRESULTSET, '__module__': 'common.consensus_pb2'})
_sym_db.RegisterMessage(ConsensusResultSet)
ConsensusResultSetValuesRequest = _reflection.GeneratedProtocolMessageType('ConsensusResultSetValuesRequest', (_message.Message,), {'DESCRIPTOR': _CONSENSUSRESULTSETVALUESREQUEST, '__module__': 'common.consensus_pb2'})
_sym_db.RegisterMessage(ConsensusResultSetValuesRequest)
ConsensusResultSetValuesResponse = _reflection.GeneratedProtocolMessageType('ConsensusResultSetValuesResponse', (_message.Message,), {'DESCRIPTOR': _CONSENSUSRESULTSETVALUESRESPONSE, '__module__': 'common.consensus_pb2'})
_sym_db.RegisterMessage(ConsensusResultSetValuesResponse)
ConsensusResultSetValues = _reflection.GeneratedProtocolMessageType('ConsensusResultSetValues', (_message.Message,), {'DESCRIPTOR': _CONSENSUSRESULTSETVALUES, '__module__': 'common.consensus_pb2'})
_sym_db.RegisterMessage(ConsensusResultSetValues)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesB\x1bConsensusServiceProtoCommonP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/common'
    _CONSENSUSACTIVEREQUEST._serialized_start = 63
    _CONSENSUSACTIVEREQUEST._serialized_end = 187
    _CONSENSUSTOPUBLISHREQUEST._serialized_start = 189
    _CONSENSUSTOPUBLISHREQUEST._serialized_end = 316
    _CONSENSUSTOPUBLISHRESPONSE._serialized_start = 319
    _CONSENSUSTOPUBLISHRESPONSE._serialized_end = 451
    _CONSENSUSTOPUBLISHRESPONSEDATA._serialized_start = 453
    _CONSENSUSTOPUBLISHRESPONSEDATA._serialized_end = 579
    _CONSENSUSPUBLISHREQUEST._serialized_start = 581
    _CONSENSUSPUBLISHREQUEST._serialized_end = 675
    _CONSENSUSHISTORYREQUEST._serialized_start = 677
    _CONSENSUSHISTORYREQUEST._serialized_end = 802
    _CONSENSUSHISTORYRESPONSE._serialized_start = 805
    _CONSENSUSHISTORYRESPONSE._serialized_end = 933
    _CONSENSUSHISTORYRESPONSEDATA._serialized_start = 935
    _CONSENSUSHISTORYRESPONSEDATA._serialized_end = 1059
    _CONSENSUSDECISIONREQUEST._serialized_start = 1061
    _CONSENSUSDECISIONREQUEST._serialized_end = 1156
    _CONSENSUSTIMESTAMPSREQUEST._serialized_start = 1158
    _CONSENSUSTIMESTAMPSREQUEST._serialized_end = 1224
    _CONSENSUSTIMESTAMPSRESPONSE._serialized_start = 1227
    _CONSENSUSTIMESTAMPSRESPONSE._serialized_end = 1361
    _CONSENSUSTIMESTAMPSRESPONSEDATA._serialized_start = 1363
    _CONSENSUSTIMESTAMPSRESPONSEDATA._serialized_end = 1450
    _CONSENSUSTIMESTAMPMETA._serialized_start = 1452
    _CONSENSUSTIMESTAMPMETA._serialized_end = 1534
    _CONSENSUSREQUEST._serialized_start = 1537
    _CONSENSUSREQUEST._serialized_end = 1750
    _CONSENSUSRESPONSE._serialized_start = 1752
    _CONSENSUSRESPONSE._serialized_end = 1866
    _CONSENSUSRESPONSEDATA._serialized_start = 1868
    _CONSENSUSRESPONSEDATA._serialized_end = 1985
    _GETCONSENSUSRUNSREQUEST._serialized_start = 1988
    _GETCONSENSUSRUNSREQUEST._serialized_end = 2214
    _GETCONSENSUSRUNSRESPONSE._serialized_start = 2216
    _GETCONSENSUSRUNSRESPONSE._serialized_end = 2336
    _GETCONSENSUSRUNSDATA._serialized_start = 2338
    _GETCONSENSUSRUNSDATA._serialized_end = 2464
    _CONSENSUSRESULTSET._serialized_start = 2467
    _CONSENSUSRESULTSET._serialized_end = 2834
    _CONSENSUSRESULTSETVALUESREQUEST._serialized_start = 2837
    _CONSENSUSRESULTSETVALUESREQUEST._serialized_end = 3161
    _CONSENSUSRESULTSETVALUESRESPONSE._serialized_start = 3164
    _CONSENSUSRESULTSETVALUESRESPONSE._serialized_end = 3296
    _CONSENSUSRESULTSETVALUES._serialized_start = 3299
    _CONSENSUSRESULTSETVALUES._serialized_end = 3429