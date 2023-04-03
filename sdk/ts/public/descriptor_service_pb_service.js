/* eslint-disable */
/*Generated by GenDocu.com*/
// package: titanium
// file: public/descriptor_service.proto

var public_descriptor_service_pb = require("../public/descriptor_service_pb");
var common_gateway_base_pb = require("../common/gateway_base_pb");
var common_descriptor_pb = require("../common/descriptor_pb");
var grpc = require("@improbable-eng/grpc-web").grpc;

var DescriptorService = (function () {
  function DescriptorService() {}
  DescriptorService.serviceName = "titanium.DescriptorService";
  return DescriptorService;
}());

DescriptorService.AddDescriptor = {
  methodName: "AddDescriptor",
  service: DescriptorService,
  requestStream: false,
  responseStream: false,
  requestType: common_gateway_base_pb.DescriptorDefinition,
  responseType: common_gateway_base_pb.AcknowledgeResponse
};

DescriptorService.GetDescriptor = {
  methodName: "GetDescriptor",
  service: DescriptorService,
  requestStream: false,
  responseStream: false,
  requestType: common_gateway_base_pb.GetDefinition,
  responseType: common_descriptor_pb.DescriptorDefinitionResponse
};

DescriptorService.EnableDescriptor = {
  methodName: "EnableDescriptor",
  service: DescriptorService,
  requestStream: false,
  responseStream: false,
  requestType: common_gateway_base_pb.EnableDisableRequest,
  responseType: common_gateway_base_pb.AcknowledgeResponse
};

DescriptorService.DisableDescriptor = {
  methodName: "DisableDescriptor",
  service: DescriptorService,
  requestStream: false,
  responseStream: false,
  requestType: common_gateway_base_pb.EnableDisableRequest,
  responseType: common_gateway_base_pb.AcknowledgeResponse
};

DescriptorService.ListDescriptors = {
  methodName: "ListDescriptors",
  service: DescriptorService,
  requestStream: false,
  responseStream: false,
  requestType: common_gateway_base_pb.ListRequest,
  responseType: common_descriptor_pb.DescriptorList
};

DescriptorService.ListDescriptorVersions = {
  methodName: "ListDescriptorVersions",
  service: DescriptorService,
  requestStream: false,
  responseStream: false,
  requestType: common_gateway_base_pb.GetDefinition,
  responseType: common_gateway_base_pb.ListVersionResponse
};

DescriptorService.GetDescriptorVersion = {
  methodName: "GetDescriptorVersion",
  service: DescriptorService,
  requestStream: false,
  responseStream: false,
  requestType: common_gateway_base_pb.VersionRequest,
  responseType: common_descriptor_pb.DescriptorDefinitionResponse
};

exports.DescriptorService = DescriptorService;

function DescriptorServiceClient(serviceHost, options) {
  this.serviceHost = serviceHost;
  this.options = options || {};
}

