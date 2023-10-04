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
 * The TitaniumEvidentalPricing model module.
 * @module model/TitaniumEvidentalPricing
 * @version 1.0.0
 */
class TitaniumEvidentalPricing {
    /**
     * Constructs a new <code>TitaniumEvidentalPricing</code>.
     * @alias module:model/TitaniumEvidentalPricing
     */
    constructor() { 
        
        TitaniumEvidentalPricing.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>TitaniumEvidentalPricing</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/TitaniumEvidentalPricing} obj Optional instance to populate.
     * @return {module:model/TitaniumEvidentalPricing} The populated <code>TitaniumEvidentalPricing</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new TitaniumEvidentalPricing();

            if (data.hasOwnProperty('absDiffFromEvpMid')) {
                obj['absDiffFromEvpMid'] = ApiClient.convertToType(data['absDiffFromEvpMid'], Object);
            }
            if (data.hasOwnProperty('ask')) {
                obj['ask'] = ApiClient.convertToType(data['ask'], Object);
            }
            if (data.hasOwnProperty('bid')) {
                obj['bid'] = ApiClient.convertToType(data['bid'], Object);
            }
            if (data.hasOwnProperty('evpMidAbsDiffFromLatestTrade')) {
                obj['evpMidAbsDiffFromLatestTrade'] = ApiClient.convertToType(data['evpMidAbsDiffFromLatestTrade'], Object);
            }
            if (data.hasOwnProperty('mid')) {
                obj['mid'] = ApiClient.convertToType(data['mid'], Object);
            }
            if (data.hasOwnProperty('subPriceDiff')) {
                obj['subPriceDiff'] = ApiClient.convertToType(data['subPriceDiff'], Object);
            }
            if (data.hasOwnProperty('tradesOrOrdersCount')) {
                obj['tradesOrOrdersCount'] = ApiClient.convertToType(data['tradesOrOrdersCount'], Object);
            }
        }
        return obj;
    }


}

/**
 * @member {Object} absDiffFromEvpMid
 */
TitaniumEvidentalPricing.prototype['absDiffFromEvpMid'] = undefined;

/**
 * @member {Object} ask
 */
TitaniumEvidentalPricing.prototype['ask'] = undefined;

/**
 * @member {Object} bid
 */
TitaniumEvidentalPricing.prototype['bid'] = undefined;

/**
 * @member {Object} evpMidAbsDiffFromLatestTrade
 */
TitaniumEvidentalPricing.prototype['evpMidAbsDiffFromLatestTrade'] = undefined;

/**
 * @member {Object} mid
 */
TitaniumEvidentalPricing.prototype['mid'] = undefined;

/**
 * @member {Object} subPriceDiff
 */
TitaniumEvidentalPricing.prototype['subPriceDiff'] = undefined;

/**
 * @member {Object} tradesOrOrdersCount
 */
TitaniumEvidentalPricing.prototype['tradesOrOrdersCount'] = undefined;






export default TitaniumEvidentalPricing;

