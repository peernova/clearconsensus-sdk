/* eslint-disable */
/*Generated by GenDocu.com*/
// package: titanium
// file: public/consensus_service.proto

var public_consensus_service_pb = require("../public/consensus_service_pb");
var common_gateway_base_pb = require("../common/gateway_base_pb");
var common_consensus_pb = require("../common/consensus_pb");
var grpc = require("@improbable-eng/grpc-web").grpc;

var ConsensusService = (function () {
  function ConsensusService() {}
  ConsensusService.serviceName = "titanium.ConsensusService";
  return ConsensusService;
}());

ConsensusService.ConsensusTimestamps = {
  methodName: "ConsensusTimestamps",
  service: ConsensusService,
  requestStream: false,
  responseStream: false,
  requestType: common_consensus_pb.ConsensusTimestampsRequest,
  responseType: common_consensus_pb.ConsensusTimestampsResponse
};

ConsensusService.Consensus = {
  methodName: "Consensus",
  service: ConsensusService,
  requestStream: false,
  responseStream: false,
  requestType: common_consensus_pb.ConsensusRequest,
  responseType: common_consensus_pb.ConsensusResponse
};

ConsensusService.EvaluatedPrice = {
  methodName: "EvaluatedPrice",
  service: ConsensusService,
  requestStream: false,
  responseStream: false,
  requestType: common_consensus_pb.EVPRequest,
  responseType: common_consensus_pb.EVPResponse
};

ConsensusService.ConsensusOutliers = {
  methodName: "ConsensusOutliers",
  service: ConsensusService,
  requestStream: false,
  responseStream: false,
  requestType: common_gateway_base_pb.OutliersListRequest,
  responseType: common_gateway_base_pb.ConsensusActiveResponse
};

ConsensusService.GetConsensusRuns = {
  methodName: "GetConsensusRuns",
  service: ConsensusService,
  requestStream: false,
  responseStream: false,
  requestType: common_consensus_pb.GetConsensusRunsRequest,
  responseType: common_consensus_pb.GetConsensusRunsResponse
};

ConsensusService.ConsensusResultSetValues = {
  methodName: "ConsensusResultSetValues",
  service: ConsensusService,
  requestStream: false,
  responseStream: false,
  requestType: common_consensus_pb.ConsensusResultSetValuesRequest,
  responseType: common_consensus_pb.ConsensusResultSetValuesResponse
};

ConsensusService.ConsensusExplorerInstrumentDetails = {
  methodName: "ConsensusExplorerInstrumentDetails",
  service: ConsensusService,
  requestStream: false,
  responseStream: false,
  requestType: common_consensus_pb.ConsensusExplorerRequest,
  responseType: common_consensus_pb.ConsensusExplorerInstrumentDetailsResponse
};

ConsensusService.ConsensusExplorerTable = {
  methodName: "ConsensusExplorerTable",
  service: ConsensusService,
  requestStream: false,
  responseStream: false,
  requestType: common_consensus_pb.ConsensusExplorerRequest,
  responseType: common_consensus_pb.ConsensusExplorerTableResponse
};

ConsensusService.ConsensusExplorerRanges = {
  methodName: "ConsensusExplorerRanges",
  service: ConsensusService,
  requestStream: false,
  responseStream: false,
  requestType: common_consensus_pb.ConsensusExplorerRangeRequest,
  responseType: common_consensus_pb.ConsensusExplorerRangeResponse
};

exports.ConsensusService = ConsensusService;

function ConsensusServiceClient(serviceHost, options) {
  this.serviceHost = serviceHost;
  this.options = options || {};
}

ConsensusServiceClient.prototype.consensusTimestamps = function consensusTimestamps(requestMessage, metadata, callback) {
  if (arguments.length === 2) {
    callback = arguments[1];
  }
  var client = grpc.unary(ConsensusService.ConsensusTimestamps, {
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

ConsensusServiceClient.prototype.consensus = function consensus(requestMessage, metadata, callback) {
  if (arguments.length === 2) {
    callback = arguments[1];
  }
  var client = grpc.unary(ConsensusService.Consensus, {
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

ConsensusServiceClient.prototype.evaluatedPrice = function evaluatedPrice(requestMessage, metadata, callback) {
  if (arguments.length === 2) {
    callback = arguments[1];
  }
  var client = grpc.unary(ConsensusService.EvaluatedPrice, {
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

ConsensusServiceClient.prototype.consensusOutliers = function consensusOutliers(requestMessage, metadata, callback) {
  if (arguments.length === 2) {
    callback = arguments[1];
  }
  var client = grpc.unary(ConsensusService.ConsensusOutliers, {
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

ConsensusServiceClient.prototype.getConsensusRuns = function getConsensusRuns(requestMessage, metadata, callback) {
  if (arguments.length === 2) {
    callback = arguments[1];
  }
  var client = grpc.unary(ConsensusService.GetConsensusRuns, {
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

ConsensusServiceClient.prototype.consensusResultSetValues = function consensusResultSetValues(requestMessage, metadata, callback) {
  if (arguments.length === 2) {
    callback = arguments[1];
  }
  var client = grpc.unary(ConsensusService.ConsensusResultSetValues, {
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

ConsensusServiceClient.prototype.consensusExplorerInstrumentDetails = function consensusExplorerInstrumentDetails(requestMessage, metadata, callback) {
  if (arguments.length === 2) {
    callback = arguments[1];
  }
  var client = grpc.unary(ConsensusService.ConsensusExplorerInstrumentDetails, {
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

ConsensusServiceClient.prototype.consensusExplorerTable = function consensusExplorerTable(requestMessage, metadata, callback) {
  if (arguments.length === 2) {
    callback = arguments[1];
  }
  var client = grpc.unary(ConsensusService.ConsensusExplorerTable, {
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

ConsensusServiceClient.prototype.consensusExplorerRanges = function consensusExplorerRanges(requestMessage, metadata, callback) {
  if (arguments.length === 2) {
    callback = arguments[1];
  }
  var client = grpc.unary(ConsensusService.ConsensusExplorerRanges, {
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

exports.ConsensusServiceClient = ConsensusServiceClient;