DescriptorServiceClient.prototype.addDescriptor = function addDescriptor(requestMessage, metadata, callback) {
  if (arguments.length === 2) {
    callback = arguments[1];
  }
  var client = grpc.unary(DescriptorService.AddDescriptor, {
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

DescriptorServiceClient.prototype.getDescriptor = function getDescriptor(requestMessage, metadata, callback) {
  if (arguments.length === 2) {
    callback = arguments[1];
  }
  var client = grpc.unary(DescriptorService.GetDescriptor, {
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

DescriptorServiceClient.prototype.enableDescriptor = function enableDescriptor(requestMessage, metadata, callback) {
  if (arguments.length === 2) {
    callback = arguments[1];
  }
  var client = grpc.unary(DescriptorService.EnableDescriptor, {
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

DescriptorServiceClient.prototype.disableDescriptor = function disableDescriptor(requestMessage, metadata, callback) {
  if (arguments.length === 2) {
    callback = arguments[1];
  }
  var client = grpc.unary(DescriptorService.DisableDescriptor, {
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

DescriptorServiceClient.prototype.listDescriptors = function listDescriptors(requestMessage, metadata, callback) {
  if (arguments.length === 2) {
    callback = arguments[1];
  }
  var client = grpc.unary(DescriptorService.ListDescriptors, {
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

DescriptorServiceClient.prototype.listDescriptorVersions = function listDescriptorVersions(requestMessage, metadata, callback) {
  if (arguments.length === 2) {
    callback = arguments[1];
  }
  var client = grpc.unary(DescriptorService.ListDescriptorVersions, {
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

DescriptorServiceClient.prototype.getDescriptorVersion = function getDescriptorVersion(requestMessage, metadata, callback) {
  if (arguments.length === 2) {
    callback = arguments[1];
  }
  var client = grpc.unary(DescriptorService.GetDescriptorVersion, {
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

exports.DescriptorServiceClient = DescriptorServiceClient;

var DbDescriptorService = (function () {
  function DbDescriptorService() {}
  DbDescriptorService.serviceName = "titanium.DbDescriptorService";
  return DbDescriptorService;
}());

DbDescriptorService.AddDbDescriptor = {
  methodName: "AddDbDescriptor",
  service: DbDescriptorService,
  requestStream: false,
  responseStream: false,
  requestType: common_gateway_base_pb.DescriptorDefinition,
  responseType: common_gateway_base_pb.AcknowledgeResponse
};

DbDescriptorService.GetDbDescriptor = {
  methodName: "GetDbDescriptor",
  service: DbDescriptorService,
  requestStream: false,
  responseStream: false,
  requestType: common_gateway_base_pb.GetDefinition,
  responseType: common_descriptor_pb.DescriptorDefinitionResponse
};

DbDescriptorService.EnableDbDescriptor = {
  methodName: "EnableDbDescriptor",
  service: DbDescriptorService,
  requestStream: false,
  responseStream: false,
  requestType: common_gateway_base_pb.EnableDisableRequest,
  responseType: common_gateway_base_pb.AcknowledgeResponse
};

DbDescriptorService.DisableDbDescriptor = {
  methodName: "DisableDbDescriptor",
  service: DbDescriptorService,
  requestStream: false,
  responseStream: false,
  requestType: common_gateway_base_pb.EnableDisableRequest,
  responseType: common_gateway_base_pb.AcknowledgeResponse
};

DbDescriptorService.ListDbDescriptors = {
  methodName: "ListDbDescriptors",
  service: DbDescriptorService,
  requestStream: false,
  responseStream: false,
  requestType: common_gateway_base_pb.ListRequest,
  responseType: common_descriptor_pb.DescriptorList
};

DbDescriptorService.ListDbDescriptorVersions = {
  methodName: "ListDbDescriptorVersions",
  service: DbDescriptorService,
  requestStream: false,
  responseStream: false,
  requestType: common_gateway_base_pb.GetDefinition,
  responseType: common_gateway_base_pb.ListVersionResponse
};

DbDescriptorService.GetDbDescriptorVersion = {
  methodName: "GetDbDescriptorVersion",
  service: DbDescriptorService,
  requestStream: false,
  responseStream: false,
  requestType: common_gateway_base_pb.VersionRequest,
  responseType: common_descriptor_pb.DescriptorDefinitionResponse
};

exports.DbDescriptorService = DbDescriptorService;

function DbDescriptorServiceClient(serviceHost, options) {
  this.serviceHost = serviceHost;
  this.options = options || {};
}

DbDescriptorServiceClient.prototype.addDbDescriptor = function addDbDescriptor(requestMessage, metadata, callback) {
  if (arguments.length === 2) {
    callback = arguments[1];
  }
  var client = grpc.unary(DbDescriptorService.AddDbDescriptor, {
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

DbDescriptorServiceClient.prototype.getDbDescriptor = function getDbDescriptor(requestMessage, metadata, callback) {
  if (arguments.length === 2) {
    callback = arguments[1];
  }
  var client = grpc.unary(DbDescriptorService.GetDbDescriptor, {
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

DbDescriptorServiceClient.prototype.enableDbDescriptor = function enableDbDescriptor(requestMessage, metadata, callback) {
  if (arguments.length === 2) {
    callback = arguments[1];
  }
  var client = grpc.unary(DbDescriptorService.EnableDbDescriptor, {
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

DbDescriptorServiceClient.prototype.disableDbDescriptor = function disableDbDescriptor(requestMessage, metadata, callback) {
  if (arguments.length === 2) {
    callback = arguments[1];
  }
  var client = grpc.unary(DbDescriptorService.DisableDbDescriptor, {
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

DbDescriptorServiceClient.prototype.listDbDescriptors = function listDbDescriptors(requestMessage, metadata, callback) {
  if (arguments.length === 2) {
    callback = arguments[1];
  }
  var client = grpc.unary(DbDescriptorService.ListDbDescriptors, {
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

DbDescriptorServiceClient.prototype.listDbDescriptorVersions = function listDbDescriptorVersions(requestMessage, metadata, callback) {
  if (arguments.length === 2) {
    callback = arguments[1];
  }
  var client = grpc.unary(DbDescriptorService.ListDbDescriptorVersions, {
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

DbDescriptorServiceClient.prototype.getDbDescriptorVersion = function getDbDescriptorVersion(requestMessage, metadata, callback) {
  if (arguments.length === 2) {
    callback = arguments[1];
  }
  var client = grpc.unary(DbDescriptorService.GetDbDescriptorVersion, {
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

exports.DbDescriptorServiceClient = DbDescriptorServiceClient;

