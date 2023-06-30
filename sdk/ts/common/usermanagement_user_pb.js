/* eslint-disable */
/*Generated by GenDocu.com*/
// source: common/usermanagement_user.proto
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

var common_usermanagement_fe_specific_pb = require('../common/usermanagement_fe_specific_pb.js');
goog.object.extend(proto, common_usermanagement_fe_specific_pb);
var common_usermanagement_entity_pb = require('../common/usermanagement_entity_pb.js');
goog.object.extend(proto, common_usermanagement_entity_pb);
goog.exportSymbol('proto.com.peernova.titanium.casbin.management.grpc.proto.UserDto', null, global);
goog.exportSymbol('proto.com.peernova.titanium.casbin.management.grpc.proto.UsersDto', null, global);
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
proto.com.peernova.titanium.casbin.management.grpc.proto.UserDto = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.com.peernova.titanium.casbin.management.grpc.proto.UserDto, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  /**
   * @public
   * @override
   */
  proto.com.peernova.titanium.casbin.management.grpc.proto.UserDto.displayName = 'proto.com.peernova.titanium.casbin.management.grpc.proto.UserDto';
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
proto.com.peernova.titanium.casbin.management.grpc.proto.UsersDto = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.com.peernova.titanium.casbin.management.grpc.proto.UsersDto.repeatedFields_, null);
};
goog.inherits(proto.com.peernova.titanium.casbin.management.grpc.proto.UsersDto, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  /**
   * @public
   * @override
   */
  proto.com.peernova.titanium.casbin.management.grpc.proto.UsersDto.displayName = 'proto.com.peernova.titanium.casbin.management.grpc.proto.UsersDto';
}



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
proto.com.peernova.titanium.casbin.management.grpc.proto.UserDto.prototype.toObject = function(opt_includeInstance) {
  return proto.com.peernova.titanium.casbin.management.grpc.proto.UserDto.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Deprecated. Whether to include
 *     the JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.com.peernova.titanium.casbin.management.grpc.proto.UserDto} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.com.peernova.titanium.casbin.management.grpc.proto.UserDto.toObject = function(includeInstance, msg) {
  var f, obj = {
    id: jspb.Message.getFieldWithDefault(msg, 1, ""),
    email: jspb.Message.getFieldWithDefault(msg, 2, ""),
    firstname: jspb.Message.getFieldWithDefault(msg, 3, ""),
    lastname: jspb.Message.getFieldWithDefault(msg, 4, ""),
    enabled: jspb.Message.getBooleanFieldWithDefault(msg, 5, false),
    entity: (f = msg.getEntity()) && common_usermanagement_entity_pb.EntityDto.toObject(includeInstance, f)
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
 * @return {!proto.com.peernova.titanium.casbin.management.grpc.proto.UserDto}
 */
proto.com.peernova.titanium.casbin.management.grpc.proto.UserDto.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.com.peernova.titanium.casbin.management.grpc.proto.UserDto;
  return proto.com.peernova.titanium.casbin.management.grpc.proto.UserDto.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.com.peernova.titanium.casbin.management.grpc.proto.UserDto} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.com.peernova.titanium.casbin.management.grpc.proto.UserDto}
 */
proto.com.peernova.titanium.casbin.management.grpc.proto.UserDto.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {string} */ (reader.readString());
      msg.setId(value);
      break;
    case 2:
      var value = /** @type {string} */ (reader.readString());
      msg.setEmail(value);
      break;
    case 3:
      var value = /** @type {string} */ (reader.readString());
      msg.setFirstname(value);
      break;
    case 4:
      var value = /** @type {string} */ (reader.readString());
      msg.setLastname(value);
      break;
    case 5:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setEnabled(value);
      break;
    case 6:
      var value = new common_usermanagement_entity_pb.EntityDto;
      reader.readMessage(value,common_usermanagement_entity_pb.EntityDto.deserializeBinaryFromReader);
      msg.setEntity(value);
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
proto.com.peernova.titanium.casbin.management.grpc.proto.UserDto.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.com.peernova.titanium.casbin.management.grpc.proto.UserDto.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.com.peernova.titanium.casbin.management.grpc.proto.UserDto} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.com.peernova.titanium.casbin.management.grpc.proto.UserDto.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getId();
  if (f.length > 0) {
    writer.writeString(
      1,
      f
    );
  }
  f = message.getEmail();
  if (f.length > 0) {
    writer.writeString(
      2,
      f
    );
  }
  f = message.getFirstname();
  if (f.length > 0) {
    writer.writeString(
      3,
      f
    );
  }
  f = message.getLastname();
  if (f.length > 0) {
    writer.writeString(
      4,
      f
    );
  }
  f = message.getEnabled();
  if (f) {
    writer.writeBool(
      5,
      f
    );
  }
  f = message.getEntity();
  if (f != null) {
    writer.writeMessage(
      6,
      f,
      common_usermanagement_entity_pb.EntityDto.serializeBinaryToWriter
    );
  }
};


