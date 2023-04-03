/* eslint-disable */
/*Generated by GenDocu.com*/
// package: titanium
// file: public/key_storage.proto

var public_key_storage_pb = require("../public/key_storage_pb");
var grpc = require("@improbable-eng/grpc-web").grpc;

var KVService = (function () {
  function KVService() {}
  KVService.serviceName = "titanium.KVService";
  return KVService;
}());

KVService.AddKey = {
  methodName: "AddKey",
  service: KVService,
  requestStream: false,
  responseStream: false,
  requestType: public_key_storage_pb.KVAsset,
  responseType: public_key_storage_pb.KVOperationResponse
};

KVService.UpdateKey = {
  methodName: "UpdateKey",
  service: KVService,
  requestStream: false,
  responseStream: false,
  requestType: public_key_storage_pb.KVAsset,
  responseType: public_key_storage_pb.KVOperationResponse
};

KVService.GetKey = {
  methodName: "GetKey",
  service: KVService,
  requestStream: false,
  responseStream: false,
  requestType: public_key_storage_pb.KVRequest,
  responseType: public_key_storage_pb.GetKVResponse
};

KVService.DeleteKey = {
  methodName: "DeleteKey",
  service: KVService,
  requestStream: false,
  responseStream: false,
  requestType: public_key_storage_pb.KVRequest,
  responseType: public_key_storage_pb.KVOperationResponse
};

KVService.ListKeys = {
  methodName: "ListKeys",
  service: KVService,
  requestStream: false,
  responseStream: false,
  requestType: public_key_storage_pb.ListKVRequest,
  responseType: public_key_storage_pb.ListKVResponse
};

exports.KVService = KVService;

function KVServiceClient(serviceHost, options) {
  this.serviceHost = serviceHost;
  this.options = options || {};
}

KVServiceClient.prototype.addKey = function addKey(requestMessage, metadata, callback) {
  if (arguments.length === 2) {
    callback = arguments[1];
  }
  var client = grpc.unary(KVService.AddKey, {
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

KVServiceClient.prototype.updateKey = function updateKey(requestMessage, metadata, callback) {
  if (arguments.length === 2) {
    callback = arguments[1];
  }
  var client = grpc.unary(KVService.UpdateKey, {
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

KVServiceClient.prototype.getKey = function getKey(requestMessage, metadata, callback) {
  if (arguments.length === 2) {
    callback = arguments[1];
  }
  var client = grpc.unary(KVService.GetKey, {
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

KVServiceClient.prototype.deleteKey = function deleteKey(requestMessage, metadata, callback) {
  if (arguments.length === 2) {
    callback = arguments[1];
  }
  var client = grpc.unary(KVService.DeleteKey, {
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

KVServiceClient.prototype.listKeys = function listKeys(requestMessage, metadata, callback) {
  if (arguments.length === 2) {
    callback = arguments[1];
  }
  var client = grpc.unary(KVService.ListKeys, {
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

exports.KVServiceClient = KVServiceClient;

