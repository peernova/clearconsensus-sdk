/* eslint-disable */
/*Generated by GenDocu.com*/
// source: common/market.proto
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

var common_gateway_base_pb = require('../common/gateway_base_pb.js');
goog.object.extend(proto, common_gateway_base_pb);
goog.exportSymbol('proto.titanium.MarketSnapTimeResponse', null, global);
goog.exportSymbol('proto.titanium.MarketSnapTimeResponse.ResponseCase', null, global);
goog.exportSymbol('proto.titanium.SnapTimes', null, global);
/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.titanium.MarketSnapTimeResponse = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, proto.titanium.MarketSnapTimeResponse.oneofGroups_);
};
goog.inherits(proto.titanium.MarketSnapTimeResponse, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  /**
   * @public
   * @override
   */
  proto.titanium.MarketSnapTimeResponse.displayName = 'proto.titanium.MarketSnapTimeResponse';
}
/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.titanium.SnapTimes = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.titanium.SnapTimes.repeatedFields_, null);
};
goog.inherits(proto.titanium.SnapTimes, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  /**
   * @public
   * @override
   */
  proto.titanium.SnapTimes.displayName = 'proto.titanium.SnapTimes';
}

/**
 * Oneof group definitions for this message. Each group defines the field
 * numbers belonging to that group. When of these fields' value is set, all
 * other fields in the group are cleared. During deserialization, if multiple
 * fields are encountered for a group, only the last value seen will be kept.
 * @private {!Array<!Array<number>>}
 * @const
 */
proto.titanium.MarketSnapTimeResponse.oneofGroups_ = [[1,2]];

/**
 * @enum {number}
 */
proto.titanium.MarketSnapTimeResponse.ResponseCase = {
  RESPONSE_NOT_SET: 0,
  DATA: 1,
  ERROR: 2
};

/**
 * @return {proto.titanium.MarketSnapTimeResponse.ResponseCase}
 */
proto.titanium.MarketSnapTimeResponse.prototype.getResponseCase = function() {
  return /** @type {proto.titanium.MarketSnapTimeResponse.ResponseCase} */(jspb.Message.computeOneofCase(this, proto.titanium.MarketSnapTimeResponse.oneofGroups_[0]));
};



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * Optional fields that are not set will be set to undefined.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     net/proto2/compiler/js/internal/generator.cc#kKeyword.
 * @param {boolean=} opt_includeInstance Deprecated. whether to include the
 *     JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @return {!Object}
 */
proto.titanium.MarketSnapTimeResponse.prototype.toObject = function(opt_includeInstance) {
  return proto.titanium.MarketSnapTimeResponse.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Deprecated. Whether to include
 *     the JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.titanium.MarketSnapTimeResponse} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.titanium.MarketSnapTimeResponse.toObject = function(includeInstance, msg) {
  var f, obj = {
    data: (f = msg.getData()) && proto.titanium.SnapTimes.toObject(includeInstance, f),
    error: (f = msg.getError()) && common_gateway_base_pb.Error.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.titanium.MarketSnapTimeResponse}
 */
proto.titanium.MarketSnapTimeResponse.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.titanium.MarketSnapTimeResponse;
  return proto.titanium.MarketSnapTimeResponse.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.titanium.MarketSnapTimeResponse} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.titanium.MarketSnapTimeResponse}
 */
proto.titanium.MarketSnapTimeResponse.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.titanium.SnapTimes;
      reader.readMessage(value,proto.titanium.SnapTimes.deserializeBinaryFromReader);
      msg.setData(value);
      break;
    case 2:
      var value = new common_gateway_base_pb.Error;
      reader.readMessage(value,common_gateway_base_pb.Error.deserializeBinaryFromReader);
      msg.setError(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.titanium.MarketSnapTimeResponse.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.titanium.MarketSnapTimeResponse.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.titanium.MarketSnapTimeResponse} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.titanium.MarketSnapTimeResponse.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getData();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      proto.titanium.SnapTimes.serializeBinaryToWriter
    );
  }
  f = message.getError();
  if (f != null) {
    writer.writeMessage(
      2,
      f,
      common_gateway_base_pb.Error.serializeBinaryToWriter
    );
  }
};


/**
 * optional SnapTimes data = 1;
 * @return {?proto.titanium.SnapTimes}
 */
proto.titanium.MarketSnapTimeResponse.prototype.getData = function() {
  return /** @type{?proto.titanium.SnapTimes} */ (
    jspb.Message.getWrapperField(this, proto.titanium.SnapTimes, 1));
};


