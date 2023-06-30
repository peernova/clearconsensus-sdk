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
 * The TitaniumEvpExplorerTableColumn model module.
 * @module model/TitaniumEvpExplorerTableColumn
 * @version 1.0.0
 */
class TitaniumEvpExplorerTableColumn {
    /**
     * Constructs a new <code>TitaniumEvpExplorerTableColumn</code>.
     * @alias module:model/TitaniumEvpExplorerTableColumn
     */
    constructor() { 
        
        TitaniumEvpExplorerTableColumn.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>TitaniumEvpExplorerTableColumn</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/TitaniumEvpExplorerTableColumn} obj Optional instance to populate.
     * @return {module:model/TitaniumEvpExplorerTableColumn} The populated <code>TitaniumEvpExplorerTableColumn</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new TitaniumEvpExplorerTableColumn();

            if (data.hasOwnProperty('absDiffFromEvpMid')) {
                obj['absDiffFromEvpMid'] = ApiClient.convertToType(data['absDiffFromEvpMid'], Object);
            }
            if (data.hasOwnProperty('ask')) {
                obj['ask'] = ApiClient.convertToType(data['ask'], Object);
            }
            if (data.hasOwnProperty('bid')) {
                obj['bid'] = ApiClient.convertToType(data['bid'], Object);
            }
            if (data.hasOwnProperty('evpLowerBoundary')) {
                obj['evpLowerBoundary'] = ApiClient.convertToType(data['evpLowerBoundary'], Object);
            }
            if (data.hasOwnProperty('evpMidAbsDiffFromLatestTrade')) {
                obj['evpMidAbsDiffFromLatestTrade'] = ApiClient.convertToType(data['evpMidAbsDiffFromLatestTrade'], Object);
            }
            if (data.hasOwnProperty('evpUpperBoundary')) {
                obj['evpUpperBoundary'] = ApiClient.convertToType(data['evpUpperBoundary'], Object);
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
TitaniumEvpExplorerTableColumn.prototype['absDiffFromEvpMid'] = undefined;

/**
 * @member {Object} ask
 */
TitaniumEvpExplorerTableColumn.prototype['ask'] = undefined;

/**
 * @member {Object} bid
 */
TitaniumEvpExplorerTableColumn.prototype['bid'] = undefined;

/**
 * @member {Object} evpLowerBoundary
 */
TitaniumEvpExplorerTableColumn.prototype['evpLowerBoundary'] = undefined;

/**
 * @member {Object} evpMidAbsDiffFromLatestTrade
 */
TitaniumEvpExplorerTableColumn.prototype['evpMidAbsDiffFromLatestTrade'] = undefined;

/**
 * @member {Object} evpUpperBoundary
 */
TitaniumEvpExplorerTableColumn.prototype['evpUpperBoundary'] = undefined;

/**
 * @member {Object} mid
 */
TitaniumEvpExplorerTableColumn.prototype['mid'] = undefined;

/**
 * @member {Object} subPriceDiff
 */
TitaniumEvpExplorerTableColumn.prototype['subPriceDiff'] = undefined;

/**
 * @member {Object} tradesOrOrdersCount
 */
TitaniumEvpExplorerTableColumn.prototype['tradesOrOrdersCount'] = undefined;






export default TitaniumEvpExplorerTableColumn;

