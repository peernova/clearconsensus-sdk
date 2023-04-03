/* eslint-disable */
/*Generated by GenDocu.com*/
// package: titanium
// file: common/user_controller.proto

import * as jspb from "google-protobuf";
import * as common_gateway_base_pb from "../common/gateway_base_pb";

export class GetUserRequest extends jspb.Message {
  getEmail(): string;
  setEmail(value: string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetUserRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetUserRequest): GetUserRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetUserRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetUserRequest;
  static deserializeBinaryFromReader(message: GetUserRequest, reader: jspb.BinaryReader): GetUserRequest;
}

export namespace GetUserRequest {
  export type AsObject = {
    email: string,
  }
}

export class UserRequest extends jspb.Message {
  hasUser(): boolean;
  clearUser(): void;
  getUser(): User | undefined;
  setUser(value?: User): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UserRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UserRequest): UserRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UserRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UserRequest;
  static deserializeBinaryFromReader(message: UserRequest, reader: jspb.BinaryReader): UserRequest;
}

export namespace UserRequest {
  export type AsObject = {
    user?: User.AsObject,
  }
}

export class UserResponse extends jspb.Message {
  hasUser(): boolean;
  clearUser(): void;
  getUser(): User | undefined;
  setUser(value?: User): void;

  hasError(): boolean;
  clearError(): void;
  getError(): common_gateway_base_pb.Error | undefined;
  setError(value?: common_gateway_base_pb.Error): void;

  getResponseCase(): UserResponse.ResponseCase;
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UserResponse.AsObject;
  static toObject(includeInstance: boolean, msg: UserResponse): UserResponse.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UserResponse, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UserResponse;
  static deserializeBinaryFromReader(message: UserResponse, reader: jspb.BinaryReader): UserResponse;
}

export namespace UserResponse {
  export type AsObject = {
    user?: User.AsObject,
    error?: common_gateway_base_pb.Error.AsObject,
  }

  export enum ResponseCase {
    RESPONSE_NOT_SET = 0,
    USER = 1,
    ERROR = 2,
  }
}

export class User extends jspb.Message {
  getId(): string;
  setId(value: string): void;

  getEmail(): string;
  setEmail(value: string): void;

  getOrganization(): string;
  setOrganization(value: string): void;

  getNotifyByEmailEnabled(): boolean;
  setNotifyByEmailEnabled(value: boolean): void;

  getNotifyByAppEnabled(): boolean;
  setNotifyByAppEnabled(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): User.AsObject;
  static toObject(includeInstance: boolean, msg: User): User.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: User, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): User;
  static deserializeBinaryFromReader(message: User, reader: jspb.BinaryReader): User;
}

export namespace User {
  export type AsObject = {
    id: string,
    email: string,
    organization: string,
    notifyByEmailEnabled: boolean,
    notifyByAppEnabled: boolean,
  }
}

export class GetUserPermissionsRequest extends jspb.Message {
  getUserId(): string;
  setUserId(value: string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetUserPermissionsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetUserPermissionsRequest): GetUserPermissionsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetUserPermissionsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetUserPermissionsRequest;
  static deserializeBinaryFromReader(message: GetUserPermissionsRequest, reader: jspb.BinaryReader): GetUserPermissionsRequest;
}

export namespace GetUserPermissionsRequest {
  export type AsObject = {
    userId: string,
  }
}

export class UserPermissionsResponse extends jspb.Message {
  hasUserPermissions(): boolean;
  clearUserPermissions(): void;
  getUserPermissions(): UserPermissions | undefined;
  setUserPermissions(value?: UserPermissions): void;

  hasError(): boolean;
  clearError(): void;
  getError(): common_gateway_base_pb.Error | undefined;
  setError(value?: common_gateway_base_pb.Error): void;

  getResponseCase(): UserPermissionsResponse.ResponseCase;
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UserPermissionsResponse.AsObject;
  static toObject(includeInstance: boolean, msg: UserPermissionsResponse): UserPermissionsResponse.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UserPermissionsResponse, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UserPermissionsResponse;
  static deserializeBinaryFromReader(message: UserPermissionsResponse, reader: jspb.BinaryReader): UserPermissionsResponse;
}

export namespace UserPermissionsResponse {
  export type AsObject = {
    userPermissions?: UserPermissions.AsObject,
    error?: common_gateway_base_pb.Error.AsObject,
  }

