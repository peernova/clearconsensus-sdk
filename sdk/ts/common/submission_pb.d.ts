/* eslint-disable */
/*Generated by GenDocu.com*/
// package: titanium
// file: common/submission.proto

import * as jspb from "google-protobuf";
import * as common_gateway_base_pb from "../common/gateway_base_pb";

export class GetSubmissionFilesRequest extends jspb.Message {
  getAssetId(): string;
  setAssetId(value: string): void;

  getTraceName(): string;
  setTraceName(value: string): void;

  getSnapDateFrom(): string;
  setSnapDateFrom(value: string): void;

  getSnapDateTo(): string;
  setSnapDateTo(value: string): void;

  hasOrderBy(): boolean;
  clearOrderBy(): void;
  getOrderBy(): common_gateway_base_pb.OrderBy | undefined;
  setOrderBy(value?: common_gateway_base_pb.OrderBy): void;

  hasFilterPack(): boolean;
  clearFilterPack(): void;
  getFilterPack(): common_gateway_base_pb.FilterPack | undefined;
  setFilterPack(value?: common_gateway_base_pb.FilterPack): void;

  hasPage(): boolean;
  clearPage(): void;
  getPage(): common_gateway_base_pb.Page | undefined;
  setPage(value?: common_gateway_base_pb.Page): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetSubmissionFilesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetSubmissionFilesRequest): GetSubmissionFilesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetSubmissionFilesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetSubmissionFilesRequest;
  static deserializeBinaryFromReader(message: GetSubmissionFilesRequest, reader: jspb.BinaryReader): GetSubmissionFilesRequest;
}

export namespace GetSubmissionFilesRequest {
  export type AsObject = {
    assetId: string,
    traceName: string,
    snapDateFrom: string,
    snapDateTo: string,
    orderBy?: common_gateway_base_pb.OrderBy.AsObject,
    filterPack?: common_gateway_base_pb.FilterPack.AsObject,
    page?: common_gateway_base_pb.Page.AsObject,
  }
}

export class GetSubmissionFilesResponse extends jspb.Message {
  hasError(): boolean;
  clearError(): void;
  getError(): common_gateway_base_pb.Error | undefined;
  setError(value?: common_gateway_base_pb.Error): void;

  hasData(): boolean;
  clearData(): void;
  getData(): GetSubmissionFilesData | undefined;
  setData(value?: GetSubmissionFilesData): void;

  getResponseCase(): GetSubmissionFilesResponse.ResponseCase;
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetSubmissionFilesResponse.AsObject;
  static toObject(includeInstance: boolean, msg: GetSubmissionFilesResponse): GetSubmissionFilesResponse.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetSubmissionFilesResponse, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetSubmissionFilesResponse;
  static deserializeBinaryFromReader(message: GetSubmissionFilesResponse, reader: jspb.BinaryReader): GetSubmissionFilesResponse;
}

export namespace GetSubmissionFilesResponse {
  export type AsObject = {
    error?: common_gateway_base_pb.Error.AsObject,
    data?: GetSubmissionFilesData.AsObject,
  }

  export enum ResponseCase {
    RESPONSE_NOT_SET = 0,
    ERROR = 1,
    DATA = 2,
  }
}

export class GetSubmissionFilesData extends jspb.Message {
  clearColumnsList(): void;
  getColumnsList(): Array<common_gateway_base_pb.ColumnInfo>;
  setColumnsList(value: Array<common_gateway_base_pb.ColumnInfo>): void;
  addColumns(value?: common_gateway_base_pb.ColumnInfo, index?: number): common_gateway_base_pb.ColumnInfo;

  clearRowsList(): void;
  getRowsList(): Array<common_gateway_base_pb.ValuesRow>;
  setRowsList(value: Array<common_gateway_base_pb.ValuesRow>): void;
  addRows(value?: common_gateway_base_pb.ValuesRow, index?: number): common_gateway_base_pb.ValuesRow;

  hasPage(): boolean;
  clearPage(): void;
  getPage(): common_gateway_base_pb.Page | undefined;
  setPage(value?: common_gateway_base_pb.Page): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetSubmissionFilesData.AsObject;
  static toObject(includeInstance: boolean, msg: GetSubmissionFilesData): GetSubmissionFilesData.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetSubmissionFilesData, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetSubmissionFilesData;
  static deserializeBinaryFromReader(message: GetSubmissionFilesData, reader: jspb.BinaryReader): GetSubmissionFilesData;
}

export namespace GetSubmissionFilesData {
  export type AsObject = {
    columnsList: Array<common_gateway_base_pb.ColumnInfo.AsObject>,
    rowsList: Array<common_gateway_base_pb.ValuesRow.AsObject>,
    page?: common_gateway_base_pb.Page.AsObject,
  }
}

