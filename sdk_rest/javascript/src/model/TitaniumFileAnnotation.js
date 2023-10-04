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
import TitaniumAssetDetails from './TitaniumAssetDetails';
import TitaniumChunk from './TitaniumChunk';

/**
 * The TitaniumFileAnnotation model module.
 * @module model/TitaniumFileAnnotation
 * @version 1.0.0
 */
class TitaniumFileAnnotation {
    /**
     * Constructs a new <code>TitaniumFileAnnotation</code>.
     * @alias module:model/TitaniumFileAnnotation
     */
    constructor() { 
        
        TitaniumFileAnnotation.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>TitaniumFileAnnotation</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/TitaniumFileAnnotation} obj Optional instance to populate.
     * @return {module:model/TitaniumFileAnnotation} The populated <code>TitaniumFileAnnotation</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new TitaniumFileAnnotation();

            if (data.hasOwnProperty('annotation')) {
                obj['annotation'] = ApiClient.convertToType(data['annotation'], Object);
            }
            if (data.hasOwnProperty('asset')) {
                obj['asset'] = TitaniumAssetDetails.constructFromObject(data['asset']);
            }
            if (data.hasOwnProperty('chunks')) {
                obj['chunks'] = ApiClient.convertToType(data['chunks'], [TitaniumChunk]);
            }
            if (data.hasOwnProperty('client')) {
                obj['client'] = ApiClient.convertToType(data['client'], 'String');
            }
            if (data.hasOwnProperty('fileName')) {
                obj['fileName'] = ApiClient.convertToType(data['fileName'], 'String');
            }
            if (data.hasOwnProperty('mode')) {
                obj['mode'] = ApiClient.convertToType(data['mode'], 'String');
            }
            if (data.hasOwnProperty('uploadTime')) {
                obj['uploadTime'] = ApiClient.convertToType(data['uploadTime'], 'String');
            }
        }
        return obj;
    }


}

/**
 * @member {Object} annotation
 */
TitaniumFileAnnotation.prototype['annotation'] = undefined;

/**
 * @member {module:model/TitaniumAssetDetails} asset
 */
TitaniumFileAnnotation.prototype['asset'] = undefined;

/**
 * @member {Array.<module:model/TitaniumChunk>} chunks
 */
TitaniumFileAnnotation.prototype['chunks'] = undefined;

/**
 * @member {String} client
 */
TitaniumFileAnnotation.prototype['client'] = undefined;

/**
 * @member {String} fileName
 */
TitaniumFileAnnotation.prototype['fileName'] = undefined;

/**
 * @member {String} mode
 */
TitaniumFileAnnotation.prototype['mode'] = undefined;

/**
 * @member {String} uploadTime
 */
TitaniumFileAnnotation.prototype['uploadTime'] = undefined;






export default TitaniumFileAnnotation;

