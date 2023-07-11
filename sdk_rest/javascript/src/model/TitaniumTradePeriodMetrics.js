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
 * The TitaniumTradePeriodMetrics model module.
 * @module model/TitaniumTradePeriodMetrics
 * @version 1.0.0
 */
class TitaniumTradePeriodMetrics {
    /**
     * Constructs a new <code>TitaniumTradePeriodMetrics</code>.
     * @alias module:model/TitaniumTradePeriodMetrics
     */
    constructor() { 
        
        TitaniumTradePeriodMetrics.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>TitaniumTradePeriodMetrics</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/TitaniumTradePeriodMetrics} obj Optional instance to populate.
     * @return {module:model/TitaniumTradePeriodMetrics} The populated <code>TitaniumTradePeriodMetrics</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new TitaniumTradePeriodMetrics();

            if (data.hasOwnProperty('maxNotionalAmount')) {
                obj['maxNotionalAmount'] = ApiClient.convertToType(data['maxNotionalAmount'], 'Number');
            }
            if (data.hasOwnProperty('minNotionalAmount')) {
                obj['minNotionalAmount'] = ApiClient.convertToType(data['minNotionalAmount'], 'Number');
            }
            if (data.hasOwnProperty('totalLiquidity')) {
                obj['totalLiquidity'] = ApiClient.convertToType(data['totalLiquidity'], 'Number');
            }
            if (data.hasOwnProperty('tradeCount')) {
                obj['tradeCount'] = ApiClient.convertToType(data['tradeCount'], 'String');
            }
        }
        return obj;
    }


}

/**
 * @member {Number} maxNotionalAmount
 */
TitaniumTradePeriodMetrics.prototype['maxNotionalAmount'] = undefined;

/**
 * @member {Number} minNotionalAmount
 */
TitaniumTradePeriodMetrics.prototype['minNotionalAmount'] = undefined;

/**
 * @member {Number} totalLiquidity
 */
TitaniumTradePeriodMetrics.prototype['totalLiquidity'] = undefined;

/**
 * @member {String} tradeCount
 */
TitaniumTradePeriodMetrics.prototype['tradeCount'] = undefined;






export default TitaniumTradePeriodMetrics;

