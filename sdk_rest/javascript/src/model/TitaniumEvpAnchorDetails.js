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
 * The TitaniumEvpAnchorDetails model module.
 * @module model/TitaniumEvpAnchorDetails
 * @version 1.0.0
 */
class TitaniumEvpAnchorDetails {
    /**
     * Constructs a new <code>TitaniumEvpAnchorDetails</code>.
     * @alias module:model/TitaniumEvpAnchorDetails
     */
    constructor() { 
        
        TitaniumEvpAnchorDetails.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>TitaniumEvpAnchorDetails</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/TitaniumEvpAnchorDetails} obj Optional instance to populate.
     * @return {module:model/TitaniumEvpAnchorDetails} The populated <code>TitaniumEvpAnchorDetails</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new TitaniumEvpAnchorDetails();

            if (data.hasOwnProperty('distanceToConsensus')) {
                obj['distanceToConsensus'] = ApiClient.convertToType(data['distanceToConsensus'], 'Number');
            }
            if (data.hasOwnProperty('mid')) {
                obj['mid'] = ApiClient.convertToType(data['mid'], 'Number');
            }
        }
        return obj;
    }


}

/**
 * @member {Number} distanceToConsensus
 */
TitaniumEvpAnchorDetails.prototype['distanceToConsensus'] = undefined;

/**
 * @member {Number} mid
 */
TitaniumEvpAnchorDetails.prototype['mid'] = undefined;






export default TitaniumEvpAnchorDetails;

