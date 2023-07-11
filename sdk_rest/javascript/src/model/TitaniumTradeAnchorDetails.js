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
 * The TitaniumTradeAnchorDetails model module.
 * @module model/TitaniumTradeAnchorDetails
 * @version 1.0.0
 */
class TitaniumTradeAnchorDetails {
    /**
     * Constructs a new <code>TitaniumTradeAnchorDetails</code>.
     * @alias module:model/TitaniumTradeAnchorDetails
     */
    constructor() { 
        
        TitaniumTradeAnchorDetails.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>TitaniumTradeAnchorDetails</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/TitaniumTradeAnchorDetails} obj Optional instance to populate.
     * @return {module:model/TitaniumTradeAnchorDetails} The populated <code>TitaniumTradeAnchorDetails</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new TitaniumTradeAnchorDetails();

            if (data.hasOwnProperty('distanceToConsensus')) {
                obj['distanceToConsensus'] = ApiClient.convertToType(data['distanceToConsensus'], 'Number');
            }
            if (data.hasOwnProperty('latestTradePrice')) {
                obj['latestTradePrice'] = ApiClient.convertToType(data['latestTradePrice'], 'Number');
            }
            if (data.hasOwnProperty('notional')) {
                obj['notional'] = ApiClient.convertToType(data['notional'], 'Number');
            }
            if (data.hasOwnProperty('pricingAge')) {
                obj['pricingAge'] = ApiClient.convertToType(data['pricingAge'], 'String');
            }
            if (data.hasOwnProperty('source')) {
                obj['source'] = ApiClient.convertToType(data['source'], 'String');
            }
            if (data.hasOwnProperty('tradeExecutionTime')) {
                obj['tradeExecutionTime'] = ApiClient.convertToType(data['tradeExecutionTime'], 'String');
            }
        }
        return obj;
    }


}

/**
 * @member {Number} distanceToConsensus
 */
TitaniumTradeAnchorDetails.prototype['distanceToConsensus'] = undefined;

/**
 * @member {Number} latestTradePrice
 */
TitaniumTradeAnchorDetails.prototype['latestTradePrice'] = undefined;

/**
 * @member {Number} notional
 */
TitaniumTradeAnchorDetails.prototype['notional'] = undefined;

/**
 * @member {String} pricingAge
 */
TitaniumTradeAnchorDetails.prototype['pricingAge'] = undefined;

/**
 * @member {String} source
 */
TitaniumTradeAnchorDetails.prototype['source'] = undefined;

/**
 * @member {String} tradeExecutionTime
 */
TitaniumTradeAnchorDetails.prototype['tradeExecutionTime'] = undefined;






export default TitaniumTradeAnchorDetails;