/**
 * optional string id = 1;
 * @return {string}
 */
proto.com.peernova.titanium.casbin.management.grpc.proto.UserDto.prototype.getId = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 1, ""));
};


/**
 * @param {string} value
 * @return {!proto.com.peernova.titanium.casbin.management.grpc.proto.UserDto} returns this
 */
proto.com.peernova.titanium.casbin.management.grpc.proto.UserDto.prototype.setId = function(value) {
  return jspb.Message.setProto3StringField(this, 1, value);
};


/**
 * optional string email = 2;
 * @return {string}
 */
proto.com.peernova.titanium.casbin.management.grpc.proto.UserDto.prototype.getEmail = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 2, ""));
};


/**
 * @param {string} value
 * @return {!proto.com.peernova.titanium.casbin.management.grpc.proto.UserDto} returns this
 */
proto.com.peernova.titanium.casbin.management.grpc.proto.UserDto.prototype.setEmail = function(value) {
  return jspb.Message.setProto3StringField(this, 2, value);
};


/**
 * optional string firstName = 3;
 * @return {string}
 */
proto.com.peernova.titanium.casbin.management.grpc.proto.UserDto.prototype.getFirstname = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 3, ""));
};


/**
 * @param {string} value
 * @return {!proto.com.peernova.titanium.casbin.management.grpc.proto.UserDto} returns this
 */
proto.com.peernova.titanium.casbin.management.grpc.proto.UserDto.prototype.setFirstname = function(value) {
  return jspb.Message.setProto3StringField(this, 3, value);
};


/**
 * optional string lastName = 4;
 * @return {string}
 */
proto.com.peernova.titanium.casbin.management.grpc.proto.UserDto.prototype.getLastname = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 4, ""));
};


/**
 * @param {string} value
 * @return {!proto.com.peernova.titanium.casbin.management.grpc.proto.UserDto} returns this
 */
proto.com.peernova.titanium.casbin.management.grpc.proto.UserDto.prototype.setLastname = function(value) {
  return jspb.Message.setProto3StringField(this, 4, value);
};


/**
 * optional bool enabled = 5;
 * @return {boolean}
 */
proto.com.peernova.titanium.casbin.management.grpc.proto.UserDto.prototype.getEnabled = function() {
  return /** @type {boolean} */ (jspb.Message.getBooleanFieldWithDefault(this, 5, false));
};


/**
 * @param {boolean} value
 * @return {!proto.com.peernova.titanium.casbin.management.grpc.proto.UserDto} returns this
 */
proto.com.peernova.titanium.casbin.management.grpc.proto.UserDto.prototype.setEnabled = function(value) {
  return jspb.Message.setProto3BooleanField(this, 5, value);
};


/**
 * optional EntityDto entity = 6;
 * @return {?proto.com.peernova.titanium.casbin.management.grpc.proto.EntityDto}
 */
proto.com.peernova.titanium.casbin.management.grpc.proto.UserDto.prototype.getEntity = function() {
  return /** @type{?proto.com.peernova.titanium.casbin.management.grpc.proto.EntityDto} */ (
    jspb.Message.getWrapperField(this, common_usermanagement_entity_pb.EntityDto, 6));
};


/**
 * @param {?proto.com.peernova.titanium.casbin.management.grpc.proto.EntityDto|undefined} value
 * @return {!proto.com.peernova.titanium.casbin.management.grpc.proto.UserDto} returns this
*/
proto.com.peernova.titanium.casbin.management.grpc.proto.UserDto.prototype.setEntity = function(value) {
  return jspb.Message.setWrapperField(this, 6, value);
};


/**
 * Clears the message field making it undefined.
 * @return {!proto.com.peernova.titanium.casbin.management.grpc.proto.UserDto} returns this
 */
