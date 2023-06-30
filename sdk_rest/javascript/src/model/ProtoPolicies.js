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
import ProtoPolicyDto from './ProtoPolicyDto';

/**
 * The ProtoPolicies model module.
 * @module model/ProtoPolicies
 * @version 1.0.0
 */
class ProtoPolicies {
    /**
     * Constructs a new <code>ProtoPolicies</code>.
     * @alias module:model/ProtoPolicies
     */
    constructor() { 
        
        ProtoPolicies.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ProtoPolicies</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ProtoPolicies} obj Optional instance to populate.
     * @return {module:model/ProtoPolicies} The populated <code>ProtoPolicies</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ProtoPolicies();

            if (data.hasOwnProperty('policyDto')) {
                obj['policyDto'] = ApiClient.convertToType(data['policyDto'], [ProtoPolicyDto]);
            }
        }
        return obj;
    }


}

/**
 * @member {Array.<module:model/ProtoPolicyDto>} policyDto
 */
ProtoPolicies.prototype['policyDto'] = undefined;






export default ProtoPolicies;

