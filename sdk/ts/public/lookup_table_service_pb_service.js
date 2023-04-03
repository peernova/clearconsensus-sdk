/* eslint-disable */
/*Generated by GenDocu.com*/
// package: titanium
// file: public/lookup_table_service.proto

var public_lookup_table_service_pb = require("../public/lookup_table_service_pb");
var common_gateway_base_pb = require("../common/gateway_base_pb");
var common_lookup_table_pb = require("../common/lookup_table_pb");
var grpc = require("@improbable-eng/grpc-web").grpc;

var LookupTableService = (function () {
  function LookupTableService() {}
  LookupTableService.serviceName = "titanium.LookupTableService";
  return LookupTableService;
}());

LookupTableService.AddLookupTable = {
  methodName: "AddLookupTable",
  service: LookupTableService,
  requestStream: false,
  responseStream: false,
  requestType: common_lookup_table_pb.AddLookupTableRequest,
  responseType: common_gateway_base_pb.AcknowledgeResponse
};

LookupTableService.GetLookupTable = {
  methodName: "GetLookupTable",
  service: LookupTableService,
  requestStream: false,
  responseStream: false,
  requestType: common_gateway_base_pb.GetDefinition,
  responseType: common_lookup_table_pb.GetLookupTableResponse
};

LookupTableService.ListLookupTables = {
  methodName: "ListLookupTables",
  service: LookupTableService,
  requestStream: false,
  responseStream: false,
  requestType: common_gateway_base_pb.ListRequest,
  responseType: common_lookup_table_pb.ListLookupTableResponse
};

LookupTableService.ListLookupTableVersions = {
  methodName: "ListLookupTableVersions",
  service: LookupTableService,
  requestStream: false,
  responseStream: false,
  requestType: common_gateway_base_pb.GetDefinition,
  responseType: common_gateway_base_pb.ListVersionResponse
};

exports.LookupTableService = LookupTableService;

function LookupTableServiceClient(serviceHost, options) {
  this.serviceHost = serviceHost;
  this.options = options || {};
}

LookupTableServiceClient.prototype.addLookupTable = function addLookupTable(requestMessage, metadata, callback) {
  if (arguments.length === 2) {
    callback = arguments[1];
  }
  var client = grpc.unary(LookupTableService.AddLookupTable, {
    request: requestMessage,
    host: this.serviceHost,
    metadata: metadata,
    transport: this.options.transport,
    debug: this.options.debug,
    onEnd: function (response) {
      if (callback) {
        if (response.status !== grpc.Code.OK) {
          var err = new Error(response.statusMessage);
          err.code = response.status;
          err.metadata = response.trailers;
          callback(err, null);
        } else {
          callback(null, response.message);
        }
      }
    }
  });
  return {
    cancel: function () {
      callback = null;
      client.close();
    }
  };
};

LookupTableServiceClient.prototype.getLookupTable = function getLookupTable(requestMessage, metadata, callback) {
  if (arguments.length === 2) {
    callback = arguments[1];
  }
  var client = grpc.unary(LookupTableService.GetLookupTable, {
    request: requestMessage,
    host: this.serviceHost,
    metadata: metadata,
    transport: this.options.transport,
    debug: this.options.debug,
    onEnd: function (response) {
      if (callback) {
        if (response.status !== grpc.Code.OK) {
          var err = new Error(response.statusMessage);
          err.code = response.status;
          err.metadata = response.trailers;
          callback(err, null);
        } else {
          callback(null, response.message);
        }
      }
    }
  });
  return {
    cancel: function () {
      callback = null;
      client.close();
    }
  };
};

LookupTableServiceClient.prototype.listLookupTables = function listLookupTables(requestMessage, metadata, callback) {
  if (arguments.length === 2) {
    callback = arguments[1];
  }
  var client = grpc.unary(LookupTableService.ListLookupTables, {
    request: requestMessage,
    host: this.serviceHost,
    metadata: metadata,
    transport: this.options.transport,
    debug: this.options.debug,
    onEnd: function (response) {
      if (callback) {
        if (response.status !== grpc.Code.OK) {
          var err = new Error(response.statusMessage);
          err.code = response.status;
          err.metadata = response.trailers;
          callback(err, null);
        } else {
          callback(null, response.message);
        }
      }
    }
  });
  return {
    cancel: function () {
      callback = null;
      client.close();
    }
  };
};

LookupTableServiceClient.prototype.listLookupTableVersions = function listLookupTableVersions(requestMessage, metadata, callback) {
  if (arguments.length === 2) {
    callback = arguments[1];
  }
  var client = grpc.unary(LookupTableService.ListLookupTableVersions, {
    request: requestMessage,
    host: this.serviceHost,
    metadata: metadata,
    transport: this.options.transport,
    debug: this.options.debug,
    onEnd: function (response) {
      if (callback) {
        if (response.status !== grpc.Code.OK) {
          var err = new Error(response.statusMessage);
          err.code = response.status;
          err.metadata = response.trailers;
          callback(err, null);
        } else {
          callback(null, response.message);
        }
      }
    }
  });
  return {
    cancel: function () {
      callback = null;
      client.close();
    }
  };
};

exports.LookupTableServiceClient = LookupTableServiceClient;

