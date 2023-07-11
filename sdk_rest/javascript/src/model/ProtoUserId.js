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
 * The ProtoUserId model module.
 * @module model/ProtoUserId
 * @version 1.0.0
 */
class ProtoUserId {
    /**
     * Constructs a new <code>ProtoUserId</code>.
     * @alias module:model/ProtoUserId
     */
    constructor() { 
        
        ProtoUserId.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ProtoUserId</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ProtoUserId} obj Optional instance to populate.
     * @return {module:model/ProtoUserId} The populated <code>ProtoUserId</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ProtoUserId();

            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
        }
        return obj;
    }


}

/**
 * @member {String} id
 */
ProtoUserId.prototype['id'] = undefined;






export default ProtoUserId;

