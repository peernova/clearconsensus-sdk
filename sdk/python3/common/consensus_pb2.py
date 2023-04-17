"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16common/consensus.proto\x12\x08titanium\x1a\x19common/gateway_base.proto\x1a\x1cgoogle/protobuf/struct.proto"|\n\x16ConsensusActiveRequest\x12\x0e\n\x06filter\x18\x01 \x01(\t\x12"\n\x07orderBy\x18\x02 \x01(\x0b2\x11.titanium.OrderBy\x12\x1e\n\x05limit\x18\x03 \x01(\x0b2\x0f.titanium.Limit\x12\x0e\n\x06offset\x18\x04 \x01(\x05"\x7f\n\x19ConsensusToPublishRequest\x12\x0e\n\x06filter\x18\x01 \x01(\t\x12"\n\x07orderBy\x18\x02 \x01(\x0b2\x11.titanium.OrderBy\x12\x1e\n\x05limit\x18\x03 \x01(\x0b2\x0f.titanium.Limit\x12\x0e\n\x06offset\x18\x04 \x01(\x05"\x84\x01\n\x1aConsensusToPublishResponse\x128\n\x04data\x18\x01 \x01(\x0b2(.titanium.ConsensusToPublishResponseDataH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"~\n\x1eConsensusToPublishResponseData\x12%\n\x07columns\x18\x01 \x03(\x0b2\x14.titanium.ColumnInfo\x12!\n\x04rows\x18\x02 \x03(\x0b2\x13.titanium.ValuesRow\x12\x12\n\ntotal_rows\x18\x03 \x01(\x05"^\n\x17ConsensusPublishRequest\x12\x1d\n\x15consensus_tracking_id\x18\x01 \x01(\t\x12\x10\n\x08asset_id\x18\x02 \x01(\t\x12\x12\n\ntrace_name\x18\x03 \x01(\t"}\n\x17ConsensusHistoryRequest\x12\x0e\n\x06filter\x18\x01 \x01(\t\x12"\n\x07orderBy\x18\x02 \x01(\x0b2\x11.titanium.OrderBy\x12\x1e\n\x05limit\x18\x03 \x01(\x0b2\x0f.titanium.Limit\x12\x0e\n\x06offset\x18\x04 \x01(\x05"\x80\x01\n\x18ConsensusHistoryResponse\x126\n\x04data\x18\x01 \x01(\x0b2&.titanium.ConsensusHistoryResponseDataH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"|\n\x1cConsensusHistoryResponseData\x12%\n\x07columns\x18\x01 \x03(\x0b2\x14.titanium.ColumnInfo\x12!\n\x04rows\x18\x02 \x03(\x0b2\x13.titanium.ValuesRow\x12\x12\n\ntotal_rows\x18\x03 \x01(\x05"_\n\x18ConsensusDecisionRequest\x12\x1d\n\x15consensus_tracking_id\x18\x01 \x01(\t\x12$\n\x08decision\x18\x02 \x01(\x0e2\x12.titanium.Decision"B\n\x1aConsensusTimestampsRequest\x12\x10\n\x08asset_id\x18\x01 \x01(\t\x12\x12\n\ntrace_name\x18\x02 \x01(\t"\x86\x01\n\x1bConsensusTimestampsResponse\x129\n\x04data\x18\x01 \x01(\x0b2).titanium.ConsensusTimestampsResponseDataH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"W\n\x1fConsensusTimestampsResponseData\x124\n\ntimestamps\x18\x01 \x03(\x0b2 .titanium.ConsensusTimestampMeta"R\n\x16ConsensusTimestampMeta\x12\x1f\n\x17consensus_run_timestamp\x18\x01 \x01(\t\x12\x17\n\x0fsubmitted_dates\x18\x02 \x03(\t"\xd5\x01\n\x10ConsensusRequest\x12\x10\n\x08asset_id\x18\x01 \x01(\t\x12\x16\n\x0esubmitted_date\x18\x02 \x01(\t\x12\x1f\n\x17consensus_run_timestamp\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12"\n\x07orderBy\x18\x05 \x01(\x0b2\x11.titanium.OrderBy\x12\x1e\n\x05limit\x18\x06 \x01(\x0b2\x0f.titanium.Limit\x12\x0e\n\x06offset\x18\x07 \x01(\x05\x12\x12\n\ntrace_name\x18\x08 \x01(\t"r\n\x11ConsensusResponse\x12/\n\x04data\x18\x01 \x01(\x0b2\x1f.titanium.ConsensusResponseDataH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"u\n\x15ConsensusResponseData\x12%\n\x07columns\x18\x01 \x03(\x0b2\x14.titanium.ColumnInfo\x12!\n\x04rows\x18\x02 \x03(\x0b2\x13.titanium.ValuesRow\x12\x12\n\ntotal_rows\x18\x03 \x01(\x05"\xe2\x01\n\x17GetConsensusRunsRequest\x12\x10\n\x08asset_id\x18\x01 \x01(\t\x12\x12\n\ntrace_name\x18\x02 \x01(\t\x12\x16\n\x0esnap_date_from\x18\x03 \x01(\t\x12\x14\n\x0csnap_date_to\x18\x04 \x01(\t\x12\x13\n\x0bparticipant\x18\x05 \x01(\t\x12\x15\n\rshow_archived\x18\x06 \x01(\x08\x12)\n\x0bfilter_pack\x18\x07 \x01(\x0b2\x14.titanium.FilterPack\x12\x1c\n\x04page\x18\x08 \x01(\x0b2\x0e.titanium.Page"x\n\x18GetConsensusRunsResponse\x12 \n\x05error\x18\x01 \x01(\x0b2\x0f.titanium.ErrorH\x00\x12.\n\x04data\x18\x02 \x01(\x0b2\x1e.titanium.GetConsensusRunsDataH\x00B\n\n\x08response"~\n\x14GetConsensusRunsData\x12%\n\x07columns\x18\x01 \x03(\x0b2\x14.titanium.ColumnInfo\x12!\n\x04rows\x18\x02 \x03(\x0b2\x13.titanium.ValuesRow\x12\x1c\n\x04page\x18\x03 \x01(\x0b2\x0e.titanium.Page"\xef\x02\n\x12ConsensusResultSet\x12\x18\n\x10consensus_run_id\x18\x01 \x01(\t\x12\x1f\n\x17consensus_result_set_id\x18\x02 \x01(\t\x12\x1c\n\x14submission_timestamp\x18\x03 \x01(\t\x12\x1c\n\x14consensus_run_status\x18\x04 \x01(\t\x12\x13\n\x0bcohort_name\x18\x05 \x01(\t\x12\x14\n\x0cdata_content\x18\x06 \x01(\t\x12\x1f\n\x17consensus_run_timestamp\x18\x07 \x01(\t\x12\x14\n\x0cparticipants\x18\x08 \x03(\t\x12\x13\n\x0bparticipant\x18\t \x01(\t\x12\x0e\n\x06status\x18\n \x01(\t\x12\x17\n\x0fconsensus_notes\x18\x0b \x01(\t\x12"\n\x1aconsensus_result_set_label\x18\x0c \x01(\t\x12\x0e\n\x06run_by\x18\r \x01(\t\x12\x0e\n\x06job_id\x18\x0e \x01(\t"\xc4\x02\n\x1fConsensusResultSetValuesRequest\x12\x10\n\x08asset_id\x18\x01 \x01(\t\x12\x12\n\ntrace_name\x18\x02 \x01(\t\x12\x14\n\x0csubmitted_id\x18\x03 \x01(\t\x12\x16\n\x0esubmitted_date\x18\x04 \x01(\t\x12\x1f\n\x17consensus_result_set_id\x18\x05 \x01(\t\x12\x1f\n\x17consensus_run_timestamp\x18\x06 \x01(\t\x12\x0e\n\x06client\x18\x07 \x01(\t\x12\x0e\n\x06filter\x18\x08 \x01(\t\x12)\n\x0bfilter_pack\x18\t \x01(\x0b2\x14.titanium.FilterPack\x12"\n\x07orderBy\x18\n \x01(\x0b2\x11.titanium.OrderBy\x12\x1c\n\x04page\x18\x0b \x01(\x0b2\x0e.titanium.Page"\x84\x01\n ConsensusResultSetValuesResponse\x122\n\x04data\x18\x01 \x01(\x0b2".titanium.ConsensusResultSetValuesH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"\x82\x01\n\x18ConsensusResultSetValues\x12%\n\x07columns\x18\x01 \x03(\x0b2\x14.titanium.ColumnInfo\x12!\n\x04rows\x18\x02 \x03(\x0b2\x13.titanium.ValuesRow\x12\x1c\n\x04page\x18\x03 \x01(\x0b2\x0e.titanium.Page"\xde\x01\n)ConsensusExplorerInstrumentDetailsRequest\x12\x10\n\x08asset_id\x18\x01 \x01(\t\x12\x16\n\x0esubmitted_date\x18\x02 \x01(\t\x12\x1f\n\x17consensus_result_set_id\x18\x03 \x01(\t\x12\x16\n\x0csubmitted_id\x18\x04 \x01(\tH\x00\x12\x16\n\x0cconsensus_id\x18\x05 \x01(\tH\x00\x12\x1c\n\x12evaluated_price_id\x18\x06 \x01(\tH\x00\x12\x12\n\ntrace_name\x18\x07 \x01(\tB\x04\n\x02id"\xa5\x01\n\x18ConsensusExplorerRequest\x12\x10\n\x08asset_id\x18\x01 \x01(\t\x12\x16\n\x0esubmitted_date\x18\x02 \x01(\t\x12\x13\n\x0bparticipant\x18\x03 \x01(\t\x12\x1f\n\x17consensus_run_timestamp\x18\x04 \x01(\t\x12\x15\n\rsubmission_id\x18\x05 \x01(\t\x12\x12\n\ntrace_name\x18\x06 \x01(\t"\x9c\x01\n*ConsensusExplorerInstrumentDetailsResponse\x12@\n\x04data\x18\x01 \x01(\x0b20.titanium.ConsensusExplorerInstrumentDetailsDataH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"\xf0\x01\n&ConsensusExplorerInstrumentDetailsData\x12\x11\n\tis_expert\x18\x01 \x01(\x08\x122\n\x12instrument_details\x18\x02 \x03(\x0b2\x16.titanium.StringKeyVal\x12J\n\x1cinstrument_submission_status\x18\x03 \x01(\x0b2$.titanium.InstrumentSubmissionStatus\x123\n\x10consensus_scores\x18\x04 \x01(\x0b2\x19.titanium.ConsensusScores"\xc1\x01\n\x1aInstrumentSubmissionStatus\x12\x13\n\x0bhighest_dqe\x18\x01 \x01(\t\x12\x18\n\x10consensus_status\x18\x02 \x01(\t\x12 \n\x18consensus_status_details\x18\x03 \x01(\t\x12$\n\x1cparticipant_consensus_status\x18\x04 \x01(\t\x12,\n$participant_consensus_status_details\x18\x05 \x01(\t"\xf6\x01\n\x0fConsensusScores\x12@\n\x17consensus_density_score\x18\x01 \x01(\x0b2\x1f.titanium.ConsensusDensityScore\x121\n\x0fexpertise_score\x18\x03 \x01(\x0b2\x18.titanium.ExpertiseScore\x124\n\x11evp_quality_score\x18\x02 \x01(\x0b2\x19.titanium.EvpQualityScore\x128\n\x13evp_alignment_score\x18\x04 \x01(\x0b2\x1b.titanium.EvpAlignmentScore"\xfb\x02\n\x15ConsensusDensityScore\x12%\n\x05score\x18\x01 \x01(\x0b2\x16.google.protobuf.Value\x12.\n\x0eoutlier_volume\x18\x02 \x01(\x0b2\x16.google.protobuf.Value\x12*\n\nbimodality\x18\x03 \x01(\x0b2\x16.google.protobuf.Value\x12*\n\ndispersion\x18\x04 \x01(\x0b2\x16.google.protobuf.Value\x123\n\x13evp_alignment_score\x18\x05 \x01(\x0b2\x16.google.protobuf.Value\x12+\n\x0bevp_quality\x18\x06 \x01(\x0b2\x16.google.protobuf.Value\x12\x1e\n\x16number_of_participants\x18\x07 \x01(\x03\x121\n\x11challenge_quality\x18\x08 \x01(\x0b2\x16.google.protobuf.Value"\xe2\x03\n\x0eExpertiseScore\x12%\n\x05score\x18\x01 \x01(\x0b2\x16.google.protobuf.Value\x12.\n\x0eexpertise_rank\x18\x02 \x01(\x0b2\x16.google.protobuf.Value\x12-\n\rexperts_count\x18\x03 \x01(\x0b2\x16.google.protobuf.Value\x12/\n\x0fsubmitted_score\x18\x04 \x01(\x0b2\x16.google.protobuf.Value\x12/\n\x0fconsensus_score\x18\x05 \x01(\x0b2\x16.google.protobuf.Value\x126\n\x16dimension_credit_score\x18\x06 \x01(\x0b2\x16.google.protobuf.Value\x12/\n\x0fchallenge_score\x18\x07 \x01(\x0b2\x16.google.protobuf.Value\x128\n\x18consensus_distance_score\x18\x08 \x01(\x0b2\x16.google.protobuf.Value\x12E\n%proximityToPostChallengeConsensusMean\x18\t \x01(\x0b2\x16.google.protobuf.Value"|\n\x0fEvpQualityScore\x12%\n\x05score\x18\x01 \x01(\x0b2\x16.google.protobuf.Value\x12\x13\n\x0btrade_count\x18\x02 \x01(\t\x12\x13\n\x0border_count\x18\x03 \x01(\t\x12\x18\n\x10indicative_count\x18\x04 \x01(\t"\x9e\x02\n\x11EvpAlignmentScore\x12%\n\x05score\x18\x01 \x01(\x0b2\x16.google.protobuf.Value\x12\x14\n\x0cscore_status\x18\x02 \x01(\t\x12\'\n\x07evp_mid\x18\x03 \x01(\x0b2\x16.google.protobuf.Value\x12/\n\x0fsubmission_mean\x18\x04 \x01(\x0b2\x16.google.protobuf.Value\x122\n\x12submission_std_dev\x18\x05 \x01(\x0b2\x16.google.protobuf.Value\x12>\n\x1eevp_alignment_dispersion_score\x18\x06 \x01(\x0b2\x16.google.protobuf.Value"\x84\x01\n\x1eConsensusExplorerTableResponse\x124\n\x04data\x18\x01 \x01(\x0b2$.titanium.ConsensusExplorerTableDataH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"Q\n\x1aConsensusExplorerTableData\x123\n\x10comparison_table\x18\x01 \x01(\x0b2\x19.titanium.ComparisonTable"\xf8\x02\n\x0fComparisonTable\x12;\n\nsubmission\x18\x01 \x01(\x0b2\'.titanium.SubmissionExplorerTableColumn\x12P\n\x15submission_statistics\x18\x02 \x01(\x0b21.titanium.SubmissionStatisticsExplorerTableColumn\x12U\n all_participant_cohort_consensus\x18\x03 \x01(\x0b2+.titanium.AllParticipantExplorerTableColumn\x129\n\x0fevaluated_price\x18\x04 \x01(\x0b2 .titanium.EvpExplorerTableColumn\x12D\n\x17expert_cohort_consensus\x18\x05 \x01(\x0b2#.titanium.ExpertExplorerTableColumn"9\n\x1dSubmissionExplorerTableColumn\x12\x18\n\x10submission_price\x18\x01 \x01(\x01"\xbe\x03\n\'SubmissionStatisticsExplorerTableColumn\x120\n\x10statistical_mean\x18\x01 \x01(\x0b2\x16.google.protobuf.Value\x12>\n\x1eabs_diff_from_statistical_mean\x18\x02 \x01(\x0b2\x16.google.protobuf.Value\x12.\n\x0esub_price_diff\x18\x03 \x01(\x0b2\x16.google.protobuf.Value\x12.\n\x0elower_boundary\x18\x04 \x01(\x0b2\x16.google.protobuf.Value\x12.\n\x0eupper_boundary\x18\x05 \x01(\x0b2\x16.google.protobuf.Value\x12\x1e\n\x16sub_valid_points_count\x18\x06 \x01(\x03\x12\'\n\x07std_dev\x18\x07 \x01(\x0b2\x16.google.protobuf.Value\x12#\n\x03min\x18\x08 \x01(\x0b2\x16.google.protobuf.Value\x12#\n\x03max\x18\t \x01(\x0b2\x16.google.protobuf.Value"\xe8\x02\n!AllParticipantExplorerTableColumn\x12/\n\x0fconsensus_price\x18\x01 \x01(\x0b2\x16.google.protobuf.Value\x12=\n\x1dabs_diff_from_consensus_price\x18\x02 \x01(\x0b2\x16.google.protobuf.Value\x12.\n\x0esub_price_diff\x18\x03 \x01(\x0b2\x16.google.protobuf.Value\x12.\n\x0elower_boundary\x18\x04 \x01(\x0b2\x16.google.protobuf.Value\x12.\n\x0eupper_boundary\x18\x05 \x01(\x0b2\x16.google.protobuf.Value\x12\x1a\n\x12participants_count\x18\x06 \x01(\x03\x12\'\n\x07std_dev\x18\x07 \x01(\x0b2\x16.google.protobuf.Value"\x8e\x03\n\x16EvpExplorerTableColumn\x12#\n\x03mid\x18\x01 \x01(\x0b2\x16.google.protobuf.Value\x12#\n\x03bid\x18\x02 \x01(\x0b2\x16.google.protobuf.Value\x12#\n\x03ask\x18\x03 \x01(\x0b2\x16.google.protobuf.Value\x125\n\x15abs_diff_from_evp_mid\x18\x04 \x01(\x0b2\x16.google.protobuf.Value\x12.\n\x0esub_price_diff\x18\x05 \x01(\x0b2\x16.google.protobuf.Value\x122\n\x12evp_lower_boundary\x18\x06 \x01(\x0b2\x16.google.protobuf.Value\x122\n\x12evp_upper_boundary\x18\x07 \x01(\x0b2\x16.google.protobuf.Value\x126\n\x16trades_or_orders_count\x18\x08 \x01(\x0b2\x16.google.protobuf.Value"\xcd\x02\n\x19ExpertExplorerTableColumn\x12$\n\x04mean\x18\x01 \x01(\x0b2\x16.google.protobuf.Value\x12@\n abs_diff_from_expert_cohort_mean\x18\x02 \x01(\x0b2\x16.google.protobuf.Value\x12.\n\x0esub_price_diff\x18\x03 \x01(\x0b2\x16.google.protobuf.Value\x12%\n\x1dparticipant_instruments_count\x18\x04 \x01(\x03\x12\'\n\x07std_dev\x18\x05 \x01(\x0b2\x16.google.protobuf.Value\x12#\n\x03min\x18\x06 \x01(\x0b2\x16.google.protobuf.Value\x12#\n\x03max\x18\x07 \x01(\x0b2\x16.google.protobuf.Value"\xba\x01\n\x1dConsensusExplorerRangeRequest\x12\x10\n\x08asset_id\x18\x01 \x01(\t\x12\x16\n\x0esubmitted_date\x18\x02 \x01(\t\x12\x13\n\x0bparticipant\x18\x03 \x01(\t\x12\x1f\n\x17consensus_run_timestamp\x18\x04 \x01(\t\x12\x15\n\rsubmission_id\x18\x05 \x01(\t\x12\x0e\n\x06expert\x18\x06 \x01(\x08\x12\x12\n\ntrace_name\x18\x07 \x01(\t"\x84\x01\n\x1eConsensusExplorerRangeResponse\x124\n\x04data\x18\x01 \x01(\x0b2$.titanium.ConsensusExplorerRangeDataH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"\xa5\x04\n\x1aConsensusExplorerRangeData\x12+\n\x0cchart_ranges\x18\x01 \x01(\x0b2\x15.titanium.ChartRanges\x12.\n\x10submission_point\x18\x02 \x01(\x0b2\x14.titanium.RangePoint\x123\n\x15submission_mean_point\x18\x03 \x01(\x0b2\x14.titanium.RangePoint\x12%\n\x07evp_mid\x18\x04 \x01(\x0b2\x14.titanium.RangePoint\x12A\n#all_participant_crs_consensus_price\x18\x05 \x01(\x0b2\x14.titanium.RangePoint\x12=\n\x1fmarket_data_crs_consensus_price\x18\x06 \x01(\x0b2\x14.titanium.RangePoint\x12C\n%challenge_overlay_crs_consensus_price\x18\x07 \x01(\x0b2\x14.titanium.RangePoint\x12B\n$expert_pre_challenge_consensus_price\x18\x08 \x01(\x0b2\x14.titanium.RangePoint\x12C\n%expert_post_challenge_consensus_price\x18\t \x01(\x0b2\x14.titanium.RangePoint"\x8a\x03\n\x0bChartRanges\x12+\n\x12submission_min_max\x18\x01 \x01(\x0b2\x0f.titanium.Range\x12/\n\x16submission_mean_median\x18\x02 \x01(\x0b2\x0f.titanium.Range\x12\x1c\n\x03evp\x18\x03 \x01(\x0b2\x0f.titanium.Range\x122\n\x19submission_only_consensus\x18\x04 \x01(\x0b2\x0f.titanium.Range\x126\n\x1dmarket_data_overlay_consensus\x18\x05 \x01(\x0b2\x0f.titanium.Range\x124\n\x1bchallenge_overlay_consensus\x18\x06 \x01(\x0b2\x0f.titanium.Range\x12-\n\x14expert_pre_challenge\x18\x07 \x01(\x0b2\x0f.titanium.Range\x12.\n\x15expert_post_challenge\x18\x08 \x01(\x0b2\x0f.titanium.Range"M\n\x05Range\x12!\n\x03min\x18\x01 \x01(\x0b2\x14.titanium.RangePoint\x12!\n\x03max\x18\x02 \x01(\x0b2\x14.titanium.RangePoint"B\n\nRangePoint\x12\r\n\x05label\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b2\x16.google.protobuf.Value"\xd8\x01\n\nEVPRequest\x12\x10\n\x08asset_id\x18\x01 \x01(\t\x12\x16\n\x0esubmitted_date\x18\x02 \x01(\t\x12\x1f\n\x17consensus_run_timestamp\x18\x03 \x01(\t\x12)\n\x0bfilter_pack\x18\x04 \x01(\x0b2\x14.titanium.FilterPack\x12"\n\x07orderBy\x18\x05 \x01(\x0b2\x11.titanium.OrderBy\x12\x1c\n\x04page\x18\x06 \x01(\x0b2\x0e.titanium.Page\x12\x12\n\ntrace_name\x18\x07 \x01(\t"f\n\x0bEVPResponse\x12)\n\x04data\x18\x01 \x01(\x0b2\x19.titanium.EVPResponseDataH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"y\n\x0fEVPResponseData\x12%\n\x07columns\x18\x01 \x03(\x0b2\x14.titanium.ColumnInfo\x12!\n\x04rows\x18\x02 \x03(\x0b2\x13.titanium.ValuesRow\x12\x1c\n\x04page\x18\x03 \x01(\x0b2\x0e.titanium.PageBw\n com.peernova.titanium.interfacesB\x1bConsensusServiceProtoCommonP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/commonb\x06proto3')
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
_CONSENSUSEXPLORERREQUEST = DESCRIPTOR.message_types_by_name['ConsensusExplorerRequest']
_CONSENSUSEXPLORERINSTRUMENTDETAILSRESPONSE = DESCRIPTOR.message_types_by_name['ConsensusExplorerInstrumentDetailsResponse']
_CONSENSUSEXPLORERINSTRUMENTDETAILSDATA = DESCRIPTOR.message_types_by_name['ConsensusExplorerInstrumentDetailsData']
_INSTRUMENTSUBMISSIONSTATUS = DESCRIPTOR.message_types_by_name['InstrumentSubmissionStatus']
_CONSENSUSSCORES = DESCRIPTOR.message_types_by_name['ConsensusScores']
_CONSENSUSDENSITYSCORE = DESCRIPTOR.message_types_by_name['ConsensusDensityScore']
_EXPERTISESCORE = DESCRIPTOR.message_types_by_name['ExpertiseScore']
_EVPQUALITYSCORE = DESCRIPTOR.message_types_by_name['EvpQualityScore']
_EVPALIGNMENTSCORE = DESCRIPTOR.message_types_by_name['EvpAlignmentScore']
_CONSENSUSEXPLORERTABLERESPONSE = DESCRIPTOR.message_types_by_name['ConsensusExplorerTableResponse']
_CONSENSUSEXPLORERTABLEDATA = DESCRIPTOR.message_types_by_name['ConsensusExplorerTableData']
_COMPARISONTABLE = DESCRIPTOR.message_types_by_name['ComparisonTable']
_SUBMISSIONEXPLORERTABLECOLUMN = DESCRIPTOR.message_types_by_name['SubmissionExplorerTableColumn']
_SUBMISSIONSTATISTICSEXPLORERTABLECOLUMN = DESCRIPTOR.message_types_by_name['SubmissionStatisticsExplorerTableColumn']
_ALLPARTICIPANTEXPLORERTABLECOLUMN = DESCRIPTOR.message_types_by_name['AllParticipantExplorerTableColumn']
_EVPEXPLORERTABLECOLUMN = DESCRIPTOR.message_types_by_name['EvpExplorerTableColumn']
_EXPERTEXPLORERTABLECOLUMN = DESCRIPTOR.message_types_by_name['ExpertExplorerTableColumn']
_CONSENSUSEXPLORERRANGEREQUEST = DESCRIPTOR.message_types_by_name['ConsensusExplorerRangeRequest']
_CONSENSUSEXPLORERRANGERESPONSE = DESCRIPTOR.message_types_by_name['ConsensusExplorerRangeResponse']
_CONSENSUSEXPLORERRANGEDATA = DESCRIPTOR.message_types_by_name['ConsensusExplorerRangeData']
_CHARTRANGES = DESCRIPTOR.message_types_by_name['ChartRanges']
_RANGE = DESCRIPTOR.message_types_by_name['Range']
_RANGEPOINT = DESCRIPTOR.message_types_by_name['RangePoint']
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
ConsensusExplorerRequest = _reflection.GeneratedProtocolMessageType('ConsensusExplorerRequest', (_message.Message,), {'DESCRIPTOR': _CONSENSUSEXPLORERREQUEST, '__module__': 'common.consensus_pb2'})
_sym_db.RegisterMessage(ConsensusExplorerRequest)
ConsensusExplorerInstrumentDetailsResponse = _reflection.GeneratedProtocolMessageType('ConsensusExplorerInstrumentDetailsResponse', (_message.Message,), {'DESCRIPTOR': _CONSENSUSEXPLORERINSTRUMENTDETAILSRESPONSE, '__module__': 'common.consensus_pb2'})
_sym_db.RegisterMessage(ConsensusExplorerInstrumentDetailsResponse)
ConsensusExplorerInstrumentDetailsData = _reflection.GeneratedProtocolMessageType('ConsensusExplorerInstrumentDetailsData', (_message.Message,), {'DESCRIPTOR': _CONSENSUSEXPLORERINSTRUMENTDETAILSDATA, '__module__': 'common.consensus_pb2'})
_sym_db.RegisterMessage(ConsensusExplorerInstrumentDetailsData)
InstrumentSubmissionStatus = _reflection.GeneratedProtocolMessageType('InstrumentSubmissionStatus', (_message.Message,), {'DESCRIPTOR': _INSTRUMENTSUBMISSIONSTATUS, '__module__': 'common.consensus_pb2'})
_sym_db.RegisterMessage(InstrumentSubmissionStatus)
ConsensusScores = _reflection.GeneratedProtocolMessageType('ConsensusScores', (_message.Message,), {'DESCRIPTOR': _CONSENSUSSCORES, '__module__': 'common.consensus_pb2'})
_sym_db.RegisterMessage(ConsensusScores)
ConsensusDensityScore = _reflection.GeneratedProtocolMessageType('ConsensusDensityScore', (_message.Message,), {'DESCRIPTOR': _CONSENSUSDENSITYSCORE, '__module__': 'common.consensus_pb2'})
_sym_db.RegisterMessage(ConsensusDensityScore)
ExpertiseScore = _reflection.GeneratedProtocolMessageType('ExpertiseScore', (_message.Message,), {'DESCRIPTOR': _EXPERTISESCORE, '__module__': 'common.consensus_pb2'})
_sym_db.RegisterMessage(ExpertiseScore)
EvpQualityScore = _reflection.GeneratedProtocolMessageType('EvpQualityScore', (_message.Message,), {'DESCRIPTOR': _EVPQUALITYSCORE, '__module__': 'common.consensus_pb2'})
_sym_db.RegisterMessage(EvpQualityScore)
EvpAlignmentScore = _reflection.GeneratedProtocolMessageType('EvpAlignmentScore', (_message.Message,), {'DESCRIPTOR': _EVPALIGNMENTSCORE, '__module__': 'common.consensus_pb2'})
_sym_db.RegisterMessage(EvpAlignmentScore)
ConsensusExplorerTableResponse = _reflection.GeneratedProtocolMessageType('ConsensusExplorerTableResponse', (_message.Message,), {'DESCRIPTOR': _CONSENSUSEXPLORERTABLERESPONSE, '__module__': 'common.consensus_pb2'})
_sym_db.RegisterMessage(ConsensusExplorerTableResponse)
ConsensusExplorerTableData = _reflection.GeneratedProtocolMessageType('ConsensusExplorerTableData', (_message.Message,), {'DESCRIPTOR': _CONSENSUSEXPLORERTABLEDATA, '__module__': 'common.consensus_pb2'})
_sym_db.RegisterMessage(ConsensusExplorerTableData)
ComparisonTable = _reflection.GeneratedProtocolMessageType('ComparisonTable', (_message.Message,), {'DESCRIPTOR': _COMPARISONTABLE, '__module__': 'common.consensus_pb2'})
_sym_db.RegisterMessage(ComparisonTable)
SubmissionExplorerTableColumn = _reflection.GeneratedProtocolMessageType('SubmissionExplorerTableColumn', (_message.Message,), {'DESCRIPTOR': _SUBMISSIONEXPLORERTABLECOLUMN, '__module__': 'common.consensus_pb2'})
_sym_db.RegisterMessage(SubmissionExplorerTableColumn)
SubmissionStatisticsExplorerTableColumn = _reflection.GeneratedProtocolMessageType('SubmissionStatisticsExplorerTableColumn', (_message.Message,), {'DESCRIPTOR': _SUBMISSIONSTATISTICSEXPLORERTABLECOLUMN, '__module__': 'common.consensus_pb2'})
_sym_db.RegisterMessage(SubmissionStatisticsExplorerTableColumn)
AllParticipantExplorerTableColumn = _reflection.GeneratedProtocolMessageType('AllParticipantExplorerTableColumn', (_message.Message,), {'DESCRIPTOR': _ALLPARTICIPANTEXPLORERTABLECOLUMN, '__module__': 'common.consensus_pb2'})
_sym_db.RegisterMessage(AllParticipantExplorerTableColumn)
EvpExplorerTableColumn = _reflection.GeneratedProtocolMessageType('EvpExplorerTableColumn', (_message.Message,), {'DESCRIPTOR': _EVPEXPLORERTABLECOLUMN, '__module__': 'common.consensus_pb2'})
_sym_db.RegisterMessage(EvpExplorerTableColumn)
ExpertExplorerTableColumn = _reflection.GeneratedProtocolMessageType('ExpertExplorerTableColumn', (_message.Message,), {'DESCRIPTOR': _EXPERTEXPLORERTABLECOLUMN, '__module__': 'common.consensus_pb2'})
_sym_db.RegisterMessage(ExpertExplorerTableColumn)
ConsensusExplorerRangeRequest = _reflection.GeneratedProtocolMessageType('ConsensusExplorerRangeRequest', (_message.Message,), {'DESCRIPTOR': _CONSENSUSEXPLORERRANGEREQUEST, '__module__': 'common.consensus_pb2'})
_sym_db.RegisterMessage(ConsensusExplorerRangeRequest)
ConsensusExplorerRangeResponse = _reflection.GeneratedProtocolMessageType('ConsensusExplorerRangeResponse', (_message.Message,), {'DESCRIPTOR': _CONSENSUSEXPLORERRANGERESPONSE, '__module__': 'common.consensus_pb2'})
_sym_db.RegisterMessage(ConsensusExplorerRangeResponse)
ConsensusExplorerRangeData = _reflection.GeneratedProtocolMessageType('ConsensusExplorerRangeData', (_message.Message,), {'DESCRIPTOR': _CONSENSUSEXPLORERRANGEDATA, '__module__': 'common.consensus_pb2'})
_sym_db.RegisterMessage(ConsensusExplorerRangeData)
ChartRanges = _reflection.GeneratedProtocolMessageType('ChartRanges', (_message.Message,), {'DESCRIPTOR': _CHARTRANGES, '__module__': 'common.consensus_pb2'})
_sym_db.RegisterMessage(ChartRanges)
Range = _reflection.GeneratedProtocolMessageType('Range', (_message.Message,), {'DESCRIPTOR': _RANGE, '__module__': 'common.consensus_pb2'})
_sym_db.RegisterMessage(Range)
RangePoint = _reflection.GeneratedProtocolMessageType('RangePoint', (_message.Message,), {'DESCRIPTOR': _RANGEPOINT, '__module__': 'common.consensus_pb2'})
_sym_db.RegisterMessage(RangePoint)
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
    _GETCONSENSUSRUNSREQUEST._serialized_end = 2244
    _GETCONSENSUSRUNSRESPONSE._serialized_start = 2246
    _GETCONSENSUSRUNSRESPONSE._serialized_end = 2366
    _GETCONSENSUSRUNSDATA._serialized_start = 2368
    _GETCONSENSUSRUNSDATA._serialized_end = 2494
    _CONSENSUSRESULTSET._serialized_start = 2497
    _CONSENSUSRESULTSET._serialized_end = 2864
    _CONSENSUSRESULTSETVALUESREQUEST._serialized_start = 2867
    _CONSENSUSRESULTSETVALUESREQUEST._serialized_end = 3191
    _CONSENSUSRESULTSETVALUESRESPONSE._serialized_start = 3194
    _CONSENSUSRESULTSETVALUESRESPONSE._serialized_end = 3326
    _CONSENSUSRESULTSETVALUES._serialized_start = 3329
    _CONSENSUSRESULTSETVALUES._serialized_end = 3459
    _CONSENSUSEXPLORERINSTRUMENTDETAILSREQUEST._serialized_start = 3462
    _CONSENSUSEXPLORERINSTRUMENTDETAILSREQUEST._serialized_end = 3684
    _CONSENSUSEXPLORERREQUEST._serialized_start = 3687
    _CONSENSUSEXPLORERREQUEST._serialized_end = 3852
    _CONSENSUSEXPLORERINSTRUMENTDETAILSRESPONSE._serialized_start = 3855
    _CONSENSUSEXPLORERINSTRUMENTDETAILSRESPONSE._serialized_end = 4011
    _CONSENSUSEXPLORERINSTRUMENTDETAILSDATA._serialized_start = 4014
    _CONSENSUSEXPLORERINSTRUMENTDETAILSDATA._serialized_end = 4254
    _INSTRUMENTSUBMISSIONSTATUS._serialized_start = 4257
    _INSTRUMENTSUBMISSIONSTATUS._serialized_end = 4450
    _CONSENSUSSCORES._serialized_start = 4453
    _CONSENSUSSCORES._serialized_end = 4699
    _CONSENSUSDENSITYSCORE._serialized_start = 4702
    _CONSENSUSDENSITYSCORE._serialized_end = 5081
    _EXPERTISESCORE._serialized_start = 5084
    _EXPERTISESCORE._serialized_end = 5566
    _EVPQUALITYSCORE._serialized_start = 5568
    _EVPQUALITYSCORE._serialized_end = 5692
    _EVPALIGNMENTSCORE._serialized_start = 5695
    _EVPALIGNMENTSCORE._serialized_end = 5981
    _CONSENSUSEXPLORERTABLERESPONSE._serialized_start = 5984
    _CONSENSUSEXPLORERTABLERESPONSE._serialized_end = 6116
    _CONSENSUSEXPLORERTABLEDATA._serialized_start = 6118
    _CONSENSUSEXPLORERTABLEDATA._serialized_end = 6199
    _COMPARISONTABLE._serialized_start = 6202
    _COMPARISONTABLE._serialized_end = 6578
    _SUBMISSIONEXPLORERTABLECOLUMN._serialized_start = 6580
    _SUBMISSIONEXPLORERTABLECOLUMN._serialized_end = 6637
    _SUBMISSIONSTATISTICSEXPLORERTABLECOLUMN._serialized_start = 6640
    _SUBMISSIONSTATISTICSEXPLORERTABLECOLUMN._serialized_end = 7086
    _ALLPARTICIPANTEXPLORERTABLECOLUMN._serialized_start = 7089
    _ALLPARTICIPANTEXPLORERTABLECOLUMN._serialized_end = 7449
    _EVPEXPLORERTABLECOLUMN._serialized_start = 7452
    _EVPEXPLORERTABLECOLUMN._serialized_end = 7850
    _EXPERTEXPLORERTABLECOLUMN._serialized_start = 7853
    _EXPERTEXPLORERTABLECOLUMN._serialized_end = 8186
    _CONSENSUSEXPLORERRANGEREQUEST._serialized_start = 8189
    _CONSENSUSEXPLORERRANGEREQUEST._serialized_end = 8375
    _CONSENSUSEXPLORERRANGERESPONSE._serialized_start = 8378
    _CONSENSUSEXPLORERRANGERESPONSE._serialized_end = 8510
    _CONSENSUSEXPLORERRANGEDATA._serialized_start = 8513
    _CONSENSUSEXPLORERRANGEDATA._serialized_end = 9062
    _CHARTRANGES._serialized_start = 9065
    _CHARTRANGES._serialized_end = 9459
    _RANGE._serialized_start = 9461
    _RANGE._serialized_end = 9538
    _RANGEPOINT._serialized_start = 9540
    _RANGEPOINT._serialized_end = 9606
    _EVPREQUEST._serialized_start = 9609
    _EVPREQUEST._serialized_end = 9825
    _EVPRESPONSE._serialized_start = 9827
    _EVPRESPONSE._serialized_end = 9929
    _EVPRESPONSEDATA._serialized_start = 9931
    _EVPRESPONSEDATA._serialized_end = 10052