proto.com.peernova.titanium.casbin.management.grpc.proto.UserDto.prototype.clearEntity = function() {
  return this.setEntity(undefined);
};


/**
 * Returns whether this field is set.
 * @return {boolean}
 */
proto.com.peernova.titanium.casbin.management.grpc.proto.UserDto.prototype.hasEntity = function() {
  return jspb.Message.getField(this, 6) != null;
};



/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.com.peernova.titanium.casbin.management.grpc.proto.UsersDto.repeatedFields_ = [1];



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
proto.com.peernova.titanium.casbin.management.grpc.proto.UsersDto.prototype.toObject = function(opt_includeInstance) {
  return proto.com.peernova.titanium.casbin.management.grpc.proto.UsersDto.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Deprecated. Whether to include
 *     the JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.com.peernova.titanium.casbin.management.grpc.proto.UsersDto} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.com.peernova.titanium.casbin.management.grpc.proto.UsersDto.toObject = function(includeInstance, msg) {
  var f, obj = {
    userList: jspb.Message.toObjectList(msg.getUserList(),
    proto.com.peernova.titanium.casbin.management.grpc.proto.UserDto.toObject, includeInstance)
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
 * @return {!proto.com.peernova.titanium.casbin.management.grpc.proto.UsersDto}
 */
proto.com.peernova.titanium.casbin.management.grpc.proto.UsersDto.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.com.peernova.titanium.casbin.management.grpc.proto.UsersDto;
  return proto.com.peernova.titanium.casbin.management.grpc.proto.UsersDto.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.com.peernova.titanium.casbin.management.grpc.proto.UsersDto} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.com.peernova.titanium.casbin.management.grpc.proto.UsersDto}
 */
proto.com.peernova.titanium.casbin.management.grpc.proto.UsersDto.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.com.peernova.titanium.casbin.management.grpc.proto.UserDto;
      reader.readMessage(value,proto.com.peernova.titanium.casbin.management.grpc.proto.UserDto.deserializeBinaryFromReader);
      msg.addUser(value);
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
proto.com.peernova.titanium.casbin.management.grpc.proto.UsersDto.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.com.peernova.titanium.casbin.management.grpc.proto.UsersDto.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.com.peernova.titanium.casbin.management.grpc.proto.UsersDto} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.com.peernova.titanium.casbin.management.grpc.proto.UsersDto.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getUserList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      1,
      f,
      proto.com.peernova.titanium.casbin.management.grpc.proto.UserDto.serializeBinaryToWriter
    );
  }
};


/**
 * repeated UserDto user = 1;
 * @return {!Array<!proto.com.peernova.titanium.casbin.management.grpc.proto.UserDto>}
 */
proto.com.peernova.titanium.casbin.management.grpc.proto.UsersDto.prototype.getUserList = function() {
  return /** @type{!Array<!proto.com.peernova.titanium.casbin.management.grpc.proto.UserDto>} */ (
    jspb.Message.getRepeatedWrapperField(this, proto.com.peernova.titanium.casbin.management.grpc.proto.UserDto, 1));
};


/**
 * @param {!Array<!proto.com.peernova.titanium.casbin.management.grpc.proto.UserDto>} value
 * @return {!proto.com.peernova.titanium.casbin.management.grpc.proto.UsersDto} returns this
*/
proto.com.peernova.titanium.casbin.management.grpc.proto.UsersDto.prototype.setUserList = function(value) {
  return jspb.Message.setRepeatedWrapperField(this, 1, value);
};


/**
 * @param {!proto.com.peernova.titanium.casbin.management.grpc.proto.UserDto=} opt_value
 * @param {number=} opt_index
 * @return {!proto.com.peernova.titanium.casbin.management.grpc.proto.UserDto}
 */
proto.com.peernova.titanium.casbin.management.grpc.proto.UsersDto.prototype.addUser = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 1, opt_value, proto.com.peernova.titanium.casbin.management.grpc.proto.UserDto, opt_index);
};


/**
 * Clears the list making it empty but non-null.
 * @return {!proto.com.peernova.titanium.casbin.management.grpc.proto.UsersDto} returns this
 */
proto.com.peernova.titanium.casbin.management.grpc.proto.UsersDto.prototype.clearUserList = function() {
  return this.setUserList([]);
};


goog.object.extend(exports, proto.com.peernova.titanium.casbin.management.grpc.proto);
