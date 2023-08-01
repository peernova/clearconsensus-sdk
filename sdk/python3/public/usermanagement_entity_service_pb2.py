"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ..common import usermanagement_entity_pb2 as common_dot_usermanagement__entity__pb2
from ..common import usermanagement_fe_specific_pb2 as common_dot_usermanagement__fe__specific__pb2
from ..google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*public/usermanagement_entity_service.proto\x124com.peernova.titanium.casbin.management.grpc.service\x1a"common/usermanagement_entity.proto\x1a\'common/usermanagement_fe_specific.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1egoogle/protobuf/wrappers.proto2\xd3\x07\n\rEntityService\x12\xbf\x01\n\x06create\x12=.com.peernova.titanium.casbin.management.grpc.proto.EntityDto\x1aB.com.peernova.titanium.casbin.management.grpc.proto.EntityResponse"2\x82\xd3\xe4\x93\x02,"\'/api/v1/user-management/entities/create:\x01*\x12\xbd\x01\n\x06update\x12=.com.peernova.titanium.casbin.management.grpc.proto.EntityDto\x1aB.com.peernova.titanium.casbin.management.grpc.proto.EntityResponse"0\x82\xd3\xe4\x93\x02*\x1a%/api/v1/user-management/entities/{id}:\x01*\x12\xba\x01\n\x07getById\x12<.com.peernova.titanium.casbin.management.grpc.proto.EntityId\x1aB.com.peernova.titanium.casbin.management.grpc.proto.EntityResponse"-\x82\xd3\xe4\x93\x02\'\x12%/api/v1/user-management/entities/{id}\x12\xc5\x01\n\x11getAllEnabledOnly\x12@.com.peernova.titanium.casbin.management.grpc.proto.NoParameters\x1aD.com.peernova.titanium.casbin.management.grpc.proto.EntitiesResponse"(\x82\xd3\xe4\x93\x02"\x12 /api/v1/user-management/entities\x12\xba\x01\n\x04find\x12B.com.peernova.titanium.casbin.management.grpc.proto.SearchCriteria\x1aA.com.peernova.titanium.casbin.management.grpc.proto.TableResponse"+\x82\xd3\xe4\x93\x02%" /api/v1/user-management/entities:\x01*Bn\n4com.peernova.titanium.casbin.management.grpc.serviceP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/publicb\x06proto3')
_ENTITYSERVICE = DESCRIPTOR.services_by_name['EntityService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n4com.peernova.titanium.casbin.management.grpc.serviceP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/public'
    _ENTITYSERVICE.methods_by_name['create']._options = None
    _ENTITYSERVICE.methods_by_name['create']._serialized_options = b'\x82\xd3\xe4\x93\x02,"\'/api/v1/user-management/entities/create:\x01*'
    _ENTITYSERVICE.methods_by_name['update']._options = None
    _ENTITYSERVICE.methods_by_name['update']._serialized_options = b'\x82\xd3\xe4\x93\x02*\x1a%/api/v1/user-management/entities/{id}:\x01*'
    _ENTITYSERVICE.methods_by_name['getById']._options = None
    _ENTITYSERVICE.methods_by_name['getById']._serialized_options = b"\x82\xd3\xe4\x93\x02'\x12%/api/v1/user-management/entities/{id}"
    _ENTITYSERVICE.methods_by_name['getAllEnabledOnly']._options = None
    _ENTITYSERVICE.methods_by_name['getAllEnabledOnly']._serialized_options = b'\x82\xd3\xe4\x93\x02"\x12 /api/v1/user-management/entities'
    _ENTITYSERVICE.methods_by_name['find']._options = None
    _ENTITYSERVICE.methods_by_name['find']._serialized_options = b'\x82\xd3\xe4\x93\x02%" /api/v1/user-management/entities:\x01*'
    _ENTITYSERVICE._serialized_start = 240
    _ENTITYSERVICE._serialized_end = 1219