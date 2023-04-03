/* eslint-disable */
/*Generated by GenDocu.com*/
// package: titanium
// file: common/descriptor.proto

import * as jspb from "google-protobuf";
import * as common_gateway_base_pb from "../common/gateway_base_pb";

export class DescriptorDefinitionResponse extends jspb.Message {
  hasData(): boolean;
  clearData(): void;
  getData(): string;
  setData(value: string): void;

  hasError(): boolean;
  clearError(): void;
  getError(): common_gateway_base_pb.Error | undefined;
  setError(value?: common_gateway_base_pb.Error): void;

  getResponseCase(): DescriptorDefinitionResponse.ResponseCase;
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DescriptorDefinitionResponse.AsObject;
  static toObject(includeInstance: boolean, msg: DescriptorDefinitionResponse): DescriptorDefinitionResponse.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DescriptorDefinitionResponse, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DescriptorDefinitionResponse;
  static deserializeBinaryFromReader(message: DescriptorDefinitionResponse, reader: jspb.BinaryReader): DescriptorDefinitionResponse;
}

export namespace DescriptorDefinitionResponse {
  export type AsObject = {
    data: string,
    error?: common_gateway_base_pb.Error.AsObject,
  }

  export enum ResponseCase {
    RESPONSE_NOT_SET = 0,
    DATA = 1,
    ERROR = 2,
  }
}

export class DescriptorList extends jspb.Message {
  hasData(): boolean;
  clearData(): void;
  getData(): common_gateway_base_pb.ResultsList | undefined;
  setData(value?: common_gateway_base_pb.ResultsList): void;

  hasError(): boolean;
  clearError(): void;
  getError(): common_gateway_base_pb.Error | undefined;
  setError(value?: common_gateway_base_pb.Error): void;

  getResponseCase(): DescriptorList.ResponseCase;
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DescriptorList.AsObject;
  static toObject(includeInstance: boolean, msg: DescriptorList): DescriptorList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DescriptorList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DescriptorList;
  static deserializeBinaryFromReader(message: DescriptorList, reader: jspb.BinaryReader): DescriptorList;
}

export namespace DescriptorList {
  export type AsObject = {
    data?: common_gateway_base_pb.ResultsList.AsObject,
    error?: common_gateway_base_pb.Error.AsObject,
  }

  export enum ResponseCase {
    RESPONSE_NOT_SET = 0,
    DATA = 1,
    ERROR = 2,
  }
}

