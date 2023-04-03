/* eslint-disable */
/*Generated by GenDocu.com*/
// package: titanium
// file: public/outliers_service.proto

import * as public_outliers_service_pb from "../public/outliers_service_pb";
import * as common_outliers_pb from "../common/outliers_pb";
import {grpc} from "@improbable-eng/grpc-web";

type OutliersServiceOutliers = {
  readonly methodName: string;
  readonly service: typeof OutliersService;
  readonly requestStream: false;
  readonly responseStream: false;
  readonly requestType: typeof common_outliers_pb.OutliersRequest;
  readonly responseType: typeof common_outliers_pb.OutliersResponse;
};

export class OutliersService {
  static readonly serviceName: string;
  static readonly Outliers: OutliersServiceOutliers;
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

export class OutliersServiceClient {
  readonly serviceHost: string;

  constructor(serviceHost: string, options?: grpc.RpcOptions);
  outliers(
    requestMessage: common_outliers_pb.OutliersRequest,
    metadata: grpc.Metadata,
    callback: (error: ServiceError|null, responseMessage: common_outliers_pb.OutliersResponse|null) => void
  ): UnaryResponse;
  outliers(
    requestMessage: common_outliers_pb.OutliersRequest,
    callback: (error: ServiceError|null, responseMessage: common_outliers_pb.OutliersResponse|null) => void
  ): UnaryResponse;
}

