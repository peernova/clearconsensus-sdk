// Code generated by protoc-gen-go-grpc. DO NOT EDIT.

package public

import (
	context "context"
	common "github.com/peernova/clearconsensus-sdk/sdk/go/common"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
	wrapperspb "google.golang.org/protobuf/types/known/wrapperspb"
)

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
// Requires gRPC-Go v1.32.0 or later.
const _ = grpc.SupportPackageIsVersion7

// PolicyServiceClient is the client API for PolicyService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type PolicyServiceClient interface {
	Create(ctx context.Context, in *common.Policies, opts ...grpc.CallOption) (*common.ServiceResponse, error)
	GetPolicies(ctx context.Context, in *wrapperspb.StringValue, opts ...grpc.CallOption) (*common.ServiceResponse, error)
	RemovePolicy(ctx context.Context, in *common.PolicyDto, opts ...grpc.CallOption) (*common.ServiceResponse, error)
	CheckPolicy(ctx context.Context, in *common.PolicyDto, opts ...grpc.CallOption) (*common.ServiceResponse, error)
	GetAssets(ctx context.Context, in *common.UsernamePermissionRequest, opts ...grpc.CallOption) (*common.ServiceResponse, error)
	GetApis(ctx context.Context, in *common.UsernamePermissionRequest, opts ...grpc.CallOption) (*common.ServiceResponse, error)
	GetAddons(ctx context.Context, in *common.UsernamePermissionRequest, opts ...grpc.CallOption) (*common.ServiceResponse, error)
}

type policyServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewPolicyServiceClient(cc grpc.ClientConnInterface) PolicyServiceClient {
	return &policyServiceClient{cc}
}

