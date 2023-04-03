// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.27.1
// 	protoc        v3.18.1
// source: private/supported_fields_private_service.proto

package private

import (
	common "github.com/peernova/clearconsensus-sdk/sdk/go/common"
	_ "google.golang.org/genproto/googleapis/api/annotations"
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

type SupportedFieldsValues struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	AssetId   string   `protobuf:"bytes,1,opt,name=asset_id,json=assetId,proto3" json:"asset_id,omitempty"`
	Field     string   `protobuf:"bytes,2,opt,name=field,proto3" json:"field,omitempty"`
	Values    []string `protobuf:"bytes,3,rep,name=values,proto3" json:"values,omitempty"`
	TraceName string   `protobuf:"bytes,4,opt,name=trace_name,json=traceName,proto3" json:"trace_name,omitempty"`
}

func (x *SupportedFieldsValues) Reset() {
	*x = SupportedFieldsValues{}
	if protoimpl.UnsafeEnabled {
		mi := &file_private_supported_fields_private_service_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *SupportedFieldsValues) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SupportedFieldsValues) ProtoMessage() {}

func (x *SupportedFieldsValues) ProtoReflect() protoreflect.Message {
	mi := &file_private_supported_fields_private_service_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SupportedFieldsValues.ProtoReflect.Descriptor instead.
func (*SupportedFieldsValues) Descriptor() ([]byte, []int) {
	return file_private_supported_fields_private_service_proto_rawDescGZIP(), []int{0}
}

func (x *SupportedFieldsValues) GetAssetId() string {
	if x != nil {
		return x.AssetId
	}
	return ""
}

func (x *SupportedFieldsValues) GetField() string {
	if x != nil {
		return x.Field
	}
	return ""
}

func (x *SupportedFieldsValues) GetValues() []string {
	if x != nil {
		return x.Values
	}
	return nil
}

func (x *SupportedFieldsValues) GetTraceName() string {
	if x != nil {
		return x.TraceName
	}
	return ""
}

var File_private_supported_fields_private_service_proto protoreflect.FileDescriptor

var file_private_supported_fields_private_service_proto_rawDesc = []byte{
	0x0a, 0x2e, 0x70, 0x72, 0x69, 0x76, 0x61, 0x74, 0x65, 0x2f, 0x73, 0x75, 0x70, 0x70, 0x6f, 0x72,
	0x74, 0x65, 0x64, 0x5f, 0x66, 0x69, 0x65, 0x6c, 0x64, 0x73, 0x5f, 0x70, 0x72, 0x69, 0x76, 0x61,
	0x74, 0x65, 0x5f, 0x73, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f,
	0x12, 0x08, 0x74, 0x69, 0x74, 0x61, 0x6e, 0x69, 0x75, 0x6d, 0x1a, 0x1c, 0x67, 0x6f, 0x6f, 0x67,
	0x6c, 0x65, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x61, 0x6e, 0x6e, 0x6f, 0x74, 0x61, 0x74, 0x69, 0x6f,
	0x6e, 0x73, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x19, 0x63, 0x6f, 0x6d, 0x6d, 0x6f, 0x6e,
	0x2f, 0x67, 0x61, 0x74, 0x65, 0x77, 0x61, 0x79, 0x5f, 0x62, 0x61, 0x73, 0x65, 0x2e, 0x70, 0x72,
	0x6f, 0x74, 0x6f, 0x22, 0x7f, 0x0a, 0x15, 0x53, 0x75, 0x70, 0x70, 0x6f, 0x72, 0x74, 0x65, 0x64,
	0x46, 0x69, 0x65, 0x6c, 0x64, 0x73, 0x56, 0x61, 0x6c, 0x75, 0x65, 0x73, 0x12, 0x19, 0x0a, 0x08,
	0x61, 0x73, 0x73, 0x65, 0x74, 0x5f, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x07,
	0x61, 0x73, 0x73, 0x65, 0x74, 0x49, 0x64, 0x12, 0x14, 0x0a, 0x05, 0x66, 0x69, 0x65, 0x6c, 0x64,
	0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x05, 0x66, 0x69, 0x65, 0x6c, 0x64, 0x12, 0x16, 0x0a,
	0x06, 0x76, 0x61, 0x6c, 0x75, 0x65, 0x73, 0x18, 0x03, 0x20, 0x03, 0x28, 0x09, 0x52, 0x06, 0x76,
	0x61, 0x6c, 0x75, 0x65, 0x73, 0x12, 0x1d, 0x0a, 0x0a, 0x74, 0x72, 0x61, 0x63, 0x65, 0x5f, 0x6e,
	0x61, 0x6d, 0x65, 0x18, 0x04, 0x20, 0x01, 0x28, 0x09, 0x52, 0x09, 0x74, 0x72, 0x61, 0x63, 0x65,
	0x4e, 0x61, 0x6d, 0x65, 0x32, 0xad, 0x03, 0x0a, 0x1d, 0x53, 0x75, 0x70, 0x70, 0x6f, 0x72, 0x74,
	0x65, 0x64, 0x46, 0x69, 0x65, 0x6c, 0x64, 0x73, 0x50, 0x72, 0x69, 0x76, 0x61, 0x74, 0x65, 0x53,
	0x65, 0x72, 0x76, 0x69, 0x63, 0x65, 0x12, 0x84, 0x01, 0x0a, 0x15, 0x43, 0x72, 0x65, 0x61, 0x74,
	0x65, 0x53, 0x75, 0x70, 0x70, 0x6f, 0x72, 0x74, 0x65, 0x64, 0x46, 0x69, 0x65, 0x6c, 0x64, 0x73,
	0x12, 0x1f, 0x2e, 0x74, 0x69, 0x74, 0x61, 0x6e, 0x69, 0x75, 0x6d, 0x2e, 0x53, 0x75, 0x70, 0x70,
	0x6f, 0x72, 0x74, 0x65, 0x64, 0x46, 0x69, 0x65, 0x6c, 0x64, 0x73, 0x56, 0x61, 0x6c, 0x75, 0x65,
	0x73, 0x1a, 0x19, 0x2e, 0x74, 0x69, 0x74, 0x61, 0x6e, 0x69, 0x75, 0x6d, 0x2e, 0x4d, 0x65, 0x73,
	0x73, 0x61, 0x67, 0x65, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x22, 0x2f, 0x82, 0xd3,
	0xe4, 0x93, 0x02, 0x29, 0x22, 0x24, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x76, 0x31, 0x2f, 0x6f, 0x70,
	0x65, 0x72, 0x61, 0x74, 0x6f, 0x72, 0x2f, 0x63, 0x72, 0x65, 0x61, 0x74, 0x65, 0x2f, 0x66, 0x69,
	0x65, 0x6c, 0x64, 0x2d, 0x76, 0x61, 0x6c, 0x75, 0x65, 0x73, 0x3a, 0x01, 0x2a, 0x12, 0x7e, 0x0a,
	0x12, 0x41, 0x64, 0x64, 0x53, 0x75, 0x70, 0x70, 0x6f, 0x72, 0x74, 0x65, 0x64, 0x46, 0x69, 0x65,
	0x6c, 0x64, 0x73, 0x12, 0x1f, 0x2e, 0x74, 0x69, 0x74, 0x61, 0x6e, 0x69, 0x75, 0x6d, 0x2e, 0x53,
	0x75, 0x70, 0x70, 0x6f, 0x72, 0x74, 0x65, 0x64, 0x46, 0x69, 0x65, 0x6c, 0x64, 0x73, 0x56, 0x61,
	0x6c, 0x75, 0x65, 0x73, 0x1a, 0x19, 0x2e, 0x74, 0x69, 0x74, 0x61, 0x6e, 0x69, 0x75, 0x6d, 0x2e,
	0x4d, 0x65, 0x73, 0x73, 0x61, 0x67, 0x65, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x22,
	0x2c, 0x82, 0xd3, 0xe4, 0x93, 0x02, 0x26, 0x22, 0x21, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x76, 0x31,
	0x2f, 0x6f, 0x70, 0x65, 0x72, 0x61, 0x74, 0x6f, 0x72, 0x2f, 0x61, 0x64, 0x64, 0x2f, 0x66, 0x69,
	0x65, 0x6c, 0x64, 0x2d, 0x76, 0x61, 0x6c, 0x75, 0x65, 0x73, 0x3a, 0x01, 0x2a, 0x12, 0x84, 0x01,
	0x0a, 0x15, 0x44, 0x65, 0x6c, 0x65, 0x74, 0x65, 0x53, 0x75, 0x70, 0x70, 0x6f, 0x72, 0x74, 0x65,
	0x64, 0x46, 0x69, 0x65, 0x6c, 0x64, 0x73, 0x12, 0x1f, 0x2e, 0x74, 0x69, 0x74, 0x61, 0x6e, 0x69,
	0x75, 0x6d, 0x2e, 0x53, 0x75, 0x70, 0x70, 0x6f, 0x72, 0x74, 0x65, 0x64, 0x46, 0x69, 0x65, 0x6c,
	0x64, 0x73, 0x56, 0x61, 0x6c, 0x75, 0x65, 0x73, 0x1a, 0x19, 0x2e, 0x74, 0x69, 0x74, 0x61, 0x6e,
	0x69, 0x75, 0x6d, 0x2e, 0x4d, 0x65, 0x73, 0x73, 0x61, 0x67, 0x65, 0x52, 0x65, 0x73, 0x70, 0x6f,
	0x6e, 0x73, 0x65, 0x22, 0x2f, 0x82, 0xd3, 0xe4, 0x93, 0x02, 0x29, 0x22, 0x24, 0x2f, 0x61, 0x70,
	0x69, 0x2f, 0x76, 0x31, 0x2f, 0x6f, 0x70, 0x65, 0x72, 0x61, 0x74, 0x6f, 0x72, 0x2f, 0x64, 0x65,
	0x6c, 0x65, 0x74, 0x65, 0x2f, 0x66, 0x69, 0x65, 0x6c, 0x64, 0x2d, 0x76, 0x61, 0x6c, 0x75, 0x65,
	0x73, 0x3a, 0x01, 0x2a, 0x42, 0x7f, 0x0a, 0x20, 0x63, 0x6f, 0x6d, 0x2e, 0x70, 0x65, 0x65, 0x72,
	0x6e, 0x6f, 0x76, 0x61, 0x2e, 0x74, 0x69, 0x74, 0x61, 0x6e, 0x69, 0x75, 0x6d, 0x2e, 0x69, 0x6e,
	0x74, 0x65, 0x72, 0x66, 0x61, 0x63, 0x65, 0x73, 0x42, 0x22, 0x53, 0x75, 0x70, 0x70, 0x6f, 0x72,
	0x74, 0x65, 0x64, 0x46, 0x69, 0x65, 0x6c, 0x64, 0x73, 0x53, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65,
	0x50, 0x72, 0x6f, 0x74, 0x6f, 0x50, 0x72, 0x69, 0x76, 0x61, 0x74, 0x65, 0x50, 0x01, 0x5a, 0x35,
	0x67, 0x69, 0x74, 0x68, 0x75, 0x62, 0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x70, 0x65, 0x65, 0x72, 0x6e,
	0x6f, 0x76, 0x61, 0x2f, 0x63, 0x6c, 0x65, 0x61, 0x72, 0x63, 0x6f, 0x6e, 0x73, 0x65, 0x6e, 0x73,
	0x75, 0x73, 0x2d, 0x73, 0x64, 0x6b, 0x2f, 0x73, 0x64, 0x6b, 0x2f, 0x67, 0x6f, 0x2f, 0x70, 0x72,
	0x69, 0x76, 0x61, 0x74, 0x65, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_private_supported_fields_private_service_proto_rawDescOnce sync.Once
	file_private_supported_fields_private_service_proto_rawDescData = file_private_supported_fields_private_service_proto_rawDesc
)

func file_private_supported_fields_private_service_proto_rawDescGZIP() []byte {
	file_private_supported_fields_private_service_proto_rawDescOnce.Do(func() {
		file_private_supported_fields_private_service_proto_rawDescData = protoimpl.X.CompressGZIP(file_private_supported_fields_private_service_proto_rawDescData)
	})
	return file_private_supported_fields_private_service_proto_rawDescData
}

var file_private_supported_fields_private_service_proto_msgTypes = make([]protoimpl.MessageInfo, 1)
var file_private_supported_fields_private_service_proto_goTypes = []interface{}{
	(*SupportedFieldsValues)(nil),  // 0: titanium.SupportedFieldsValues
	(*common.MessageResponse)(nil), // 1: titanium.MessageResponse
}
var file_private_supported_fields_private_service_proto_depIdxs = []int32{
	0, // 0: titanium.SupportedFieldsPrivateService.CreateSupportedFields:input_type -> titanium.SupportedFieldsValues
	0, // 1: titanium.SupportedFieldsPrivateService.AddSupportedFields:input_type -> titanium.SupportedFieldsValues
	0, // 2: titanium.SupportedFieldsPrivateService.DeleteSupportedFields:input_type -> titanium.SupportedFieldsValues
	1, // 3: titanium.SupportedFieldsPrivateService.CreateSupportedFields:output_type -> titanium.MessageResponse
	1, // 4: titanium.SupportedFieldsPrivateService.AddSupportedFields:output_type -> titanium.MessageResponse
	1, // 5: titanium.SupportedFieldsPrivateService.DeleteSupportedFields:output_type -> titanium.MessageResponse
	3, // [3:6] is the sub-list for method output_type
	0, // [0:3] is the sub-list for method input_type
	0, // [0:0] is the sub-list for extension type_name
	0, // [0:0] is the sub-list for extension extendee
	0, // [0:0] is the sub-list for field type_name
}

func init() { file_private_supported_fields_private_service_proto_init() }
func file_private_supported_fields_private_service_proto_init() {
	if File_private_supported_fields_private_service_proto != nil {
		return
	}
	if !protoimpl.UnsafeEnabled {
		file_private_supported_fields_private_service_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*SupportedFieldsValues); i {
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
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_private_supported_fields_private_service_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   1,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_private_supported_fields_private_service_proto_goTypes,
		DependencyIndexes: file_private_supported_fields_private_service_proto_depIdxs,
		MessageInfos:      file_private_supported_fields_private_service_proto_msgTypes,
	}.Build()
	File_private_supported_fields_private_service_proto = out.File
	file_private_supported_fields_private_service_proto_rawDesc = nil
	file_private_supported_fields_private_service_proto_goTypes = nil
	file_private_supported_fields_private_service_proto_depIdxs = nil
}
