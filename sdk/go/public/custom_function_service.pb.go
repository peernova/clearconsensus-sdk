// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.27.1
// 	protoc        v3.18.1
// source: public/custom_function_service.proto

package public

import (
	common "github.com/peernova/clearconsensus-sdk/sdk/go/common"
	_ "google.golang.org/genproto/googleapis/api/annotations"
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	reflect "reflect"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

var File_public_custom_function_service_proto protoreflect.FileDescriptor

var file_public_custom_function_service_proto_rawDesc = []byte{
	0x0a, 0x24, 0x70, 0x75, 0x62, 0x6c, 0x69, 0x63, 0x2f, 0x63, 0x75, 0x73, 0x74, 0x6f, 0x6d, 0x5f,
	0x66, 0x75, 0x6e, 0x63, 0x74, 0x69, 0x6f, 0x6e, 0x5f, 0x73, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65,
	0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x12, 0x08, 0x74, 0x69, 0x74, 0x61, 0x6e, 0x69, 0x75, 0x6d,
	0x1a, 0x1c, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x61, 0x6e, 0x6e,
	0x6f, 0x74, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x73, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x19,
	0x63, 0x6f, 0x6d, 0x6d, 0x6f, 0x6e, 0x2f, 0x67, 0x61, 0x74, 0x65, 0x77, 0x61, 0x79, 0x5f, 0x62,
	0x61, 0x73, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x1c, 0x63, 0x6f, 0x6d, 0x6d, 0x6f,
	0x6e, 0x2f, 0x63, 0x75, 0x73, 0x74, 0x6f, 0x6d, 0x5f, 0x66, 0x75, 0x6e, 0x63, 0x74, 0x69, 0x6f,
	0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x32, 0xaa, 0x04, 0x0a, 0x15, 0x43, 0x75, 0x73, 0x74,
	0x6f, 0x6d, 0x46, 0x75, 0x6e, 0x63, 0x74, 0x69, 0x6f, 0x6e, 0x53, 0x65, 0x72, 0x76, 0x69, 0x63,
	0x65, 0x12, 0x73, 0x0a, 0x11, 0x41, 0x64, 0x64, 0x43, 0x75, 0x73, 0x74, 0x6f, 0x6d, 0x46, 0x75,
	0x6e, 0x63, 0x74, 0x69, 0x6f, 0x6e, 0x12, 0x18, 0x2e, 0x74, 0x69, 0x74, 0x61, 0x6e, 0x69, 0x75,
	0x6d, 0x2e, 0x43, 0x75, 0x73, 0x74, 0x6f, 0x6d, 0x46, 0x75, 0x6e, 0x63, 0x74, 0x69, 0x6f, 0x6e,
	0x1a, 0x1d, 0x2e, 0x74, 0x69, 0x74, 0x61, 0x6e, 0x69, 0x75, 0x6d, 0x2e, 0x41, 0x63, 0x6b, 0x6e,
	0x6f, 0x77, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x22,
	0x25, 0x82, 0xd3, 0xe4, 0x93, 0x02, 0x1f, 0x22, 0x1a, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x76, 0x31,
	0x2f, 0x63, 0x75, 0x73, 0x74, 0x6f, 0x6d, 0x66, 0x75, 0x6e, 0x63, 0x74, 0x69, 0x6f, 0x6e, 0x2f,
	0x61, 0x64, 0x64, 0x3a, 0x01, 0x2a, 0x12, 0x8d, 0x01, 0x0a, 0x11, 0x47, 0x65, 0x74, 0x43, 0x75,
	0x73, 0x74, 0x6f, 0x6d, 0x46, 0x75, 0x6e, 0x63, 0x74, 0x69, 0x6f, 0x6e, 0x12, 0x25, 0x2e, 0x74,
	0x69, 0x74, 0x61, 0x6e, 0x69, 0x75, 0x6d, 0x2e, 0x43, 0x75, 0x73, 0x74, 0x6f, 0x6d, 0x46, 0x75,
	0x6e, 0x63, 0x74, 0x69, 0x6f, 0x6e, 0x47, 0x65, 0x74, 0x44, 0x65, 0x66, 0x69, 0x6e, 0x69, 0x74,
	0x69, 0x6f, 0x6e, 0x1a, 0x2a, 0x2e, 0x74, 0x69, 0x74, 0x61, 0x6e, 0x69, 0x75, 0x6d, 0x2e, 0x43,
	0x75, 0x73, 0x74, 0x6f, 0x6d, 0x46, 0x75, 0x6e, 0x63, 0x74, 0x69, 0x6f, 0x6e, 0x44, 0x65, 0x66,
	0x69, 0x6e, 0x69, 0x74, 0x69, 0x6f, 0x6e, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x22,
	0x25, 0x82, 0xd3, 0xe4, 0x93, 0x02, 0x1f, 0x22, 0x1a, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x76, 0x31,
	0x2f, 0x63, 0x75, 0x73, 0x74, 0x6f, 0x6d, 0x66, 0x75, 0x6e, 0x63, 0x74, 0x69, 0x6f, 0x6e, 0x2f,
	0x67, 0x65, 0x74, 0x3a, 0x01, 0x2a, 0x12, 0x88, 0x01, 0x0a, 0x13, 0x4c, 0x69, 0x73, 0x74, 0x43,
	0x75, 0x73, 0x74, 0x6f, 0x6d, 0x46, 0x75, 0x6e, 0x63, 0x74, 0x69, 0x6f, 0x6e, 0x73, 0x12, 0x23,
	0x2e, 0x74, 0x69, 0x74, 0x61, 0x6e, 0x69, 0x75, 0x6d, 0x2e, 0x4c, 0x69, 0x73, 0x74, 0x43, 0x75,
	0x73, 0x74, 0x6f, 0x6d, 0x46, 0x75, 0x6e, 0x63, 0x74, 0x69, 0x6f, 0x6e, 0x52, 0x65, 0x71, 0x75,
	0x65, 0x73, 0x74, 0x1a, 0x24, 0x2e, 0x74, 0x69, 0x74, 0x61, 0x6e, 0x69, 0x75, 0x6d, 0x2e, 0x4c,
	0x69, 0x73, 0x74, 0x43, 0x75, 0x73, 0x74, 0x6f, 0x6d, 0x46, 0x75, 0x6e, 0x63, 0x74, 0x69, 0x6f,
	0x6e, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x22, 0x26, 0x82, 0xd3, 0xe4, 0x93, 0x02,
	0x20, 0x22, 0x1b, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x76, 0x31, 0x2f, 0x63, 0x75, 0x73, 0x74, 0x6f,
	0x6d, 0x66, 0x75, 0x6e, 0x63, 0x74, 0x69, 0x6f, 0x6e, 0x2f, 0x6c, 0x69, 0x73, 0x74, 0x3a, 0x01,
	0x2a, 0x12, 0x80, 0x01, 0x0a, 0x1a, 0x4c, 0x69, 0x73, 0x74, 0x43, 0x75, 0x73, 0x74, 0x6f, 0x6d,
	0x46, 0x75, 0x6e, 0x63, 0x74, 0x69, 0x6f, 0x6e, 0x56, 0x65, 0x72, 0x73, 0x69, 0x6f, 0x6e, 0x73,
	0x12, 0x17, 0x2e, 0x74, 0x69, 0x74, 0x61, 0x6e, 0x69, 0x75, 0x6d, 0x2e, 0x47, 0x65, 0x74, 0x44,
	0x65, 0x66, 0x69, 0x6e, 0x69, 0x74, 0x69, 0x6f, 0x6e, 0x1a, 0x1d, 0x2e, 0x74, 0x69, 0x74, 0x61,
	0x6e, 0x69, 0x75, 0x6d, 0x2e, 0x4c, 0x69, 0x73, 0x74, 0x56, 0x65, 0x72, 0x73, 0x69, 0x6f, 0x6e,
	0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x22, 0x2a, 0x82, 0xd3, 0xe4, 0x93, 0x02, 0x24,
	0x22, 0x1f, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x76, 0x31, 0x2f, 0x63, 0x75, 0x73, 0x74, 0x6f, 0x6d,
	0x66, 0x75, 0x6e, 0x63, 0x74, 0x69, 0x6f, 0x6e, 0x2f, 0x76, 0x65, 0x72, 0x73, 0x69, 0x6f, 0x6e,
	0x73, 0x3a, 0x01, 0x2a, 0x42, 0x7c, 0x0a, 0x20, 0x63, 0x6f, 0x6d, 0x2e, 0x70, 0x65, 0x65, 0x72,
	0x6e, 0x6f, 0x76, 0x61, 0x2e, 0x74, 0x69, 0x74, 0x61, 0x6e, 0x69, 0x75, 0x6d, 0x2e, 0x69, 0x6e,
	0x74, 0x65, 0x72, 0x66, 0x61, 0x63, 0x65, 0x73, 0x42, 0x20, 0x43, 0x75, 0x73, 0x74, 0x6f, 0x6d,
	0x46, 0x75, 0x6e, 0x63, 0x74, 0x69, 0x6f, 0x6e, 0x53, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65, 0x50,
	0x72, 0x6f, 0x74, 0x6f, 0x50, 0x75, 0x62, 0x6c, 0x69, 0x63, 0x50, 0x01, 0x5a, 0x34, 0x67, 0x69,
	0x74, 0x68, 0x75, 0x62, 0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x70, 0x65, 0x65, 0x72, 0x6e, 0x6f, 0x76,
	0x61, 0x2f, 0x63, 0x6c, 0x65, 0x61, 0x72, 0x63, 0x6f, 0x6e, 0x73, 0x65, 0x6e, 0x73, 0x75, 0x73,
	0x2d, 0x73, 0x64, 0x6b, 0x2f, 0x73, 0x64, 0x6b, 0x2f, 0x67, 0x6f, 0x2f, 0x70, 0x75, 0x62, 0x6c,
	0x69, 0x63, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var file_public_custom_function_service_proto_goTypes = []interface{}{
	(*common.CustomFunction)(nil),                   // 0: titanium.CustomFunction
	(*common.CustomFunctionGetDefinition)(nil),      // 1: titanium.CustomFunctionGetDefinition
	(*common.ListCustomFunctionRequest)(nil),        // 2: titanium.ListCustomFunctionRequest
	(*common.GetDefinition)(nil),                    // 3: titanium.GetDefinition
	(*common.AcknowledgeResponse)(nil),              // 4: titanium.AcknowledgeResponse
	(*common.CustomFunctionDefinitionResponse)(nil), // 5: titanium.CustomFunctionDefinitionResponse
	(*common.ListCustomFunctionResponse)(nil),       // 6: titanium.ListCustomFunctionResponse
	(*common.ListVersionResponse)(nil),              // 7: titanium.ListVersionResponse
}
var file_public_custom_function_service_proto_depIdxs = []int32{
	0, // 0: titanium.CustomFunctionService.AddCustomFunction:input_type -> titanium.CustomFunction
	1, // 1: titanium.CustomFunctionService.GetCustomFunction:input_type -> titanium.CustomFunctionGetDefinition
	2, // 2: titanium.CustomFunctionService.ListCustomFunctions:input_type -> titanium.ListCustomFunctionRequest
	3, // 3: titanium.CustomFunctionService.ListCustomFunctionVersions:input_type -> titanium.GetDefinition
	4, // 4: titanium.CustomFunctionService.AddCustomFunction:output_type -> titanium.AcknowledgeResponse
	5, // 5: titanium.CustomFunctionService.GetCustomFunction:output_type -> titanium.CustomFunctionDefinitionResponse
	6, // 6: titanium.CustomFunctionService.ListCustomFunctions:output_type -> titanium.ListCustomFunctionResponse
	7, // 7: titanium.CustomFunctionService.ListCustomFunctionVersions:output_type -> titanium.ListVersionResponse
	4, // [4:8] is the sub-list for method output_type
	0, // [0:4] is the sub-list for method input_type
	0, // [0:0] is the sub-list for extension type_name
	0, // [0:0] is the sub-list for extension extendee
	0, // [0:0] is the sub-list for field type_name
}

func init() { file_public_custom_function_service_proto_init() }
func file_public_custom_function_service_proto_init() {
	if File_public_custom_function_service_proto != nil {
		return
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_public_custom_function_service_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   0,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_public_custom_function_service_proto_goTypes,
		DependencyIndexes: file_public_custom_function_service_proto_depIdxs,
	}.Build()
	File_public_custom_function_service_proto = out.File
	file_public_custom_function_service_proto_rawDesc = nil
	file_public_custom_function_service_proto_goTypes = nil
	file_public_custom_function_service_proto_depIdxs = nil
}
