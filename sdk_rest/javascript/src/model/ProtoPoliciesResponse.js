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
import GrpcprotoError from './GrpcprotoError';
import ProtoPolicies from './ProtoPolicies';

/**
 * The ProtoPoliciesResponse model module.
 * @module model/ProtoPoliciesResponse
 * @version 1.0.0
 */
class ProtoPoliciesResponse {
    /**
     * Constructs a new <code>ProtoPoliciesResponse</code>.
     * @alias module:model/ProtoPoliciesResponse
     */
    constructor() { 
        
        ProtoPoliciesResponse.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ProtoPoliciesResponse</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ProtoPoliciesResponse} obj Optional instance to populate.
     * @return {module:model/ProtoPoliciesResponse} The populated <code>ProtoPoliciesResponse</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ProtoPoliciesResponse();

            if (data.hasOwnProperty('data')) {
                obj['data'] = ProtoPolicies.constructFromObject(data['data']);
            }
            if (data.hasOwnProperty('error')) {
                obj['error'] = GrpcprotoError.constructFromObject(data['error']);
            }
        }
        return obj;
    }


}

/**
 * @member {module:model/ProtoPolicies} data
 */
ProtoPoliciesResponse.prototype['data'] = undefined;

/**
 * @member {module:model/GrpcprotoError} error
 */
ProtoPoliciesResponse.prototype['error'] = undefined;






export default ProtoPoliciesResponse;