  export enum ResponseCase {
    RESPONSE_NOT_SET = 0,
    USER_PERMISSIONS = 1,
    ERROR = 2,
  }
}

export class UserPermissions extends jspb.Message {
  clearUserPermissionList(): void;
  getUserPermissionList(): Array<UserPermission>;
  setUserPermissionList(value: Array<UserPermission>): void;
  addUserPermission(value?: UserPermission, index?: number): UserPermission;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UserPermissions.AsObject;
  static toObject(includeInstance: boolean, msg: UserPermissions): UserPermissions.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UserPermissions, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UserPermissions;
  static deserializeBinaryFromReader(message: UserPermissions, reader: jspb.BinaryReader): UserPermissions;
}

export namespace UserPermissions {
  export type AsObject = {
    userPermissionList: Array<UserPermission.AsObject>,
  }
}

export class UserPermission extends jspb.Message {
  getAssetId(): string;
  setAssetId(value: string): void;

  getType(): string;
  setType(value: string): void;

  getEnabled(): boolean;
  setEnabled(value: boolean): void;

  getTraceName(): string;
  setTraceName(value: string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UserPermission.AsObject;
  static toObject(includeInstance: boolean, msg: UserPermission): UserPermission.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UserPermission, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UserPermission;
  static deserializeBinaryFromReader(message: UserPermission, reader: jspb.BinaryReader): UserPermission;
}

export namespace UserPermission {
  export type AsObject = {
    assetId: string,
    type: string,
    enabled: boolean,
    traceName: string,
  }
}

export class GetUserNotificationRequest extends jspb.Message {
  getUserId(): string;
  setUserId(value: string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetUserNotificationRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetUserNotificationRequest): GetUserNotificationRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetUserNotificationRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetUserNotificationRequest;
  static deserializeBinaryFromReader(message: GetUserNotificationRequest, reader: jspb.BinaryReader): GetUserNotificationRequest;
}

export namespace GetUserNotificationRequest {
  export type AsObject = {
    userId: string,
  }
}

export class GetUserNotificationByMarketRequest extends jspb.Message {
  getUserId(): string;
  setUserId(value: string): void;

  getMarketId(): string;
  setMarketId(value: string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetUserNotificationByMarketRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetUserNotificationByMarketRequest): GetUserNotificationByMarketRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetUserNotificationByMarketRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetUserNotificationByMarketRequest;
  static deserializeBinaryFromReader(message: GetUserNotificationByMarketRequest, reader: jspb.BinaryReader): GetUserNotificationByMarketRequest;
}

export namespace GetUserNotificationByMarketRequest {
  export type AsObject = {
    userId: string,
    marketId: string,
  }
}

export class UserNotificationsResponse extends jspb.Message {
  hasUserNotifications(): boolean;
  clearUserNotifications(): void;
  getUserNotifications(): UserNotifications | undefined;
  setUserNotifications(value?: UserNotifications): void;

  hasError(): boolean;
  clearError(): void;
  getError(): common_gateway_base_pb.Error | undefined;
  setError(value?: common_gateway_base_pb.Error): void;

  getResponseCase(): UserNotificationsResponse.ResponseCase;
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UserNotificationsResponse.AsObject;
  static toObject(includeInstance: boolean, msg: UserNotificationsResponse): UserNotificationsResponse.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UserNotificationsResponse, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UserNotificationsResponse;
  static deserializeBinaryFromReader(message: UserNotificationsResponse, reader: jspb.BinaryReader): UserNotificationsResponse;
}

export namespace UserNotificationsResponse {
  export type AsObject = {
    userNotifications?: UserNotifications.AsObject,
    error?: common_gateway_base_pb.Error.AsObject,
  }

  export enum ResponseCase {
    RESPONSE_NOT_SET = 0,
    USER_NOTIFICATIONS = 1,
    ERROR = 2,
  }
}

export class UserNotificationRequest extends jspb.Message {
  hasUserNotification(): boolean;
  clearUserNotification(): void;
  getUserNotification(): UserNotification | undefined;
  setUserNotification(value?: UserNotification): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UserNotificationRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UserNotificationRequest): UserNotificationRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UserNotificationRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UserNotificationRequest;
  static deserializeBinaryFromReader(message: UserNotificationRequest, reader: jspb.BinaryReader): UserNotificationRequest;
}

