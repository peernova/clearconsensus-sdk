/* eslint-disable */
/*Generated by GenDocu.com*/
// source: google/cloud/bigquery/storage/v1/annotations.proto
/**
 * @fileoverview
 * @enhanceable
 * @suppress {missingRequire} reports error on implicit type usages.
 * @suppress {messageConventions} JS Compiler reports an error if a variable or
 *     field starts with 'MSG_' and isn't a translatable message.
 * @public
 */
// GENERATED CODE -- DO NOT EDIT!
/* eslint-disable */
// @ts-nocheck

var jspb = require('google-protobuf');
var goog = jspb;
var global = Function('return this')();

var google_protobuf_descriptor_pb = require('google-protobuf/google/protobuf/descriptor_pb.js');
goog.object.extend(proto, google_protobuf_descriptor_pb);
goog.exportSymbol('proto.google.cloud.bigquery.storage.v1.columnName', null, global);

/**
 * A tuple of {field number, class constructor} for the extension
 * field named `columnName`.
 * @type {!jspb.ExtensionFieldInfo<string>}
 */
proto.google.cloud.bigquery.storage.v1.columnName = new jspb.ExtensionFieldInfo(
    454943157,
    {columnName: 0},
    null,
     /** @type {?function((boolean|undefined),!jspb.Message=): !Object} */ (
         null),
    0);

google_protobuf_descriptor_pb.FieldOptions.extensionsBinary[454943157] = new jspb.ExtensionFieldBinaryInfo(
    proto.google.cloud.bigquery.storage.v1.columnName,
    jspb.BinaryReader.prototype.readString,
    jspb.BinaryWriter.prototype.writeString,
    undefined,
    undefined,
    false);
// This registers the extension field with the extended class, so that
// toObject() will function correctly.
google_protobuf_descriptor_pb.FieldOptions.extensions[454943157] = proto.google.cloud.bigquery.storage.v1.columnName;

goog.object.extend(exports, proto.google.cloud.bigquery.storage.v1);
