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
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1epublic/consensus_service.proto\x12\x08titanium\x1a\x1cgoogle/api/annotations.proto\x1a\x19common/gateway_base.proto\x1a\x16common/consensus.proto2\xdf\t\n\x10ConsensusService\x12\x8b\x01\n\x13ConsensusTimestamps\x12$.titanium.ConsensusTimestampsRequest\x1a%.titanium.ConsensusTimestampsResponse"\'\x82\xd3\xe4\x93\x02!"\x1c/api/v1/consensus/timestamps:\x01*\x12b\n\tConsensus\x12\x1a.titanium.ConsensusRequest\x1a\x1b.titanium.ConsensusResponse"\x1c\x82\xd3\xe4\x93\x02\x16"\x11/api/v1/consensus:\x01*\x12a\n\x0eEvaluatedPrice\x12\x14.titanium.EVPRequest\x1a\x15.titanium.EVPResponse""\x82\xd3\xe4\x93\x02\x1c"\x17/api/v1/evaluated-price:\x01*\x12w\n\x11ConsensusOutliers\x12\x1d.titanium.OutliersListRequest\x1a!.titanium.ConsensusActiveResponse" \x82\xd3\xe4\x93\x02\x1a"\x15/api/v1/outliers-list:\x01*\x12\x81\x01\n\x10GetConsensusRuns\x12!.titanium.GetConsensusRunsRequest\x1a".titanium.GetConsensusRunsResponse"&\x82\xd3\xe4\x93\x02 "\x1b/api/v1/consensus-runs-view:\x01*\x12\x9f\x01\n\x18ConsensusResultSetValues\x12).titanium.ConsensusResultSetValuesRequest\x1a*.titanium.ConsensusResultSetValuesResponse",\x82\xd3\xe4\x93\x02&"!/api/v1/consensus-result-set-view:\x01*\x12\xaa\x01\n"ConsensusExplorerInstrumentDetails\x12".titanium.ConsensusExplorerRequest\x1a4.titanium.ConsensusExplorerInstrumentDetailsResponse"*\x82\xd3\xe4\x93\x02$""/api/v1/consensus-explorer/details\x12\x90\x01\n\x16ConsensusExplorerTable\x12".titanium.ConsensusExplorerRequest\x1a(.titanium.ConsensusExplorerTableResponse"(\x82\xd3\xe4\x93\x02"" /api/v1/consensus-explorer/table\x12\x96\x01\n\x17ConsensusExplorerRanges\x12\'.titanium.ConsensusExplorerRangeRequest\x1a(.titanium.ConsensusExplorerRangeResponse"(\x82\xd3\xe4\x93\x02"" /api/v1/consensus-explorer/rangeB~\n com.peernova.titanium.interfacesB"ConsensusServiceServiceProtoPublicP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/publicb\x06proto3')
_CONSENSUSSERVICE = DESCRIPTOR.services_by_name['ConsensusService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesB"ConsensusServiceServiceProtoPublicP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/public'
    _CONSENSUSSERVICE.methods_by_name['ConsensusTimestamps']._options = None
    _CONSENSUSSERVICE.methods_by_name['ConsensusTimestamps']._serialized_options = b'\x82\xd3\xe4\x93\x02!"\x1c/api/v1/consensus/timestamps:\x01*'
    _CONSENSUSSERVICE.methods_by_name['Consensus']._options = None
    _CONSENSUSSERVICE.methods_by_name['Consensus']._serialized_options = b'\x82\xd3\xe4\x93\x02\x16"\x11/api/v1/consensus:\x01*'
    _CONSENSUSSERVICE.methods_by_name['EvaluatedPrice']._options = None
    _CONSENSUSSERVICE.methods_by_name['EvaluatedPrice']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1c"\x17/api/v1/evaluated-price:\x01*'
    _CONSENSUSSERVICE.methods_by_name['ConsensusOutliers']._options = None
    _CONSENSUSSERVICE.methods_by_name['ConsensusOutliers']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1a"\x15/api/v1/outliers-list:\x01*'
    _CONSENSUSSERVICE.methods_by_name['GetConsensusRuns']._options = None
    _CONSENSUSSERVICE.methods_by_name['GetConsensusRuns']._serialized_options = b'\x82\xd3\xe4\x93\x02 "\x1b/api/v1/consensus-runs-view:\x01*'
    _CONSENSUSSERVICE.methods_by_name['ConsensusResultSetValues']._options = None
    _CONSENSUSSERVICE.methods_by_name['ConsensusResultSetValues']._serialized_options = b'\x82\xd3\xe4\x93\x02&"!/api/v1/consensus-result-set-view:\x01*'
    _CONSENSUSSERVICE.methods_by_name['ConsensusExplorerInstrumentDetails']._options = None
    _CONSENSUSSERVICE.methods_by_name['ConsensusExplorerInstrumentDetails']._serialized_options = b'\x82\xd3\xe4\x93\x02$""/api/v1/consensus-explorer/details'
    _CONSENSUSSERVICE.methods_by_name['ConsensusExplorerTable']._options = None
    _CONSENSUSSERVICE.methods_by_name['ConsensusExplorerTable']._serialized_options = b'\x82\xd3\xe4\x93\x02"" /api/v1/consensus-explorer/table'
    _CONSENSUSSERVICE.methods_by_name['ConsensusExplorerRanges']._options = None
    _CONSENSUSSERVICE.methods_by_name['ConsensusExplorerRanges']._serialized_options = b'\x82\xd3\xe4\x93\x02"" /api/v1/consensus-explorer/range'
    _CONSENSUSSERVICE._serialized_start = 126
    _CONSENSUSSERVICE._serialized_end = 1373