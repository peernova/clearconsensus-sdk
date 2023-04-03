// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.27.1
// 	protoc        v3.18.1
// source: common/validation_service.proto

package common

import (
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	reflect "reflect"
	sync "sync"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

// definition of validation rule
type ValidationRuleDefinition struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Uid            string             `protobuf:"bytes,1,opt,name=uid,proto3" json:"uid,omitempty"`
	Definition     *RulesetDefinition `protobuf:"bytes,3,opt,name=definition,proto3" json:"definition,omitempty"`
	Scope          string             `protobuf:"bytes,4,opt,name=scope,proto3" json:"scope,omitempty"`
	DescriptorName string             `protobuf:"bytes,5,opt,name=descriptor_name,json=descriptorName,proto3" json:"descriptor_name,omitempty"`
}

func (x *ValidationRuleDefinition) Reset() {
	*x = ValidationRuleDefinition{}
	if protoimpl.UnsafeEnabled {
		mi := &file_common_validation_service_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *ValidationRuleDefinition) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ValidationRuleDefinition) ProtoMessage() {}

func (x *ValidationRuleDefinition) ProtoReflect() protoreflect.Message {
	mi := &file_common_validation_service_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ValidationRuleDefinition.ProtoReflect.Descriptor instead.
func (*ValidationRuleDefinition) Descriptor() ([]byte, []int) {
	return file_common_validation_service_proto_rawDescGZIP(), []int{0}
}

func (x *ValidationRuleDefinition) GetUid() string {
	if x != nil {
		return x.Uid
	}
	return ""
}

func (x *ValidationRuleDefinition) GetDefinition() *RulesetDefinition {
	if x != nil {
		return x.Definition
	}
	return nil
}

func (x *ValidationRuleDefinition) GetScope() string {
	if x != nil {
		return x.Scope
	}
	return ""
}

func (x *ValidationRuleDefinition) GetDescriptorName() string {
	if x != nil {
		return x.DescriptorName
	}
	return ""
}

type GetValidationRuleResponse struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// Types that are assignable to Response:
	//
	//	*GetValidationRuleResponse_Data
	//	*GetValidationRuleResponse_Error
	Response isGetValidationRuleResponse_Response `protobuf_oneof:"response"`
}

