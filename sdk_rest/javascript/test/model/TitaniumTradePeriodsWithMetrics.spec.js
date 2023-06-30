/**
 * clearconsensus-sdk
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD.
    define(['expect.js', process.cwd()+'/src/index'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    factory(require('expect.js'), require(process.cwd()+'/src/index'));
  } else {
    // Browser globals (root is window)
    factory(root.expect, root.ClearconsensusSdk);
  }
}(this, function(expect, ClearconsensusSdk) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new ClearconsensusSdk.TitaniumTradePeriodsWithMetrics();
  });

  var getProperty = function(object, getter, property) {
    // Use getter method if present; otherwise, get the property directly.
    if (typeof object[getter] === 'function')
      return object[getter]();
    else
      return object[property];
  }

  var setProperty = function(object, setter, property, value) {
    // Use setter method if present; otherwise, set the property directly.
    if (typeof object[setter] === 'function')
      object[setter](value);
    else
      object[property] = value;
  }

  describe('TitaniumTradePeriodsWithMetrics', function() {
    it('should create an instance of TitaniumTradePeriodsWithMetrics', function() {
      // uncomment below and update the code to test TitaniumTradePeriodsWithMetrics
      //var instance = new ClearconsensusSdk.TitaniumTradePeriodsWithMetrics();
      //expect(instance).to.be.a(ClearconsensusSdk.TitaniumTradePeriodsWithMetrics);
    });

    it('should have the property lessDay (base name: "lessDay")', function() {
      // uncomment below and update the code to test the property lessDay
      //var instance = new ClearconsensusSdk.TitaniumTradePeriodsWithMetrics();
      //expect(instance).to.be();
    });

    it('should have the property lessMonth (base name: "lessMonth")', function() {
      // uncomment below and update the code to test the property lessMonth
      //var instance = new ClearconsensusSdk.TitaniumTradePeriodsWithMetrics();
      //expect(instance).to.be();
    });

    it('should have the property lessWeek (base name: "lessWeek")', function() {
      // uncomment below and update the code to test the property lessWeek
      //var instance = new ClearconsensusSdk.TitaniumTradePeriodsWithMetrics();
      //expect(instance).to.be();
    });

  });

}));
