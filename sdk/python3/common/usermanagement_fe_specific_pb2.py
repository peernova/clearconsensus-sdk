"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ..common import usermanagement_error_pb2 as common_dot_usermanagement__error__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'common/usermanagement_fe_specific.proto\x122com.peernova.titanium.casbin.management.grpc.proto\x1a!common/usermanagement_error.proto\x1a\x19google/protobuf/any.proto"\xb0\x02\n\x05Table\x12\x11\n\ttotalRows\x18\x01 \x01(\x03\x12Q\n\x07columns\x18\x02 \x03(\x0b2@.com.peernova.titanium.casbin.management.grpc.proto.Table.Column\x12K\n\x04rows\x18\x03 \x03(\x0b2=.com.peernova.titanium.casbin.management.grpc.proto.Table.Row\x1a]\n\x06Column\x12\x14\n\x0ccolumnDbType\x18\x01 \x01(\t\x12\x12\n\ncolumnName\x18\x02 \x01(\t\x12\x12\n\ncolumnType\x18\x03 \x01(\t\x12\x15\n\rrawColumnName\x18\x04 \x01(\t\x1a\x15\n\x03Row\x12\x0e\n\x06values\x18\x01 \x03(\t"\xa8\x02\n\x0eSearchCriteria\x12W\n\x05limit\x18\x01 \x01(\x0b2H.com.peernova.titanium.casbin.management.grpc.proto.SearchCriteria.Limit\x12\x0e\n\x06offset\x18\x02 \x01(\x05\x12[\n\x07orderBy\x18\x03 \x01(\x0b2J.com.peernova.titanium.casbin.management.grpc.proto.SearchCriteria.OrderBy\x12\x0e\n\x06filter\x18\x04 \x01(\t\x1a\x16\n\x05Limit\x12\r\n\x05value\x18\x01 \x01(\x05\x1a(\n\x07OrderBy\x12\x0e\n\x06column\x18\x01 \x01(\t\x12\r\n\x05order\x18\x02 \x01(\t"\x8f\x01\n\x0fServiceResponse\x12$\n\x04data\x18\x01 \x01(\x0b2\x14.google.protobuf.AnyH\x00\x12J\n\x05error\x18\x02 \x01(\x0b29.com.peernova.titanium.casbin.management.grpc.proto.ErrorH\x00B\n\n\x08responseBl\n2com.peernova.titanium.casbin.management.grpc.protoP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/commonb\x06proto3')
_TABLE = DESCRIPTOR.message_types_by_name['Table']
_TABLE_COLUMN = _TABLE.nested_types_by_name['Column']
_TABLE_ROW = _TABLE.nested_types_by_name['Row']
_SEARCHCRITERIA = DESCRIPTOR.message_types_by_name['SearchCriteria']
_SEARCHCRITERIA_LIMIT = _SEARCHCRITERIA.nested_types_by_name['Limit']
_SEARCHCRITERIA_ORDERBY = _SEARCHCRITERIA.nested_types_by_name['OrderBy']
_SERVICERESPONSE = DESCRIPTOR.message_types_by_name['ServiceResponse']
Table = _reflection.GeneratedProtocolMessageType('Table', (_message.Message,), {'Column': _reflection.GeneratedProtocolMessageType('Column', (_message.Message,), {'DESCRIPTOR': _TABLE_COLUMN, '__module__': 'common.usermanagement_fe_specific_pb2'}), 'Row': _reflection.GeneratedProtocolMessageType('Row', (_message.Message,), {'DESCRIPTOR': _TABLE_ROW, '__module__': 'common.usermanagement_fe_specific_pb2'}), 'DESCRIPTOR': _TABLE, '__module__': 'common.usermanagement_fe_specific_pb2'})
_sym_db.RegisterMessage(Table)
_sym_db.RegisterMessage(Table.Column)
_sym_db.RegisterMessage(Table.Row)
SearchCriteria = _reflection.GeneratedProtocolMessageType('SearchCriteria', (_message.Message,), {'Limit': _reflection.GeneratedProtocolMessageType('Limit', (_message.Message,), {'DESCRIPTOR': _SEARCHCRITERIA_LIMIT, '__module__': 'common.usermanagement_fe_specific_pb2'}), 'OrderBy': _reflection.GeneratedProtocolMessageType('OrderBy', (_message.Message,), {'DESCRIPTOR': _SEARCHCRITERIA_ORDERBY, '__module__': 'common.usermanagement_fe_specific_pb2'}), 'DESCRIPTOR': _SEARCHCRITERIA, '__module__': 'common.usermanagement_fe_specific_pb2'})
_sym_db.RegisterMessage(SearchCriteria)
_sym_db.RegisterMessage(SearchCriteria.Limit)
_sym_db.RegisterMessage(SearchCriteria.OrderBy)
ServiceResponse = _reflection.GeneratedProtocolMessageType('ServiceResponse', (_message.Message,), {'DESCRIPTOR': _SERVICERESPONSE, '__module__': 'common.usermanagement_fe_specific_pb2'})
_sym_db.RegisterMessage(ServiceResponse)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n2com.peernova.titanium.casbin.management.grpc.protoP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/common'
    _TABLE._serialized_start = 158
    _TABLE._serialized_end = 462
    _TABLE_COLUMN._serialized_start = 346
    _TABLE_COLUMN._serialized_end = 439
    _TABLE_ROW._serialized_start = 441
    _TABLE_ROW._serialized_end = 462
    _SEARCHCRITERIA._serialized_start = 465
    _SEARCHCRITERIA._serialized_end = 761
    _SEARCHCRITERIA_LIMIT._serialized_start = 697
    _SEARCHCRITERIA_LIMIT._serialized_end = 719
    _SEARCHCRITERIA_ORDERBY._serialized_start = 721
    _SEARCHCRITERIA_ORDERBY._serialized_end = 761
    _SERVICERESPONSE._serialized_start = 764
    _SERVICERESPONSE._serialized_end = 907