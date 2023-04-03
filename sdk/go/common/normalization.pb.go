// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.27.1
// 	protoc        v3.18.1
// source: common/normalization.proto

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

// Definition for normalization rule that can be add the the system.
type NormalizationRuleDefinition struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Uid             string            `protobuf:"bytes,1,opt,name=uid,proto3" json:"uid,omitempty"`
	DescriptorName  string            `protobuf:"bytes,2,opt,name=descriptor_name,json=descriptorName,proto3" json:"descriptor_name,omitempty"`
	Transformations []*Transformation `protobuf:"bytes,4,rep,name=transformations,proto3" json:"transformations,omitempty"`
	Scope           string            `protobuf:"bytes,5,opt,name=scope,proto3" json:"scope,omitempty"`
}

func (x *NormalizationRuleDefinition) Reset() {
	*x = NormalizationRuleDefinition{}
	if protoimpl.UnsafeEnabled {
		mi := &file_common_normalization_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *NormalizationRuleDefinition) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*NormalizationRuleDefinition) ProtoMessage() {}

func (x *NormalizationRuleDefinition) ProtoReflect() protoreflect.Message {
	mi := &file_common_normalization_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use NormalizationRuleDefinition.ProtoReflect.Descriptor instead.
func (*NormalizationRuleDefinition) Descriptor() ([]byte, []int) {
	return file_common_normalization_proto_rawDescGZIP(), []int{0}
}

func (x *NormalizationRuleDefinition) GetUid() string {
	if x != nil {
		return x.Uid
	}
	return ""
}

func (x *NormalizationRuleDefinition) GetDescriptorName() string {
	if x != nil {
		return x.DescriptorName
	}
	return ""
}

func (x *NormalizationRuleDefinition) GetTransformations() []*Transformation {
	if x != nil {
		return x.Transformations
	}
	return nil
}

func (x *NormalizationRuleDefinition) GetScope() string {
	if x != nil {
		return x.Scope
	}
	return ""
}

// NormalizationRuleResponse is response after adding rule to the system(can return error or data for the rule that was added)
type NormalizationRuleResponse struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// Types that are assignable to Response:
	//
	//	*NormalizationRuleResponse_Data
	//	*NormalizationRuleResponse_Error
	Response isNormalizationRuleResponse_Response `protobuf_oneof:"response"`
}