/**
 * @param {?proto.titanium.SnapTimes|undefined} value
 * @return {!proto.titanium.MarketSnapTimeResponse} returns this
*/
proto.titanium.MarketSnapTimeResponse.prototype.setData = function(value) {
  return jspb.Message.setOneofWrapperField(this, 1, proto.titanium.MarketSnapTimeResponse.oneofGroups_[0], value);
};


/**
 * Clears the message field making it undefined.
 * @return {!proto.titanium.MarketSnapTimeResponse} returns this
 */
proto.titanium.MarketSnapTimeResponse.prototype.clearData = function() {
  return this.setData(undefined);
};


/**
 * Returns whether this field is set.
 * @return {boolean}
 */
proto.titanium.MarketSnapTimeResponse.prototype.hasData = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional Error error = 2;
 * @return {?proto.titanium.Error}
 */
proto.titanium.MarketSnapTimeResponse.prototype.getError = function() {
  return /** @type{?proto.titanium.Error} */ (
    jspb.Message.getWrapperField(this, common_gateway_base_pb.Error, 2));
};


/**
 * @param {?proto.titanium.Error|undefined} value
 * @return {!proto.titanium.MarketSnapTimeResponse} returns this
*/
proto.titanium.MarketSnapTimeResponse.prototype.setError = function(value) {
  return jspb.Message.setOneofWrapperField(this, 2, proto.titanium.MarketSnapTimeResponse.oneofGroups_[0], value);
};


/**
 * Clears the message field making it undefined.
 * @return {!proto.titanium.MarketSnapTimeResponse} returns this
 */
proto.titanium.MarketSnapTimeResponse.prototype.clearError = function() {
  return this.setError(undefined);
};


/**
 * Returns whether this field is set.
 * @return {boolean}
 */
proto.titanium.MarketSnapTimeResponse.prototype.hasError = function() {
  return jspb.Message.getField(this, 2) != null;
};



/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.titanium.SnapTimes.repeatedFields_ = [1];



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * Optional fields that are not set will be set to undefined.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     net/proto2/compiler/js/internal/generator.cc#kKeyword.
 * @param {boolean=} opt_includeInstance Deprecated. whether to include the
 *     JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @return {!Object}
 */
proto.titanium.SnapTimes.prototype.toObject = function(opt_includeInstance) {
  return proto.titanium.SnapTimes.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Deprecated. Whether to include
 *     the JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.titanium.SnapTimes} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.titanium.SnapTimes.toObject = function(includeInstance, msg) {
  var f, obj = {
    snapTimesList: (f = jspb.Message.getRepeatedField(msg, 1)) == null ? undefined : f
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.titanium.SnapTimes}
 */
proto.titanium.SnapTimes.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.titanium.SnapTimes;
  return proto.titanium.SnapTimes.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.titanium.SnapTimes} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.titanium.SnapTimes}
 */
proto.titanium.SnapTimes.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {string} */ (reader.readString());
      msg.addSnapTimes(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.titanium.SnapTimes.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.titanium.SnapTimes.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.titanium.SnapTimes} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.titanium.SnapTimes.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getSnapTimesList();
  if (f.length > 0) {
    writer.writeRepeatedString(
      1,
      f
    );
  }
};


/**
 * repeated string snap_times = 1;
 * @return {!Array<string>}
 */
proto.titanium.SnapTimes.prototype.getSnapTimesList = function() {
  return /** @type {!Array<string>} */ (jspb.Message.getRepeatedField(this, 1));
};


/**
 * @param {!Array<string>} value
 * @return {!proto.titanium.SnapTimes} returns this
 */
proto.titanium.SnapTimes.prototype.setSnapTimesList = function(value) {
  return jspb.Message.setField(this, 1, value || []);
};


/**
 * @param {string} value
 * @param {number=} opt_index
 * @return {!proto.titanium.SnapTimes} returns this
 */
proto.titanium.SnapTimes.prototype.addSnapTimes = function(value, opt_index) {
  return jspb.Message.addToRepeatedField(this, 1, value, opt_index);
};


/**
 * Clears the list making it empty but non-null.
 * @return {!proto.titanium.SnapTimes} returns this
 */
proto.titanium.SnapTimes.prototype.clearSnapTimesList = function() {
  return this.setSnapTimesList([]);
};


goog.object.extend(exports, proto.titanium);
