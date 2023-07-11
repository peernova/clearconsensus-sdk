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
import TitaniumFilterPack from './TitaniumFilterPack';

/**
 * The TitaniumGetDataQualityErrorsRequest model module.
 * @module model/TitaniumGetDataQualityErrorsRequest
 * @version 1.0.0
 */
class TitaniumGetDataQualityErrorsRequest {
    /**
     * Constructs a new <code>TitaniumGetDataQualityErrorsRequest</code>.
     * @alias module:model/TitaniumGetDataQualityErrorsRequest
     */
    constructor() { 
        
        TitaniumGetDataQualityErrorsRequest.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>TitaniumGetDataQualityErrorsRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/TitaniumGetDataQualityErrorsRequest} obj Optional instance to populate.
     * @return {module:model/TitaniumGetDataQualityErrorsRequest} The populated <code>TitaniumGetDataQualityErrorsRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new TitaniumGetDataQualityErrorsRequest();

            if (data.hasOwnProperty('assetId')) {
                obj['assetId'] = ApiClient.convertToType(data['assetId'], 'String');
            }
            if (data.hasOwnProperty('groupKeys')) {
                obj['groupKeys'] = TitaniumFilterPack.constructFromObject(data['groupKeys']);
            }
            if (data.hasOwnProperty('submissionId')) {
                obj['submissionId'] = ApiClient.convertToType(data['submissionId'], 'String');
            }
            if (data.hasOwnProperty('submittedDate')) {
                obj['submittedDate'] = ApiClient.convertToType(data['submittedDate'], 'String');
            }
            if (data.hasOwnProperty('traceName')) {
                obj['traceName'] = ApiClient.convertToType(data['traceName'], 'String');
            }
        }
        return obj;
    }


}

/**
 * @member {String} assetId
 */
TitaniumGetDataQualityErrorsRequest.prototype['assetId'] = undefined;

/**
 * @member {module:model/TitaniumFilterPack} groupKeys
 */
TitaniumGetDataQualityErrorsRequest.prototype['groupKeys'] = undefined;

/**
 * @member {String} submissionId
 */
TitaniumGetDataQualityErrorsRequest.prototype['submissionId'] = undefined;

/**
 * @member {String} submittedDate
 */
TitaniumGetDataQualityErrorsRequest.prototype['submittedDate'] = undefined;

/**
 * @member {String} traceName
 */
TitaniumGetDataQualityErrorsRequest.prototype['traceName'] = undefined;






export default TitaniumGetDataQualityErrorsRequest;

