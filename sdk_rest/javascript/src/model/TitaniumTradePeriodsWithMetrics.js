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
import TitaniumTradePeriodMetrics from './TitaniumTradePeriodMetrics';

/**
 * The TitaniumTradePeriodsWithMetrics model module.
 * @module model/TitaniumTradePeriodsWithMetrics
 * @version 1.0.0
 */
class TitaniumTradePeriodsWithMetrics {
    /**
     * Constructs a new <code>TitaniumTradePeriodsWithMetrics</code>.
     * @alias module:model/TitaniumTradePeriodsWithMetrics
     */
    constructor() { 
        
        TitaniumTradePeriodsWithMetrics.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>TitaniumTradePeriodsWithMetrics</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/TitaniumTradePeriodsWithMetrics} obj Optional instance to populate.
     * @return {module:model/TitaniumTradePeriodsWithMetrics} The populated <code>TitaniumTradePeriodsWithMetrics</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new TitaniumTradePeriodsWithMetrics();

            if (data.hasOwnProperty('lessDay')) {
                obj['lessDay'] = TitaniumTradePeriodMetrics.constructFromObject(data['lessDay']);
            }
            if (data.hasOwnProperty('lessMonth')) {
                obj['lessMonth'] = TitaniumTradePeriodMetrics.constructFromObject(data['lessMonth']);
            }
            if (data.hasOwnProperty('lessWeek')) {
                obj['lessWeek'] = TitaniumTradePeriodMetrics.constructFromObject(data['lessWeek']);
            }
        }
        return obj;
    }


}

/**
 * @member {module:model/TitaniumTradePeriodMetrics} lessDay
 */
TitaniumTradePeriodsWithMetrics.prototype['lessDay'] = undefined;

/**
 * @member {module:model/TitaniumTradePeriodMetrics} lessMonth
 */
TitaniumTradePeriodsWithMetrics.prototype['lessMonth'] = undefined;

/**
 * @member {module:model/TitaniumTradePeriodMetrics} lessWeek
 */
TitaniumTradePeriodsWithMetrics.prototype['lessWeek'] = undefined;






export default TitaniumTradePeriodsWithMetrics;

