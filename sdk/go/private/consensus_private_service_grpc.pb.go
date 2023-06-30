// Code generated by protoc-gen-go-grpc. DO NOT EDIT.

package private

import (
	context "context"
	common "github.com/peernova/clearconsensus-sdk/sdk/go/common"
	public "github.com/peernova/clearconsensus-sdk/sdk/go/public"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
)

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
// Requires gRPC-Go v1.32.0 or later.
const _ = grpc.SupportPackageIsVersion7

// ConsensusServicePrivateClient is the client API for ConsensusServicePrivate service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type ConsensusServicePrivateClient interface {
	ConsensusActive(ctx context.Context, in *public.ConsensusActiveRequest, opts ...grpc.CallOption) (*common.ConsensusActiveResponse, error)
	ConsensusToPublish(ctx context.Context, in *public.ConsensusToPublishRequest, opts ...grpc.CallOption) (*public.ConsensusToPublishResponse, error)
	ConsensusPublish(ctx context.Context, in *public.ConsensusPublishRequest, opts ...grpc.CallOption) (*common.MessageResponse, error)
	ConsensusHistory(ctx context.Context, in *public.ConsensusHistoryRequest, opts ...grpc.CallOption) (*public.ConsensusHistoryResponse, error)
	ConsensusDecision(ctx context.Context, in *public.ConsensusDecisionRequest, opts ...grpc.CallOption) (*common.MessageResponse, error)
}

type consensusServicePrivateClient struct {
	cc grpc.ClientConnInterface
}

func NewConsensusServicePrivateClient(cc grpc.ClientConnInterface) ConsensusServicePrivateClient {
	return &consensusServicePrivateClient{cc}
}

