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

import ApiClient from '../ApiClient';

/**
 * The TitaniumCohortConsensusColumn model module.
 * @module model/TitaniumCohortConsensusColumn
 * @version 1.0.0
 */
class TitaniumCohortConsensusColumn {
    /**
     * Constructs a new <code>TitaniumCohortConsensusColumn</code>.
     * @alias module:model/TitaniumCohortConsensusColumn
     */
    constructor() { 
        
        TitaniumCohortConsensusColumn.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>TitaniumCohortConsensusColumn</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/TitaniumCohortConsensusColumn} obj Optional instance to populate.
     * @return {module:model/TitaniumCohortConsensusColumn} The populated <code>TitaniumCohortConsensusColumn</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new TitaniumCohortConsensusColumn();

            if (data.hasOwnProperty('absDiffFromConsensus')) {
                obj['absDiffFromConsensus'] = ApiClient.convertToType(data['absDiffFromConsensus'], Object);
            }
            if (data.hasOwnProperty('cohortConsensusPrice')) {
                obj['cohortConsensusPrice'] = ApiClient.convertToType(data['cohortConsensusPrice'], Object);
            }
            if (data.hasOwnProperty('consAbsDiffFromAnchorEvpMid')) {
                obj['consAbsDiffFromAnchorEvpMid'] = ApiClient.convertToType(data['consAbsDiffFromAnchorEvpMid'], Object);
            }
            if (data.hasOwnProperty('consAbsDiffFromAnchorEvpMidCalc')) {
                obj['consAbsDiffFromAnchorEvpMidCalc'] = ApiClient.convertToType(data['consAbsDiffFromAnchorEvpMidCalc'], Object);
            }
            if (data.hasOwnProperty('consAbsDiffFromAnchorSub')) {
                obj['consAbsDiffFromAnchorSub'] = ApiClient.convertToType(data['consAbsDiffFromAnchorSub'], Object);
            }
            if (data.hasOwnProperty('consAbsDiffFromAnchorTrade')) {
                obj['consAbsDiffFromAnchorTrade'] = ApiClient.convertToType(data['consAbsDiffFromAnchorTrade'], Object);
            }
            if (data.hasOwnProperty('lowerBoundary')) {
                obj['lowerBoundary'] = ApiClient.convertToType(data['lowerBoundary'], Object);
            }
            if (data.hasOwnProperty('numberOfInstruments')) {
                obj['numberOfInstruments'] = ApiClient.convertToType(data['numberOfInstruments'], 'String');
            }
            if (data.hasOwnProperty('stdDev')) {
                obj['stdDev'] = ApiClient.convertToType(data['stdDev'], Object);
            }
            if (data.hasOwnProperty('subPriceDiff')) {
                obj['subPriceDiff'] = ApiClient.convertToType(data['subPriceDiff'], Object);
            }
            if (data.hasOwnProperty('upperBoundary')) {
                obj['upperBoundary'] = ApiClient.convertToType(data['upperBoundary'], Object);
            }
        }
        return obj;
    }


}

/**
 * @member {Object} absDiffFromConsensus
 */
TitaniumCohortConsensusColumn.prototype['absDiffFromConsensus'] = undefined;

/**
 * @member {Object} cohortConsensusPrice
 */
TitaniumCohortConsensusColumn.prototype['cohortConsensusPrice'] = undefined;

/**
 * @member {Object} consAbsDiffFromAnchorEvpMid
 */
TitaniumCohortConsensusColumn.prototype['consAbsDiffFromAnchorEvpMid'] = undefined;

/**
 * @member {Object} consAbsDiffFromAnchorEvpMidCalc
 */
TitaniumCohortConsensusColumn.prototype['consAbsDiffFromAnchorEvpMidCalc'] = undefined;

/**
 * @member {Object} consAbsDiffFromAnchorSub
 */
TitaniumCohortConsensusColumn.prototype['consAbsDiffFromAnchorSub'] = undefined;

/**
 * @member {Object} consAbsDiffFromAnchorTrade
 */
TitaniumCohortConsensusColumn.prototype['consAbsDiffFromAnchorTrade'] = undefined;

/**
 * @member {Object} lowerBoundary
 */
TitaniumCohortConsensusColumn.prototype['lowerBoundary'] = undefined;

/**
 * @member {String} numberOfInstruments
 */
TitaniumCohortConsensusColumn.prototype['numberOfInstruments'] = undefined;

/**
 * @member {Object} stdDev
 */
TitaniumCohortConsensusColumn.prototype['stdDev'] = undefined;

/**
 * @member {Object} subPriceDiff
 */
TitaniumCohortConsensusColumn.prototype['subPriceDiff'] = undefined;

/**
 * @member {Object} upperBoundary
 */
TitaniumCohortConsensusColumn.prototype['upperBoundary'] = undefined;






export default TitaniumCohortConsensusColumn;

