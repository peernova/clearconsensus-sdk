/* eslint-disable */
/*Generated by GenDocu.com*/
// package: titanium
// file: public/scope_service.proto

import * as public_scope_service_pb from "../public/scope_service_pb";
import * as google_protobuf_empty_pb from "google-protobuf/google/protobuf/empty_pb";
import * as common_gateway_base_pb from "../common/gateway_base_pb";
import * as common_scope_pb from "../common/scope_pb";
import {grpc} from "@improbable-eng/grpc-web";

type ScopeServiceAddScope = {
  readonly methodName: string;
  readonly service: typeof ScopeService;
  readonly requestStream: false;
  readonly responseStream: false;
  readonly requestType: typeof common_scope_pb.ScopeIdentifier;
  readonly responseType: typeof common_gateway_base_pb.AcknowledgeResponse;
};

type ScopeServiceExistScope = {
  readonly methodName: string;
  readonly service: typeof ScopeService;
  readonly requestStream: false;
  readonly responseStream: false;
  readonly requestType: typeof common_scope_pb.ScopeIdentifier;
  readonly responseType: typeof common_scope_pb.ScopeExistResponse;
};

type ScopeServiceListScope = {
  readonly methodName: string;
  readonly service: typeof ScopeService;
  readonly requestStream: false;
  readonly responseStream: false;
  readonly requestType: typeof google_protobuf_empty_pb.Empty;
  readonly responseType: typeof common_scope_pb.ScopeListResponse;
};

export class ScopeService {
  static readonly serviceName: string;
  static readonly AddScope: ScopeServiceAddScope;
  static readonly ExistScope: ScopeServiceExistScope;
  static readonly ListScope: ScopeServiceListScope;
}

export type ServiceError = { message: string, code: number; metadata: grpc.Metadata }
export type Status = { details: string, code: number; metadata: grpc.Metadata }

interface UnaryResponse {
  cancel(): void;
}
interface ResponseStream<T> {
  cancel(): void;
  on(type: 'data', handler: (message: T) => void): ResponseStream<T>;
  on(type: 'end', handler: (status?: Status) => void): ResponseStream<T>;
  on(type: 'status', handler: (status: Status) => void): ResponseStream<T>;
}
interface RequestStream<T> {
  write(message: T): RequestStream<T>;
  end(): void;
  cancel(): void;
  on(type: 'end', handler: (status?: Status) => void): RequestStream<T>;
  on(type: 'status', handler: (status: Status) => void): RequestStream<T>;
}
interface BidirectionalStream<ReqT, ResT> {
  write(message: ReqT): BidirectionalStream<ReqT, ResT>;
  end(): void;
  cancel(): void;
  on(type: 'data', handler: (message: ResT) => void): BidirectionalStream<ReqT, ResT>;
  on(type: 'end', handler: (status?: Status) => void): BidirectionalStream<ReqT, ResT>;
  on(type: 'status', handler: (status: Status) => void): BidirectionalStream<ReqT, ResT>;
}

export class ScopeServiceClient {
  readonly serviceHost: string;

  constructor(serviceHost: string, options?: grpc.RpcOptions);
  addScope(
    requestMessage: common_scope_pb.ScopeIdentifier,
    metadata: grpc.Metadata,
    callback: (error: ServiceError|null, responseMessage: common_gateway_base_pb.AcknowledgeResponse|null) => void
  ): UnaryResponse;
  addScope(
    requestMessage: common_scope_pb.ScopeIdentifier,
    callback: (error: ServiceError|null, responseMessage: common_gateway_base_pb.AcknowledgeResponse|null) => void
  ): UnaryResponse;
  existScope(
    requestMessage: common_scope_pb.ScopeIdentifier,
    metadata: grpc.Metadata,
    callback: (error: ServiceError|null, responseMessage: common_scope_pb.ScopeExistResponse|null) => void
  ): UnaryResponse;
  existScope(
    requestMessage: common_scope_pb.ScopeIdentifier,
    callback: (error: ServiceError|null, responseMessage: common_scope_pb.ScopeExistResponse|null) => void
  ): UnaryResponse;
  listScope(
    requestMessage: google_protobuf_empty_pb.Empty,
    metadata: grpc.Metadata,
    callback: (error: ServiceError|null, responseMessage: common_scope_pb.ScopeListResponse|null) => void
  ): UnaryResponse;
  listScope(
    requestMessage: google_protobuf_empty_pb.Empty,
    callback: (error: ServiceError|null, responseMessage: common_scope_pb.ScopeListResponse|null) => void
  ): UnaryResponse;
}

