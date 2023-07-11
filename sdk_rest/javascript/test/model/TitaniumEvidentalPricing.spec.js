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
    instance = new ClearconsensusSdk.TitaniumEvidentalPricing();
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

  describe('TitaniumEvidentalPricing', function() {
    it('should create an instance of TitaniumEvidentalPricing', function() {
      // uncomment below and update the code to test TitaniumEvidentalPricing
      //var instance = new ClearconsensusSdk.TitaniumEvidentalPricing();
      //expect(instance).to.be.a(ClearconsensusSdk.TitaniumEvidentalPricing);
    });

    it('should have the property absDiffFromEvpMid (base name: "absDiffFromEvpMid")', function() {
      // uncomment below and update the code to test the property absDiffFromEvpMid
      //var instance = new ClearconsensusSdk.TitaniumEvidentalPricing();
      //expect(instance).to.be();
    });

    it('should have the property ask (base name: "ask")', function() {
      // uncomment below and update the code to test the property ask
      //var instance = new ClearconsensusSdk.TitaniumEvidentalPricing();
      //expect(instance).to.be();
    });

    it('should have the property bid (base name: "bid")', function() {
      // uncomment below and update the code to test the property bid
      //var instance = new ClearconsensusSdk.TitaniumEvidentalPricing();
      //expect(instance).to.be();
    });

    it('should have the property evpLowerBoundary (base name: "evpLowerBoundary")', function() {
      // uncomment below and update the code to test the property evpLowerBoundary
      //var instance = new ClearconsensusSdk.TitaniumEvidentalPricing();
      //expect(instance).to.be();
    });

    it('should have the property evpMidAbsDiffFromLatestTrade (base name: "evpMidAbsDiffFromLatestTrade")', function() {
      // uncomment below and update the code to test the property evpMidAbsDiffFromLatestTrade
      //var instance = new ClearconsensusSdk.TitaniumEvidentalPricing();
      //expect(instance).to.be();
    });

    it('should have the property evpUpperBoundary (base name: "evpUpperBoundary")', function() {
      // uncomment below and update the code to test the property evpUpperBoundary
      //var instance = new ClearconsensusSdk.TitaniumEvidentalPricing();
      //expect(instance).to.be();
    });

    it('should have the property mid (base name: "mid")', function() {
      // uncomment below and update the code to test the property mid
      //var instance = new ClearconsensusSdk.TitaniumEvidentalPricing();
      //expect(instance).to.be();
    });

    it('should have the property subPriceDiff (base name: "subPriceDiff")', function() {
      // uncomment below and update the code to test the property subPriceDiff
      //var instance = new ClearconsensusSdk.TitaniumEvidentalPricing();
      //expect(instance).to.be();
    });

    it('should have the property tradesOrOrdersCount (base name: "tradesOrOrdersCount")', function() {
      // uncomment below and update the code to test the property tradesOrOrdersCount
      //var instance = new ClearconsensusSdk.TitaniumEvidentalPricing();
      //expect(instance).to.be();
    });

  });

}));
