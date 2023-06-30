"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19common/gateway_base.proto\x12\x08titanium\x1a\x1cgoogle/protobuf/struct.proto"&\n\x05Error\x12\x0c\n\x04code\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t"\'\n\nIdentifier\x12\x0b\n\x03uid\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t"a\n\rGetDefinition\x12(\n\nidentifier\x18\x01 \x01(\x0b2\x14.titanium.Identifier\x12\r\n\x05scope\x18\x02 \x01(\t\x12\x17\n\x0fdescriptor_name\x18\x03 \x01(\t"\x16\n\x05Limit\x12\r\n\x05value\x18\x01 \x01(\x05"9\n\x07OrderBy\x12\x0e\n\x06column\x18\x01 \x01(\t\x12\x1e\n\x05order\x18\x02 \x01(\x0e2\x0f.titanium.Order"\x80\x01\n\x0bListRequest\x12\r\n\x05scope\x18\x01 \x01(\t\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12"\n\x07orderBy\x18\x03 \x01(\x0b2\x11.titanium.OrderBy\x12\x1e\n\x05limit\x18\x04 \x01(\x0b2\x0f.titanium.Limit\x12\x0e\n\x06offset\x18\x05 \x01(\x05"i\n\x13AcknowledgeResponse\x12$\n\x04data\x18\x01 \x01(\x0b2\x14.titanium.IdentifierH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"1\n\x07Version\x12\x12\n\nversion_id\x18\x01 \x01(\t\x12\x12\n\ncreated_at\x18\x02 \x01(\t"2\n\x0bVersionList\x12#\n\x08versions\x18\x01 \x03(\x0b2\x11.titanium.Version"j\n\x13ListVersionResponse\x12%\n\x04data\x18\x01 \x01(\x0b2\x15.titanium.VersionListH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"Z\n\x0eVersionRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nversion_id\x18\x02 \x01(\t\x12\r\n\x05scope\x18\x03 \x01(\t\x12\x17\n\x0fdescriptor_name\x18\x04 \x01(\t"x\n\x0fDescriptorField\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12(\n\x07options\x18\x03 \x01(\x0b2\x17.google.protobuf.Struct\x12\x10\n\x08nullable\x18\x04 \x01(\x08\x12\r\n\x05alias\x18\x05 \x01(\t"\x88\x01\n\x14DescriptorDefinition\x12\x0c\n\x04name\x18\x01 \x01(\t\x12)\n\x06fields\x18\x02 \x03(\x0b2\x19.titanium.DescriptorField\x12(\n\x07options\x18\x03 \x01(\x0b2\x17.google.protobuf.Struct\x12\r\n\x05scope\x18\x04 \x01(\t"n\n\x0fMessageResponse\x12-\n\x04data\x18\x01 \x01(\x0b2\x1d.titanium.MessageResponseDataH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"&\n\x13MessageResponseData\x12\x0f\n\x07message\x18\x01 \x01(\t"\x92\x01\n\x0eTransformation\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\rtarget_column\x18\x02 \x01(\t\x12\x15\n\rsource_column\x18\x03 \x01(\t\x12\x0c\n\x04rule\x18\x04 \x01(\t\x12!\n\x03lut\x18\x05 \x01(\x0b2\x14.titanium.DynamicLut\x12\x13\n\x0bdescription\x18\x06 \x01(\t"4\n\x0bResultsList\x12%\n\x07results\x18\x01 \x03(\x0b2\x14.titanium.Identifier"a\n\nColumnInfo\x12\x12\n\ncolumnName\x18\x01 \x01(\t\x12\x15\n\rrawColumnName\x18\x02 \x01(\t\x12\x12\n\ncolumnType\x18\x03 \x01(\t\x12\x14\n\x0ccolumnDbType\x18\x04 \x01(\t"v\n\x10ListRuleResponse\x124\n\x04data\x18\x01 \x01(\x0b2$.titanium.DescriptorBasedResultsListH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"R\n\x1aDescriptorBasedResultsList\x124\n\x07results\x18\x01 \x03(\x0b2#.titanium.DescriptorBasedIdentifier"A\n\x19DescriptorBasedIdentifier\x12\x0b\n\x03uid\x18\x01 \x01(\t\x12\x17\n\x0fdescriptor_name\x18\x02 \x01(\t"3\n\tValuesRow\x12&\n\x06values\x18\x01 \x03(\x0b2\x16.google.protobuf.Value"\x8a\x01\n\x0cResponseData\x12%\n\x07columns\x18\x01 \x03(\x0b2\x14.titanium.ColumnInfo\x12!\n\x04rows\x18\x02 \x03(\x0b2\x13.titanium.ValuesRow\x12\x1c\n\x04page\x18\x03 \x01(\x0b2\x0e.titanium.Page\x12\x12\n\ntotal_rows\x18\x04 \x01(\x05"l\n\x0eStatusResponse\x12,\n\x04data\x18\x01 \x01(\x0b2\x1c.titanium.StatusResponseDataH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"$\n\x12StatusResponseData\x12\x0e\n\x06status\x18\x01 \x01(\t"o\n\x17ConsensusActiveResponse\x12&\n\x04data\x18\x01 \x01(\x0b2\x16.titanium.ResponseDataH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"5\n\x10DataQualityError\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x10\n\x08severity\x18\x02 \x01(\x05"t\n\x0fConsensusDetail\x12\x14\n\x0cparse_status\x18\x01 \x01(\t\x12\x13\n\x0bhighest_sev\x18\x02 \x01(\t\x12\x1a\n\x12calculation_status\x18\x03 \x01(\t\x12\x1a\n\x12calculation_detail\x18\x04 \x01(\t"?\n\x11DataQualityErrors\x12*\n\x06errors\x18\x01 \x03(\x0b2\x1a.titanium.DataQualityError"(\n\x0cStringKeyVal\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0b\n\x03val\x18\x02 \x01(\t"2\n\x11BenchmarkMetadata\x12\r\n\x05tenor\x18\x01 \x01(\t\x12\x0e\n\x06reason\x18\x02 \x01(\t"0\n\x0fOutlierMetadata\x12\r\n\x05tenor\x18\x01 \x01(\t\x12\x0e\n\x06reason\x18\x02 \x01(\t"4\n\x06Fields\x12*\n\x0cgroupingKeys\x18\x01 \x03(\x0b2\x14.titanium.ColumnInfo">\n\x06Values\x12\x0c\n\x04type\x18\x01 \x01(\t\x12&\n\x06values\x18\x02 \x03(\x0b2\x16.google.protobuf.Value"#\n\x11UploadURLResponse\x12\x0e\n\x06s3_url\x18\x01 \x01(\t"N\n\x06Filter\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x10\n\x08operator\x18\x02 \x01(\t\x12%\n\x05value\x18\x03 \x01(\x0b2\x16.google.protobuf.Value"\x8b\x01\n\x10PredefinedFilter\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x10\n\x08operator\x18\x02 \x01(\t\x12%\n\x05value\x18\x03 \x01(\x0b2\x16.google.protobuf.Value\x12\x13\n\x0bresultCount\x18\x04 \x01(\x05\x12\x1c\n\x14predefinedValueLabel\x18\x05 \x01(\t",\n\rNameAliasPair\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05alias\x18\x02 \x01(\t"\x82\x01\n\x14GenericChartResponse\x12%\n\x07columns\x18\x01 \x03(\x0b2\x14.titanium.ColumnInfo\x12/\n\x04rows\x18\x02 \x03(\x0b2!.titanium.GenericChartResponseRow\x12\x12\n\ntotal_rows\x18\x03 \x01(\x05"A\n\x17GenericChartResponseRow\x12&\n\x06values\x18\x01 \x03(\x0b2\x16.google.protobuf.Value"3\n\x14EnableDisableRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05scope\x18\x02 \x01(\t"\xee\x01\n\x13OutliersListRequest\x12\x16\n\x0esubmitted_date\x18\x01 \x01(\t\x12\x14\n\x0csubmitted_id\x18\x02 \x01(\t\x12\x1f\n\x17consensus_run_timestamp\x18\x03 \x01(\t\x12\x10\n\x08asset_id\x18\x04 \x01(\t\x12\x0e\n\x06filter\x18\x05 \x01(\t\x12"\n\x07orderBy\x18\x06 \x01(\x0b2\x11.titanium.OrderBy\x12\x1e\n\x05limit\x18\x07 \x01(\x0b2\x0f.titanium.Limit\x12\x0e\n\x06offset\x18\x08 \x01(\x05\x12\x12\n\ntrace_name\x18\t \x01(\t"\\\n\x11RulesetDefinition\x12\x17\n\x0fdescriptor_name\x18\x01 \x01(\t\x12.\n\x08criteria\x18\x02 \x03(\x0b2\x1c.titanium.CriteriaDefinition"\x94\x01\n\x12CriteriaDefinition\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12\x0c\n\x04rule\x18\x03 \x01(\t\x12\x0c\n\x04tags\x18\x04 \x03(\t\x12\x10\n\x08metadata\x18\x05 \x03(\t\x12-\n\x0bvalidations\x18\x06 \x03(\x0b2\x18.titanium.RuleDefinition"\xab\x02\n\x0eRuleDefinition\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12\x0c\n\x04rule\x18\x03 \x01(\t\x124\n\trule_type\x18\x04 \x01(\x0e2!.titanium.RuleDefinition.RuleType\x12\x10\n\x08severity\x18\x05 \x01(\x05\x12\x0c\n\x04tags\x18\x06 \x03(\t\x12(\n\x05error\x18\x07 \x01(\x0b2\x19.titanium.ErrorDefinition\x12)\n\x0blookuptable\x18\x08 \x01(\x0b2\x14.titanium.DynamicLut\x12\x0e\n\x06filter\x18\t \x01(\t"-\n\x08RuleType\x12\x0e\n\nINPUT_DATA\x10\x00\x12\x11\n\rBUSINESS_DATA\x10\x01"8\n\x0fErrorDefinition\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x14\n\x0cmessage_args\x18\x02 \x03(\t"\xb2\x01\n\nDynamicLut\x12\x0b\n\x03key\x18\x01 \x03(\t\x12\r\n\x05value\x18\x02 \x01(\t\x121\n\x04type\x18\x03 \x01(\x0e2#.titanium.DynamicLut.DynamicLutType\x12\x0e\n\x06filter\x18\x04 \x01(\t"E\n\x0eDynamicLutType\x12\x0b\n\x07BOOLEAN\x10\x00\x12\n\n\x06STRING\x10\x01\x12\x0b\n\x07NUMERIC\x10\x02\x12\r\n\tTIMESTAMP\x10\x03"v\n\nFilterPack\x12!\n\x07filters\x18\x01 \x03(\x0b2\x10.titanium.Filter\x12\x19\n\x11logical_operation\x18\x02 \x01(\t\x12*\n\x0cfilter_packs\x18\x03 \x03(\x0b2\x14.titanium.FilterPack"\x9e\x01\n\x10ConsensusRunInfo\x12\x18\n\x10consensus_run_id\x18\x01 \x01(\t\x12\x0e\n\x06run_by\x18\x02 \x01(\t\x12\x1e\n\x16number_of_participants\x18\x03 \x01(\x05\x12@\n\x16consensusResultSetInfo\x18\x04 \x03(\x0b2 .titanium.ConsensusResultSetInfo"\xb8\x01\n\x16ConsensusResultSetInfo\x12\x1f\n\x17consensus_result_set_id\x18\x01 \x01(\t\x12\x1f\n\x17consensus_run_timestamp\x18\x02 \x01(\t\x12\x0e\n\x06status\x18\x03 \x01(\t\x12\x13\n\x0bdescription\x18\x04 \x01(\t\x12\x0c\n\x04type\x18\x05 \x01(\t\x12\x13\n\x0bcohort_name\x18\x06 \x01(\t\x12\x14\n\x0cdata_content\x18\x07 \x01(\t"K\n\x04Page\x12\x0c\n\x04size\x18\x01 \x01(\x05\x12\x13\n\x0bpage_number\x18\x02 \x01(\x05\x12 \n\x18total_number_of_elements\x18\x03 \x01(\x03"g\n\x10EntityDefinition\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05scope\x18\x02 \x01(\t\x12"\n\x04type\x18\x03 \x01(\x0e2\x14.titanium.EntityType\x12\x12\n\ndefinition\x18\x04 \x01(\t"o\n\x10EntityIdentifier\x12(\n\nidentifier\x18\x01 \x01(\x0b2\x14.titanium.Identifier\x12\r\n\x05scope\x18\x02 \x01(\t\x12"\n\x04type\x18\x03 \x01(\x0e2\x14.titanium.EntityType"1\n\nListOfKeys\x12#\n\x04list\x18\x01 \x03(\x0b2\x15.titanium.KeyAndValue"A\n\x0bKeyAndValue\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b2\x16.google.protobuf.Value*\x1a\n\x05Order\x12\x07\n\x03ASC\x10\x00\x12\x08\n\x04DESC\x10\x01*;\n\x08Decision\x12\x18\n\x14DECISION_UNSPECIFIED\x10\x00\x12\x0b\n\x07APPROVE\x10\x01\x12\x08\n\x04DENY\x10\x02*\x82\x01\n\nEntityType\x12\x1b\n\x17ADVANCED_TRANSFORM_RULE\x10\x00\x12\x15\n\x11VALIDATIONRULESET\x10\x01\x12\x18\n\x14NORMALIZATIONRULESET\x10\x02\x12\x12\n\x0eMAPPINGRULESET\x10\x03\x12\x12\n\x0eCUSTOMFUNCTION\x10\x04BZ\n com.peernova.titanium.interfacesP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/commonb\x06proto3')
_ORDER = DESCRIPTOR.enum_types_by_name['Order']
Order = enum_type_wrapper.EnumTypeWrapper(_ORDER)
_DECISION = DESCRIPTOR.enum_types_by_name['Decision']
Decision = enum_type_wrapper.EnumTypeWrapper(_DECISION)
_ENTITYTYPE = DESCRIPTOR.enum_types_by_name['EntityType']
EntityType = enum_type_wrapper.EnumTypeWrapper(_ENTITYTYPE)
ASC = 0
DESC = 1
DECISION_UNSPECIFIED = 0
APPROVE = 1
DENY = 2
ADVANCED_TRANSFORM_RULE = 0
VALIDATIONRULESET = 1
NORMALIZATIONRULESET = 2
MAPPINGRULESET = 3
CUSTOMFUNCTION = 4
_ERROR = DESCRIPTOR.message_types_by_name['Error']
_IDENTIFIER = DESCRIPTOR.message_types_by_name['Identifier']
_GETDEFINITION = DESCRIPTOR.message_types_by_name['GetDefinition']
_LIMIT = DESCRIPTOR.message_types_by_name['Limit']
_ORDERBY = DESCRIPTOR.message_types_by_name['OrderBy']
_LISTREQUEST = DESCRIPTOR.message_types_by_name['ListRequest']
_ACKNOWLEDGERESPONSE = DESCRIPTOR.message_types_by_name['AcknowledgeResponse']
_VERSION = DESCRIPTOR.message_types_by_name['Version']
_VERSIONLIST = DESCRIPTOR.message_types_by_name['VersionList']
_LISTVERSIONRESPONSE = DESCRIPTOR.message_types_by_name['ListVersionResponse']
_VERSIONREQUEST = DESCRIPTOR.message_types_by_name['VersionRequest']
_DESCRIPTORFIELD = DESCRIPTOR.message_types_by_name['DescriptorField']
_DESCRIPTORDEFINITION = DESCRIPTOR.message_types_by_name['DescriptorDefinition']
_MESSAGERESPONSE = DESCRIPTOR.message_types_by_name['MessageResponse']
_MESSAGERESPONSEDATA = DESCRIPTOR.message_types_by_name['MessageResponseData']
_TRANSFORMATION = DESCRIPTOR.message_types_by_name['Transformation']
_RESULTSLIST = DESCRIPTOR.message_types_by_name['ResultsList']
_COLUMNINFO = DESCRIPTOR.message_types_by_name['ColumnInfo']
_LISTRULERESPONSE = DESCRIPTOR.message_types_by_name['ListRuleResponse']
_DESCRIPTORBASEDRESULTSLIST = DESCRIPTOR.message_types_by_name['DescriptorBasedResultsList']
_DESCRIPTORBASEDIDENTIFIER = DESCRIPTOR.message_types_by_name['DescriptorBasedIdentifier']
_VALUESROW = DESCRIPTOR.message_types_by_name['ValuesRow']
_RESPONSEDATA = DESCRIPTOR.message_types_by_name['ResponseData']
_STATUSRESPONSE = DESCRIPTOR.message_types_by_name['StatusResponse']
_STATUSRESPONSEDATA = DESCRIPTOR.message_types_by_name['StatusResponseData']
_CONSENSUSACTIVERESPONSE = DESCRIPTOR.message_types_by_name['ConsensusActiveResponse']
_DATAQUALITYERROR = DESCRIPTOR.message_types_by_name['DataQualityError']
_CONSENSUSDETAIL = DESCRIPTOR.message_types_by_name['ConsensusDetail']
_DATAQUALITYERRORS = DESCRIPTOR.message_types_by_name['DataQualityErrors']
_STRINGKEYVAL = DESCRIPTOR.message_types_by_name['StringKeyVal']
_BENCHMARKMETADATA = DESCRIPTOR.message_types_by_name['BenchmarkMetadata']
_OUTLIERMETADATA = DESCRIPTOR.message_types_by_name['OutlierMetadata']
_FIELDS = DESCRIPTOR.message_types_by_name['Fields']
_VALUES = DESCRIPTOR.message_types_by_name['Values']
_UPLOADURLRESPONSE = DESCRIPTOR.message_types_by_name['UploadURLResponse']
_FILTER = DESCRIPTOR.message_types_by_name['Filter']
_PREDEFINEDFILTER = DESCRIPTOR.message_types_by_name['PredefinedFilter']
_NAMEALIASPAIR = DESCRIPTOR.message_types_by_name['NameAliasPair']
_GENERICCHARTRESPONSE = DESCRIPTOR.message_types_by_name['GenericChartResponse']
_GENERICCHARTRESPONSEROW = DESCRIPTOR.message_types_by_name['GenericChartResponseRow']
_ENABLEDISABLEREQUEST = DESCRIPTOR.message_types_by_name['EnableDisableRequest']
_OUTLIERSLISTREQUEST = DESCRIPTOR.message_types_by_name['OutliersListRequest']
_RULESETDEFINITION = DESCRIPTOR.message_types_by_name['RulesetDefinition']
_CRITERIADEFINITION = DESCRIPTOR.message_types_by_name['CriteriaDefinition']
_RULEDEFINITION = DESCRIPTOR.message_types_by_name['RuleDefinition']
_ERRORDEFINITION = DESCRIPTOR.message_types_by_name['ErrorDefinition']
_DYNAMICLUT = DESCRIPTOR.message_types_by_name['DynamicLut']
_FILTERPACK = DESCRIPTOR.message_types_by_name['FilterPack']
_CONSENSUSRUNINFO = DESCRIPTOR.message_types_by_name['ConsensusRunInfo']
_CONSENSUSRESULTSETINFO = DESCRIPTOR.message_types_by_name['ConsensusResultSetInfo']
_PAGE = DESCRIPTOR.message_types_by_name['Page']
_ENTITYDEFINITION = DESCRIPTOR.message_types_by_name['EntityDefinition']
_ENTITYIDENTIFIER = DESCRIPTOR.message_types_by_name['EntityIdentifier']
_LISTOFKEYS = DESCRIPTOR.message_types_by_name['ListOfKeys']
_KEYANDVALUE = DESCRIPTOR.message_types_by_name['KeyAndValue']
_RULEDEFINITION_RULETYPE = _RULEDEFINITION.enum_types_by_name['RuleType']
_DYNAMICLUT_DYNAMICLUTTYPE = _DYNAMICLUT.enum_types_by_name['DynamicLutType']
Error = _reflection.GeneratedProtocolMessageType('Error', (_message.Message,), {'DESCRIPTOR': _ERROR, '__module__': 'common.gateway_base_pb2'})
_sym_db.RegisterMessage(Error)
Identifier = _reflection.GeneratedProtocolMessageType('Identifier', (_message.Message,), {'DESCRIPTOR': _IDENTIFIER, '__module__': 'common.gateway_base_pb2'})
_sym_db.RegisterMessage(Identifier)
GetDefinition = _reflection.GeneratedProtocolMessageType('GetDefinition', (_message.Message,), {'DESCRIPTOR': _GETDEFINITION, '__module__': 'common.gateway_base_pb2'})
_sym_db.RegisterMessage(GetDefinition)
Limit = _reflection.GeneratedProtocolMessageType('Limit', (_message.Message,), {'DESCRIPTOR': _LIMIT, '__module__': 'common.gateway_base_pb2'})
_sym_db.RegisterMessage(Limit)
OrderBy = _reflection.GeneratedProtocolMessageType('OrderBy', (_message.Message,), {'DESCRIPTOR': _ORDERBY, '__module__': 'common.gateway_base_pb2'})
_sym_db.RegisterMessage(OrderBy)
ListRequest = _reflection.GeneratedProtocolMessageType('ListRequest', (_message.Message,), {'DESCRIPTOR': _LISTREQUEST, '__module__': 'common.gateway_base_pb2'})
_sym_db.RegisterMessage(ListRequest)
AcknowledgeResponse = _reflection.GeneratedProtocolMessageType('AcknowledgeResponse', (_message.Message,), {'DESCRIPTOR': _ACKNOWLEDGERESPONSE, '__module__': 'common.gateway_base_pb2'})
_sym_db.RegisterMessage(AcknowledgeResponse)
Version = _reflection.GeneratedProtocolMessageType('Version', (_message.Message,), {'DESCRIPTOR': _VERSION, '__module__': 'common.gateway_base_pb2'})
_sym_db.RegisterMessage(Version)
VersionList = _reflection.GeneratedProtocolMessageType('VersionList', (_message.Message,), {'DESCRIPTOR': _VERSIONLIST, '__module__': 'common.gateway_base_pb2'})
_sym_db.RegisterMessage(VersionList)
ListVersionResponse = _reflection.GeneratedProtocolMessageType('ListVersionResponse', (_message.Message,), {'DESCRIPTOR': _LISTVERSIONRESPONSE, '__module__': 'common.gateway_base_pb2'})
_sym_db.RegisterMessage(ListVersionResponse)
VersionRequest = _reflection.GeneratedProtocolMessageType('VersionRequest', (_message.Message,), {'DESCRIPTOR': _VERSIONREQUEST, '__module__': 'common.gateway_base_pb2'})
_sym_db.RegisterMessage(VersionRequest)
DescriptorField = _reflection.GeneratedProtocolMessageType('DescriptorField', (_message.Message,), {'DESCRIPTOR': _DESCRIPTORFIELD, '__module__': 'common.gateway_base_pb2'})
_sym_db.RegisterMessage(DescriptorField)
DescriptorDefinition = _reflection.GeneratedProtocolMessageType('DescriptorDefinition', (_message.Message,), {'DESCRIPTOR': _DESCRIPTORDEFINITION, '__module__': 'common.gateway_base_pb2'})
_sym_db.RegisterMessage(DescriptorDefinition)
MessageResponse = _reflection.GeneratedProtocolMessageType('MessageResponse', (_message.Message,), {'DESCRIPTOR': _MESSAGERESPONSE, '__module__': 'common.gateway_base_pb2'})
_sym_db.RegisterMessage(MessageResponse)
MessageResponseData = _reflection.GeneratedProtocolMessageType('MessageResponseData', (_message.Message,), {'DESCRIPTOR': _MESSAGERESPONSEDATA, '__module__': 'common.gateway_base_pb2'})
_sym_db.RegisterMessage(MessageResponseData)
Transformation = _reflection.GeneratedProtocolMessageType('Transformation', (_message.Message,), {'DESCRIPTOR': _TRANSFORMATION, '__module__': 'common.gateway_base_pb2'})
_sym_db.RegisterMessage(Transformation)
ResultsList = _reflection.GeneratedProtocolMessageType('ResultsList', (_message.Message,), {'DESCRIPTOR': _RESULTSLIST, '__module__': 'common.gateway_base_pb2'})
_sym_db.RegisterMessage(ResultsList)
ColumnInfo = _reflection.GeneratedProtocolMessageType('ColumnInfo', (_message.Message,), {'DESCRIPTOR': _COLUMNINFO, '__module__': 'common.gateway_base_pb2'})
_sym_db.RegisterMessage(ColumnInfo)
ListRuleResponse = _reflection.GeneratedProtocolMessageType('ListRuleResponse', (_message.Message,), {'DESCRIPTOR': _LISTRULERESPONSE, '__module__': 'common.gateway_base_pb2'})
_sym_db.RegisterMessage(ListRuleResponse)
DescriptorBasedResultsList = _reflection.GeneratedProtocolMessageType('DescriptorBasedResultsList', (_message.Message,), {'DESCRIPTOR': _DESCRIPTORBASEDRESULTSLIST, '__module__': 'common.gateway_base_pb2'})
_sym_db.RegisterMessage(DescriptorBasedResultsList)
DescriptorBasedIdentifier = _reflection.GeneratedProtocolMessageType('DescriptorBasedIdentifier', (_message.Message,), {'DESCRIPTOR': _DESCRIPTORBASEDIDENTIFIER, '__module__': 'common.gateway_base_pb2'})
_sym_db.RegisterMessage(DescriptorBasedIdentifier)
ValuesRow = _reflection.GeneratedProtocolMessageType('ValuesRow', (_message.Message,), {'DESCRIPTOR': _VALUESROW, '__module__': 'common.gateway_base_pb2'})
_sym_db.RegisterMessage(ValuesRow)
ResponseData = _reflection.GeneratedProtocolMessageType('ResponseData', (_message.Message,), {'DESCRIPTOR': _RESPONSEDATA, '__module__': 'common.gateway_base_pb2'})
_sym_db.RegisterMessage(ResponseData)
StatusResponse = _reflection.GeneratedProtocolMessageType('StatusResponse', (_message.Message,), {'DESCRIPTOR': _STATUSRESPONSE, '__module__': 'common.gateway_base_pb2'})
_sym_db.RegisterMessage(StatusResponse)
StatusResponseData = _reflection.GeneratedProtocolMessageType('StatusResponseData', (_message.Message,), {'DESCRIPTOR': _STATUSRESPONSEDATA, '__module__': 'common.gateway_base_pb2'})
_sym_db.RegisterMessage(StatusResponseData)
ConsensusActiveResponse = _reflection.GeneratedProtocolMessageType('ConsensusActiveResponse', (_message.Message,), {'DESCRIPTOR': _CONSENSUSACTIVERESPONSE, '__module__': 'common.gateway_base_pb2'})
_sym_db.RegisterMessage(ConsensusActiveResponse)
DataQualityError = _reflection.GeneratedProtocolMessageType('DataQualityError', (_message.Message,), {'DESCRIPTOR': _DATAQUALITYERROR, '__module__': 'common.gateway_base_pb2'})
_sym_db.RegisterMessage(DataQualityError)
ConsensusDetail = _reflection.GeneratedProtocolMessageType('ConsensusDetail', (_message.Message,), {'DESCRIPTOR': _CONSENSUSDETAIL, '__module__': 'common.gateway_base_pb2'})
_sym_db.RegisterMessage(ConsensusDetail)
DataQualityErrors = _reflection.GeneratedProtocolMessageType('DataQualityErrors', (_message.Message,), {'DESCRIPTOR': _DATAQUALITYERRORS, '__module__': 'common.gateway_base_pb2'})
_sym_db.RegisterMessage(DataQualityErrors)
StringKeyVal = _reflection.GeneratedProtocolMessageType('StringKeyVal', (_message.Message,), {'DESCRIPTOR': _STRINGKEYVAL, '__module__': 'common.gateway_base_pb2'})
_sym_db.RegisterMessage(StringKeyVal)
BenchmarkMetadata = _reflection.GeneratedProtocolMessageType('BenchmarkMetadata', (_message.Message,), {'DESCRIPTOR': _BENCHMARKMETADATA, '__module__': 'common.gateway_base_pb2'})
_sym_db.RegisterMessage(BenchmarkMetadata)
OutlierMetadata = _reflection.GeneratedProtocolMessageType('OutlierMetadata', (_message.Message,), {'DESCRIPTOR': _OUTLIERMETADATA, '__module__': 'common.gateway_base_pb2'})
_sym_db.RegisterMessage(OutlierMetadata)
Fields = _reflection.GeneratedProtocolMessageType('Fields', (_message.Message,), {'DESCRIPTOR': _FIELDS, '__module__': 'common.gateway_base_pb2'})
_sym_db.RegisterMessage(Fields)
Values = _reflection.GeneratedProtocolMessageType('Values', (_message.Message,), {'DESCRIPTOR': _VALUES, '__module__': 'common.gateway_base_pb2'})
_sym_db.RegisterMessage(Values)
UploadURLResponse = _reflection.GeneratedProtocolMessageType('UploadURLResponse', (_message.Message,), {'DESCRIPTOR': _UPLOADURLRESPONSE, '__module__': 'common.gateway_base_pb2'})
_sym_db.RegisterMessage(UploadURLResponse)
Filter = _reflection.GeneratedProtocolMessageType('Filter', (_message.Message,), {'DESCRIPTOR': _FILTER, '__module__': 'common.gateway_base_pb2'})
_sym_db.RegisterMessage(Filter)
PredefinedFilter = _reflection.GeneratedProtocolMessageType('PredefinedFilter', (_message.Message,), {'DESCRIPTOR': _PREDEFINEDFILTER, '__module__': 'common.gateway_base_pb2'})
_sym_db.RegisterMessage(PredefinedFilter)
NameAliasPair = _reflection.GeneratedProtocolMessageType('NameAliasPair', (_message.Message,), {'DESCRIPTOR': _NAMEALIASPAIR, '__module__': 'common.gateway_base_pb2'})
_sym_db.RegisterMessage(NameAliasPair)
GenericChartResponse = _reflection.GeneratedProtocolMessageType('GenericChartResponse', (_message.Message,), {'DESCRIPTOR': _GENERICCHARTRESPONSE, '__module__': 'common.gateway_base_pb2'})
_sym_db.RegisterMessage(GenericChartResponse)
GenericChartResponseRow = _reflection.GeneratedProtocolMessageType('GenericChartResponseRow', (_message.Message,), {'DESCRIPTOR': _GENERICCHARTRESPONSEROW, '__module__': 'common.gateway_base_pb2'})
_sym_db.RegisterMessage(GenericChartResponseRow)
EnableDisableRequest = _reflection.GeneratedProtocolMessageType('EnableDisableRequest', (_message.Message,), {'DESCRIPTOR': _ENABLEDISABLEREQUEST, '__module__': 'common.gateway_base_pb2'})
_sym_db.RegisterMessage(EnableDisableRequest)
OutliersListRequest = _reflection.GeneratedProtocolMessageType('OutliersListRequest', (_message.Message,), {'DESCRIPTOR': _OUTLIERSLISTREQUEST, '__module__': 'common.gateway_base_pb2'})
_sym_db.RegisterMessage(OutliersListRequest)
RulesetDefinition = _reflection.GeneratedProtocolMessageType('RulesetDefinition', (_message.Message,), {'DESCRIPTOR': _RULESETDEFINITION, '__module__': 'common.gateway_base_pb2'})
_sym_db.RegisterMessage(RulesetDefinition)
CriteriaDefinition = _reflection.GeneratedProtocolMessageType('CriteriaDefinition', (_message.Message,), {'DESCRIPTOR': _CRITERIADEFINITION, '__module__': 'common.gateway_base_pb2'})
_sym_db.RegisterMessage(CriteriaDefinition)
RuleDefinition = _reflection.GeneratedProtocolMessageType('RuleDefinition', (_message.Message,), {'DESCRIPTOR': _RULEDEFINITION, '__module__': 'common.gateway_base_pb2'})
_sym_db.RegisterMessage(RuleDefinition)
ErrorDefinition = _reflection.GeneratedProtocolMessageType('ErrorDefinition', (_message.Message,), {'DESCRIPTOR': _ERRORDEFINITION, '__module__': 'common.gateway_base_pb2'})
_sym_db.RegisterMessage(ErrorDefinition)
DynamicLut = _reflection.GeneratedProtocolMessageType('DynamicLut', (_message.Message,), {'DESCRIPTOR': _DYNAMICLUT, '__module__': 'common.gateway_base_pb2'})
_sym_db.RegisterMessage(DynamicLut)
FilterPack = _reflection.GeneratedProtocolMessageType('FilterPack', (_message.Message,), {'DESCRIPTOR': _FILTERPACK, '__module__': 'common.gateway_base_pb2'})
_sym_db.RegisterMessage(FilterPack)
ConsensusRunInfo = _reflection.GeneratedProtocolMessageType('ConsensusRunInfo', (_message.Message,), {'DESCRIPTOR': _CONSENSUSRUNINFO, '__module__': 'common.gateway_base_pb2'})
_sym_db.RegisterMessage(ConsensusRunInfo)
ConsensusResultSetInfo = _reflection.GeneratedProtocolMessageType('ConsensusResultSetInfo', (_message.Message,), {'DESCRIPTOR': _CONSENSUSRESULTSETINFO, '__module__': 'common.gateway_base_pb2'})
_sym_db.RegisterMessage(ConsensusResultSetInfo)
Page = _reflection.GeneratedProtocolMessageType('Page', (_message.Message,), {'DESCRIPTOR': _PAGE, '__module__': 'common.gateway_base_pb2'})
_sym_db.RegisterMessage(Page)
EntityDefinition = _reflection.GeneratedProtocolMessageType('EntityDefinition', (_message.Message,), {'DESCRIPTOR': _ENTITYDEFINITION, '__module__': 'common.gateway_base_pb2'})
_sym_db.RegisterMessage(EntityDefinition)
EntityIdentifier = _reflection.GeneratedProtocolMessageType('EntityIdentifier', (_message.Message,), {'DESCRIPTOR': _ENTITYIDENTIFIER, '__module__': 'common.gateway_base_pb2'})
_sym_db.RegisterMessage(EntityIdentifier)
ListOfKeys = _reflection.GeneratedProtocolMessageType('ListOfKeys', (_message.Message,), {'DESCRIPTOR': _LISTOFKEYS, '__module__': 'common.gateway_base_pb2'})
_sym_db.RegisterMessage(ListOfKeys)
KeyAndValue = _reflection.GeneratedProtocolMessageType('KeyAndValue', (_message.Message,), {'DESCRIPTOR': _KEYANDVALUE, '__module__': 'common.gateway_base_pb2'})
_sym_db.RegisterMessage(KeyAndValue)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/common'
    _ORDER._serialized_start = 5280
    _ORDER._serialized_end = 5306
    _DECISION._serialized_start = 5308
    _DECISION._serialized_end = 5367
    _ENTITYTYPE._serialized_start = 5370
    _ENTITYTYPE._serialized_end = 5500
    _ERROR._serialized_start = 69
    _ERROR._serialized_end = 107
    _IDENTIFIER._serialized_start = 109
    _IDENTIFIER._serialized_end = 148
    _GETDEFINITION._serialized_start = 150
    _GETDEFINITION._serialized_end = 247
    _LIMIT._serialized_start = 249
    _LIMIT._serialized_end = 271
    _ORDERBY._serialized_start = 273
    _ORDERBY._serialized_end = 330
    _LISTREQUEST._serialized_start = 333
    _LISTREQUEST._serialized_end = 461
    _ACKNOWLEDGERESPONSE._serialized_start = 463
    _ACKNOWLEDGERESPONSE._serialized_end = 568
    _VERSION._serialized_start = 570
    _VERSION._serialized_end = 619
    _VERSIONLIST._serialized_start = 621
    _VERSIONLIST._serialized_end = 671
    _LISTVERSIONRESPONSE._serialized_start = 673
    _LISTVERSIONRESPONSE._serialized_end = 779
    _VERSIONREQUEST._serialized_start = 781
    _VERSIONREQUEST._serialized_end = 871
    _DESCRIPTORFIELD._serialized_start = 873
    _DESCRIPTORFIELD._serialized_end = 993
    _DESCRIPTORDEFINITION._serialized_start = 996
    _DESCRIPTORDEFINITION._serialized_end = 1132
    _MESSAGERESPONSE._serialized_start = 1134
    _MESSAGERESPONSE._serialized_end = 1244
    _MESSAGERESPONSEDATA._serialized_start = 1246
    _MESSAGERESPONSEDATA._serialized_end = 1284
    _TRANSFORMATION._serialized_start = 1287
    _TRANSFORMATION._serialized_end = 1433
    _RESULTSLIST._serialized_start = 1435
    _RESULTSLIST._serialized_end = 1487
    _COLUMNINFO._serialized_start = 1489
    _COLUMNINFO._serialized_end = 1586
    _LISTRULERESPONSE._serialized_start = 1588
    _LISTRULERESPONSE._serialized_end = 1706
    _DESCRIPTORBASEDRESULTSLIST._serialized_start = 1708
    _DESCRIPTORBASEDRESULTSLIST._serialized_end = 1790
    _DESCRIPTORBASEDIDENTIFIER._serialized_start = 1792
    _DESCRIPTORBASEDIDENTIFIER._serialized_end = 1857
    _VALUESROW._serialized_start = 1859
    _VALUESROW._serialized_end = 1910
    _RESPONSEDATA._serialized_start = 1913
    _RESPONSEDATA._serialized_end = 2051
    _STATUSRESPONSE._serialized_start = 2053
    _STATUSRESPONSE._serialized_end = 2161
    _STATUSRESPONSEDATA._serialized_start = 2163
    _STATUSRESPONSEDATA._serialized_end = 2199
    _CONSENSUSACTIVERESPONSE._serialized_start = 2201
    _CONSENSUSACTIVERESPONSE._serialized_end = 2312
    _DATAQUALITYERROR._serialized_start = 2314
    _DATAQUALITYERROR._serialized_end = 2367
    _CONSENSUSDETAIL._serialized_start = 2369
    _CONSENSUSDETAIL._serialized_end = 2485
    _DATAQUALITYERRORS._serialized_start = 2487
    _DATAQUALITYERRORS._serialized_end = 2550
    _STRINGKEYVAL._serialized_start = 2552
    _STRINGKEYVAL._serialized_end = 2592
    _BENCHMARKMETADATA._serialized_start = 2594
    _BENCHMARKMETADATA._serialized_end = 2644
    _OUTLIERMETADATA._serialized_start = 2646
    _OUTLIERMETADATA._serialized_end = 2694
    _FIELDS._serialized_start = 2696
    _FIELDS._serialized_end = 2748
    _VALUES._serialized_start = 2750
    _VALUES._serialized_end = 2812
    _UPLOADURLRESPONSE._serialized_start = 2814
    _UPLOADURLRESPONSE._serialized_end = 2849
    _FILTER._serialized_start = 2851
    _FILTER._serialized_end = 2929
    _PREDEFINEDFILTER._serialized_start = 2932
    _PREDEFINEDFILTER._serialized_end = 3071
    _NAMEALIASPAIR._serialized_start = 3073
    _NAMEALIASPAIR._serialized_end = 3117
    _GENERICCHARTRESPONSE._serialized_start = 3120
    _GENERICCHARTRESPONSE._serialized_end = 3250
    _GENERICCHARTRESPONSEROW._serialized_start = 3252
    _GENERICCHARTRESPONSEROW._serialized_end = 3317
    _ENABLEDISABLEREQUEST._serialized_start = 3319
    _ENABLEDISABLEREQUEST._serialized_end = 3370
    _OUTLIERSLISTREQUEST._serialized_start = 3373
    _OUTLIERSLISTREQUEST._serialized_end = 3611
    _RULESETDEFINITION._serialized_start = 3613
    _RULESETDEFINITION._serialized_end = 3705
    _CRITERIADEFINITION._serialized_start = 3708
    _CRITERIADEFINITION._serialized_end = 3856
    _RULEDEFINITION._serialized_start = 3859
    _RULEDEFINITION._serialized_end = 4158
    _RULEDEFINITION_RULETYPE._serialized_start = 4113
    _RULEDEFINITION_RULETYPE._serialized_end = 4158
    _ERRORDEFINITION._serialized_start = 4160
    _ERRORDEFINITION._serialized_end = 4216
    _DYNAMICLUT._serialized_start = 4219
    _DYNAMICLUT._serialized_end = 4397
    _DYNAMICLUT_DYNAMICLUTTYPE._serialized_start = 4328
    _DYNAMICLUT_DYNAMICLUTTYPE._serialized_end = 4397
    _FILTERPACK._serialized_start = 4399
    _FILTERPACK._serialized_end = 4517
    _CONSENSUSRUNINFO._serialized_start = 4520
    _CONSENSUSRUNINFO._serialized_end = 4678
    _CONSENSUSRESULTSETINFO._serialized_start = 4681
    _CONSENSUSRESULTSETINFO._serialized_end = 4865
    _PAGE._serialized_start = 4867
    _PAGE._serialized_end = 4942
    _ENTITYDEFINITION._serialized_start = 4944
    _ENTITYDEFINITION._serialized_end = 5047
    _ENTITYIDENTIFIER._serialized_start = 5049
    _ENTITYIDENTIFIER._serialized_end = 5160
    _LISTOFKEYS._serialized_start = 5162
    _LISTOFKEYS._serialized_end = 5211
    _KEYANDVALUE._serialized_start = 5213
    _KEYANDVALUE._serialized_end = 5278