export namespace UserNotificationRequest {
  export type AsObject = {
    userNotification?: UserNotification.AsObject,
  }
}

export class UserNotifications extends jspb.Message {
  clearUserNotificationList(): void;
  getUserNotificationList(): Array<UserNotification>;
  setUserNotificationList(value: Array<UserNotification>): void;
  addUserNotification(value?: UserNotification, index?: number): UserNotification;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UserNotifications.AsObject;
  static toObject(includeInstance: boolean, msg: UserNotifications): UserNotifications.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UserNotifications, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UserNotifications;
  static deserializeBinaryFromReader(message: UserNotifications, reader: jspb.BinaryReader): UserNotifications;
}

export namespace UserNotifications {
  export type AsObject = {
    userNotificationList: Array<UserNotification.AsObject>,
  }
}

export class UserNotification extends jspb.Message {
  getId(): string;
  setId(value: string): void;

  hasUser(): boolean;
  clearUser(): void;
  getUser(): User | undefined;
  setUser(value?: User): void;

  hasAsset(): boolean;
  clearAsset(): void;
  getAsset(): AssetM | undefined;
  setAsset(value?: AssetM): void;

  hasMarket(): boolean;
  clearMarket(): void;
  getMarket(): Market | undefined;
  setMarket(value?: Market): void;

  getType(): string;
  setType(value: string): void;

  getValue(): string;
  setValue(value: string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UserNotification.AsObject;
  static toObject(includeInstance: boolean, msg: UserNotification): UserNotification.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UserNotification, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UserNotification;
  static deserializeBinaryFromReader(message: UserNotification, reader: jspb.BinaryReader): UserNotification;
}

export namespace UserNotification {
  export type AsObject = {
    id: string,
    user?: User.AsObject,
    asset?: AssetM.AsObject,
    market?: Market.AsObject,
    type: string,
    value: string,
  }
}

export class AssetM extends jspb.Message {
  getName(): string;
  setName(value: string): void;

  clearInstrumentTypesList(): void;
  getInstrumentTypesList(): Array<string>;
  setInstrumentTypesList(value: Array<string>): void;
  addInstrumentTypes(value: string, index?: number): string;

  getId(): string;
  setId(value: string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssetM.AsObject;
  static toObject(includeInstance: boolean, msg: AssetM): AssetM.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssetM, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssetM;
  static deserializeBinaryFromReader(message: AssetM, reader: jspb.BinaryReader): AssetM;
}

export namespace AssetM {
  export type AsObject = {
    name: string,
    instrumentTypesList: Array<string>,
    id: string,
  }
}

export class Market extends jspb.Message {
  getId(): string;
  setId(value: string): void;

  hasUser(): boolean;
  clearUser(): void;
  getUser(): User | undefined;
  setUser(value?: User): void;

  getName(): string;
  setName(value: string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Market.AsObject;
  static toObject(includeInstance: boolean, msg: Market): Market.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Market, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Market;
  static deserializeBinaryFromReader(message: Market, reader: jspb.BinaryReader): Market;
}

export namespace Market {
  export type AsObject = {
    id: string,
    user?: User.AsObject,
    name: string,
  }
}

export class UserNotificationResponse extends jspb.Message {
  hasUserNotification(): boolean;
  clearUserNotification(): void;
  getUserNotification(): UserNotification | undefined;
  setUserNotification(value?: UserNotification): void;

  hasError(): boolean;
  clearError(): void;
  getError(): common_gateway_base_pb.Error | undefined;
  setError(value?: common_gateway_base_pb.Error): void;

  getResponseCase(): UserNotificationResponse.ResponseCase;
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UserNotificationResponse.AsObject;
  static toObject(includeInstance: boolean, msg: UserNotificationResponse): UserNotificationResponse.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UserNotificationResponse, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UserNotificationResponse;
  static deserializeBinaryFromReader(message: UserNotificationResponse, reader: jspb.BinaryReader): UserNotificationResponse;
}

export namespace UserNotificationResponse {
  export type AsObject = {
    userNotification?: UserNotification.AsObject,
    error?: common_gateway_base_pb.Error.AsObject,
  }

  export enum ResponseCase {
    RESPONSE_NOT_SET = 0,
    USER_NOTIFICATION = 1,
    ERROR = 2,
  }
}