func (c *policyServiceClient) Create(ctx context.Context, in *common.Policies, opts ...grpc.CallOption) (*common.ServiceResponse, error) {
	out := new(common.ServiceResponse)
	err := c.cc.Invoke(ctx, "/com.peernova.titanium.casbin.management.grpc.service.PolicyService/create", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *policyServiceClient) GetPolicies(ctx context.Context, in *wrapperspb.StringValue, opts ...grpc.CallOption) (*common.ServiceResponse, error) {
	out := new(common.ServiceResponse)
	err := c.cc.Invoke(ctx, "/com.peernova.titanium.casbin.management.grpc.service.PolicyService/getPolicies", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *policyServiceClient) RemovePolicy(ctx context.Context, in *common.PolicyDto, opts ...grpc.CallOption) (*common.ServiceResponse, error) {
	out := new(common.ServiceResponse)
	err := c.cc.Invoke(ctx, "/com.peernova.titanium.casbin.management.grpc.service.PolicyService/removePolicy", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *policyServiceClient) CheckPolicy(ctx context.Context, in *common.PolicyDto, opts ...grpc.CallOption) (*common.ServiceResponse, error) {
	out := new(common.ServiceResponse)
	err := c.cc.Invoke(ctx, "/com.peernova.titanium.casbin.management.grpc.service.PolicyService/checkPolicy", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *policyServiceClient) GetAssets(ctx context.Context, in *common.UsernamePermissionRequest, opts ...grpc.CallOption) (*common.ServiceResponse, error) {
	out := new(common.ServiceResponse)
	err := c.cc.Invoke(ctx, "/com.peernova.titanium.casbin.management.grpc.service.PolicyService/getAssets", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *policyServiceClient) GetApis(ctx context.Context, in *common.UsernamePermissionRequest, opts ...grpc.CallOption) (*common.ServiceResponse, error) {
	out := new(common.ServiceResponse)
	err := c.cc.Invoke(ctx, "/com.peernova.titanium.casbin.management.grpc.service.PolicyService/getApis", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *policyServiceClient) GetAddons(ctx context.Context, in *common.UsernamePermissionRequest, opts ...grpc.CallOption) (*common.ServiceResponse, error) {
	out := new(common.ServiceResponse)
	err := c.cc.Invoke(ctx, "/com.peernova.titanium.casbin.management.grpc.service.PolicyService/getAddons", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// PolicyServiceServer is the server API for PolicyService service.
// All implementations must embed UnimplementedPolicyServiceServer
// for forward compatibility
type PolicyServiceServer interface {
	Create(context.Context, *common.Policies) (*common.ServiceResponse, error)
	GetPolicies(context.Context, *wrapperspb.StringValue) (*common.ServiceResponse, error)
	RemovePolicy(context.Context, *common.PolicyDto) (*common.ServiceResponse, error)
	CheckPolicy(context.Context, *common.PolicyDto) (*common.ServiceResponse, error)
	GetAssets(context.Context, *common.UsernamePermissionRequest) (*common.ServiceResponse, error)
	GetApis(context.Context, *common.UsernamePermissionRequest) (*common.ServiceResponse, error)
	GetAddons(context.Context, *common.UsernamePermissionRequest) (*common.ServiceResponse, error)
	mustEmbedUnimplementedPolicyServiceServer()
}

// UnimplementedPolicyServiceServer must be embedded to have forward compatible implementations.
type UnimplementedPolicyServiceServer struct {
}

func (UnimplementedPolicyServiceServer) Create(context.Context, *common.Policies) (*common.ServiceResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Create not implemented")
}
func (UnimplementedPolicyServiceServer) GetPolicies(context.Context, *wrapperspb.StringValue) (*common.ServiceResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetPolicies not implemented")
}
func (UnimplementedPolicyServiceServer) RemovePolicy(context.Context, *common.PolicyDto) (*common.ServiceResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method RemovePolicy not implemented")
}
func (UnimplementedPolicyServiceServer) CheckPolicy(context.Context, *common.PolicyDto) (*common.ServiceResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method CheckPolicy not implemented")
}
func (UnimplementedPolicyServiceServer) GetAssets(context.Context, *common.UsernamePermissionRequest) (*common.ServiceResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetAssets not implemented")
}
func (UnimplementedPolicyServiceServer) GetApis(context.Context, *common.UsernamePermissionRequest) (*common.ServiceResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetApis not implemented")
}
func (UnimplementedPolicyServiceServer) GetAddons(context.Context, *common.UsernamePermissionRequest) (*common.ServiceResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetAddons not implemented")
}
func (UnimplementedPolicyServiceServer) mustEmbedUnimplementedPolicyServiceServer() {}

// UnsafePolicyServiceServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to PolicyServiceServer will
// result in compilation errors.
type UnsafePolicyServiceServer interface {
	mustEmbedUnimplementedPolicyServiceServer()
}

func RegisterPolicyServiceServer(s grpc.ServiceRegistrar, srv PolicyServiceServer) {
	s.RegisterService(&PolicyService_ServiceDesc, srv)
}

func _PolicyService_Create_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(common.Policies)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(PolicyServiceServer).Create(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.peernova.titanium.casbin.management.grpc.service.PolicyService/create",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(PolicyServiceServer).Create(ctx, req.(*common.Policies))
	}
	return interceptor(ctx, in, info, handler)
}

func _PolicyService_GetPolicies_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(wrapperspb.StringValue)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(PolicyServiceServer).GetPolicies(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.peernova.titanium.casbin.management.grpc.service.PolicyService/getPolicies",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(PolicyServiceServer).GetPolicies(ctx, req.(*wrapperspb.StringValue))
	}
	return interceptor(ctx, in, info, handler)
}

func _PolicyService_RemovePolicy_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(common.PolicyDto)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(PolicyServiceServer).RemovePolicy(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.peernova.titanium.casbin.management.grpc.service.PolicyService/removePolicy",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(PolicyServiceServer).RemovePolicy(ctx, req.(*common.PolicyDto))
	}
	return interceptor(ctx, in, info, handler)
}

func _PolicyService_CheckPolicy_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(common.PolicyDto)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(PolicyServiceServer).CheckPolicy(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.peernova.titanium.casbin.management.grpc.service.PolicyService/checkPolicy",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(PolicyServiceServer).CheckPolicy(ctx, req.(*common.PolicyDto))
	}
	return interceptor(ctx, in, info, handler)
}

func _PolicyService_GetAssets_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(common.UsernamePermissionRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(PolicyServiceServer).GetAssets(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.peernova.titanium.casbin.management.grpc.service.PolicyService/getAssets",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(PolicyServiceServer).GetAssets(ctx, req.(*common.UsernamePermissionRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _PolicyService_GetApis_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(common.UsernamePermissionRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(PolicyServiceServer).GetApis(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.peernova.titanium.casbin.management.grpc.service.PolicyService/getApis",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(PolicyServiceServer).GetApis(ctx, req.(*common.UsernamePermissionRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _PolicyService_GetAddons_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(common.UsernamePermissionRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(PolicyServiceServer).GetAddons(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.peernova.titanium.casbin.management.grpc.service.PolicyService/getAddons",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(PolicyServiceServer).GetAddons(ctx, req.(*common.UsernamePermissionRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// PolicyService_ServiceDesc is the grpc.ServiceDesc for PolicyService service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var PolicyService_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "com.peernova.titanium.casbin.management.grpc.service.PolicyService",
	HandlerType: (*PolicyServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "create",
			Handler:    _PolicyService_Create_Handler,
		},
		{
			MethodName: "getPolicies",
			Handler:    _PolicyService_GetPolicies_Handler,
		},
		{
			MethodName: "removePolicy",
			Handler:    _PolicyService_RemovePolicy_Handler,
		},
		{
			MethodName: "checkPolicy",
			Handler:    _PolicyService_CheckPolicy_Handler,
		},
		{
			MethodName: "getAssets",
			Handler:    _PolicyService_GetAssets_Handler,
		},
		{
			MethodName: "getApis",
			Handler:    _PolicyService_GetApis_Handler,
		},
		{
			MethodName: "getAddons",
			Handler:    _PolicyService_GetAddons_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "public/usermanagement_policy_service.proto",
}
