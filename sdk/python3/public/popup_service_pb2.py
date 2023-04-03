"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ..google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ..common import popup_pb2 as common_dot_popup__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1apublic/popup_service.proto\x12\x08titanium\x1a\x1cgoogle/api/annotations.proto\x1a\x12common/popup.proto2s\n\x0cPopUpService\x12c\n\tPopUpView\x12\x1a.titanium.PopUpViewRequest\x1a\x1b.titanium.PopUpViewResponse"\x1d\x82\xd3\xe4\x93\x02\x17"\x12/api/v1/popup-view:\x01*Bs\n com.peernova.titanium.interfacesB\x17PopUpServiceProtoPublicP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/publicb\x06proto3')
_POPUPSERVICE = DESCRIPTOR.services_by_name['PopUpService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.peernova.titanium.interfacesB\x17PopUpServiceProtoPublicP\x01Z4github.com/peernova/clearconsensus-sdk/sdk/go/public'
    _POPUPSERVICE.methods_by_name['PopUpView']._options = None
    _POPUPSERVICE.methods_by_name['PopUpView']._serialized_options = b'\x82\xd3\xe4\x93\x02\x17"\x12/api/v1/popup-view:\x01*'
    _POPUPSERVICE._serialized_start = 90
    _POPUPSERVICE._serialized_end = 205