func (c *consensusServicePrivateClient) ConsensusActive(ctx context.Context, in *public.ConsensusActiveRequest, opts ...grpc.CallOption) (*common.ConsensusActiveResponse, error) {
	out := new(common.ConsensusActiveResponse)
	err := c.cc.Invoke(ctx, "/titanium.ConsensusServicePrivate/ConsensusActive", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *consensusServicePrivateClient) ConsensusToPublish(ctx context.Context, in *public.ConsensusToPublishRequest, opts ...grpc.CallOption) (*public.ConsensusToPublishResponse, error) {
	out := new(public.ConsensusToPublishResponse)
	err := c.cc.Invoke(ctx, "/titanium.ConsensusServicePrivate/ConsensusToPublish", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *consensusServicePrivateClient) ConsensusPublish(ctx context.Context, in *public.ConsensusPublishRequest, opts ...grpc.CallOption) (*common.MessageResponse, error) {
	out := new(common.MessageResponse)
	err := c.cc.Invoke(ctx, "/titanium.ConsensusServicePrivate/ConsensusPublish", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *consensusServicePrivateClient) ConsensusHistory(ctx context.Context, in *public.ConsensusHistoryRequest, opts ...grpc.CallOption) (*public.ConsensusHistoryResponse, error) {
	out := new(public.ConsensusHistoryResponse)
	err := c.cc.Invoke(ctx, "/titanium.ConsensusServicePrivate/ConsensusHistory", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *consensusServicePrivateClient) ConsensusDecision(ctx context.Context, in *public.ConsensusDecisionRequest, opts ...grpc.CallOption) (*common.MessageResponse, error) {
	out := new(common.MessageResponse)
	err := c.cc.Invoke(ctx, "/titanium.ConsensusServicePrivate/ConsensusDecision", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// ConsensusServicePrivateServer is the server API for ConsensusServicePrivate service.
// All implementations must embed UnimplementedConsensusServicePrivateServer
// for forward compatibility
type ConsensusServicePrivateServer interface {
	ConsensusActive(context.Context, *public.ConsensusActiveRequest) (*common.ConsensusActiveResponse, error)
	ConsensusToPublish(context.Context, *public.ConsensusToPublishRequest) (*public.ConsensusToPublishResponse, error)
	ConsensusPublish(context.Context, *public.ConsensusPublishRequest) (*common.MessageResponse, error)
	ConsensusHistory(context.Context, *public.ConsensusHistoryRequest) (*public.ConsensusHistoryResponse, error)
	ConsensusDecision(context.Context, *public.ConsensusDecisionRequest) (*common.MessageResponse, error)
	mustEmbedUnimplementedConsensusServicePrivateServer()
}

// UnimplementedConsensusServicePrivateServer must be embedded to have forward compatible implementations.
type UnimplementedConsensusServicePrivateServer struct {
}

func (UnimplementedConsensusServicePrivateServer) ConsensusActive(context.Context, *public.ConsensusActiveRequest) (*common.ConsensusActiveResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ConsensusActive not implemented")
}
func (UnimplementedConsensusServicePrivateServer) ConsensusToPublish(context.Context, *public.ConsensusToPublishRequest) (*public.ConsensusToPublishResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ConsensusToPublish not implemented")
}
func (UnimplementedConsensusServicePrivateServer) ConsensusPublish(context.Context, *public.ConsensusPublishRequest) (*common.MessageResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ConsensusPublish not implemented")
}
func (UnimplementedConsensusServicePrivateServer) ConsensusHistory(context.Context, *public.ConsensusHistoryRequest) (*public.ConsensusHistoryResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ConsensusHistory not implemented")
}
func (UnimplementedConsensusServicePrivateServer) ConsensusDecision(context.Context, *public.ConsensusDecisionRequest) (*common.MessageResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ConsensusDecision not implemented")
}
func (UnimplementedConsensusServicePrivateServer) mustEmbedUnimplementedConsensusServicePrivateServer() {
}

// UnsafeConsensusServicePrivateServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to ConsensusServicePrivateServer will
// result in compilation errors.
type UnsafeConsensusServicePrivateServer interface {
	mustEmbedUnimplementedConsensusServicePrivateServer()
}

func RegisterConsensusServicePrivateServer(s grpc.ServiceRegistrar, srv ConsensusServicePrivateServer) {
	s.RegisterService(&ConsensusServicePrivate_ServiceDesc, srv)
}

func _ConsensusServicePrivate_ConsensusActive_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(public.ConsensusActiveRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ConsensusServicePrivateServer).ConsensusActive(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/titanium.ConsensusServicePrivate/ConsensusActive",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ConsensusServicePrivateServer).ConsensusActive(ctx, req.(*public.ConsensusActiveRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _ConsensusServicePrivate_ConsensusToPublish_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(public.ConsensusToPublishRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ConsensusServicePrivateServer).ConsensusToPublish(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/titanium.ConsensusServicePrivate/ConsensusToPublish",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ConsensusServicePrivateServer).ConsensusToPublish(ctx, req.(*public.ConsensusToPublishRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _ConsensusServicePrivate_ConsensusPublish_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(public.ConsensusPublishRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ConsensusServicePrivateServer).ConsensusPublish(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/titanium.ConsensusServicePrivate/ConsensusPublish",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ConsensusServicePrivateServer).ConsensusPublish(ctx, req.(*public.ConsensusPublishRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _ConsensusServicePrivate_ConsensusHistory_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(public.ConsensusHistoryRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ConsensusServicePrivateServer).ConsensusHistory(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/titanium.ConsensusServicePrivate/ConsensusHistory",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ConsensusServicePrivateServer).ConsensusHistory(ctx, req.(*public.ConsensusHistoryRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _ConsensusServicePrivate_ConsensusDecision_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(public.ConsensusDecisionRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ConsensusServicePrivateServer).ConsensusDecision(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/titanium.ConsensusServicePrivate/ConsensusDecision",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ConsensusServicePrivateServer).ConsensusDecision(ctx, req.(*public.ConsensusDecisionRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// ConsensusServicePrivate_ServiceDesc is the grpc.ServiceDesc for ConsensusServicePrivate service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var ConsensusServicePrivate_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "titanium.ConsensusServicePrivate",
	HandlerType: (*ConsensusServicePrivateServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "ConsensusActive",
			Handler:    _ConsensusServicePrivate_ConsensusActive_Handler,
		},
		{
			MethodName: "ConsensusToPublish",
			Handler:    _ConsensusServicePrivate_ConsensusToPublish_Handler,
		},
		{
			MethodName: "ConsensusPublish",
			Handler:    _ConsensusServicePrivate_ConsensusPublish_Handler,
		},
		{
			MethodName: "ConsensusHistory",
			Handler:    _ConsensusServicePrivate_ConsensusHistory_Handler,
		},
		{
			MethodName: "ConsensusDecision",
			Handler:    _ConsensusServicePrivate_ConsensusDecision_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "private/consensus_private_service.proto",
}
