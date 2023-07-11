"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16common/consensus.proto\x12\x08titanium\x1a\x19common/gateway_base.proto\x1a\x1cgoogle/protobuf/struct.proto"|\n\x16ConsensusActiveRequest\x12\x0e\n\x06filter\x18\x01 \x01(\t\x12"\n\x07orderBy\x18\x02 \x01(\x0b2\x11.titanium.OrderBy\x12\x1e\n\x05limit\x18\x03 \x01(\x0b2\x0f.titanium.Limit\x12\x0e\n\x06offset\x18\x04 \x01(\x05"\x7f\n\x19ConsensusToPublishRequest\x12\x0e\n\x06filter\x18\x01 \x01(\t\x12"\n\x07orderBy\x18\x02 \x01(\x0b2\x11.titanium.OrderBy\x12\x1e\n\x05limit\x18\x03 \x01(\x0b2\x0f.titanium.Limit\x12\x0e\n\x06offset\x18\x04 \x01(\x05"\x84\x01\n\x1aConsensusToPublishResponse\x128\n\x04data\x18\x01 \x01(\x0b2(.titanium.ConsensusToPublishResponseDataH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"~\n\x1eConsensusToPublishResponseData\x12%\n\x07columns\x18\x01 \x03(\x0b2\x14.titanium.ColumnInfo\x12!\n\x04rows\x18\x02 \x03(\x0b2\x13.titanium.ValuesRow\x12\x12\n\ntotal_rows\x18\x03 \x01(\x05"^\n\x17ConsensusPublishRequest\x12\x1d\n\x15consensus_tracking_id\x18\x01 \x01(\t\x12\x10\n\x08asset_id\x18\x02 \x01(\t\x12\x12\n\ntrace_name\x18\x03 \x01(\t"}\n\x17ConsensusHistoryRequest\x12\x0e\n\x06filter\x18\x01 \x01(\t\x12"\n\x07orderBy\x18\x02 \x01(\x0b2\x11.titanium.OrderBy\x12\x1e\n\x05limit\x18\x03 \x01(\x0b2\x0f.titanium.Limit\x12\x0e\n\x06offset\x18\x04 \x01(\x05"\x80\x01\n\x18ConsensusHistoryResponse\x126\n\x04data\x18\x01 \x01(\x0b2&.titanium.ConsensusHistoryResponseDataH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"|\n\x1cConsensusHistoryResponseData\x12%\n\x07columns\x18\x01 \x03(\x0b2\x14.titanium.ColumnInfo\x12!\n\x04rows\x18\x02 \x03(\x0b2\x13.titanium.ValuesRow\x12\x12\n\ntotal_rows\x18\x03 \x01(\x05"_\n\x18ConsensusDecisionRequest\x12\x1d\n\x15consensus_tracking_id\x18\x01 \x01(\t\x12$\n\x08decision\x18\x02 \x01(\x0e2\x12.titanium.Decision"B\n\x1aConsensusTimestampsRequest\x12\x10\n\x08asset_id\x18\x01 \x01(\t\x12\x12\n\ntrace_name\x18\x02 \x01(\t"\x86\x01\n\x1bConsensusTimestampsResponse\x129\n\x04data\x18\x01 \x01(\x0b2).titanium.ConsensusTimestampsResponseDataH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"W\n\x1fConsensusTimestampsResponseData\x124\n\ntimestamps\x18\x01 \x03(\x0b2 .titanium.ConsensusTimestampMeta"R\n\x16ConsensusTimestampMeta\x12\x1f\n\x17consensus_run_timestamp\x18\x01 \x01(\t\x12\x17\n\x0fsubmitted_dates\x18\x02 \x03(\t"\xd5\x01\n\x10ConsensusRequest\x12\x10\n\x08asset_id\x18\x01 \x01(\t\x12\x16\n\x0esubmitted_date\x18\x02 \x01(\t\x12\x1f\n\x17consensus_run_timestamp\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12"\n\x07orderBy\x18\x05 \x01(\x0b2\x11.titanium.OrderBy\x12\x1e\n\x05limit\x18\x06 \x01(\x0b2\x0f.titanium.Limit\x12\x0e\n\x06offset\x18\x07 \x01(\x05\x12\x12\n\ntrace_name\x18\x08 \x01(\t"r\n\x11ConsensusResponse\x12/\n\x04data\x18\x01 \x01(\x0b2\x1f.titanium.ConsensusResponseDataH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"u\n\x15ConsensusResponseData\x12%\n\x07columns\x18\x01 \x03(\x0b2\x14.titanium.ColumnInfo\x12!\n\x04rows\x18\x02 \x03(\x0b2\x13.titanium.ValuesRow\x12\x12\n\ntotal_rows\x18\x03 \x01(\x05"\x87\x02\n\x17GetConsensusRunsRequest\x12\x10\n\x08asset_id\x18\x01 \x01(\t\x12\x12\n\ntrace_name\x18\x02 \x01(\t\x12\x16\n\x0esnap_date_from\x18\x03 \x01(\t\x12\x14\n\x0csnap_date_to\x18\x04 \x01(\t\x12\x13\n\x0bparticipant\x18\x05 \x01(\t\x12\x15\n\rshow_archived\x18\x06 \x01(\x08\x12)\n\x0bfilter_pack\x18\x07 \x01(\x0b2\x14.titanium.FilterPack\x12\x1c\n\x04page\x18\x08 \x01(\x0b2\x0e.titanium.Page\x12#\n\x08order_by\x18\t \x01(\x0b2\x11.titanium.OrderBy"x\n\x18GetConsensusRunsResponse\x12 \n\x05error\x18\x01 \x01(\x0b2\x0f.titanium.ErrorH\x00\x12.\n\x04data\x18\x02 \x01(\x0b2\x1e.titanium.GetConsensusRunsDataH\x00B\n\n\x08response"~\n\x14GetConsensusRunsData\x12%\n\x07columns\x18\x01 \x03(\x0b2\x14.titanium.ColumnInfo\x12!\n\x04rows\x18\x02 \x03(\x0b2\x13.titanium.ValuesRow\x12\x1c\n\x04page\x18\x03 \x01(\x0b2\x0e.titanium.Page"\xef\x02\n\x12ConsensusResultSet\x12\x18\n\x10consensus_run_id\x18\x01 \x01(\t\x12\x1f\n\x17consensus_result_set_id\x18\x02 \x01(\t\x12\x1c\n\x14submission_timestamp\x18\x03 \x01(\t\x12\x1c\n\x14consensus_run_status\x18\x04 \x01(\t\x12\x13\n\x0bcohort_name\x18\x05 \x01(\t\x12\x14\n\x0cdata_content\x18\x06 \x01(\t\x12\x1f\n\x17consensus_run_timestamp\x18\x07 \x01(\t\x12\x14\n\x0cparticipants\x18\x08 \x03(\t\x12\x13\n\x0bparticipant\x18\t \x01(\t\x12\x0e\n\x06status\x18\n \x01(\t\x12\x17\n\x0fconsensus_notes\x18\x0b \x01(\t\x12"\n\x1aconsensus_result_set_label\x18\x0c \x01(\t\x12\x0e\n\x06run_by\x18\r \x01(\t\x12\x0e\n\x06job_id\x18\x0e \x01(\t"\xfd\x01\n\x1fConsensusResultSetValuesRequest\x12\x10\n\x08asset_id\x18\x01 \x01(\t\x12\x12\n\ntrace_name\x18\x02 \x01(\t\x12\x16\n\x0esubmitted_date\x18\x03 \x01(\t\x12\x1f\n\x17consensus_run_timestamp\x18\x04 \x01(\t\x12\x0e\n\x06client\x18\x05 \x01(\t\x12)\n\x0bfilter_pack\x18\x06 \x01(\x0b2\x14.titanium.FilterPack\x12"\n\x07orderBy\x18\x07 \x01(\x0b2\x11.titanium.OrderBy\x12\x1c\n\x04page\x18\x08 \x01(\x0b2\x0e.titanium.Page"\x84\x01\n ConsensusResultSetValuesResponse\x122\n\x04data\x18\x01 \x01(\x0b2".titanium.ConsensusResultSetValuesH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"\x82\x01\n\x18ConsensusResultSetValues\x12%\n\x07columns\x18\x01 \x03(\x0b2\x14.titanium.ColumnInfo\x12!\n\x04rows\x18\x02 \x03(\x0b2\x13.titanium.ValuesRow\x12\x1c\n\x04page\x18\x03 \x01(\x0b2\x0e.titanium.Page"\xde\x01\n)ConsensusExplorerInstrumentDetailsRequest\x12\x10\n\x08asset_id\x18\x01 \x01(\t\x12\x16\n\x0esubmitted_date\x18\x02 \x01(\t\x12\x1f\n\x17consensus_result_set_id\x18\x03 \x01(\t\x12\x16\n\x0csubmitted_id\x18\x04 \x01(\tH\x00\x12\x16\n\x0cconsensus_id\x18\x05 \x01(\tH\x00\x12\x1c\n\x12evaluated_price_id\x18\x06 \x01(\tH\x00\x12\x12\n\ntrace_name\x18\x07 \x01(\tB\x04\n\x02id"\xba\x01\n\x1dConsensusExplorerRangeRequest\x12\x10\n\x08asset_id\x18\x01 \x01(\t\x12\x16\n\x0esubmitted_date\x18\x02 \x01(\t\x12\x13\n\x0bparticipant\x18\x03 \x01(\t\x12\x1f\n\x17consensus_run_timestamp\x18\x04 \x01(\t\x12\x15\n\rsubmission_id\x18\x05 \x01(\t\x12\x0e\n\x06expert\x18\x06 \x01(\x08\x12\x12\n\ntrace_name\x18\x07 \x01(\t"\xd8\x01\n\nEVPRequest\x12\x10\n\x08asset_id\x18\x01 \x01(\t\x12\x16\n\x0esubmitted_date\x18\x02 \x01(\t\x12\x1f\n\x17consensus_run_timestamp\x18\x03 \x01(\t\x12)\n\x0bfilter_pack\x18\x04 \x01(\x0b2\x14.titanium.FilterPack\x12"\n\x07orderBy\x18\x05 \x01(\x0b2\x11.titanium.OrderBy\x12\x1c\n\x04page\x18\x06 \x01(\x0b2\x0e.titanium.Page\x12\x12\n\ntrace_name\x18\x07 \x01(\t"f\n\x0bEVPResponse\x12)\n\x04data\x18\x01 \x01(\x0b2\x19.titanium.EVPResponseDataH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"y\n\x0fEVPResponseData\x12%\n\x07columns\x18\x01 \x03(\x0b2\x14.titanium.ColumnInfo\x12!\n\x04rows\x18\x02 \x03(\x0b2\x13.titanium.ValuesRow\x12\x1c\n\x04page\x18\x03 \x01(\x0b2\x0e.titanium.PageBw\n com.peernova.titanium.interfacesB\x1bConsensusServiceProtoCommonP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/commonb\x06proto3')
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
_CONSENSUSEXPLORERINSTRUMENTDETAILSREQUEST = DESCRIPTOR.message_types_by_name['ConsensusExplorerInstrumentDetailsRequest']
_CONSENSUSEXPLORERRANGEREQUEST = DESCRIPTOR.message_types_by_name['ConsensusExplorerRangeRequest']
_EVPREQUEST = DESCRIPTOR.message_types_by_name['EVPRequest']
_EVPRESPONSE = DESCRIPTOR.message_types_by_name['EVPResponse']
_EVPRESPONSEDATA = DESCRIPTOR.message_types_by_name['EVPResponseData']
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
ConsensusExplorerInstrumentDetailsRequest = _reflection.GeneratedProtocolMessageType('ConsensusExplorerInstrumentDetailsRequest', (_message.Message,), {'DESCRIPTOR': _CONSENSUSEXPLORERINSTRUMENTDETAILSREQUEST, '__module__': 'common.consensus_pb2'})
_sym_db.RegisterMessage(ConsensusExplorerInstrumentDetailsRequest)
ConsensusExplorerRangeRequest = _reflection.GeneratedProtocolMessageType('ConsensusExplorerRangeRequest', (_message.Message,), {'DESCRIPTOR': _CONSENSUSEXPLORERRANGEREQUEST, '__module__': 'common.consensus_pb2'})
_sym_db.RegisterMessage(ConsensusExplorerRangeRequest)
EVPRequest = _reflection.GeneratedProtocolMessageType('EVPRequest', (_message.Message,), {'DESCRIPTOR': _EVPREQUEST, '__module__': 'common.consensus_pb2'})
_sym_db.RegisterMessage(EVPRequest)
EVPResponse = _reflection.GeneratedProtocolMessageType('EVPResponse', (_message.Message,), {'DESCRIPTOR': _EVPRESPONSE, '__module__': 'common.consensus_pb2'})
_sym_db.RegisterMessage(EVPResponse)
EVPResponseData = _reflection.GeneratedProtocolMessageType('EVPResponseData', (_message.Message,), {'DESCRIPTOR': _EVPRESPONSEDATA, '__module__': 'common.consensus_pb2'})
_sym_db.RegisterMessage(EVPResponseData)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesB\x1bConsensusServiceProtoCommonP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/common'
    _CONSENSUSACTIVEREQUEST._serialized_start = 93
    _CONSENSUSACTIVEREQUEST._serialized_end = 217
    _CONSENSUSTOPUBLISHREQUEST._serialized_start = 219
    _CONSENSUSTOPUBLISHREQUEST._serialized_end = 346
    _CONSENSUSTOPUBLISHRESPONSE._serialized_start = 349
    _CONSENSUSTOPUBLISHRESPONSE._serialized_end = 481
    _CONSENSUSTOPUBLISHRESPONSEDATA._serialized_start = 483
    _CONSENSUSTOPUBLISHRESPONSEDATA._serialized_end = 609
    _CONSENSUSPUBLISHREQUEST._serialized_start = 611
    _CONSENSUSPUBLISHREQUEST._serialized_end = 705
    _CONSENSUSHISTORYREQUEST._serialized_start = 707
    _CONSENSUSHISTORYREQUEST._serialized_end = 832
    _CONSENSUSHISTORYRESPONSE._serialized_start = 835
    _CONSENSUSHISTORYRESPONSE._serialized_end = 963
    _CONSENSUSHISTORYRESPONSEDATA._serialized_start = 965
    _CONSENSUSHISTORYRESPONSEDATA._serialized_end = 1089
    _CONSENSUSDECISIONREQUEST._serialized_start = 1091
    _CONSENSUSDECISIONREQUEST._serialized_end = 1186
    _CONSENSUSTIMESTAMPSREQUEST._serialized_start = 1188
    _CONSENSUSTIMESTAMPSREQUEST._serialized_end = 1254
    _CONSENSUSTIMESTAMPSRESPONSE._serialized_start = 1257
    _CONSENSUSTIMESTAMPSRESPONSE._serialized_end = 1391
    _CONSENSUSTIMESTAMPSRESPONSEDATA._serialized_start = 1393
    _CONSENSUSTIMESTAMPSRESPONSEDATA._serialized_end = 1480
    _CONSENSUSTIMESTAMPMETA._serialized_start = 1482
    _CONSENSUSTIMESTAMPMETA._serialized_end = 1564
    _CONSENSUSREQUEST._serialized_start = 1567
    _CONSENSUSREQUEST._serialized_end = 1780
    _CONSENSUSRESPONSE._serialized_start = 1782
    _CONSENSUSRESPONSE._serialized_end = 1896
    _CONSENSUSRESPONSEDATA._serialized_start = 1898
    _CONSENSUSRESPONSEDATA._serialized_end = 2015
    _GETCONSENSUSRUNSREQUEST._serialized_start = 2018
    _GETCONSENSUSRUNSREQUEST._serialized_end = 2281
    _GETCONSENSUSRUNSRESPONSE._serialized_start = 2283
    _GETCONSENSUSRUNSRESPONSE._serialized_end = 2403
    _GETCONSENSUSRUNSDATA._serialized_start = 2405
    _GETCONSENSUSRUNSDATA._serialized_end = 2531
    _CONSENSUSRESULTSET._serialized_start = 2534
    _CONSENSUSRESULTSET._serialized_end = 2901
    _CONSENSUSRESULTSETVALUESREQUEST._serialized_start = 2904
    _CONSENSUSRESULTSETVALUESREQUEST._serialized_end = 3157
    _CONSENSUSRESULTSETVALUESRESPONSE._serialized_start = 3160
    _CONSENSUSRESULTSETVALUESRESPONSE._serialized_end = 3292
    _CONSENSUSRESULTSETVALUES._serialized_start = 3295
    _CONSENSUSRESULTSETVALUES._serialized_end = 3425
    _CONSENSUSEXPLORERINSTRUMENTDETAILSREQUEST._serialized_start = 3428
    _CONSENSUSEXPLORERINSTRUMENTDETAILSREQUEST._serialized_end = 3650
    _CONSENSUSEXPLORERRANGEREQUEST._serialized_start = 3653
    _CONSENSUSEXPLORERRANGEREQUEST._serialized_end = 3839
    _EVPREQUEST._serialized_start = 3842
    _EVPREQUEST._serialized_end = 4058
    _EVPRESPONSE._serialized_start = 4060
    _EVPRESPONSE._serialized_end = 4162
    _EVPRESPONSEDATA._serialized_start = 4164
    _EVPRESPONSEDATA._serialized_end = 4285