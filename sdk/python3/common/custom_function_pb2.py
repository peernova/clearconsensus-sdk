"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ..common import gateway_base_pb2 as common_dot_gateway__base__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ccommon/custom_function.proto\x12\x08titanium\x1a\x19common/gateway_base.proto"\xdc\x01\n\x18CustomFunctionIdentifier\x12\x0b\n\x03uid\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12F\n\x0boutput_type\x18\x03 \x01(\x0e21.titanium.CustomFunctionIdentifier.FunctionOutput\x12\r\n\x05scope\x18\x04 \x01(\t"N\n\x0eFunctionOutput\x12\x0b\n\x07NO_TYPE\x10\x00\x12\n\n\x06NUMBER\x10\x01\x12\n\n\x06STRING\x10\x02\x12\x08\n\x04DATE\x10\x03\x12\r\n\tTIMESTAMP\x10\x04"\xdf\x01\n\x13CustomFunctionUsage\x12(\n\nidentifier\x18\x01 \x01(\x0b2\x14.titanium.Identifier\x125\n\x04type\x18\x02 \x01(\x0e2\'.titanium.CustomFunctionUsage.UsageType"g\n\tUsageType\x12\x12\n\x0eCUSTOMFUNCTION\x10\x00\x12\x16\n\x12VALIDATION_RULESET\x10\x01\x12\x19\n\x15NORMALIZATION_RULESET\x10\x02\x12\x13\n\x0fMAPPING_RULESET\x10\x03"\x84\x03\n\x0eCustomFunction\x12\x0b\n\x03uid\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12<\n\x0boutput_type\x18\x03 \x01(\x0e2\'.titanium.CustomFunction.FunctionOutput\x12\x17\n\x0fdescriptor_name\x18\x04 \x01(\t\x12\x12\n\ndefinition\x18\x05 \x01(\t\x12\x10\n\x08category\x18\x06 \x01(\t\x12-\n\x06usages\x18\x07 \x03(\x0b2\x1d.titanium.CustomFunctionUsage\x12\r\n\x05scope\x18\x08 \x01(\t\x12?\n\x0fdescriptor_type\x18\t \x01(\x0e2&.titanium.CustomFunctionDescriptorType"[\n\x0eFunctionOutput\x12\x0b\n\x07NO_TYPE\x10\x00\x12\n\n\x06NUMBER\x10\x01\x12\n\n\x06STRING\x10\x02\x12\x08\n\x04DATE\x10\x03\x12\r\n\tTIMESTAMP\x10\x04\x12\x0b\n\x07BOOLEAN\x10\x05"\x89\x01\n\x1bCustomFunctionGetDefinition\x12)\n\x08id_scope\x18\x01 \x01(\x0b2\x17.titanium.GetDefinition\x12?\n\x0fdescriptor_type\x18\x02 \x01(\x0e2&.titanium.CustomFunctionDescriptorType"?\n\x12CustomFunctionList\x12)\n\x07results\x18\x01 \x03(\x0b2\x18.titanium.CustomFunction"\x9d\x01\n\x19ListCustomFunctionRequest\x12&\n\x07request\x18\x01 \x01(\x0b2\x15.titanium.ListRequest\x12\x17\n\x0fdescriptor_name\x18\x02 \x01(\t\x12?\n\x0fdescriptor_type\x18\x03 \x01(\x0e2&.titanium.CustomFunctionDescriptorType"x\n\x1aListCustomFunctionResponse\x12,\n\x04data\x18\x01 \x01(\x0b2\x1c.titanium.CustomFunctionListH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response"m\n\x18CustomFunctionDefinition\x12\x0b\n\x03uid\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x12\n\ndefinition\x18\x03 \x01(\t\x12\r\n\x05scope\x18\x04 \x01(\t\x12\x13\n\x0bdescription\x18\x05 \x01(\t"z\n CustomFunctionDefinitionResponse\x12(\n\x04data\x18\x01 \x01(\x0b2\x18.titanium.CustomFunctionH\x00\x12 \n\x05error\x18\x02 \x01(\x0b2\x0f.titanium.ErrorH\x00B\n\n\x08response*\x80\x01\n\x1cCustomFunctionDescriptorType\x12\x0b\n\x07NO_TYPE\x10\x00\x12\x0e\n\nDESCRIPTOR\x10\x01\x12\x10\n\x0cDBDESCRIPTOR\x10\x02\x12\x0b\n\x07no_type\x10\x00\x12\x0e\n\ndescriptor\x10\x01\x12\x10\n\x0cdbdescriptor\x10\x02\x1a\x02\x10\x01B|\n com.peernova.titanium.interfacesB CustomFunctionServiceProtoCommonP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/commonb\x06proto3')
_CUSTOMFUNCTIONDESCRIPTORTYPE = DESCRIPTOR.enum_types_by_name['CustomFunctionDescriptorType']
CustomFunctionDescriptorType = enum_type_wrapper.EnumTypeWrapper(_CUSTOMFUNCTIONDESCRIPTORTYPE)
NO_TYPE = 0
DESCRIPTOR = 1
DBDESCRIPTOR = 2
no_type = 0
descriptor = 1
dbdescriptor = 2
_CUSTOMFUNCTIONIDENTIFIER = DESCRIPTOR.message_types_by_name['CustomFunctionIdentifier']
_CUSTOMFUNCTIONUSAGE = DESCRIPTOR.message_types_by_name['CustomFunctionUsage']
_CUSTOMFUNCTION = DESCRIPTOR.message_types_by_name['CustomFunction']
_CUSTOMFUNCTIONGETDEFINITION = DESCRIPTOR.message_types_by_name['CustomFunctionGetDefinition']
_CUSTOMFUNCTIONLIST = DESCRIPTOR.message_types_by_name['CustomFunctionList']
_LISTCUSTOMFUNCTIONREQUEST = DESCRIPTOR.message_types_by_name['ListCustomFunctionRequest']
_LISTCUSTOMFUNCTIONRESPONSE = DESCRIPTOR.message_types_by_name['ListCustomFunctionResponse']
_CUSTOMFUNCTIONDEFINITION = DESCRIPTOR.message_types_by_name['CustomFunctionDefinition']
_CUSTOMFUNCTIONDEFINITIONRESPONSE = DESCRIPTOR.message_types_by_name['CustomFunctionDefinitionResponse']
_CUSTOMFUNCTIONIDENTIFIER_FUNCTIONOUTPUT = _CUSTOMFUNCTIONIDENTIFIER.enum_types_by_name['FunctionOutput']
_CUSTOMFUNCTIONUSAGE_USAGETYPE = _CUSTOMFUNCTIONUSAGE.enum_types_by_name['UsageType']
_CUSTOMFUNCTION_FUNCTIONOUTPUT = _CUSTOMFUNCTION.enum_types_by_name['FunctionOutput']
CustomFunctionIdentifier = _reflection.GeneratedProtocolMessageType('CustomFunctionIdentifier', (_message.Message,), {'DESCRIPTOR': _CUSTOMFUNCTIONIDENTIFIER, '__module__': 'common.custom_function_pb2'})
_sym_db.RegisterMessage(CustomFunctionIdentifier)
CustomFunctionUsage = _reflection.GeneratedProtocolMessageType('CustomFunctionUsage', (_message.Message,), {'DESCRIPTOR': _CUSTOMFUNCTIONUSAGE, '__module__': 'common.custom_function_pb2'})
_sym_db.RegisterMessage(CustomFunctionUsage)
CustomFunction = _reflection.GeneratedProtocolMessageType('CustomFunction', (_message.Message,), {'DESCRIPTOR': _CUSTOMFUNCTION, '__module__': 'common.custom_function_pb2'})
_sym_db.RegisterMessage(CustomFunction)
CustomFunctionGetDefinition = _reflection.GeneratedProtocolMessageType('CustomFunctionGetDefinition', (_message.Message,), {'DESCRIPTOR': _CUSTOMFUNCTIONGETDEFINITION, '__module__': 'common.custom_function_pb2'})
_sym_db.RegisterMessage(CustomFunctionGetDefinition)
CustomFunctionList = _reflection.GeneratedProtocolMessageType('CustomFunctionList', (_message.Message,), {'DESCRIPTOR': _CUSTOMFUNCTIONLIST, '__module__': 'common.custom_function_pb2'})
_sym_db.RegisterMessage(CustomFunctionList)
ListCustomFunctionRequest = _reflection.GeneratedProtocolMessageType('ListCustomFunctionRequest', (_message.Message,), {'DESCRIPTOR': _LISTCUSTOMFUNCTIONREQUEST, '__module__': 'common.custom_function_pb2'})
_sym_db.RegisterMessage(ListCustomFunctionRequest)
ListCustomFunctionResponse = _reflection.GeneratedProtocolMessageType('ListCustomFunctionResponse', (_message.Message,), {'DESCRIPTOR': _LISTCUSTOMFUNCTIONRESPONSE, '__module__': 'common.custom_function_pb2'})
_sym_db.RegisterMessage(ListCustomFunctionResponse)
CustomFunctionDefinition = _reflection.GeneratedProtocolMessageType('CustomFunctionDefinition', (_message.Message,), {'DESCRIPTOR': _CUSTOMFUNCTIONDEFINITION, '__module__': 'common.custom_function_pb2'})
_sym_db.RegisterMessage(CustomFunctionDefinition)
CustomFunctionDefinitionResponse = _reflection.GeneratedProtocolMessageType('CustomFunctionDefinitionResponse', (_message.Message,), {'DESCRIPTOR': _CUSTOMFUNCTIONDEFINITIONRESPONSE, '__module__': 'common.custom_function_pb2'})
_sym_db.RegisterMessage(CustomFunctionDefinitionResponse)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesB CustomFunctionServiceProtoCommonP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/common'
    _CUSTOMFUNCTIONDESCRIPTORTYPE._options = None
    _CUSTOMFUNCTIONDESCRIPTORTYPE._serialized_options = b'\x10\x01'
    _CUSTOMFUNCTIONDESCRIPTORTYPE._serialized_start = 1632
    _CUSTOMFUNCTIONDESCRIPTORTYPE._serialized_end = 1760
    _CUSTOMFUNCTIONIDENTIFIER._serialized_start = 70
    _CUSTOMFUNCTIONIDENTIFIER._serialized_end = 290
    _CUSTOMFUNCTIONIDENTIFIER_FUNCTIONOUTPUT._serialized_start = 212
    _CUSTOMFUNCTIONIDENTIFIER_FUNCTIONOUTPUT._serialized_end = 290
    _CUSTOMFUNCTIONUSAGE._serialized_start = 293
    _CUSTOMFUNCTIONUSAGE._serialized_end = 516
    _CUSTOMFUNCTIONUSAGE_USAGETYPE._serialized_start = 413
    _CUSTOMFUNCTIONUSAGE_USAGETYPE._serialized_end = 516
    _CUSTOMFUNCTION._serialized_start = 519
    _CUSTOMFUNCTION._serialized_end = 907
    _CUSTOMFUNCTION_FUNCTIONOUTPUT._serialized_start = 816
    _CUSTOMFUNCTION_FUNCTIONOUTPUT._serialized_end = 907
    _CUSTOMFUNCTIONGETDEFINITION._serialized_start = 910
    _CUSTOMFUNCTIONGETDEFINITION._serialized_end = 1047
    _CUSTOMFUNCTIONLIST._serialized_start = 1049
    _CUSTOMFUNCTIONLIST._serialized_end = 1112
    _LISTCUSTOMFUNCTIONREQUEST._serialized_start = 1115
    _LISTCUSTOMFUNCTIONREQUEST._serialized_end = 1272
    _LISTCUSTOMFUNCTIONRESPONSE._serialized_start = 1274
    _LISTCUSTOMFUNCTIONRESPONSE._serialized_end = 1394
    _CUSTOMFUNCTIONDEFINITION._serialized_start = 1396
    _CUSTOMFUNCTIONDEFINITION._serialized_end = 1505
    _CUSTOMFUNCTIONDEFINITIONRESPONSE._serialized_start = 1507
    _CUSTOMFUNCTIONDEFINITIONRESPONSE._serialized_end = 1629