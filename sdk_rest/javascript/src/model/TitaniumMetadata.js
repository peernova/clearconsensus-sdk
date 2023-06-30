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
 * The TitaniumMetadata model module.
 * @module model/TitaniumMetadata
 * @version 1.0.0
 */
class TitaniumMetadata {
    /**
     * Constructs a new <code>TitaniumMetadata</code>.
     * @alias module:model/TitaniumMetadata
     */
    constructor() { 
        
        TitaniumMetadata.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>TitaniumMetadata</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/TitaniumMetadata} obj Optional instance to populate.
     * @return {module:model/TitaniumMetadata} The populated <code>TitaniumMetadata</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new TitaniumMetadata();

            if (data.hasOwnProperty('columnNames')) {
                obj['columnNames'] = ApiClient.convertToType(data['columnNames'], ['String']);
            }
        }
        return obj;
    }


}

/**
 * @member {Array.<String>} columnNames
 */
TitaniumMetadata.prototype['columnNames'] = undefined;






export default TitaniumMetadata;

