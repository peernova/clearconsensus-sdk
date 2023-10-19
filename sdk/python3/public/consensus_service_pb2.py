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
from ..common import data_pb2 as common_dot_data__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1epublic/consensus_service.proto\x12\x08titanium\x1a\x1cgoogle/api/annotations.proto\x1a\x19common/gateway_base.proto\x1a\x16common/consensus.proto\x1a\x11common/data.proto\x1a\x1cgoogle/protobuf/struct.proto"\xc4\x01\n\x18ConsensusExplorerRequest\x12\x10\n\x08asset_id\x18\x01 \x01(\t\x12\x12\n\ntrace_name\x18\x02 \x01(\t\x12\x16\n\x0esubmitted_date\x18\x03 \x01(\t\x12\x1f\n\x17consensus_run_timestamp\x18\x04 \x01(\t\x12\x17\n\rsubmission_id\x18\x05 \x01(\tH\x00\x12*\n\ngroup_keys\x18\x06 \x01(\x0b2\x14.titanium.FilterPackH\x00B\x04\n\x02id"\x9c\x01\n*ConsensusExplorerInstrumentDetailsResponse\x12@\n\x04data\x18\x01 \x01(\x0b20.titanium.ConsensusExplorerInstrumentDetailsDataH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"\xf4\x01\n&ConsensusExplorerInstrumentDetailsData\x122\n\x12instrument_details\x18\x01 \x03(\x0b2\x16.titanium.StringKeyVal\x12J\n\x1cinstrument_submission_status\x18\x02 \x01(\x0b2$.titanium.InstrumentSubmissionStatus\x123\n\x10consensus_scores\x18\x03 \x01(\x0b2\x19.titanium.ConsensusScores\x12\x15\n\rsubmission_id\x18\x04 \x01(\t"\x92\x04\n\x1aInstrumentSubmissionStatus\x12\x13\n\x0bhighest_dqe\x18\x01 \x01(\t\x12\x18\n\x10consensus_status\x18\x02 \x01(\t\x12 \n\x18consensus_status_details\x18\x03 \x01(\t\x12+\n#participant_cohort_consensus_status\x18\x04 \x01(\t\x12/\n\'participant_submissions_evidence_status\x18\x05 \x01(\t\x12+\n\x0bdqe_history\x18\x06 \x03(\x0b2\x16.titanium.DateAndValue\x128\n\x18consensus_status_history\x18\x07 \x03(\x0b2\x16.titanium.DateAndValue\x12@\n consensus_status_details_history\x18\x08 \x03(\x0b2\x16.titanium.DateAndValue\x12K\n+participant_cohort_consensus_status_history\x18\t \x03(\x0b2\x16.titanium.DateAndValue\x12O\n/participant_submissions_evidence_status_history\x18\n \x03(\x0b2\x16.titanium.DateAndValue"C\n\x0cDateAndValue\x12\x0c\n\x04date\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b2\x16.google.protobuf.Value"\xdc\x02\n\x0fConsensusScores\x12/\n\x0eexpertise_rank\x18\x01 \x01(\x0b2\x17.titanium.ExpertiseRank\x12@\n\x17consensus_density_score\x18\x02 \x01(\x0b2\x1f.titanium.ConsensusDensityScore\x12<\n\x15trade_alignment_score\x18\x03 \x01(\x0b2\x1d.titanium.TradeAlignmentScore\x128\n\x13evp_alignment_score\x18\x04 \x01(\x0b2\x1b.titanium.EvpAlignmentScore\x12(\n\nbimodality\x18\x05 \x01(\x0b2\x14.titanium.Bimodality\x124\n\x11evp_quality_score\x18\x06 \x01(\x0b2\x19.titanium.EvpQualityScore"\xe5\x02\n\rExpertiseRank\x12$\n\x04rank\x18\x01 \x01(\x0b2\x16.google.protobuf.Value\x12-\n\rexperts_count\x18\x02 \x01(\x0b2\x16.google.protobuf.Value\x120\n\x10submission_price\x18\x03 \x01(\x0b2\x16.google.protobuf.Value\x12,\n\x0canchor_price\x18\x04 \x01(\x0b2\x16.google.protobuf.Value\x126\n\x16abs_distance_to_anchor\x18\x05 \x01(\x0b2\x16.google.protobuf.Value\x12/\n\x0fexpertise_score\x18\x06 \x01(\x0b2\x16.google.protobuf.Value\x126\n\x07history\x18\x07 \x03(\x0b2%.titanium.ExpertiseRankHistoryElement"\x80\x01\n\x1bExpertiseRankHistoryElement\x12\x0c\n\x04date\x18\x01 \x01(\t\x12$\n\x04rank\x18\x02 \x01(\x0b2\x16.google.protobuf.Value\x12-\n\rexperts_count\x18\x03 \x01(\x0b2\x16.google.protobuf.Value"\xb1\x02\n\x15ConsensusDensityScore\x12%\n\x05score\x18\x01 \x01(\x0b2\x16.google.protobuf.Value\x120\n\x10bimodality_score\x18\x02 \x01(\x0b2\x16.google.protobuf.Value\x125\n\x15trade_alignment_score\x18\x03 \x01(\x0b2\x16.google.protobuf.Value\x12*\n\ndispersion\x18\x04 \x01(\x0b2\x16.google.protobuf.Value\x123\n\x13evp_alignment_score\x18\x05 \x01(\x0b2\x16.google.protobuf.Value\x12\'\n\x07history\x18\x06 \x03(\x0b2\x16.titanium.DateAndValue"\x8f\x02\n\x13TradeAlignmentScore\x12%\n\x05score\x18\x01 \x01(\x0b2\x16.google.protobuf.Value\x12\x14\n\x0cscore_status\x18\x02 \x01(\t\x122\n\x12latest_trade_price\x18\x03 \x01(\x0b2\x16.google.protobuf.Value\x12(\n\x08centroid\x18\x04 \x01(\x0b2\x16.google.protobuf.Value\x12\'\n\x07std_dev\x18\x05 \x01(\x0b2\x16.google.protobuf.Value\x124\n\x07history\x18\x06 \x03(\x0b2#.titanium.TradeAligmentDateAndValue"f\n\x19TradeAligmentDateAndValue\x12\x0c\n\x04date\x18\x01 \x01(\t\x12%\n\x05score\x18\x02 \x01(\x0b2\x16.google.protobuf.Value\x12\x14\n\x0cscore_status\x18\x03 \x01(\t"\x82\x02\n\x11EvpAlignmentScore\x12%\n\x05score\x18\x01 \x01(\x0b2\x16.google.protobuf.Value\x12\x14\n\x0cscore_status\x18\x02 \x01(\t\x12\'\n\x07evp_mid\x18\x03 \x01(\x0b2\x16.google.protobuf.Value\x12(\n\x08centroid\x18\x04 \x01(\x0b2\x16.google.protobuf.Value\x12\'\n\x07std_dev\x18\x05 \x01(\x0b2\x16.google.protobuf.Value\x124\n\x07history\x18\x06 \x03(\x0b2#.titanium.TradeAligmentDateAndValue"v\n\nBimodality\x12\r\n\x05value\x18\x01 \x01(\t\x120\n\x10bimodality_index\x18\x02 \x01(\x0b2\x16.google.protobuf.Value\x12\'\n\x07history\x18\x03 \x03(\x0b2\x16.titanium.DateAndValue"\xa5\x01\n\x0fEvpQualityScore\x12%\n\x05score\x18\x01 \x01(\x0b2\x16.google.protobuf.Value\x12\x13\n\x0btrade_count\x18\x02 \x01(\t\x12\x13\n\x0border_count\x18\x03 \x01(\t\x12\x18\n\x10indicative_count\x18\x04 \x01(\t\x12\'\n\x07history\x18\x05 \x03(\x0b2\x16.titanium.DateAndValue"\x84\x01\n\x1eConsensusExplorerRangeResponse\x124\n\x04data\x18\x01 \x01(\x0b2$.titanium.ConsensusExplorerRangeDataH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"\x9d\x04\n\x1aConsensusExplorerRangeData\x12+\n\x0cchart_ranges\x18\x01 \x01(\x0b2\x15.titanium.ChartRanges\x12.\n\x10submission_point\x18\x02 \x01(\x0b2\x14.titanium.RangePoint\x12-\n\x0fsubmission_mean\x18\x03 \x01(\x0b2\x14.titanium.RangePoint\x12*\n\x0canchor_point\x18\x04 \x01(\x0b2\x14.titanium.RangePoint\x12%\n\x07evp_mid\x18\x05 \x01(\x0b2\x14.titanium.RangePoint\x127\n\x19submission_evidence_price\x18\x06 \x01(\x0b2\x14.titanium.RangePoint\x124\n\x16cohort_consensus_price\x18\x07 \x01(\x0b2\x14.titanium.RangePoint\x12/\n\x11bimodal_left_mean\x18\x08 \x01(\x0b2\x14.titanium.RangePoint\x120\n\x12bimodal_right_mean\x18\t \x01(\x0b2\x14.titanium.RangePoint\x12N\n\x1fcohort_consensus_range_tab_data\x18\n \x01(\x0b2%.titanium.CohortConsensusRangeTabData"\x96\x02\n\x0bChartRanges\x12+\n\x12submission_min_max\x18\x01 \x01(\x0b2\x0f.titanium.Range\x12\x1c\n\x03evp\x18\x02 \x01(\x0b2\x0f.titanium.Range\x12,\n\x13submission_evidence\x18\x03 \x01(\x0b2\x0f.titanium.Range\x12)\n\x10cohort_consensus\x18\x04 \x01(\x0b2\x0f.titanium.Range\x120\n\x17bimodal_left_population\x18\x05 \x01(\x0b2\x0f.titanium.Range\x121\n\x18bimodal_right_population\x18\x06 \x01(\x0b2\x0f.titanium.Range"\xaa\x04\n\x1bCohortConsensusRangeTabData\x12.\n\x0eexpertise_rank\x18\x01 \x01(\x0b2\x16.google.protobuf.Value\x12\x15\n\rexperts_count\x18\x02 \x01(\x05\x12/\n\x0fexpertise_score\x18\x03 \x01(\x0b2\x16.google.protobuf.Value\x122\n\x12distance_to_anchor\x18\x04 \x01(\x0b2\x16.google.protobuf.Value\x125\n\x15distance_to_consensus\x18\x05 \x01(\x0b2\x16.google.protobuf.Value\x12E\n\x1atrade_periods_with_metrics\x18\x06 \x01(\x0b2!.titanium.TradePeriodsWithMetrics\x12<\n\x14trade_anchor_details\x18\x07 \x01(\x0b2\x1c.titanium.TradeAnchorDetailsH\x00\x128\n\x12evp_anchor_details\x18\x08 \x01(\x0b2\x1a.titanium.EvpAnchorDetailsH\x00\x12W\n"submission_evidence_anchor_details\x18\t \x01(\x0b2).titanium.SubmissionEvidenceAnchorDetailsH\x00B\x10\n\x0eanchor_details"\xb6\x01\n\x12TradeAnchorDetails\x12\x1a\n\x12latest_trade_price\x18\x01 \x01(\x01\x12\x1d\n\x15distance_to_consensus\x18\x02 \x01(\x01\x12\x10\n\x08notional\x18\x03 \x01(\x01\x12\x10\n\x08currency\x18\x04 \x01(\t\x12\x1c\n\x14trade_execution_time\x18\x05 \x01(\t\x12\x13\n\x0bpricing_age\x18\x06 \x01(\t\x12\x0e\n\x06source\x18\x07 \x01(\t"\x86\x01\n\x10EvpAnchorDetails\x12#\n\x03mid\x18\x01 \x01(\x0b2\x16.google.protobuf.Value\x12.\n\x0emid_calculated\x18\x02 \x01(\x0b2\x16.google.protobuf.Value\x12\x1d\n\x15distance_to_consensus\x18\x03 \x01(\x01"]\n\x1fSubmissionEvidenceAnchorDetails\x12\x1b\n\x13submission_evidence\x18\x01 \x01(\x01\x12\x1d\n\x15distance_to_consensus\x18\x02 \x01(\x01"\xac\x01\n\x17TradePeriodsWithMetrics\x12.\n\x08less_day\x18\x01 \x01(\x0b2\x1c.titanium.TradePeriodMetrics\x12/\n\tless_week\x18\x02 \x01(\x0b2\x1c.titanium.TradePeriodMetrics\x120\n\nless_month\x18\x03 \x01(\x0b2\x1c.titanium.TradePeriodMetrics"\x8e\x01\n\x12TradePeriodMetrics\x12\x13\n\x0btrade_count\x18\x01 \x01(\x03\x12\x1b\n\x13min_notional_amount\x18\x02 \x01(\x01\x12\x1b\n\x13max_notional_amount\x18\x03 \x01(\x01\x12\x17\n\x0ftotal_liquidity\x18\x04 \x01(\x01\x12\x10\n\x08currency\x18\x05 \x01(\t"\x84\x01\n\x1eConsensusExplorerTableResponse\x124\n\x04data\x18\x01 \x01(\x0b2$.titanium.ConsensusExplorerTableDataH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"Q\n\x1aConsensusExplorerTableData\x123\n\x10comparison_table\x18\x01 \x01(\x0b2\x19.titanium.ComparisonTable"\xec\x02\n\x0fComparisonTable\x12,\n\tconsensus\x18\x01 \x01(\x0b2\x19.titanium.ConsensusColumn\x121\n\rmy_submission\x18\x02 \x01(\x0b2\x1a.titanium.SubmissionColumn\x129\n\x10submission_range\x18\x03 \x01(\x0b2\x1f.titanium.SubmissionRangeColumn\x124\n\x11trade_time_series\x18\x04 \x01(\x0b2\x19.titanium.AvailableTrades\x126\n\x12evidential_pricing\x18\x05 \x01(\x0b2\x1a.titanium.EvidentalPricing\x12O\n!submission_statistical_boundaries\x18\x06 \x01(\x0b2$.titanium.SubmissionStatisticsColumn"\x83\x05\n\x0fConsensusColumn\x12)\n\tconsensus\x18\x01 \x01(\x0b2\x16.google.protobuf.Value\x127\n\x17abs_diff_from_consensus\x18\x02 \x01(\x0b2\x16.google.protobuf.Value\x12.\n\x0esub_price_diff\x18\x03 \x01(\x0b2\x16.google.protobuf.Value\x12A\n\x1fcons_abs_diff_from_anchor_trade\x18\x04 \x01(\x0b2\x16.google.protobuf.ValueH\x00\x12C\n!cons_abs_diff_from_anchor_evp_mid\x18\x05 \x01(\x0b2\x16.google.protobuf.ValueH\x00\x12H\n&cons_abs_diff_from_anchor_evp_mid_calc\x18\x06 \x01(\x0b2\x16.google.protobuf.ValueH\x00\x12?\n\x1dcons_abs_diff_from_anchor_sub\x18\x07 \x01(\x0b2\x16.google.protobuf.ValueH\x00\x12,\n\x0caccepted_min\x18\x08 \x01(\x0b2\x16.google.protobuf.Value\x12,\n\x0caccepted_max\x18\t \x01(\x0b2\x16.google.protobuf.Value\x125\n\x15number_of_instruments\x18\n \x01(\x0b2\x16.google.protobuf.Value\x12\'\n\x07std_dev\x18\x0b \x01(\x0b2\x16.google.protobuf.ValueB\r\n\x0banchor_diff"D\n\x10SubmissionColumn\x120\n\x10submission_price\x18\x01 \x01(\x0b2\x16.google.protobuf.Value"\xc0\x03\n\x1aSubmissionStatisticsColumn\x123\n\x13submission_evidence\x18\x01 \x01(\x0b2\x16.google.protobuf.Value\x12:\n\x1aabs_diff_from_sub_evidence\x18\x02 \x01(\x0b2\x16.google.protobuf.Value\x12.\n\x0esub_price_diff\x18\x03 \x01(\x0b2\x16.google.protobuf.Value\x12:\n\x1aabs_diff_from_latest_trade\x18\x04 \x01(\x0b2\x16.google.protobuf.Value\x12.\n\x0elower_boundary\x18\x05 \x01(\x0b2\x16.google.protobuf.Value\x12.\n\x0eupper_boundary\x18\x06 \x01(\x0b2\x16.google.protobuf.Value\x12<\n\x1cnumber_of_part_in_boundaries\x18\x07 \x01(\x0b2\x16.google.protobuf.Value\x12\'\n\x07std_dev\x18\x08 \x01(\x0b2\x16.google.protobuf.Value"\x98\x03\n\x15SubmissionRangeColumn\x12$\n\x04mean\x18\x01 \x01(\x0b2\x16.google.protobuf.Value\x122\n\x12abs_diff_from_mean\x18\x02 \x01(\x0b2\x16.google.protobuf.Value\x12.\n\x0esub_price_diff\x18\x03 \x01(\x0b2\x16.google.protobuf.Value\x12?\n\x1fmean_abs_diff_from_latest_trade\x18\x04 \x01(\x0b2\x16.google.protobuf.Value\x12.\n\x0esubmission_min\x18\x05 \x01(\x0b2\x16.google.protobuf.Value\x12.\n\x0esubmission_max\x18\x06 \x01(\x0b2\x16.google.protobuf.Value\x12+\n\x0bvalid_count\x18\x07 \x01(\x0b2\x16.google.protobuf.Value\x12\'\n\x07std_dev\x18\x08 \x01(\x0b2\x16.google.protobuf.Value"\xe4\x02\n\x10EvidentalPricing\x12#\n\x03mid\x18\x01 \x01(\x0b2\x16.google.protobuf.Value\x12#\n\x03bid\x18\x02 \x01(\x0b2\x16.google.protobuf.Value\x12#\n\x03ask\x18\x03 \x01(\x0b2\x16.google.protobuf.Value\x125\n\x15abs_diff_from_evp_mid\x18\x04 \x01(\x0b2\x16.google.protobuf.Value\x12.\n\x0esub_price_diff\x18\x05 \x01(\x0b2\x16.google.protobuf.Value\x12B\n"evp_mid_abs_diff_from_latest_trade\x18\x06 \x01(\x0b2\x16.google.protobuf.Value\x126\n\x16trades_or_orders_count\x18\t \x01(\x0b2\x16.google.protobuf.Value"\x8c\x03\n\x0fAvailableTrades\x122\n\x12latest_trade_price\x18\x01 \x01(\x0b2\x16.google.protobuf.Value\x12:\n\x1aabs_diff_from_latest_trade\x18\x02 \x01(\x0b2\x16.google.protobuf.Value\x12.\n\x0esub_price_diff\x18\x03 \x01(\x0b2\x16.google.protobuf.Value\x12D\n$sub_price_abs_diff_from_latest_trade\x18\x04 \x01(\x0b2\x16.google.protobuf.Value\x12#\n\x03min\x18\x05 \x01(\x0b2\x16.google.protobuf.Value\x12#\n\x03max\x18\x06 \x01(\x0b2\x16.google.protobuf.Value\x12\x16\n\x0edayTradeNumber\x18\x07 \x01(\x03\x12\x17\n\x0fweekTradeNumber\x18\x08 \x01(\x03\x12\x18\n\x10monthTradeNumber\x18\t \x01(\x03"\x8f\x02\n\x13ConsensusTabRequest\x12\x10\n\x08asset_id\x18\x01 \x01(\t\x12\x12\n\ntrace_name\x18\x02 \x01(\t\x12\x1f\n\x17consensus_run_timestamp\x18\x03 \x01(\t\x12(\n\tdata_type\x18\x05 \x01(\x0e2\x15.titanium.TabDataType\x12.\n\x0ctable_config\x18\x06 \x01(\x0b2\x16.titanium.TableRequestH\x00\x12?\n\x15collapse_table_config\x18\x07 \x01(\x0b2\x1e.titanium.CollapseTableRequestH\x00B\x16\n\x14search_configuration2\x9b\x10\n\x10ConsensusService\x12\x8b\x01\n\x13ConsensusTimestamps\x12$.titanium.ConsensusTimestampsRequest\x1a%.titanium.ConsensusTimestampsResponse"\'\x82\xd3\xe4\x93\x02!"\x1c/api/v1/consensus/timestamps:\x01*\x12b\n\tConsensus\x12\x1a.titanium.ConsensusRequest\x1a\x1b.titanium.ConsensusResponse"\x1c\x82\xd3\xe4\x93\x02\x16"\x11/api/v1/consensus:\x01*\x12a\n\x0eEvaluatedPrice\x12\x14.titanium.EVPRequest\x1a\x15.titanium.EVPResponse""\x82\xd3\xe4\x93\x02\x1c"\x17/api/v1/evaluated-price:\x01*\x12w\n\x11ConsensusOutliers\x12\x1d.titanium.OutliersListRequest\x1a!.titanium.ConsensusActiveResponse" \x82\xd3\xe4\x93\x02\x1a"\x15/api/v1/outliers-list:\x01*\x12\x81\x01\n\x10GetConsensusRuns\x12!.titanium.GetConsensusRunsRequest\x1a".titanium.GetConsensusRunsResponse"&\x82\xd3\xe4\x93\x02 "\x1b/api/v1/consensus-runs-view:\x01*\x12\xaa\x01\n"ConsensusExplorerInstrumentDetails\x12".titanium.ConsensusExplorerRequest\x1a4.titanium.ConsensusExplorerInstrumentDetailsResponse"*\x82\xd3\xe4\x93\x02$""/api/v1/consensus-explorer/details\x12\x90\x01\n\x16ConsensusExplorerTable\x12".titanium.ConsensusExplorerRequest\x1a(.titanium.ConsensusExplorerTableResponse"(\x82\xd3\xe4\x93\x02"" /api/v1/consensus-explorer/table\x12\x91\x01\n\x17ConsensusExplorerRanges\x12".titanium.ConsensusExplorerRequest\x1a(.titanium.ConsensusExplorerRangeResponse"(\x82\xd3\xe4\x93\x02"" /api/v1/consensus-explorer/range\x12\x8d\x01\n\x12CohortConsensusTab\x12\x1d.titanium.ConsensusTabRequest\x1a*.titanium.ConsensusResultSetValuesResponse",\x82\xd3\xe4\x93\x02&"!/api/v1/consensus-result-set-view:\x01*\x12\xa4\x01\n\x15SubmissionEvidenceTab\x12\x1d.titanium.ConsensusTabRequest\x1a*.titanium.ConsensusResultSetValuesResponse"@\x82\xd3\xe4\x93\x02:"5/api/v1/consensus-result-set-view/submission-evidence:\x01*\x12\x84\x01\n\x0fConsensusActive\x12 .titanium.ConsensusActiveRequest\x1a!.titanium.ConsensusActiveResponse",\x82\xd3\xe4\x93\x02&"!/api/v1/operator/consensus/active:\x01*\x12\x91\x01\n\x12ConsensusToPublish\x12#.titanium.ConsensusToPublishRequest\x1a$.titanium.ConsensusToPublishResponse"0\x82\xd3\xe4\x93\x02*"%/api/v1/operator/consensus/to-publish:\x01*\x12\x7f\n\x10ConsensusPublish\x12!.titanium.ConsensusPublishRequest\x1a\x19.titanium.MessageResponse"-\x82\xd3\xe4\x93\x02\'""/api/v1/operator/consensus/publish:\x01*\x12\x88\x01\n\x10ConsensusHistory\x12!.titanium.ConsensusHistoryRequest\x1a".titanium.ConsensusHistoryResponse"-\x82\xd3\xe4\x93\x02\'""/api/v1/operator/consensus/history:\x01*\x12\x82\x01\n\x11ConsensusDecision\x12".titanium.ConsensusDecisionRequest\x1a\x19.titanium.MessageResponse".\x82\xd3\xe4\x93\x02("#/api/v1/operator/consensus/decision:\x01*Bo\n com.peernova.titanium.interfacesB\x15ConsensusServiceProtoZ4github.com/peernova/clearconsensus-sdk/sdk/go/publicb\x06proto3')
_CONSENSUSEXPLORERREQUEST = DESCRIPTOR.message_types_by_name['ConsensusExplorerRequest']
_CONSENSUSEXPLORERINSTRUMENTDETAILSRESPONSE = DESCRIPTOR.message_types_by_name['ConsensusExplorerInstrumentDetailsResponse']
_CONSENSUSEXPLORERINSTRUMENTDETAILSDATA = DESCRIPTOR.message_types_by_name['ConsensusExplorerInstrumentDetailsData']
_INSTRUMENTSUBMISSIONSTATUS = DESCRIPTOR.message_types_by_name['InstrumentSubmissionStatus']
_DATEANDVALUE = DESCRIPTOR.message_types_by_name['DateAndValue']
_CONSENSUSSCORES = DESCRIPTOR.message_types_by_name['ConsensusScores']
_EXPERTISERANK = DESCRIPTOR.message_types_by_name['ExpertiseRank']
_EXPERTISERANKHISTORYELEMENT = DESCRIPTOR.message_types_by_name['ExpertiseRankHistoryElement']
_CONSENSUSDENSITYSCORE = DESCRIPTOR.message_types_by_name['ConsensusDensityScore']
_TRADEALIGNMENTSCORE = DESCRIPTOR.message_types_by_name['TradeAlignmentScore']
_TRADEALIGMENTDATEANDVALUE = DESCRIPTOR.message_types_by_name['TradeAligmentDateAndValue']
_EVPALIGNMENTSCORE = DESCRIPTOR.message_types_by_name['EvpAlignmentScore']
_BIMODALITY = DESCRIPTOR.message_types_by_name['Bimodality']
_EVPQUALITYSCORE = DESCRIPTOR.message_types_by_name['EvpQualityScore']
_CONSENSUSEXPLORERRANGERESPONSE = DESCRIPTOR.message_types_by_name['ConsensusExplorerRangeResponse']
_CONSENSUSEXPLORERRANGEDATA = DESCRIPTOR.message_types_by_name['ConsensusExplorerRangeData']
_CHARTRANGES = DESCRIPTOR.message_types_by_name['ChartRanges']
_COHORTCONSENSUSRANGETABDATA = DESCRIPTOR.message_types_by_name['CohortConsensusRangeTabData']
_TRADEANCHORDETAILS = DESCRIPTOR.message_types_by_name['TradeAnchorDetails']
_EVPANCHORDETAILS = DESCRIPTOR.message_types_by_name['EvpAnchorDetails']
_SUBMISSIONEVIDENCEANCHORDETAILS = DESCRIPTOR.message_types_by_name['SubmissionEvidenceAnchorDetails']
_TRADEPERIODSWITHMETRICS = DESCRIPTOR.message_types_by_name['TradePeriodsWithMetrics']
_TRADEPERIODMETRICS = DESCRIPTOR.message_types_by_name['TradePeriodMetrics']
_CONSENSUSEXPLORERTABLERESPONSE = DESCRIPTOR.message_types_by_name['ConsensusExplorerTableResponse']
_CONSENSUSEXPLORERTABLEDATA = DESCRIPTOR.message_types_by_name['ConsensusExplorerTableData']
_COMPARISONTABLE = DESCRIPTOR.message_types_by_name['ComparisonTable']
_CONSENSUSCOLUMN = DESCRIPTOR.message_types_by_name['ConsensusColumn']
_SUBMISSIONCOLUMN = DESCRIPTOR.message_types_by_name['SubmissionColumn']
_SUBMISSIONSTATISTICSCOLUMN = DESCRIPTOR.message_types_by_name['SubmissionStatisticsColumn']
_SUBMISSIONRANGECOLUMN = DESCRIPTOR.message_types_by_name['SubmissionRangeColumn']
_EVIDENTALPRICING = DESCRIPTOR.message_types_by_name['EvidentalPricing']
_AVAILABLETRADES = DESCRIPTOR.message_types_by_name['AvailableTrades']
_CONSENSUSTABREQUEST = DESCRIPTOR.message_types_by_name['ConsensusTabRequest']
ConsensusExplorerRequest = _reflection.GeneratedProtocolMessageType('ConsensusExplorerRequest', (_message.Message,), {'DESCRIPTOR': _CONSENSUSEXPLORERREQUEST, '__module__': 'public.consensus_service_pb2'})
_sym_db.RegisterMessage(ConsensusExplorerRequest)
ConsensusExplorerInstrumentDetailsResponse = _reflection.GeneratedProtocolMessageType('ConsensusExplorerInstrumentDetailsResponse', (_message.Message,), {'DESCRIPTOR': _CONSENSUSEXPLORERINSTRUMENTDETAILSRESPONSE, '__module__': 'public.consensus_service_pb2'})
_sym_db.RegisterMessage(ConsensusExplorerInstrumentDetailsResponse)
ConsensusExplorerInstrumentDetailsData = _reflection.GeneratedProtocolMessageType('ConsensusExplorerInstrumentDetailsData', (_message.Message,), {'DESCRIPTOR': _CONSENSUSEXPLORERINSTRUMENTDETAILSDATA, '__module__': 'public.consensus_service_pb2'})
_sym_db.RegisterMessage(ConsensusExplorerInstrumentDetailsData)
InstrumentSubmissionStatus = _reflection.GeneratedProtocolMessageType('InstrumentSubmissionStatus', (_message.Message,), {'DESCRIPTOR': _INSTRUMENTSUBMISSIONSTATUS, '__module__': 'public.consensus_service_pb2'})
_sym_db.RegisterMessage(InstrumentSubmissionStatus)
DateAndValue = _reflection.GeneratedProtocolMessageType('DateAndValue', (_message.Message,), {'DESCRIPTOR': _DATEANDVALUE, '__module__': 'public.consensus_service_pb2'})
_sym_db.RegisterMessage(DateAndValue)
ConsensusScores = _reflection.GeneratedProtocolMessageType('ConsensusScores', (_message.Message,), {'DESCRIPTOR': _CONSENSUSSCORES, '__module__': 'public.consensus_service_pb2'})
_sym_db.RegisterMessage(ConsensusScores)
ExpertiseRank = _reflection.GeneratedProtocolMessageType('ExpertiseRank', (_message.Message,), {'DESCRIPTOR': _EXPERTISERANK, '__module__': 'public.consensus_service_pb2'})
_sym_db.RegisterMessage(ExpertiseRank)
ExpertiseRankHistoryElement = _reflection.GeneratedProtocolMessageType('ExpertiseRankHistoryElement', (_message.Message,), {'DESCRIPTOR': _EXPERTISERANKHISTORYELEMENT, '__module__': 'public.consensus_service_pb2'})
_sym_db.RegisterMessage(ExpertiseRankHistoryElement)
ConsensusDensityScore = _reflection.GeneratedProtocolMessageType('ConsensusDensityScore', (_message.Message,), {'DESCRIPTOR': _CONSENSUSDENSITYSCORE, '__module__': 'public.consensus_service_pb2'})
_sym_db.RegisterMessage(ConsensusDensityScore)
TradeAlignmentScore = _reflection.GeneratedProtocolMessageType('TradeAlignmentScore', (_message.Message,), {'DESCRIPTOR': _TRADEALIGNMENTSCORE, '__module__': 'public.consensus_service_pb2'})
_sym_db.RegisterMessage(TradeAlignmentScore)
TradeAligmentDateAndValue = _reflection.GeneratedProtocolMessageType('TradeAligmentDateAndValue', (_message.Message,), {'DESCRIPTOR': _TRADEALIGMENTDATEANDVALUE, '__module__': 'public.consensus_service_pb2'})
_sym_db.RegisterMessage(TradeAligmentDateAndValue)
EvpAlignmentScore = _reflection.GeneratedProtocolMessageType('EvpAlignmentScore', (_message.Message,), {'DESCRIPTOR': _EVPALIGNMENTSCORE, '__module__': 'public.consensus_service_pb2'})
_sym_db.RegisterMessage(EvpAlignmentScore)
Bimodality = _reflection.GeneratedProtocolMessageType('Bimodality', (_message.Message,), {'DESCRIPTOR': _BIMODALITY, '__module__': 'public.consensus_service_pb2'})
_sym_db.RegisterMessage(Bimodality)
EvpQualityScore = _reflection.GeneratedProtocolMessageType('EvpQualityScore', (_message.Message,), {'DESCRIPTOR': _EVPQUALITYSCORE, '__module__': 'public.consensus_service_pb2'})
_sym_db.RegisterMessage(EvpQualityScore)
ConsensusExplorerRangeResponse = _reflection.GeneratedProtocolMessageType('ConsensusExplorerRangeResponse', (_message.Message,), {'DESCRIPTOR': _CONSENSUSEXPLORERRANGERESPONSE, '__module__': 'public.consensus_service_pb2'})
_sym_db.RegisterMessage(ConsensusExplorerRangeResponse)
ConsensusExplorerRangeData = _reflection.GeneratedProtocolMessageType('ConsensusExplorerRangeData', (_message.Message,), {'DESCRIPTOR': _CONSENSUSEXPLORERRANGEDATA, '__module__': 'public.consensus_service_pb2'})
_sym_db.RegisterMessage(ConsensusExplorerRangeData)
ChartRanges = _reflection.GeneratedProtocolMessageType('ChartRanges', (_message.Message,), {'DESCRIPTOR': _CHARTRANGES, '__module__': 'public.consensus_service_pb2'})
_sym_db.RegisterMessage(ChartRanges)
CohortConsensusRangeTabData = _reflection.GeneratedProtocolMessageType('CohortConsensusRangeTabData', (_message.Message,), {'DESCRIPTOR': _COHORTCONSENSUSRANGETABDATA, '__module__': 'public.consensus_service_pb2'})
_sym_db.RegisterMessage(CohortConsensusRangeTabData)
TradeAnchorDetails = _reflection.GeneratedProtocolMessageType('TradeAnchorDetails', (_message.Message,), {'DESCRIPTOR': _TRADEANCHORDETAILS, '__module__': 'public.consensus_service_pb2'})
_sym_db.RegisterMessage(TradeAnchorDetails)
EvpAnchorDetails = _reflection.GeneratedProtocolMessageType('EvpAnchorDetails', (_message.Message,), {'DESCRIPTOR': _EVPANCHORDETAILS, '__module__': 'public.consensus_service_pb2'})
_sym_db.RegisterMessage(EvpAnchorDetails)
SubmissionEvidenceAnchorDetails = _reflection.GeneratedProtocolMessageType('SubmissionEvidenceAnchorDetails', (_message.Message,), {'DESCRIPTOR': _SUBMISSIONEVIDENCEANCHORDETAILS, '__module__': 'public.consensus_service_pb2'})
_sym_db.RegisterMessage(SubmissionEvidenceAnchorDetails)
TradePeriodsWithMetrics = _reflection.GeneratedProtocolMessageType('TradePeriodsWithMetrics', (_message.Message,), {'DESCRIPTOR': _TRADEPERIODSWITHMETRICS, '__module__': 'public.consensus_service_pb2'})
_sym_db.RegisterMessage(TradePeriodsWithMetrics)
TradePeriodMetrics = _reflection.GeneratedProtocolMessageType('TradePeriodMetrics', (_message.Message,), {'DESCRIPTOR': _TRADEPERIODMETRICS, '__module__': 'public.consensus_service_pb2'})
_sym_db.RegisterMessage(TradePeriodMetrics)
ConsensusExplorerTableResponse = _reflection.GeneratedProtocolMessageType('ConsensusExplorerTableResponse', (_message.Message,), {'DESCRIPTOR': _CONSENSUSEXPLORERTABLERESPONSE, '__module__': 'public.consensus_service_pb2'})
_sym_db.RegisterMessage(ConsensusExplorerTableResponse)
ConsensusExplorerTableData = _reflection.GeneratedProtocolMessageType('ConsensusExplorerTableData', (_message.Message,), {'DESCRIPTOR': _CONSENSUSEXPLORERTABLEDATA, '__module__': 'public.consensus_service_pb2'})
_sym_db.RegisterMessage(ConsensusExplorerTableData)
ComparisonTable = _reflection.GeneratedProtocolMessageType('ComparisonTable', (_message.Message,), {'DESCRIPTOR': _COMPARISONTABLE, '__module__': 'public.consensus_service_pb2'})
_sym_db.RegisterMessage(ComparisonTable)
ConsensusColumn = _reflection.GeneratedProtocolMessageType('ConsensusColumn', (_message.Message,), {'DESCRIPTOR': _CONSENSUSCOLUMN, '__module__': 'public.consensus_service_pb2'})
_sym_db.RegisterMessage(ConsensusColumn)
SubmissionColumn = _reflection.GeneratedProtocolMessageType('SubmissionColumn', (_message.Message,), {'DESCRIPTOR': _SUBMISSIONCOLUMN, '__module__': 'public.consensus_service_pb2'})
_sym_db.RegisterMessage(SubmissionColumn)
SubmissionStatisticsColumn = _reflection.GeneratedProtocolMessageType('SubmissionStatisticsColumn', (_message.Message,), {'DESCRIPTOR': _SUBMISSIONSTATISTICSCOLUMN, '__module__': 'public.consensus_service_pb2'})
_sym_db.RegisterMessage(SubmissionStatisticsColumn)
SubmissionRangeColumn = _reflection.GeneratedProtocolMessageType('SubmissionRangeColumn', (_message.Message,), {'DESCRIPTOR': _SUBMISSIONRANGECOLUMN, '__module__': 'public.consensus_service_pb2'})
_sym_db.RegisterMessage(SubmissionRangeColumn)
EvidentalPricing = _reflection.GeneratedProtocolMessageType('EvidentalPricing', (_message.Message,), {'DESCRIPTOR': _EVIDENTALPRICING, '__module__': 'public.consensus_service_pb2'})
_sym_db.RegisterMessage(EvidentalPricing)
AvailableTrades = _reflection.GeneratedProtocolMessageType('AvailableTrades', (_message.Message,), {'DESCRIPTOR': _AVAILABLETRADES, '__module__': 'public.consensus_service_pb2'})
_sym_db.RegisterMessage(AvailableTrades)
ConsensusTabRequest = _reflection.GeneratedProtocolMessageType('ConsensusTabRequest', (_message.Message,), {'DESCRIPTOR': _CONSENSUSTABREQUEST, '__module__': 'public.consensus_service_pb2'})
_sym_db.RegisterMessage(ConsensusTabRequest)
_CONSENSUSSERVICE = DESCRIPTOR.services_by_name['ConsensusService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesB\x15ConsensusServiceProtoZ4github.com/peernova/clearconsensus-sdk/sdk/go/public'
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
    _CONSENSUSSERVICE.methods_by_name['ConsensusExplorerInstrumentDetails']._options = None
    _CONSENSUSSERVICE.methods_by_name['ConsensusExplorerInstrumentDetails']._serialized_options = b'\x82\xd3\xe4\x93\x02$""/api/v1/consensus-explorer/details'
    _CONSENSUSSERVICE.methods_by_name['ConsensusExplorerTable']._options = None
    _CONSENSUSSERVICE.methods_by_name['ConsensusExplorerTable']._serialized_options = b'\x82\xd3\xe4\x93\x02"" /api/v1/consensus-explorer/table'
    _CONSENSUSSERVICE.methods_by_name['ConsensusExplorerRanges']._options = None
    _CONSENSUSSERVICE.methods_by_name['ConsensusExplorerRanges']._serialized_options = b'\x82\xd3\xe4\x93\x02"" /api/v1/consensus-explorer/range'
    _CONSENSUSSERVICE.methods_by_name['CohortConsensusTab']._options = None
    _CONSENSUSSERVICE.methods_by_name['CohortConsensusTab']._serialized_options = b'\x82\xd3\xe4\x93\x02&"!/api/v1/consensus-result-set-view:\x01*'
    _CONSENSUSSERVICE.methods_by_name['SubmissionEvidenceTab']._options = None
    _CONSENSUSSERVICE.methods_by_name['SubmissionEvidenceTab']._serialized_options = b'\x82\xd3\xe4\x93\x02:"5/api/v1/consensus-result-set-view/submission-evidence:\x01*'
    _CONSENSUSSERVICE.methods_by_name['ConsensusActive']._options = None
    _CONSENSUSSERVICE.methods_by_name['ConsensusActive']._serialized_options = b'\x82\xd3\xe4\x93\x02&"!/api/v1/operator/consensus/active:\x01*'
    _CONSENSUSSERVICE.methods_by_name['ConsensusToPublish']._options = None
    _CONSENSUSSERVICE.methods_by_name['ConsensusToPublish']._serialized_options = b'\x82\xd3\xe4\x93\x02*"%/api/v1/operator/consensus/to-publish:\x01*'
    _CONSENSUSSERVICE.methods_by_name['ConsensusPublish']._options = None
    _CONSENSUSSERVICE.methods_by_name['ConsensusPublish']._serialized_options = b'\x82\xd3\xe4\x93\x02\'""/api/v1/operator/consensus/publish:\x01*'
    _CONSENSUSSERVICE.methods_by_name['ConsensusHistory']._options = None
    _CONSENSUSSERVICE.methods_by_name['ConsensusHistory']._serialized_options = b'\x82\xd3\xe4\x93\x02\'""/api/v1/operator/consensus/history:\x01*'
    _CONSENSUSSERVICE.methods_by_name['ConsensusDecision']._options = None
    _CONSENSUSSERVICE.methods_by_name['ConsensusDecision']._serialized_options = b'\x82\xd3\xe4\x93\x02("#/api/v1/operator/consensus/decision:\x01*'
    _CONSENSUSEXPLORERREQUEST._serialized_start = 175
    _CONSENSUSEXPLORERREQUEST._serialized_end = 371
    _CONSENSUSEXPLORERINSTRUMENTDETAILSRESPONSE._serialized_start = 374
    _CONSENSUSEXPLORERINSTRUMENTDETAILSRESPONSE._serialized_end = 530
    _CONSENSUSEXPLORERINSTRUMENTDETAILSDATA._serialized_start = 533
    _CONSENSUSEXPLORERINSTRUMENTDETAILSDATA._serialized_end = 777
    _INSTRUMENTSUBMISSIONSTATUS._serialized_start = 780
    _INSTRUMENTSUBMISSIONSTATUS._serialized_end = 1310
    _DATEANDVALUE._serialized_start = 1312
    _DATEANDVALUE._serialized_end = 1379
    _CONSENSUSSCORES._serialized_start = 1382
    _CONSENSUSSCORES._serialized_end = 1730
    _EXPERTISERANK._serialized_start = 1733
    _EXPERTISERANK._serialized_end = 2090
    _EXPERTISERANKHISTORYELEMENT._serialized_start = 2093
    _EXPERTISERANKHISTORYELEMENT._serialized_end = 2221
    _CONSENSUSDENSITYSCORE._serialized_start = 2224
    _CONSENSUSDENSITYSCORE._serialized_end = 2529
    _TRADEALIGNMENTSCORE._serialized_start = 2532
    _TRADEALIGNMENTSCORE._serialized_end = 2803
    _TRADEALIGMENTDATEANDVALUE._serialized_start = 2805
    _TRADEALIGMENTDATEANDVALUE._serialized_end = 2907
    _EVPALIGNMENTSCORE._serialized_start = 2910
    _EVPALIGNMENTSCORE._serialized_end = 3168
    _BIMODALITY._serialized_start = 3170
    _BIMODALITY._serialized_end = 3288
    _EVPQUALITYSCORE._serialized_start = 3291
    _EVPQUALITYSCORE._serialized_end = 3456
    _CONSENSUSEXPLORERRANGERESPONSE._serialized_start = 3459
    _CONSENSUSEXPLORERRANGERESPONSE._serialized_end = 3591
    _CONSENSUSEXPLORERRANGEDATA._serialized_start = 3594
    _CONSENSUSEXPLORERRANGEDATA._serialized_end = 4135
    _CHARTRANGES._serialized_start = 4138
    _CHARTRANGES._serialized_end = 4416
    _COHORTCONSENSUSRANGETABDATA._serialized_start = 4419
    _COHORTCONSENSUSRANGETABDATA._serialized_end = 4973
    _TRADEANCHORDETAILS._serialized_start = 4976
    _TRADEANCHORDETAILS._serialized_end = 5158
    _EVPANCHORDETAILS._serialized_start = 5161
    _EVPANCHORDETAILS._serialized_end = 5295
    _SUBMISSIONEVIDENCEANCHORDETAILS._serialized_start = 5297
    _SUBMISSIONEVIDENCEANCHORDETAILS._serialized_end = 5390
    _TRADEPERIODSWITHMETRICS._serialized_start = 5393
    _TRADEPERIODSWITHMETRICS._serialized_end = 5565
    _TRADEPERIODMETRICS._serialized_start = 5568
    _TRADEPERIODMETRICS._serialized_end = 5710
    _CONSENSUSEXPLORERTABLERESPONSE._serialized_start = 5713
    _CONSENSUSEXPLORERTABLERESPONSE._serialized_end = 5845
    _CONSENSUSEXPLORERTABLEDATA._serialized_start = 5847
    _CONSENSUSEXPLORERTABLEDATA._serialized_end = 5928
    _COMPARISONTABLE._serialized_start = 5931
    _COMPARISONTABLE._serialized_end = 6295
    _CONSENSUSCOLUMN._serialized_start = 6298
    _CONSENSUSCOLUMN._serialized_end = 6941
    _SUBMISSIONCOLUMN._serialized_start = 6943
    _SUBMISSIONCOLUMN._serialized_end = 7011
    _SUBMISSIONSTATISTICSCOLUMN._serialized_start = 7014
    _SUBMISSIONSTATISTICSCOLUMN._serialized_end = 7462
    _SUBMISSIONRANGECOLUMN._serialized_start = 7465
    _SUBMISSIONRANGECOLUMN._serialized_end = 7873
    _EVIDENTALPRICING._serialized_start = 7876
    _EVIDENTALPRICING._serialized_end = 8232
    _AVAILABLETRADES._serialized_start = 8235
    _AVAILABLETRADES._serialized_end = 8631
    _CONSENSUSTABREQUEST._serialized_start = 8634
    _CONSENSUSTABREQUEST._serialized_end = 8905
    _CONSENSUSSERVICE._serialized_start = 8908
    _CONSENSUSSERVICE._serialized_end = 10983