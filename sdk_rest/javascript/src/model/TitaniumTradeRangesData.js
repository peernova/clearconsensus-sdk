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
 * The TitaniumTradeRangesData model module.
 * @module model/TitaniumTradeRangesData
 * @version 1.0.0
 */
class TitaniumTradeRangesData {
    /**
     * Constructs a new <code>TitaniumTradeRangesData</code>.
     * @alias module:model/TitaniumTradeRangesData
     */
    constructor() { 
        
        TitaniumTradeRangesData.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>TitaniumTradeRangesData</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/TitaniumTradeRangesData} obj Optional instance to populate.
     * @return {module:model/TitaniumTradeRangesData} The populated <code>TitaniumTradeRangesData</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new TitaniumTradeRangesData();

            if (data.hasOwnProperty('latestTradePrice')) {
                obj['latestTradePrice'] = ApiClient.convertToType(data['latestTradePrice'], 'Number');
            }
            if (data.hasOwnProperty('notional')) {
                obj['notional'] = ApiClient.convertToType(data['notional'], 'Number');
            }
            if (data.hasOwnProperty('pricingRecency')) {
                obj['pricingRecency'] = ApiClient.convertToType(data['pricingRecency'], 'String');
            }
            if (data.hasOwnProperty('tradeExecutionTime')) {
                obj['tradeExecutionTime'] = ApiClient.convertToType(data['tradeExecutionTime'], 'String');
            }
        }
        return obj;
    }


}

/**
 * @member {Number} latestTradePrice
 */
TitaniumTradeRangesData.prototype['latestTradePrice'] = undefined;

/**
 * @member {Number} notional
 */
TitaniumTradeRangesData.prototype['notional'] = undefined;

/**
 * @member {String} pricingRecency
 */
TitaniumTradeRangesData.prototype['pricingRecency'] = undefined;

/**
 * @member {String} tradeExecutionTime
 */
TitaniumTradeRangesData.prototype['tradeExecutionTime'] = undefined;






export default TitaniumTradeRangesData;

