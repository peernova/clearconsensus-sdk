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
 * The TitaniumAllParticipantExplorerTableColumn model module.
 * @module model/TitaniumAllParticipantExplorerTableColumn
 * @version 1.0.0
 */
class TitaniumAllParticipantExplorerTableColumn {
    /**
     * Constructs a new <code>TitaniumAllParticipantExplorerTableColumn</code>.
     * @alias module:model/TitaniumAllParticipantExplorerTableColumn
     */
    constructor() { 
        
        TitaniumAllParticipantExplorerTableColumn.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>TitaniumAllParticipantExplorerTableColumn</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/TitaniumAllParticipantExplorerTableColumn} obj Optional instance to populate.
     * @return {module:model/TitaniumAllParticipantExplorerTableColumn} The populated <code>TitaniumAllParticipantExplorerTableColumn</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new TitaniumAllParticipantExplorerTableColumn();

            if (data.hasOwnProperty('absDiffFromConsensusPrice')) {
                obj['absDiffFromConsensusPrice'] = ApiClient.convertToType(data['absDiffFromConsensusPrice'], Object);
            }
            if (data.hasOwnProperty('conPriceAbsDiffFromLatestTrade')) {
                obj['conPriceAbsDiffFromLatestTrade'] = ApiClient.convertToType(data['conPriceAbsDiffFromLatestTrade'], Object);
            }
            if (data.hasOwnProperty('consensusPrice')) {
                obj['consensusPrice'] = ApiClient.convertToType(data['consensusPrice'], Object);
            }
            if (data.hasOwnProperty('lowerBoundary')) {
                obj['lowerBoundary'] = ApiClient.convertToType(data['lowerBoundary'], Object);
            }
            if (data.hasOwnProperty('participantsCount')) {
                obj['participantsCount'] = ApiClient.convertToType(data['participantsCount'], 'String');
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
 * @member {Object} absDiffFromConsensusPrice
 */
TitaniumAllParticipantExplorerTableColumn.prototype['absDiffFromConsensusPrice'] = undefined;

/**
 * @member {Object} conPriceAbsDiffFromLatestTrade
 */
TitaniumAllParticipantExplorerTableColumn.prototype['conPriceAbsDiffFromLatestTrade'] = undefined;

/**
 * @member {Object} consensusPrice
 */
TitaniumAllParticipantExplorerTableColumn.prototype['consensusPrice'] = undefined;

/**
 * @member {Object} lowerBoundary
 */
TitaniumAllParticipantExplorerTableColumn.prototype['lowerBoundary'] = undefined;

/**
 * @member {String} participantsCount
 */
TitaniumAllParticipantExplorerTableColumn.prototype['participantsCount'] = undefined;

/**
 * @member {Object} stdDev
 */
TitaniumAllParticipantExplorerTableColumn.prototype['stdDev'] = undefined;

/**
 * @member {Object} subPriceDiff
 */
TitaniumAllParticipantExplorerTableColumn.prototype['subPriceDiff'] = undefined;

/**
 * @member {Object} upperBoundary
 */
TitaniumAllParticipantExplorerTableColumn.prototype['upperBoundary'] = undefined;






export default TitaniumAllParticipantExplorerTableColumn;