func (x *NormalizationRuleResponse) Reset() {
	*x = NormalizationRuleResponse{}
	if protoimpl.UnsafeEnabled {
		mi := &file_common_normalization_proto_msgTypes[1]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *NormalizationRuleResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*NormalizationRuleResponse) ProtoMessage() {}

func (x *NormalizationRuleResponse) ProtoReflect() protoreflect.Message {
	mi := &file_common_normalization_proto_msgTypes[1]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use NormalizationRuleResponse.ProtoReflect.Descriptor instead.
func (*NormalizationRuleResponse) Descriptor() ([]byte, []int) {
	return file_common_normalization_proto_rawDescGZIP(), []int{1}
}

func (m *NormalizationRuleResponse) GetResponse() isNormalizationRuleResponse_Response {
	if m != nil {
		return m.Response
	}
	return nil
}

func (x *NormalizationRuleResponse) GetData() *NormalizationRuleDefinition {
	if x, ok := x.GetResponse().(*NormalizationRuleResponse_Data); ok {
		return x.Data
	}
	return nil
}

func (x *NormalizationRuleResponse) GetError() *Error {
	if x, ok := x.GetResponse().(*NormalizationRuleResponse_Error); ok {
		return x.Error
	}
	return nil
}

type isNormalizationRuleResponse_Response interface {
	isNormalizationRuleResponse_Response()
}

type NormalizationRuleResponse_Data struct {
	Data *NormalizationRuleDefinition `protobuf:"bytes,1,opt,name=data,proto3,oneof"`
}

type NormalizationRuleResponse_Error struct {
	Error *Error `protobuf:"bytes,2,opt,name=error,proto3,oneof"`
}

func (*NormalizationRuleResponse_Data) isNormalizationRuleResponse_Response() {}

func (*NormalizationRuleResponse_Error) isNormalizationRuleResponse_Response() {}

var File_common_normalization_proto protoreflect.FileDescriptor

var file_common_normalization_proto_rawDesc = []byte{
	0x0a, 0x1a, 0x63, 0x6f, 0x6d, 0x6d, 0x6f, 0x6e, 0x2f, 0x6e, 0x6f, 0x72, 0x6d, 0x61, 0x6c, 0x69,
	0x7a, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x12, 0x08, 0x74, 0x69,
	0x74, 0x61, 0x6e, 0x69, 0x75, 0x6d, 0x1a, 0x19, 0x63, 0x6f, 0x6d, 0x6d, 0x6f, 0x6e, 0x2f, 0x67,
	0x61, 0x74, 0x65, 0x77, 0x61, 0x79, 0x5f, 0x62, 0x61, 0x73, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74,
	0x6f, 0x22, 0xb2, 0x01, 0x0a, 0x1b, 0x4e, 0x6f, 0x72, 0x6d, 0x61, 0x6c, 0x69, 0x7a, 0x61, 0x74,
	0x69, 0x6f, 0x6e, 0x52, 0x75, 0x6c, 0x65, 0x44, 0x65, 0x66, 0x69, 0x6e, 0x69, 0x74, 0x69, 0x6f,
	0x6e, 0x12, 0x10, 0x0a, 0x03, 0x75, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x03,
	0x75, 0x69, 0x64, 0x12, 0x27, 0x0a, 0x0f, 0x64, 0x65, 0x73, 0x63, 0x72, 0x69, 0x70, 0x74, 0x6f,
	0x72, 0x5f, 0x6e, 0x61, 0x6d, 0x65, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0e, 0x64, 0x65,
	0x73, 0x63, 0x72, 0x69, 0x70, 0x74, 0x6f, 0x72, 0x4e, 0x61, 0x6d, 0x65, 0x12, 0x42, 0x0a, 0x0f,
	0x74, 0x72, 0x61, 0x6e, 0x73, 0x66, 0x6f, 0x72, 0x6d, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x73, 0x18,
	0x04, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x18, 0x2e, 0x74, 0x69, 0x74, 0x61, 0x6e, 0x69, 0x75, 0x6d,
	0x2e, 0x54, 0x72, 0x61, 0x6e, 0x73, 0x66, 0x6f, 0x72, 0x6d, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x52,
	0x0f, 0x74, 0x72, 0x61, 0x6e, 0x73, 0x66, 0x6f, 0x72, 0x6d, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x73,
	0x12, 0x14, 0x0a, 0x05, 0x73, 0x63, 0x6f, 0x70, 0x65, 0x18, 0x05, 0x20, 0x01, 0x28, 0x09, 0x52,
	0x05, 0x73, 0x63, 0x6f, 0x70, 0x65, 0x22, 0x8d, 0x01, 0x0a, 0x19, 0x4e, 0x6f, 0x72, 0x6d, 0x61,
	0x6c, 0x69, 0x7a, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x52, 0x75, 0x6c, 0x65, 0x52, 0x65, 0x73, 0x70,
	0x6f, 0x6e, 0x73, 0x65, 0x12, 0x3b, 0x0a, 0x04, 0x64, 0x61, 0x74, 0x61, 0x18, 0x01, 0x20, 0x01,
	0x28, 0x0b, 0x32, 0x25, 0x2e, 0x74, 0x69, 0x74, 0x61, 0x6e, 0x69, 0x75, 0x6d, 0x2e, 0x4e, 0x6f,
	0x72, 0x6d, 0x61, 0x6c, 0x69, 0x7a, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x52, 0x75, 0x6c, 0x65, 0x44,
	0x65, 0x66, 0x69, 0x6e, 0x69, 0x74, 0x69, 0x6f, 0x6e, 0x48, 0x00, 0x52, 0x04, 0x64, 0x61, 0x74,
	0x61, 0x12, 0x27, 0x0a, 0x05, 0x65, 0x72, 0x72, 0x6f, 0x72, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0b,
	0x32, 0x0f, 0x2e, 0x74, 0x69, 0x74, 0x61, 0x6e, 0x69, 0x75, 0x6d, 0x2e, 0x45, 0x72, 0x72, 0x6f,
	0x72, 0x48, 0x00, 0x52, 0x05, 0x65, 0x72, 0x72, 0x6f, 0x72, 0x42, 0x0a, 0x0a, 0x08, 0x72, 0x65,
	0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x42, 0x7b, 0x0a, 0x20, 0x63, 0x6f, 0x6d, 0x2e, 0x70, 0x65,
	0x65, 0x72, 0x6e, 0x6f, 0x76, 0x61, 0x2e, 0x74, 0x69, 0x74, 0x61, 0x6e, 0x69, 0x75, 0x6d, 0x2e,
	0x69, 0x6e, 0x74, 0x65, 0x72, 0x66, 0x61, 0x63, 0x65, 0x73, 0x42, 0x1f, 0x4e, 0x6f, 0x72, 0x6d,
	0x61, 0x6c, 0x69, 0x7a, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x53, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65,
	0x50, 0x72, 0x6f, 0x74, 0x6f, 0x43, 0x6f, 0x6d, 0x6d, 0x6f, 0x6e, 0x50, 0x01, 0x5a, 0x34, 0x67,
	0x69, 0x74, 0x68, 0x75, 0x62, 0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x70, 0x65, 0x65, 0x72, 0x6e, 0x6f,
	0x76, 0x61, 0x2f, 0x63, 0x6c, 0x65, 0x61, 0x72, 0x63, 0x6f, 0x6e, 0x73, 0x65, 0x6e, 0x73, 0x75,
	0x73, 0x2d, 0x73, 0x64, 0x6b, 0x2f, 0x73, 0x64, 0x6b, 0x2f, 0x67, 0x6f, 0x2f, 0x63, 0x6f, 0x6d,
	0x6d, 0x6f, 0x6e, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_common_normalization_proto_rawDescOnce sync.Once
	file_common_normalization_proto_rawDescData = file_common_normalization_proto_rawDesc
)

func file_common_normalization_proto_rawDescGZIP() []byte {
	file_common_normalization_proto_rawDescOnce.Do(func() {
		file_common_normalization_proto_rawDescData = protoimpl.X.CompressGZIP(file_common_normalization_proto_rawDescData)
	})
	return file_common_normalization_proto_rawDescData
}

var file_common_normalization_proto_msgTypes = make([]protoimpl.MessageInfo, 2)
var file_common_normalization_proto_goTypes = []interface{}{
	(*NormalizationRuleDefinition)(nil), // 0: titanium.NormalizationRuleDefinition
	(*NormalizationRuleResponse)(nil),   // 1: titanium.NormalizationRuleResponse
	(*Transformation)(nil),              // 2: titanium.Transformation
	(*Error)(nil),                       // 3: titanium.Error
}
var file_common_normalization_proto_depIdxs = []int32{
	2, // 0: titanium.NormalizationRuleDefinition.transformations:type_name -> titanium.Transformation
	0, // 1: titanium.NormalizationRuleResponse.data:type_name -> titanium.NormalizationRuleDefinition
	3, // 2: titanium.NormalizationRuleResponse.error:type_name -> titanium.Error
	3, // [3:3] is the sub-list for method output_type
	3, // [3:3] is the sub-list for method input_type
	3, // [3:3] is the sub-list for extension type_name
	3, // [3:3] is the sub-list for extension extendee
	0, // [0:3] is the sub-list for field type_name
}

func init() { file_common_normalization_proto_init() }
func file_common_normalization_proto_init() {
	if File_common_normalization_proto != nil {
		return
	}
	file_common_gateway_base_proto_init()
	if !protoimpl.UnsafeEnabled {
		file_common_normalization_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*NormalizationRuleDefinition); i {
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
		file_common_normalization_proto_msgTypes[1].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*NormalizationRuleResponse); i {
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
	file_common_normalization_proto_msgTypes[1].OneofWrappers = []interface{}{
		(*NormalizationRuleResponse_Data)(nil),
		(*NormalizationRuleResponse_Error)(nil),
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_common_normalization_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   2,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_common_normalization_proto_goTypes,
		DependencyIndexes: file_common_normalization_proto_depIdxs,
		MessageInfos:      file_common_normalization_proto_msgTypes,
	}.Build()
	File_common_normalization_proto = out.File
	file_common_normalization_proto_rawDesc = nil
	file_common_normalization_proto_goTypes = nil
	file_common_normalization_proto_depIdxs = nil
}
