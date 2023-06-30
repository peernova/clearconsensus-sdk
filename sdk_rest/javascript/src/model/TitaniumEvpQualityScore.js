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
import TitaniumDateAndValue from './TitaniumDateAndValue';

/**
 * The TitaniumEvpQualityScore model module.
 * @module model/TitaniumEvpQualityScore
 * @version 1.0.0
 */
class TitaniumEvpQualityScore {
    /**
     * Constructs a new <code>TitaniumEvpQualityScore</code>.
     * @alias module:model/TitaniumEvpQualityScore
     */
    constructor() { 
        
        TitaniumEvpQualityScore.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>TitaniumEvpQualityScore</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/TitaniumEvpQualityScore} obj Optional instance to populate.
     * @return {module:model/TitaniumEvpQualityScore} The populated <code>TitaniumEvpQualityScore</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new TitaniumEvpQualityScore();

            if (data.hasOwnProperty('history')) {
                obj['history'] = ApiClient.convertToType(data['history'], [TitaniumDateAndValue]);
            }
            if (data.hasOwnProperty('indicativeCount')) {
                obj['indicativeCount'] = ApiClient.convertToType(data['indicativeCount'], 'String');
            }
            if (data.hasOwnProperty('orderCount')) {
                obj['orderCount'] = ApiClient.convertToType(data['orderCount'], 'String');
            }
            if (data.hasOwnProperty('score')) {
                obj['score'] = ApiClient.convertToType(data['score'], Object);
            }
            if (data.hasOwnProperty('tradeCount')) {
                obj['tradeCount'] = ApiClient.convertToType(data['tradeCount'], 'String');
            }
        }
        return obj;
    }


}

/**
 * @member {Array.<module:model/TitaniumDateAndValue>} history
 */
TitaniumEvpQualityScore.prototype['history'] = undefined;

/**
 * @member {String} indicativeCount
 */
TitaniumEvpQualityScore.prototype['indicativeCount'] = undefined;

/**
 * @member {String} orderCount
 */
TitaniumEvpQualityScore.prototype['orderCount'] = undefined;

/**
 * @member {Object} score
 */
TitaniumEvpQualityScore.prototype['score'] = undefined;

/**
 * @member {String} tradeCount
 */
TitaniumEvpQualityScore.prototype['tradeCount'] = undefined;






export default TitaniumEvpQualityScore;

