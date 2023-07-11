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
    instance = new ClearconsensusSdk.TitaniumSubmissionEvidenceTableColumn();
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

  describe('TitaniumSubmissionEvidenceTableColumn', function() {
    it('should create an instance of TitaniumSubmissionEvidenceTableColumn', function() {
      // uncomment below and update the code to test TitaniumSubmissionEvidenceTableColumn
      //var instance = new ClearconsensusSdk.TitaniumSubmissionEvidenceTableColumn();
      //expect(instance).to.be.a(ClearconsensusSdk.TitaniumSubmissionEvidenceTableColumn);
    });

    it('should have the property absDiffFromEvidence (base name: "absDiffFromEvidence")', function() {
      // uncomment below and update the code to test the property absDiffFromEvidence
      //var instance = new ClearconsensusSdk.TitaniumSubmissionEvidenceTableColumn();
      //expect(instance).to.be();
    });

    it('should have the property eviPriceAbsDiffFromLatestTrade (base name: "eviPriceAbsDiffFromLatestTrade")', function() {
      // uncomment below and update the code to test the property eviPriceAbsDiffFromLatestTrade
      //var instance = new ClearconsensusSdk.TitaniumSubmissionEvidenceTableColumn();
      //expect(instance).to.be();
    });

    it('should have the property evidence (base name: "evidence")', function() {
      // uncomment below and update the code to test the property evidence
      //var instance = new ClearconsensusSdk.TitaniumSubmissionEvidenceTableColumn();
      //expect(instance).to.be();
    });

    it('should have the property lowerBoundary (base name: "lowerBoundary")', function() {
      // uncomment below and update the code to test the property lowerBoundary
      //var instance = new ClearconsensusSdk.TitaniumSubmissionEvidenceTableColumn();
      //expect(instance).to.be();
    });

    it('should have the property participantsCount (base name: "participantsCount")', function() {
      // uncomment below and update the code to test the property participantsCount
      //var instance = new ClearconsensusSdk.TitaniumSubmissionEvidenceTableColumn();
      //expect(instance).to.be();
    });

    it('should have the property stdDev (base name: "stdDev")', function() {
      // uncomment below and update the code to test the property stdDev
      //var instance = new ClearconsensusSdk.TitaniumSubmissionEvidenceTableColumn();
      //expect(instance).to.be();
    });

    it('should have the property subPriceDiff (base name: "subPriceDiff")', function() {
      // uncomment below and update the code to test the property subPriceDiff
      //var instance = new ClearconsensusSdk.TitaniumSubmissionEvidenceTableColumn();
      //expect(instance).to.be();
    });

    it('should have the property upperBoundary (base name: "upperBoundary")', function() {
      // uncomment below and update the code to test the property upperBoundary
      //var instance = new ClearconsensusSdk.TitaniumSubmissionEvidenceTableColumn();
      //expect(instance).to.be();
    });

  });

}));