func (x *GetValidationRuleResponse) Reset() {
	*x = GetValidationRuleResponse{}
	if protoimpl.UnsafeEnabled {
		mi := &file_common_validation_service_proto_msgTypes[1]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *GetValidationRuleResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GetValidationRuleResponse) ProtoMessage() {}

func (x *GetValidationRuleResponse) ProtoReflect() protoreflect.Message {
	mi := &file_common_validation_service_proto_msgTypes[1]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GetValidationRuleResponse.ProtoReflect.Descriptor instead.
func (*GetValidationRuleResponse) Descriptor() ([]byte, []int) {
	return file_common_validation_service_proto_rawDescGZIP(), []int{1}
}

func (m *GetValidationRuleResponse) GetResponse() isGetValidationRuleResponse_Response {
	if m != nil {
		return m.Response
	}
	return nil
}

func (x *GetValidationRuleResponse) GetData() *ValidationRuleDefinition {
	if x, ok := x.GetResponse().(*GetValidationRuleResponse_Data); ok {
		return x.Data
	}
	return nil
}

func (x *GetValidationRuleResponse) GetError() *Error {
	if x, ok := x.GetResponse().(*GetValidationRuleResponse_Error); ok {
		return x.Error
	}
	return nil
}

type isGetValidationRuleResponse_Response interface {
	isGetValidationRuleResponse_Response()
}

type GetValidationRuleResponse_Data struct {
	Data *ValidationRuleDefinition `protobuf:"bytes,1,opt,name=data,proto3,oneof"`
}

type GetValidationRuleResponse_Error struct {
	Error *Error `protobuf:"bytes,2,opt,name=error,proto3,oneof"`
}

func (*GetValidationRuleResponse_Data) isGetValidationRuleResponse_Response() {}

func (*GetValidationRuleResponse_Error) isGetValidationRuleResponse_Response() {}

type GetGeneratedValidationRuleResponse struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// Types that are assignable to Response:
	//
	//	*GetGeneratedValidationRuleResponse_Data
	//	*GetGeneratedValidationRuleResponse_Error
	Response isGetGeneratedValidationRuleResponse_Response `protobuf_oneof:"response"`
}

func (x *GetGeneratedValidationRuleResponse) Reset() {
	*x = GetGeneratedValidationRuleResponse{}
	if protoimpl.UnsafeEnabled {
		mi := &file_common_validation_service_proto_msgTypes[2]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *GetGeneratedValidationRuleResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GetGeneratedValidationRuleResponse) ProtoMessage() {}

func (x *GetGeneratedValidationRuleResponse) ProtoReflect() protoreflect.Message {
	mi := &file_common_validation_service_proto_msgTypes[2]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GetGeneratedValidationRuleResponse.ProtoReflect.Descriptor instead.
func (*GetGeneratedValidationRuleResponse) Descriptor() ([]byte, []int) {
	return file_common_validation_service_proto_rawDescGZIP(), []int{2}
}

func (m *GetGeneratedValidationRuleResponse) GetResponse() isGetGeneratedValidationRuleResponse_Response {
	if m != nil {
		return m.Response
	}
	return nil
}

func (x *GetGeneratedValidationRuleResponse) GetData() string {
	if x, ok := x.GetResponse().(*GetGeneratedValidationRuleResponse_Data); ok {
		return x.Data
	}
	return ""
}

func (x *GetGeneratedValidationRuleResponse) GetError() *Error {
	if x, ok := x.GetResponse().(*GetGeneratedValidationRuleResponse_Error); ok {
		return x.Error
	}
	return nil
}

type isGetGeneratedValidationRuleResponse_Response interface {
	isGetGeneratedValidationRuleResponse_Response()
}

type GetGeneratedValidationRuleResponse_Data struct {
	Data string `protobuf:"bytes,1,opt,name=data,proto3,oneof"`
}

type GetGeneratedValidationRuleResponse_Error struct {
	Error *Error `protobuf:"bytes,2,opt,name=error,proto3,oneof"`
}

func (*GetGeneratedValidationRuleResponse_Data) isGetGeneratedValidationRuleResponse_Response() {}

func (*GetGeneratedValidationRuleResponse_Error) isGetGeneratedValidationRuleResponse_Response() {}

// request to perform check using rdl.
type RdlCheckRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Rdl string `protobuf:"bytes,1,opt,name=rdl,proto3" json:"rdl,omitempty"`
}

func (x *RdlCheckRequest) Reset() {
	*x = RdlCheckRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_common_validation_service_proto_msgTypes[3]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *RdlCheckRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*RdlCheckRequest) ProtoMessage() {}

func (x *RdlCheckRequest) ProtoReflect() protoreflect.Message {
	mi := &file_common_validation_service_proto_msgTypes[3]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use RdlCheckRequest.ProtoReflect.Descriptor instead.
func (*RdlCheckRequest) Descriptor() ([]byte, []int) {
	return file_common_validation_service_proto_rawDescGZIP(), []int{3}
}

func (x *RdlCheckRequest) GetRdl() string {
	if x != nil {
		return x.Rdl
	}
	return ""
}

var File_common_validation_service_proto protoreflect.FileDescriptor

var file_common_validation_service_proto_rawDesc = []byte{
	0x0a, 0x1f, 0x63, 0x6f, 0x6d, 0x6d, 0x6f, 0x6e, 0x2f, 0x76, 0x61, 0x6c, 0x69, 0x64, 0x61, 0x74,
	0x69, 0x6f, 0x6e, 0x5f, 0x73, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74,
	0x6f, 0x12, 0x08, 0x74, 0x69, 0x74, 0x61, 0x6e, 0x69, 0x75, 0x6d, 0x1a, 0x19, 0x63, 0x6f, 0x6d,
	0x6d, 0x6f, 0x6e, 0x2f, 0x67, 0x61, 0x74, 0x65, 0x77, 0x61, 0x79, 0x5f, 0x62, 0x61, 0x73, 0x65,
	0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x22, 0xae, 0x01, 0x0a, 0x18, 0x56, 0x61, 0x6c, 0x69, 0x64,
	0x61, 0x74, 0x69, 0x6f, 0x6e, 0x52, 0x75, 0x6c, 0x65, 0x44, 0x65, 0x66, 0x69, 0x6e, 0x69, 0x74,
	0x69, 0x6f, 0x6e, 0x12, 0x10, 0x0a, 0x03, 0x75, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09,
	0x52, 0x03, 0x75, 0x69, 0x64, 0x12, 0x3b, 0x0a, 0x0a, 0x64, 0x65, 0x66, 0x69, 0x6e, 0x69, 0x74,
	0x69, 0x6f, 0x6e, 0x18, 0x03, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x1b, 0x2e, 0x74, 0x69, 0x74, 0x61,
	0x6e, 0x69, 0x75, 0x6d, 0x2e, 0x52, 0x75, 0x6c, 0x65, 0x73, 0x65, 0x74, 0x44, 0x65, 0x66, 0x69,
	0x6e, 0x69, 0x74, 0x69, 0x6f, 0x6e, 0x52, 0x0a, 0x64, 0x65, 0x66, 0x69, 0x6e, 0x69, 0x74, 0x69,
	0x6f, 0x6e, 0x12, 0x14, 0x0a, 0x05, 0x73, 0x63, 0x6f, 0x70, 0x65, 0x18, 0x04, 0x20, 0x01, 0x28,
	0x09, 0x52, 0x05, 0x73, 0x63, 0x6f, 0x70, 0x65, 0x12, 0x27, 0x0a, 0x0f, 0x64, 0x65, 0x73, 0x63,
	0x72, 0x69, 0x70, 0x74, 0x6f, 0x72, 0x5f, 0x6e, 0x61, 0x6d, 0x65, 0x18, 0x05, 0x20, 0x01, 0x28,
	0x09, 0x52, 0x0e, 0x64, 0x65, 0x73, 0x63, 0x72, 0x69, 0x70, 0x74, 0x6f, 0x72, 0x4e, 0x61, 0x6d,
	0x65, 0x4a, 0x04, 0x08, 0x02, 0x10, 0x03, 0x22, 0x8a, 0x01, 0x0a, 0x19, 0x47, 0x65, 0x74, 0x56,
	0x61, 0x6c, 0x69, 0x64, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x52, 0x75, 0x6c, 0x65, 0x52, 0x65, 0x73,
	0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x38, 0x0a, 0x04, 0x64, 0x61, 0x74, 0x61, 0x18, 0x01, 0x20,
	0x01, 0x28, 0x0b, 0x32, 0x22, 0x2e, 0x74, 0x69, 0x74, 0x61, 0x6e, 0x69, 0x75, 0x6d, 0x2e, 0x56,
	0x61, 0x6c, 0x69, 0x64, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x52, 0x75, 0x6c, 0x65, 0x44, 0x65, 0x66,
	0x69, 0x6e, 0x69, 0x74, 0x69, 0x6f, 0x6e, 0x48, 0x00, 0x52, 0x04, 0x64, 0x61, 0x74, 0x61, 0x12,
	0x27, 0x0a, 0x05, 0x65, 0x72, 0x72, 0x6f, 0x72, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x0f,
	0x2e, 0x74, 0x69, 0x74, 0x61, 0x6e, 0x69, 0x75, 0x6d, 0x2e, 0x45, 0x72, 0x72, 0x6f, 0x72, 0x48,
	0x00, 0x52, 0x05, 0x65, 0x72, 0x72, 0x6f, 0x72, 0x42, 0x0a, 0x0a, 0x08, 0x72, 0x65, 0x73, 0x70,
	0x6f, 0x6e, 0x73, 0x65, 0x22, 0x6f, 0x0a, 0x22, 0x47, 0x65, 0x74, 0x47, 0x65, 0x6e, 0x65, 0x72,
	0x61, 0x74, 0x65, 0x64, 0x56, 0x61, 0x6c, 0x69, 0x64, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x52, 0x75,
	0x6c, 0x65, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x14, 0x0a, 0x04, 0x64, 0x61,
	0x74, 0x61, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x48, 0x00, 0x52, 0x04, 0x64, 0x61, 0x74, 0x61,
	0x12, 0x27, 0x0a, 0x05, 0x65, 0x72, 0x72, 0x6f, 0x72, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0b, 0x32,
	0x0f, 0x2e, 0x74, 0x69, 0x74, 0x61, 0x6e, 0x69, 0x75, 0x6d, 0x2e, 0x45, 0x72, 0x72, 0x6f, 0x72,
	0x48, 0x00, 0x52, 0x05, 0x65, 0x72, 0x72, 0x6f, 0x72, 0x42, 0x0a, 0x0a, 0x08, 0x72, 0x65, 0x73,
	0x70, 0x6f, 0x6e, 0x73, 0x65, 0x22, 0x23, 0x0a, 0x0f, 0x52, 0x64, 0x6c, 0x43, 0x68, 0x65, 0x63,
	0x6b, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x12, 0x10, 0x0a, 0x03, 0x72, 0x64, 0x6c, 0x18,
	0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x03, 0x72, 0x64, 0x6c, 0x42, 0x78, 0x0a, 0x20, 0x63, 0x6f,
	0x6d, 0x2e, 0x70, 0x65, 0x65, 0x72, 0x6e, 0x6f, 0x76, 0x61, 0x2e, 0x74, 0x69, 0x74, 0x61, 0x6e,
	0x69, 0x75, 0x6d, 0x2e, 0x69, 0x6e, 0x74, 0x65, 0x72, 0x66, 0x61, 0x63, 0x65, 0x73, 0x42, 0x1c,
	0x56, 0x61, 0x6c, 0x69, 0x64, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x53, 0x65, 0x72, 0x76, 0x69, 0x63,
	0x65, 0x50, 0x72, 0x6f, 0x74, 0x6f, 0x43, 0x6f, 0x6d, 0x6d, 0x6f, 0x6e, 0x50, 0x01, 0x5a, 0x34,
	0x67, 0x69, 0x74, 0x68, 0x75, 0x62, 0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x70, 0x65, 0x65, 0x72, 0x6e,
	0x6f, 0x76, 0x61, 0x2f, 0x63, 0x6c, 0x65, 0x61, 0x72, 0x63, 0x6f, 0x6e, 0x73, 0x65, 0x6e, 0x73,
	0x75, 0x73, 0x2d, 0x73, 0x64, 0x6b, 0x2f, 0x73, 0x64, 0x6b, 0x2f, 0x67, 0x6f, 0x2f, 0x63, 0x6f,
	0x6d, 0x6d, 0x6f, 0x6e, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_common_validation_service_proto_rawDescOnce sync.Once
	file_common_validation_service_proto_rawDescData = file_common_validation_service_proto_rawDesc
)

func file_common_validation_service_proto_rawDescGZIP() []byte {
	file_common_validation_service_proto_rawDescOnce.Do(func() {
		file_common_validation_service_proto_rawDescData = protoimpl.X.CompressGZIP(file_common_validation_service_proto_rawDescData)
	})
	return file_common_validation_service_proto_rawDescData
}

var file_common_validation_service_proto_msgTypes = make([]protoimpl.MessageInfo, 4)
var file_common_validation_service_proto_goTypes = []interface{}{
	(*ValidationRuleDefinition)(nil),           // 0: titanium.ValidationRuleDefinition
	(*GetValidationRuleResponse)(nil),          // 1: titanium.GetValidationRuleResponse
	(*GetGeneratedValidationRuleResponse)(nil), // 2: titanium.GetGeneratedValidationRuleResponse
	(*RdlCheckRequest)(nil),                    // 3: titanium.RdlCheckRequest
	(*RulesetDefinition)(nil),                  // 4: titanium.RulesetDefinition
	(*Error)(nil),                              // 5: titanium.Error
}
var file_common_validation_service_proto_depIdxs = []int32{
	4, // 0: titanium.ValidationRuleDefinition.definition:type_name -> titanium.RulesetDefinition
	0, // 1: titanium.GetValidationRuleResponse.data:type_name -> titanium.ValidationRuleDefinition
	5, // 2: titanium.GetValidationRuleResponse.error:type_name -> titanium.Error
	5, // 3: titanium.GetGeneratedValidationRuleResponse.error:type_name -> titanium.Error
	4, // [4:4] is the sub-list for method output_type
	4, // [4:4] is the sub-list for method input_type
	4, // [4:4] is the sub-list for extension type_name
	4, // [4:4] is the sub-list for extension extendee
	0, // [0:4] is the sub-list for field type_name
}

func init() { file_common_validation_service_proto_init() }
func file_common_validation_service_proto_init() {
	if File_common_validation_service_proto != nil {
		return
	}
	file_common_gateway_base_proto_init()
	if !protoimpl.UnsafeEnabled {
		file_common_validation_service_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*ValidationRuleDefinition); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_common_validation_service_proto_msgTypes[1].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*GetValidationRuleResponse); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_common_validation_service_proto_msgTypes[2].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*GetGeneratedValidationRuleResponse); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_common_validation_service_proto_msgTypes[3].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*RdlCheckRequest); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
	}
	file_common_validation_service_proto_msgTypes[1].OneofWrappers = []interface{}{
		(*GetValidationRuleResponse_Data)(nil),
		(*GetValidationRuleResponse_Error)(nil),
	}
	file_common_validation_service_proto_msgTypes[2].OneofWrappers = []interface{}{
		(*GetGeneratedValidationRuleResponse_Data)(nil),
		(*GetGeneratedValidationRuleResponse_Error)(nil),
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_common_validation_service_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   4,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_common_validation_service_proto_goTypes,
		DependencyIndexes: file_common_validation_service_proto_depIdxs,
		MessageInfos:      file_common_validation_service_proto_msgTypes,
	}.Build()
	File_common_validation_service_proto = out.File
	file_common_validation_service_proto_rawDesc = nil
	file_common_validation_service_proto_goTypes = nil
	file_common_validation_service_proto_depIdxs = nil
}
