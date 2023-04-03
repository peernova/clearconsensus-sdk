// Code generated by protoc-gen-go-grpc. DO NOT EDIT.

package public

import (
	context "context"
	common "github.com/peernova/clearconsensus-sdk/sdk/go/common"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
)

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
// Requires gRPC-Go v1.32.0 or later.
const _ = grpc.SupportPackageIsVersion7

// OutliersServiceClient is the client API for OutliersService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type OutliersServiceClient interface {
	// Outliers returns outliers according to request.
	Outliers(ctx context.Context, in *common.OutliersRequest, opts ...grpc.CallOption) (*common.OutliersResponse, error)
}

type outliersServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewOutliersServiceClient(cc grpc.ClientConnInterface) OutliersServiceClient {
	return &outliersServiceClient{cc}
}

func (c *outliersServiceClient) Outliers(ctx context.Context, in *common.OutliersRequest, opts ...grpc.CallOption) (*common.OutliersResponse, error) {
	out := new(common.OutliersResponse)
	err := c.cc.Invoke(ctx, "/titanium.OutliersService/Outliers", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// OutliersServiceServer is the server API for OutliersService service.
// All implementations must embed UnimplementedOutliersServiceServer
// for forward compatibility
type OutliersServiceServer interface {
	// Outliers returns outliers according to request.
	Outliers(context.Context, *common.OutliersRequest) (*common.OutliersResponse, error)
	mustEmbedUnimplementedOutliersServiceServer()
}

// UnimplementedOutliersServiceServer must be embedded to have forward compatible implementations.
type UnimplementedOutliersServiceServer struct {
}

func (UnimplementedOutliersServiceServer) Outliers(context.Context, *common.OutliersRequest) (*common.OutliersResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Outliers not implemented")
}
func (UnimplementedOutliersServiceServer) mustEmbedUnimplementedOutliersServiceServer() {}

// UnsafeOutliersServiceServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to OutliersServiceServer will
// result in compilation errors.
type UnsafeOutliersServiceServer interface {
	mustEmbedUnimplementedOutliersServiceServer()
}

func RegisterOutliersServiceServer(s grpc.ServiceRegistrar, srv OutliersServiceServer) {
	s.RegisterService(&OutliersService_ServiceDesc, srv)
}

func _OutliersService_Outliers_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(common.OutliersRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(OutliersServiceServer).Outliers(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/titanium.OutliersService/Outliers",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(OutliersServiceServer).Outliers(ctx, req.(*common.OutliersRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// OutliersService_ServiceDesc is the grpc.ServiceDesc for OutliersService service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var OutliersService_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "titanium.OutliersService",
	HandlerType: (*OutliersServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "Outliers",
			Handler:    _OutliersService_Outliers_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "public/outliers_service.proto",
}
