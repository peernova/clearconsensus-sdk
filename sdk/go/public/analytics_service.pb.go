// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.27.1
// 	protoc        v3.18.1
// source: public/analytics_service.proto

package public

import (
	common "github.com/peernova/clearconsensus-sdk/sdk/go/common"
	_ "google.golang.org/genproto/googleapis/api/annotations"
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	emptypb "google.golang.org/protobuf/types/known/emptypb"
	reflect "reflect"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

var File_public_analytics_service_proto protoreflect.FileDescriptor

var file_public_analytics_service_proto_rawDesc = []byte{
	0x0a, 0x1e, 0x70, 0x75, 0x62, 0x6c, 0x69, 0x63, 0x2f, 0x61, 0x6e, 0x61, 0x6c, 0x79, 0x74, 0x69,
	0x63, 0x73, 0x5f, 0x73, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f,
	0x12, 0x08, 0x74, 0x69, 0x74, 0x61, 0x6e, 0x69, 0x75, 0x6d, 0x1a, 0x1c, 0x67, 0x6f, 0x6f, 0x67,
	0x6c, 0x65, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x61, 0x6e, 0x6e, 0x6f, 0x74, 0x61, 0x74, 0x69, 0x6f,
	0x6e, 0x73, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x1b, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65,
	0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2f, 0x65, 0x6d, 0x70, 0x74, 0x79, 0x2e,
	0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x16, 0x63, 0x6f, 0x6d, 0x6d, 0x6f, 0x6e, 0x2f, 0x61, 0x6e,
	0x61, 0x6c, 0x79, 0x74, 0x69, 0x63, 0x73, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x32, 0xa8, 0x07,
	0x0a, 0x13, 0x41, 0x6e, 0x61, 0x6c, 0x79, 0x74, 0x69, 0x63, 0x73, 0x43, 0x6f, 0x6e, 0x74, 0x72,
	0x6f, 0x6c, 0x6c, 0x65, 0x72, 0x12, 0xac, 0x01, 0x0a, 0x15, 0x46, 0x69, 0x6e, 0x64, 0x44, 0x61,
	0x74, 0x61, 0x51, 0x75, 0x61, 0x6c, 0x69, 0x74, 0x79, 0x45, 0x72, 0x72, 0x6f, 0x72, 0x73, 0x12,
	0x29, 0x2e, 0x74, 0x69, 0x74, 0x61, 0x6e, 0x69, 0x75, 0x6d, 0x2e, 0x47, 0x65, 0x6e, 0x65, 0x72,
	0x69, 0x63, 0x43, 0x68, 0x61, 0x72, 0x74, 0x4d, 0x65, 0x74, 0x61, 0x64, 0x61, 0x74, 0x61, 0x44,
	0x61, 0x74, 0x61, 0x51, 0x75, 0x61, 0x6c, 0x69, 0x74, 0x79, 0x1a, 0x31, 0x2e, 0x74, 0x69, 0x74,
	0x61, 0x6e, 0x69, 0x75, 0x6d, 0x2e, 0x47, 0x65, 0x6e, 0x65, 0x72, 0x69, 0x63, 0x43, 0x68, 0x61,
	0x72, 0x74, 0x4d, 0x65, 0x74, 0x61, 0x64, 0x61, 0x74, 0x61, 0x44, 0x61, 0x74, 0x61, 0x51, 0x75,
	0x61, 0x6c, 0x69, 0x74, 0x79, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x22, 0x35, 0x82,
	0xd3, 0xe4, 0x93, 0x02, 0x2f, 0x22, 0x2a, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x76, 0x31, 0x2f, 0x61,
	0x6e, 0x61, 0x6c, 0x79, 0x74, 0x69, 0x63, 0x73, 0x2f, 0x64, 0x61, 0x74, 0x61, 0x2d, 0x71, 0x75,
	0x61, 0x6c, 0x69, 0x74, 0x79, 0x2d, 0x65, 0x72, 0x72, 0x6f, 0x72, 0x73, 0x2f, 0x66, 0x69, 0x6e,
	0x64, 0x3a, 0x01, 0x2a, 0x12, 0x9b, 0x01, 0x0a, 0x17, 0x47, 0x65, 0x74, 0x41, 0x6c, 0x6c, 0x44,
	0x61, 0x74, 0x61, 0x51, 0x75, 0x61, 0x6c, 0x69, 0x74, 0x79, 0x45, 0x72, 0x72, 0x6f, 0x72, 0x73,
	0x12, 0x16, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62,
	0x75, 0x66, 0x2e, 0x45, 0x6d, 0x70, 0x74, 0x79, 0x1a, 0x31, 0x2e, 0x74, 0x69, 0x74, 0x61, 0x6e,
	0x69, 0x75, 0x6d, 0x2e, 0x47, 0x65, 0x6e, 0x65, 0x72, 0x69, 0x63, 0x43, 0x68, 0x61, 0x72, 0x74,
	0x4d, 0x65, 0x74, 0x61, 0x64, 0x61, 0x74, 0x61, 0x44, 0x61, 0x74, 0x61, 0x51, 0x75, 0x61, 0x6c,
	0x69, 0x74, 0x79, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x22, 0x35, 0x82, 0xd3, 0xe4,
	0x93, 0x02, 0x2f, 0x22, 0x2d, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x76, 0x31, 0x2f, 0x61, 0x6e, 0x61,
	0x6c, 0x79, 0x74, 0x69, 0x63, 0x73, 0x2f, 0x64, 0x61, 0x74, 0x61, 0x2d, 0x71, 0x75, 0x61, 0x6c,
	0x69, 0x74, 0x79, 0x2d, 0x65, 0x72, 0x72, 0x6f, 0x72, 0x73, 0x2f, 0x67, 0x65, 0x74, 0x2d, 0x61,
	0x6c, 0x6c, 0x12, 0xa3, 0x01, 0x0a, 0x16, 0x46, 0x69, 0x6e, 0x64, 0x43, 0x6f, 0x6e, 0x73, 0x65,
	0x6e, 0x73, 0x75, 0x73, 0x41, 0x6e, 0x61, 0x6c, 0x79, 0x74, 0x69, 0x63, 0x73, 0x12, 0x29, 0x2e,
	0x74, 0x69, 0x74, 0x61, 0x6e, 0x69, 0x75, 0x6d, 0x2e, 0x47, 0x65, 0x6e, 0x65, 0x72, 0x69, 0x63,
	0x43, 0x68, 0x61, 0x72, 0x74, 0x4d, 0x65, 0x74, 0x61, 0x64, 0x61, 0x74, 0x61, 0x44, 0x61, 0x74,
	0x61, 0x51, 0x75, 0x61, 0x6c, 0x69, 0x74, 0x79, 0x1a, 0x31, 0x2e, 0x74, 0x69, 0x74, 0x61, 0x6e,
	0x69, 0x75, 0x6d, 0x2e, 0x47, 0x65, 0x6e, 0x65, 0x72, 0x69, 0x63, 0x43, 0x68, 0x61, 0x72, 0x74,
	0x4d, 0x65, 0x74, 0x61, 0x64, 0x61, 0x74, 0x61, 0x44, 0x61, 0x74, 0x61, 0x51, 0x75, 0x61, 0x6c,
	0x69, 0x74, 0x79, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x22, 0x2b, 0x82, 0xd3, 0xe4,
	0x93, 0x02, 0x25, 0x22, 0x20, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x76, 0x31, 0x2f, 0x61, 0x6e, 0x61,
	0x6c, 0x79, 0x74, 0x69, 0x63, 0x73, 0x2f, 0x63, 0x6f, 0x6e, 0x73, 0x65, 0x6e, 0x73, 0x75, 0x73,
	0x2f, 0x66, 0x69, 0x6e, 0x64, 0x3a, 0x01, 0x2a, 0x12, 0x92, 0x01, 0x0a, 0x18, 0x47, 0x65, 0x74,
	0x41, 0x6c, 0x6c, 0x43, 0x6f, 0x6e, 0x73, 0x65, 0x6e, 0x73, 0x75, 0x73, 0x41, 0x6e, 0x61, 0x6c,
	0x79, 0x74, 0x69, 0x63, 0x73, 0x12, 0x16, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70,
	0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e, 0x45, 0x6d, 0x70, 0x74, 0x79, 0x1a, 0x31, 0x2e,
	0x74, 0x69, 0x74, 0x61, 0x6e, 0x69, 0x75, 0x6d, 0x2e, 0x47, 0x65, 0x6e, 0x65, 0x72, 0x69, 0x63,
	0x43, 0x68, 0x61, 0x72, 0x74, 0x4d, 0x65, 0x74, 0x61, 0x64, 0x61, 0x74, 0x61, 0x44, 0x61, 0x74,
	0x61, 0x51, 0x75, 0x61, 0x6c, 0x69, 0x74, 0x79, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65,
	0x22, 0x2b, 0x82, 0xd3, 0xe4, 0x93, 0x02, 0x25, 0x22, 0x23, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x76,
	0x31, 0x2f, 0x61, 0x6e, 0x61, 0x6c, 0x79, 0x74, 0x69, 0x63, 0x73, 0x2f, 0x63, 0x6f, 0x6e, 0x73,
	0x65, 0x6e, 0x73, 0x75, 0x73, 0x2f, 0x67, 0x65, 0x74, 0x2d, 0x61, 0x6c, 0x6c, 0x12, 0x92, 0x01,
	0x0a, 0x13, 0x47, 0x65, 0x74, 0x50, 0x72, 0x65, 0x64, 0x65, 0x66, 0x69, 0x6e, 0x65, 0x64, 0x46,
	0x69, 0x6c, 0x74, 0x65, 0x72, 0x12, 0x25, 0x2e, 0x74, 0x69, 0x74, 0x61, 0x6e, 0x69, 0x75, 0x6d,
	0x2e, 0x47, 0x65, 0x74, 0x50, 0x72, 0x65, 0x64, 0x65, 0x66, 0x69, 0x6e, 0x65, 0x64, 0x46, 0x69,
	0x6c, 0x74, 0x65, 0x72, 0x73, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x26, 0x2e, 0x74,
	0x69, 0x74, 0x61, 0x6e, 0x69, 0x75, 0x6d, 0x2e, 0x47, 0x65, 0x74, 0x50, 0x72, 0x65, 0x64, 0x65,
	0x66, 0x69, 0x6e, 0x65, 0x64, 0x46, 0x69, 0x6c, 0x74, 0x65, 0x72, 0x73, 0x52, 0x65, 0x73, 0x70,
	0x6f, 0x6e, 0x73, 0x65, 0x22, 0x2c, 0x82, 0xd3, 0xe4, 0x93, 0x02, 0x26, 0x22, 0x24, 0x2f, 0x61,
	0x70, 0x69, 0x2f, 0x76, 0x31, 0x2f, 0x61, 0x6e, 0x61, 0x6c, 0x79, 0x74, 0x69, 0x63, 0x73, 0x2f,
	0x70, 0x72, 0x65, 0x64, 0x65, 0x66, 0x69, 0x6e, 0x65, 0x64, 0x2f, 0x66, 0x69, 0x6c, 0x74, 0x65,
	0x72, 0x73, 0x12, 0x74, 0x0a, 0x0c, 0x47, 0x65, 0x74, 0x48, 0x69, 0x73, 0x74, 0x6f, 0x67, 0x72,
	0x61, 0x6d, 0x12, 0x1a, 0x2e, 0x74, 0x69, 0x74, 0x61, 0x6e, 0x69, 0x75, 0x6d, 0x2e, 0x48, 0x69,
	0x73, 0x74, 0x6f, 0x67, 0x72, 0x61, 0x6d, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x1b,
	0x2e, 0x74, 0x69, 0x74, 0x61, 0x6e, 0x69, 0x75, 0x6d, 0x2e, 0x48, 0x69, 0x73, 0x74, 0x6f, 0x67,
	0x72, 0x61, 0x6d, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x22, 0x2b, 0x82, 0xd3, 0xe4,
	0x93, 0x02, 0x25, 0x22, 0x23, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x76, 0x31, 0x2f, 0x61, 0x6e, 0x61,
	0x6c, 0x79, 0x74, 0x69, 0x63, 0x73, 0x2f, 0x68, 0x69, 0x73, 0x74, 0x6f, 0x67, 0x72, 0x61, 0x6d,
	0x2f, 0x67, 0x65, 0x74, 0x2d, 0x61, 0x6c, 0x6c, 0x42, 0x7a, 0x0a, 0x20, 0x63, 0x6f, 0x6d, 0x2e,
	0x70, 0x65, 0x65, 0x72, 0x6e, 0x6f, 0x76, 0x61, 0x2e, 0x74, 0x69, 0x74, 0x61, 0x6e, 0x69, 0x75,
	0x6d, 0x2e, 0x69, 0x6e, 0x74, 0x65, 0x72, 0x66, 0x61, 0x63, 0x65, 0x73, 0x42, 0x1e, 0x41, 0x6e,
	0x61, 0x6c, 0x79, 0x74, 0x69, 0x63, 0x73, 0x43, 0x6f, 0x6e, 0x74, 0x72, 0x6f, 0x6c, 0x6c, 0x65,
	0x72, 0x50, 0x72, 0x6f, 0x74, 0x6f, 0x50, 0x75, 0x62, 0x6c, 0x69, 0x63, 0x50, 0x01, 0x5a, 0x34,
	0x67, 0x69, 0x74, 0x68, 0x75, 0x62, 0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x70, 0x65, 0x65, 0x72, 0x6e,
	0x6f, 0x76, 0x61, 0x2f, 0x63, 0x6c, 0x65, 0x61, 0x72, 0x63, 0x6f, 0x6e, 0x73, 0x65, 0x6e, 0x73,
	0x75, 0x73, 0x2d, 0x73, 0x64, 0x6b, 0x2f, 0x73, 0x64, 0x6b, 0x2f, 0x67, 0x6f, 0x2f, 0x70, 0x75,
	0x62, 0x6c, 0x69, 0x63, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var file_public_analytics_service_proto_goTypes = []interface{}{
	(*common.GenericChartMetadataDataQuality)(nil),         // 0: titanium.GenericChartMetadataDataQuality
	(*emptypb.Empty)(nil),                                  // 1: google.protobuf.Empty
	(*common.GetPredefinedFiltersRequest)(nil),             // 2: titanium.GetPredefinedFiltersRequest
	(*common.HistogramRequest)(nil),                        // 3: titanium.HistogramRequest
	(*common.GenericChartMetadataDataQualityResponse)(nil), // 4: titanium.GenericChartMetadataDataQualityResponse
	(*common.GetPredefinedFiltersResponse)(nil),            // 5: titanium.GetPredefinedFiltersResponse
	(*common.HistogramResponse)(nil),                       // 6: titanium.HistogramResponse
}
var file_public_analytics_service_proto_depIdxs = []int32{
	0, // 0: titanium.AnalyticsController.FindDataQualityErrors:input_type -> titanium.GenericChartMetadataDataQuality
	1, // 1: titanium.AnalyticsController.GetAllDataQualityErrors:input_type -> google.protobuf.Empty
	0, // 2: titanium.AnalyticsController.FindConsensusAnalytics:input_type -> titanium.GenericChartMetadataDataQuality
	1, // 3: titanium.AnalyticsController.GetAllConsensusAnalytics:input_type -> google.protobuf.Empty
	2, // 4: titanium.AnalyticsController.GetPredefinedFilter:input_type -> titanium.GetPredefinedFiltersRequest
	3, // 5: titanium.AnalyticsController.GetHistogram:input_type -> titanium.HistogramRequest
	4, // 6: titanium.AnalyticsController.FindDataQualityErrors:output_type -> titanium.GenericChartMetadataDataQualityResponse
	4, // 7: titanium.AnalyticsController.GetAllDataQualityErrors:output_type -> titanium.GenericChartMetadataDataQualityResponse
	4, // 8: titanium.AnalyticsController.FindConsensusAnalytics:output_type -> titanium.GenericChartMetadataDataQualityResponse
	4, // 9: titanium.AnalyticsController.GetAllConsensusAnalytics:output_type -> titanium.GenericChartMetadataDataQualityResponse
	5, // 10: titanium.AnalyticsController.GetPredefinedFilter:output_type -> titanium.GetPredefinedFiltersResponse
	6, // 11: titanium.AnalyticsController.GetHistogram:output_type -> titanium.HistogramResponse
	6, // [6:12] is the sub-list for method output_type
	0, // [0:6] is the sub-list for method input_type
	0, // [0:0] is the sub-list for extension type_name
	0, // [0:0] is the sub-list for extension extendee
	0, // [0:0] is the sub-list for field type_name
}

func init() { file_public_analytics_service_proto_init() }
func file_public_analytics_service_proto_init() {
	if File_public_analytics_service_proto != nil {
		return
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_public_analytics_service_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   0,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_public_analytics_service_proto_goTypes,
		DependencyIndexes: file_public_analytics_service_proto_depIdxs,
	}.Build()
	File_public_analytics_service_proto = out.File
	file_public_analytics_service_proto_rawDesc = nil
	file_public_analytics_service_proto_goTypes = nil
	file_public_analytics_service_proto_depIdxs = nil
}
